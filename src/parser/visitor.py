from database import *
from SQLoperation import *
from exceptions import *
from condition import *
from antlr4 import *
from .miniSQLParser import miniSQLParser
from functools import reduce

class Visitor(ParseTreeVisitor):

    def __init__(self):
        ParseTreeVisitor.__init__(self)

        self.relationNames = dict() # alias -> real name
        self.attributeNames = dict() # alias -> Attribute(table,name)
        self.allAttr = False

        self.dataManager = DataManager() # will handle relation loading

        self.notInCond = []

    def visitMain(self, ctx:miniSQLParser.MainContext):
        print_debug("visitMain")
        resultRelation = self.visit(ctx.sql())
        self.dataManager.discard()
        return resultRelation

    # ________________________ sql rules _______________________________________
    def visitSqlNormal(self, ctx:miniSQLParser.SqlNormalContext):
        # SELECT (DISTINCT)? atts FROM rels (WHERE cond)? (GROUPBY att)? orderby?
        print_debug("visitSqlNormal")

        # 1/ Get the tables in main query
        relations = self.visit(ctx.rels())

        # 2/ Get eventual tables from subqueries
        if ctx.cond() is not None:
            _,relList,_ = self.visit(ctx.cond())
            relations += relList

        # 3/ Load all the tables
        for i,(fileName,tableName) in enumerate(relations) :
            self.dataManager.load(fileName)
            self.relationNames[tableName]=fileName
            if fileName!=tableName :
                self.dataManager.rename_table(fileName,tableName)
            relations[i]=tableName # get rid of fileName : not useful from now
        print_debug(" Relations :" + str(self.relationNames))

        # 4/ Perform a join on the tables
        if len(relations)==1:
            resultRelation = self.dataManager[relations[0]]
        else:
            resultRelation = reduce(lambda x,y : join(x, y), self.dataManager.get_tables(relations))

        # 5/ Getting attributes
        attributes, aggregations = self.visit(ctx.atts())
        print_debug(aggregations)
        print_debug(" Attributes :", attributes)

        # 6/ 2nd pass over conditions to get condition tree
        if ctx.cond() is not None:
            condTree,_,notIn = self.visit(ctx.cond())
            if notIn:
                print_debug("___ NOT INT SUBQUERY ___")
                resultRelation = minus()
            else:
                resultRelation = select(resultRelation, Or(condTree))
            print_debug(" Conditions : " + str(condTree))

        # 7/ Group By
        if ctx.GROUPBY() is not None:
            grpAttr = self.visit(ctx.att())
            resultRelation = groupBy(resultRelation, grpAttr, aggregation)

        # 8/ Sorting of output
        if ctx.orderby() is not None :
            orderkeys,desc = self.visit(ctx.orderby())
            print_debug("Order keys : ", orderkeys)
            resultRelation = orderBy(resultRelation, orderkeys, desc=desc)

        # 9/ Perform final projection if not a 'SELECT *'
        if not self.allAttr:
            resultRelation = project(resultRelation, attributes)

        # 10/ Delete duplicates
        if ctx.DISTINCT() is not None :
            print_debug("Select Distinct")
            resultRelation = project_distinct(resultRelation)

        return resultRelation


    def visitSqlMinus(self, ctx:miniSQLParser.SqlMinusContext):
        # LPAR sql RPAR MINUS LPAR sql RPAR
        print_debug("visitSqlMinus")
        rel1 = self.visit(ctx.sql(0))
        rel2 = self.visit(ctx.sql(1))
        return minus(rel1,rel2)

    def visitSqlUnion(self, ctx:miniSQLParser.SqlUnionContext):
        # LPAR sql RPAR UNION LPAR sql RPAR
        print_debug("visitSqlUnion")
        rel1 = self.visit(ctx.sql(0))
        rel2 = self.visit(ctx.sql(1))
        return union(rel1,rel2)

    # _________________________ subsql rules ___________________________________
    def visitSubSql(self, ctx, attr):
        """
        Called when visiting a sub query
        """
        print_debug("visitSubSql")
        clue = ctx.getChild(3).getText()
        if clue == 'MINUS':
            return self.visitSubSqlMinus(ctx,attr)
        elif clue == 'UNION':
            return self.visitSubSqlUnion(ctx,attr)
        else:
            return self.visitSubSqlNormal(ctx,attr)

    def visitSubSqlNormal(self, ctx, attr):
        print_debug("visitSubSqlNormal")
        attributes = self.visit(ctx.atts())
        assert(len(attributes)==1) # There should be only one here
        subAttr = attributes[0]
        relations = self.visit(ctx.rels())
        condTree, rels = self.visit(ctx.cond()) # condTree a list of list : CDF form
        return [Or(condTree),Condition(attr,Op.EQ,subAttr)], relations+rels

    def visitSubSqlMinus(self, ctx, attr): # TODO : false version
        print_debug("visitSubSqlUnion")
        condTree1, rels1 = self.visitSubSql(ctx.sql(0), attr)
        condTree2, rels2 = self.visitSubSql(ctx.sql(1), attr)
        return [Or([And(condTree1),And(condTree2)])], rels1+rels2

    def visitSubSqlUnion(self, ctx, attr):
        print_debug("visitSubSqlUnion")
        condTree1, rels1 = self.visitSubSql(ctx.sql(0), attr)
        condTree2, rels2 = self.visitSubSql(ctx.sql(1), attr)
        return [Or([And(condTree1),And(condTree2)])], rels1+rels2

    # _________________________ Order By rules _____________________________________

    def visitOrderBy(self, ctx:miniSQLParser.OrderByContext):
        # ORDERBY atts (DESC|ASC)?
        orderkeys = self.visit(ctx.atts())
        desc = ctx.DESC() is not None
        return orderkeys,desc

    # _________________________ atts rules _____________________________________
    def visitAttributeDeclAll(self, ctx:miniSQLParser.AttributeDeclAllContext):
        # SELECT *
        print_debug("visitAttributeDeclAll")
        self.allAttr = True
        return [], []

    def visitAttributeDeclList(self, ctx:miniSQLParser.AttributeDeclListContext):
        print_debug("visitAttributeDeclList")
        queueOfAttrList, queueOfAggrList = self.visit(ctx.atts())
        firstAttrElem, firstAggrElem = self.visit(ctx.attd())
        return [firstAttrElem]+queueOfAttrList, [firstAggrElem]+queueOfAggrList,

    def visitAttributeDeclSimple(self, ctx:miniSQLParser.AttributeDeclSimpleContext):
        print_debug("visitAttributeDeclSimple")
        attr, aggr = self.visitChildren(ctx)
        return [attr], [aggr]

    # ___________________ attd rules ___________________________________________
    def visitAttributeSimple(self, ctx:miniSQLParser.AttributeSimpleContext):
        print_debug("visitAttributeSimple")
        attr = self.visit(ctx.att())
        self.attributeNames[attr.fullName] = attr
        return attr, Aggregation.GROUPBY

    def visitAttributeAs(self, ctx:miniSQLParser.AttributeAsContext):
        print_debug("visitAttributeAs")
        attr = self.visit(ctx.att())
        alias = ctx.ID().getText()
        self.attributeNames[alias] = attr
        return attr, Aggregation.GROUPBY

    def visitAttributeAggr(self, ctx:miniSQLParser.AttributeAggrContext):
        print_debug("visitAttributeAggr")
        attr = self.visit(ctx.att())
        self.attributeNames[attr.fullName] = attr
        aggr = ctx.aggr().getText()
        if aggr == "MAX":
            aggr = Aggregation.MAX
        elif aggr == "MIN":
            aggr = Aggregation.MIN
        elif aggr == "COUNT":
            aggr = Aggregation.COUNT
        elif aggr == "SUM":
            aggr = Aggregation.SUM
        return attr, aggr

    # __________________ att rule ______________________________________________
    def visitAtt(self, ctx:miniSQLParser.AttContext):
        print_debug("visitAtt")
        tableName = ctx.ID(0).getText()
        attrName = ctx.ID(1).getText()
        return Attribute(tableName,attrName)

    # __________________ rels rules ____________________________________________
    def visitRelationDeclList(self, ctx:miniSQLParser.RelationDeclListContext):
        print_debug("visitRelationDeclList")
        queueRel = self.visit(ctx.rels())
        firstRel = self.visit(ctx.rel())
        return [firstRel]+queueRel

    def visitRelationDeclSimple(self, ctx:miniSQLParser.RelationDeclSimpleContext):
        print_debug("visitRelationDeclSimple")
        return [self.visit(ctx.rel())]

    # __________________ rel rules _____________________________________________
    def visitRelationID(self, ctx:miniSQLParser.RelationIDContext):
        print_debug("visitRelationID")
        fileName = ctx.FILENAME().getText()
        tableName = ctx.ID().getText()
        return (fileName,tableName)

    def visitRelationSubQuery(self, ctx:miniSQLParser.RelationSubQueryContext):
        # When a table in the FROM is a subquery
        print_debug("visitRelationSubQuery")
        tableName = ctx.ID().getText()

        mem = self.allAttr
        self.allAttr = False
        rel = self.visit(ctx.sql())
        self.allAttr = mem

        self.relationNames[tableName]=tableName
        rel.rename(tableName)
        self.dataManager.add_table(rel)

        return (tableName,tableName)

    # _____________________ cond rules _________________________________________
    def visitCondOrList(self, ctx:miniSQLParser.CondOrListContext):
        print_debug("visitCondOrList")
        queueCond, listRel1, notIn1 = self.visit(ctx.cond())
        firstCond, listRel2, notIn2 = self.visit(ctx.and_cond())
        return [And(firstCond)]+queueCond, listRel1+listRel2, (notIn1 or notIn2)

    def visitCondOrSimple(self, ctx:miniSQLParser.CondOrSimpleContext):
        print_debug("visitCondOrSimple")
        cond , listRel, notIn = self.visit(ctx.and_cond())
        return [And(cond)], listRel, notIn

    # ____________________ and_cond rules ______________________________________
    def visitCondAndOr(self, ctx:miniSQLParser.CondAndOrContext):
        print_debug("visitCondAndOr")
        queueCond, listRel1, notIn1 = self.visit(ctx.and_cond())
        firstCond, listRel2, notIn2 = self.visit(ctx.cond())
        return [Or(firstCond)]+queueCond, listRel1+listRel2, (notIn1 or notIn2)

    def visitCondAndList(self, ctx:miniSQLParser.CondAndListContext):
        print_debug("visitCondAndList")
        queueCond, listRel1, notIn1 = self.visit(ctx.and_cond())
        firstCond, listRel2, notIn2 = self.visit(ctx.at_cond())
        return firstCond+queueCond, listRel1+listRel2, notIn1 or notIn2

    def visitCondAndSimple(self, ctx:miniSQLParser.CondAndSimpleContext):
        print_debug("visitCondAndSimple")
        cond, rel, notIn = self.visit(ctx.at_cond())
        return (cond, rel, notIn)

    # ____________________ at_cond rules _______________________________________
    def visitCompSimple(self, ctx:miniSQLParser.CompSimpleContext):
        print_debug("visitCompSimple")
        op = ctx.op().getText()
        if op == "=":
            op = Op.EQ
        elif op == "!=":
            op = Op.NEQ
        elif op == "<=":
            op = Op.LE
        elif op == "<":
            op = Op.LT
        elif op == ">=":
            op = Op.GE
        elif op == ">":
            op = Op.GT
        attr1,attr2 = self.visit(ctx.att(0)), self.visit(ctx.att(1))
        return [Condition(attr1,op,attr2)], [], False

    def visitCompIn(self, ctx:miniSQLParser.CompInContext):
        print_debug("visitCompIn")
        attr = self.visit(ctx.att())
        cond, rel = self.visitSubSql(ctx.sql(), attr)
        return cond, rel, False

    def visitCompNotIn(self, ctx:miniSQLParser.CompNotInContext):
        print_debug("visitCompNotIn")
        attr = self.visit(ctx.att())
        cond,rel = self.visitSubSql(ctx.sql(), attr)
        self.notInCond = toCNF(cond)
        return [], rel, True

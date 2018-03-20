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
        self.relationAliases = dict() # real name -> alias
        self.attributeNames = dict() # alias -> Attribute(table,name)
        self.allAttr = False

        self.dataManager = DataManager() # will handle relation loading

    def visitMain(self, ctx:miniSQLParser.MainContext):
        print_debug("visitMain")
        resultRelation = self.visit(ctx.sql())
        self.dataManager.discard()
        return resultRelation

    # ________________________ sql rules _______________________________________
    def visitSqlNormal(self, ctx:miniSQLParser.SqlNormalContext):
        print_debug("visitSqlNormal")

        relations = self.visit(ctx.rels()) # Load the tables & builds self.relationNames
        if ctx.cond() is not None:
            condList,relList = self.visit(ctx.cond())   # A list of list : CDF form
                                                        # Second return value is the list of the relations into IN subqueries
            relations += relList

        for i,(fileName,tableName) in enumerate(relations) :
            self.dataManager.load(fileName)
            self.relationNames[tableName]=fileName
            if fileName!=tableName :
                self.dataManager.rename_table(fileName,tableName)
            relations[i]=tableName # get rid of fileName
        print_debug(" Relations :" + str(self.relationNames))

        # perform a join on the tables
        if len(relations)==1:
            resultRelation = self.dataManager[relations[0]]
        else:
            resultRelation = reduce(lambda x,y : join(x, y), self.dataManager.get_tables(relations))

        attributes = self.visit(ctx.atts())
        print_debug(" Attributes :", attributes)

        if ctx.cond() is not None:
            condList,relList = self.visit(ctx.cond())   # A list of list : CDF form
                                                        # Second return value is the list of the relations into IN subqueries
            print_debug(" Conditions : " + str(condList))
            print_debug(" Perform select in main query")
            resultRelation = select(resultRelation, Or(condList))
            print_debug(" End select")

        if not self.allAttr: # No * request -> perform a projection
            print_debug(" Perform project in main query")
            resultRelation = project(resultRelation, attributes)
            print_debug(" End project")

        return resultRelation

    def visitSqlSub(self, ctx):
        print_debug("visitSqlSub")
        attributes = self.visit(ctx.atts())
        assert(len(attributes)==1) # There should be only one here
        subAttr = attributes[0]
        relations = self.visit(ctx.rels())
        condList, rels = self.visit(ctx.cond()) # condList a list of list : CDF form
        return subAttr,relations+rels,condList


    # Visit a parse tree produced by miniSQLParser#sqlMinus.
    def visitSqlMinus(self, ctx:miniSQLParser.SqlMinusContext):
        print_debug("visitSqlMinus")
        rel1 = self.visit(ctx.sql(0))
        rel2 = self.visit(ctx.sql(1))
        return minus(rel1,rel2)

    # Visit a parse tree produced by miniSQLParser#sqlUnion.
    def visitSqlUnion(self, ctx:miniSQLParser.SqlUnionContext):
        print_debug("visitSqlUnion")
        rel1 = self.visit(ctx.sql(0))
        rel2 = self.visit(ctx.sql(1))
        return union(rel1,rel2)


    # _________________________ atts rules _____________________________________
    def visitAttributeDeclAll(self, ctx:miniSQLParser.AttributeDeclAllContext):
        # SELECT *
        print_debug("visitAttributeDeclAll")
        self.allAttr = True
        return []

    def visitAttributeDeclList(self, ctx:miniSQLParser.AttributeDeclListContext):
        print_debug("visitAttributeDeclList")
        queueOfList = self.visit(ctx.atts())
        firstElem = self.visit(ctx.attd())
        return [firstElem]+queueOfList

    def visitAttributeDeclSimple(self, ctx:miniSQLParser.AttributeDeclSimpleContext):
        print_debug("visitAttributeDeclSimple")
        return [self.visitChildren(ctx)]

    # ___________________ attd rules ___________________________________________
    def visitAttributeSimple(self, ctx:miniSQLParser.AttributeSimpleContext):
        print_debug("visitAttributeSimple")
        attr = self.visit(ctx.att())
        self.attributeNames[attr.fullName] = attr
        return attr

    def visitAttributeAs(self, ctx:miniSQLParser.AttributeAsContext):
        print_debug("visitAttributeAs")
        attr = self.visit(ctx.att())
        alias = ctx.ID().getText()
        self.attributeNames[alias] = attr
        return attr

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

    def visitSubquery(self, ctx:miniSQLParser.SubqueryContext):
        # When a table in the FROM is a subquery
        print_debug("visitSubquery")
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
        queueCond, listRel1 = self.visit(ctx.cond())
        firstCond, listRel2 = self.visit(ctx.and_cond())
        return [And(firstCond)]+queueCond, listRel1+listRel2

    def visitCondOrSimple(self, ctx:miniSQLParser.CondOrSimpleContext):
        print_debug("visitCondOrSimple")
        cond , listRel = self.visit(ctx.and_cond())
        return ([And(cond)], listRel)

    # ____________________ and_cond rules ______________________________________
    def visitCondAndOr(self, ctx:miniSQLParser.CondAndOrContext):
        print_debug("visitCondAndOr")
        queueCond, listRel1 = self.visit(ctx.and_cond())
        firstCond, listRel2 = self.visit(ctx.cond())
        return [Or(firstCond)]+queueCond, listRel1+listRel2

    def visitCondAndList(self, ctx:miniSQLParser.CondAndListContext):
        print_debug("visitCondAndList")
        queueCond, listRel1 = self.visit(ctx.and_cond())
        firstCond, listRel2 = self.visit(ctx.at_cond())
        return firstCond+queueCond, listRel1+listRel2

    def visitCondAndSimple(self, ctx:miniSQLParser.CondAndSimpleContext):
        print_debug("visitCondAndSimple")
        cond,rel = self.visit(ctx.at_cond())
        return (cond,rel)

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
        return [Condition(attr1,op,attr2)], []

    def visitCompIn(self, ctx:miniSQLParser.CompInContext):
        print_debug("visitCompIn")
        attr = self.visit(ctx.att())
        subAttr,rels,cond = self.visitSqlSub(ctx.sql())
        return cond+[Condition(attr,Op.EQ,subAttr)], rels

    def visitCompNotIn(self, ctx:miniSQLParser.CompNotInContext):
        print_debug("visitCompNotIn")
        attr = self.visit(ctx.att())
        table = self.dataManager[attr.table]
        rel = self.visitSqlSub(ctx.sql(), table, attr)
        rel.rename(attr.table)
        return NotInCondition(attr,rel), set(rel.name)

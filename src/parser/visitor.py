# Generated from src/parser/miniSQL.g4 by ANTLR 4.7
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

        self.visit(ctx.rels()) # Load the tables. Builds self.relationNames
        print_debug("Relations :" + str(self.relationNames))

        # perform a rename on all tables
        for (alias,name) in self.relationNames.items():
            self.dataManager.rename_table(name,alias)

        # perform a join on the tables
        resultRelation = reduce(lambda x,y : join(self.dataManager[x], self.dataManager[y]),
                                list(self.relationNames.keys()))

        attributes = self.visit(ctx.atts())
        print_debug("Attributes :" + str(attributes))

        if ctx.cond() is not None:
            condList = self.visit(ctx.cond()) # a list of list : CDF form
            print_debug("Conditions : " + str(condList))
            resultRelation = select(resultRelation, condList)

        if not self.allAttr: # No * request -> perform a projection
            resultRelation = project(resultRelation, attributes)

        return resultRelation


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
        attr =  self.visit(ctx.att())
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
        queueOfList = self.visit(ctx.rels())
        firstElem = self.visit(ctx.rel())
        return [firstElem]+queueOfList

    def visitRelationDeclSimple(self, ctx:miniSQLParser.RelationDeclSimpleContext):
        print_debug("visitRelationDeclSimple")
        return [self.visit(ctx.rel())]

    # __________________ rel rules _____________________________________________
    def visitRelationID(self, ctx:miniSQLParser.RelationIDContext):
        print_debug("visitRelationID")
        filename = ctx.FILENAME().getText()
        self.dataManager.load(filename)
        tableName = ctx.ID().getText()
        self.relationNames[tableName]=filename
        return tableName

    def visitSubquery(self, ctx:miniSQLParser.SubqueryContext):
        print_debug("visitSubquery")
        return self.visit(ctx.sql())

    # _____________________ cond rules _________________________________________
    def visitCondOrList(self, ctx:miniSQLParser.CondOrListContext):
        print_debug("visitCondOrList")
        queueOfList = self.visit(ctx.cond())
        firstElem = self.visit(ctx.and_cond())
        return [firstElem]+queueOfList

    def visitCondOrSimple(self, ctx:miniSQLParser.CondOrSimpleContext):
        print_debug("visitCondOrSimple")
        return [self.visit(ctx.and_cond())]

    # ____________________ and_cond rules ______________________________________
    def visitCondAndList(self, ctx:miniSQLParser.CondAndListContext):
        print_debug("visitCondAndList")
        queueOfList = self.visit(ctx.cond())
        firstElem = self.visit(ctx.and_cond())
        return [firstElem]+queueOfList

    def visitCondAndSimple(self, ctx:miniSQLParser.CondAndSimpleContext):
        print_debug("visitCondAndSimple")
        return [self.visit(ctx.at_cond())]

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
        return Condition(attr1,op,attr2)

    def visitCompIn(self, ctx:miniSQLParser.CompInContext):
        print_debug("visitCompIn")
        print("Not implemented Yet !")
        return Condition(Op.EQ)

    def visitCompNotIn(self, ctx:miniSQLParser.CompNotInContext):
        print_debug("visitCompNotIn")
        print("Not implemented Yet !")
        return Condition(Op.EQ)

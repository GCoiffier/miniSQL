# Generated from src/parser/miniSQL.g4 by ANTLR 4.7
from database import *
from SQLoperation import *
from exceptions import *
from condition import *
from antlr4 import *
from .miniSQLParser import miniSQLParser

# This class defines a complete generic visitor for a parse tree produced by miniSQLParser.

class miniSQLVisitor(ParseTreeVisitor):

    def __init__(self):
        ParseTreeVisitor.__init__(self)
        self.relationNames = dict()
        self.attributeNames = dict()

    # Visit a parse tree produced by miniSQLParser#main.
    def visitMain(self, ctx:miniSQLParser.MainContext):
        return self.visit(ctx.sql())

    # ________________________ sql rules _______________________________________
    # Visit a parse tree produced by miniSQLParser#sqlNormal.
    def visitSqlNormal(self, ctx:miniSQLParser.SqlNormalContext):

        # Load the tables
        self.visit(ctx.rels())

        nbTables = len(self.relationNames)
        print_debug(self.relationNames)

        k = list(self.relationNames.keys())
        resultRelation = DATAS[self.relationNames[k[0]]]

        if (nbTables>1): # perform a join
            for i in range(1,nbTables):
                resultRelation = join(resultRelation, DATAS[self.relationNames[k[i]]])

        attributes = self.visit(ctx.atts())
        print_debug(attributes)

        if ctx.WHERE() is not None:
            print("There is a WHERE")

        resultRelation = project(resultRelation, attributes)

        return resultRelation


    # Visit a parse tree produced by miniSQLParser#sqlMinus.
    def visitSqlMinus(self, ctx:miniSQLParser.SqlMinusContext):
        print("MINUS not implemented yet")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#sqlUnion.
    def visitSqlUnion(self, ctx:miniSQLParser.SqlUnionContext):
        print("Union not implemented yet")
        return self.visitChildren(ctx)


    # _________________________ atts rules _____________________________________
    def visitAttributeDeclAll(self, ctx:miniSQLParser.AttributeDeclAllContext):
        # SELECT *
        attributes = []
        for relationName in self.relationNames.values():
            attributes += DATAS[relationName].get_keys()
        return attributes

    def visitAttributeDeclList(self, ctx:miniSQLParser.AttributeDeclListContext):
        queueOfList = self.visit(ctx.atts())
        firstElem = self.visit(ctx.attd())
        return [firstElem]+queueOfList

    def visitAttributeDeclSimple(self, ctx:miniSQLParser.AttributeDeclSimpleContext):
        return [self.visitChildren(ctx)]

    # ___________________ attd rules ___________________________________________
    def visitAttributeSimple(self, ctx:miniSQLParser.AttributeSimpleContext):
        fullName =  self.visit(ctx.att())
        self.attributeNames[fullName] = fullName
        return fullName

    def visitAttributeAs(self, ctx:miniSQLParser.AttributeAsContext):
        fullName = self.visit(ctx.att())
        asName = ctx.ID().getText()
        self.attributeNames[asName] = fullName
        return asName

    # __________________ att rule ______________________________________________
    def visitAtt(self, ctx:miniSQLParser.AttContext):
        tableName = ctx.ID(0).getText()
        attrName = ctx.ID(1).getText()
        return (tableName,attrName)

    # __________________ rels rules ____________________________________________
    def visitRelationDeclList(self, ctx:miniSQLParser.RelationDeclListContext):
        queueOfList = self.visit(ctx.rels())
        firstElem = self.visit(ctx.rel())
        return [firstElem]+queueOfList

    def visitRelationDeclSimple(self, ctx:miniSQLParser.RelationDeclSimpleContext):
        return [self.visit(ctx.rel())]

    # __________________ rel rules _____________________________________________
    def visitRelationID(self, ctx:miniSQLParser.RelationIDContext):
        filename = ctx.FILENAME().getText()
        DATAS.load(filename)
        tableName = ctx.ID().getText()
        self.relationNames[tableName]=filename
        return tableName

    # Visit a parse tree produced by miniSQLParser#Subquery.
    def visitSubquery(self, ctx:miniSQLParser.SubqueryContext):
        # TODO
        pass

    # Visit a parse tree produced by miniSQLParser#CondOrList.
    def visitCondOrList(self, ctx:miniSQLParser.CondOrListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#CondOrSimple.
    def visitCondOrSimple(self, ctx:miniSQLParser.CondOrSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#CondAndList.
    def visitCondAndList(self, ctx:miniSQLParser.CondAndListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#CondAndSimple.
    def visitCondAndSimple(self, ctx:miniSQLParser.CondAndSimpleContext):
        return self.visitChildren(ctx)

    def visitCompSimple(self, ctx:miniSQLParser.CompSimpleContext):
        op = ctx.COMP_OP().getText()
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
        return FilterCondition()


    def visitCompIn(self, ctx:miniSQLParser.CompInContext):
        return self.visitChildren(ctx)

    def visitCompNotIN(self, ctx:miniSQLParser.CompNotINContext):
        return self.visitChildren(ctx)



del miniSQLParser

# Generated from src/parser/miniSQL.g4 by ANTLR 4.7
from database import *
from SQLoperation import *
from exceptions import *
from antlr4 import *
from .miniSQLParser import miniSQLParser

# This class defines a complete generic visitor for a parse tree produced by miniSQLParser.

class miniSQLVisitor(ParseTreeVisitor):

    def __init__(self):
        ParseTreeVisitor.__init__(self)
        self.relationNames = []

    # Visit a parse tree produced by miniSQLParser#main.
    def visitMain(self, ctx:miniSQLParser.MainContext):
        return self.visit(ctx.sql())

    # ________________________ sql rules _______________________________________
    # Visit a parse tree produced by miniSQLParser#sqlNormal.
    def visitSqlNormal(self, ctx:miniSQLParser.SqlNormalContext):

        tables = self.visit(ctx.rels())
        for relName in tables:
            self.relationNames.append(relName)
        nbTables = len(self.relationNames)
        print_debug(self.relationNames)

        resultRelation = DATAS[self.relationNames[0]]

        print_debug("--- in visitor : --")
        print_debug(resultRelation)

        if (nbTables>1): # perform a join
            for i in range(1,nbTables):
                resultRelation = join(resultRelation, DATAS[self.relationNames[i]])

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
        for relationName in self.relationNames:
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
        return self.visit(ctx.att())

    def visitAttributeAs(self, ctx:miniSQLParser.AttributeAsContext):
        # TODO : the AS does nothing for now
        return self.visit(ctx.att())

    # __________________ att rule ______________________________________________
    def visitAttributeID(self, ctx:miniSQLParser.AttributeIDContext):
        return ctx.getText()

    def visitAttributeRefID(self, ctx:miniSQLParser.AttributeRefIDContext):
        # TODO : the table.elem does nothing for now
        return str(self.visit(ctx.ID(1)))

    # __________________ rels rules ____________________________________________
    def visitRelationDeclList(self, ctx:miniSQLParser.RelationDeclListContext):
        queueOfList = self.visit(ctx.rels())
        firstElem = self.visit(ctx.rel())
        return [firstElem]+queueOfList

    def visitRelationDeclSimple(self, ctx:miniSQLParser.RelationDeclSimpleContext):
        return [self.visit(ctx.rel())]

    # __________________ rel rules _____________________________________________
    def visitRelationID(self, ctx:miniSQLParser.RelationIDContext):
        return ctx.getText()

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


    # Visit a parse tree produced by miniSQLParser#at_cond.
    def visitAt_cond(self, ctx:miniSQLParser.At_condContext):
        return self.visitChildren(ctx)



del miniSQLParser

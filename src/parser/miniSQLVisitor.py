# Generated from src/parser/miniSQL.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .miniSQLParser import miniSQLParser
else:
    from miniSQLParser import miniSQLParser

# This class defines a complete generic visitor for a parse tree produced by miniSQLParser.

class miniSQLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by miniSQLParser#main.
    def visitMain(self, ctx:miniSQLParser.MainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#sqlNormal.
    def visitSqlNormal(self, ctx:miniSQLParser.SqlNormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#sqlMinus.
    def visitSqlMinus(self, ctx:miniSQLParser.SqlMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#sqlUnion.
    def visitSqlUnion(self, ctx:miniSQLParser.SqlUnionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#sqlGroupBy.
    def visitSqlGroupBy(self, ctx:miniSQLParser.SqlGroupByContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#orderBy.
    def visitOrderBy(self, ctx:miniSQLParser.OrderByContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#AttributeDeclAll.
    def visitAttributeDeclAll(self, ctx:miniSQLParser.AttributeDeclAllContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#AttributeDeclList.
    def visitAttributeDeclList(self, ctx:miniSQLParser.AttributeDeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#AttributeDeclSimple.
    def visitAttributeDeclSimple(self, ctx:miniSQLParser.AttributeDeclSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#AttributeSimple.
    def visitAttributeSimple(self, ctx:miniSQLParser.AttributeSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#AttributeAs.
    def visitAttributeAs(self, ctx:miniSQLParser.AttributeAsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#att.
    def visitAtt(self, ctx:miniSQLParser.AttContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#attgrp.
    def visitAttgrp(self, ctx:miniSQLParser.AttgrpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#attgrpbis.
    def visitAttgrpbis(self, ctx:miniSQLParser.AttgrpbisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#RelationDeclList.
    def visitRelationDeclList(self, ctx:miniSQLParser.RelationDeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#RelationDeclSimple.
    def visitRelationDeclSimple(self, ctx:miniSQLParser.RelationDeclSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#RelationID.
    def visitRelationID(self, ctx:miniSQLParser.RelationIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#RelationSubQuery.
    def visitRelationSubQuery(self, ctx:miniSQLParser.RelationSubQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#CondOrList.
    def visitCondOrList(self, ctx:miniSQLParser.CondOrListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#CondOrSimple.
    def visitCondOrSimple(self, ctx:miniSQLParser.CondOrSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#CondAndOr.
    def visitCondAndOr(self, ctx:miniSQLParser.CondAndOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#CondAndList.
    def visitCondAndList(self, ctx:miniSQLParser.CondAndListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#CondAndSimple.
    def visitCondAndSimple(self, ctx:miniSQLParser.CondAndSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#CompSimple.
    def visitCompSimple(self, ctx:miniSQLParser.CompSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#CompIn.
    def visitCompIn(self, ctx:miniSQLParser.CompInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#CompNotIn.
    def visitCompNotIn(self, ctx:miniSQLParser.CompNotInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#op.
    def visitOp(self, ctx:miniSQLParser.OpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#aggr.
    def visitAggr(self, ctx:miniSQLParser.AggrContext):
        return self.visitChildren(ctx)



del miniSQLParser
# Generated from src/parser/miniSQL.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .miniSQLParser import miniSQLParser
else:
    from miniSQLParser import miniSQLParser

# This class defines a complete generic visitor for a parse tree produced by miniSQLParser.

class miniSQLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by miniSQLParser#sql.
    def visitSql(self, ctx:miniSQLParser.SqlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#atts.
    def visitAtts(self, ctx:miniSQLParser.AttsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#attd.
    def visitAttd(self, ctx:miniSQLParser.AttdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#att.
    def visitAtt(self, ctx:miniSQLParser.AttContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#rels.
    def visitRels(self, ctx:miniSQLParser.RelsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#rel.
    def visitRel(self, ctx:miniSQLParser.RelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#filename.
    def visitFilename(self, ctx:miniSQLParser.FilenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#cond.
    def visitCond(self, ctx:miniSQLParser.CondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#and_cond.
    def visitAnd_cond(self, ctx:miniSQLParser.And_condContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniSQLParser#at_cond.
    def visitAt_cond(self, ctx:miniSQLParser.At_condContext):
        return self.visitChildren(ctx)



del miniSQLParser
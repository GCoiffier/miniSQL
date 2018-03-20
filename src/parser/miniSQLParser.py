# Generated from src/parser/miniSQL.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\37")
        buf.write("\u0085\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\5\2")
        buf.write("\33\n\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3#\n\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3")
        buf.write("\65\n\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4=\n\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\5\5D\n\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\5")
        buf.write("\7O\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\bZ\n\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\5\ta\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\5\nn\n\n\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\5\13\u0081\n\13\3\f\3\f\3\f\2\2\r\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\2\3\3\2\26\33\2\u0087\2\30\3\2\2\2\4\64\3")
        buf.write("\2\2\2\6<\3\2\2\2\bC\3\2\2\2\nE\3\2\2\2\fN\3\2\2\2\16")
        buf.write("Y\3\2\2\2\20`\3\2\2\2\22m\3\2\2\2\24\u0080\3\2\2\2\26")
        buf.write("\u0082\3\2\2\2\30\32\5\4\3\2\31\33\7\7\2\2\32\31\3\2\2")
        buf.write("\2\32\33\3\2\2\2\33\3\3\2\2\2\34\35\7\n\2\2\35\36\5\6")
        buf.write("\4\2\36\37\7\13\2\2\37\"\5\f\7\2 !\7\f\2\2!#\5\20\t\2")
        buf.write("\" \3\2\2\2\"#\3\2\2\2#\65\3\2\2\2$%\7\5\2\2%&\5\4\3\2")
        buf.write("&\'\7\6\2\2\'(\7\16\2\2()\7\5\2\2)*\5\4\3\2*+\7\6\2\2")
        buf.write("+\65\3\2\2\2,-\7\5\2\2-.\5\4\3\2./\7\6\2\2/\60\7\17\2")
        buf.write("\2\60\61\7\5\2\2\61\62\5\4\3\2\62\63\7\6\2\2\63\65\3\2")
        buf.write("\2\2\64\34\3\2\2\2\64$\3\2\2\2\64,\3\2\2\2\65\5\3\2\2")
        buf.write("\2\66=\7\b\2\2\678\5\b\5\289\7\3\2\29:\5\6\4\2:=\3\2\2")
        buf.write("\2;=\5\b\5\2<\66\3\2\2\2<\67\3\2\2\2<;\3\2\2\2=\7\3\2")
        buf.write("\2\2>D\5\n\6\2?@\5\n\6\2@A\7\r\2\2AB\7\35\2\2BD\3\2\2")
        buf.write("\2C>\3\2\2\2C?\3\2\2\2D\t\3\2\2\2EF\7\35\2\2FG\7\4\2\2")
        buf.write("GH\7\35\2\2H\13\3\2\2\2IJ\5\16\b\2JK\7\3\2\2KL\5\f\7\2")
        buf.write("LO\3\2\2\2MO\5\16\b\2NI\3\2\2\2NM\3\2\2\2O\r\3\2\2\2P")
        buf.write("Q\7\t\2\2QR\7\34\2\2RS\7\t\2\2SZ\7\35\2\2TU\7\5\2\2UV")
        buf.write("\5\4\3\2VW\7\6\2\2WX\7\35\2\2XZ\3\2\2\2YP\3\2\2\2YT\3")
        buf.write("\2\2\2Z\17\3\2\2\2[\\\5\22\n\2\\]\7\23\2\2]^\5\20\t\2")
        buf.write("^a\3\2\2\2_a\5\22\n\2`[\3\2\2\2`_\3\2\2\2a\21\3\2\2\2")
        buf.write("bc\7\5\2\2cd\5\20\t\2de\7\6\2\2ef\7\22\2\2fg\5\22\n\2")
        buf.write("gn\3\2\2\2hi\5\24\13\2ij\7\22\2\2jk\5\22\n\2kn\3\2\2\2")
        buf.write("ln\5\24\13\2mb\3\2\2\2mh\3\2\2\2ml\3\2\2\2n\23\3\2\2\2")
        buf.write("op\5\n\6\2pq\5\26\f\2qr\5\n\6\2r\u0081\3\2\2\2st\5\n\6")
        buf.write("\2tu\7\25\2\2uv\7\5\2\2vw\5\4\3\2wx\7\6\2\2x\u0081\3\2")
        buf.write("\2\2yz\5\n\6\2z{\7\24\2\2{|\7\25\2\2|}\7\5\2\2}~\5\4\3")
        buf.write("\2~\177\7\6\2\2\177\u0081\3\2\2\2\u0080o\3\2\2\2\u0080")
        buf.write("s\3\2\2\2\u0080y\3\2\2\2\u0081\25\3\2\2\2\u0082\u0083")
        buf.write("\t\2\2\2\u0083\27\3\2\2\2\f\32\"\64<CNY`m\u0080")
        return buf.getvalue()


class miniSQLParser ( Parser ):

    grammarFileName = "miniSQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'.'", "'('", "')'", "';'", "'*'", 
                     "'\"'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'='", "'!='", "'<'", "'<='", "'>'", "'>='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "LPAR", "RPAR", 
                      "COLON", "STAR", "QUOTE", "SELECT", "FROM", "WHERE", 
                      "AS", "MINUS", "UNION", "JOIN", "GROUPBY", "AND", 
                      "OR", "NOT", "IN", "EQ", "NEQ", "LT", "LE", "GT", 
                      "GE", "FILENAME", "ID", "WS", "NEWLINE" ]

    RULE_main = 0
    RULE_sql = 1
    RULE_atts = 2
    RULE_attd = 3
    RULE_att = 4
    RULE_rels = 5
    RULE_rel = 6
    RULE_cond = 7
    RULE_and_cond = 8
    RULE_at_cond = 9
    RULE_op = 10

    ruleNames =  [ "main", "sql", "atts", "attd", "att", "rels", "rel", 
                   "cond", "and_cond", "at_cond", "op" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    LPAR=3
    RPAR=4
    COLON=5
    STAR=6
    QUOTE=7
    SELECT=8
    FROM=9
    WHERE=10
    AS=11
    MINUS=12
    UNION=13
    JOIN=14
    GROUPBY=15
    AND=16
    OR=17
    NOT=18
    IN=19
    EQ=20
    NEQ=21
    LT=22
    LE=23
    GT=24
    GE=25
    FILENAME=26
    ID=27
    WS=28
    NEWLINE=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class MainContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sql(self):
            return self.getTypedRuleContext(miniSQLParser.SqlContext,0)


        def COLON(self):
            return self.getToken(miniSQLParser.COLON, 0)

        def getRuleIndex(self):
            return miniSQLParser.RULE_main

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain" ):
                return visitor.visitMain(self)
            else:
                return visitor.visitChildren(self)




    def main(self):

        localctx = miniSQLParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.sql()
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==miniSQLParser.COLON:
                self.state = 23
                self.match(miniSQLParser.COLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SqlContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return miniSQLParser.RULE_sql

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SqlMinusContext(SqlContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miniSQLParser.SqlContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self, i:int=None):
            if i is None:
                return self.getTokens(miniSQLParser.LPAR)
            else:
                return self.getToken(miniSQLParser.LPAR, i)
        def sql(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniSQLParser.SqlContext)
            else:
                return self.getTypedRuleContext(miniSQLParser.SqlContext,i)

        def RPAR(self, i:int=None):
            if i is None:
                return self.getTokens(miniSQLParser.RPAR)
            else:
                return self.getToken(miniSQLParser.RPAR, i)
        def MINUS(self):
            return self.getToken(miniSQLParser.MINUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSqlMinus" ):
                return visitor.visitSqlMinus(self)
            else:
                return visitor.visitChildren(self)


    class SqlUnionContext(SqlContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miniSQLParser.SqlContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self, i:int=None):
            if i is None:
                return self.getTokens(miniSQLParser.LPAR)
            else:
                return self.getToken(miniSQLParser.LPAR, i)
        def sql(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniSQLParser.SqlContext)
            else:
                return self.getTypedRuleContext(miniSQLParser.SqlContext,i)

        def RPAR(self, i:int=None):
            if i is None:
                return self.getTokens(miniSQLParser.RPAR)
            else:
                return self.getToken(miniSQLParser.RPAR, i)
        def UNION(self):
            return self.getToken(miniSQLParser.UNION, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSqlUnion" ):
                return visitor.visitSqlUnion(self)
            else:
                return visitor.visitChildren(self)


    class SqlNormalContext(SqlContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miniSQLParser.SqlContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SELECT(self):
            return self.getToken(miniSQLParser.SELECT, 0)
        def atts(self):
            return self.getTypedRuleContext(miniSQLParser.AttsContext,0)

        def FROM(self):
            return self.getToken(miniSQLParser.FROM, 0)
        def rels(self):
            return self.getTypedRuleContext(miniSQLParser.RelsContext,0)

        def WHERE(self):
            return self.getToken(miniSQLParser.WHERE, 0)
        def cond(self):
            return self.getTypedRuleContext(miniSQLParser.CondContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSqlNormal" ):
                return visitor.visitSqlNormal(self)
            else:
                return visitor.visitChildren(self)



    def sql(self):

        localctx = miniSQLParser.SqlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sql)
        self._la = 0 # Token type
        try:
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = miniSQLParser.SqlNormalContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.match(miniSQLParser.SELECT)
                self.state = 27
                self.atts()
                self.state = 28
                self.match(miniSQLParser.FROM)
                self.state = 29
                self.rels()
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miniSQLParser.WHERE:
                    self.state = 30
                    self.match(miniSQLParser.WHERE)
                    self.state = 31
                    self.cond()


                pass

            elif la_ == 2:
                localctx = miniSQLParser.SqlMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.match(miniSQLParser.LPAR)
                self.state = 35
                self.sql()
                self.state = 36
                self.match(miniSQLParser.RPAR)
                self.state = 37
                self.match(miniSQLParser.MINUS)
                self.state = 38
                self.match(miniSQLParser.LPAR)
                self.state = 39
                self.sql()
                self.state = 40
                self.match(miniSQLParser.RPAR)
                pass

            elif la_ == 3:
                localctx = miniSQLParser.SqlUnionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.match(miniSQLParser.LPAR)
                self.state = 43
                self.sql()
                self.state = 44
                self.match(miniSQLParser.RPAR)
                self.state = 45
                self.match(miniSQLParser.UNION)
                self.state = 46
                self.match(miniSQLParser.LPAR)
                self.state = 47
                self.sql()
                self.state = 48
                self.match(miniSQLParser.RPAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AttsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return miniSQLParser.RULE_atts

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AttributeDeclListContext(AttsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miniSQLParser.AttsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def attd(self):
            return self.getTypedRuleContext(miniSQLParser.AttdContext,0)

        def atts(self):
            return self.getTypedRuleContext(miniSQLParser.AttsContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributeDeclList" ):
                return visitor.visitAttributeDeclList(self)
            else:
                return visitor.visitChildren(self)


    class AttributeDeclSimpleContext(AttsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miniSQLParser.AttsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def attd(self):
            return self.getTypedRuleContext(miniSQLParser.AttdContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributeDeclSimple" ):
                return visitor.visitAttributeDeclSimple(self)
            else:
                return visitor.visitChildren(self)


    class AttributeDeclAllContext(AttsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miniSQLParser.AttsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STAR(self):
            return self.getToken(miniSQLParser.STAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributeDeclAll" ):
                return visitor.visitAttributeDeclAll(self)
            else:
                return visitor.visitChildren(self)



    def atts(self):

        localctx = miniSQLParser.AttsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_atts)
        try:
            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = miniSQLParser.AttributeDeclAllContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.match(miniSQLParser.STAR)
                pass

            elif la_ == 2:
                localctx = miniSQLParser.AttributeDeclListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.attd()
                self.state = 54
                self.match(miniSQLParser.T__0)
                self.state = 55
                self.atts()
                pass

            elif la_ == 3:
                localctx = miniSQLParser.AttributeDeclSimpleContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 57
                self.attd()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AttdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return miniSQLParser.RULE_attd

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AttributeSimpleContext(AttdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miniSQLParser.AttdContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def att(self):
            return self.getTypedRuleContext(miniSQLParser.AttContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributeSimple" ):
                return visitor.visitAttributeSimple(self)
            else:
                return visitor.visitChildren(self)


    class AttributeAsContext(AttdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miniSQLParser.AttdContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def att(self):
            return self.getTypedRuleContext(miniSQLParser.AttContext,0)

        def AS(self):
            return self.getToken(miniSQLParser.AS, 0)
        def ID(self):
            return self.getToken(miniSQLParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributeAs" ):
                return visitor.visitAttributeAs(self)
            else:
                return visitor.visitChildren(self)



    def attd(self):

        localctx = miniSQLParser.AttdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attd)
        try:
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = miniSQLParser.AttributeSimpleContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.att()
                pass

            elif la_ == 2:
                localctx = miniSQLParser.AttributeAsContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.att()
                self.state = 62
                self.match(miniSQLParser.AS)
                self.state = 63
                self.match(miniSQLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AttContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(miniSQLParser.ID)
            else:
                return self.getToken(miniSQLParser.ID, i)

        def getRuleIndex(self):
            return miniSQLParser.RULE_att

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtt" ):
                return visitor.visitAtt(self)
            else:
                return visitor.visitChildren(self)




    def att(self):

        localctx = miniSQLParser.AttContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_att)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(miniSQLParser.ID)
            self.state = 68
            self.match(miniSQLParser.T__1)
            self.state = 69
            self.match(miniSQLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RelsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return miniSQLParser.RULE_rels

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RelationDeclSimpleContext(RelsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miniSQLParser.RelsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def rel(self):
            return self.getTypedRuleContext(miniSQLParser.RelContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationDeclSimple" ):
                return visitor.visitRelationDeclSimple(self)
            else:
                return visitor.visitChildren(self)


    class RelationDeclListContext(RelsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miniSQLParser.RelsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def rel(self):
            return self.getTypedRuleContext(miniSQLParser.RelContext,0)

        def rels(self):
            return self.getTypedRuleContext(miniSQLParser.RelsContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationDeclList" ):
                return visitor.visitRelationDeclList(self)
            else:
                return visitor.visitChildren(self)



    def rels(self):

        localctx = miniSQLParser.RelsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_rels)
        try:
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = miniSQLParser.RelationDeclListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.rel()
                self.state = 72
                self.match(miniSQLParser.T__0)
                self.state = 73
                self.rels()
                pass

            elif la_ == 2:
                localctx = miniSQLParser.RelationDeclSimpleContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.rel()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return miniSQLParser.RULE_rel

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RelationIDContext(RelContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miniSQLParser.RelContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def QUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(miniSQLParser.QUOTE)
            else:
                return self.getToken(miniSQLParser.QUOTE, i)
        def FILENAME(self):
            return self.getToken(miniSQLParser.FILENAME, 0)
        def ID(self):
            return self.getToken(miniSQLParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationID" ):
                return visitor.visitRelationID(self)
            else:
                return visitor.visitChildren(self)


    class SubqueryContext(RelContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miniSQLParser.RelContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(miniSQLParser.LPAR, 0)
        def sql(self):
            return self.getTypedRuleContext(miniSQLParser.SqlContext,0)

        def RPAR(self):
            return self.getToken(miniSQLParser.RPAR, 0)
        def ID(self):
            return self.getToken(miniSQLParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubquery" ):
                return visitor.visitSubquery(self)
            else:
                return visitor.visitChildren(self)



    def rel(self):

        localctx = miniSQLParser.RelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_rel)
        try:
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [miniSQLParser.QUOTE]:
                localctx = miniSQLParser.RelationIDContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.match(miniSQLParser.QUOTE)
                self.state = 79
                self.match(miniSQLParser.FILENAME)
                self.state = 80
                self.match(miniSQLParser.QUOTE)
                self.state = 81
                self.match(miniSQLParser.ID)
                pass
            elif token in [miniSQLParser.LPAR]:
                localctx = miniSQLParser.SubqueryContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.match(miniSQLParser.LPAR)
                self.state = 83
                self.sql()
                self.state = 84
                self.match(miniSQLParser.RPAR)
                self.state = 85
                self.match(miniSQLParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CondContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return miniSQLParser.RULE_cond

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CondOrSimpleContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miniSQLParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def and_cond(self):
            return self.getTypedRuleContext(miniSQLParser.And_condContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondOrSimple" ):
                return visitor.visitCondOrSimple(self)
            else:
                return visitor.visitChildren(self)


    class CondOrListContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miniSQLParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def and_cond(self):
            return self.getTypedRuleContext(miniSQLParser.And_condContext,0)

        def OR(self):
            return self.getToken(miniSQLParser.OR, 0)
        def cond(self):
            return self.getTypedRuleContext(miniSQLParser.CondContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondOrList" ):
                return visitor.visitCondOrList(self)
            else:
                return visitor.visitChildren(self)



    def cond(self):

        localctx = miniSQLParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_cond)
        try:
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = miniSQLParser.CondOrListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.and_cond()
                self.state = 90
                self.match(miniSQLParser.OR)
                self.state = 91
                self.cond()
                pass

            elif la_ == 2:
                localctx = miniSQLParser.CondOrSimpleContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.and_cond()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class And_condContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return miniSQLParser.RULE_and_cond

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CondAndSimpleContext(And_condContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miniSQLParser.And_condContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def at_cond(self):
            return self.getTypedRuleContext(miniSQLParser.At_condContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondAndSimple" ):
                return visitor.visitCondAndSimple(self)
            else:
                return visitor.visitChildren(self)


    class CondAndListContext(And_condContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miniSQLParser.And_condContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def at_cond(self):
            return self.getTypedRuleContext(miniSQLParser.At_condContext,0)

        def AND(self):
            return self.getToken(miniSQLParser.AND, 0)
        def and_cond(self):
            return self.getTypedRuleContext(miniSQLParser.And_condContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondAndList" ):
                return visitor.visitCondAndList(self)
            else:
                return visitor.visitChildren(self)


    class CondAndOrContext(And_condContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miniSQLParser.And_condContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(miniSQLParser.LPAR, 0)
        def cond(self):
            return self.getTypedRuleContext(miniSQLParser.CondContext,0)

        def RPAR(self):
            return self.getToken(miniSQLParser.RPAR, 0)
        def AND(self):
            return self.getToken(miniSQLParser.AND, 0)
        def and_cond(self):
            return self.getTypedRuleContext(miniSQLParser.And_condContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondAndOr" ):
                return visitor.visitCondAndOr(self)
            else:
                return visitor.visitChildren(self)



    def and_cond(self):

        localctx = miniSQLParser.And_condContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_and_cond)
        try:
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = miniSQLParser.CondAndOrContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.match(miniSQLParser.LPAR)
                self.state = 97
                self.cond()
                self.state = 98
                self.match(miniSQLParser.RPAR)
                self.state = 99
                self.match(miniSQLParser.AND)
                self.state = 100
                self.and_cond()
                pass

            elif la_ == 2:
                localctx = miniSQLParser.CondAndListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.at_cond()
                self.state = 103
                self.match(miniSQLParser.AND)
                self.state = 104
                self.and_cond()
                pass

            elif la_ == 3:
                localctx = miniSQLParser.CondAndSimpleContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 106
                self.at_cond()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class At_condContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return miniSQLParser.RULE_at_cond

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CompInContext(At_condContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miniSQLParser.At_condContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def att(self):
            return self.getTypedRuleContext(miniSQLParser.AttContext,0)

        def IN(self):
            return self.getToken(miniSQLParser.IN, 0)
        def LPAR(self):
            return self.getToken(miniSQLParser.LPAR, 0)
        def sql(self):
            return self.getTypedRuleContext(miniSQLParser.SqlContext,0)

        def RPAR(self):
            return self.getToken(miniSQLParser.RPAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompIn" ):
                return visitor.visitCompIn(self)
            else:
                return visitor.visitChildren(self)


    class CompNotInContext(At_condContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miniSQLParser.At_condContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def att(self):
            return self.getTypedRuleContext(miniSQLParser.AttContext,0)

        def NOT(self):
            return self.getToken(miniSQLParser.NOT, 0)
        def IN(self):
            return self.getToken(miniSQLParser.IN, 0)
        def LPAR(self):
            return self.getToken(miniSQLParser.LPAR, 0)
        def sql(self):
            return self.getTypedRuleContext(miniSQLParser.SqlContext,0)

        def RPAR(self):
            return self.getToken(miniSQLParser.RPAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompNotIn" ):
                return visitor.visitCompNotIn(self)
            else:
                return visitor.visitChildren(self)


    class CompSimpleContext(At_condContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miniSQLParser.At_condContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def att(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniSQLParser.AttContext)
            else:
                return self.getTypedRuleContext(miniSQLParser.AttContext,i)

        def op(self):
            return self.getTypedRuleContext(miniSQLParser.OpContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompSimple" ):
                return visitor.visitCompSimple(self)
            else:
                return visitor.visitChildren(self)



    def at_cond(self):

        localctx = miniSQLParser.At_condContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_at_cond)
        try:
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = miniSQLParser.CompSimpleContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.att()
                self.state = 110
                self.op()
                self.state = 111
                self.att()
                pass

            elif la_ == 2:
                localctx = miniSQLParser.CompInContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.att()
                self.state = 114
                self.match(miniSQLParser.IN)
                self.state = 115
                self.match(miniSQLParser.LPAR)
                self.state = 116
                self.sql()
                self.state = 117
                self.match(miniSQLParser.RPAR)
                pass

            elif la_ == 3:
                localctx = miniSQLParser.CompNotInContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 119
                self.att()
                self.state = 120
                self.match(miniSQLParser.NOT)
                self.state = 121
                self.match(miniSQLParser.IN)
                self.state = 122
                self.match(miniSQLParser.LPAR)
                self.state = 123
                self.sql()
                self.state = 124
                self.match(miniSQLParser.RPAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(miniSQLParser.EQ, 0)

        def NEQ(self):
            return self.getToken(miniSQLParser.NEQ, 0)

        def LT(self):
            return self.getToken(miniSQLParser.LT, 0)

        def LE(self):
            return self.getToken(miniSQLParser.LE, 0)

        def GT(self):
            return self.getToken(miniSQLParser.GT, 0)

        def GE(self):
            return self.getToken(miniSQLParser.GE, 0)

        def getRuleIndex(self):
            return miniSQLParser.RULE_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp" ):
                return visitor.visitOp(self)
            else:
                return visitor.visitChildren(self)




    def op(self):

        localctx = miniSQLParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miniSQLParser.EQ) | (1 << miniSQLParser.NEQ) | (1 << miniSQLParser.LT) | (1 << miniSQLParser.LE) | (1 << miniSQLParser.GT) | (1 << miniSQLParser.GE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






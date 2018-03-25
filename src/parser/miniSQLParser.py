# Generated from src/parser/miniSQL.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\'")
        buf.write("\u009f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\5\2\37\n\2\3\3\3\3\5\3#\n\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\5\3*\n\3\3\3\3\3\5\3.\n\3\3\3\5\3\61\n\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\5\3C\n\3\3\4\3\4\3\4\5\4H\n\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\5\5P\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\5\6\\\n\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\5\bg")
        buf.write("\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\tr\n\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\5\ny\n\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\5\13\u0086\n\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\5\f\u0099\n\f\3\r\3\r\3\16\3\16\3\16\2\2\17\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\2\5\3\2\30\31\3\2\36#\3\2\32")
        buf.write("\35\2\u00a4\2\34\3\2\2\2\4B\3\2\2\2\6D\3\2\2\2\bO\3\2")
        buf.write("\2\2\n[\3\2\2\2\f]\3\2\2\2\16f\3\2\2\2\20q\3\2\2\2\22")
        buf.write("x\3\2\2\2\24\u0085\3\2\2\2\26\u0098\3\2\2\2\30\u009a\3")
        buf.write("\2\2\2\32\u009c\3\2\2\2\34\36\5\4\3\2\35\37\7\7\2\2\36")
        buf.write("\35\3\2\2\2\36\37\3\2\2\2\37\3\3\2\2\2 \"\7\n\2\2!#\7")
        buf.write("\13\2\2\"!\3\2\2\2\"#\3\2\2\2#$\3\2\2\2$%\5\b\5\2%&\7")
        buf.write("\f\2\2&)\5\16\b\2\'(\7\r\2\2(*\5\22\n\2)\'\3\2\2\2)*\3")
        buf.write("\2\2\2*-\3\2\2\2+,\7\22\2\2,.\5\f\7\2-+\3\2\2\2-.\3\2")
        buf.write("\2\2.\60\3\2\2\2/\61\5\6\4\2\60/\3\2\2\2\60\61\3\2\2\2")
        buf.write("\61C\3\2\2\2\62\63\7\5\2\2\63\64\5\4\3\2\64\65\7\6\2\2")
        buf.write("\65\66\7\17\2\2\66\67\7\5\2\2\678\5\4\3\289\7\6\2\29C")
        buf.write("\3\2\2\2:;\7\5\2\2;<\5\4\3\2<=\7\6\2\2=>\7\20\2\2>?\7")
        buf.write("\5\2\2?@\5\4\3\2@A\7\6\2\2AC\3\2\2\2B \3\2\2\2B\62\3\2")
        buf.write("\2\2B:\3\2\2\2C\5\3\2\2\2DE\7\23\2\2EG\5\b\5\2FH\t\2\2")
        buf.write("\2GF\3\2\2\2GH\3\2\2\2H\7\3\2\2\2IP\7\b\2\2JK\5\n\6\2")
        buf.write("KL\7\3\2\2LM\5\b\5\2MP\3\2\2\2NP\5\n\6\2OI\3\2\2\2OJ\3")
        buf.write("\2\2\2ON\3\2\2\2P\t\3\2\2\2Q\\\5\f\7\2RS\5\f\7\2ST\7\16")
        buf.write("\2\2TU\7%\2\2U\\\3\2\2\2VW\5\32\16\2WX\7\5\2\2XY\5\f\7")
        buf.write("\2YZ\7\6\2\2Z\\\3\2\2\2[Q\3\2\2\2[R\3\2\2\2[V\3\2\2\2")
        buf.write("\\\13\3\2\2\2]^\7%\2\2^_\7\4\2\2_`\7%\2\2`\r\3\2\2\2a")
        buf.write("b\5\20\t\2bc\7\3\2\2cd\5\16\b\2dg\3\2\2\2eg\5\20\t\2f")
        buf.write("a\3\2\2\2fe\3\2\2\2g\17\3\2\2\2hi\7\t\2\2ij\7$\2\2jk\7")
        buf.write("\t\2\2kr\7%\2\2lm\7\5\2\2mn\5\4\3\2no\7\6\2\2op\7%\2\2")
        buf.write("pr\3\2\2\2qh\3\2\2\2ql\3\2\2\2r\21\3\2\2\2st\5\24\13\2")
        buf.write("tu\7\25\2\2uv\5\22\n\2vy\3\2\2\2wy\5\24\13\2xs\3\2\2\2")
        buf.write("xw\3\2\2\2y\23\3\2\2\2z{\7\5\2\2{|\5\22\n\2|}\7\6\2\2")
        buf.write("}~\7\24\2\2~\177\5\24\13\2\177\u0086\3\2\2\2\u0080\u0081")
        buf.write("\5\26\f\2\u0081\u0082\7\24\2\2\u0082\u0083\5\24\13\2\u0083")
        buf.write("\u0086\3\2\2\2\u0084\u0086\5\26\f\2\u0085z\3\2\2\2\u0085")
        buf.write("\u0080\3\2\2\2\u0085\u0084\3\2\2\2\u0086\25\3\2\2\2\u0087")
        buf.write("\u0088\5\f\7\2\u0088\u0089\5\30\r\2\u0089\u008a\5\f\7")
        buf.write("\2\u008a\u0099\3\2\2\2\u008b\u008c\5\f\7\2\u008c\u008d")
        buf.write("\7\27\2\2\u008d\u008e\7\5\2\2\u008e\u008f\5\4\3\2\u008f")
        buf.write("\u0090\7\6\2\2\u0090\u0099\3\2\2\2\u0091\u0092\5\f\7\2")
        buf.write("\u0092\u0093\7\26\2\2\u0093\u0094\7\27\2\2\u0094\u0095")
        buf.write("\7\5\2\2\u0095\u0096\5\4\3\2\u0096\u0097\7\6\2\2\u0097")
        buf.write("\u0099\3\2\2\2\u0098\u0087\3\2\2\2\u0098\u008b\3\2\2\2")
        buf.write("\u0098\u0091\3\2\2\2\u0099\27\3\2\2\2\u009a\u009b\t\3")
        buf.write("\2\2\u009b\31\3\2\2\2\u009c\u009d\t\4\2\2\u009d\33\3\2")
        buf.write("\2\2\20\36\")-\60BGO[fqx\u0085\u0098")
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
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'='", "'!='", "'<'", "'<='", "'>'", "'>='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "LPAR", "RPAR", 
                      "COLON", "STAR", "QUOTE", "SELECT", "DISTINCT", "FROM", 
                      "WHERE", "AS", "MINUS", "UNION", "JOIN", "GROUPBY", 
                      "ORDERBY", "AND", "OR", "NOT", "IN", "DESC", "ASC", 
                      "MAX", "MIN", "COUNT", "SUM", "EQ", "NEQ", "LT", "LE", 
                      "GT", "GE", "FILENAME", "ID", "WS", "NEWLINE" ]

    RULE_main = 0
    RULE_sql = 1
    RULE_orderby = 2
    RULE_atts = 3
    RULE_attd = 4
    RULE_att = 5
    RULE_rels = 6
    RULE_rel = 7
    RULE_cond = 8
    RULE_and_cond = 9
    RULE_at_cond = 10
    RULE_op = 11
    RULE_aggr = 12

    ruleNames =  [ "main", "sql", "orderby", "atts", "attd", "att", "rels", 
                   "rel", "cond", "and_cond", "at_cond", "op", "aggr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    LPAR=3
    RPAR=4
    COLON=5
    STAR=6
    QUOTE=7
    SELECT=8
    DISTINCT=9
    FROM=10
    WHERE=11
    AS=12
    MINUS=13
    UNION=14
    JOIN=15
    GROUPBY=16
    ORDERBY=17
    AND=18
    OR=19
    NOT=20
    IN=21
    DESC=22
    ASC=23
    MAX=24
    MIN=25
    COUNT=26
    SUM=27
    EQ=28
    NEQ=29
    LT=30
    LE=31
    GT=32
    GE=33
    FILENAME=34
    ID=35
    WS=36
    NEWLINE=37

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
            self.state = 26
            self.sql()
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==miniSQLParser.COLON:
                self.state = 27
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

        def DISTINCT(self):
            return self.getToken(miniSQLParser.DISTINCT, 0)
        def WHERE(self):
            return self.getToken(miniSQLParser.WHERE, 0)
        def cond(self):
            return self.getTypedRuleContext(miniSQLParser.CondContext,0)

        def GROUPBY(self):
            return self.getToken(miniSQLParser.GROUPBY, 0)
        def att(self):
            return self.getTypedRuleContext(miniSQLParser.AttContext,0)

        def orderby(self):
            return self.getTypedRuleContext(miniSQLParser.OrderbyContext,0)


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
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = miniSQLParser.SqlNormalContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.match(miniSQLParser.SELECT)
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miniSQLParser.DISTINCT:
                    self.state = 31
                    self.match(miniSQLParser.DISTINCT)


                self.state = 34
                self.atts()
                self.state = 35
                self.match(miniSQLParser.FROM)
                self.state = 36
                self.rels()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miniSQLParser.WHERE:
                    self.state = 37
                    self.match(miniSQLParser.WHERE)
                    self.state = 38
                    self.cond()


                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miniSQLParser.GROUPBY:
                    self.state = 41
                    self.match(miniSQLParser.GROUPBY)
                    self.state = 42
                    self.att()


                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miniSQLParser.ORDERBY:
                    self.state = 45
                    self.orderby()


                pass

            elif la_ == 2:
                localctx = miniSQLParser.SqlMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.match(miniSQLParser.LPAR)
                self.state = 49
                self.sql()
                self.state = 50
                self.match(miniSQLParser.RPAR)
                self.state = 51
                self.match(miniSQLParser.MINUS)
                self.state = 52
                self.match(miniSQLParser.LPAR)
                self.state = 53
                self.sql()
                self.state = 54
                self.match(miniSQLParser.RPAR)
                pass

            elif la_ == 3:
                localctx = miniSQLParser.SqlUnionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.match(miniSQLParser.LPAR)
                self.state = 57
                self.sql()
                self.state = 58
                self.match(miniSQLParser.RPAR)
                self.state = 59
                self.match(miniSQLParser.UNION)
                self.state = 60
                self.match(miniSQLParser.LPAR)
                self.state = 61
                self.sql()
                self.state = 62
                self.match(miniSQLParser.RPAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OrderbyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return miniSQLParser.RULE_orderby

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class OrderByContext(OrderbyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miniSQLParser.OrderbyContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ORDERBY(self):
            return self.getToken(miniSQLParser.ORDERBY, 0)
        def atts(self):
            return self.getTypedRuleContext(miniSQLParser.AttsContext,0)

        def DESC(self):
            return self.getToken(miniSQLParser.DESC, 0)
        def ASC(self):
            return self.getToken(miniSQLParser.ASC, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrderBy" ):
                return visitor.visitOrderBy(self)
            else:
                return visitor.visitChildren(self)



    def orderby(self):

        localctx = miniSQLParser.OrderbyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_orderby)
        self._la = 0 # Token type
        try:
            localctx = miniSQLParser.OrderByContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(miniSQLParser.ORDERBY)
            self.state = 67
            self.atts()
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==miniSQLParser.DESC or _la==miniSQLParser.ASC:
                self.state = 68
                _la = self._input.LA(1)
                if not(_la==miniSQLParser.DESC or _la==miniSQLParser.ASC):
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
        self.enterRule(localctx, 6, self.RULE_atts)
        try:
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = miniSQLParser.AttributeDeclAllContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.match(miniSQLParser.STAR)
                pass

            elif la_ == 2:
                localctx = miniSQLParser.AttributeDeclListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.attd()
                self.state = 73
                self.match(miniSQLParser.T__0)
                self.state = 74
                self.atts()
                pass

            elif la_ == 3:
                localctx = miniSQLParser.AttributeDeclSimpleContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 76
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


    class AttributeAggrContext(AttdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miniSQLParser.AttdContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def aggr(self):
            return self.getTypedRuleContext(miniSQLParser.AggrContext,0)

        def LPAR(self):
            return self.getToken(miniSQLParser.LPAR, 0)
        def att(self):
            return self.getTypedRuleContext(miniSQLParser.AttContext,0)

        def RPAR(self):
            return self.getToken(miniSQLParser.RPAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributeAggr" ):
                return visitor.visitAttributeAggr(self)
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
        self.enterRule(localctx, 8, self.RULE_attd)
        try:
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = miniSQLParser.AttributeSimpleContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.att()
                pass

            elif la_ == 2:
                localctx = miniSQLParser.AttributeAsContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.att()
                self.state = 81
                self.match(miniSQLParser.AS)
                self.state = 82
                self.match(miniSQLParser.ID)
                pass

            elif la_ == 3:
                localctx = miniSQLParser.AttributeAggrContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 84
                self.aggr()
                self.state = 85
                self.match(miniSQLParser.LPAR)
                self.state = 86
                self.att()
                self.state = 87
                self.match(miniSQLParser.RPAR)
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
        self.enterRule(localctx, 10, self.RULE_att)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(miniSQLParser.ID)
            self.state = 92
            self.match(miniSQLParser.T__1)
            self.state = 93
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
        self.enterRule(localctx, 12, self.RULE_rels)
        try:
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = miniSQLParser.RelationDeclListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.rel()
                self.state = 96
                self.match(miniSQLParser.T__0)
                self.state = 97
                self.rels()
                pass

            elif la_ == 2:
                localctx = miniSQLParser.RelationDeclSimpleContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 99
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


    class RelationSubQueryContext(RelContext):

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
            if hasattr( visitor, "visitRelationSubQuery" ):
                return visitor.visitRelationSubQuery(self)
            else:
                return visitor.visitChildren(self)



    def rel(self):

        localctx = miniSQLParser.RelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_rel)
        try:
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [miniSQLParser.QUOTE]:
                localctx = miniSQLParser.RelationIDContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.match(miniSQLParser.QUOTE)
                self.state = 103
                self.match(miniSQLParser.FILENAME)
                self.state = 104
                self.match(miniSQLParser.QUOTE)
                self.state = 105
                self.match(miniSQLParser.ID)
                pass
            elif token in [miniSQLParser.LPAR]:
                localctx = miniSQLParser.RelationSubQueryContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.match(miniSQLParser.LPAR)
                self.state = 107
                self.sql()
                self.state = 108
                self.match(miniSQLParser.RPAR)
                self.state = 109
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
        self.enterRule(localctx, 16, self.RULE_cond)
        try:
            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                localctx = miniSQLParser.CondOrListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.and_cond()
                self.state = 114
                self.match(miniSQLParser.OR)
                self.state = 115
                self.cond()
                pass

            elif la_ == 2:
                localctx = miniSQLParser.CondOrSimpleContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 117
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
        self.enterRule(localctx, 18, self.RULE_and_cond)
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                localctx = miniSQLParser.CondAndOrContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.match(miniSQLParser.LPAR)
                self.state = 121
                self.cond()
                self.state = 122
                self.match(miniSQLParser.RPAR)
                self.state = 123
                self.match(miniSQLParser.AND)
                self.state = 124
                self.and_cond()
                pass

            elif la_ == 2:
                localctx = miniSQLParser.CondAndListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.at_cond()
                self.state = 127
                self.match(miniSQLParser.AND)
                self.state = 128
                self.and_cond()
                pass

            elif la_ == 3:
                localctx = miniSQLParser.CondAndSimpleContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 130
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
        self.enterRule(localctx, 20, self.RULE_at_cond)
        try:
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = miniSQLParser.CompSimpleContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.att()
                self.state = 134
                self.op()
                self.state = 135
                self.att()
                pass

            elif la_ == 2:
                localctx = miniSQLParser.CompInContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.att()
                self.state = 138
                self.match(miniSQLParser.IN)
                self.state = 139
                self.match(miniSQLParser.LPAR)
                self.state = 140
                self.sql()
                self.state = 141
                self.match(miniSQLParser.RPAR)
                pass

            elif la_ == 3:
                localctx = miniSQLParser.CompNotInContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 143
                self.att()
                self.state = 144
                self.match(miniSQLParser.NOT)
                self.state = 145
                self.match(miniSQLParser.IN)
                self.state = 146
                self.match(miniSQLParser.LPAR)
                self.state = 147
                self.sql()
                self.state = 148
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
        self.enterRule(localctx, 22, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
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

    class AggrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAX(self):
            return self.getToken(miniSQLParser.MAX, 0)

        def MIN(self):
            return self.getToken(miniSQLParser.MIN, 0)

        def COUNT(self):
            return self.getToken(miniSQLParser.COUNT, 0)

        def SUM(self):
            return self.getToken(miniSQLParser.SUM, 0)

        def getRuleIndex(self):
            return miniSQLParser.RULE_aggr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggr" ):
                return visitor.visitAggr(self)
            else:
                return visitor.visitChildren(self)




    def aggr(self):

        localctx = miniSQLParser.AggrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_aggr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miniSQLParser.MAX) | (1 << miniSQLParser.MIN) | (1 << miniSQLParser.COUNT) | (1 << miniSQLParser.SUM))) != 0)):
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






# Generated from src/parser/miniSQL.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\'")
        buf.write("\u00d0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\5\2#\n\2\3\3\3\3\5\3")
        buf.write("\'\n\3\3\3\3\3\3\3\3\3\3\3\5\3.\n\3\3\3\5\3\61\n\3\3\3")
        buf.write("\3\3\5\3\65\n\3\3\3\3\3\3\3\3\3\3\3\5\3<\n\3\3\3\3\3\3")
        buf.write("\3\5\3A\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\5\3S\n\3\3\4\3\4\3\4\5\4X\n\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\5\5`\n\5\3\6\3\6\3\6\3\6\3\6\5")
        buf.write("\6g\n\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\5\b\u0083\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\5\t\u0091\n\t\3\n\3\n\3\n\3\n\3\n\5\n\u0098")
        buf.write("\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13")
        buf.write("\u00a3\n\13\3\f\3\f\3\f\3\f\3\f\5\f\u00aa\n\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00b7\n\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\5\16\u00ca\n\16\3\17\3\17\3")
        buf.write("\20\3\20\3\20\2\2\21\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36\2\5\3\2\30\31\3\2\36#\3\2\32\35\2\u00da\2 \3\2")
        buf.write("\2\2\4R\3\2\2\2\6T\3\2\2\2\b_\3\2\2\2\nf\3\2\2\2\fh\3")
        buf.write("\2\2\2\16\u0082\3\2\2\2\20\u0090\3\2\2\2\22\u0097\3\2")
        buf.write("\2\2\24\u00a2\3\2\2\2\26\u00a9\3\2\2\2\30\u00b6\3\2\2")
        buf.write("\2\32\u00c9\3\2\2\2\34\u00cb\3\2\2\2\36\u00cd\3\2\2\2")
        buf.write(" \"\5\4\3\2!#\7\7\2\2\"!\3\2\2\2\"#\3\2\2\2#\3\3\2\2\2")
        buf.write("$&\7\n\2\2%\'\7\13\2\2&%\3\2\2\2&\'\3\2\2\2\'(\3\2\2\2")
        buf.write("()\5\b\5\2)*\7\f\2\2*-\5\22\n\2+,\7\r\2\2,.\5\26\f\2-")
        buf.write("+\3\2\2\2-.\3\2\2\2.\60\3\2\2\2/\61\5\6\4\2\60/\3\2\2")
        buf.write("\2\60\61\3\2\2\2\61S\3\2\2\2\62\64\7\n\2\2\63\65\7\13")
        buf.write("\2\2\64\63\3\2\2\2\64\65\3\2\2\2\65\66\3\2\2\2\66\67\5")
        buf.write("\16\b\2\678\7\f\2\28;\5\22\n\29:\7\r\2\2:<\5\26\f\2;9")
        buf.write("\3\2\2\2;<\3\2\2\2<=\3\2\2\2=>\7\22\2\2>@\5\f\7\2?A\5")
        buf.write("\6\4\2@?\3\2\2\2@A\3\2\2\2AS\3\2\2\2BC\7\5\2\2CD\5\4\3")
        buf.write("\2DE\7\6\2\2EF\7\17\2\2FG\7\5\2\2GH\5\4\3\2HI\7\6\2\2")
        buf.write("IS\3\2\2\2JK\7\5\2\2KL\5\4\3\2LM\7\6\2\2MN\7\20\2\2NO")
        buf.write("\7\5\2\2OP\5\4\3\2PQ\7\6\2\2QS\3\2\2\2R$\3\2\2\2R\62\3")
        buf.write("\2\2\2RB\3\2\2\2RJ\3\2\2\2S\5\3\2\2\2TU\7\23\2\2UW\5\b")
        buf.write("\5\2VX\t\2\2\2WV\3\2\2\2WX\3\2\2\2X\7\3\2\2\2Y`\7\b\2")
        buf.write("\2Z[\5\n\6\2[\\\7\3\2\2\\]\5\b\5\2]`\3\2\2\2^`\5\n\6\2")
        buf.write("_Y\3\2\2\2_Z\3\2\2\2_^\3\2\2\2`\t\3\2\2\2ag\5\f\7\2bc")
        buf.write("\5\f\7\2cd\7\16\2\2de\7%\2\2eg\3\2\2\2fa\3\2\2\2fb\3\2")
        buf.write("\2\2g\13\3\2\2\2hi\7%\2\2ij\7\4\2\2jk\7%\2\2k\r\3\2\2")
        buf.write("\2l\u0083\5\f\7\2mn\5\f\7\2no\7\3\2\2op\5\20\t\2p\u0083")
        buf.write("\3\2\2\2qr\5\f\7\2rs\7\16\2\2st\7%\2\2t\u0083\3\2\2\2")
        buf.write("uv\5\f\7\2vw\7\16\2\2wx\7%\2\2xy\7\3\2\2yz\5\20\t\2z\u0083")
        buf.write("\3\2\2\2{|\5\36\20\2|}\7\5\2\2}~\5\f\7\2~\177\7\6\2\2")
        buf.write("\177\u0080\7\3\2\2\u0080\u0081\5\16\b\2\u0081\u0083\3")
        buf.write("\2\2\2\u0082l\3\2\2\2\u0082m\3\2\2\2\u0082q\3\2\2\2\u0082")
        buf.write("u\3\2\2\2\u0082{\3\2\2\2\u0083\17\3\2\2\2\u0084\u0085")
        buf.write("\5\36\20\2\u0085\u0086\7\5\2\2\u0086\u0087\5\f\7\2\u0087")
        buf.write("\u0088\7\6\2\2\u0088\u0091\3\2\2\2\u0089\u008a\5\36\20")
        buf.write("\2\u008a\u008b\7\5\2\2\u008b\u008c\5\f\7\2\u008c\u008d")
        buf.write("\7\6\2\2\u008d\u008e\7\3\2\2\u008e\u008f\5\20\t\2\u008f")
        buf.write("\u0091\3\2\2\2\u0090\u0084\3\2\2\2\u0090\u0089\3\2\2\2")
        buf.write("\u0091\21\3\2\2\2\u0092\u0093\5\24\13\2\u0093\u0094\7")
        buf.write("\3\2\2\u0094\u0095\5\22\n\2\u0095\u0098\3\2\2\2\u0096")
        buf.write("\u0098\5\24\13\2\u0097\u0092\3\2\2\2\u0097\u0096\3\2\2")
        buf.write("\2\u0098\23\3\2\2\2\u0099\u009a\7\t\2\2\u009a\u009b\7")
        buf.write("$\2\2\u009b\u009c\7\t\2\2\u009c\u00a3\7%\2\2\u009d\u009e")
        buf.write("\7\5\2\2\u009e\u009f\5\4\3\2\u009f\u00a0\7\6\2\2\u00a0")
        buf.write("\u00a1\7%\2\2\u00a1\u00a3\3\2\2\2\u00a2\u0099\3\2\2\2")
        buf.write("\u00a2\u009d\3\2\2\2\u00a3\25\3\2\2\2\u00a4\u00a5\5\30")
        buf.write("\r\2\u00a5\u00a6\7\25\2\2\u00a6\u00a7\5\26\f\2\u00a7\u00aa")
        buf.write("\3\2\2\2\u00a8\u00aa\5\30\r\2\u00a9\u00a4\3\2\2\2\u00a9")
        buf.write("\u00a8\3\2\2\2\u00aa\27\3\2\2\2\u00ab\u00ac\7\5\2\2\u00ac")
        buf.write("\u00ad\5\26\f\2\u00ad\u00ae\7\6\2\2\u00ae\u00af\7\24\2")
        buf.write("\2\u00af\u00b0\5\30\r\2\u00b0\u00b7\3\2\2\2\u00b1\u00b2")
        buf.write("\5\32\16\2\u00b2\u00b3\7\24\2\2\u00b3\u00b4\5\30\r\2\u00b4")
        buf.write("\u00b7\3\2\2\2\u00b5\u00b7\5\32\16\2\u00b6\u00ab\3\2\2")
        buf.write("\2\u00b6\u00b1\3\2\2\2\u00b6\u00b5\3\2\2\2\u00b7\31\3")
        buf.write("\2\2\2\u00b8\u00b9\5\f\7\2\u00b9\u00ba\5\34\17\2\u00ba")
        buf.write("\u00bb\5\f\7\2\u00bb\u00ca\3\2\2\2\u00bc\u00bd\5\f\7\2")
        buf.write("\u00bd\u00be\7\27\2\2\u00be\u00bf\7\5\2\2\u00bf\u00c0")
        buf.write("\5\4\3\2\u00c0\u00c1\7\6\2\2\u00c1\u00ca\3\2\2\2\u00c2")
        buf.write("\u00c3\5\f\7\2\u00c3\u00c4\7\26\2\2\u00c4\u00c5\7\27\2")
        buf.write("\2\u00c5\u00c6\7\5\2\2\u00c6\u00c7\5\4\3\2\u00c7\u00c8")
        buf.write("\7\6\2\2\u00c8\u00ca\3\2\2\2\u00c9\u00b8\3\2\2\2\u00c9")
        buf.write("\u00bc\3\2\2\2\u00c9\u00c2\3\2\2\2\u00ca\33\3\2\2\2\u00cb")
        buf.write("\u00cc\t\3\2\2\u00cc\35\3\2\2\2\u00cd\u00ce\t\4\2\2\u00ce")
        buf.write("\37\3\2\2\2\24\"&-\60\64;@RW_f\u0082\u0090\u0097\u00a2")
        buf.write("\u00a9\u00b6\u00c9")
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
    RULE_attgrp = 6
    RULE_attgrpbis = 7
    RULE_rels = 8
    RULE_rel = 9
    RULE_cond = 10
    RULE_and_cond = 11
    RULE_at_cond = 12
    RULE_op = 13
    RULE_aggr = 14

    ruleNames =  [ "main", "sql", "orderby", "atts", "attd", "att", "attgrp", 
                   "attgrpbis", "rels", "rel", "cond", "and_cond", "at_cond", 
                   "op", "aggr" ]

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
            self.state = 30
            self.sql()
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==miniSQLParser.COLON:
                self.state = 31
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

        def orderby(self):
            return self.getTypedRuleContext(miniSQLParser.OrderbyContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSqlNormal" ):
                return visitor.visitSqlNormal(self)
            else:
                return visitor.visitChildren(self)


    class SqlGroupByContext(SqlContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miniSQLParser.SqlContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SELECT(self):
            return self.getToken(miniSQLParser.SELECT, 0)
        def attgrp(self):
            return self.getTypedRuleContext(miniSQLParser.AttgrpContext,0)

        def FROM(self):
            return self.getToken(miniSQLParser.FROM, 0)
        def rels(self):
            return self.getTypedRuleContext(miniSQLParser.RelsContext,0)

        def GROUPBY(self):
            return self.getToken(miniSQLParser.GROUPBY, 0)
        def att(self):
            return self.getTypedRuleContext(miniSQLParser.AttContext,0)

        def DISTINCT(self):
            return self.getToken(miniSQLParser.DISTINCT, 0)
        def WHERE(self):
            return self.getToken(miniSQLParser.WHERE, 0)
        def cond(self):
            return self.getTypedRuleContext(miniSQLParser.CondContext,0)

        def orderby(self):
            return self.getTypedRuleContext(miniSQLParser.OrderbyContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSqlGroupBy" ):
                return visitor.visitSqlGroupBy(self)
            else:
                return visitor.visitChildren(self)



    def sql(self):

        localctx = miniSQLParser.SqlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sql)
        self._la = 0 # Token type
        try:
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = miniSQLParser.SqlNormalContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.match(miniSQLParser.SELECT)
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miniSQLParser.DISTINCT:
                    self.state = 35
                    self.match(miniSQLParser.DISTINCT)


                self.state = 38
                self.atts()
                self.state = 39
                self.match(miniSQLParser.FROM)
                self.state = 40
                self.rels()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miniSQLParser.WHERE:
                    self.state = 41
                    self.match(miniSQLParser.WHERE)
                    self.state = 42
                    self.cond()


                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miniSQLParser.ORDERBY:
                    self.state = 45
                    self.orderby()


                pass

            elif la_ == 2:
                localctx = miniSQLParser.SqlGroupByContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.match(miniSQLParser.SELECT)
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miniSQLParser.DISTINCT:
                    self.state = 49
                    self.match(miniSQLParser.DISTINCT)


                self.state = 52
                self.attgrp()
                self.state = 53
                self.match(miniSQLParser.FROM)
                self.state = 54
                self.rels()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miniSQLParser.WHERE:
                    self.state = 55
                    self.match(miniSQLParser.WHERE)
                    self.state = 56
                    self.cond()


                self.state = 59
                self.match(miniSQLParser.GROUPBY)
                self.state = 60
                self.att()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miniSQLParser.ORDERBY:
                    self.state = 61
                    self.orderby()


                pass

            elif la_ == 3:
                localctx = miniSQLParser.SqlMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.match(miniSQLParser.LPAR)
                self.state = 65
                self.sql()
                self.state = 66
                self.match(miniSQLParser.RPAR)
                self.state = 67
                self.match(miniSQLParser.MINUS)
                self.state = 68
                self.match(miniSQLParser.LPAR)
                self.state = 69
                self.sql()
                self.state = 70
                self.match(miniSQLParser.RPAR)
                pass

            elif la_ == 4:
                localctx = miniSQLParser.SqlUnionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 72
                self.match(miniSQLParser.LPAR)
                self.state = 73
                self.sql()
                self.state = 74
                self.match(miniSQLParser.RPAR)
                self.state = 75
                self.match(miniSQLParser.UNION)
                self.state = 76
                self.match(miniSQLParser.LPAR)
                self.state = 77
                self.sql()
                self.state = 78
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
            self.state = 82
            self.match(miniSQLParser.ORDERBY)
            self.state = 83
            self.atts()
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==miniSQLParser.DESC or _la==miniSQLParser.ASC:
                self.state = 84
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
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = miniSQLParser.AttributeDeclAllContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.match(miniSQLParser.STAR)
                pass

            elif la_ == 2:
                localctx = miniSQLParser.AttributeDeclListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.attd()
                self.state = 89
                self.match(miniSQLParser.T__0)
                self.state = 90
                self.atts()
                pass

            elif la_ == 3:
                localctx = miniSQLParser.AttributeDeclSimpleContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 92
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
        self.enterRule(localctx, 8, self.RULE_attd)
        try:
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = miniSQLParser.AttributeSimpleContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.att()
                pass

            elif la_ == 2:
                localctx = miniSQLParser.AttributeAsContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.att()
                self.state = 97
                self.match(miniSQLParser.AS)
                self.state = 98
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
        self.enterRule(localctx, 10, self.RULE_att)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(miniSQLParser.ID)
            self.state = 103
            self.match(miniSQLParser.T__1)
            self.state = 104
            self.match(miniSQLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AttgrpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def att(self):
            return self.getTypedRuleContext(miniSQLParser.AttContext,0)


        def attgrpbis(self):
            return self.getTypedRuleContext(miniSQLParser.AttgrpbisContext,0)


        def AS(self):
            return self.getToken(miniSQLParser.AS, 0)

        def ID(self):
            return self.getToken(miniSQLParser.ID, 0)

        def aggr(self):
            return self.getTypedRuleContext(miniSQLParser.AggrContext,0)


        def LPAR(self):
            return self.getToken(miniSQLParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(miniSQLParser.RPAR, 0)

        def attgrp(self):
            return self.getTypedRuleContext(miniSQLParser.AttgrpContext,0)


        def getRuleIndex(self):
            return miniSQLParser.RULE_attgrp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttgrp" ):
                return visitor.visitAttgrp(self)
            else:
                return visitor.visitChildren(self)




    def attgrp(self):

        localctx = miniSQLParser.AttgrpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attgrp)
        try:
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.att()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.att()
                self.state = 108
                self.match(miniSQLParser.T__0)
                self.state = 109
                self.attgrpbis()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 111
                self.att()
                self.state = 112
                self.match(miniSQLParser.AS)
                self.state = 113
                self.match(miniSQLParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 115
                self.att()
                self.state = 116
                self.match(miniSQLParser.AS)
                self.state = 117
                self.match(miniSQLParser.ID)
                self.state = 118
                self.match(miniSQLParser.T__0)
                self.state = 119
                self.attgrpbis()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 121
                self.aggr()
                self.state = 122
                self.match(miniSQLParser.LPAR)
                self.state = 123
                self.att()
                self.state = 124
                self.match(miniSQLParser.RPAR)
                self.state = 125
                self.match(miniSQLParser.T__0)
                self.state = 126
                self.attgrp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AttgrpbisContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aggr(self):
            return self.getTypedRuleContext(miniSQLParser.AggrContext,0)


        def LPAR(self):
            return self.getToken(miniSQLParser.LPAR, 0)

        def att(self):
            return self.getTypedRuleContext(miniSQLParser.AttContext,0)


        def RPAR(self):
            return self.getToken(miniSQLParser.RPAR, 0)

        def attgrpbis(self):
            return self.getTypedRuleContext(miniSQLParser.AttgrpbisContext,0)


        def getRuleIndex(self):
            return miniSQLParser.RULE_attgrpbis

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttgrpbis" ):
                return visitor.visitAttgrpbis(self)
            else:
                return visitor.visitChildren(self)




    def attgrpbis(self):

        localctx = miniSQLParser.AttgrpbisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attgrpbis)
        try:
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.aggr()
                self.state = 131
                self.match(miniSQLParser.LPAR)
                self.state = 132
                self.att()
                self.state = 133
                self.match(miniSQLParser.RPAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.aggr()
                self.state = 136
                self.match(miniSQLParser.LPAR)
                self.state = 137
                self.att()
                self.state = 138
                self.match(miniSQLParser.RPAR)
                self.state = 139
                self.match(miniSQLParser.T__0)
                self.state = 140
                self.attgrpbis()
                pass


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
        self.enterRule(localctx, 16, self.RULE_rels)
        try:
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = miniSQLParser.RelationDeclListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.rel()
                self.state = 145
                self.match(miniSQLParser.T__0)
                self.state = 146
                self.rels()
                pass

            elif la_ == 2:
                localctx = miniSQLParser.RelationDeclSimpleContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 148
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
        self.enterRule(localctx, 18, self.RULE_rel)
        try:
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [miniSQLParser.QUOTE]:
                localctx = miniSQLParser.RelationIDContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.match(miniSQLParser.QUOTE)
                self.state = 152
                self.match(miniSQLParser.FILENAME)
                self.state = 153
                self.match(miniSQLParser.QUOTE)
                self.state = 154
                self.match(miniSQLParser.ID)
                pass
            elif token in [miniSQLParser.LPAR]:
                localctx = miniSQLParser.SubqueryContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.match(miniSQLParser.LPAR)
                self.state = 156
                self.sql()
                self.state = 157
                self.match(miniSQLParser.RPAR)
                self.state = 158
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
        self.enterRule(localctx, 20, self.RULE_cond)
        try:
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                localctx = miniSQLParser.CondOrListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.and_cond()
                self.state = 163
                self.match(miniSQLParser.OR)
                self.state = 164
                self.cond()
                pass

            elif la_ == 2:
                localctx = miniSQLParser.CondOrSimpleContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 166
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
        self.enterRule(localctx, 22, self.RULE_and_cond)
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                localctx = miniSQLParser.CondAndOrContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.match(miniSQLParser.LPAR)
                self.state = 170
                self.cond()
                self.state = 171
                self.match(miniSQLParser.RPAR)
                self.state = 172
                self.match(miniSQLParser.AND)
                self.state = 173
                self.and_cond()
                pass

            elif la_ == 2:
                localctx = miniSQLParser.CondAndListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.at_cond()
                self.state = 176
                self.match(miniSQLParser.AND)
                self.state = 177
                self.and_cond()
                pass

            elif la_ == 3:
                localctx = miniSQLParser.CondAndSimpleContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 179
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
        self.enterRule(localctx, 24, self.RULE_at_cond)
        try:
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                localctx = miniSQLParser.CompSimpleContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.att()
                self.state = 183
                self.op()
                self.state = 184
                self.att()
                pass

            elif la_ == 2:
                localctx = miniSQLParser.CompInContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.att()
                self.state = 187
                self.match(miniSQLParser.IN)
                self.state = 188
                self.match(miniSQLParser.LPAR)
                self.state = 189
                self.sql()
                self.state = 190
                self.match(miniSQLParser.RPAR)
                pass

            elif la_ == 3:
                localctx = miniSQLParser.CompNotInContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 192
                self.att()
                self.state = 193
                self.match(miniSQLParser.NOT)
                self.state = 194
                self.match(miniSQLParser.IN)
                self.state = 195
                self.match(miniSQLParser.LPAR)
                self.state = 196
                self.sql()
                self.state = 197
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
        self.enterRule(localctx, 26, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
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
        self.enterRule(localctx, 28, self.RULE_aggr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
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






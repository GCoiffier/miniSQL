# Generated from src/parser/miniSQL.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\'")
        buf.write("\u00cb\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\5\2!\n\2\3\3\3\3\5\3%\n\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\5\3,\n\3\3\3\3\3\3\3\5\3\61\n\3\5\3\63")
        buf.write("\n\3\3\3\3\3\5\3\67\n\3\3\3\3\3\3\3\3\3\3\3\5\3>\n\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\5\3S\n\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\5\4[\n\4\3\5\3\5\3\5\3\5\3\5\5\5b\n\5\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7~\n\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u008c\n\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\5\t\u0093\n\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\5\n\u009e\n\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\5\13\u00a5\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\5\f\u00b2\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00c5\n\r\3\16")
        buf.write("\3\16\3\17\3\17\3\17\2\2\20\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\2\5\3\2\30\31\3\2\36#\3\2\32\35\2\u00d5\2\36")
        buf.write("\3\2\2\2\4R\3\2\2\2\6Z\3\2\2\2\ba\3\2\2\2\nc\3\2\2\2\f")
        buf.write("}\3\2\2\2\16\u008b\3\2\2\2\20\u0092\3\2\2\2\22\u009d\3")
        buf.write("\2\2\2\24\u00a4\3\2\2\2\26\u00b1\3\2\2\2\30\u00c4\3\2")
        buf.write("\2\2\32\u00c6\3\2\2\2\34\u00c8\3\2\2\2\36 \5\4\3\2\37")
        buf.write("!\7\7\2\2 \37\3\2\2\2 !\3\2\2\2!\3\3\2\2\2\"$\7\n\2\2")
        buf.write("#%\7\13\2\2$#\3\2\2\2$%\3\2\2\2%&\3\2\2\2&\'\5\6\4\2\'")
        buf.write("(\7\f\2\2(+\5\20\t\2)*\7\r\2\2*,\5\24\13\2+)\3\2\2\2+")
        buf.write(",\3\2\2\2,\62\3\2\2\2-.\7\23\2\2.\60\5\n\6\2/\61\t\2\2")
        buf.write("\2\60/\3\2\2\2\60\61\3\2\2\2\61\63\3\2\2\2\62-\3\2\2\2")
        buf.write("\62\63\3\2\2\2\63S\3\2\2\2\64\66\7\n\2\2\65\67\7\13\2")
        buf.write("\2\66\65\3\2\2\2\66\67\3\2\2\2\678\3\2\2\289\5\f\7\29")
        buf.write(":\7\f\2\2:=\5\20\t\2;<\7\r\2\2<>\5\24\13\2=;\3\2\2\2=")
        buf.write(">\3\2\2\2>?\3\2\2\2?@\7\22\2\2@A\5\n\6\2AS\3\2\2\2BC\7")
        buf.write("\5\2\2CD\5\4\3\2DE\7\6\2\2EF\7\17\2\2FG\7\5\2\2GH\5\4")
        buf.write("\3\2HI\7\6\2\2IS\3\2\2\2JK\7\5\2\2KL\5\4\3\2LM\7\6\2\2")
        buf.write("MN\7\20\2\2NO\7\5\2\2OP\5\4\3\2PQ\7\6\2\2QS\3\2\2\2R\"")
        buf.write("\3\2\2\2R\64\3\2\2\2RB\3\2\2\2RJ\3\2\2\2S\5\3\2\2\2T[")
        buf.write("\7\b\2\2UV\5\b\5\2VW\7\3\2\2WX\5\6\4\2X[\3\2\2\2Y[\5\b")
        buf.write("\5\2ZT\3\2\2\2ZU\3\2\2\2ZY\3\2\2\2[\7\3\2\2\2\\b\5\n\6")
        buf.write("\2]^\5\n\6\2^_\7\16\2\2_`\7%\2\2`b\3\2\2\2a\\\3\2\2\2")
        buf.write("a]\3\2\2\2b\t\3\2\2\2cd\7%\2\2de\7\4\2\2ef\7%\2\2f\13")
        buf.write("\3\2\2\2g~\5\n\6\2hi\5\n\6\2ij\7\3\2\2jk\5\16\b\2k~\3")
        buf.write("\2\2\2lm\5\n\6\2mn\7\16\2\2no\7%\2\2o~\3\2\2\2pq\5\n\6")
        buf.write("\2qr\7\16\2\2rs\7%\2\2st\7\3\2\2tu\5\16\b\2u~\3\2\2\2")
        buf.write("vw\5\34\17\2wx\7\5\2\2xy\5\n\6\2yz\7\6\2\2z{\7\3\2\2{")
        buf.write("|\5\f\7\2|~\3\2\2\2}g\3\2\2\2}h\3\2\2\2}l\3\2\2\2}p\3")
        buf.write("\2\2\2}v\3\2\2\2~\r\3\2\2\2\177\u0080\5\34\17\2\u0080")
        buf.write("\u0081\7\5\2\2\u0081\u0082\5\n\6\2\u0082\u0083\7\6\2\2")
        buf.write("\u0083\u008c\3\2\2\2\u0084\u0085\5\34\17\2\u0085\u0086")
        buf.write("\7\5\2\2\u0086\u0087\5\n\6\2\u0087\u0088\7\6\2\2\u0088")
        buf.write("\u0089\7\3\2\2\u0089\u008a\5\16\b\2\u008a\u008c\3\2\2")
        buf.write("\2\u008b\177\3\2\2\2\u008b\u0084\3\2\2\2\u008c\17\3\2")
        buf.write("\2\2\u008d\u008e\5\22\n\2\u008e\u008f\7\3\2\2\u008f\u0090")
        buf.write("\5\20\t\2\u0090\u0093\3\2\2\2\u0091\u0093\5\22\n\2\u0092")
        buf.write("\u008d\3\2\2\2\u0092\u0091\3\2\2\2\u0093\21\3\2\2\2\u0094")
        buf.write("\u0095\7\t\2\2\u0095\u0096\7$\2\2\u0096\u0097\7\t\2\2")
        buf.write("\u0097\u009e\7%\2\2\u0098\u0099\7\5\2\2\u0099\u009a\5")
        buf.write("\4\3\2\u009a\u009b\7\6\2\2\u009b\u009c\7%\2\2\u009c\u009e")
        buf.write("\3\2\2\2\u009d\u0094\3\2\2\2\u009d\u0098\3\2\2\2\u009e")
        buf.write("\23\3\2\2\2\u009f\u00a0\5\26\f\2\u00a0\u00a1\7\25\2\2")
        buf.write("\u00a1\u00a2\5\24\13\2\u00a2\u00a5\3\2\2\2\u00a3\u00a5")
        buf.write("\5\26\f\2\u00a4\u009f\3\2\2\2\u00a4\u00a3\3\2\2\2\u00a5")
        buf.write("\25\3\2\2\2\u00a6\u00a7\7\5\2\2\u00a7\u00a8\5\24\13\2")
        buf.write("\u00a8\u00a9\7\6\2\2\u00a9\u00aa\7\24\2\2\u00aa\u00ab")
        buf.write("\5\26\f\2\u00ab\u00b2\3\2\2\2\u00ac\u00ad\5\30\r\2\u00ad")
        buf.write("\u00ae\7\24\2\2\u00ae\u00af\5\26\f\2\u00af\u00b2\3\2\2")
        buf.write("\2\u00b0\u00b2\5\30\r\2\u00b1\u00a6\3\2\2\2\u00b1\u00ac")
        buf.write("\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2\27\3\2\2\2\u00b3\u00b4")
        buf.write("\5\n\6\2\u00b4\u00b5\5\32\16\2\u00b5\u00b6\5\n\6\2\u00b6")
        buf.write("\u00c5\3\2\2\2\u00b7\u00b8\5\n\6\2\u00b8\u00b9\7\27\2")
        buf.write("\2\u00b9\u00ba\7\5\2\2\u00ba\u00bb\5\4\3\2\u00bb\u00bc")
        buf.write("\7\6\2\2\u00bc\u00c5\3\2\2\2\u00bd\u00be\5\n\6\2\u00be")
        buf.write("\u00bf\7\26\2\2\u00bf\u00c0\7\27\2\2\u00c0\u00c1\7\5\2")
        buf.write("\2\u00c1\u00c2\5\4\3\2\u00c2\u00c3\7\6\2\2\u00c3\u00c5")
        buf.write("\3\2\2\2\u00c4\u00b3\3\2\2\2\u00c4\u00b7\3\2\2\2\u00c4")
        buf.write("\u00bd\3\2\2\2\u00c5\31\3\2\2\2\u00c6\u00c7\t\3\2\2\u00c7")
        buf.write("\33\3\2\2\2\u00c8\u00c9\t\4\2\2\u00c9\35\3\2\2\2\23 $")
        buf.write("+\60\62\66=RZa}\u008b\u0092\u009d\u00a4\u00b1\u00c4")
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
    RULE_atts = 2
    RULE_attd = 3
    RULE_att = 4
    RULE_attgrp = 5
    RULE_attgrpbis = 6
    RULE_rels = 7
    RULE_rel = 8
    RULE_cond = 9
    RULE_and_cond = 10
    RULE_at_cond = 11
    RULE_op = 12
    RULE_aggr = 13

    ruleNames =  [ "main", "sql", "atts", "attd", "att", "attgrp", "attgrpbis", 
                   "rels", "rel", "cond", "and_cond", "at_cond", "op", "aggr" ]

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
            self.state = 28
            self.sql()
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==miniSQLParser.COLON:
                self.state = 29
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

        def ORDERBY(self):
            return self.getToken(miniSQLParser.ORDERBY, 0)
        def att(self):
            return self.getTypedRuleContext(miniSQLParser.AttContext,0)

        def DESC(self):
            return self.getToken(miniSQLParser.DESC, 0)
        def ASC(self):
            return self.getToken(miniSQLParser.ASC, 0)

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
                self.state = 32
                self.match(miniSQLParser.SELECT)
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miniSQLParser.DISTINCT:
                    self.state = 33
                    self.match(miniSQLParser.DISTINCT)


                self.state = 36
                self.atts()
                self.state = 37
                self.match(miniSQLParser.FROM)
                self.state = 38
                self.rels()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miniSQLParser.WHERE:
                    self.state = 39
                    self.match(miniSQLParser.WHERE)
                    self.state = 40
                    self.cond()


                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miniSQLParser.ORDERBY:
                    self.state = 43
                    self.match(miniSQLParser.ORDERBY)
                    self.state = 44
                    self.att()
                    self.state = 46
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==miniSQLParser.DESC or _la==miniSQLParser.ASC:
                        self.state = 45
                        _la = self._input.LA(1)
                        if not(_la==miniSQLParser.DESC or _la==miniSQLParser.ASC):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()




                pass

            elif la_ == 2:
                localctx = miniSQLParser.SqlGroupByContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.match(miniSQLParser.SELECT)
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miniSQLParser.DISTINCT:
                    self.state = 51
                    self.match(miniSQLParser.DISTINCT)


                self.state = 54
                self.attgrp()
                self.state = 55
                self.match(miniSQLParser.FROM)
                self.state = 56
                self.rels()
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miniSQLParser.WHERE:
                    self.state = 57
                    self.match(miniSQLParser.WHERE)
                    self.state = 58
                    self.cond()


                self.state = 61
                self.match(miniSQLParser.GROUPBY)
                self.state = 62
                self.att()
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
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = miniSQLParser.AttributeDeclAllContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.match(miniSQLParser.STAR)
                pass

            elif la_ == 2:
                localctx = miniSQLParser.AttributeDeclListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.attd()
                self.state = 84
                self.match(miniSQLParser.T__0)
                self.state = 85
                self.atts()
                pass

            elif la_ == 3:
                localctx = miniSQLParser.AttributeDeclSimpleContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 87
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
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = miniSQLParser.AttributeSimpleContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.att()
                pass

            elif la_ == 2:
                localctx = miniSQLParser.AttributeAsContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.att()
                self.state = 92
                self.match(miniSQLParser.AS)
                self.state = 93
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
            self.state = 97
            self.match(miniSQLParser.ID)
            self.state = 98
            self.match(miniSQLParser.T__1)
            self.state = 99
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
        self.enterRule(localctx, 10, self.RULE_attgrp)
        try:
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.att()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.att()
                self.state = 103
                self.match(miniSQLParser.T__0)
                self.state = 104
                self.attgrpbis()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 106
                self.att()
                self.state = 107
                self.match(miniSQLParser.AS)
                self.state = 108
                self.match(miniSQLParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 110
                self.att()
                self.state = 111
                self.match(miniSQLParser.AS)
                self.state = 112
                self.match(miniSQLParser.ID)
                self.state = 113
                self.match(miniSQLParser.T__0)
                self.state = 114
                self.attgrpbis()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 116
                self.aggr()
                self.state = 117
                self.match(miniSQLParser.LPAR)
                self.state = 118
                self.att()
                self.state = 119
                self.match(miniSQLParser.RPAR)
                self.state = 120
                self.match(miniSQLParser.T__0)
                self.state = 121
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
        self.enterRule(localctx, 12, self.RULE_attgrpbis)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.aggr()
                self.state = 126
                self.match(miniSQLParser.LPAR)
                self.state = 127
                self.att()
                self.state = 128
                self.match(miniSQLParser.RPAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.aggr()
                self.state = 131
                self.match(miniSQLParser.LPAR)
                self.state = 132
                self.att()
                self.state = 133
                self.match(miniSQLParser.RPAR)
                self.state = 134
                self.match(miniSQLParser.T__0)
                self.state = 135
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
        self.enterRule(localctx, 14, self.RULE_rels)
        try:
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                localctx = miniSQLParser.RelationDeclListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.rel()
                self.state = 140
                self.match(miniSQLParser.T__0)
                self.state = 141
                self.rels()
                pass

            elif la_ == 2:
                localctx = miniSQLParser.RelationDeclSimpleContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 143
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
        self.enterRule(localctx, 16, self.RULE_rel)
        try:
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [miniSQLParser.QUOTE]:
                localctx = miniSQLParser.RelationIDContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.match(miniSQLParser.QUOTE)
                self.state = 147
                self.match(miniSQLParser.FILENAME)
                self.state = 148
                self.match(miniSQLParser.QUOTE)
                self.state = 149
                self.match(miniSQLParser.ID)
                pass
            elif token in [miniSQLParser.LPAR]:
                localctx = miniSQLParser.SubqueryContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.match(miniSQLParser.LPAR)
                self.state = 151
                self.sql()
                self.state = 152
                self.match(miniSQLParser.RPAR)
                self.state = 153
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
        self.enterRule(localctx, 18, self.RULE_cond)
        try:
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = miniSQLParser.CondOrListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.and_cond()
                self.state = 158
                self.match(miniSQLParser.OR)
                self.state = 159
                self.cond()
                pass

            elif la_ == 2:
                localctx = miniSQLParser.CondOrSimpleContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 161
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
        self.enterRule(localctx, 20, self.RULE_and_cond)
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                localctx = miniSQLParser.CondAndOrContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.match(miniSQLParser.LPAR)
                self.state = 165
                self.cond()
                self.state = 166
                self.match(miniSQLParser.RPAR)
                self.state = 167
                self.match(miniSQLParser.AND)
                self.state = 168
                self.and_cond()
                pass

            elif la_ == 2:
                localctx = miniSQLParser.CondAndListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.at_cond()
                self.state = 171
                self.match(miniSQLParser.AND)
                self.state = 172
                self.and_cond()
                pass

            elif la_ == 3:
                localctx = miniSQLParser.CondAndSimpleContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 174
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
        self.enterRule(localctx, 22, self.RULE_at_cond)
        try:
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                localctx = miniSQLParser.CompSimpleContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.att()
                self.state = 178
                self.op()
                self.state = 179
                self.att()
                pass

            elif la_ == 2:
                localctx = miniSQLParser.CompInContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.att()
                self.state = 182
                self.match(miniSQLParser.IN)
                self.state = 183
                self.match(miniSQLParser.LPAR)
                self.state = 184
                self.sql()
                self.state = 185
                self.match(miniSQLParser.RPAR)
                pass

            elif la_ == 3:
                localctx = miniSQLParser.CompNotInContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 187
                self.att()
                self.state = 188
                self.match(miniSQLParser.NOT)
                self.state = 189
                self.match(miniSQLParser.IN)
                self.state = 190
                self.match(miniSQLParser.LPAR)
                self.state = 191
                self.sql()
                self.state = 192
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
        self.enterRule(localctx, 24, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
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
        self.enterRule(localctx, 26, self.RULE_aggr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
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






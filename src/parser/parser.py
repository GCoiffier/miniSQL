# Generated from src/parser/miniSQL.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\34")
        buf.write("v\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\5\2.\n\2\3\3\3\3\3\3\3\3\3\3\5\3\65\n\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\5\4<\n\4\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\5\6G\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\5\7Q\n\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\5\tZ\n\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\5\na\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\5\13t\n\13\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24\2\2\2u")
        buf.write("\2-\3\2\2\2\4\64\3\2\2\2\6;\3\2\2\2\b=\3\2\2\2\nF\3\2")
        buf.write("\2\2\fP\3\2\2\2\16R\3\2\2\2\20Y\3\2\2\2\22`\3\2\2\2\24")
        buf.write("s\3\2\2\2\26\27\7\7\2\2\27\30\5\4\3\2\30\31\7\b\2\2\31")
        buf.write("\32\5\n\6\2\32\33\7\t\2\2\33\34\5\20\t\2\34.\3\2\2\2\35")
        buf.write("\36\7\5\2\2\36\37\5\2\2\2\37 \7\6\2\2 !\7\13\2\2!\"\7")
        buf.write("\5\2\2\"#\5\2\2\2#$\7\6\2\2$.\3\2\2\2%&\7\5\2\2&\'\5\2")
        buf.write("\2\2\'(\7\6\2\2()\7\f\2\2)*\7\5\2\2*+\5\2\2\2+,\7\6\2")
        buf.write("\2,.\3\2\2\2-\26\3\2\2\2-\35\3\2\2\2-%\3\2\2\2.\3\3\2")
        buf.write("\2\2/\60\5\6\4\2\60\61\7\3\2\2\61\62\5\4\3\2\62\65\3\2")
        buf.write("\2\2\63\65\5\6\4\2\64/\3\2\2\2\64\63\3\2\2\2\65\5\3\2")
        buf.write("\2\2\66<\5\b\5\2\678\5\b\5\289\7\n\2\29:\7\32\2\2:<\3")
        buf.write("\2\2\2;\66\3\2\2\2;\67\3\2\2\2<\7\3\2\2\2=>\7\32\2\2>")
        buf.write("?\7\4\2\2?@\7\32\2\2@\t\3\2\2\2AB\5\f\7\2BC\7\3\2\2CD")
        buf.write("\5\n\6\2DG\3\2\2\2EG\5\f\7\2FA\3\2\2\2FE\3\2\2\2G\13\3")
        buf.write("\2\2\2HI\5\16\b\2IJ\7\32\2\2JQ\3\2\2\2KL\7\5\2\2LM\5\2")
        buf.write("\2\2MN\7\6\2\2NO\7\32\2\2OQ\3\2\2\2PH\3\2\2\2PK\3\2\2")
        buf.write("\2Q\r\3\2\2\2RS\7\32\2\2S\17\3\2\2\2TU\5\22\n\2UV\7\20")
        buf.write("\2\2VW\5\20\t\2WZ\3\2\2\2XZ\5\22\n\2YT\3\2\2\2YX\3\2\2")
        buf.write("\2Z\21\3\2\2\2[\\\5\24\13\2\\]\7\17\2\2]^\5\22\n\2^a\3")
        buf.write("\2\2\2_a\5\24\13\2`[\3\2\2\2`_\3\2\2\2a\23\3\2\2\2bc\5")
        buf.write("\b\5\2cd\7\31\2\2de\5\b\5\2et\3\2\2\2fg\5\b\5\2gh\7\22")
        buf.write("\2\2hi\7\5\2\2ij\5\2\2\2jk\7\6\2\2kt\3\2\2\2lm\5\b\5\2")
        buf.write("mn\7\21\2\2no\7\22\2\2op\7\5\2\2pq\5\2\2\2qr\7\6\2\2r")
        buf.write("t\3\2\2\2sb\3\2\2\2sf\3\2\2\2sl\3\2\2\2t\25\3\2\2\2\n")
        buf.write("-\64;FPY`s")
        return buf.getvalue()


class miniSQLParser ( Parser ):

    grammarFileName = "miniSQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'.'", "'('", "')'", "'SELECT'", 
                     "'FROM'", "'WHERE'", "'AS'", "'MINUS'", "'UNION'", 
                     "'JOIN'", "'GROUP BY'", "'AND'", "'OR'", "'NOT'", "'IN'", 
                     "'='", "'!='", "'<'", "'<='", "'>'", "'>='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "LPAR", "RPAR", 
                      "SELECT", "FROM", "WHERE", "AS", "MINUS", "UNION", 
                      "JOIN", "GROUPBY", "AND", "OR", "NOT", "IN", "EQ", 
                      "NEQ", "LT", "LE", "GT", "GE", "COMP_OP", "ID", "WS", 
                      "NEWLINE" ]

    RULE_sql = 0
    RULE_atts = 1
    RULE_attd = 2
    RULE_att = 3
    RULE_rels = 4
    RULE_rel = 5
    RULE_filename = 6
    RULE_cond = 7
    RULE_and_cond = 8
    RULE_at_cond = 9

    ruleNames =  [ "sql", "atts", "attd", "att", "rels", "rel", "filename", 
                   "cond", "and_cond", "at_cond" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    LPAR=3
    RPAR=4
    SELECT=5
    FROM=6
    WHERE=7
    AS=8
    MINUS=9
    UNION=10
    JOIN=11
    GROUPBY=12
    AND=13
    OR=14
    NOT=15
    IN=16
    EQ=17
    NEQ=18
    LT=19
    LE=20
    GT=21
    GE=22
    COMP_OP=23
    ID=24
    WS=25
    NEWLINE=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class SqlContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def project(self):
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

        def UNION(self):
            return self.getToken(miniSQLParser.UNION, 0)

        def getRuleIndex(self):
            return miniSQLParser.RULE_sql

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSql" ):
                return visitor.visitSql(self)
            else:
                return visitor.visitChildren(self)




    def sql(self):

        localctx = miniSQLParser.SqlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sql)
        try:
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.match(miniSQLParser.SELECT)
                self.state = 21
                self.atts()
                self.state = 22
                self.match(miniSQLParser.FROM)
                self.state = 23
                self.rels()
                self.state = 24
                self.match(miniSQLParser.WHERE)
                self.state = 25
                self.cond()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.match(miniSQLParser.LPAR)
                self.state = 28
                self.sql()
                self.state = 29
                self.match(miniSQLParser.RPAR)
                self.state = 30
                self.match(miniSQLParser.MINUS)
                self.state = 31
                self.match(miniSQLParser.LPAR)
                self.state = 32
                self.sql()
                self.state = 33
                self.match(miniSQLParser.RPAR)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.match(miniSQLParser.LPAR)
                self.state = 36
                self.sql()
                self.state = 37
                self.match(miniSQLParser.RPAR)
                self.state = 38
                self.match(miniSQLParser.UNION)
                self.state = 39
                self.match(miniSQLParser.LPAR)
                self.state = 40
                self.sql()
                self.state = 41
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

        def attd(self):
            return self.getTypedRuleContext(miniSQLParser.AttdContext,0)


        def atts(self):
            return self.getTypedRuleContext(miniSQLParser.AttsContext,0)


        def getRuleIndex(self):
            return miniSQLParser.RULE_atts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtts" ):
                return visitor.visitAtts(self)
            else:
                return visitor.visitChildren(self)




    def atts(self):

        localctx = miniSQLParser.AttsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_atts)
        try:
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.attd()
                self.state = 46
                self.match(miniSQLParser.T__0)
                self.state = 47
                self.atts()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
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

        def att(self):
            return self.getTypedRuleContext(miniSQLParser.AttContext,0)


        def AS(self):
            return self.getToken(miniSQLParser.AS, 0)

        def ID(self):
            return self.getToken(miniSQLParser.ID, 0)

        def getRuleIndex(self):
            return miniSQLParser.RULE_attd

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttd" ):
                return visitor.visitAttd(self)
            else:
                return visitor.visitChildren(self)




    def attd(self):

        localctx = miniSQLParser.AttdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_attd)
        try:
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.att()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.att()
                self.state = 54
                self.match(miniSQLParser.AS)
                self.state = 55
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
        self.enterRule(localctx, 6, self.RULE_att)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(miniSQLParser.ID)
            self.state = 60
            self.match(miniSQLParser.T__1)
            self.state = 61
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

        def rel(self):
            return self.getTypedRuleContext(miniSQLParser.RelContext,0)


        def rels(self):
            return self.getTypedRuleContext(miniSQLParser.RelsContext,0)


        def getRuleIndex(self):
            return miniSQLParser.RULE_rels

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRels" ):
                return visitor.visitRels(self)
            else:
                return visitor.visitChildren(self)




    def rels(self):

        localctx = miniSQLParser.RelsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_rels)
        try:
            self.state = 68
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.rel()
                self.state = 64
                self.match(miniSQLParser.T__0)
                self.state = 65
                self.rels()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
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

        def filename(self):
            return self.getTypedRuleContext(miniSQLParser.FilenameContext,0)


        def ID(self):
            return self.getToken(miniSQLParser.ID, 0)

        def LPAR(self):
            return self.getToken(miniSQLParser.LPAR, 0)

        def sql(self):
            return self.getTypedRuleContext(miniSQLParser.SqlContext,0)


        def RPAR(self):
            return self.getToken(miniSQLParser.RPAR, 0)

        def getRuleIndex(self):
            return miniSQLParser.RULE_rel

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRel" ):
                return visitor.visitRel(self)
            else:
                return visitor.visitChildren(self)




    def rel(self):

        localctx = miniSQLParser.RelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_rel)
        try:
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [miniSQLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.filename()
                self.state = 71
                self.match(miniSQLParser.ID)
                pass
            elif token in [miniSQLParser.LPAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.match(miniSQLParser.LPAR)
                self.state = 74
                self.sql()
                self.state = 75
                self.match(miniSQLParser.RPAR)
                self.state = 76
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

    class FilenameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(miniSQLParser.ID, 0)

        def getRuleIndex(self):
            return miniSQLParser.RULE_filename

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilename" ):
                return visitor.visitFilename(self)
            else:
                return visitor.visitChildren(self)




    def filename(self):

        localctx = miniSQLParser.FilenameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_filename)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(miniSQLParser.ID)
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

        def and_cond(self):
            return self.getTypedRuleContext(miniSQLParser.And_condContext,0)


        def OR(self):
            return self.getToken(miniSQLParser.OR, 0)

        def cond(self):
            return self.getTypedRuleContext(miniSQLParser.CondContext,0)


        def getRuleIndex(self):
            return miniSQLParser.RULE_cond

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCond" ):
                return visitor.visitCond(self)
            else:
                return visitor.visitChildren(self)




    def cond(self):

        localctx = miniSQLParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_cond)
        try:
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.and_cond()
                self.state = 83
                self.match(miniSQLParser.OR)
                self.state = 84
                self.cond()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
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

        def at_cond(self):
            return self.getTypedRuleContext(miniSQLParser.At_condContext,0)


        def AND(self):
            return self.getToken(miniSQLParser.AND, 0)

        def and_cond(self):
            return self.getTypedRuleContext(miniSQLParser.And_condContext,0)


        def getRuleIndex(self):
            return miniSQLParser.RULE_and_cond

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd_cond" ):
                return visitor.visitAnd_cond(self)
            else:
                return visitor.visitChildren(self)




    def and_cond(self):

        localctx = miniSQLParser.And_condContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_and_cond)
        try:
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.at_cond()
                self.state = 90
                self.match(miniSQLParser.AND)
                self.state = 91
                self.and_cond()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
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

        def att(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniSQLParser.AttContext)
            else:
                return self.getTypedRuleContext(miniSQLParser.AttContext,i)


        def COMP_OP(self):
            return self.getToken(miniSQLParser.COMP_OP, 0)

        def IN(self):
            return self.getToken(miniSQLParser.IN, 0)

        def LPAR(self):
            return self.getToken(miniSQLParser.LPAR, 0)

        def sql(self):
            return self.getTypedRuleContext(miniSQLParser.SqlContext,0)


        def RPAR(self):
            return self.getToken(miniSQLParser.RPAR, 0)

        def NOT(self):
            return self.getToken(miniSQLParser.NOT, 0)

        def getRuleIndex(self):
            return miniSQLParser.RULE_at_cond

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAt_cond" ):
                return visitor.visitAt_cond(self)
            else:
                return visitor.visitChildren(self)




    def at_cond(self):

        localctx = miniSQLParser.At_condContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_at_cond)
        try:
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.att()
                self.state = 97
                self.match(miniSQLParser.COMP_OP)
                self.state = 98
                self.att()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.att()
                self.state = 101
                self.match(miniSQLParser.IN)
                self.state = 102
                self.match(miniSQLParser.LPAR)
                self.state = 103
                self.sql()
                self.state = 104
                self.match(miniSQLParser.RPAR)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 106
                self.att()
                self.state = 107
                self.match(miniSQLParser.NOT)
                self.state = 108
                self.match(miniSQLParser.IN)
                self.state = 109
                self.match(miniSQLParser.LPAR)
                self.state = 110
                self.sql()
                self.state = 111
                self.match(miniSQLParser.RPAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






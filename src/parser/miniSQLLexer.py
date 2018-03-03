# Generated from src/parser/miniSQL.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\34")
        buf.write("\u00a6\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\3\2\3\2\3\3\3\3\3\4\3\4")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\5\30")
        buf.write("\u0092\n\30\3\31\3\31\7\31\u0096\n\31\f\31\16\31\u0099")
        buf.write("\13\31\3\32\6\32\u009c\n\32\r\32\16\32\u009d\3\32\3\32")
        buf.write("\3\33\6\33\u00a3\n\33\r\33\16\33\u00a4\2\2\34\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\3\2\6\4\2C\\c|\6\2\62;C\\aac|\5\2\13\f\17\17")
        buf.write("\"\"\3\2\f\f\2\u00ad\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\3\67\3\2\2\2\59\3\2\2\2\7;\3\2\2\2\t=\3")
        buf.write("\2\2\2\13?\3\2\2\2\rF\3\2\2\2\17K\3\2\2\2\21Q\3\2\2\2")
        buf.write("\23T\3\2\2\2\25Z\3\2\2\2\27`\3\2\2\2\31e\3\2\2\2\33n\3")
        buf.write("\2\2\2\35r\3\2\2\2\37u\3\2\2\2!y\3\2\2\2#|\3\2\2\2%~\3")
        buf.write("\2\2\2\'\u0081\3\2\2\2)\u0083\3\2\2\2+\u0086\3\2\2\2-")
        buf.write("\u0088\3\2\2\2/\u0091\3\2\2\2\61\u0093\3\2\2\2\63\u009b")
        buf.write("\3\2\2\2\65\u00a2\3\2\2\2\678\7.\2\28\4\3\2\2\29:\7\60")
        buf.write("\2\2:\6\3\2\2\2;<\7*\2\2<\b\3\2\2\2=>\7+\2\2>\n\3\2\2")
        buf.write("\2?@\7U\2\2@A\7G\2\2AB\7N\2\2BC\7G\2\2CD\7E\2\2DE\7V\2")
        buf.write("\2E\f\3\2\2\2FG\7H\2\2GH\7T\2\2HI\7Q\2\2IJ\7O\2\2J\16")
        buf.write("\3\2\2\2KL\7Y\2\2LM\7J\2\2MN\7G\2\2NO\7T\2\2OP\7G\2\2")
        buf.write("P\20\3\2\2\2QR\7C\2\2RS\7U\2\2S\22\3\2\2\2TU\7O\2\2UV")
        buf.write("\7K\2\2VW\7P\2\2WX\7W\2\2XY\7U\2\2Y\24\3\2\2\2Z[\7W\2")
        buf.write("\2[\\\7P\2\2\\]\7K\2\2]^\7Q\2\2^_\7P\2\2_\26\3\2\2\2`")
        buf.write("a\7L\2\2ab\7Q\2\2bc\7K\2\2cd\7P\2\2d\30\3\2\2\2ef\7I\2")
        buf.write("\2fg\7T\2\2gh\7Q\2\2hi\7W\2\2ij\7R\2\2jk\7\"\2\2kl\7D")
        buf.write("\2\2lm\7[\2\2m\32\3\2\2\2no\7C\2\2op\7P\2\2pq\7F\2\2q")
        buf.write("\34\3\2\2\2rs\7Q\2\2st\7T\2\2t\36\3\2\2\2uv\7P\2\2vw\7")
        buf.write("Q\2\2wx\7V\2\2x \3\2\2\2yz\7K\2\2z{\7P\2\2{\"\3\2\2\2")
        buf.write("|}\7?\2\2}$\3\2\2\2~\177\7#\2\2\177\u0080\7?\2\2\u0080")
        buf.write("&\3\2\2\2\u0081\u0082\7>\2\2\u0082(\3\2\2\2\u0083\u0084")
        buf.write("\7>\2\2\u0084\u0085\7?\2\2\u0085*\3\2\2\2\u0086\u0087")
        buf.write("\7@\2\2\u0087,\3\2\2\2\u0088\u0089\7@\2\2\u0089\u008a")
        buf.write("\7?\2\2\u008a.\3\2\2\2\u008b\u0092\5#\22\2\u008c\u0092")
        buf.write("\5%\23\2\u008d\u0092\5\'\24\2\u008e\u0092\5)\25\2\u008f")
        buf.write("\u0092\5+\26\2\u0090\u0092\5-\27\2\u0091\u008b\3\2\2\2")
        buf.write("\u0091\u008c\3\2\2\2\u0091\u008d\3\2\2\2\u0091\u008e\3")
        buf.write("\2\2\2\u0091\u008f\3\2\2\2\u0091\u0090\3\2\2\2\u0092\60")
        buf.write("\3\2\2\2\u0093\u0097\t\2\2\2\u0094\u0096\t\3\2\2\u0095")
        buf.write("\u0094\3\2\2\2\u0096\u0099\3\2\2\2\u0097\u0095\3\2\2\2")
        buf.write("\u0097\u0098\3\2\2\2\u0098\62\3\2\2\2\u0099\u0097\3\2")
        buf.write("\2\2\u009a\u009c\t\4\2\2\u009b\u009a\3\2\2\2\u009c\u009d")
        buf.write("\3\2\2\2\u009d\u009b\3\2\2\2\u009d\u009e\3\2\2\2\u009e")
        buf.write("\u009f\3\2\2\2\u009f\u00a0\b\32\2\2\u00a0\64\3\2\2\2\u00a1")
        buf.write("\u00a3\t\5\2\2\u00a2\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2")
        buf.write("\u00a4\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\66\3\2")
        buf.write("\2\2\7\2\u0091\u0097\u009d\u00a4\3\b\2\2")
        return buf.getvalue()


class miniSQLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    LPAR = 3
    RPAR = 4
    SELECT = 5
    FROM = 6
    WHERE = 7
    AS = 8
    MINUS = 9
    UNION = 10
    JOIN = 11
    GROUPBY = 12
    AND = 13
    OR = 14
    NOT = 15
    IN = 16
    EQ = 17
    NEQ = 18
    LT = 19
    LE = 20
    GT = 21
    GE = 22
    COMP_OP = 23
    ID = 24
    WS = 25
    NEWLINE = 26

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "'.'", "'('", "')'", "'SELECT'", "'FROM'", "'WHERE'", 
            "'AS'", "'MINUS'", "'UNION'", "'JOIN'", "'GROUP BY'", "'AND'", 
            "'OR'", "'NOT'", "'IN'", "'='", "'!='", "'<'", "'<='", "'>'", 
            "'>='" ]

    symbolicNames = [ "<INVALID>",
            "LPAR", "RPAR", "SELECT", "FROM", "WHERE", "AS", "MINUS", "UNION", 
            "JOIN", "GROUPBY", "AND", "OR", "NOT", "IN", "EQ", "NEQ", "LT", 
            "LE", "GT", "GE", "COMP_OP", "ID", "WS", "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "LPAR", "RPAR", "SELECT", "FROM", "WHERE", 
                  "AS", "MINUS", "UNION", "JOIN", "GROUPBY", "AND", "OR", 
                  "NOT", "IN", "EQ", "NEQ", "LT", "LE", "GT", "GE", "COMP_OP", 
                  "ID", "WS", "NEWLINE" ]

    grammarFileName = "miniSQL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



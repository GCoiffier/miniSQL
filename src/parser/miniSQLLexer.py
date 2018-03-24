# Generated from src/parser/miniSQL.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2 ")
        buf.write("\u0107\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\5\tZ\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\nl\n\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\5\13v\n\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u0082\n\f\3\r\3\r\3\r\3")
        buf.write("\r\5\r\u0088\n\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\5\16\u0094\n\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\5\17\u00a0\n\17\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\5\20\u00aa\n\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\5\21\u00bc\n\21\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\5\22\u00c4\n\22\3\23\3\23\3\23\3\23\5\23\u00ca")
        buf.write("\n\23\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u00d2\n\24\3")
        buf.write("\25\3\25\3\25\3\25\5\25\u00d8\n\25\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\34\3\34\7\34\u00eb\n\34\f\34\16\34\u00ee\13\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\7\35\u00f7\n\35\f\35\16")
        buf.write("\35\u00fa\13\35\3\36\6\36\u00fd\n\36\r\36\16\36\u00fe")
        buf.write("\3\36\3\36\3\37\6\37\u0104\n\37\r\37\16\37\u0105\2\2 ")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= \3\2\6\4\2C\\c|\6\2")
        buf.write("\62;C\\aac|\5\2\13\f\17\17\"\"\3\2\f\f\2\u0117\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\3?\3\2\2\2\5A\3\2\2")
        buf.write("\2\7C\3\2\2\2\tE\3\2\2\2\13G\3\2\2\2\rI\3\2\2\2\17K\3")
        buf.write("\2\2\2\21Y\3\2\2\2\23k\3\2\2\2\25u\3\2\2\2\27\u0081\3")
        buf.write("\2\2\2\31\u0087\3\2\2\2\33\u0093\3\2\2\2\35\u009f\3\2")
        buf.write("\2\2\37\u00a9\3\2\2\2!\u00bb\3\2\2\2#\u00c3\3\2\2\2%\u00c9")
        buf.write("\3\2\2\2\'\u00d1\3\2\2\2)\u00d7\3\2\2\2+\u00d9\3\2\2\2")
        buf.write("-\u00db\3\2\2\2/\u00de\3\2\2\2\61\u00e0\3\2\2\2\63\u00e3")
        buf.write("\3\2\2\2\65\u00e5\3\2\2\2\67\u00e8\3\2\2\29\u00f4\3\2")
        buf.write("\2\2;\u00fc\3\2\2\2=\u0103\3\2\2\2?@\7.\2\2@\4\3\2\2\2")
        buf.write("AB\7\60\2\2B\6\3\2\2\2CD\7*\2\2D\b\3\2\2\2EF\7+\2\2F\n")
        buf.write("\3\2\2\2GH\7=\2\2H\f\3\2\2\2IJ\7,\2\2J\16\3\2\2\2KL\7")
        buf.write("$\2\2L\20\3\2\2\2MN\7U\2\2NO\7G\2\2OP\7N\2\2PQ\7G\2\2")
        buf.write("QR\7E\2\2RZ\7V\2\2ST\7u\2\2TU\7g\2\2UV\7n\2\2VW\7g\2\2")
        buf.write("WX\7e\2\2XZ\7v\2\2YM\3\2\2\2YS\3\2\2\2Z\22\3\2\2\2[\\")
        buf.write("\7F\2\2\\]\7K\2\2]^\7U\2\2^_\7V\2\2_`\7K\2\2`a\7P\2\2")
        buf.write("ab\7E\2\2bl\7V\2\2cd\7f\2\2de\7k\2\2ef\7u\2\2fg\7v\2\2")
        buf.write("gh\7k\2\2hi\7p\2\2ij\7e\2\2jl\7v\2\2k[\3\2\2\2kc\3\2\2")
        buf.write("\2l\24\3\2\2\2mn\7H\2\2no\7T\2\2op\7Q\2\2pv\7O\2\2qr\7")
        buf.write("h\2\2rs\7t\2\2st\7q\2\2tv\7o\2\2um\3\2\2\2uq\3\2\2\2v")
        buf.write("\26\3\2\2\2wx\7Y\2\2xy\7J\2\2yz\7G\2\2z{\7T\2\2{\u0082")
        buf.write("\7G\2\2|}\7y\2\2}~\7j\2\2~\177\7g\2\2\177\u0080\7t\2\2")
        buf.write("\u0080\u0082\7g\2\2\u0081w\3\2\2\2\u0081|\3\2\2\2\u0082")
        buf.write("\30\3\2\2\2\u0083\u0084\7C\2\2\u0084\u0088\7U\2\2\u0085")
        buf.write("\u0086\7c\2\2\u0086\u0088\7u\2\2\u0087\u0083\3\2\2\2\u0087")
        buf.write("\u0085\3\2\2\2\u0088\32\3\2\2\2\u0089\u008a\7O\2\2\u008a")
        buf.write("\u008b\7K\2\2\u008b\u008c\7P\2\2\u008c\u008d\7W\2\2\u008d")
        buf.write("\u0094\7U\2\2\u008e\u008f\7o\2\2\u008f\u0090\7k\2\2\u0090")
        buf.write("\u0091\7p\2\2\u0091\u0092\7w\2\2\u0092\u0094\7u\2\2\u0093")
        buf.write("\u0089\3\2\2\2\u0093\u008e\3\2\2\2\u0094\34\3\2\2\2\u0095")
        buf.write("\u0096\7W\2\2\u0096\u0097\7P\2\2\u0097\u0098\7K\2\2\u0098")
        buf.write("\u0099\7Q\2\2\u0099\u00a0\7P\2\2\u009a\u009b\7w\2\2\u009b")
        buf.write("\u009c\7p\2\2\u009c\u009d\7k\2\2\u009d\u009e\7q\2\2\u009e")
        buf.write("\u00a0\7p\2\2\u009f\u0095\3\2\2\2\u009f\u009a\3\2\2\2")
        buf.write("\u00a0\36\3\2\2\2\u00a1\u00a2\7L\2\2\u00a2\u00a3\7Q\2")
        buf.write("\2\u00a3\u00a4\7K\2\2\u00a4\u00aa\7P\2\2\u00a5\u00a6\7")
        buf.write("l\2\2\u00a6\u00a7\7q\2\2\u00a7\u00a8\7k\2\2\u00a8\u00aa")
        buf.write("\7p\2\2\u00a9\u00a1\3\2\2\2\u00a9\u00a5\3\2\2\2\u00aa")
        buf.write(" \3\2\2\2\u00ab\u00ac\7I\2\2\u00ac\u00ad\7T\2\2\u00ad")
        buf.write("\u00ae\7Q\2\2\u00ae\u00af\7W\2\2\u00af\u00b0\7R\2\2\u00b0")
        buf.write("\u00b1\7\"\2\2\u00b1\u00b2\7D\2\2\u00b2\u00bc\7[\2\2\u00b3")
        buf.write("\u00b4\7i\2\2\u00b4\u00b5\7t\2\2\u00b5\u00b6\7q\2\2\u00b6")
        buf.write("\u00b7\7w\2\2\u00b7\u00b8\7r\2\2\u00b8\u00b9\7\"\2\2\u00b9")
        buf.write("\u00ba\7d\2\2\u00ba\u00bc\7{\2\2\u00bb\u00ab\3\2\2\2\u00bb")
        buf.write("\u00b3\3\2\2\2\u00bc\"\3\2\2\2\u00bd\u00be\7C\2\2\u00be")
        buf.write("\u00bf\7P\2\2\u00bf\u00c4\7F\2\2\u00c0\u00c1\7c\2\2\u00c1")
        buf.write("\u00c2\7p\2\2\u00c2\u00c4\7f\2\2\u00c3\u00bd\3\2\2\2\u00c3")
        buf.write("\u00c0\3\2\2\2\u00c4$\3\2\2\2\u00c5\u00c6\7Q\2\2\u00c6")
        buf.write("\u00ca\7T\2\2\u00c7\u00c8\7q\2\2\u00c8\u00ca\7t\2\2\u00c9")
        buf.write("\u00c5\3\2\2\2\u00c9\u00c7\3\2\2\2\u00ca&\3\2\2\2\u00cb")
        buf.write("\u00cc\7P\2\2\u00cc\u00cd\7Q\2\2\u00cd\u00d2\7V\2\2\u00ce")
        buf.write("\u00cf\7p\2\2\u00cf\u00d0\7q\2\2\u00d0\u00d2\7v\2\2\u00d1")
        buf.write("\u00cb\3\2\2\2\u00d1\u00ce\3\2\2\2\u00d2(\3\2\2\2\u00d3")
        buf.write("\u00d4\7K\2\2\u00d4\u00d8\7P\2\2\u00d5\u00d6\7k\2\2\u00d6")
        buf.write("\u00d8\7p\2\2\u00d7\u00d3\3\2\2\2\u00d7\u00d5\3\2\2\2")
        buf.write("\u00d8*\3\2\2\2\u00d9\u00da\7?\2\2\u00da,\3\2\2\2\u00db")
        buf.write("\u00dc\7#\2\2\u00dc\u00dd\7?\2\2\u00dd.\3\2\2\2\u00de")
        buf.write("\u00df\7>\2\2\u00df\60\3\2\2\2\u00e0\u00e1\7>\2\2\u00e1")
        buf.write("\u00e2\7?\2\2\u00e2\62\3\2\2\2\u00e3\u00e4\7@\2\2\u00e4")
        buf.write("\64\3\2\2\2\u00e5\u00e6\7@\2\2\u00e6\u00e7\7?\2\2\u00e7")
        buf.write("\66\3\2\2\2\u00e8\u00ec\t\2\2\2\u00e9\u00eb\t\3\2\2\u00ea")
        buf.write("\u00e9\3\2\2\2\u00eb\u00ee\3\2\2\2\u00ec\u00ea\3\2\2\2")
        buf.write("\u00ec\u00ed\3\2\2\2\u00ed\u00ef\3\2\2\2\u00ee\u00ec\3")
        buf.write("\2\2\2\u00ef\u00f0\7\60\2\2\u00f0\u00f1\7e\2\2\u00f1\u00f2")
        buf.write("\7u\2\2\u00f2\u00f3\7x\2\2\u00f38\3\2\2\2\u00f4\u00f8")
        buf.write("\t\2\2\2\u00f5\u00f7\t\3\2\2\u00f6\u00f5\3\2\2\2\u00f7")
        buf.write("\u00fa\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2")
        buf.write("\u00f9:\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fb\u00fd\t\4\2")
        buf.write("\2\u00fc\u00fb\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u00fc")
        buf.write("\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0100\3\2\2\2\u0100")
        buf.write("\u0101\b\36\2\2\u0101<\3\2\2\2\u0102\u0104\t\5\2\2\u0103")
        buf.write("\u0102\3\2\2\2\u0104\u0105\3\2\2\2\u0105\u0103\3\2\2\2")
        buf.write("\u0105\u0106\3\2\2\2\u0106>\3\2\2\2\24\2Yku\u0081\u0087")
        buf.write("\u0093\u009f\u00a9\u00bb\u00c3\u00c9\u00d1\u00d7\u00ec")
        buf.write("\u00f8\u00fe\u0105\3\b\2\2")
        return buf.getvalue()


class miniSQLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    LPAR = 3
    RPAR = 4
    COLON = 5
    STAR = 6
    QUOTE = 7
    SELECT = 8
    DISTINCT = 9
    FROM = 10
    WHERE = 11
    AS = 12
    MINUS = 13
    UNION = 14
    JOIN = 15
    GROUPBY = 16
    AND = 17
    OR = 18
    NOT = 19
    IN = 20
    EQ = 21
    NEQ = 22
    LT = 23
    LE = 24
    GT = 25
    GE = 26
    FILENAME = 27
    ID = 28
    WS = 29
    NEWLINE = 30

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "'.'", "'('", "')'", "';'", "'*'", "'\"'", "'='", "'!='", 
            "'<'", "'<='", "'>'", "'>='" ]

    symbolicNames = [ "<INVALID>",
            "LPAR", "RPAR", "COLON", "STAR", "QUOTE", "SELECT", "DISTINCT", 
            "FROM", "WHERE", "AS", "MINUS", "UNION", "JOIN", "GROUPBY", 
            "AND", "OR", "NOT", "IN", "EQ", "NEQ", "LT", "LE", "GT", "GE", 
            "FILENAME", "ID", "WS", "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "LPAR", "RPAR", "COLON", "STAR", "QUOTE", 
                  "SELECT", "DISTINCT", "FROM", "WHERE", "AS", "MINUS", 
                  "UNION", "JOIN", "GROUPBY", "AND", "OR", "NOT", "IN", 
                  "EQ", "NEQ", "LT", "LE", "GT", "GE", "FILENAME", "ID", 
                  "WS", "NEWLINE" ]

    grammarFileName = "miniSQL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



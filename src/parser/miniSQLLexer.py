# Generated from src/parser/miniSQL.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2 ")
        buf.write("\u00fd\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\5\tZ\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\5\nd\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\5\13p\n\13\3\f\3\f\3\f\3\f\5\fv\n\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u0082\n\r\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u008e\n\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u0098\n")
        buf.write("\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00aa\n\20\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\5\21\u00b2\n\21\3\22\3\22\3\22")
        buf.write("\3\22\5\22\u00b8\n\22\3\23\3\23\3\23\3\23\3\23\3\23\5")
        buf.write("\23\u00c0\n\23\3\24\3\24\3\24\3\24\5\24\u00c6\n\24\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u00dd")
        buf.write("\n\33\3\34\3\34\7\34\u00e1\n\34\f\34\16\34\u00e4\13\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\35\3\35\7\35\u00ed\n\35\f")
        buf.write("\35\16\35\u00f0\13\35\3\36\6\36\u00f3\n\36\r\36\16\36")
        buf.write("\u00f4\3\36\3\36\3\37\6\37\u00fa\n\37\r\37\16\37\u00fb")
        buf.write("\2\2 \3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= \3\2\6\4\2C\\c|")
        buf.write("\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\3\2\f\f\2\u0111\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\3?\3\2\2\2\5")
        buf.write("A\3\2\2\2\7C\3\2\2\2\tE\3\2\2\2\13G\3\2\2\2\rI\3\2\2\2")
        buf.write("\17K\3\2\2\2\21Y\3\2\2\2\23c\3\2\2\2\25o\3\2\2\2\27u\3")
        buf.write("\2\2\2\31\u0081\3\2\2\2\33\u008d\3\2\2\2\35\u0097\3\2")
        buf.write("\2\2\37\u00a9\3\2\2\2!\u00b1\3\2\2\2#\u00b7\3\2\2\2%\u00bf")
        buf.write("\3\2\2\2\'\u00c5\3\2\2\2)\u00c7\3\2\2\2+\u00c9\3\2\2\2")
        buf.write("-\u00cc\3\2\2\2/\u00ce\3\2\2\2\61\u00d1\3\2\2\2\63\u00d3")
        buf.write("\3\2\2\2\65\u00dc\3\2\2\2\67\u00de\3\2\2\29\u00ea\3\2")
        buf.write("\2\2;\u00f2\3\2\2\2=\u00f9\3\2\2\2?@\7.\2\2@\4\3\2\2\2")
        buf.write("AB\7\60\2\2B\6\3\2\2\2CD\7*\2\2D\b\3\2\2\2EF\7+\2\2F\n")
        buf.write("\3\2\2\2GH\7=\2\2H\f\3\2\2\2IJ\7,\2\2J\16\3\2\2\2KL\7")
        buf.write("$\2\2L\20\3\2\2\2MN\7U\2\2NO\7G\2\2OP\7N\2\2PQ\7G\2\2")
        buf.write("QR\7E\2\2RZ\7V\2\2ST\7u\2\2TU\7g\2\2UV\7n\2\2VW\7g\2\2")
        buf.write("WX\7e\2\2XZ\7v\2\2YM\3\2\2\2YS\3\2\2\2Z\22\3\2\2\2[\\")
        buf.write("\7H\2\2\\]\7T\2\2]^\7Q\2\2^d\7O\2\2_`\7h\2\2`a\7t\2\2")
        buf.write("ab\7q\2\2bd\7o\2\2c[\3\2\2\2c_\3\2\2\2d\24\3\2\2\2ef\7")
        buf.write("Y\2\2fg\7J\2\2gh\7G\2\2hi\7T\2\2ip\7G\2\2jk\7y\2\2kl\7")
        buf.write("j\2\2lm\7g\2\2mn\7t\2\2np\7g\2\2oe\3\2\2\2oj\3\2\2\2p")
        buf.write("\26\3\2\2\2qr\7C\2\2rv\7U\2\2st\7c\2\2tv\7u\2\2uq\3\2")
        buf.write("\2\2us\3\2\2\2v\30\3\2\2\2wx\7O\2\2xy\7K\2\2yz\7P\2\2")
        buf.write("z{\7W\2\2{\u0082\7U\2\2|}\7o\2\2}~\7k\2\2~\177\7p\2\2")
        buf.write("\177\u0080\7w\2\2\u0080\u0082\7u\2\2\u0081w\3\2\2\2\u0081")
        buf.write("|\3\2\2\2\u0082\32\3\2\2\2\u0083\u0084\7W\2\2\u0084\u0085")
        buf.write("\7P\2\2\u0085\u0086\7K\2\2\u0086\u0087\7Q\2\2\u0087\u008e")
        buf.write("\7P\2\2\u0088\u0089\7w\2\2\u0089\u008a\7p\2\2\u008a\u008b")
        buf.write("\7k\2\2\u008b\u008c\7q\2\2\u008c\u008e\7p\2\2\u008d\u0083")
        buf.write("\3\2\2\2\u008d\u0088\3\2\2\2\u008e\34\3\2\2\2\u008f\u0090")
        buf.write("\7L\2\2\u0090\u0091\7Q\2\2\u0091\u0092\7K\2\2\u0092\u0098")
        buf.write("\7P\2\2\u0093\u0094\7l\2\2\u0094\u0095\7q\2\2\u0095\u0096")
        buf.write("\7k\2\2\u0096\u0098\7p\2\2\u0097\u008f\3\2\2\2\u0097\u0093")
        buf.write("\3\2\2\2\u0098\36\3\2\2\2\u0099\u009a\7I\2\2\u009a\u009b")
        buf.write("\7T\2\2\u009b\u009c\7Q\2\2\u009c\u009d\7W\2\2\u009d\u009e")
        buf.write("\7R\2\2\u009e\u009f\7\"\2\2\u009f\u00a0\7D\2\2\u00a0\u00aa")
        buf.write("\7[\2\2\u00a1\u00a2\7i\2\2\u00a2\u00a3\7t\2\2\u00a3\u00a4")
        buf.write("\7q\2\2\u00a4\u00a5\7w\2\2\u00a5\u00a6\7r\2\2\u00a6\u00a7")
        buf.write("\7\"\2\2\u00a7\u00a8\7d\2\2\u00a8\u00aa\7{\2\2\u00a9\u0099")
        buf.write("\3\2\2\2\u00a9\u00a1\3\2\2\2\u00aa \3\2\2\2\u00ab\u00ac")
        buf.write("\7C\2\2\u00ac\u00ad\7P\2\2\u00ad\u00b2\7F\2\2\u00ae\u00af")
        buf.write("\7c\2\2\u00af\u00b0\7p\2\2\u00b0\u00b2\7f\2\2\u00b1\u00ab")
        buf.write("\3\2\2\2\u00b1\u00ae\3\2\2\2\u00b2\"\3\2\2\2\u00b3\u00b4")
        buf.write("\7Q\2\2\u00b4\u00b8\7T\2\2\u00b5\u00b6\7q\2\2\u00b6\u00b8")
        buf.write("\7t\2\2\u00b7\u00b3\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8")
        buf.write("$\3\2\2\2\u00b9\u00ba\7P\2\2\u00ba\u00bb\7Q\2\2\u00bb")
        buf.write("\u00c0\7V\2\2\u00bc\u00bd\7p\2\2\u00bd\u00be\7q\2\2\u00be")
        buf.write("\u00c0\7v\2\2\u00bf\u00b9\3\2\2\2\u00bf\u00bc\3\2\2\2")
        buf.write("\u00c0&\3\2\2\2\u00c1\u00c2\7K\2\2\u00c2\u00c6\7P\2\2")
        buf.write("\u00c3\u00c4\7k\2\2\u00c4\u00c6\7p\2\2\u00c5\u00c1\3\2")
        buf.write("\2\2\u00c5\u00c3\3\2\2\2\u00c6(\3\2\2\2\u00c7\u00c8\7")
        buf.write("?\2\2\u00c8*\3\2\2\2\u00c9\u00ca\7#\2\2\u00ca\u00cb\7")
        buf.write("?\2\2\u00cb,\3\2\2\2\u00cc\u00cd\7>\2\2\u00cd.\3\2\2\2")
        buf.write("\u00ce\u00cf\7>\2\2\u00cf\u00d0\7?\2\2\u00d0\60\3\2\2")
        buf.write("\2\u00d1\u00d2\7@\2\2\u00d2\62\3\2\2\2\u00d3\u00d4\7@")
        buf.write("\2\2\u00d4\u00d5\7?\2\2\u00d5\64\3\2\2\2\u00d6\u00dd\5")
        buf.write(")\25\2\u00d7\u00dd\5+\26\2\u00d8\u00dd\5-\27\2\u00d9\u00dd")
        buf.write("\5/\30\2\u00da\u00dd\5\61\31\2\u00db\u00dd\5\63\32\2\u00dc")
        buf.write("\u00d6\3\2\2\2\u00dc\u00d7\3\2\2\2\u00dc\u00d8\3\2\2\2")
        buf.write("\u00dc\u00d9\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00db\3")
        buf.write("\2\2\2\u00dd\66\3\2\2\2\u00de\u00e2\t\2\2\2\u00df\u00e1")
        buf.write("\t\3\2\2\u00e0\u00df\3\2\2\2\u00e1\u00e4\3\2\2\2\u00e2")
        buf.write("\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e5\3\2\2\2")
        buf.write("\u00e4\u00e2\3\2\2\2\u00e5\u00e6\7\60\2\2\u00e6\u00e7")
        buf.write("\7e\2\2\u00e7\u00e8\7u\2\2\u00e8\u00e9\7x\2\2\u00e98\3")
        buf.write("\2\2\2\u00ea\u00ee\t\2\2\2\u00eb\u00ed\t\3\2\2\u00ec\u00eb")
        buf.write("\3\2\2\2\u00ed\u00f0\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ee")
        buf.write("\u00ef\3\2\2\2\u00ef:\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f1")
        buf.write("\u00f3\t\4\2\2\u00f2\u00f1\3\2\2\2\u00f3\u00f4\3\2\2\2")
        buf.write("\u00f4\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f6\3")
        buf.write("\2\2\2\u00f6\u00f7\b\36\2\2\u00f7<\3\2\2\2\u00f8\u00fa")
        buf.write("\t\5\2\2\u00f9\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb")
        buf.write("\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc>\3\2\2\2\24\2")
        buf.write("Ycou\u0081\u008d\u0097\u00a9\u00b1\u00b7\u00bf\u00c5\u00dc")
        buf.write("\u00e2\u00ee\u00f4\u00fb\3\b\2\2")
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
    FROM = 9
    WHERE = 10
    AS = 11
    MINUS = 12
    UNION = 13
    JOIN = 14
    GROUPBY = 15
    AND = 16
    OR = 17
    NOT = 18
    IN = 19
    EQ = 20
    NEQ = 21
    LT = 22
    LE = 23
    GT = 24
    GE = 25
    COMP_OP = 26
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
            "LPAR", "RPAR", "COLON", "STAR", "QUOTE", "SELECT", "FROM", 
            "WHERE", "AS", "MINUS", "UNION", "JOIN", "GROUPBY", "AND", "OR", 
            "NOT", "IN", "EQ", "NEQ", "LT", "LE", "GT", "GE", "COMP_OP", 
            "FILENAME", "ID", "WS", "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "LPAR", "RPAR", "COLON", "STAR", "QUOTE", 
                  "SELECT", "FROM", "WHERE", "AS", "MINUS", "UNION", "JOIN", 
                  "GROUPBY", "AND", "OR", "NOT", "IN", "EQ", "NEQ", "LT", 
                  "LE", "GT", "GE", "COMP_OP", "FILENAME", "ID", "WS", "NEWLINE" ]

    grammarFileName = "miniSQL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



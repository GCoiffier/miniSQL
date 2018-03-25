# Generated from src/parser/miniSQL.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\'")
        buf.write("\u015d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\5\th\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\5\nz\n\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\5\13\u0084\n\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\5\f\u0090\n\f\3\r\3\r\3\r\3\r\5\r")
        buf.write("\u0096\n\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\5\16\u00a2\n\16\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\5\17\u00ae\n\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\5\20\u00b8\n\20\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\5\21\u00ca\n\21\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\5\22\u00dc\n\22\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00e4")
        buf.write("\n\23\3\24\3\24\3\24\3\24\5\24\u00ea\n\24\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\5\25\u00f2\n\25\3\26\3\26\3\26\3\26")
        buf.write("\5\26\u00f8\n\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\5\27\u0102\n\27\3\30\3\30\3\30\3\30\3\30\3\30\5\30")
        buf.write("\u010a\n\30\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u0112\n")
        buf.write("\31\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u011a\n\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u0126")
        buf.write("\n\33\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u012e\n\34\3")
        buf.write("\35\3\35\3\36\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3\"\3")
        buf.write("\"\3\"\3#\3#\7#\u0141\n#\f#\16#\u0144\13#\3#\3#\3#\3#")
        buf.write("\3#\3$\3$\7$\u014d\n$\f$\16$\u0150\13$\3%\6%\u0153\n%")
        buf.write("\r%\16%\u0154\3%\3%\3&\6&\u015a\n&\r&\16&\u015b\2\2\'")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'\3\2")
        buf.write("\6\4\2C\\c|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\3\2\f\f")
        buf.write("\2\u0174\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write("\2I\3\2\2\2\2K\3\2\2\2\3M\3\2\2\2\5O\3\2\2\2\7Q\3\2\2")
        buf.write("\2\tS\3\2\2\2\13U\3\2\2\2\rW\3\2\2\2\17Y\3\2\2\2\21g\3")
        buf.write("\2\2\2\23y\3\2\2\2\25\u0083\3\2\2\2\27\u008f\3\2\2\2\31")
        buf.write("\u0095\3\2\2\2\33\u00a1\3\2\2\2\35\u00ad\3\2\2\2\37\u00b7")
        buf.write("\3\2\2\2!\u00c9\3\2\2\2#\u00db\3\2\2\2%\u00e3\3\2\2\2")
        buf.write("\'\u00e9\3\2\2\2)\u00f1\3\2\2\2+\u00f7\3\2\2\2-\u0101")
        buf.write("\3\2\2\2/\u0109\3\2\2\2\61\u0111\3\2\2\2\63\u0119\3\2")
        buf.write("\2\2\65\u0125\3\2\2\2\67\u012d\3\2\2\29\u012f\3\2\2\2")
        buf.write(";\u0131\3\2\2\2=\u0134\3\2\2\2?\u0136\3\2\2\2A\u0139\3")
        buf.write("\2\2\2C\u013b\3\2\2\2E\u013e\3\2\2\2G\u014a\3\2\2\2I\u0152")
        buf.write("\3\2\2\2K\u0159\3\2\2\2MN\7.\2\2N\4\3\2\2\2OP\7\60\2\2")
        buf.write("P\6\3\2\2\2QR\7*\2\2R\b\3\2\2\2ST\7+\2\2T\n\3\2\2\2UV")
        buf.write("\7=\2\2V\f\3\2\2\2WX\7,\2\2X\16\3\2\2\2YZ\7$\2\2Z\20\3")
        buf.write("\2\2\2[\\\7U\2\2\\]\7G\2\2]^\7N\2\2^_\7G\2\2_`\7E\2\2")
        buf.write("`h\7V\2\2ab\7u\2\2bc\7g\2\2cd\7n\2\2de\7g\2\2ef\7e\2\2")
        buf.write("fh\7v\2\2g[\3\2\2\2ga\3\2\2\2h\22\3\2\2\2ij\7F\2\2jk\7")
        buf.write("K\2\2kl\7U\2\2lm\7V\2\2mn\7K\2\2no\7P\2\2op\7E\2\2pz\7")
        buf.write("V\2\2qr\7f\2\2rs\7k\2\2st\7u\2\2tu\7v\2\2uv\7k\2\2vw\7")
        buf.write("p\2\2wx\7e\2\2xz\7v\2\2yi\3\2\2\2yq\3\2\2\2z\24\3\2\2")
        buf.write("\2{|\7H\2\2|}\7T\2\2}~\7Q\2\2~\u0084\7O\2\2\177\u0080")
        buf.write("\7h\2\2\u0080\u0081\7t\2\2\u0081\u0082\7q\2\2\u0082\u0084")
        buf.write("\7o\2\2\u0083{\3\2\2\2\u0083\177\3\2\2\2\u0084\26\3\2")
        buf.write("\2\2\u0085\u0086\7Y\2\2\u0086\u0087\7J\2\2\u0087\u0088")
        buf.write("\7G\2\2\u0088\u0089\7T\2\2\u0089\u0090\7G\2\2\u008a\u008b")
        buf.write("\7y\2\2\u008b\u008c\7j\2\2\u008c\u008d\7g\2\2\u008d\u008e")
        buf.write("\7t\2\2\u008e\u0090\7g\2\2\u008f\u0085\3\2\2\2\u008f\u008a")
        buf.write("\3\2\2\2\u0090\30\3\2\2\2\u0091\u0092\7C\2\2\u0092\u0096")
        buf.write("\7U\2\2\u0093\u0094\7c\2\2\u0094\u0096\7u\2\2\u0095\u0091")
        buf.write("\3\2\2\2\u0095\u0093\3\2\2\2\u0096\32\3\2\2\2\u0097\u0098")
        buf.write("\7O\2\2\u0098\u0099\7K\2\2\u0099\u009a\7P\2\2\u009a\u009b")
        buf.write("\7W\2\2\u009b\u00a2\7U\2\2\u009c\u009d\7o\2\2\u009d\u009e")
        buf.write("\7k\2\2\u009e\u009f\7p\2\2\u009f\u00a0\7w\2\2\u00a0\u00a2")
        buf.write("\7u\2\2\u00a1\u0097\3\2\2\2\u00a1\u009c\3\2\2\2\u00a2")
        buf.write("\34\3\2\2\2\u00a3\u00a4\7W\2\2\u00a4\u00a5\7P\2\2\u00a5")
        buf.write("\u00a6\7K\2\2\u00a6\u00a7\7Q\2\2\u00a7\u00ae\7P\2\2\u00a8")
        buf.write("\u00a9\7w\2\2\u00a9\u00aa\7p\2\2\u00aa\u00ab\7k\2\2\u00ab")
        buf.write("\u00ac\7q\2\2\u00ac\u00ae\7p\2\2\u00ad\u00a3\3\2\2\2\u00ad")
        buf.write("\u00a8\3\2\2\2\u00ae\36\3\2\2\2\u00af\u00b0\7L\2\2\u00b0")
        buf.write("\u00b1\7Q\2\2\u00b1\u00b2\7K\2\2\u00b2\u00b8\7P\2\2\u00b3")
        buf.write("\u00b4\7l\2\2\u00b4\u00b5\7q\2\2\u00b5\u00b6\7k\2\2\u00b6")
        buf.write("\u00b8\7p\2\2\u00b7\u00af\3\2\2\2\u00b7\u00b3\3\2\2\2")
        buf.write("\u00b8 \3\2\2\2\u00b9\u00ba\7I\2\2\u00ba\u00bb\7T\2\2")
        buf.write("\u00bb\u00bc\7Q\2\2\u00bc\u00bd\7W\2\2\u00bd\u00be\7R")
        buf.write("\2\2\u00be\u00bf\7\"\2\2\u00bf\u00c0\7D\2\2\u00c0\u00ca")
        buf.write("\7[\2\2\u00c1\u00c2\7i\2\2\u00c2\u00c3\7t\2\2\u00c3\u00c4")
        buf.write("\7q\2\2\u00c4\u00c5\7w\2\2\u00c5\u00c6\7r\2\2\u00c6\u00c7")
        buf.write("\7\"\2\2\u00c7\u00c8\7d\2\2\u00c8\u00ca\7{\2\2\u00c9\u00b9")
        buf.write("\3\2\2\2\u00c9\u00c1\3\2\2\2\u00ca\"\3\2\2\2\u00cb\u00cc")
        buf.write("\7Q\2\2\u00cc\u00cd\7T\2\2\u00cd\u00ce\7F\2\2\u00ce\u00cf")
        buf.write("\7G\2\2\u00cf\u00d0\7T\2\2\u00d0\u00d1\7\"\2\2\u00d1\u00d2")
        buf.write("\7D\2\2\u00d2\u00dc\7[\2\2\u00d3\u00d4\7q\2\2\u00d4\u00d5")
        buf.write("\7t\2\2\u00d5\u00d6\7f\2\2\u00d6\u00d7\7g\2\2\u00d7\u00d8")
        buf.write("\7t\2\2\u00d8\u00d9\7\"\2\2\u00d9\u00da\7d\2\2\u00da\u00dc")
        buf.write("\7{\2\2\u00db\u00cb\3\2\2\2\u00db\u00d3\3\2\2\2\u00dc")
        buf.write("$\3\2\2\2\u00dd\u00de\7C\2\2\u00de\u00df\7P\2\2\u00df")
        buf.write("\u00e4\7F\2\2\u00e0\u00e1\7c\2\2\u00e1\u00e2\7p\2\2\u00e2")
        buf.write("\u00e4\7f\2\2\u00e3\u00dd\3\2\2\2\u00e3\u00e0\3\2\2\2")
        buf.write("\u00e4&\3\2\2\2\u00e5\u00e6\7Q\2\2\u00e6\u00ea\7T\2\2")
        buf.write("\u00e7\u00e8\7q\2\2\u00e8\u00ea\7t\2\2\u00e9\u00e5\3\2")
        buf.write("\2\2\u00e9\u00e7\3\2\2\2\u00ea(\3\2\2\2\u00eb\u00ec\7")
        buf.write("P\2\2\u00ec\u00ed\7Q\2\2\u00ed\u00f2\7V\2\2\u00ee\u00ef")
        buf.write("\7p\2\2\u00ef\u00f0\7q\2\2\u00f0\u00f2\7v\2\2\u00f1\u00eb")
        buf.write("\3\2\2\2\u00f1\u00ee\3\2\2\2\u00f2*\3\2\2\2\u00f3\u00f4")
        buf.write("\7K\2\2\u00f4\u00f8\7P\2\2\u00f5\u00f6\7k\2\2\u00f6\u00f8")
        buf.write("\7p\2\2\u00f7\u00f3\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f8")
        buf.write(",\3\2\2\2\u00f9\u00fa\7F\2\2\u00fa\u00fb\7G\2\2\u00fb")
        buf.write("\u00fc\7U\2\2\u00fc\u0102\7E\2\2\u00fd\u00fe\7f\2\2\u00fe")
        buf.write("\u00ff\7g\2\2\u00ff\u0100\7u\2\2\u0100\u0102\7e\2\2\u0101")
        buf.write("\u00f9\3\2\2\2\u0101\u00fd\3\2\2\2\u0102.\3\2\2\2\u0103")
        buf.write("\u0104\7C\2\2\u0104\u0105\7U\2\2\u0105\u010a\7E\2\2\u0106")
        buf.write("\u0107\7c\2\2\u0107\u0108\7u\2\2\u0108\u010a\7e\2\2\u0109")
        buf.write("\u0103\3\2\2\2\u0109\u0106\3\2\2\2\u010a\60\3\2\2\2\u010b")
        buf.write("\u010c\7O\2\2\u010c\u010d\7C\2\2\u010d\u0112\7Z\2\2\u010e")
        buf.write("\u010f\7o\2\2\u010f\u0110\7c\2\2\u0110\u0112\7z\2\2\u0111")
        buf.write("\u010b\3\2\2\2\u0111\u010e\3\2\2\2\u0112\62\3\2\2\2\u0113")
        buf.write("\u0114\7O\2\2\u0114\u0115\7K\2\2\u0115\u011a\7P\2\2\u0116")
        buf.write("\u0117\7o\2\2\u0117\u0118\7k\2\2\u0118\u011a\7p\2\2\u0119")
        buf.write("\u0113\3\2\2\2\u0119\u0116\3\2\2\2\u011a\64\3\2\2\2\u011b")
        buf.write("\u011c\7E\2\2\u011c\u011d\7Q\2\2\u011d\u011e\7W\2\2\u011e")
        buf.write("\u011f\7P\2\2\u011f\u0126\7V\2\2\u0120\u0121\7e\2\2\u0121")
        buf.write("\u0122\7q\2\2\u0122\u0123\7w\2\2\u0123\u0124\7p\2\2\u0124")
        buf.write("\u0126\7v\2\2\u0125\u011b\3\2\2\2\u0125\u0120\3\2\2\2")
        buf.write("\u0126\66\3\2\2\2\u0127\u0128\7U\2\2\u0128\u0129\7W\2")
        buf.write("\2\u0129\u012e\7O\2\2\u012a\u012b\7u\2\2\u012b\u012c\7")
        buf.write("w\2\2\u012c\u012e\7o\2\2\u012d\u0127\3\2\2\2\u012d\u012a")
        buf.write("\3\2\2\2\u012e8\3\2\2\2\u012f\u0130\7?\2\2\u0130:\3\2")
        buf.write("\2\2\u0131\u0132\7#\2\2\u0132\u0133\7?\2\2\u0133<\3\2")
        buf.write("\2\2\u0134\u0135\7>\2\2\u0135>\3\2\2\2\u0136\u0137\7>")
        buf.write("\2\2\u0137\u0138\7?\2\2\u0138@\3\2\2\2\u0139\u013a\7@")
        buf.write("\2\2\u013aB\3\2\2\2\u013b\u013c\7@\2\2\u013c\u013d\7?")
        buf.write("\2\2\u013dD\3\2\2\2\u013e\u0142\t\2\2\2\u013f\u0141\t")
        buf.write("\3\2\2\u0140\u013f\3\2\2\2\u0141\u0144\3\2\2\2\u0142\u0140")
        buf.write("\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0145\3\2\2\2\u0144")
        buf.write("\u0142\3\2\2\2\u0145\u0146\7\60\2\2\u0146\u0147\7e\2\2")
        buf.write("\u0147\u0148\7u\2\2\u0148\u0149\7x\2\2\u0149F\3\2\2\2")
        buf.write("\u014a\u014e\t\2\2\2\u014b\u014d\t\3\2\2\u014c\u014b\3")
        buf.write("\2\2\2\u014d\u0150\3\2\2\2\u014e\u014c\3\2\2\2\u014e\u014f")
        buf.write("\3\2\2\2\u014fH\3\2\2\2\u0150\u014e\3\2\2\2\u0151\u0153")
        buf.write("\t\4\2\2\u0152\u0151\3\2\2\2\u0153\u0154\3\2\2\2\u0154")
        buf.write("\u0152\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0156\3\2\2\2")
        buf.write("\u0156\u0157\b%\2\2\u0157J\3\2\2\2\u0158\u015a\t\5\2\2")
        buf.write("\u0159\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u0159\3")
        buf.write("\2\2\2\u015b\u015c\3\2\2\2\u015cL\3\2\2\2\33\2gy\u0083")
        buf.write("\u008f\u0095\u00a1\u00ad\u00b7\u00c9\u00db\u00e3\u00e9")
        buf.write("\u00f1\u00f7\u0101\u0109\u0111\u0119\u0125\u012d\u0142")
        buf.write("\u014e\u0154\u015b\3\b\2\2")
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
    ORDERBY = 17
    AND = 18
    OR = 19
    NOT = 20
    IN = 21
    DESC = 22
    ASC = 23
    MAX = 24
    MIN = 25
    COUNT = 26
    SUM = 27
    EQ = 28
    NEQ = 29
    LT = 30
    LE = 31
    GT = 32
    GE = 33
    FILENAME = 34
    ID = 35
    WS = 36
    NEWLINE = 37

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "'.'", "'('", "')'", "';'", "'*'", "'\"'", "'='", "'!='", 
            "'<'", "'<='", "'>'", "'>='" ]

    symbolicNames = [ "<INVALID>",
            "LPAR", "RPAR", "COLON", "STAR", "QUOTE", "SELECT", "DISTINCT", 
            "FROM", "WHERE", "AS", "MINUS", "UNION", "JOIN", "GROUPBY", 
            "ORDERBY", "AND", "OR", "NOT", "IN", "DESC", "ASC", "MAX", "MIN", 
            "COUNT", "SUM", "EQ", "NEQ", "LT", "LE", "GT", "GE", "FILENAME", 
            "ID", "WS", "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "LPAR", "RPAR", "COLON", "STAR", "QUOTE", 
                  "SELECT", "DISTINCT", "FROM", "WHERE", "AS", "MINUS", 
                  "UNION", "JOIN", "GROUPBY", "ORDERBY", "AND", "OR", "NOT", 
                  "IN", "DESC", "ASC", "MAX", "MIN", "COUNT", "SUM", "EQ", 
                  "NEQ", "LT", "LE", "GT", "GE", "FILENAME", "ID", "WS", 
                  "NEWLINE" ]

    grammarFileName = "miniSQL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



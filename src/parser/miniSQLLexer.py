# Generated from src/parser/miniSQL.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\36")
        buf.write("\u00eb\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\bT\n\b\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t^\n\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\5\nj\n\n\3\13\3\13\3\13\3\13\5")
        buf.write("\13p\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f")
        buf.write("|\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u0088")
        buf.write("\n\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u0092")
        buf.write("\n\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00a4\n\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\5\20\u00ac\n\20\3\21\3\21\3\21")
        buf.write("\3\21\5\21\u00b2\n\21\3\22\3\22\3\22\3\22\3\22\3\22\5")
        buf.write("\22\u00ba\n\22\3\23\3\23\3\23\3\23\5\23\u00c0\n\23\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u00d7")
        buf.write("\n\32\3\33\3\33\7\33\u00db\n\33\f\33\16\33\u00de\13\33")
        buf.write("\3\34\6\34\u00e1\n\34\r\34\16\34\u00e2\3\34\3\34\3\35")
        buf.write("\6\35\u00e8\n\35\r\35\16\35\u00e9\2\2\36\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36\3\2\6\4\2C\\c|\6\2\62;C\\aac|\5\2\13\f\17")
        buf.write("\17\"\"\3\2\f\f\2\u00fe\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\3;\3\2\2\2")
        buf.write("\5=\3\2\2\2\7?\3\2\2\2\tA\3\2\2\2\13C\3\2\2\2\rE\3\2\2")
        buf.write("\2\17S\3\2\2\2\21]\3\2\2\2\23i\3\2\2\2\25o\3\2\2\2\27")
        buf.write("{\3\2\2\2\31\u0087\3\2\2\2\33\u0091\3\2\2\2\35\u00a3\3")
        buf.write("\2\2\2\37\u00ab\3\2\2\2!\u00b1\3\2\2\2#\u00b9\3\2\2\2")
        buf.write("%\u00bf\3\2\2\2\'\u00c1\3\2\2\2)\u00c3\3\2\2\2+\u00c6")
        buf.write("\3\2\2\2-\u00c8\3\2\2\2/\u00cb\3\2\2\2\61\u00cd\3\2\2")
        buf.write("\2\63\u00d6\3\2\2\2\65\u00d8\3\2\2\2\67\u00e0\3\2\2\2")
        buf.write("9\u00e7\3\2\2\2;<\7.\2\2<\4\3\2\2\2=>\7\60\2\2>\6\3\2")
        buf.write("\2\2?@\7*\2\2@\b\3\2\2\2AB\7+\2\2B\n\3\2\2\2CD\7=\2\2")
        buf.write("D\f\3\2\2\2EF\7,\2\2F\16\3\2\2\2GH\7U\2\2HI\7G\2\2IJ\7")
        buf.write("N\2\2JK\7G\2\2KL\7E\2\2LT\7V\2\2MN\7u\2\2NO\7g\2\2OP\7")
        buf.write("n\2\2PQ\7g\2\2QR\7e\2\2RT\7v\2\2SG\3\2\2\2SM\3\2\2\2T")
        buf.write("\20\3\2\2\2UV\7H\2\2VW\7T\2\2WX\7Q\2\2X^\7O\2\2YZ\7h\2")
        buf.write("\2Z[\7t\2\2[\\\7q\2\2\\^\7o\2\2]U\3\2\2\2]Y\3\2\2\2^\22")
        buf.write("\3\2\2\2_`\7Y\2\2`a\7J\2\2ab\7G\2\2bc\7T\2\2cj\7G\2\2")
        buf.write("de\7y\2\2ef\7j\2\2fg\7g\2\2gh\7t\2\2hj\7g\2\2i_\3\2\2")
        buf.write("\2id\3\2\2\2j\24\3\2\2\2kl\7C\2\2lp\7U\2\2mn\7c\2\2np")
        buf.write("\7u\2\2ok\3\2\2\2om\3\2\2\2p\26\3\2\2\2qr\7O\2\2rs\7K")
        buf.write("\2\2st\7P\2\2tu\7W\2\2u|\7U\2\2vw\7o\2\2wx\7k\2\2xy\7")
        buf.write("p\2\2yz\7w\2\2z|\7u\2\2{q\3\2\2\2{v\3\2\2\2|\30\3\2\2")
        buf.write("\2}~\7W\2\2~\177\7P\2\2\177\u0080\7K\2\2\u0080\u0081\7")
        buf.write("Q\2\2\u0081\u0088\7P\2\2\u0082\u0083\7w\2\2\u0083\u0084")
        buf.write("\7p\2\2\u0084\u0085\7k\2\2\u0085\u0086\7q\2\2\u0086\u0088")
        buf.write("\7p\2\2\u0087}\3\2\2\2\u0087\u0082\3\2\2\2\u0088\32\3")
        buf.write("\2\2\2\u0089\u008a\7L\2\2\u008a\u008b\7Q\2\2\u008b\u008c")
        buf.write("\7K\2\2\u008c\u0092\7P\2\2\u008d\u008e\7l\2\2\u008e\u008f")
        buf.write("\7q\2\2\u008f\u0090\7k\2\2\u0090\u0092\7p\2\2\u0091\u0089")
        buf.write("\3\2\2\2\u0091\u008d\3\2\2\2\u0092\34\3\2\2\2\u0093\u0094")
        buf.write("\7I\2\2\u0094\u0095\7T\2\2\u0095\u0096\7Q\2\2\u0096\u0097")
        buf.write("\7W\2\2\u0097\u0098\7R\2\2\u0098\u0099\7\"\2\2\u0099\u009a")
        buf.write("\7D\2\2\u009a\u00a4\7[\2\2\u009b\u009c\7i\2\2\u009c\u009d")
        buf.write("\7t\2\2\u009d\u009e\7q\2\2\u009e\u009f\7w\2\2\u009f\u00a0")
        buf.write("\7r\2\2\u00a0\u00a1\7\"\2\2\u00a1\u00a2\7d\2\2\u00a2\u00a4")
        buf.write("\7{\2\2\u00a3\u0093\3\2\2\2\u00a3\u009b\3\2\2\2\u00a4")
        buf.write("\36\3\2\2\2\u00a5\u00a6\7C\2\2\u00a6\u00a7\7P\2\2\u00a7")
        buf.write("\u00ac\7F\2\2\u00a8\u00a9\7c\2\2\u00a9\u00aa\7p\2\2\u00aa")
        buf.write("\u00ac\7f\2\2\u00ab\u00a5\3\2\2\2\u00ab\u00a8\3\2\2\2")
        buf.write("\u00ac \3\2\2\2\u00ad\u00ae\7Q\2\2\u00ae\u00b2\7T\2\2")
        buf.write("\u00af\u00b0\7q\2\2\u00b0\u00b2\7t\2\2\u00b1\u00ad\3\2")
        buf.write("\2\2\u00b1\u00af\3\2\2\2\u00b2\"\3\2\2\2\u00b3\u00b4\7")
        buf.write("P\2\2\u00b4\u00b5\7Q\2\2\u00b5\u00ba\7V\2\2\u00b6\u00b7")
        buf.write("\7p\2\2\u00b7\u00b8\7q\2\2\u00b8\u00ba\7v\2\2\u00b9\u00b3")
        buf.write("\3\2\2\2\u00b9\u00b6\3\2\2\2\u00ba$\3\2\2\2\u00bb\u00bc")
        buf.write("\7K\2\2\u00bc\u00c0\7P\2\2\u00bd\u00be\7k\2\2\u00be\u00c0")
        buf.write("\7p\2\2\u00bf\u00bb\3\2\2\2\u00bf\u00bd\3\2\2\2\u00c0")
        buf.write("&\3\2\2\2\u00c1\u00c2\7?\2\2\u00c2(\3\2\2\2\u00c3\u00c4")
        buf.write("\7#\2\2\u00c4\u00c5\7?\2\2\u00c5*\3\2\2\2\u00c6\u00c7")
        buf.write("\7>\2\2\u00c7,\3\2\2\2\u00c8\u00c9\7>\2\2\u00c9\u00ca")
        buf.write("\7?\2\2\u00ca.\3\2\2\2\u00cb\u00cc\7@\2\2\u00cc\60\3\2")
        buf.write("\2\2\u00cd\u00ce\7@\2\2\u00ce\u00cf\7?\2\2\u00cf\62\3")
        buf.write("\2\2\2\u00d0\u00d7\5\'\24\2\u00d1\u00d7\5)\25\2\u00d2")
        buf.write("\u00d7\5+\26\2\u00d3\u00d7\5-\27\2\u00d4\u00d7\5/\30\2")
        buf.write("\u00d5\u00d7\5\61\31\2\u00d6\u00d0\3\2\2\2\u00d6\u00d1")
        buf.write("\3\2\2\2\u00d6\u00d2\3\2\2\2\u00d6\u00d3\3\2\2\2\u00d6")
        buf.write("\u00d4\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7\64\3\2\2\2\u00d8")
        buf.write("\u00dc\t\2\2\2\u00d9\u00db\t\3\2\2\u00da\u00d9\3\2\2\2")
        buf.write("\u00db\u00de\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00dd\3")
        buf.write("\2\2\2\u00dd\66\3\2\2\2\u00de\u00dc\3\2\2\2\u00df\u00e1")
        buf.write("\t\4\2\2\u00e0\u00df\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2")
        buf.write("\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e4\3\2\2\2")
        buf.write("\u00e4\u00e5\b\34\2\2\u00e58\3\2\2\2\u00e6\u00e8\t\5\2")
        buf.write("\2\u00e7\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00e7")
        buf.write("\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea:\3\2\2\2\23\2S]io{")
        buf.write("\u0087\u0091\u00a3\u00ab\u00b1\u00b9\u00bf\u00d6\u00dc")
        buf.write("\u00e2\u00e9\3\b\2\2")
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
    SELECT = 7
    FROM = 8
    WHERE = 9
    AS = 10
    MINUS = 11
    UNION = 12
    JOIN = 13
    GROUPBY = 14
    AND = 15
    OR = 16
    NOT = 17
    IN = 18
    EQ = 19
    NEQ = 20
    LT = 21
    LE = 22
    GT = 23
    GE = 24
    COMP_OP = 25
    ID = 26
    WS = 27
    NEWLINE = 28

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "'.'", "'('", "')'", "';'", "'*'", "'='", "'!='", "'<'", 
            "'<='", "'>'", "'>='" ]

    symbolicNames = [ "<INVALID>",
            "LPAR", "RPAR", "COLON", "STAR", "SELECT", "FROM", "WHERE", 
            "AS", "MINUS", "UNION", "JOIN", "GROUPBY", "AND", "OR", "NOT", 
            "IN", "EQ", "NEQ", "LT", "LE", "GT", "GE", "COMP_OP", "ID", 
            "WS", "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "LPAR", "RPAR", "COLON", "STAR", "SELECT", 
                  "FROM", "WHERE", "AS", "MINUS", "UNION", "JOIN", "GROUPBY", 
                  "AND", "OR", "NOT", "IN", "EQ", "NEQ", "LT", "LE", "GT", 
                  "GE", "COMP_OP", "ID", "WS", "NEWLINE" ]

    grammarFileName = "miniSQL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



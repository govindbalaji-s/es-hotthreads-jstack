# Generated from HotThreads.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write("/\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\3\2\3\2\3\3\3\3\3\4\6\4\27\n\4\r\4\16\4\30\3")
        buf.write("\5\6\5\34\n\5\r\5\16\5\35\3\5\3\5\6\5\"\n\5\r\5\16\5#")
        buf.write("\5\5&\n\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\2\2\t\3\3\5")
        buf.write("\4\7\5\t\6\13\2\r\2\17\7\3\2\4\4\2\13\13\"\"\3\2\62;\2")
        buf.write("\60\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2")
        buf.write("\17\3\2\2\2\3\21\3\2\2\2\5\23\3\2\2\2\7\26\3\2\2\2\t\33")
        buf.write("\3\2\2\2\13)\3\2\2\2\r+\3\2\2\2\17-\3\2\2\2\21\22\7)\2")
        buf.write("\2\22\4\3\2\2\2\23\24\7\f\2\2\24\6\3\2\2\2\25\27\t\2\2")
        buf.write("\2\26\25\3\2\2\2\27\30\3\2\2\2\30\26\3\2\2\2\30\31\3\2")
        buf.write("\2\2\31\b\3\2\2\2\32\34\5\13\6\2\33\32\3\2\2\2\34\35\3")
        buf.write("\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36%\3\2\2\2\37!\5\r")
        buf.write("\7\2 \"\5\13\6\2! \3\2\2\2\"#\3\2\2\2#!\3\2\2\2#$\3\2")
        buf.write("\2\2$&\3\2\2\2%\37\3\2\2\2%&\3\2\2\2&\'\3\2\2\2\'(\7\'")
        buf.write("\2\2(\n\3\2\2\2)*\t\3\2\2*\f\3\2\2\2+,\7\60\2\2,\16\3")
        buf.write("\2\2\2-.\13\2\2\2.\20\3\2\2\2\7\2\30\35#%\2")
        return buf.getvalue()


class HotThreadsLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    Quote = 1
    NL = 2
    WS = 3
    Percentage = 4
    NoQuote = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'''", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "Quote", "NL", "WS", "Percentage", "NoQuote" ]

    ruleNames = [ "Quote", "NL", "WS", "Percentage", "Digit", "Dot", "NoQuote" ]

    grammarFileName = "HotThreads.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



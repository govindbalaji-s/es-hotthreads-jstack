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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\6")
        buf.write("\27\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\4\6\4\22\n\4\r\4\16\4\23\3\5\3\5\2\2\6\3\3\5")
        buf.write("\4\7\5\t\6\3\2\3\4\2\f\f))\2\27\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\3\13\3\2\2\2\5\16\3\2\2\2\7")
        buf.write("\21\3\2\2\2\t\25\3\2\2\2\13\f\7)\2\2\f\r\7\f\2\2\r\4\3")
        buf.write("\2\2\2\16\17\7\f\2\2\17\6\3\2\2\2\20\22\n\2\2\2\21\20")
        buf.write("\3\2\2\2\22\23\3\2\2\2\23\21\3\2\2\2\23\24\3\2\2\2\24")
        buf.write("\b\3\2\2\2\25\26\7)\2\2\26\n\3\2\2\2\4\2\23\2")
        return buf.getvalue()


class HotThreadsLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    NoQuote = 3
    Quote = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "''\n'", "'\n'", "'''" ]

    symbolicNames = [ "<INVALID>",
            "NoQuote", "Quote" ]

    ruleNames = [ "T__0", "T__1", "NoQuote", "Quote" ]

    grammarFileName = "HotThreads.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



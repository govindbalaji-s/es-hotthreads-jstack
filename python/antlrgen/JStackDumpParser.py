# Generated from JStackDump.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\5")
        buf.write(";\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\7\2\21\n\2\f\2\16\2\24\13\2\3\3\7\3\27\n\3\f\3\16")
        buf.write("\3\32\13\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\6\5$\n\5\r")
        buf.write("\5\16\5%\3\6\7\6)\n\6\f\6\16\6,\13\6\3\7\7\7/\n\7\f\7")
        buf.write("\16\7\62\13\7\3\7\3\7\7\7\66\n\7\f\7\16\79\13\7\3\7\2")
        buf.write("\2\b\2\4\6\b\n\f\2\2\2:\2\16\3\2\2\2\4\30\3\2\2\2\6\33")
        buf.write("\3\2\2\2\b\36\3\2\2\2\n*\3\2\2\2\f\60\3\2\2\2\16\22\5")
        buf.write("\4\3\2\17\21\5\6\4\2\20\17\3\2\2\2\21\24\3\2\2\2\22\20")
        buf.write("\3\2\2\2\22\23\3\2\2\2\23\3\3\2\2\2\24\22\3\2\2\2\25\27")
        buf.write("\5\f\7\2\26\25\3\2\2\2\27\32\3\2\2\2\30\26\3\2\2\2\30")
        buf.write("\31\3\2\2\2\31\5\3\2\2\2\32\30\3\2\2\2\33\34\5\b\5\2\34")
        buf.write("\35\5\n\6\2\35\7\3\2\2\2\36\37\7\5\2\2\37 \7\4\2\2 !\7")
        buf.write("\5\2\2!#\7\4\2\2\"$\7\3\2\2#\"\3\2\2\2$%\3\2\2\2%#\3\2")
        buf.write("\2\2%&\3\2\2\2&\t\3\2\2\2\')\5\f\7\2(\'\3\2\2\2),\3\2")
        buf.write("\2\2*(\3\2\2\2*+\3\2\2\2+\13\3\2\2\2,*\3\2\2\2-/\7\3\2")
        buf.write("\2.-\3\2\2\2/\62\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\61")
        buf.write("\63\3\2\2\2\62\60\3\2\2\2\63\67\7\4\2\2\64\66\7\3\2\2")
        buf.write("\65\64\3\2\2\2\669\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28")
        buf.write("\r\3\2\2\29\67\3\2\2\2\b\22\30%*\60\67")
        return buf.getvalue()


class JStackDumpParser ( Parser ):

    grammarFileName = "JStackDump.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\n'", "<INVALID>", "'\"'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "NoQuote", "Quote" ]

    RULE_dump = 0
    RULE_bplate = 1
    RULE_threadDump = 2
    RULE_threadHeader = 3
    RULE_threadInfo = 4
    RULE_quoteLessLine = 5

    ruleNames =  [ "dump", "bplate", "threadDump", "threadHeader", "threadInfo", 
                   "quoteLessLine" ]

    EOF = Token.EOF
    T__0=1
    NoQuote=2
    Quote=3

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DumpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bplate(self):
            return self.getTypedRuleContext(JStackDumpParser.BplateContext,0)


        def threadDump(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JStackDumpParser.ThreadDumpContext)
            else:
                return self.getTypedRuleContext(JStackDumpParser.ThreadDumpContext,i)


        def getRuleIndex(self):
            return JStackDumpParser.RULE_dump

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDump" ):
                listener.enterDump(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDump" ):
                listener.exitDump(self)




    def dump(self):

        localctx = JStackDumpParser.DumpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_dump)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.bplate()
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JStackDumpParser.Quote:
                self.state = 13
                self.threadDump()
                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BplateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def quoteLessLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JStackDumpParser.QuoteLessLineContext)
            else:
                return self.getTypedRuleContext(JStackDumpParser.QuoteLessLineContext,i)


        def getRuleIndex(self):
            return JStackDumpParser.RULE_bplate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBplate" ):
                listener.enterBplate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBplate" ):
                listener.exitBplate(self)




    def bplate(self):

        localctx = JStackDumpParser.BplateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_bplate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JStackDumpParser.T__0 or _la==JStackDumpParser.NoQuote:
                self.state = 19
                self.quoteLessLine()
                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThreadDumpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def threadHeader(self):
            return self.getTypedRuleContext(JStackDumpParser.ThreadHeaderContext,0)


        def threadInfo(self):
            return self.getTypedRuleContext(JStackDumpParser.ThreadInfoContext,0)


        def getRuleIndex(self):
            return JStackDumpParser.RULE_threadDump

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThreadDump" ):
                listener.enterThreadDump(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThreadDump" ):
                listener.exitThreadDump(self)




    def threadDump(self):

        localctx = JStackDumpParser.ThreadDumpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_threadDump)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.threadHeader()
            self.state = 26
            self.threadInfo()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThreadHeaderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token

        def Quote(self, i:int=None):
            if i is None:
                return self.getTokens(JStackDumpParser.Quote)
            else:
                return self.getToken(JStackDumpParser.Quote, i)

        def NoQuote(self, i:int=None):
            if i is None:
                return self.getTokens(JStackDumpParser.NoQuote)
            else:
                return self.getToken(JStackDumpParser.NoQuote, i)

        def getRuleIndex(self):
            return JStackDumpParser.RULE_threadHeader

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThreadHeader" ):
                listener.enterThreadHeader(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThreadHeader" ):
                listener.exitThreadHeader(self)




    def threadHeader(self):

        localctx = JStackDumpParser.ThreadHeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_threadHeader)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(JStackDumpParser.Quote)
            self.state = 29
            localctx.name = self.match(JStackDumpParser.NoQuote)
            self.state = 30
            self.match(JStackDumpParser.Quote)
            self.state = 31
            self.match(JStackDumpParser.NoQuote)
            self.state = 33 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 32
                    self.match(JStackDumpParser.T__0)

                else:
                    raise NoViableAltException(self)
                self.state = 35 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThreadInfoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def quoteLessLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JStackDumpParser.QuoteLessLineContext)
            else:
                return self.getTypedRuleContext(JStackDumpParser.QuoteLessLineContext,i)


        def getRuleIndex(self):
            return JStackDumpParser.RULE_threadInfo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThreadInfo" ):
                listener.enterThreadInfo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThreadInfo" ):
                listener.exitThreadInfo(self)




    def threadInfo(self):

        localctx = JStackDumpParser.ThreadInfoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_threadInfo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JStackDumpParser.T__0 or _la==JStackDumpParser.NoQuote:
                self.state = 37
                self.quoteLessLine()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuoteLessLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NoQuote(self):
            return self.getToken(JStackDumpParser.NoQuote, 0)

        def getRuleIndex(self):
            return JStackDumpParser.RULE_quoteLessLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuoteLessLine" ):
                listener.enterQuoteLessLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuoteLessLine" ):
                listener.exitQuoteLessLine(self)




    def quoteLessLine(self):

        localctx = JStackDumpParser.QuoteLessLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_quoteLessLine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JStackDumpParser.T__0:
                self.state = 43
                self.match(JStackDumpParser.T__0)
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
            self.match(JStackDumpParser.NoQuote)
            self.state = 53
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 50
                    self.match(JStackDumpParser.T__0) 
                self.state = 55
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






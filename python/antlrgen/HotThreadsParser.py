# Generated from HotThreads.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\6")
        buf.write("\67\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3")
        buf.write("\2\3\2\7\2\21\n\2\f\2\16\2\24\13\2\3\3\7\3\27\n\3\f\3")
        buf.write("\16\3\32\13\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\7\6")
        buf.write("%\n\6\f\6\16\6(\13\6\3\7\7\7+\n\7\f\7\16\7.\13\7\3\7\3")
        buf.write("\7\7\7\62\n\7\f\7\16\7\65\13\7\3\7\2\2\b\2\4\6\b\n\f\2")
        buf.write("\2\2\65\2\16\3\2\2\2\4\30\3\2\2\2\6\33\3\2\2\2\b\36\3")
        buf.write("\2\2\2\n&\3\2\2\2\f,\3\2\2\2\16\22\5\4\3\2\17\21\5\6\4")
        buf.write("\2\20\17\3\2\2\2\21\24\3\2\2\2\22\20\3\2\2\2\22\23\3\2")
        buf.write("\2\2\23\3\3\2\2\2\24\22\3\2\2\2\25\27\5\f\7\2\26\25\3")
        buf.write("\2\2\2\27\32\3\2\2\2\30\26\3\2\2\2\30\31\3\2\2\2\31\5")
        buf.write("\3\2\2\2\32\30\3\2\2\2\33\34\5\b\5\2\34\35\5\n\6\2\35")
        buf.write("\7\3\2\2\2\36\37\7\5\2\2\37 \7\6\2\2 !\7\5\2\2!\"\7\3")
        buf.write("\2\2\"\t\3\2\2\2#%\5\f\7\2$#\3\2\2\2%(\3\2\2\2&$\3\2\2")
        buf.write("\2&\'\3\2\2\2\'\13\3\2\2\2(&\3\2\2\2)+\7\4\2\2*)\3\2\2")
        buf.write("\2+.\3\2\2\2,*\3\2\2\2,-\3\2\2\2-/\3\2\2\2.,\3\2\2\2/")
        buf.write("\63\7\5\2\2\60\62\7\4\2\2\61\60\3\2\2\2\62\65\3\2\2\2")
        buf.write("\63\61\3\2\2\2\63\64\3\2\2\2\64\r\3\2\2\2\65\63\3\2\2")
        buf.write("\2\7\22\30&,\63")
        return buf.getvalue()


class HotThreadsParser ( Parser ):

    grammarFileName = "HotThreads.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "''\n'", "'\n'", "<INVALID>", "'''" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "NoQuote", 
                      "Quote" ]

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
    T__1=2
    NoQuote=3
    Quote=4

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
            return self.getTypedRuleContext(HotThreadsParser.BplateContext,0)


        def threadDump(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HotThreadsParser.ThreadDumpContext)
            else:
                return self.getTypedRuleContext(HotThreadsParser.ThreadDumpContext,i)


        def getRuleIndex(self):
            return HotThreadsParser.RULE_dump

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDump" ):
                listener.enterDump(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDump" ):
                listener.exitDump(self)




    def dump(self):

        localctx = HotThreadsParser.DumpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_dump)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.bplate()
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HotThreadsParser.NoQuote:
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
                return self.getTypedRuleContexts(HotThreadsParser.QuoteLessLineContext)
            else:
                return self.getTypedRuleContext(HotThreadsParser.QuoteLessLineContext,i)


        def getRuleIndex(self):
            return HotThreadsParser.RULE_bplate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBplate" ):
                listener.enterBplate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBplate" ):
                listener.exitBplate(self)




    def bplate(self):

        localctx = HotThreadsParser.BplateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_bplate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 19
                    self.quoteLessLine() 
                self.state = 24
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

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
            return self.getTypedRuleContext(HotThreadsParser.ThreadHeaderContext,0)


        def threadInfo(self):
            return self.getTypedRuleContext(HotThreadsParser.ThreadInfoContext,0)


        def getRuleIndex(self):
            return HotThreadsParser.RULE_threadDump

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThreadDump" ):
                listener.enterThreadDump(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThreadDump" ):
                listener.exitThreadDump(self)




    def threadDump(self):

        localctx = HotThreadsParser.ThreadDumpContext(self, self._ctx, self.state)
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

        def NoQuote(self, i:int=None):
            if i is None:
                return self.getTokens(HotThreadsParser.NoQuote)
            else:
                return self.getToken(HotThreadsParser.NoQuote, i)

        def Quote(self):
            return self.getToken(HotThreadsParser.Quote, 0)

        def getRuleIndex(self):
            return HotThreadsParser.RULE_threadHeader

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThreadHeader" ):
                listener.enterThreadHeader(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThreadHeader" ):
                listener.exitThreadHeader(self)




    def threadHeader(self):

        localctx = HotThreadsParser.ThreadHeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_threadHeader)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(HotThreadsParser.NoQuote)
            self.state = 29
            self.match(HotThreadsParser.Quote)
            self.state = 30
            self.match(HotThreadsParser.NoQuote)
            self.state = 31
            self.match(HotThreadsParser.T__0)
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
                return self.getTypedRuleContexts(HotThreadsParser.QuoteLessLineContext)
            else:
                return self.getTypedRuleContext(HotThreadsParser.QuoteLessLineContext,i)


        def getRuleIndex(self):
            return HotThreadsParser.RULE_threadInfo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThreadInfo" ):
                listener.enterThreadInfo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThreadInfo" ):
                listener.exitThreadInfo(self)




    def threadInfo(self):

        localctx = HotThreadsParser.ThreadInfoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_threadInfo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 33
                    self.quoteLessLine() 
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
            return self.getToken(HotThreadsParser.NoQuote, 0)

        def getRuleIndex(self):
            return HotThreadsParser.RULE_quoteLessLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuoteLessLine" ):
                listener.enterQuoteLessLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuoteLessLine" ):
                listener.exitQuoteLessLine(self)




    def quoteLessLine(self):

        localctx = HotThreadsParser.QuoteLessLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_quoteLessLine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HotThreadsParser.T__1:
                self.state = 39
                self.match(HotThreadsParser.T__1)
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
            self.match(HotThreadsParser.NoQuote)
            self.state = 49
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 46
                    self.match(HotThreadsParser.T__1) 
                self.state = 51
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






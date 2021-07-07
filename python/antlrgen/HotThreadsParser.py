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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\7")
        buf.write(";\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\7\2\23\n\2\f\2\16\2\26\13\2\3\3\6\3\31\n")
        buf.write("\3\r\3\16\3\32\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\6\7\6)\n\6\f\6\16\6,\13\6\3\7\3\7\3\7\3\7\6\7\62")
        buf.write("\n\7\r\7\16\7\63\3\b\6\b\67\n\b\r\b\16\b8\3\b\2\2\t\2")
        buf.write("\4\6\b\n\f\16\2\3\4\2\5\5\7\7\29\2\20\3\2\2\2\4\30\3\2")
        buf.write("\2\2\6\34\3\2\2\2\b\37\3\2\2\2\n*\3\2\2\2\f\61\3\2\2\2")
        buf.write("\16\66\3\2\2\2\20\24\5\4\3\2\21\23\5\6\4\2\22\21\3\2\2")
        buf.write("\2\23\26\3\2\2\2\24\22\3\2\2\2\24\25\3\2\2\2\25\3\3\2")
        buf.write("\2\2\26\24\3\2\2\2\27\31\5\f\7\2\30\27\3\2\2\2\31\32\3")
        buf.write("\2\2\2\32\30\3\2\2\2\32\33\3\2\2\2\33\5\3\2\2\2\34\35")
        buf.write("\5\b\5\2\35\36\5\n\6\2\36\7\3\2\2\2\37 \7\5\2\2 !\7\6")
        buf.write("\2\2!\"\5\16\b\2\"#\7\3\2\2#$\5\16\b\2$%\7\3\2\2%&\7\4")
        buf.write("\2\2&\t\3\2\2\2\')\5\f\7\2(\'\3\2\2\2),\3\2\2\2*(\3\2")
        buf.write("\2\2*+\3\2\2\2+\13\3\2\2\2,*\3\2\2\2-.\5\16\b\2./\7\4")
        buf.write("\2\2/\62\3\2\2\2\60\62\7\4\2\2\61-\3\2\2\2\61\60\3\2\2")
        buf.write("\2\62\63\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64\r\3\2")
        buf.write("\2\2\65\67\t\2\2\2\66\65\3\2\2\2\678\3\2\2\28\66\3\2\2")
        buf.write("\289\3\2\2\29\17\3\2\2\2\b\24\32*\61\638")
        return buf.getvalue()


class HotThreadsParser ( Parser ):

    grammarFileName = "HotThreads.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'''", "'\n'" ]

    symbolicNames = [ "<INVALID>", "Quote", "NL", "WS", "Percentage", "NoQuote" ]

    RULE_dump = 0
    RULE_bplate = 1
    RULE_threadDump = 2
    RULE_threadHeader = 3
    RULE_threadInfo = 4
    RULE_quoteLessLine = 5
    RULE_unquoted = 6

    ruleNames =  [ "dump", "bplate", "threadDump", "threadHeader", "threadInfo", 
                   "quoteLessLine", "unquoted" ]

    EOF = Token.EOF
    Quote=1
    NL=2
    WS=3
    Percentage=4
    NoQuote=5

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
            self.state = 14
            self.bplate()
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HotThreadsParser.WS:
                self.state = 15
                self.threadDump()
                self.state = 20
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
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 21
                    self.quoteLessLine()

                else:
                    raise NoViableAltException(self)
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
            self.state = 26
            self.threadHeader()
            self.state = 27
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
            self.name = None # UnquotedContext

        def WS(self):
            return self.getToken(HotThreadsParser.WS, 0)

        def Percentage(self):
            return self.getToken(HotThreadsParser.Percentage, 0)

        def unquoted(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HotThreadsParser.UnquotedContext)
            else:
                return self.getTypedRuleContext(HotThreadsParser.UnquotedContext,i)


        def Quote(self, i:int=None):
            if i is None:
                return self.getTokens(HotThreadsParser.Quote)
            else:
                return self.getToken(HotThreadsParser.Quote, i)

        def NL(self):
            return self.getToken(HotThreadsParser.NL, 0)

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
            self.state = 29
            self.match(HotThreadsParser.WS)
            self.state = 30
            self.match(HotThreadsParser.Percentage)
            self.state = 31
            self.unquoted()
            self.state = 32
            self.match(HotThreadsParser.Quote)
            self.state = 33
            localctx.name = self.unquoted()
            self.state = 34
            self.match(HotThreadsParser.Quote)
            self.state = 35
            self.match(HotThreadsParser.NL)
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
            self.state = 40
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 37
                    self.quoteLessLine() 
                self.state = 42
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

        def unquoted(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HotThreadsParser.UnquotedContext)
            else:
                return self.getTypedRuleContext(HotThreadsParser.UnquotedContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(HotThreadsParser.NL)
            else:
                return self.getToken(HotThreadsParser.NL, i)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 47
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [HotThreadsParser.WS, HotThreadsParser.NoQuote]:
                        self.state = 43
                        self.unquoted()
                        self.state = 44
                        self.match(HotThreadsParser.NL)
                        pass
                    elif token in [HotThreadsParser.NL]:
                        self.state = 46
                        self.match(HotThreadsParser.NL)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 49 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnquotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NoQuote(self, i:int=None):
            if i is None:
                return self.getTokens(HotThreadsParser.NoQuote)
            else:
                return self.getToken(HotThreadsParser.NoQuote, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(HotThreadsParser.WS)
            else:
                return self.getToken(HotThreadsParser.WS, i)

        def getRuleIndex(self):
            return HotThreadsParser.RULE_unquoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnquoted" ):
                listener.enterUnquoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnquoted" ):
                listener.exitUnquoted(self)




    def unquoted(self):

        localctx = HotThreadsParser.UnquotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_unquoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 51
                _la = self._input.LA(1)
                if not(_la==HotThreadsParser.WS or _la==HotThreadsParser.NoQuote):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 54 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==HotThreadsParser.WS or _la==HotThreadsParser.NoQuote):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






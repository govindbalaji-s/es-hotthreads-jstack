// Generated from JStackDump.g4 by ANTLR 4.5
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class JStackDumpParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.5", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, NoQuote=2, Quote=3;
	public static final int
		RULE_dump = 0, RULE_bplate = 1, RULE_threadDump = 2, RULE_threadHeader = 3, 
		RULE_threadInfo = 4, RULE_quoteLessLine = 5;
	public static final String[] ruleNames = {
		"dump", "bplate", "threadDump", "threadHeader", "threadInfo", "quoteLessLine"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'\n'", null, "'\"'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, "NoQuote", "Quote"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "JStackDump.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public JStackDumpParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class DumpContext extends ParserRuleContext {
		public BplateContext bplate() {
			return getRuleContext(BplateContext.class,0);
		}
		public List<ThreadDumpContext> threadDump() {
			return getRuleContexts(ThreadDumpContext.class);
		}
		public ThreadDumpContext threadDump(int i) {
			return getRuleContext(ThreadDumpContext.class,i);
		}
		public DumpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dump; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JStackDumpListener ) ((JStackDumpListener)listener).enterDump(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JStackDumpListener ) ((JStackDumpListener)listener).exitDump(this);
		}
	}

	public final DumpContext dump() throws RecognitionException {
		DumpContext _localctx = new DumpContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_dump);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(12);
			bplate();
			setState(16);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==Quote) {
				{
				{
				setState(13);
				threadDump();
				}
				}
				setState(18);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BplateContext extends ParserRuleContext {
		public List<QuoteLessLineContext> quoteLessLine() {
			return getRuleContexts(QuoteLessLineContext.class);
		}
		public QuoteLessLineContext quoteLessLine(int i) {
			return getRuleContext(QuoteLessLineContext.class,i);
		}
		public BplateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bplate; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JStackDumpListener ) ((JStackDumpListener)listener).enterBplate(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JStackDumpListener ) ((JStackDumpListener)listener).exitBplate(this);
		}
	}

	public final BplateContext bplate() throws RecognitionException {
		BplateContext _localctx = new BplateContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_bplate);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(22);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__0 || _la==NoQuote) {
				{
				{
				setState(19);
				quoteLessLine();
				}
				}
				setState(24);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ThreadDumpContext extends ParserRuleContext {
		public ThreadHeaderContext threadHeader() {
			return getRuleContext(ThreadHeaderContext.class,0);
		}
		public ThreadInfoContext threadInfo() {
			return getRuleContext(ThreadInfoContext.class,0);
		}
		public ThreadDumpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_threadDump; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JStackDumpListener ) ((JStackDumpListener)listener).enterThreadDump(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JStackDumpListener ) ((JStackDumpListener)listener).exitThreadDump(this);
		}
	}

	public final ThreadDumpContext threadDump() throws RecognitionException {
		ThreadDumpContext _localctx = new ThreadDumpContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_threadDump);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(25);
			threadHeader();
			setState(26);
			threadInfo();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ThreadHeaderContext extends ParserRuleContext {
		public List<TerminalNode> NoQuote() { return getTokens(JStackDumpParser.NoQuote); }
		public TerminalNode NoQuote(int i) {
			return getToken(JStackDumpParser.NoQuote, i);
		}
		public ThreadHeaderContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_threadHeader; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JStackDumpListener ) ((JStackDumpListener)listener).enterThreadHeader(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JStackDumpListener ) ((JStackDumpListener)listener).exitThreadHeader(this);
		}
	}

	public final ThreadHeaderContext threadHeader() throws RecognitionException {
		ThreadHeaderContext _localctx = new ThreadHeaderContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_threadHeader);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(28);
			match(Quote);
			setState(29);
			match(NoQuote);
			setState(30);
			match(Quote);
			setState(31);
			match(NoQuote);
			setState(33); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(32);
					match(T__0);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(35); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ThreadInfoContext extends ParserRuleContext {
		public List<QuoteLessLineContext> quoteLessLine() {
			return getRuleContexts(QuoteLessLineContext.class);
		}
		public QuoteLessLineContext quoteLessLine(int i) {
			return getRuleContext(QuoteLessLineContext.class,i);
		}
		public ThreadInfoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_threadInfo; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JStackDumpListener ) ((JStackDumpListener)listener).enterThreadInfo(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JStackDumpListener ) ((JStackDumpListener)listener).exitThreadInfo(this);
		}
	}

	public final ThreadInfoContext threadInfo() throws RecognitionException {
		ThreadInfoContext _localctx = new ThreadInfoContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_threadInfo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(40);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__0 || _la==NoQuote) {
				{
				{
				setState(37);
				quoteLessLine();
				}
				}
				setState(42);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class QuoteLessLineContext extends ParserRuleContext {
		public TerminalNode NoQuote() { return getToken(JStackDumpParser.NoQuote, 0); }
		public QuoteLessLineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_quoteLessLine; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JStackDumpListener ) ((JStackDumpListener)listener).enterQuoteLessLine(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JStackDumpListener ) ((JStackDumpListener)listener).exitQuoteLessLine(this);
		}
	}

	public final QuoteLessLineContext quoteLessLine() throws RecognitionException {
		QuoteLessLineContext _localctx = new QuoteLessLineContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_quoteLessLine);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(46);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__0) {
				{
				{
				setState(43);
				match(T__0);
				}
				}
				setState(48);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(49);
			match(NoQuote);
			setState(53);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(50);
					match(T__0);
					}
					} 
				}
				setState(55);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\5;\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2\3\2\7\2\21\n\2\f\2\16\2\24\13\2"+
		"\3\3\7\3\27\n\3\f\3\16\3\32\13\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\6\5$"+
		"\n\5\r\5\16\5%\3\6\7\6)\n\6\f\6\16\6,\13\6\3\7\7\7/\n\7\f\7\16\7\62\13"+
		"\7\3\7\3\7\7\7\66\n\7\f\7\16\79\13\7\3\7\2\2\b\2\4\6\b\n\f\2\2:\2\16\3"+
		"\2\2\2\4\30\3\2\2\2\6\33\3\2\2\2\b\36\3\2\2\2\n*\3\2\2\2\f\60\3\2\2\2"+
		"\16\22\5\4\3\2\17\21\5\6\4\2\20\17\3\2\2\2\21\24\3\2\2\2\22\20\3\2\2\2"+
		"\22\23\3\2\2\2\23\3\3\2\2\2\24\22\3\2\2\2\25\27\5\f\7\2\26\25\3\2\2\2"+
		"\27\32\3\2\2\2\30\26\3\2\2\2\30\31\3\2\2\2\31\5\3\2\2\2\32\30\3\2\2\2"+
		"\33\34\5\b\5\2\34\35\5\n\6\2\35\7\3\2\2\2\36\37\7\5\2\2\37 \7\4\2\2 !"+
		"\7\5\2\2!#\7\4\2\2\"$\7\3\2\2#\"\3\2\2\2$%\3\2\2\2%#\3\2\2\2%&\3\2\2\2"+
		"&\t\3\2\2\2\')\5\f\7\2(\'\3\2\2\2),\3\2\2\2*(\3\2\2\2*+\3\2\2\2+\13\3"+
		"\2\2\2,*\3\2\2\2-/\7\3\2\2.-\3\2\2\2/\62\3\2\2\2\60.\3\2\2\2\60\61\3\2"+
		"\2\2\61\63\3\2\2\2\62\60\3\2\2\2\63\67\7\4\2\2\64\66\7\3\2\2\65\64\3\2"+
		"\2\2\669\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28\r\3\2\2\29\67\3\2\2\2\b\22"+
		"\30%*\60\67";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
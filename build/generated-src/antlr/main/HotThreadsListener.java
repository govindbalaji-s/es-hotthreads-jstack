// Generated from HotThreads.g4 by ANTLR 4.5
import org.antlr.v4.runtime.misc.NotNull;
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link HotThreadsParser}.
 */
public interface HotThreadsListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link HotThreadsParser#dump}.
	 * @param ctx the parse tree
	 */
	void enterDump(HotThreadsParser.DumpContext ctx);
	/**
	 * Exit a parse tree produced by {@link HotThreadsParser#dump}.
	 * @param ctx the parse tree
	 */
	void exitDump(HotThreadsParser.DumpContext ctx);
	/**
	 * Enter a parse tree produced by {@link HotThreadsParser#bplate}.
	 * @param ctx the parse tree
	 */
	void enterBplate(HotThreadsParser.BplateContext ctx);
	/**
	 * Exit a parse tree produced by {@link HotThreadsParser#bplate}.
	 * @param ctx the parse tree
	 */
	void exitBplate(HotThreadsParser.BplateContext ctx);
	/**
	 * Enter a parse tree produced by {@link HotThreadsParser#threadDump}.
	 * @param ctx the parse tree
	 */
	void enterThreadDump(HotThreadsParser.ThreadDumpContext ctx);
	/**
	 * Exit a parse tree produced by {@link HotThreadsParser#threadDump}.
	 * @param ctx the parse tree
	 */
	void exitThreadDump(HotThreadsParser.ThreadDumpContext ctx);
	/**
	 * Enter a parse tree produced by {@link HotThreadsParser#threadHeader}.
	 * @param ctx the parse tree
	 */
	void enterThreadHeader(HotThreadsParser.ThreadHeaderContext ctx);
	/**
	 * Exit a parse tree produced by {@link HotThreadsParser#threadHeader}.
	 * @param ctx the parse tree
	 */
	void exitThreadHeader(HotThreadsParser.ThreadHeaderContext ctx);
	/**
	 * Enter a parse tree produced by {@link HotThreadsParser#threadInfo}.
	 * @param ctx the parse tree
	 */
	void enterThreadInfo(HotThreadsParser.ThreadInfoContext ctx);
	/**
	 * Exit a parse tree produced by {@link HotThreadsParser#threadInfo}.
	 * @param ctx the parse tree
	 */
	void exitThreadInfo(HotThreadsParser.ThreadInfoContext ctx);
	/**
	 * Enter a parse tree produced by {@link HotThreadsParser#quoteLessLine}.
	 * @param ctx the parse tree
	 */
	void enterQuoteLessLine(HotThreadsParser.QuoteLessLineContext ctx);
	/**
	 * Exit a parse tree produced by {@link HotThreadsParser#quoteLessLine}.
	 * @param ctx the parse tree
	 */
	void exitQuoteLessLine(HotThreadsParser.QuoteLessLineContext ctx);
}
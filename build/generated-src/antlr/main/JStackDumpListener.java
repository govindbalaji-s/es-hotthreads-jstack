// Generated from JStackDump.g4 by ANTLR 4.5
import org.antlr.v4.runtime.misc.NotNull;
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link JStackDumpParser}.
 */
public interface JStackDumpListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link JStackDumpParser#dump}.
	 * @param ctx the parse tree
	 */
	void enterDump(JStackDumpParser.DumpContext ctx);
	/**
	 * Exit a parse tree produced by {@link JStackDumpParser#dump}.
	 * @param ctx the parse tree
	 */
	void exitDump(JStackDumpParser.DumpContext ctx);
	/**
	 * Enter a parse tree produced by {@link JStackDumpParser#bplate}.
	 * @param ctx the parse tree
	 */
	void enterBplate(JStackDumpParser.BplateContext ctx);
	/**
	 * Exit a parse tree produced by {@link JStackDumpParser#bplate}.
	 * @param ctx the parse tree
	 */
	void exitBplate(JStackDumpParser.BplateContext ctx);
	/**
	 * Enter a parse tree produced by {@link JStackDumpParser#threadDump}.
	 * @param ctx the parse tree
	 */
	void enterThreadDump(JStackDumpParser.ThreadDumpContext ctx);
	/**
	 * Exit a parse tree produced by {@link JStackDumpParser#threadDump}.
	 * @param ctx the parse tree
	 */
	void exitThreadDump(JStackDumpParser.ThreadDumpContext ctx);
	/**
	 * Enter a parse tree produced by {@link JStackDumpParser#threadHeader}.
	 * @param ctx the parse tree
	 */
	void enterThreadHeader(JStackDumpParser.ThreadHeaderContext ctx);
	/**
	 * Exit a parse tree produced by {@link JStackDumpParser#threadHeader}.
	 * @param ctx the parse tree
	 */
	void exitThreadHeader(JStackDumpParser.ThreadHeaderContext ctx);
	/**
	 * Enter a parse tree produced by {@link JStackDumpParser#threadInfo}.
	 * @param ctx the parse tree
	 */
	void enterThreadInfo(JStackDumpParser.ThreadInfoContext ctx);
	/**
	 * Exit a parse tree produced by {@link JStackDumpParser#threadInfo}.
	 * @param ctx the parse tree
	 */
	void exitThreadInfo(JStackDumpParser.ThreadInfoContext ctx);
	/**
	 * Enter a parse tree produced by {@link JStackDumpParser#quoteLessLine}.
	 * @param ctx the parse tree
	 */
	void enterQuoteLessLine(JStackDumpParser.QuoteLessLineContext ctx);
	/**
	 * Exit a parse tree produced by {@link JStackDumpParser#quoteLessLine}.
	 * @param ctx the parse tree
	 */
	void exitQuoteLessLine(JStackDumpParser.QuoteLessLineContext ctx);
}
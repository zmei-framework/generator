// Generated from /Users/aleksandrrudakov/dev/generator/grammar/ZmeiLanguage.g4 by ANTLR 4.7
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ZmeiLanguageParser}.
 */
public interface ZmeiLanguageListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ZmeiLanguageParser#col_file}.
	 * @param ctx the parse tree
	 */
	void enterCol_file(ZmeiLanguageParser.Col_fileContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZmeiLanguageParser#col_file}.
	 * @param ctx the parse tree
	 */
	void exitCol_file(ZmeiLanguageParser.Col_fileContext ctx);
}
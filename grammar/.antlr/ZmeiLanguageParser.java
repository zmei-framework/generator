// Generated from /Users/aleksandrrudakov/dev/generator/grammar/ZmeiLanguage.g4 by ANTLR 4.7
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class ZmeiLanguageParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ANNOT_BLOCK=1, COMMENT_LINE=2, COMMENT_BLOCK=3, PAGE_IMPORTS=4, DOCUMENT_START=5, 
		PAGE_HDR_START=6, COL_HDR_START=7, GENERAL_COMMENT_LINE=8, GENERAL_COMMENT_BLOCK=9, 
		MODEL_IMPORTS=10, NEWLINE=11, WHITESPACE=12, ERRCHAR=13, COL_NAME=14, 
		COL_HDR_SEPARATOR=15, COL_HDR_ERRCHAR=16, COL_COMMENT_LINE=17, COL_COMMENT_BLOCK=18, 
		COL_STR_EXPR=19, COL_MODIFIER__STR=20, COL_MODIFIER__LOC=21, COL_MODIFIER__UNQ=22, 
		COL_MODIFIER__IDX=23, COL_MODIFIER__REQ=24, COL_MODIFIER__NNL=25, COL_FIELD=26, 
		COL_ANNOT=27, COL_FIELD_HELP=28, COL_FIELD_VNAME=29, COL_FIELD_SEPARATOR=30, 
		COL_ERRCHAR=31, FIELD_DECL_COMMENT_LINE=32, FIELD_DECL_COMMENT_BLOCK=33, 
		COL_FIELD_CALCULATED=34, COL_FIELD_TYPE=35, COL_FIELD_ARGS=36, FIELD_DECL_ERRCHAR=37, 
		PAGE_BASE=38, PAGE_NAME=39, PAGE_HDR_WHITESPACE=40, PAGE_HDR_ERRCHAR=41, 
		PAGE_HDR_SEPARATOR=42, PAGE_HDR_PART=43, PAGE_HDR_END=44, PAGE_HDR_PARTS_WHITESPACE=45, 
		PAGE_HDR_PARTS_ERRCHAR=46, PAGE_COMMENT_LINE=47, PAGE_COMMENT_BLOCK=48, 
		PAGE_FIELD=49, PAGE_FIELD_SEPARATOR=50, PAGE_CODE=51, PAGE_ANNOT=52, PAGE_ERRCHAR=53, 
		PYTHON_LINE_END=54, PYTHON_LINE_CODE=55, PYTHON_LINE_ERRCHAR=56, ANNOT_COMMENT_LINE=57, 
		ANNOT_COMMENT_BLOCK=58, ANNOT_DESCR=59, ANNOT_ERRCHAR=60;
	public static final int
		RULE_col_file = 0;
	public static final String[] ruleNames = {
		"col_file"
	};

	private static final String[] _LITERAL_NAMES = {
		null, null, null, null, null, null, "'['", "'#'", null, null, null, null, 
		null, null, null, null, null, null, null, null, "'='", "'$'", "'&'", "'!'", 
		"'*'", "'~'", null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, "':'", null, "']'", null, null, null, 
		null, null, null, null, null, null, "';'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "ANNOT_BLOCK", "COMMENT_LINE", "COMMENT_BLOCK", "PAGE_IMPORTS", 
		"DOCUMENT_START", "PAGE_HDR_START", "COL_HDR_START", "GENERAL_COMMENT_LINE", 
		"GENERAL_COMMENT_BLOCK", "MODEL_IMPORTS", "NEWLINE", "WHITESPACE", "ERRCHAR", 
		"COL_NAME", "COL_HDR_SEPARATOR", "COL_HDR_ERRCHAR", "COL_COMMENT_LINE", 
		"COL_COMMENT_BLOCK", "COL_STR_EXPR", "COL_MODIFIER__STR", "COL_MODIFIER__LOC", 
		"COL_MODIFIER__UNQ", "COL_MODIFIER__IDX", "COL_MODIFIER__REQ", "COL_MODIFIER__NNL", 
		"COL_FIELD", "COL_ANNOT", "COL_FIELD_HELP", "COL_FIELD_VNAME", "COL_FIELD_SEPARATOR", 
		"COL_ERRCHAR", "FIELD_DECL_COMMENT_LINE", "FIELD_DECL_COMMENT_BLOCK", 
		"COL_FIELD_CALCULATED", "COL_FIELD_TYPE", "COL_FIELD_ARGS", "FIELD_DECL_ERRCHAR", 
		"PAGE_BASE", "PAGE_NAME", "PAGE_HDR_WHITESPACE", "PAGE_HDR_ERRCHAR", "PAGE_HDR_SEPARATOR", 
		"PAGE_HDR_PART", "PAGE_HDR_END", "PAGE_HDR_PARTS_WHITESPACE", "PAGE_HDR_PARTS_ERRCHAR", 
		"PAGE_COMMENT_LINE", "PAGE_COMMENT_BLOCK", "PAGE_FIELD", "PAGE_FIELD_SEPARATOR", 
		"PAGE_CODE", "PAGE_ANNOT", "PAGE_ERRCHAR", "PYTHON_LINE_END", "PYTHON_LINE_CODE", 
		"PYTHON_LINE_ERRCHAR", "ANNOT_COMMENT_LINE", "ANNOT_COMMENT_BLOCK", "ANNOT_DESCR", 
		"ANNOT_ERRCHAR"
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
	public String getGrammarFileName() { return "ZmeiLanguage.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ZmeiLanguageParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class Col_fileContext extends ParserRuleContext {
		public List<TerminalNode> NEWLINE() { return getTokens(ZmeiLanguageParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(ZmeiLanguageParser.NEWLINE, i);
		}
		public Col_fileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_col_file; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ZmeiLanguageListener ) ((ZmeiLanguageListener)listener).enterCol_file(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ZmeiLanguageListener ) ((ZmeiLanguageListener)listener).exitCol_file(this);
		}
	}

	public final Col_fileContext col_file() throws RecognitionException {
		Col_fileContext _localctx = new Col_fileContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_col_file);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(5);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NEWLINE) {
				{
				{
				setState(2);
				match(NEWLINE);
				}
				}
				setState(7);
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

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3>\13\4\2\t\2\3\2\7"+
		"\2\6\n\2\f\2\16\2\t\13\2\3\2\2\2\3\2\2\2\2\n\2\7\3\2\2\2\4\6\7\r\2\2\5"+
		"\4\3\2\2\2\6\t\3\2\2\2\7\5\3\2\2\2\7\b\3\2\2\2\b\3\3\2\2\2\t\7\3\2\2\2"+
		"\3\7";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
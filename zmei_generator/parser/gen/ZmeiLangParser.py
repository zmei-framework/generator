# Generated from /Users/aleksandrrudakov/dev/generator/grammar/ZmeiLangParser.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3[")
        buf.write("\u02bb\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\tU\4V\t")
        buf.write("V\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\3\2\5\2\u00ba")
        buf.write("\n\2\3\2\7\2\u00bd\n\2\f\2\16\2\u00c0\13\2\3\2\7\2\u00c3")
        buf.write("\n\2\f\2\16\2\u00c6\13\2\3\2\7\2\u00c9\n\2\f\2\16\2\u00cc")
        buf.write("\13\2\3\2\5\2\u00cf\n\2\3\2\7\2\u00d2\n\2\f\2\16\2\u00d5")
        buf.write("\13\2\3\2\7\2\u00d8\n\2\f\2\16\2\u00db\13\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\6\3\6\7\6\u00e9\n\6\f")
        buf.write("\6\16\6\u00ec\13\6\3\6\3\6\3\7\3\7\5\7\u00f2\n\7\3\7\3")
        buf.write("\7\5\7\u00f6\n\7\3\7\3\7\5\7\u00fa\n\7\3\7\3\7\5\7\u00fe")
        buf.write("\n\7\5\7\u0100\n\7\3\7\3\7\3\7\7\7\u0105\n\7\f\7\16\7")
        buf.write("\u0108\13\7\3\7\7\7\u010b\n\7\f\7\16\7\u010e\13\7\3\7")
        buf.write("\5\7\u0111\n\7\3\7\7\7\u0114\n\7\f\7\16\7\u0117\13\7\3")
        buf.write("\7\5\7\u011a\n\7\3\7\7\7\u011d\n\7\f\7\16\7\u0120\13\7")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r")
        buf.write("\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\20\3\20\6\20\u0138")
        buf.write("\n\20\r\20\16\20\u0139\3\20\5\20\u013d\n\20\3\21\3\21")
        buf.write("\3\22\3\22\3\23\3\23\5\23\u0145\n\23\3\23\7\23\u0148\n")
        buf.write("\23\f\23\16\23\u014b\13\23\3\23\7\23\u014e\n\23\f\23\16")
        buf.write("\23\u0151\13\23\3\24\3\24\3\24\6\24\u0156\n\24\r\24\16")
        buf.write("\24\u0157\3\24\5\24\u015b\n\24\3\25\3\25\5\25\u015f\n")
        buf.write("\25\3\25\3\25\5\25\u0163\n\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\5\26\u016c\n\26\3\27\3\27\3\30\3\30\3\30\3")
        buf.write("\31\3\31\3\32\7\32\u0176\n\32\f\32\16\32\u0179\13\32\3")
        buf.write("\32\3\32\3\32\3\32\5\32\u017f\n\32\3\32\5\32\u0182\n\32")
        buf.write("\3\32\5\32\u0185\n\32\3\32\6\32\u0188\n\32\r\32\16\32")
        buf.write("\u0189\3\32\5\32\u018d\n\32\3\33\3\33\3\33\3\34\3\34\3")
        buf.write("\35\3\35\3\36\6\36\u0197\n\36\r\36\16\36\u0198\3\36\3")
        buf.write("\36\5\36\u019d\n\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"")
        buf.write("\3\"\3#\3#\5#\u01ab\n#\3#\5#\u01ae\n#\3#\7#\u01b1\n#\f")
        buf.write("#\16#\u01b4\13#\3$\3$\3$\3%\3%\3&\5&\u01bc\n&\3&\3&\5")
        buf.write("&\u01c0\n&\3&\5&\u01c3\n&\7&\u01c5\n&\f&\16&\u01c8\13")
        buf.write("&\3\'\3\'\3\'\7\'\u01cd\n\'\f\'\16\'\u01d0\13\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u01dc\n\'\f\'\16")
        buf.write("\'\u01df\13\'\3\'\3\'\5\'\u01e3\n\'\3(\3(\5(\u01e7\n(")
        buf.write("\3)\3)\5)\u01eb\n)\3*\3*\3+\3+\3,\3,\3-\3-\3-\3-\3.\3")
        buf.write(".\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\5\60\u0210\n\60\3\61\3\61\3\62\3\62\3\63\3\63\3")
        buf.write("\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:")
        buf.write("\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3@\3@\3@\5@\u0235")
        buf.write("\n@\3@\3@\5@\u0239\n@\3A\3A\3B\3B\3B\3B\3B\7B\u0242\n")
        buf.write("B\fB\16B\u0245\13B\3C\5C\u0248\nC\3C\3C\3D\3D\3E\3E\3")
        buf.write("E\3F\3F\3F\3F\3F\5F\u0256\nF\3G\3G\3G\3G\3G\7G\u025d\n")
        buf.write("G\fG\16G\u0260\13G\3H\5H\u0263\nH\3H\3H\3I\3I\3J\3J\3")
        buf.write("J\3K\3K\3K\3K\3K\3L\3L\3L\7L\u0274\nL\fL\16L\u0277\13")
        buf.write("L\3M\3M\3N\3N\3N\3N\3N\5N\u0280\nN\3O\3O\3P\3P\3P\3P\3")
        buf.write("P\5P\u0289\nP\3Q\3Q\3R\3R\3R\7R\u0290\nR\fR\16R\u0293")
        buf.write("\13R\3S\3S\3S\3S\3T\3T\3U\3U\3U\3V\7V\u029f\nV\fV\16V")
        buf.write("\u02a2\13V\3W\3W\3X\3X\3X\3X\5X\u02aa\nX\3X\5X\u02ad\n")
        buf.write("X\3X\3X\3Y\3Y\3Z\3Z\3Z\3[\3[\3\\\3\\\3\\\3\\\2\2]\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084")
        buf.write("\u0086\u0088\u008a\u008c\u008e\u0090\u0092\u0094\u0096")
        buf.write("\u0098\u009a\u009c\u009e\u00a0\u00a2\u00a4\u00a6\u00a8")
        buf.write("\u00aa\u00ac\u00ae\u00b0\u00b2\u00b4\u00b6\2\20\5\2  ")
        buf.write("##\67\67\4\2!!\66\66\3\2./\4\2!!./\3\2\61\62\3\289\3\2")
        buf.write("=B\3\2MN\3\2WX\5\2\37\37CCPP\4\2\37\37CC\4\2\"\"++\4\2")
        buf.write("\20\20\26\26\3\2\33\35\2\u02b4\2\u00b9\3\2\2\2\4\u00de")
        buf.write("\3\2\2\2\6\u00e1\3\2\2\2\b\u00e4\3\2\2\2\n\u00e6\3\2\2")
        buf.write("\2\f\u00ef\3\2\2\2\16\u0121\3\2\2\2\20\u0124\3\2\2\2\22")
        buf.write("\u0127\3\2\2\2\24\u0129\3\2\2\2\26\u012b\3\2\2\2\30\u012d")
        buf.write("\3\2\2\2\32\u012f\3\2\2\2\34\u0131\3\2\2\2\36\u0133\3")
        buf.write("\2\2\2 \u013e\3\2\2\2\"\u0140\3\2\2\2$\u0142\3\2\2\2&")
        buf.write("\u0152\3\2\2\2(\u015c\3\2\2\2*\u0167\3\2\2\2,\u016d\3")
        buf.write("\2\2\2.\u016f\3\2\2\2\60\u0172\3\2\2\2\62\u0177\3\2\2")
        buf.write("\2\64\u018e\3\2\2\2\66\u0191\3\2\2\28\u0193\3\2\2\2:\u019c")
        buf.write("\3\2\2\2<\u019e\3\2\2\2>\u01a1\3\2\2\2@\u01a4\3\2\2\2")
        buf.write("B\u01a6\3\2\2\2D\u01a8\3\2\2\2F\u01b5\3\2\2\2H\u01b8\3")
        buf.write("\2\2\2J\u01bb\3\2\2\2L\u01e2\3\2\2\2N\u01e6\3\2\2\2P\u01ea")
        buf.write("\3\2\2\2R\u01ec\3\2\2\2T\u01ee\3\2\2\2V\u01f0\3\2\2\2")
        buf.write("X\u01f2\3\2\2\2Z\u01f6\3\2\2\2\\\u01f8\3\2\2\2^\u020f")
        buf.write("\3\2\2\2`\u0211\3\2\2\2b\u0213\3\2\2\2d\u0215\3\2\2\2")
        buf.write("f\u0217\3\2\2\2h\u0219\3\2\2\2j\u021b\3\2\2\2l\u021d\3")
        buf.write("\2\2\2n\u021f\3\2\2\2p\u0221\3\2\2\2r\u0223\3\2\2\2t\u0225")
        buf.write("\3\2\2\2v\u0227\3\2\2\2x\u0229\3\2\2\2z\u022b\3\2\2\2")
        buf.write("|\u022d\3\2\2\2~\u022f\3\2\2\2\u0080\u023a\3\2\2\2\u0082")
        buf.write("\u023c\3\2\2\2\u0084\u0247\3\2\2\2\u0086\u024b\3\2\2\2")
        buf.write("\u0088\u024d\3\2\2\2\u008a\u0250\3\2\2\2\u008c\u0257\3")
        buf.write("\2\2\2\u008e\u0262\3\2\2\2\u0090\u0266\3\2\2\2\u0092\u0268")
        buf.write("\3\2\2\2\u0094\u026b\3\2\2\2\u0096\u0270\3\2\2\2\u0098")
        buf.write("\u0278\3\2\2\2\u009a\u027a\3\2\2\2\u009c\u0281\3\2\2\2")
        buf.write("\u009e\u0283\3\2\2\2\u00a0\u028a\3\2\2\2\u00a2\u028c\3")
        buf.write("\2\2\2\u00a4\u0294\3\2\2\2\u00a6\u0298\3\2\2\2\u00a8\u029a")
        buf.write("\3\2\2\2\u00aa\u02a0\3\2\2\2\u00ac\u02a3\3\2\2\2\u00ae")
        buf.write("\u02a5\3\2\2\2\u00b0\u02b0\3\2\2\2\u00b2\u02b2\3\2\2\2")
        buf.write("\u00b4\u02b5\3\2\2\2\u00b6\u02b7\3\2\2\2\u00b8\u00ba\5")
        buf.write("\4\3\2\u00b9\u00b8\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00be")
        buf.write("\3\2\2\2\u00bb\u00bd\7\37\2\2\u00bc\u00bb\3\2\2\2\u00bd")
        buf.write("\u00c0\3\2\2\2\u00be\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2")
        buf.write("\u00bf\u00c4\3\2\2\2\u00c0\u00be\3\2\2\2\u00c1\u00c3\5")
        buf.write("D#\2\u00c2\u00c1\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4\u00c2")
        buf.write("\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00ca\3\2\2\2\u00c6")
        buf.write("\u00c4\3\2\2\2\u00c7\u00c9\5\f\7\2\u00c8\u00c7\3\2\2\2")
        buf.write("\u00c9\u00cc\3\2\2\2\u00ca\u00c8\3\2\2\2\u00ca\u00cb\3")
        buf.write("\2\2\2\u00cb\u00ce\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cd\u00cf")
        buf.write("\5\6\4\2\u00ce\u00cd\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf")
        buf.write("\u00d3\3\2\2\2\u00d0\u00d2\5$\23\2\u00d1\u00d0\3\2\2\2")
        buf.write("\u00d2\u00d5\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3")
        buf.write("\2\2\2\u00d4\u00d9\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d6\u00d8")
        buf.write("\7\37\2\2\u00d7\u00d6\3\2\2\2\u00d8\u00db\3\2\2\2\u00d9")
        buf.write("\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00dc\3\2\2\2")
        buf.write("\u00db\u00d9\3\2\2\2\u00dc\u00dd\7\2\2\3\u00dd\3\3\2\2")
        buf.write("\2\u00de\u00df\7\4\2\2\u00df\u00e0\5\b\5\2\u00e0\5\3\2")
        buf.write("\2\2\u00e1\u00e2\7\4\2\2\u00e2\u00e3\5\b\5\2\u00e3\7\3")
        buf.write("\2\2\2\u00e4\u00e5\5\n\6\2\u00e5\t\3\2\2\2\u00e6\u00ea")
        buf.write("\7E\2\2\u00e7\u00e9\7G\2\2\u00e8\u00e7\3\2\2\2\u00e9\u00ec")
        buf.write("\3\2\2\2\u00ea\u00e8\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb")
        buf.write("\u00ed\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ed\u00ee\7H\2\2")
        buf.write("\u00ee\13\3\2\2\2\u00ef\u00f1\7)\2\2\u00f0\u00f2\5\16")
        buf.write("\b\2\u00f1\u00f0\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f3")
        buf.write("\3\2\2\2\u00f3\u00f5\5\34\17\2\u00f4\u00f6\5\20\t\2\u00f5")
        buf.write("\u00f4\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00ff\3\2\2\2")
        buf.write("\u00f7\u00f9\7&\2\2\u00f8\u00fa\5\30\r\2\u00f9\u00f8\3")
        buf.write("\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fd\3\2\2\2\u00fb\u00fc")
        buf.write("\7&\2\2\u00fc\u00fe\5\26\f\2\u00fd\u00fb\3\2\2\2\u00fd")
        buf.write("\u00fe\3\2\2\2\u00fe\u0100\3\2\2\2\u00ff\u00f7\3\2\2\2")
        buf.write("\u00ff\u0100\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u0102\7")
        buf.write("*\2\2\u0102\u0106\7\37\2\2\u0103\u0105\5\36\20\2\u0104")
        buf.write("\u0103\3\2\2\2\u0105\u0108\3\2\2\2\u0106\u0104\3\2\2\2")
        buf.write("\u0106\u0107\3\2\2\2\u0107\u010c\3\2\2\2\u0108\u0106\3")
        buf.write("\2\2\2\u0109\u010b\5D#\2\u010a\u0109\3\2\2\2\u010b\u010e")
        buf.write("\3\2\2\2\u010c\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010d")
        buf.write("\u0110\3\2\2\2\u010e\u010c\3\2\2\2\u010f\u0111\5\32\16")
        buf.write("\2\u0110\u010f\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u0115")
        buf.write("\3\2\2\2\u0112\u0114\5D#\2\u0113\u0112\3\2\2\2\u0114\u0117")
        buf.write("\3\2\2\2\u0115\u0113\3\2\2\2\u0115\u0116\3\2\2\2\u0116")
        buf.write("\u0119\3\2\2\2\u0117\u0115\3\2\2\2\u0118\u011a\5\24\13")
        buf.write("\2\u0119\u0118\3\2\2\2\u0119\u011a\3\2\2\2\u011a\u011e")
        buf.write("\3\2\2\2\u011b\u011d\7\37\2\2\u011c\u011b\3\2\2\2\u011d")
        buf.write("\u0120\3\2\2\2\u011e\u011c\3\2\2\2\u011e\u011f\3\2\2\2")
        buf.write("\u011f\r\3\2\2\2\u0120\u011e\3\2\2\2\u0121\u0122\7!\2")
        buf.write("\2\u0122\u0123\7\61\2\2\u0123\17\3\2\2\2\u0124\u0125\7")
        buf.write("\5\2\2\u0125\u0126\5\22\n\2\u0126\21\3\2\2\2\u0127\u0128")
        buf.write("\7!\2\2\u0128\23\3\2\2\2\u0129\u012a\5L\'\2\u012a\25\3")
        buf.write("\2\2\2\u012b\u012c\t\2\2\2\u012c\27\3\2\2\2\u012d\u012e")
        buf.write("\t\3\2\2\u012e\31\3\2\2\2\u012f\u0130\5\n\6\2\u0130\33")
        buf.write("\3\2\2\2\u0131\u0132\7!\2\2\u0132\35\3\2\2\2\u0133\u0134")
        buf.write("\5 \21\2\u0134\u0135\78\2\2\u0135\u013c\5\"\22\2\u0136")
        buf.write("\u0138\7\37\2\2\u0137\u0136\3\2\2\2\u0138\u0139\3\2\2")
        buf.write("\2\u0139\u0137\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u013d")
        buf.write("\3\2\2\2\u013b\u013d\7\2\2\3\u013c\u0137\3\2\2\2\u013c")
        buf.write("\u013b\3\2\2\2\u013d\37\3\2\2\2\u013e\u013f\7!\2\2\u013f")
        buf.write("!\3\2\2\2\u0140\u0141\7I\2\2\u0141#\3\2\2\2\u0142\u0144")
        buf.write("\5(\25\2\u0143\u0145\5&\24\2\u0144\u0143\3\2\2\2\u0144")
        buf.write("\u0145\3\2\2\2\u0145\u0149\3\2\2\2\u0146\u0148\5\62\32")
        buf.write("\2\u0147\u0146\3\2\2\2\u0148\u014b\3\2\2\2\u0149\u0147")
        buf.write("\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u014f\3\2\2\2\u014b")
        buf.write("\u0149\3\2\2\2\u014c\u014e\5D#\2\u014d\u014c\3\2\2\2\u014e")
        buf.write("\u0151\3\2\2\2\u014f\u014d\3\2\2\2\u014f\u0150\3\2\2\2")
        buf.write("\u0150%\3\2\2\2\u0151\u014f\3\2\2\2\u0152\u0153\7=\2\2")
        buf.write("\u0153\u015a\t\4\2\2\u0154\u0156\7\37\2\2\u0155\u0154")
        buf.write("\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0155\3\2\2\2\u0157")
        buf.write("\u0158\3\2\2\2\u0158\u015b\3\2\2\2\u0159\u015b\7\2\2\3")
        buf.write("\u015a\u0155\3\2\2\2\u015a\u0159\3\2\2\2\u015b\'\3\2\2")
        buf.write("\2\u015c\u015e\7\63\2\2\u015d\u015f\5.\30\2\u015e\u015d")
        buf.write("\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u0160\3\2\2\2\u0160")
        buf.write("\u0162\5\60\31\2\u0161\u0163\5*\26\2\u0162\u0161\3\2\2")
        buf.write("\2\u0162\u0163\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0165")
        buf.write("\7\65\2\2\u0165\u0166\7\37\2\2\u0166)\3\2\2\2\u0167\u0168")
        buf.write("\7&\2\2\u0168\u016b\5,\27\2\u0169\u016a\7<\2\2\u016a\u016c")
        buf.write("\5,\27\2\u016b\u0169\3\2\2\2\u016b\u016c\3\2\2\2\u016c")
        buf.write("+\3\2\2\2\u016d\u016e\t\5\2\2\u016e-\3\2\2\2\u016f\u0170")
        buf.write("\7!\2\2\u0170\u0171\t\6\2\2\u0171/\3\2\2\2\u0172\u0173")
        buf.write("\7!\2\2\u0173\61\3\2\2\2\u0174\u0176\5B\"\2\u0175\u0174")
        buf.write("\3\2\2\2\u0176\u0179\3\2\2\2\u0177\u0175\3\2\2\2\u0177")
        buf.write("\u0178\3\2\2\2\u0178\u017a\3\2\2\2\u0179\u0177\3\2\2\2")
        buf.write("\u017a\u017e\5@!\2\u017b\u017c\7&\2\2\u017c\u017f\5^\60")
        buf.write("\2\u017d\u017f\5\64\33\2\u017e\u017b\3\2\2\2\u017e\u017d")
        buf.write("\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0181\3\2\2\2\u0180")
        buf.write("\u0182\5> \2\u0181\u0180\3\2\2\2\u0181\u0182\3\2\2\2\u0182")
        buf.write("\u0184\3\2\2\2\u0183\u0185\5<\37\2\u0184\u0183\3\2\2\2")
        buf.write("\u0184\u0185\3\2\2\2\u0185\u018c\3\2\2\2\u0186\u0188\7")
        buf.write("\37\2\2\u0187\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189")
        buf.write("\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018d\3\2\2\2")
        buf.write("\u018b\u018d\7\2\2\3\u018c\u0187\3\2\2\2\u018c\u018b\3")
        buf.write("\2\2\2\u018d\63\3\2\2\2\u018e\u018f\5\66\34\2\u018f\u0190")
        buf.write("\58\35\2\u0190\65\3\2\2\2\u0191\u0192\t\7\2\2\u0192\67")
        buf.write("\3\2\2\2\u0193\u0194\7I\2\2\u01949\3\2\2\2\u0195\u0197")
        buf.write("\7!\2\2\u0196\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198")
        buf.write("\u0196\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u019d\3\2\2\2")
        buf.write("\u019a\u019d\7.\2\2\u019b\u019d\7/\2\2\u019c\u0196\3\2")
        buf.write("\2\2\u019c\u019a\3\2\2\2\u019c\u019b\3\2\2\2\u019d;\3")
        buf.write("\2\2\2\u019e\u019f\7+\2\2\u019f\u01a0\5:\36\2\u01a0=\3")
        buf.write("\2\2\2\u01a1\u01a2\7<\2\2\u01a2\u01a3\5:\36\2\u01a3?\3")
        buf.write("\2\2\2\u01a4\u01a5\7!\2\2\u01a5A\3\2\2\2\u01a6\u01a7\t")
        buf.write("\b\2\2\u01a7C\3\2\2\2\u01a8\u01aa\7\64\2\2\u01a9\u01ab")
        buf.write("\5F$\2\u01aa\u01a9\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ad")
        buf.write("\3\2\2\2\u01ac\u01ae\5H%\2\u01ad\u01ac\3\2\2\2\u01ad\u01ae")
        buf.write("\3\2\2\2\u01ae\u01b2\3\2\2\2\u01af\u01b1\7\37\2\2\u01b0")
        buf.write("\u01af\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2\u01b0\3\2\2\2")
        buf.write("\u01b2\u01b3\3\2\2\2\u01b3E\3\2\2\2\u01b4\u01b2\3\2\2")
        buf.write("\2\u01b5\u01b6\7-\2\2\u01b6\u01b7\7!\2\2\u01b7G\3\2\2")
        buf.write("\2\u01b8\u01b9\5\n\6\2\u01b9I\3\2\2\2\u01ba\u01bc\5Z.")
        buf.write("\2\u01bb\u01ba\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01c6")
        buf.write("\3\2\2\2\u01bd\u01c0\5L\'\2\u01be\u01c0\5V,\2\u01bf\u01bd")
        buf.write("\3\2\2\2\u01bf\u01be\3\2\2\2\u01c0\u01c2\3\2\2\2\u01c1")
        buf.write("\u01c3\5Z.\2\u01c2\u01c1\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3")
        buf.write("\u01c5\3\2\2\2\u01c4\u01bf\3\2\2\2\u01c5\u01c8\3\2\2\2")
        buf.write("\u01c6\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7K\3\2\2")
        buf.write("\2\u01c8\u01c6\3\2\2\2\u01c9\u01ca\7F\2\2\u01ca\u01ce")
        buf.write("\5N(\2\u01cb\u01cd\5X-\2\u01cc\u01cb\3\2\2\2\u01cd\u01d0")
        buf.write("\3\2\2\2\u01ce\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf")
        buf.write("\u01d1\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d1\u01d2\7R\2\2")
        buf.write("\u01d2\u01d3\5J&\2\u01d3\u01d4\7F\2\2\u01d4\u01d5\7U\2")
        buf.write("\2\u01d5\u01d6\5P)\2\u01d6\u01d7\7R\2\2\u01d7\u01e3\3")
        buf.write("\2\2\2\u01d8\u01d9\7F\2\2\u01d9\u01dd\5N(\2\u01da\u01dc")
        buf.write("\5X-\2\u01db\u01da\3\2\2\2\u01dc\u01df\3\2\2\2\u01dd\u01db")
        buf.write("\3\2\2\2\u01dd\u01de\3\2\2\2\u01de\u01e0\3\2\2\2\u01df")
        buf.write("\u01dd\3\2\2\2\u01e0\u01e1\7T\2\2\u01e1\u01e3\3\2\2\2")
        buf.write("\u01e2\u01c9\3\2\2\2\u01e2\u01d8\3\2\2\2\u01e3M\3\2\2")
        buf.write("\2\u01e4\u01e7\5T+\2\u01e5\u01e7\5R*\2\u01e6\u01e4\3\2")
        buf.write("\2\2\u01e6\u01e5\3\2\2\2\u01e7O\3\2\2\2\u01e8\u01eb\5")
        buf.write("T+\2\u01e9\u01eb\5R*\2\u01ea\u01e8\3\2\2\2\u01ea\u01e9")
        buf.write("\3\2\2\2\u01ebQ\3\2\2\2\u01ec\u01ed\7Z\2\2\u01edS\3\2")
        buf.write("\2\2\u01ee\u01ef\7Y\2\2\u01efU\3\2\2\2\u01f0\u01f1\t\t")
        buf.write("\2\2\u01f1W\3\2\2\2\u01f2\u01f3\7Z\2\2\u01f3\u01f4\7V")
        buf.write("\2\2\u01f4\u01f5\t\n\2\2\u01f5Y\3\2\2\2\u01f6\u01f7\t")
        buf.write("\13\2\2\u01f7[\3\2\2\2\u01f8\u01f9\t\f\2\2\u01f9]\3\2")
        buf.write("\2\2\u01fa\u0210\5`\61\2\u01fb\u0210\5d\63\2\u01fc\u0210")
        buf.write("\5b\62\2\u01fd\u0210\5f\64\2\u01fe\u0210\5h\65\2\u01ff")
        buf.write("\u0210\5j\66\2\u0200\u0210\5l\67\2\u0201\u0210\5n8\2\u0202")
        buf.write("\u0210\5p9\2\u0203\u0210\5~@\2\u0204\u0210\5\u008aF\2")
        buf.write("\u0205\u0210\5\u0094K\2\u0206\u0210\5\u009aN\2\u0207\u0210")
        buf.write("\5\u00aeX\2\u0208\u0210\5r:\2\u0209\u0210\5\u009eP\2\u020a")
        buf.write("\u0210\5t;\2\u020b\u0210\5v<\2\u020c\u0210\5x=\2\u020d")
        buf.write("\u0210\5z>\2\u020e\u0210\5|?\2\u020f\u01fa\3\2\2\2\u020f")
        buf.write("\u01fb\3\2\2\2\u020f\u01fc\3\2\2\2\u020f\u01fd\3\2\2\2")
        buf.write("\u020f\u01fe\3\2\2\2\u020f\u01ff\3\2\2\2\u020f\u0200\3")
        buf.write("\2\2\2\u020f\u0201\3\2\2\2\u020f\u0202\3\2\2\2\u020f\u0203")
        buf.write("\3\2\2\2\u020f\u0204\3\2\2\2\u020f\u0205\3\2\2\2\u020f")
        buf.write("\u0206\3\2\2\2\u020f\u0207\3\2\2\2\u020f\u0208\3\2\2\2")
        buf.write("\u020f\u0209\3\2\2\2\u020f\u020a\3\2\2\2\u020f\u020b\3")
        buf.write("\2\2\2\u020f\u020c\3\2\2\2\u020f\u020d\3\2\2\2\u020f\u020e")
        buf.write("\3\2\2\2\u0210_\3\2\2\2\u0211\u0212\7\6\2\2\u0212a\3\2")
        buf.write("\2\2\u0213\u0214\7\7\2\2\u0214c\3\2\2\2\u0215\u0216\7")
        buf.write("\b\2\2\u0216e\3\2\2\2\u0217\u0218\7\t\2\2\u0218g\3\2\2")
        buf.write("\2\u0219\u021a\7\n\2\2\u021ai\3\2\2\2\u021b\u021c\7\13")
        buf.write("\2\2\u021ck\3\2\2\2\u021d\u021e\7\f\2\2\u021em\3\2\2\2")
        buf.write("\u021f\u0220\7\r\2\2\u0220o\3\2\2\2\u0221\u0222\7\16\2")
        buf.write("\2\u0222q\3\2\2\2\u0223\u0224\7\17\2\2\u0224s\3\2\2\2")
        buf.write("\u0225\u0226\7\21\2\2\u0226u\3\2\2\2\u0227\u0228\7\22")
        buf.write("\2\2\u0228w\3\2\2\2\u0229\u022a\7\23\2\2\u022ay\3\2\2")
        buf.write("\2\u022b\u022c\7\24\2\2\u022c{\3\2\2\2\u022d\u022e\7\25")
        buf.write("\2\2\u022e}\3\2\2\2\u022f\u0238\7\27\2\2\u0230\u0231\7")
        buf.write("\'\2\2\u0231\u0234\5\u0080A\2\u0232\u0233\7,\2\2\u0233")
        buf.write("\u0235\5\u0082B\2\u0234\u0232\3\2\2\2\u0234\u0235\3\2")
        buf.write("\2\2\u0235\u0236\3\2\2\2\u0236\u0237\7(\2\2\u0237\u0239")
        buf.write("\3\2\2\2\u0238\u0230\3\2\2\2\u0238\u0239\3\2\2\2\u0239")
        buf.write("\177\3\2\2\2\u023a\u023b\t\r\2\2\u023b\u0081\3\2\2\2\u023c")
        buf.write("\u023d\7\36\2\2\u023d\u023e\7=\2\2\u023e\u0243\5\u0084")
        buf.write("C\2\u023f\u0240\7,\2\2\u0240\u0242\5\u0084C\2\u0241\u023f")
        buf.write("\3\2\2\2\u0242\u0245\3\2\2\2\u0243\u0241\3\2\2\2\u0243")
        buf.write("\u0244\3\2\2\2\u0244\u0083\3\2\2\2\u0245\u0243\3\2\2\2")
        buf.write("\u0246\u0248\5\u0088E\2\u0247\u0246\3\2\2\2\u0247\u0248")
        buf.write("\3\2\2\2\u0248\u0249\3\2\2\2\u0249\u024a\5\u0086D\2\u024a")
        buf.write("\u0085\3\2\2\2\u024b\u024c\t\5\2\2\u024c\u0087\3\2\2\2")
        buf.write("\u024d\u024e\7!\2\2\u024e\u024f\7&\2\2\u024f\u0089\3\2")
        buf.write("\2\2\u0250\u0255\7\30\2\2\u0251\u0252\7\'\2\2\u0252\u0253")
        buf.write("\5\u008cG\2\u0253\u0254\7(\2\2\u0254\u0256\3\2\2\2\u0255")
        buf.write("\u0251\3\2\2\2\u0255\u0256\3\2\2\2\u0256\u008b\3\2\2\2")
        buf.write("\u0257\u0258\7\36\2\2\u0258\u0259\7=\2\2\u0259\u025e\5")
        buf.write("\u008eH\2\u025a\u025b\7,\2\2\u025b\u025d\5\u008eH\2\u025c")
        buf.write("\u025a\3\2\2\2\u025d\u0260\3\2\2\2\u025e\u025c\3\2\2\2")
        buf.write("\u025e\u025f\3\2\2\2\u025f\u008d\3\2\2\2\u0260\u025e\3")
        buf.write("\2\2\2\u0261\u0263\5\u0092J\2\u0262\u0261\3\2\2\2\u0262")
        buf.write("\u0263\3\2\2\2\u0263\u0264\3\2\2\2\u0264\u0265\5\u0090")
        buf.write("I\2\u0265\u008f\3\2\2\2\u0266\u0267\t\5\2\2\u0267\u0091")
        buf.write("\3\2\2\2\u0268\u0269\7\"\2\2\u0269\u026a\7&\2\2\u026a")
        buf.write("\u0093\3\2\2\2\u026b\u026c\7\31\2\2\u026c\u026d\7\'\2")
        buf.write("\2\u026d\u026e\5\u0096L\2\u026e\u026f\7(\2\2\u026f\u0095")
        buf.write("\3\2\2\2\u0270\u0275\5\u0098M\2\u0271\u0272\7,\2\2\u0272")
        buf.write("\u0274\5\u0098M\2\u0273\u0271\3\2\2\2\u0274\u0277\3\2")
        buf.write("\2\2\u0275\u0273\3\2\2\2\u0275\u0276\3\2\2\2\u0276\u0097")
        buf.write("\3\2\2\2\u0277\u0275\3\2\2\2\u0278\u0279\7!\2\2\u0279")
        buf.write("\u0099\3\2\2\2\u027a\u027f\7\32\2\2\u027b\u027c\7\'\2")
        buf.write("\2\u027c\u027d\5\u009cO\2\u027d\u027e\7(\2\2\u027e\u0280")
        buf.write("\3\2\2\2\u027f\u027b\3\2\2\2\u027f\u0280\3\2\2\2\u0280")
        buf.write("\u009b\3\2\2\2\u0281\u0282\7\3\2\2\u0282\u009d\3\2\2\2")
        buf.write("\u0283\u0288\5\u00a0Q\2\u0284\u0285\7\'\2\2\u0285\u0286")
        buf.write("\5\u00a2R\2\u0286\u0287\7(\2\2\u0287\u0289\3\2\2\2\u0288")
        buf.write("\u0284\3\2\2\2\u0288\u0289\3\2\2\2\u0289\u009f\3\2\2\2")
        buf.write("\u028a\u028b\t\16\2\2\u028b\u00a1\3\2\2\2\u028c\u0291")
        buf.write("\5\u00a4S\2\u028d\u028e\7,\2\2\u028e\u0290\5\u00a4S\2")
        buf.write("\u028f\u028d\3\2\2\2\u0290\u0293\3\2\2\2\u0291\u028f\3")
        buf.write("\2\2\2\u0291\u0292\3\2\2\2\u0292\u00a3\3\2\2\2\u0293\u0291")
        buf.write("\3\2\2\2\u0294\u0295\5\u00a8U\2\u0295\u0296\5\u00a6T\2")
        buf.write("\u0296\u0297\5\u00aaV\2\u0297\u00a5\3\2\2\2\u0298\u0299")
        buf.write("\7$\2\2\u0299\u00a7\3\2\2\2\u029a\u029b\7!\2\2\u029b\u029c")
        buf.write("\7=\2\2\u029c\u00a9\3\2\2\2\u029d\u029f\5\u00acW\2\u029e")
        buf.write("\u029d\3\2\2\2\u029f\u02a2\3\2\2\2\u02a0\u029e\3\2\2\2")
        buf.write("\u02a0\u02a1\3\2\2\2\u02a1\u00ab\3\2\2\2\u02a2\u02a0\3")
        buf.write("\2\2\2\u02a3\u02a4\7%\2\2\u02a4\u00ad\3\2\2\2\u02a5\u02a6")
        buf.write("\5\u00b0Y\2\u02a6\u02a9\7\'\2\2\u02a7\u02aa\5\u00b2Z\2")
        buf.write("\u02a8\u02aa\5\u00b4[\2\u02a9\u02a7\3\2\2\2\u02a9\u02a8")
        buf.write("\3\2\2\2\u02aa\u02ac\3\2\2\2\u02ab\u02ad\5\u00b6\\\2\u02ac")
        buf.write("\u02ab\3\2\2\2\u02ac\u02ad\3\2\2\2\u02ad\u02ae\3\2\2\2")
        buf.write("\u02ae\u02af\7(\2\2\u02af\u00af\3\2\2\2\u02b0\u02b1\t")
        buf.write("\17\2\2\u02b1\u00b1\3\2\2\2\u02b2\u02b3\7\63\2\2\u02b3")
        buf.write("\u02b4\7!\2\2\u02b4\u00b3\3\2\2\2\u02b5\u02b6\7#\2\2\u02b6")
        buf.write("\u00b5\3\2\2\2\u02b7\u02b8\7\61\2\2\u02b8\u02b9\7!\2\2")
        buf.write("\u02b9\u00b7\3\2\2\2B\u00b9\u00be\u00c4\u00ca\u00ce\u00d3")
        buf.write("\u00d9\u00ea\u00f1\u00f5\u00f9\u00fd\u00ff\u0106\u010c")
        buf.write("\u0110\u0115\u0119\u011e\u0139\u013c\u0144\u0149\u014f")
        buf.write("\u0157\u015a\u015e\u0162\u016b\u0177\u017e\u0181\u0184")
        buf.write("\u0189\u018c\u0198\u019c\u01aa\u01ad\u01b2\u01bb\u01bf")
        buf.write("\u01c2\u01c6\u01ce\u01dd\u01e2\u01e6\u01ea\u020f\u0234")
        buf.write("\u0238\u0243\u0247\u0255\u025e\u0262\u0275\u027f\u0288")
        buf.write("\u0291\u02a0\u02a9\u02ac")
        return buf.getvalue()


class ZmeiLangParser ( Parser ):

    grammarFileName = "ZmeiLangParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'import'", "'as'", "'text'", 
                     "'html'", "'html_media'", "'float'", "'decimal'", "'date'", 
                     "'datetime'", "'create_time'", "'update_time'", "'image_file'", 
                     "'image'", "'filer_image'", "'filer_file'", "'file'", 
                     "'simple_file'", "'folder'", "'image_folder'", "'str'", 
                     "'int'", "'slug'", "'bool'", "'one'", "'one2one'", 
                     "'many'", "'choices'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "':'", "'('", "')'", "'['", "']'", "'?'", "','", "'.'", 
                     "<INVALID>", "<INVALID>", "'=>'", "'->'", "'~>'", "'#'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'$'", "'&'", "'!'", "'*'", 
                     "'~'", "' '", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'}'", "<INVALID>", "<INVALID>", "';'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'<'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'?>'", "'/>'" ]

    symbolicNames = [ "<INVALID>", "BOOL", "KW_IMPORT", "KW_AS", "COL_FIELD_TYPE_LONGTEXT", 
                      "COL_FIELD_TYPE_HTML", "COL_FIELD_TYPE_HTML_MEDIA", 
                      "COL_FIELD_TYPE_FLOAT", "COL_FIELD_TYPE_DECIMAL", 
                      "COL_FIELD_TYPE_DATE", "COL_FIELD_TYPE_DATETIME", 
                      "COL_FIELD_TYPE_CREATE_TIME", "COL_FIELD_TYPE_UPDATE_TIME", 
                      "COL_FIELD_TYPE_IMAGE_FILE", "COL_FIELD_TYPE_IMAGE", 
                      "COL_FIELD_TYPE_FILER_IMAGE", "COL_FIELD_TYPE_FILER_FILE", 
                      "COL_FIELD_TYPE_FILE", "COL_FIELD_TYPE_SIMPLE_FILE", 
                      "COL_FIELD_TYPE_FOLDER", "COL_FIELD_TYPE_IMAGE_FOLDER", 
                      "COL_FIELD_TYPE_TEXT", "COL_FIELD_TYPE_INT", "COL_FIELD_TYPE_SLUG", 
                      "COL_FIELD_TYPE_BOOL", "COL_FIELD_TYPE_ONE", "COL_FIELD_TYPE_ONE2ONE", 
                      "COL_FIELD_TYPE_MANY", "COL_FIELD_CHOICES", "NL", 
                      "INLINE_CODE_BLOCK", "ID", "DIGIT", "CLASSNAME", "SIZE2D", 
                      "FILTER", "COLON", "BRACE_OPEN", "BRACE_CLOSE", "SQ_BRACE_OPEN", 
                      "SQ_BRACE_CLOSE", "QUESTION_MARK", "COMA", "DOT", 
                      "STRING_DQ", "STRING_SQ", "FIELD_VNAME", "RELATED", 
                      "RELATED_EXTEND", "REF_SIGN", "ANNOTATION", "LINE_SEPARATOR", 
                      "URL_SEGMENTS", "TEMPLATE_NAME", "ASSIGN", "ASSIGN_STATIC", 
                      "COMMENT_LINE", "COMMENT_BLOCK", "SLASH", "EQUALS", 
                      "DOLLAR", "AMP", "EXCLAM", "STAR", "APPROX", "WS", 
                      "COL_FIELD_CALCULATED", "CODE_BLOCK_START", "XML_OPEN", 
                      "CODE_BLOCK_LINE", "CODE_BLOCK_END", "PYTHON_LINE_CODE", 
                      "PYTHON_LINE_ERRCHAR", "PYTHON_LINE_END", "PYTHON_EXPR_ERRCHAR", 
                      "XML_EntityRef", "XML_CharRef", "XML_TAG_OPEN", "XML_TEXT", 
                      "XML_ERRCHAR", "XML_CLOSE", "XML_SPECIAL_CLOSE", "XML_SLASH_CLOSE", 
                      "XML_SLASH", "XML_EQUALS", "XML_REACT_ATTR", "XML_STRING", 
                      "XML_CmpName", "XML_Name", "XML_INSIDE_ERRCHAR" ]

    RULE_col_file = 0
    RULE_page_imports = 1
    RULE_model_imports = 2
    RULE_import_source = 3
    RULE_code_block = 4
    RULE_page = 5
    RULE_page_base = 6
    RULE_page_alias = 7
    RULE_page_alias_name = 8
    RULE_page_element = 9
    RULE_page_template = 10
    RULE_page_url = 11
    RULE_page_code = 12
    RULE_page_name = 13
    RULE_page_field = 14
    RULE_page_field_name = 15
    RULE_page_field_code = 16
    RULE_col = 17
    RULE_col_str_expr = 18
    RULE_col_header = 19
    RULE_col_verbose_name = 20
    RULE_verbose_name_part = 21
    RULE_col_base_name = 22
    RULE_col_name = 23
    RULE_col_field = 24
    RULE_col_field_expr = 25
    RULE_col_field_expr_marker = 26
    RULE_col_feild_expr_code = 27
    RULE_string_or_quoted = 28
    RULE_col_field_help_text = 29
    RULE_col_field_vrebose_name = 30
    RULE_col_field_name = 31
    RULE_col_modifier = 32
    RULE_annotation = 33
    RULE_annotation_descr = 34
    RULE_annotation_code = 35
    RULE_xml_content = 36
    RULE_xml_element = 37
    RULE_xml_name = 38
    RULE_xml_name_end = 39
    RULE_xml_tag_name = 40
    RULE_xml_component_name = 41
    RULE_xml_reference = 42
    RULE_xml_attribute = 43
    RULE_xml_chardata = 44
    RULE_xml_misc = 45
    RULE_col_field_def = 46
    RULE_field_longtext = 47
    RULE_field_html = 48
    RULE_field_html_media = 49
    RULE_field_float = 50
    RULE_field_decimal = 51
    RULE_field_date = 52
    RULE_field_datetime = 53
    RULE_field_create_time = 54
    RULE_field_update_time = 55
    RULE_field_image_file = 56
    RULE_field_filer_image = 57
    RULE_field_filer_file = 58
    RULE_field_file = 59
    RULE_field_simple_file = 60
    RULE_field_folder = 61
    RULE_field_text = 62
    RULE_field_text_size = 63
    RULE_field_text_choices = 64
    RULE_field_text_choice = 65
    RULE_field_text_choice_val = 66
    RULE_field_text_choice_key = 67
    RULE_field_int = 68
    RULE_field_int_choices = 69
    RULE_field_int_choice = 70
    RULE_field_int_choice_val = 71
    RULE_field_int_choice_key = 72
    RULE_field_slug = 73
    RULE_field_slug_ref_field = 74
    RULE_field_slug_ref_field_id = 75
    RULE_field_bool = 76
    RULE_field_bool_default = 77
    RULE_field_image = 78
    RULE_filer_image_type = 79
    RULE_field_image_sizes = 80
    RULE_field_image_size = 81
    RULE_field_image_size_dimensions = 82
    RULE_field_image_size_name = 83
    RULE_field_image_filters = 84
    RULE_field_image_filter = 85
    RULE_field_relation = 86
    RULE_field_relation_type = 87
    RULE_field_relation_target_ref = 88
    RULE_field_relation_target_class = 89
    RULE_field_relation_related_name = 90

    ruleNames =  [ "col_file", "page_imports", "model_imports", "import_source", 
                   "code_block", "page", "page_base", "page_alias", "page_alias_name", 
                   "page_element", "page_template", "page_url", "page_code", 
                   "page_name", "page_field", "page_field_name", "page_field_code", 
                   "col", "col_str_expr", "col_header", "col_verbose_name", 
                   "verbose_name_part", "col_base_name", "col_name", "col_field", 
                   "col_field_expr", "col_field_expr_marker", "col_feild_expr_code", 
                   "string_or_quoted", "col_field_help_text", "col_field_vrebose_name", 
                   "col_field_name", "col_modifier", "annotation", "annotation_descr", 
                   "annotation_code", "xml_content", "xml_element", "xml_name", 
                   "xml_name_end", "xml_tag_name", "xml_component_name", 
                   "xml_reference", "xml_attribute", "xml_chardata", "xml_misc", 
                   "col_field_def", "field_longtext", "field_html", "field_html_media", 
                   "field_float", "field_decimal", "field_date", "field_datetime", 
                   "field_create_time", "field_update_time", "field_image_file", 
                   "field_filer_image", "field_filer_file", "field_file", 
                   "field_simple_file", "field_folder", "field_text", "field_text_size", 
                   "field_text_choices", "field_text_choice", "field_text_choice_val", 
                   "field_text_choice_key", "field_int", "field_int_choices", 
                   "field_int_choice", "field_int_choice_val", "field_int_choice_key", 
                   "field_slug", "field_slug_ref_field", "field_slug_ref_field_id", 
                   "field_bool", "field_bool_default", "field_image", "filer_image_type", 
                   "field_image_sizes", "field_image_size", "field_image_size_dimensions", 
                   "field_image_size_name", "field_image_filters", "field_image_filter", 
                   "field_relation", "field_relation_type", "field_relation_target_ref", 
                   "field_relation_target_class", "field_relation_related_name" ]

    EOF = Token.EOF
    BOOL=1
    KW_IMPORT=2
    KW_AS=3
    COL_FIELD_TYPE_LONGTEXT=4
    COL_FIELD_TYPE_HTML=5
    COL_FIELD_TYPE_HTML_MEDIA=6
    COL_FIELD_TYPE_FLOAT=7
    COL_FIELD_TYPE_DECIMAL=8
    COL_FIELD_TYPE_DATE=9
    COL_FIELD_TYPE_DATETIME=10
    COL_FIELD_TYPE_CREATE_TIME=11
    COL_FIELD_TYPE_UPDATE_TIME=12
    COL_FIELD_TYPE_IMAGE_FILE=13
    COL_FIELD_TYPE_IMAGE=14
    COL_FIELD_TYPE_FILER_IMAGE=15
    COL_FIELD_TYPE_FILER_FILE=16
    COL_FIELD_TYPE_FILE=17
    COL_FIELD_TYPE_SIMPLE_FILE=18
    COL_FIELD_TYPE_FOLDER=19
    COL_FIELD_TYPE_IMAGE_FOLDER=20
    COL_FIELD_TYPE_TEXT=21
    COL_FIELD_TYPE_INT=22
    COL_FIELD_TYPE_SLUG=23
    COL_FIELD_TYPE_BOOL=24
    COL_FIELD_TYPE_ONE=25
    COL_FIELD_TYPE_ONE2ONE=26
    COL_FIELD_TYPE_MANY=27
    COL_FIELD_CHOICES=28
    NL=29
    INLINE_CODE_BLOCK=30
    ID=31
    DIGIT=32
    CLASSNAME=33
    SIZE2D=34
    FILTER=35
    COLON=36
    BRACE_OPEN=37
    BRACE_CLOSE=38
    SQ_BRACE_OPEN=39
    SQ_BRACE_CLOSE=40
    QUESTION_MARK=41
    COMA=42
    DOT=43
    STRING_DQ=44
    STRING_SQ=45
    FIELD_VNAME=46
    RELATED=47
    RELATED_EXTEND=48
    REF_SIGN=49
    ANNOTATION=50
    LINE_SEPARATOR=51
    URL_SEGMENTS=52
    TEMPLATE_NAME=53
    ASSIGN=54
    ASSIGN_STATIC=55
    COMMENT_LINE=56
    COMMENT_BLOCK=57
    SLASH=58
    EQUALS=59
    DOLLAR=60
    AMP=61
    EXCLAM=62
    STAR=63
    APPROX=64
    WS=65
    COL_FIELD_CALCULATED=66
    CODE_BLOCK_START=67
    XML_OPEN=68
    CODE_BLOCK_LINE=69
    CODE_BLOCK_END=70
    PYTHON_LINE_CODE=71
    PYTHON_LINE_ERRCHAR=72
    PYTHON_LINE_END=73
    PYTHON_EXPR_ERRCHAR=74
    XML_EntityRef=75
    XML_CharRef=76
    XML_TAG_OPEN=77
    XML_TEXT=78
    XML_ERRCHAR=79
    XML_CLOSE=80
    XML_SPECIAL_CLOSE=81
    XML_SLASH_CLOSE=82
    XML_SLASH=83
    XML_EQUALS=84
    XML_REACT_ATTR=85
    XML_STRING=86
    XML_CmpName=87
    XML_Name=88
    XML_INSIDE_ERRCHAR=89

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Col_fileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ZmeiLangParser.EOF, 0)

        def page_imports(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_importsContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.AnnotationContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.AnnotationContext,i)


        def page(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.PageContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.PageContext,i)


        def model_imports(self):
            return self.getTypedRuleContext(ZmeiLangParser.Model_importsContext,0)


        def col(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.ColContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.ColContext,i)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_file" ):
                listener.enterCol_file(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_file" ):
                listener.exitCol_file(self)




    def col_file(self):

        localctx = ZmeiLangParser.Col_fileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_col_file)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 182
                self.page_imports()


            self.state = 188
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 185
                    self.match(ZmeiLangParser.NL) 
                self.state = 190
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.ANNOTATION:
                self.state = 191
                self.annotation()
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.SQ_BRACE_OPEN:
                self.state = 197
                self.page()
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.KW_IMPORT:
                self.state = 203
                self.model_imports()


            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.REF_SIGN:
                self.state = 206
                self.col()
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 212
                self.match(ZmeiLangParser.NL)
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 218
            self.match(ZmeiLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Page_importsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_IMPORT(self):
            return self.getToken(ZmeiLangParser.KW_IMPORT, 0)

        def import_source(self):
            return self.getTypedRuleContext(ZmeiLangParser.Import_sourceContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_imports

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_imports" ):
                listener.enterPage_imports(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_imports" ):
                listener.exitPage_imports(self)




    def page_imports(self):

        localctx = ZmeiLangParser.Page_importsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_page_imports)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(ZmeiLangParser.KW_IMPORT)
            self.state = 221
            self.import_source()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Model_importsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_IMPORT(self):
            return self.getToken(ZmeiLangParser.KW_IMPORT, 0)

        def import_source(self):
            return self.getTypedRuleContext(ZmeiLangParser.Import_sourceContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_model_imports

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModel_imports" ):
                listener.enterModel_imports(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModel_imports" ):
                listener.exitModel_imports(self)




    def model_imports(self):

        localctx = ZmeiLangParser.Model_importsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_model_imports)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(ZmeiLangParser.KW_IMPORT)
            self.state = 224
            self.import_source()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Import_sourceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_import_source

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_source" ):
                listener.enterImport_source(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_source" ):
                listener.exitImport_source(self)




    def import_source(self):

        localctx = ZmeiLangParser.Import_sourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_import_source)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Code_blockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CODE_BLOCK_START(self):
            return self.getToken(ZmeiLangParser.CODE_BLOCK_START, 0)

        def CODE_BLOCK_END(self):
            return self.getToken(ZmeiLangParser.CODE_BLOCK_END, 0)

        def CODE_BLOCK_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.CODE_BLOCK_LINE)
            else:
                return self.getToken(ZmeiLangParser.CODE_BLOCK_LINE, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_code_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCode_block" ):
                listener.enterCode_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCode_block" ):
                listener.exitCode_block(self)




    def code_block(self):

        localctx = ZmeiLangParser.Code_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_code_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(ZmeiLangParser.CODE_BLOCK_START)
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.CODE_BLOCK_LINE:
                self.state = 229
                self.match(ZmeiLangParser.CODE_BLOCK_LINE)
                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 235
            self.match(ZmeiLangParser.CODE_BLOCK_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PageContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQ_BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.SQ_BRACE_OPEN, 0)

        def page_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_nameContext,0)


        def SQ_BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.SQ_BRACE_CLOSE, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def page_base(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_baseContext,0)


        def page_alias(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_aliasContext,0)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COLON)
            else:
                return self.getToken(ZmeiLangParser.COLON, i)

        def page_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Page_fieldContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Page_fieldContext,i)


        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.AnnotationContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.AnnotationContext,i)


        def page_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_codeContext,0)


        def page_element(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_elementContext,0)


        def page_url(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_urlContext,0)


        def page_template(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_templateContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage" ):
                listener.enterPage(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage" ):
                listener.exitPage(self)




    def page(self):

        localctx = ZmeiLangParser.PageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_page)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(ZmeiLangParser.SQ_BRACE_OPEN)
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 238
                self.page_base()


            self.state = 241
            self.page_name()
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.KW_AS:
                self.state = 242
                self.page_alias()


            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COLON:
                self.state = 245
                self.match(ZmeiLangParser.COLON)
                self.state = 247
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.ID or _la==ZmeiLangParser.URL_SEGMENTS:
                    self.state = 246
                    self.page_url()


                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.COLON:
                    self.state = 249
                    self.match(ZmeiLangParser.COLON)
                    self.state = 250
                    self.page_template()




            self.state = 255
            self.match(ZmeiLangParser.SQ_BRACE_CLOSE)
            self.state = 256
            self.match(ZmeiLangParser.NL)
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.ID:
                self.state = 257
                self.page_field()
                self.state = 262
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 266
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 263
                    self.annotation() 
                self.state = 268
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK_START:
                self.state = 269
                self.page_code()


            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.ANNOTATION:
                self.state = 272
                self.annotation()
                self.state = 277
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.XML_OPEN:
                self.state = 278
                self.page_element()


            self.state = 284
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 281
                    self.match(ZmeiLangParser.NL) 
                self.state = 286
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Page_baseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZmeiLangParser.ID, 0)

        def RELATED(self):
            return self.getToken(ZmeiLangParser.RELATED, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_base

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_base" ):
                listener.enterPage_base(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_base" ):
                listener.exitPage_base(self)




    def page_base(self):

        localctx = ZmeiLangParser.Page_baseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_page_base)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(ZmeiLangParser.ID)
            self.state = 288
            self.match(ZmeiLangParser.RELATED)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Page_aliasContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_AS(self):
            return self.getToken(ZmeiLangParser.KW_AS, 0)

        def page_alias_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_alias_nameContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_alias

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_alias" ):
                listener.enterPage_alias(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_alias" ):
                listener.exitPage_alias(self)




    def page_alias(self):

        localctx = ZmeiLangParser.Page_aliasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_page_alias)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(ZmeiLangParser.KW_AS)
            self.state = 291
            self.page_alias_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Page_alias_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZmeiLangParser.ID, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_alias_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_alias_name" ):
                listener.enterPage_alias_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_alias_name" ):
                listener.exitPage_alias_name(self)




    def page_alias_name(self):

        localctx = ZmeiLangParser.Page_alias_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_page_alias_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(ZmeiLangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Page_elementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def xml_element(self):
            return self.getTypedRuleContext(ZmeiLangParser.Xml_elementContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_element" ):
                listener.enterPage_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_element" ):
                listener.exitPage_element(self)




    def page_element(self):

        localctx = ZmeiLangParser.Page_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_page_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.xml_element()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Page_templateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASSNAME(self):
            return self.getToken(ZmeiLangParser.CLASSNAME, 0)

        def TEMPLATE_NAME(self):
            return self.getToken(ZmeiLangParser.TEMPLATE_NAME, 0)

        def INLINE_CODE_BLOCK(self):
            return self.getToken(ZmeiLangParser.INLINE_CODE_BLOCK, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_template

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_template" ):
                listener.enterPage_template(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_template" ):
                listener.exitPage_template(self)




    def page_template(self):

        localctx = ZmeiLangParser.Page_templateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_page_template)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.INLINE_CODE_BLOCK) | (1 << ZmeiLangParser.CLASSNAME) | (1 << ZmeiLangParser.TEMPLATE_NAME))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Page_urlContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZmeiLangParser.ID, 0)

        def URL_SEGMENTS(self):
            return self.getToken(ZmeiLangParser.URL_SEGMENTS, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_url

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_url" ):
                listener.enterPage_url(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_url" ):
                listener.exitPage_url(self)




    def page_url(self):

        localctx = ZmeiLangParser.Page_urlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_page_url)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.ID or _la==ZmeiLangParser.URL_SEGMENTS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Page_codeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_code

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_code" ):
                listener.enterPage_code(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_code" ):
                listener.exitPage_code(self)




    def page_code(self):

        localctx = ZmeiLangParser.Page_codeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_page_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Page_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZmeiLangParser.ID, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_name" ):
                listener.enterPage_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_name" ):
                listener.exitPage_name(self)




    def page_name(self):

        localctx = ZmeiLangParser.Page_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_page_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(ZmeiLangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Page_fieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def page_field_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_field_nameContext,0)


        def ASSIGN(self):
            return self.getToken(ZmeiLangParser.ASSIGN, 0)

        def page_field_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_field_codeContext,0)


        def EOF(self):
            return self.getToken(ZmeiLangParser.EOF, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_field" ):
                listener.enterPage_field(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_field" ):
                listener.exitPage_field(self)




    def page_field(self):

        localctx = ZmeiLangParser.Page_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_page_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.page_field_name()
            self.state = 306
            self.match(ZmeiLangParser.ASSIGN)
            self.state = 307
            self.page_field_code()
            self.state = 314
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.NL]:
                self.state = 309 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 308
                        self.match(ZmeiLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 311 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

                pass
            elif token in [ZmeiLangParser.EOF]:
                self.state = 313
                self.match(ZmeiLangParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Page_field_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZmeiLangParser.ID, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_field_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_field_name" ):
                listener.enterPage_field_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_field_name" ):
                listener.exitPage_field_name(self)




    def page_field_name(self):

        localctx = ZmeiLangParser.Page_field_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_page_field_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(ZmeiLangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Page_field_codeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PYTHON_LINE_CODE(self):
            return self.getToken(ZmeiLangParser.PYTHON_LINE_CODE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_field_code

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_field_code" ):
                listener.enterPage_field_code(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_field_code" ):
                listener.exitPage_field_code(self)




    def page_field_code(self):

        localctx = ZmeiLangParser.Page_field_codeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_page_field_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(ZmeiLangParser.PYTHON_LINE_CODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ColContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def col_header(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_headerContext,0)


        def col_str_expr(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_str_exprContext,0)


        def col_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Col_fieldContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Col_fieldContext,i)


        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.AnnotationContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.AnnotationContext,i)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol" ):
                listener.enterCol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol" ):
                listener.exitCol(self)




    def col(self):

        localctx = ZmeiLangParser.ColContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_col)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.col_header()
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 321
                self.col_str_expr()


            self.state = 327
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 31)) & ~0x3f) == 0 and ((1 << (_la - 31)) & ((1 << (ZmeiLangParser.ID - 31)) | (1 << (ZmeiLangParser.EQUALS - 31)) | (1 << (ZmeiLangParser.DOLLAR - 31)) | (1 << (ZmeiLangParser.AMP - 31)) | (1 << (ZmeiLangParser.EXCLAM - 31)) | (1 << (ZmeiLangParser.STAR - 31)) | (1 << (ZmeiLangParser.APPROX - 31)))) != 0):
                self.state = 324
                self.col_field()
                self.state = 329
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.ANNOTATION:
                self.state = 330
                self.annotation()
                self.state = 335
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Col_str_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(ZmeiLangParser.EQUALS, 0)

        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def EOF(self):
            return self.getToken(ZmeiLangParser.EOF, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_str_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_str_expr" ):
                listener.enterCol_str_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_str_expr" ):
                listener.exitCol_str_expr(self)




    def col_str_expr(self):

        localctx = ZmeiLangParser.Col_str_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_col_str_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(ZmeiLangParser.EQUALS)
            self.state = 337
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.STRING_DQ or _la==ZmeiLangParser.STRING_SQ):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 344
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.NL]:
                self.state = 339 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 338
                        self.match(ZmeiLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 341 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

                pass
            elif token in [ZmeiLangParser.EOF]:
                self.state = 343
                self.match(ZmeiLangParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Col_headerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REF_SIGN(self):
            return self.getToken(ZmeiLangParser.REF_SIGN, 0)

        def col_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_nameContext,0)


        def LINE_SEPARATOR(self):
            return self.getToken(ZmeiLangParser.LINE_SEPARATOR, 0)

        def NL(self):
            return self.getToken(ZmeiLangParser.NL, 0)

        def col_base_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_base_nameContext,0)


        def col_verbose_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_verbose_nameContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_header" ):
                listener.enterCol_header(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_header" ):
                listener.exitCol_header(self)




    def col_header(self):

        localctx = ZmeiLangParser.Col_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_col_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(ZmeiLangParser.REF_SIGN)
            self.state = 348
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 347
                self.col_base_name()


            self.state = 350
            self.col_name()
            self.state = 352
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COLON:
                self.state = 351
                self.col_verbose_name()


            self.state = 354
            self.match(ZmeiLangParser.LINE_SEPARATOR)
            self.state = 355
            self.match(ZmeiLangParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Col_verbose_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def verbose_name_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Verbose_name_partContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Verbose_name_partContext,i)


        def SLASH(self):
            return self.getToken(ZmeiLangParser.SLASH, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_verbose_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_verbose_name" ):
                listener.enterCol_verbose_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_verbose_name" ):
                listener.exitCol_verbose_name(self)




    def col_verbose_name(self):

        localctx = ZmeiLangParser.Col_verbose_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_col_verbose_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(ZmeiLangParser.COLON)
            self.state = 358
            self.verbose_name_part()
            self.state = 361
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.SLASH:
                self.state = 359
                self.match(ZmeiLangParser.SLASH)
                self.state = 360
                self.verbose_name_part()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Verbose_name_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZmeiLangParser.ID, 0)

        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_verbose_name_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVerbose_name_part" ):
                listener.enterVerbose_name_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVerbose_name_part" ):
                listener.exitVerbose_name_part(self)




    def verbose_name_part(self):

        localctx = ZmeiLangParser.Verbose_name_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_verbose_name_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.ID) | (1 << ZmeiLangParser.STRING_DQ) | (1 << ZmeiLangParser.STRING_SQ))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Col_base_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZmeiLangParser.ID, 0)

        def RELATED(self):
            return self.getToken(ZmeiLangParser.RELATED, 0)

        def RELATED_EXTEND(self):
            return self.getToken(ZmeiLangParser.RELATED_EXTEND, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_base_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_base_name" ):
                listener.enterCol_base_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_base_name" ):
                listener.exitCol_base_name(self)




    def col_base_name(self):

        localctx = ZmeiLangParser.Col_base_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_col_base_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(ZmeiLangParser.ID)
            self.state = 366
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.RELATED or _la==ZmeiLangParser.RELATED_EXTEND):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Col_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZmeiLangParser.ID, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_name" ):
                listener.enterCol_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_name" ):
                listener.exitCol_name(self)




    def col_name(self):

        localctx = ZmeiLangParser.Col_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_col_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.match(ZmeiLangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Col_fieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def col_field_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_field_nameContext,0)


        def EOF(self):
            return self.getToken(ZmeiLangParser.EOF, 0)

        def col_modifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Col_modifierContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Col_modifierContext,i)


        def col_field_expr(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_field_exprContext,0)


        def col_field_vrebose_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_field_vrebose_nameContext,0)


        def col_field_help_text(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_field_help_textContext,0)


        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def col_field_def(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_field_defContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_field" ):
                listener.enterCol_field(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_field" ):
                listener.exitCol_field(self)




    def col_field(self):

        localctx = ZmeiLangParser.Col_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_col_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 59)) & ~0x3f) == 0 and ((1 << (_la - 59)) & ((1 << (ZmeiLangParser.EQUALS - 59)) | (1 << (ZmeiLangParser.DOLLAR - 59)) | (1 << (ZmeiLangParser.AMP - 59)) | (1 << (ZmeiLangParser.EXCLAM - 59)) | (1 << (ZmeiLangParser.STAR - 59)) | (1 << (ZmeiLangParser.APPROX - 59)))) != 0):
                self.state = 370
                self.col_modifier()
                self.state = 375
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 376
            self.col_field_name()
            self.state = 380
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.COLON]:
                self.state = 377
                self.match(ZmeiLangParser.COLON)
                self.state = 378
                self.col_field_def()
                pass
            elif token in [ZmeiLangParser.ASSIGN, ZmeiLangParser.ASSIGN_STATIC]:
                self.state = 379
                self.col_field_expr()
                pass
            elif token in [ZmeiLangParser.EOF, ZmeiLangParser.NL, ZmeiLangParser.QUESTION_MARK, ZmeiLangParser.SLASH]:
                pass
            else:
                pass
            self.state = 383
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.SLASH:
                self.state = 382
                self.col_field_vrebose_name()


            self.state = 386
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.QUESTION_MARK:
                self.state = 385
                self.col_field_help_text()


            self.state = 394
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.NL]:
                self.state = 389 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 388
                        self.match(ZmeiLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 391 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

                pass
            elif token in [ZmeiLangParser.EOF]:
                self.state = 393
                self.match(ZmeiLangParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Col_field_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def col_field_expr_marker(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_field_expr_markerContext,0)


        def col_feild_expr_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_feild_expr_codeContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_field_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_field_expr" ):
                listener.enterCol_field_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_field_expr" ):
                listener.exitCol_field_expr(self)




    def col_field_expr(self):

        localctx = ZmeiLangParser.Col_field_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_col_field_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.col_field_expr_marker()
            self.state = 397
            self.col_feild_expr_code()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Col_field_expr_markerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(ZmeiLangParser.ASSIGN, 0)

        def ASSIGN_STATIC(self):
            return self.getToken(ZmeiLangParser.ASSIGN_STATIC, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_field_expr_marker

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_field_expr_marker" ):
                listener.enterCol_field_expr_marker(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_field_expr_marker" ):
                listener.exitCol_field_expr_marker(self)




    def col_field_expr_marker(self):

        localctx = ZmeiLangParser.Col_field_expr_markerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_col_field_expr_marker)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.ASSIGN or _la==ZmeiLangParser.ASSIGN_STATIC):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Col_feild_expr_codeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PYTHON_LINE_CODE(self):
            return self.getToken(ZmeiLangParser.PYTHON_LINE_CODE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_feild_expr_code

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_feild_expr_code" ):
                listener.enterCol_feild_expr_code(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_feild_expr_code" ):
                listener.exitCol_feild_expr_code(self)




    def col_feild_expr_code(self):

        localctx = ZmeiLangParser.Col_feild_expr_codeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_col_feild_expr_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.match(ZmeiLangParser.PYTHON_LINE_CODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class String_or_quotedContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.ID)
            else:
                return self.getToken(ZmeiLangParser.ID, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_string_or_quoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_or_quoted" ):
                listener.enterString_or_quoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_or_quoted" ):
                listener.exitString_or_quoted(self)




    def string_or_quoted(self):

        localctx = ZmeiLangParser.String_or_quotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_string_or_quoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.ID]:
                self.state = 404 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 403
                    self.match(ZmeiLangParser.ID)
                    self.state = 406 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZmeiLangParser.ID):
                        break

                pass
            elif token in [ZmeiLangParser.STRING_DQ]:
                self.state = 408
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.state = 409
                self.match(ZmeiLangParser.STRING_SQ)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Col_field_help_textContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUESTION_MARK(self):
            return self.getToken(ZmeiLangParser.QUESTION_MARK, 0)

        def string_or_quoted(self):
            return self.getTypedRuleContext(ZmeiLangParser.String_or_quotedContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_field_help_text

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_field_help_text" ):
                listener.enterCol_field_help_text(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_field_help_text" ):
                listener.exitCol_field_help_text(self)




    def col_field_help_text(self):

        localctx = ZmeiLangParser.Col_field_help_textContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_col_field_help_text)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.match(ZmeiLangParser.QUESTION_MARK)
            self.state = 413
            self.string_or_quoted()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Col_field_vrebose_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SLASH(self):
            return self.getToken(ZmeiLangParser.SLASH, 0)

        def string_or_quoted(self):
            return self.getTypedRuleContext(ZmeiLangParser.String_or_quotedContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_field_vrebose_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_field_vrebose_name" ):
                listener.enterCol_field_vrebose_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_field_vrebose_name" ):
                listener.exitCol_field_vrebose_name(self)




    def col_field_vrebose_name(self):

        localctx = ZmeiLangParser.Col_field_vrebose_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_col_field_vrebose_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(ZmeiLangParser.SLASH)
            self.state = 416
            self.string_or_quoted()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Col_field_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZmeiLangParser.ID, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_field_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_field_name" ):
                listener.enterCol_field_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_field_name" ):
                listener.exitCol_field_name(self)




    def col_field_name(self):

        localctx = ZmeiLangParser.Col_field_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_col_field_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.match(ZmeiLangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Col_modifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(ZmeiLangParser.EQUALS, 0)

        def DOLLAR(self):
            return self.getToken(ZmeiLangParser.DOLLAR, 0)

        def AMP(self):
            return self.getToken(ZmeiLangParser.AMP, 0)

        def EXCLAM(self):
            return self.getToken(ZmeiLangParser.EXCLAM, 0)

        def STAR(self):
            return self.getToken(ZmeiLangParser.STAR, 0)

        def APPROX(self):
            return self.getToken(ZmeiLangParser.APPROX, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_modifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_modifier" ):
                listener.enterCol_modifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_modifier" ):
                listener.exitCol_modifier(self)




    def col_modifier(self):

        localctx = ZmeiLangParser.Col_modifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_col_modifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            _la = self._input.LA(1)
            if not(((((_la - 59)) & ~0x3f) == 0 and ((1 << (_la - 59)) & ((1 << (ZmeiLangParser.EQUALS - 59)) | (1 << (ZmeiLangParser.DOLLAR - 59)) | (1 << (ZmeiLangParser.AMP - 59)) | (1 << (ZmeiLangParser.EXCLAM - 59)) | (1 << (ZmeiLangParser.STAR - 59)) | (1 << (ZmeiLangParser.APPROX - 59)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AnnotationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ANNOTATION(self):
            return self.getToken(ZmeiLangParser.ANNOTATION, 0)

        def annotation_descr(self):
            return self.getTypedRuleContext(ZmeiLangParser.Annotation_descrContext,0)


        def annotation_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Annotation_codeContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_annotation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnnotation" ):
                listener.enterAnnotation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnnotation" ):
                listener.exitAnnotation(self)




    def annotation(self):

        localctx = ZmeiLangParser.AnnotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_annotation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(ZmeiLangParser.ANNOTATION)
            self.state = 424
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 423
                self.annotation_descr()


            self.state = 427
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 426
                self.annotation_code()


            self.state = 432
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 429
                    self.match(ZmeiLangParser.NL) 
                self.state = 434
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Annotation_descrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(ZmeiLangParser.DOT, 0)

        def ID(self):
            return self.getToken(ZmeiLangParser.ID, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_annotation_descr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnnotation_descr" ):
                listener.enterAnnotation_descr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnnotation_descr" ):
                listener.exitAnnotation_descr(self)




    def annotation_descr(self):

        localctx = ZmeiLangParser.Annotation_descrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_annotation_descr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.match(ZmeiLangParser.DOT)
            self.state = 436
            self.match(ZmeiLangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Annotation_codeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_annotation_code

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnnotation_code" ):
                listener.enterAnnotation_code(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnnotation_code" ):
                listener.exitAnnotation_code(self)




    def annotation_code(self):

        localctx = ZmeiLangParser.Annotation_codeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_annotation_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Xml_contentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def xml_chardata(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Xml_chardataContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Xml_chardataContext,i)


        def xml_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Xml_elementContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Xml_elementContext,i)


        def xml_reference(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Xml_referenceContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Xml_referenceContext,i)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_xml_content

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXml_content" ):
                listener.enterXml_content(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXml_content" ):
                listener.exitXml_content(self)




    def xml_content(self):

        localctx = ZmeiLangParser.Xml_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_xml_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 29)) & ~0x3f) == 0 and ((1 << (_la - 29)) & ((1 << (ZmeiLangParser.NL - 29)) | (1 << (ZmeiLangParser.WS - 29)) | (1 << (ZmeiLangParser.XML_TEXT - 29)))) != 0):
                self.state = 440
                self.xml_chardata()


            self.state = 452
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 445
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [ZmeiLangParser.XML_OPEN]:
                        self.state = 443
                        self.xml_element()
                        pass
                    elif token in [ZmeiLangParser.XML_EntityRef, ZmeiLangParser.XML_CharRef]:
                        self.state = 444
                        self.xml_reference()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 448
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if ((((_la - 29)) & ~0x3f) == 0 and ((1 << (_la - 29)) & ((1 << (ZmeiLangParser.NL - 29)) | (1 << (ZmeiLangParser.WS - 29)) | (1 << (ZmeiLangParser.XML_TEXT - 29)))) != 0):
                        self.state = 447
                        self.xml_chardata()

             
                self.state = 454
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Xml_elementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def XML_OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.XML_OPEN)
            else:
                return self.getToken(ZmeiLangParser.XML_OPEN, i)

        def xml_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Xml_nameContext,0)


        def XML_CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.XML_CLOSE)
            else:
                return self.getToken(ZmeiLangParser.XML_CLOSE, i)

        def xml_content(self):
            return self.getTypedRuleContext(ZmeiLangParser.Xml_contentContext,0)


        def XML_SLASH(self):
            return self.getToken(ZmeiLangParser.XML_SLASH, 0)

        def xml_name_end(self):
            return self.getTypedRuleContext(ZmeiLangParser.Xml_name_endContext,0)


        def xml_attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Xml_attributeContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Xml_attributeContext,i)


        def XML_SLASH_CLOSE(self):
            return self.getToken(ZmeiLangParser.XML_SLASH_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_xml_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXml_element" ):
                listener.enterXml_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXml_element" ):
                listener.exitXml_element(self)




    def xml_element(self):

        localctx = ZmeiLangParser.Xml_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_xml_element)
        self._la = 0 # Token type
        try:
            self.state = 480
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 455
                self.match(ZmeiLangParser.XML_OPEN)
                self.state = 456
                self.xml_name()
                self.state = 460
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZmeiLangParser.XML_Name:
                    self.state = 457
                    self.xml_attribute()
                    self.state = 462
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 463
                self.match(ZmeiLangParser.XML_CLOSE)
                self.state = 464
                self.xml_content()
                self.state = 465
                self.match(ZmeiLangParser.XML_OPEN)
                self.state = 466
                self.match(ZmeiLangParser.XML_SLASH)
                self.state = 467
                self.xml_name_end()
                self.state = 468
                self.match(ZmeiLangParser.XML_CLOSE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 470
                self.match(ZmeiLangParser.XML_OPEN)
                self.state = 471
                self.xml_name()
                self.state = 475
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZmeiLangParser.XML_Name:
                    self.state = 472
                    self.xml_attribute()
                    self.state = 477
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 478
                self.match(ZmeiLangParser.XML_SLASH_CLOSE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Xml_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def xml_component_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Xml_component_nameContext,0)


        def xml_tag_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Xml_tag_nameContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_xml_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXml_name" ):
                listener.enterXml_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXml_name" ):
                listener.exitXml_name(self)




    def xml_name(self):

        localctx = ZmeiLangParser.Xml_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_xml_name)
        try:
            self.state = 484
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.XML_CmpName]:
                self.enterOuterAlt(localctx, 1)
                self.state = 482
                self.xml_component_name()
                pass
            elif token in [ZmeiLangParser.XML_Name]:
                self.enterOuterAlt(localctx, 2)
                self.state = 483
                self.xml_tag_name()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Xml_name_endContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def xml_component_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Xml_component_nameContext,0)


        def xml_tag_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Xml_tag_nameContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_xml_name_end

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXml_name_end" ):
                listener.enterXml_name_end(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXml_name_end" ):
                listener.exitXml_name_end(self)




    def xml_name_end(self):

        localctx = ZmeiLangParser.Xml_name_endContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_xml_name_end)
        try:
            self.state = 488
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.XML_CmpName]:
                self.enterOuterAlt(localctx, 1)
                self.state = 486
                self.xml_component_name()
                pass
            elif token in [ZmeiLangParser.XML_Name]:
                self.enterOuterAlt(localctx, 2)
                self.state = 487
                self.xml_tag_name()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Xml_tag_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def XML_Name(self):
            return self.getToken(ZmeiLangParser.XML_Name, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_xml_tag_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXml_tag_name" ):
                listener.enterXml_tag_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXml_tag_name" ):
                listener.exitXml_tag_name(self)




    def xml_tag_name(self):

        localctx = ZmeiLangParser.Xml_tag_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_xml_tag_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            self.match(ZmeiLangParser.XML_Name)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Xml_component_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def XML_CmpName(self):
            return self.getToken(ZmeiLangParser.XML_CmpName, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_xml_component_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXml_component_name" ):
                listener.enterXml_component_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXml_component_name" ):
                listener.exitXml_component_name(self)




    def xml_component_name(self):

        localctx = ZmeiLangParser.Xml_component_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_xml_component_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            self.match(ZmeiLangParser.XML_CmpName)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Xml_referenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def XML_EntityRef(self):
            return self.getToken(ZmeiLangParser.XML_EntityRef, 0)

        def XML_CharRef(self):
            return self.getToken(ZmeiLangParser.XML_CharRef, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_xml_reference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXml_reference" ):
                listener.enterXml_reference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXml_reference" ):
                listener.exitXml_reference(self)




    def xml_reference(self):

        localctx = ZmeiLangParser.Xml_referenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_xml_reference)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.XML_EntityRef or _la==ZmeiLangParser.XML_CharRef):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Xml_attributeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def XML_Name(self):
            return self.getToken(ZmeiLangParser.XML_Name, 0)

        def XML_EQUALS(self):
            return self.getToken(ZmeiLangParser.XML_EQUALS, 0)

        def XML_STRING(self):
            return self.getToken(ZmeiLangParser.XML_STRING, 0)

        def XML_REACT_ATTR(self):
            return self.getToken(ZmeiLangParser.XML_REACT_ATTR, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_xml_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXml_attribute" ):
                listener.enterXml_attribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXml_attribute" ):
                listener.exitXml_attribute(self)




    def xml_attribute(self):

        localctx = ZmeiLangParser.Xml_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_xml_attribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496
            self.match(ZmeiLangParser.XML_Name)
            self.state = 497
            self.match(ZmeiLangParser.XML_EQUALS)
            self.state = 498
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.XML_REACT_ATTR or _la==ZmeiLangParser.XML_STRING):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Xml_chardataContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def XML_TEXT(self):
            return self.getToken(ZmeiLangParser.XML_TEXT, 0)

        def WS(self):
            return self.getToken(ZmeiLangParser.WS, 0)

        def NL(self):
            return self.getToken(ZmeiLangParser.NL, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_xml_chardata

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXml_chardata" ):
                listener.enterXml_chardata(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXml_chardata" ):
                listener.exitXml_chardata(self)




    def xml_chardata(self):

        localctx = ZmeiLangParser.Xml_chardataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_xml_chardata)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            _la = self._input.LA(1)
            if not(((((_la - 29)) & ~0x3f) == 0 and ((1 << (_la - 29)) & ((1 << (ZmeiLangParser.NL - 29)) | (1 << (ZmeiLangParser.WS - 29)) | (1 << (ZmeiLangParser.XML_TEXT - 29)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Xml_miscContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WS(self):
            return self.getToken(ZmeiLangParser.WS, 0)

        def NL(self):
            return self.getToken(ZmeiLangParser.NL, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_xml_misc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXml_misc" ):
                listener.enterXml_misc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXml_misc" ):
                listener.exitXml_misc(self)




    def xml_misc(self):

        localctx = ZmeiLangParser.Xml_miscContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_xml_misc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.NL or _la==ZmeiLangParser.WS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Col_field_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_longtext(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_longtextContext,0)


        def field_html_media(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_html_mediaContext,0)


        def field_html(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_htmlContext,0)


        def field_float(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_floatContext,0)


        def field_decimal(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_decimalContext,0)


        def field_date(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_dateContext,0)


        def field_datetime(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_datetimeContext,0)


        def field_create_time(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_create_timeContext,0)


        def field_update_time(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_update_timeContext,0)


        def field_text(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_textContext,0)


        def field_int(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_intContext,0)


        def field_slug(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_slugContext,0)


        def field_bool(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_boolContext,0)


        def field_relation(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_relationContext,0)


        def field_image_file(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_image_fileContext,0)


        def field_image(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_imageContext,0)


        def field_filer_image(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_filer_imageContext,0)


        def field_filer_file(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_filer_fileContext,0)


        def field_file(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_fileContext,0)


        def field_simple_file(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_simple_fileContext,0)


        def field_folder(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_folderContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_field_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_field_def" ):
                listener.enterCol_field_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_field_def" ):
                listener.exitCol_field_def(self)




    def col_field_def(self):

        localctx = ZmeiLangParser.Col_field_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_col_field_def)
        try:
            self.state = 525
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 504
                self.field_longtext()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 505
                self.field_html_media()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_HTML]:
                self.enterOuterAlt(localctx, 3)
                self.state = 506
                self.field_html()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_FLOAT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 507
                self.field_float()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_DECIMAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 508
                self.field_decimal()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_DATE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 509
                self.field_date()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_DATETIME]:
                self.enterOuterAlt(localctx, 7)
                self.state = 510
                self.field_datetime()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME]:
                self.enterOuterAlt(localctx, 8)
                self.state = 511
                self.field_create_time()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME]:
                self.enterOuterAlt(localctx, 9)
                self.state = 512
                self.field_update_time()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_TEXT]:
                self.enterOuterAlt(localctx, 10)
                self.state = 513
                self.field_text()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_INT]:
                self.enterOuterAlt(localctx, 11)
                self.state = 514
                self.field_int()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_SLUG]:
                self.enterOuterAlt(localctx, 12)
                self.state = 515
                self.field_slug()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_BOOL]:
                self.enterOuterAlt(localctx, 13)
                self.state = 516
                self.field_bool()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY]:
                self.enterOuterAlt(localctx, 14)
                self.state = 517
                self.field_relation()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_IMAGE_FILE]:
                self.enterOuterAlt(localctx, 15)
                self.state = 518
                self.field_image_file()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_IMAGE_FOLDER]:
                self.enterOuterAlt(localctx, 16)
                self.state = 519
                self.field_image()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE]:
                self.enterOuterAlt(localctx, 17)
                self.state = 520
                self.field_filer_image()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE]:
                self.enterOuterAlt(localctx, 18)
                self.state = 521
                self.field_filer_file()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_FILE]:
                self.enterOuterAlt(localctx, 19)
                self.state = 522
                self.field_file()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_SIMPLE_FILE]:
                self.enterOuterAlt(localctx, 20)
                self.state = 523
                self.field_simple_file()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_FOLDER]:
                self.enterOuterAlt(localctx, 21)
                self.state = 524
                self.field_folder()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_longtextContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_LONGTEXT(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_longtext

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_longtext" ):
                listener.enterField_longtext(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_longtext" ):
                listener.exitField_longtext(self)




    def field_longtext(self):

        localctx = ZmeiLangParser.Field_longtextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_field_longtext)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 527
            self.match(ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_htmlContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_HTML(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_HTML, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_html

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_html" ):
                listener.enterField_html(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_html" ):
                listener.exitField_html(self)




    def field_html(self):

        localctx = ZmeiLangParser.Field_htmlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_field_html)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
            self.match(ZmeiLangParser.COL_FIELD_TYPE_HTML)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_html_mediaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_HTML_MEDIA(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_html_media

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_html_media" ):
                listener.enterField_html_media(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_html_media" ):
                listener.exitField_html_media(self)




    def field_html_media(self):

        localctx = ZmeiLangParser.Field_html_mediaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_field_html_media)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 531
            self.match(ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_floatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_FLOAT(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_FLOAT, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_float

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_float" ):
                listener.enterField_float(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_float" ):
                listener.exitField_float(self)




    def field_float(self):

        localctx = ZmeiLangParser.Field_floatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_field_float)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            self.match(ZmeiLangParser.COL_FIELD_TYPE_FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_decimalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_DECIMAL(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_decimal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_decimal" ):
                listener.enterField_decimal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_decimal" ):
                listener.exitField_decimal(self)




    def field_decimal(self):

        localctx = ZmeiLangParser.Field_decimalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_field_decimal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 535
            self.match(ZmeiLangParser.COL_FIELD_TYPE_DECIMAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_dateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_DATE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_DATE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_date

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_date" ):
                listener.enterField_date(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_date" ):
                listener.exitField_date(self)




    def field_date(self):

        localctx = ZmeiLangParser.Field_dateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_field_date)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 537
            self.match(ZmeiLangParser.COL_FIELD_TYPE_DATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_datetimeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_DATETIME(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_DATETIME, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_datetime

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_datetime" ):
                listener.enterField_datetime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_datetime" ):
                listener.exitField_datetime(self)




    def field_datetime(self):

        localctx = ZmeiLangParser.Field_datetimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_field_datetime)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 539
            self.match(ZmeiLangParser.COL_FIELD_TYPE_DATETIME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_create_timeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_CREATE_TIME(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_create_time

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_create_time" ):
                listener.enterField_create_time(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_create_time" ):
                listener.exitField_create_time(self)




    def field_create_time(self):

        localctx = ZmeiLangParser.Field_create_timeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_field_create_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 541
            self.match(ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_update_timeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_UPDATE_TIME(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_update_time

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_update_time" ):
                listener.enterField_update_time(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_update_time" ):
                listener.exitField_update_time(self)




    def field_update_time(self):

        localctx = ZmeiLangParser.Field_update_timeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_field_update_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 543
            self.match(ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_image_fileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_IMAGE_FILE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_IMAGE_FILE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_image_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_image_file" ):
                listener.enterField_image_file(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_image_file" ):
                listener.exitField_image_file(self)




    def field_image_file(self):

        localctx = ZmeiLangParser.Field_image_fileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_field_image_file)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
            self.match(ZmeiLangParser.COL_FIELD_TYPE_IMAGE_FILE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_filer_imageContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_FILER_IMAGE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_filer_image

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_filer_image" ):
                listener.enterField_filer_image(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_filer_image" ):
                listener.exitField_filer_image(self)




    def field_filer_image(self):

        localctx = ZmeiLangParser.Field_filer_imageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_field_filer_image)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 547
            self.match(ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_filer_fileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_FILER_FILE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_filer_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_filer_file" ):
                listener.enterField_filer_file(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_filer_file" ):
                listener.exitField_filer_file(self)




    def field_filer_file(self):

        localctx = ZmeiLangParser.Field_filer_fileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_field_filer_file)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 549
            self.match(ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_fileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_FILE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_FILE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_file" ):
                listener.enterField_file(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_file" ):
                listener.exitField_file(self)




    def field_file(self):

        localctx = ZmeiLangParser.Field_fileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_field_file)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 551
            self.match(ZmeiLangParser.COL_FIELD_TYPE_FILE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_simple_fileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_SIMPLE_FILE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_SIMPLE_FILE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_simple_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_simple_file" ):
                listener.enterField_simple_file(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_simple_file" ):
                listener.exitField_simple_file(self)




    def field_simple_file(self):

        localctx = ZmeiLangParser.Field_simple_fileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_field_simple_file)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 553
            self.match(ZmeiLangParser.COL_FIELD_TYPE_SIMPLE_FILE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_folderContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_FOLDER(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_FOLDER, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_folder

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_folder" ):
                listener.enterField_folder(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_folder" ):
                listener.exitField_folder(self)




    def field_folder(self):

        localctx = ZmeiLangParser.Field_folderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_field_folder)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 555
            self.match(ZmeiLangParser.COL_FIELD_TYPE_FOLDER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_textContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_TEXT(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_TEXT, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def field_text_size(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_text_sizeContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def COMA(self):
            return self.getToken(ZmeiLangParser.COMA, 0)

        def field_text_choices(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_text_choicesContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_text

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_text" ):
                listener.enterField_text(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_text" ):
                listener.exitField_text(self)




    def field_text(self):

        localctx = ZmeiLangParser.Field_textContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_field_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 557
            self.match(ZmeiLangParser.COL_FIELD_TYPE_TEXT)
            self.state = 566
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 558
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 559
                self.field_text_size()
                self.state = 562
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.COMA:
                    self.state = 560
                    self.match(ZmeiLangParser.COMA)
                    self.state = 561
                    self.field_text_choices()


                self.state = 564
                self.match(ZmeiLangParser.BRACE_CLOSE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_text_sizeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self):
            return self.getToken(ZmeiLangParser.DIGIT, 0)

        def QUESTION_MARK(self):
            return self.getToken(ZmeiLangParser.QUESTION_MARK, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_text_size

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_text_size" ):
                listener.enterField_text_size(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_text_size" ):
                listener.exitField_text_size(self)




    def field_text_size(self):

        localctx = ZmeiLangParser.Field_text_sizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_field_text_size)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 568
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.DIGIT or _la==ZmeiLangParser.QUESTION_MARK):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_text_choicesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_CHOICES(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_CHOICES, 0)

        def EQUALS(self):
            return self.getToken(ZmeiLangParser.EQUALS, 0)

        def field_text_choice(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Field_text_choiceContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Field_text_choiceContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_text_choices

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_text_choices" ):
                listener.enterField_text_choices(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_text_choices" ):
                listener.exitField_text_choices(self)




    def field_text_choices(self):

        localctx = ZmeiLangParser.Field_text_choicesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_field_text_choices)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570
            self.match(ZmeiLangParser.COL_FIELD_CHOICES)
            self.state = 571
            self.match(ZmeiLangParser.EQUALS)
            self.state = 572
            self.field_text_choice()
            self.state = 577
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 573
                self.match(ZmeiLangParser.COMA)
                self.state = 574
                self.field_text_choice()
                self.state = 579
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_text_choiceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_text_choice_val(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_text_choice_valContext,0)


        def field_text_choice_key(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_text_choice_keyContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_text_choice

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_text_choice" ):
                listener.enterField_text_choice(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_text_choice" ):
                listener.exitField_text_choice(self)




    def field_text_choice(self):

        localctx = ZmeiLangParser.Field_text_choiceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_field_text_choice)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.state = 580
                self.field_text_choice_key()


            self.state = 583
            self.field_text_choice_val()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_text_choice_valContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZmeiLangParser.ID, 0)

        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_text_choice_val

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_text_choice_val" ):
                listener.enterField_text_choice_val(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_text_choice_val" ):
                listener.exitField_text_choice_val(self)




    def field_text_choice_val(self):

        localctx = ZmeiLangParser.Field_text_choice_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_field_text_choice_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.ID) | (1 << ZmeiLangParser.STRING_DQ) | (1 << ZmeiLangParser.STRING_SQ))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_text_choice_keyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZmeiLangParser.ID, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_text_choice_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_text_choice_key" ):
                listener.enterField_text_choice_key(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_text_choice_key" ):
                listener.exitField_text_choice_key(self)




    def field_text_choice_key(self):

        localctx = ZmeiLangParser.Field_text_choice_keyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_field_text_choice_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 587
            self.match(ZmeiLangParser.ID)
            self.state = 588
            self.match(ZmeiLangParser.COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_intContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_INT(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_INT, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def field_int_choices(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_int_choicesContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_int

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_int" ):
                listener.enterField_int(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_int" ):
                listener.exitField_int(self)




    def field_int(self):

        localctx = ZmeiLangParser.Field_intContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_field_int)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 590
            self.match(ZmeiLangParser.COL_FIELD_TYPE_INT)
            self.state = 595
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 591
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 592
                self.field_int_choices()
                self.state = 593
                self.match(ZmeiLangParser.BRACE_CLOSE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_int_choicesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_CHOICES(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_CHOICES, 0)

        def EQUALS(self):
            return self.getToken(ZmeiLangParser.EQUALS, 0)

        def field_int_choice(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Field_int_choiceContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Field_int_choiceContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_int_choices

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_int_choices" ):
                listener.enterField_int_choices(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_int_choices" ):
                listener.exitField_int_choices(self)




    def field_int_choices(self):

        localctx = ZmeiLangParser.Field_int_choicesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_field_int_choices)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 597
            self.match(ZmeiLangParser.COL_FIELD_CHOICES)
            self.state = 598
            self.match(ZmeiLangParser.EQUALS)
            self.state = 599
            self.field_int_choice()
            self.state = 604
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 600
                self.match(ZmeiLangParser.COMA)
                self.state = 601
                self.field_int_choice()
                self.state = 606
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_int_choiceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_int_choice_val(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_int_choice_valContext,0)


        def field_int_choice_key(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_int_choice_keyContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_int_choice

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_int_choice" ):
                listener.enterField_int_choice(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_int_choice" ):
                listener.exitField_int_choice(self)




    def field_int_choice(self):

        localctx = ZmeiLangParser.Field_int_choiceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_field_int_choice)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 608
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DIGIT:
                self.state = 607
                self.field_int_choice_key()


            self.state = 610
            self.field_int_choice_val()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_int_choice_valContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZmeiLangParser.ID, 0)

        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_int_choice_val

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_int_choice_val" ):
                listener.enterField_int_choice_val(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_int_choice_val" ):
                listener.exitField_int_choice_val(self)




    def field_int_choice_val(self):

        localctx = ZmeiLangParser.Field_int_choice_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_field_int_choice_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 612
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.ID) | (1 << ZmeiLangParser.STRING_DQ) | (1 << ZmeiLangParser.STRING_SQ))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_int_choice_keyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self):
            return self.getToken(ZmeiLangParser.DIGIT, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_int_choice_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_int_choice_key" ):
                listener.enterField_int_choice_key(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_int_choice_key" ):
                listener.exitField_int_choice_key(self)




    def field_int_choice_key(self):

        localctx = ZmeiLangParser.Field_int_choice_keyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_field_int_choice_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 614
            self.match(ZmeiLangParser.DIGIT)
            self.state = 615
            self.match(ZmeiLangParser.COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_slugContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_SLUG(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_SLUG, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def field_slug_ref_field(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_slug_ref_fieldContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_slug

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_slug" ):
                listener.enterField_slug(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_slug" ):
                listener.exitField_slug(self)




    def field_slug(self):

        localctx = ZmeiLangParser.Field_slugContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_field_slug)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 617
            self.match(ZmeiLangParser.COL_FIELD_TYPE_SLUG)
            self.state = 618
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 619
            self.field_slug_ref_field()
            self.state = 620
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_slug_ref_fieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_slug_ref_field_id(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Field_slug_ref_field_idContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Field_slug_ref_field_idContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_slug_ref_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_slug_ref_field" ):
                listener.enterField_slug_ref_field(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_slug_ref_field" ):
                listener.exitField_slug_ref_field(self)




    def field_slug_ref_field(self):

        localctx = ZmeiLangParser.Field_slug_ref_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_field_slug_ref_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 622
            self.field_slug_ref_field_id()
            self.state = 627
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 623
                self.match(ZmeiLangParser.COMA)
                self.state = 624
                self.field_slug_ref_field_id()
                self.state = 629
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_slug_ref_field_idContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZmeiLangParser.ID, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_slug_ref_field_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_slug_ref_field_id" ):
                listener.enterField_slug_ref_field_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_slug_ref_field_id" ):
                listener.exitField_slug_ref_field_id(self)




    def field_slug_ref_field_id(self):

        localctx = ZmeiLangParser.Field_slug_ref_field_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_field_slug_ref_field_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 630
            self.match(ZmeiLangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_boolContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_BOOL(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_BOOL, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def field_bool_default(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_bool_defaultContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_bool

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_bool" ):
                listener.enterField_bool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_bool" ):
                listener.exitField_bool(self)




    def field_bool(self):

        localctx = ZmeiLangParser.Field_boolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_field_bool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 632
            self.match(ZmeiLangParser.COL_FIELD_TYPE_BOOL)
            self.state = 637
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 633
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 634
                self.field_bool_default()
                self.state = 635
                self.match(ZmeiLangParser.BRACE_CLOSE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_bool_defaultContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(ZmeiLangParser.BOOL, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_bool_default

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_bool_default" ):
                listener.enterField_bool_default(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_bool_default" ):
                listener.exitField_bool_default(self)




    def field_bool_default(self):

        localctx = ZmeiLangParser.Field_bool_defaultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_field_bool_default)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 639
            self.match(ZmeiLangParser.BOOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_imageContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def filer_image_type(self):
            return self.getTypedRuleContext(ZmeiLangParser.Filer_image_typeContext,0)


        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def field_image_sizes(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_image_sizesContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_image

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_image" ):
                listener.enterField_image(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_image" ):
                listener.exitField_image(self)




    def field_image(self):

        localctx = ZmeiLangParser.Field_imageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_field_image)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 641
            self.filer_image_type()
            self.state = 646
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 642
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 643
                self.field_image_sizes()
                self.state = 644
                self.match(ZmeiLangParser.BRACE_CLOSE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Filer_image_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_IMAGE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_IMAGE, 0)

        def COL_FIELD_TYPE_IMAGE_FOLDER(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_IMAGE_FOLDER, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_filer_image_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFiler_image_type" ):
                listener.enterFiler_image_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFiler_image_type" ):
                listener.exitFiler_image_type(self)




    def filer_image_type(self):

        localctx = ZmeiLangParser.Filer_image_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_filer_image_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 648
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.COL_FIELD_TYPE_IMAGE or _la==ZmeiLangParser.COL_FIELD_TYPE_IMAGE_FOLDER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_image_sizesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_image_size(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Field_image_sizeContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Field_image_sizeContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_image_sizes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_image_sizes" ):
                listener.enterField_image_sizes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_image_sizes" ):
                listener.exitField_image_sizes(self)




    def field_image_sizes(self):

        localctx = ZmeiLangParser.Field_image_sizesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_field_image_sizes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 650
            self.field_image_size()
            self.state = 655
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 651
                self.match(ZmeiLangParser.COMA)
                self.state = 652
                self.field_image_size()
                self.state = 657
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_image_sizeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_image_size_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_image_size_nameContext,0)


        def field_image_size_dimensions(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_image_size_dimensionsContext,0)


        def field_image_filters(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_image_filtersContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_image_size

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_image_size" ):
                listener.enterField_image_size(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_image_size" ):
                listener.exitField_image_size(self)




    def field_image_size(self):

        localctx = ZmeiLangParser.Field_image_sizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_field_image_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 658
            self.field_image_size_name()
            self.state = 659
            self.field_image_size_dimensions()
            self.state = 660
            self.field_image_filters()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_image_size_dimensionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIZE2D(self):
            return self.getToken(ZmeiLangParser.SIZE2D, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_image_size_dimensions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_image_size_dimensions" ):
                listener.enterField_image_size_dimensions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_image_size_dimensions" ):
                listener.exitField_image_size_dimensions(self)




    def field_image_size_dimensions(self):

        localctx = ZmeiLangParser.Field_image_size_dimensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_field_image_size_dimensions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 662
            self.match(ZmeiLangParser.SIZE2D)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_image_size_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZmeiLangParser.ID, 0)

        def EQUALS(self):
            return self.getToken(ZmeiLangParser.EQUALS, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_image_size_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_image_size_name" ):
                listener.enterField_image_size_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_image_size_name" ):
                listener.exitField_image_size_name(self)




    def field_image_size_name(self):

        localctx = ZmeiLangParser.Field_image_size_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_field_image_size_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 664
            self.match(ZmeiLangParser.ID)
            self.state = 665
            self.match(ZmeiLangParser.EQUALS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_image_filtersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_image_filter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Field_image_filterContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Field_image_filterContext,i)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_image_filters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_image_filters" ):
                listener.enterField_image_filters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_image_filters" ):
                listener.exitField_image_filters(self)




    def field_image_filters(self):

        localctx = ZmeiLangParser.Field_image_filtersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_field_image_filters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 670
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.FILTER:
                self.state = 667
                self.field_image_filter()
                self.state = 672
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_image_filterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FILTER(self):
            return self.getToken(ZmeiLangParser.FILTER, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_image_filter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_image_filter" ):
                listener.enterField_image_filter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_image_filter" ):
                listener.exitField_image_filter(self)




    def field_image_filter(self):

        localctx = ZmeiLangParser.Field_image_filterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_field_image_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 673
            self.match(ZmeiLangParser.FILTER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_relationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_relation_type(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_relation_typeContext,0)


        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def field_relation_target_ref(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_relation_target_refContext,0)


        def field_relation_target_class(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_relation_target_classContext,0)


        def field_relation_related_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_relation_related_nameContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_relation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_relation" ):
                listener.enterField_relation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_relation" ):
                listener.exitField_relation(self)




    def field_relation(self):

        localctx = ZmeiLangParser.Field_relationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_field_relation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 675
            self.field_relation_type()
            self.state = 676
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 679
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.REF_SIGN]:
                self.state = 677
                self.field_relation_target_ref()
                pass
            elif token in [ZmeiLangParser.CLASSNAME]:
                self.state = 678
                self.field_relation_target_class()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 682
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.RELATED:
                self.state = 681
                self.field_relation_related_name()


            self.state = 684
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_relation_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_ONE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_ONE, 0)

        def COL_FIELD_TYPE_ONE2ONE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, 0)

        def COL_FIELD_TYPE_MANY(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_MANY, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_relation_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_relation_type" ):
                listener.enterField_relation_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_relation_type" ):
                listener.exitField_relation_type(self)




    def field_relation_type(self):

        localctx = ZmeiLangParser.Field_relation_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_field_relation_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 686
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.COL_FIELD_TYPE_ONE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_MANY))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_relation_target_refContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REF_SIGN(self):
            return self.getToken(ZmeiLangParser.REF_SIGN, 0)

        def ID(self):
            return self.getToken(ZmeiLangParser.ID, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_relation_target_ref

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_relation_target_ref" ):
                listener.enterField_relation_target_ref(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_relation_target_ref" ):
                listener.exitField_relation_target_ref(self)




    def field_relation_target_ref(self):

        localctx = ZmeiLangParser.Field_relation_target_refContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_field_relation_target_ref)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 688
            self.match(ZmeiLangParser.REF_SIGN)
            self.state = 689
            self.match(ZmeiLangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_relation_target_classContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASSNAME(self):
            return self.getToken(ZmeiLangParser.CLASSNAME, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_relation_target_class

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_relation_target_class" ):
                listener.enterField_relation_target_class(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_relation_target_class" ):
                listener.exitField_relation_target_class(self)




    def field_relation_target_class(self):

        localctx = ZmeiLangParser.Field_relation_target_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_field_relation_target_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 691
            self.match(ZmeiLangParser.CLASSNAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_relation_related_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RELATED(self):
            return self.getToken(ZmeiLangParser.RELATED, 0)

        def ID(self):
            return self.getToken(ZmeiLangParser.ID, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_relation_related_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_relation_related_name" ):
                listener.enterField_relation_related_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_relation_related_name" ):
                listener.exitField_relation_related_name(self)




    def field_relation_related_name(self):

        localctx = ZmeiLangParser.Field_relation_related_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_field_relation_related_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 693
            self.match(ZmeiLangParser.RELATED)
            self.state = 694
            self.match(ZmeiLangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






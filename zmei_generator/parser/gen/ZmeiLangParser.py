# Generated from /Users/aleksandrrudakov/dev/generator/grammar/ZmeiLangParser.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3g")
        buf.write("\u03a3\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("V\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4^\t^\4")
        buf.write("_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4g\tg\4")
        buf.write("h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\4n\tn\4o\to\4p\tp\4")
        buf.write("q\tq\3\2\5\2\u00e4\n\2\3\2\7\2\u00e7\n\2\f\2\16\2\u00ea")
        buf.write("\13\2\3\2\7\2\u00ed\n\2\f\2\16\2\u00f0\13\2\3\2\7\2\u00f3")
        buf.write("\n\2\f\2\16\2\u00f6\13\2\3\2\5\2\u00f9\n\2\3\2\7\2\u00fc")
        buf.write("\n\2\f\2\16\2\u00ff\13\2\3\2\7\2\u0102\n\2\f\2\16\2\u0105")
        buf.write("\13\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\6\3\6")
        buf.write("\7\6\u0113\n\6\f\6\16\6\u0116\13\6\3\6\3\6\3\7\3\7\5\7")
        buf.write("\u011c\n\7\3\7\3\7\5\7\u0120\n\7\3\7\3\7\5\7\u0124\n\7")
        buf.write("\3\7\3\7\5\7\u0128\n\7\5\7\u012a\n\7\3\7\3\7\3\7\7\7\u012f")
        buf.write("\n\7\f\7\16\7\u0132\13\7\3\7\7\7\u0135\n\7\f\7\16\7\u0138")
        buf.write("\13\7\3\7\5\7\u013b\n\7\3\7\7\7\u013e\n\7\f\7\16\7\u0141")
        buf.write("\13\7\3\7\5\7\u0144\n\7\3\7\7\7\u0147\n\7\f\7\16\7\u014a")
        buf.write("\13\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3")
        buf.write("\f\3\r\3\r\5\r\u015a\n\r\3\16\3\16\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\6\20\u0164\n\20\r\20\16\20\u0165\3\20\5\20")
        buf.write("\u0169\n\20\3\21\3\21\3\22\3\22\3\23\3\23\5\23\u0171\n")
        buf.write("\23\3\23\7\23\u0174\n\23\f\23\16\23\u0177\13\23\3\23\7")
        buf.write("\23\u017a\n\23\f\23\16\23\u017d\13\23\3\24\3\24\3\24\6")
        buf.write("\24\u0182\n\24\r\24\16\24\u0183\3\24\5\24\u0187\n\24\3")
        buf.write("\25\3\25\5\25\u018b\n\25\3\25\3\25\5\25\u018f\n\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\5\26\u0198\n\26\3\27\3")
        buf.write("\27\3\27\5\27\u019d\n\27\3\30\3\30\3\30\3\31\3\31\3\32")
        buf.write("\7\32\u01a5\n\32\f\32\16\32\u01a8\13\32\3\32\3\32\3\32")
        buf.write("\3\32\5\32\u01ae\n\32\3\32\5\32\u01b1\n\32\3\32\5\32\u01b4")
        buf.write("\n\32\3\32\6\32\u01b7\n\32\r\32\16\32\u01b8\3\32\5\32")
        buf.write("\u01bc\n\32\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\36\6")
        buf.write("\36\u01c6\n\36\r\36\16\36\u01c7\3\36\3\36\5\36\u01cc\n")
        buf.write("\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$")
        buf.write("\3$\3$\3$\3$\3$\3$\3$\3$\3$\7$\u01e5\n$\f$\16$\u01e8\13")
        buf.write("$\3$\5$\u01eb\n$\3$\7$\u01ee\n$\f$\16$\u01f1\13$\3$\5")
        buf.write("$\u01f4\n$\3$\7$\u01f7\n$\f$\16$\u01fa\13$\3%\3%\3%\3")
        buf.write("%\3%\7%\u0201\n%\f%\16%\u0204\13%\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\7&\u020d\n&\f&\16&\u0210\13&\3&\5&\u0213\n&\3\'\3\'")
        buf.write("\3(\3(\3(\3(\3)\3)\3)\3)\3*\3*\3*\3*\3+\3+\3+\3+\3+\7")
        buf.write("+\u0228\n+\f+\16+\u022b\13+\3,\3,\5,\u022f\n,\3,\3,\3")
        buf.write(",\3,\3-\3-\3.\3.\3/\3/\3/\3/\7/\u023d\n/\f/\16/\u0240")
        buf.write("\13/\3\60\3\60\3\60\3\60\7\60\u0246\n\60\f\60\16\60\u0249")
        buf.write("\13\60\3\61\3\61\3\61\3\61\7\61\u024f\n\61\f\61\16\61")
        buf.write("\u0252\13\61\3\62\3\62\3\62\3\62\7\62\u0258\n\62\f\62")
        buf.write("\16\62\u025b\13\62\3\63\3\63\3\63\3\63\7\63\u0261\n\63")
        buf.write("\f\63\16\63\u0264\13\63\3\64\3\64\3\64\3\64\7\64\u026a")
        buf.write("\n\64\f\64\16\64\u026d\13\64\3\65\5\65\u0270\n\65\3\65")
        buf.write("\3\65\3\65\3\65\7\65\u0276\n\65\f\65\16\65\u0279\13\65")
        buf.write("\3\65\3\65\3\65\5\65\u027e\n\65\3\65\7\65\u0281\n\65\f")
        buf.write("\65\16\65\u0284\13\65\5\65\u0286\n\65\3\66\5\66\u0289")
        buf.write("\n\66\3\66\3\66\5\66\u028d\n\66\3\67\3\67\5\67\u0291\n")
        buf.write("\67\3\67\5\67\u0294\n\67\3\67\7\67\u0297\n\67\f\67\16")
        buf.write("\67\u029a\13\67\38\38\38\39\39\3:\5:\u02a2\n:\3:\3:\5")
        buf.write(":\u02a6\n:\3:\5:\u02a9\n:\7:\u02ab\n:\f:\16:\u02ae\13")
        buf.write(":\3;\3;\3;\7;\u02b3\n;\f;\16;\u02b6\13;\3;\3;\3;\3;\3")
        buf.write(";\3;\3;\3;\3;\3;\7;\u02c2\n;\f;\16;\u02c5\13;\3;\3;\5")
        buf.write(";\u02c9\n;\3<\3<\5<\u02cd\n<\3=\3=\5=\u02d1\n=\3>\3>\3")
        buf.write("?\3?\3@\3@\3A\3A\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3E\3E\3")
        buf.write("E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\5E\u02f8")
        buf.write("\nE\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3K\3K\3L\3L\3M\3M\3")
        buf.write("N\3N\3O\3O\3P\3P\3Q\3Q\3R\3R\3S\3S\3T\3T\3U\3U\3U\3U\3")
        buf.write("U\5U\u031d\nU\3U\3U\5U\u0321\nU\3V\3V\3W\3W\3W\3W\3W\7")
        buf.write("W\u032a\nW\fW\16W\u032d\13W\3X\5X\u0330\nX\3X\3X\3Y\3")
        buf.write("Y\3Z\3Z\3Z\3[\3[\3[\3[\3[\5[\u033e\n[\3\\\3\\\3\\\3\\")
        buf.write("\3\\\7\\\u0345\n\\\f\\\16\\\u0348\13\\\3]\5]\u034b\n]")
        buf.write("\3]\3]\3^\3^\3_\3_\3_\3`\3`\3`\3`\3`\3a\3a\3a\7a\u035c")
        buf.write("\na\fa\16a\u035f\13a\3b\3b\3c\3c\3c\3c\3c\5c\u0368\nc")
        buf.write("\3d\3d\3e\3e\3e\3e\3e\5e\u0371\ne\3f\3f\3g\3g\3g\7g\u0378")
        buf.write("\ng\fg\16g\u037b\13g\3h\3h\3h\3h\3i\3i\3j\3j\3j\3k\7k")
        buf.write("\u0387\nk\fk\16k\u038a\13k\3l\3l\3m\3m\3m\3m\5m\u0392")
        buf.write("\nm\3m\5m\u0395\nm\3m\3m\3n\3n\3o\3o\3o\3p\3p\3q\3q\3")
        buf.write("q\3q\2\2r\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&")
        buf.write("(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~")
        buf.write("\u0080\u0082\u0084\u0086\u0088\u008a\u008c\u008e\u0090")
        buf.write("\u0092\u0094\u0096\u0098\u009a\u009c\u009e\u00a0\u00a2")
        buf.write("\u00a4\u00a6\u00a8\u00aa\u00ac\u00ae\u00b0\u00b2\u00b4")
        buf.write("\u00b6\u00b8\u00ba\u00bc\u00be\u00c0\u00c2\u00c4\u00c6")
        buf.write("\u00c8\u00ca\u00cc\u00ce\u00d0\u00d2\u00d4\u00d6\u00d8")
        buf.write("\u00da\u00dc\u00de\u00e0\2\20\5\2,,//DD\3\2;<\3\2>?\3")
        buf.write("\2EF\3\2JO\3\2Z[\3\2cd\5\2++PP\\\\\4\2++PP\4\2\4*--\4")
        buf.write("\2..88\4\2--;<\4\2\34\34\"\"\3\2\')\2\u03ad\2\u00e3\3")
        buf.write("\2\2\2\4\u0108\3\2\2\2\6\u010b\3\2\2\2\b\u010e\3\2\2\2")
        buf.write("\n\u0110\3\2\2\2\f\u0119\3\2\2\2\16\u014b\3\2\2\2\20\u014e")
        buf.write("\3\2\2\2\22\u0151\3\2\2\2\24\u0153\3\2\2\2\26\u0155\3")
        buf.write("\2\2\2\30\u0159\3\2\2\2\32\u015b\3\2\2\2\34\u015d\3\2")
        buf.write("\2\2\36\u015f\3\2\2\2 \u016a\3\2\2\2\"\u016c\3\2\2\2$")
        buf.write("\u016e\3\2\2\2&\u017e\3\2\2\2(\u0188\3\2\2\2*\u0193\3")
        buf.write("\2\2\2,\u019c\3\2\2\2.\u019e\3\2\2\2\60\u01a1\3\2\2\2")
        buf.write("\62\u01a6\3\2\2\2\64\u01bd\3\2\2\2\66\u01c0\3\2\2\28\u01c2")
        buf.write("\3\2\2\2:\u01cb\3\2\2\2<\u01cd\3\2\2\2>\u01d0\3\2\2\2")
        buf.write("@\u01d3\3\2\2\2B\u01d5\3\2\2\2D\u01d7\3\2\2\2F\u01d9\3")
        buf.write("\2\2\2H\u01fb\3\2\2\2J\u0205\3\2\2\2L\u0214\3\2\2\2N\u0216")
        buf.write("\3\2\2\2P\u021a\3\2\2\2R\u021e\3\2\2\2T\u0222\3\2\2\2")
        buf.write("V\u022c\3\2\2\2X\u0234\3\2\2\2Z\u0236\3\2\2\2\\\u0238")
        buf.write("\3\2\2\2^\u0241\3\2\2\2`\u024a\3\2\2\2b\u0253\3\2\2\2")
        buf.write("d\u025c\3\2\2\2f\u0265\3\2\2\2h\u0285\3\2\2\2j\u0288\3")
        buf.write("\2\2\2l\u028e\3\2\2\2n\u029b\3\2\2\2p\u029e\3\2\2\2r\u02a1")
        buf.write("\3\2\2\2t\u02c8\3\2\2\2v\u02cc\3\2\2\2x\u02d0\3\2\2\2")
        buf.write("z\u02d2\3\2\2\2|\u02d4\3\2\2\2~\u02d6\3\2\2\2\u0080\u02d8")
        buf.write("\3\2\2\2\u0082\u02dc\3\2\2\2\u0084\u02de\3\2\2\2\u0086")
        buf.write("\u02e0\3\2\2\2\u0088\u02f7\3\2\2\2\u008a\u02f9\3\2\2\2")
        buf.write("\u008c\u02fb\3\2\2\2\u008e\u02fd\3\2\2\2\u0090\u02ff\3")
        buf.write("\2\2\2\u0092\u0301\3\2\2\2\u0094\u0303\3\2\2\2\u0096\u0305")
        buf.write("\3\2\2\2\u0098\u0307\3\2\2\2\u009a\u0309\3\2\2\2\u009c")
        buf.write("\u030b\3\2\2\2\u009e\u030d\3\2\2\2\u00a0\u030f\3\2\2\2")
        buf.write("\u00a2\u0311\3\2\2\2\u00a4\u0313\3\2\2\2\u00a6\u0315\3")
        buf.write("\2\2\2\u00a8\u0317\3\2\2\2\u00aa\u0322\3\2\2\2\u00ac\u0324")
        buf.write("\3\2\2\2\u00ae\u032f\3\2\2\2\u00b0\u0333\3\2\2\2\u00b2")
        buf.write("\u0335\3\2\2\2\u00b4\u0338\3\2\2\2\u00b6\u033f\3\2\2\2")
        buf.write("\u00b8\u034a\3\2\2\2\u00ba\u034e\3\2\2\2\u00bc\u0350\3")
        buf.write("\2\2\2\u00be\u0353\3\2\2\2\u00c0\u0358\3\2\2\2\u00c2\u0360")
        buf.write("\3\2\2\2\u00c4\u0362\3\2\2\2\u00c6\u0369\3\2\2\2\u00c8")
        buf.write("\u036b\3\2\2\2\u00ca\u0372\3\2\2\2\u00cc\u0374\3\2\2\2")
        buf.write("\u00ce\u037c\3\2\2\2\u00d0\u0380\3\2\2\2\u00d2\u0382\3")
        buf.write("\2\2\2\u00d4\u0388\3\2\2\2\u00d6\u038b\3\2\2\2\u00d8\u038d")
        buf.write("\3\2\2\2\u00da\u0398\3\2\2\2\u00dc\u039a\3\2\2\2\u00de")
        buf.write("\u039d\3\2\2\2\u00e0\u039f\3\2\2\2\u00e2\u00e4\5\4\3\2")
        buf.write("\u00e3\u00e2\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e8\3")
        buf.write("\2\2\2\u00e5\u00e7\7+\2\2\u00e6\u00e5\3\2\2\2\u00e7\u00ea")
        buf.write("\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9")
        buf.write("\u00ee\3\2\2\2\u00ea\u00e8\3\2\2\2\u00eb\u00ed\5l\67\2")
        buf.write("\u00ec\u00eb\3\2\2\2\u00ed\u00f0\3\2\2\2\u00ee\u00ec\3")
        buf.write("\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f4\3\2\2\2\u00f0\u00ee")
        buf.write("\3\2\2\2\u00f1\u00f3\5\f\7\2\u00f2\u00f1\3\2\2\2\u00f3")
        buf.write("\u00f6\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2")
        buf.write("\u00f5\u00f8\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f7\u00f9\5")
        buf.write("\6\4\2\u00f8\u00f7\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u00fd")
        buf.write("\3\2\2\2\u00fa\u00fc\5$\23\2\u00fb\u00fa\3\2\2\2\u00fc")
        buf.write("\u00ff\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fe\3\2\2\2")
        buf.write("\u00fe\u0103\3\2\2\2\u00ff\u00fd\3\2\2\2\u0100\u0102\7")
        buf.write("+\2\2\u0101\u0100\3\2\2\2\u0102\u0105\3\2\2\2\u0103\u0101")
        buf.write("\3\2\2\2\u0103\u0104\3\2\2\2\u0104\u0106\3\2\2\2\u0105")
        buf.write("\u0103\3\2\2\2\u0106\u0107\7\2\2\3\u0107\3\3\2\2\2\u0108")
        buf.write("\u0109\7\20\2\2\u0109\u010a\5\b\5\2\u010a\5\3\2\2\2\u010b")
        buf.write("\u010c\7\20\2\2\u010c\u010d\5\b\5\2\u010d\7\3\2\2\2\u010e")
        buf.write("\u010f\5\n\6\2\u010f\t\3\2\2\2\u0110\u0114\7R\2\2\u0111")
        buf.write("\u0113\7T\2\2\u0112\u0111\3\2\2\2\u0113\u0116\3\2\2\2")
        buf.write("\u0114\u0112\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0117\3")
        buf.write("\2\2\2\u0116\u0114\3\2\2\2\u0117\u0118\7U\2\2\u0118\13")
        buf.write("\3\2\2\2\u0119\u011b\7\66\2\2\u011a\u011c\5\16\b\2\u011b")
        buf.write("\u011a\3\2\2\2\u011b\u011c\3\2\2\2\u011c\u011d\3\2\2\2")
        buf.write("\u011d\u011f\5\34\17\2\u011e\u0120\5\20\t\2\u011f\u011e")
        buf.write("\3\2\2\2\u011f\u0120\3\2\2\2\u0120\u0129\3\2\2\2\u0121")
        buf.write("\u0123\7\62\2\2\u0122\u0124\5\30\r\2\u0123\u0122\3\2\2")
        buf.write("\2\u0123\u0124\3\2\2\2\u0124\u0127\3\2\2\2\u0125\u0126")
        buf.write("\7\62\2\2\u0126\u0128\5\26\f\2\u0127\u0125\3\2\2\2\u0127")
        buf.write("\u0128\3\2\2\2\u0128\u012a\3\2\2\2\u0129\u0121\3\2\2\2")
        buf.write("\u0129\u012a\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012c\7")
        buf.write("\67\2\2\u012c\u0130\7+\2\2\u012d\u012f\5\36\20\2\u012e")
        buf.write("\u012d\3\2\2\2\u012f\u0132\3\2\2\2\u0130\u012e\3\2\2\2")
        buf.write("\u0130\u0131\3\2\2\2\u0131\u0136\3\2\2\2\u0132\u0130\3")
        buf.write("\2\2\2\u0133\u0135\5l\67\2\u0134\u0133\3\2\2\2\u0135\u0138")
        buf.write("\3\2\2\2\u0136\u0134\3\2\2\2\u0136\u0137\3\2\2\2\u0137")
        buf.write("\u013a\3\2\2\2\u0138\u0136\3\2\2\2\u0139\u013b\5\32\16")
        buf.write("\2\u013a\u0139\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u013f")
        buf.write("\3\2\2\2\u013c\u013e\5l\67\2\u013d\u013c\3\2\2\2\u013e")
        buf.write("\u0141\3\2\2\2\u013f\u013d\3\2\2\2\u013f\u0140\3\2\2\2")
        buf.write("\u0140\u0143\3\2\2\2\u0141\u013f\3\2\2\2\u0142\u0144\5")
        buf.write("\24\13\2\u0143\u0142\3\2\2\2\u0143\u0144\3\2\2\2\u0144")
        buf.write("\u0148\3\2\2\2\u0145\u0147\7+\2\2\u0146\u0145\3\2\2\2")
        buf.write("\u0147\u014a\3\2\2\2\u0148\u0146\3\2\2\2\u0148\u0149\3")
        buf.write("\2\2\2\u0149\r\3\2\2\2\u014a\u0148\3\2\2\2\u014b\u014c")
        buf.write("\5\u0086D\2\u014c\u014d\7>\2\2\u014d\17\3\2\2\2\u014e")
        buf.write("\u014f\7\21\2\2\u014f\u0150\5\22\n\2\u0150\21\3\2\2\2")
        buf.write("\u0151\u0152\5\u0086D\2\u0152\23\3\2\2\2\u0153\u0154\5")
        buf.write("t;\2\u0154\25\3\2\2\2\u0155\u0156\t\2\2\2\u0156\27\3\2")
        buf.write("\2\2\u0157\u015a\5\u0086D\2\u0158\u015a\7C\2\2\u0159\u0157")
        buf.write("\3\2\2\2\u0159\u0158\3\2\2\2\u015a\31\3\2\2\2\u015b\u015c")
        buf.write("\5\n\6\2\u015c\33\3\2\2\2\u015d\u015e\5\u0086D\2\u015e")
        buf.write("\35\3\2\2\2\u015f\u0160\5 \21\2\u0160\u0161\7E\2\2\u0161")
        buf.write("\u0168\5\"\22\2\u0162\u0164\7+\2\2\u0163\u0162\3\2\2\2")
        buf.write("\u0164\u0165\3\2\2\2\u0165\u0163\3\2\2\2\u0165\u0166\3")
        buf.write("\2\2\2\u0166\u0169\3\2\2\2\u0167\u0169\7\2\2\3\u0168\u0163")
        buf.write("\3\2\2\2\u0168\u0167\3\2\2\2\u0169\37\3\2\2\2\u016a\u016b")
        buf.write("\5\u0086D\2\u016b!\3\2\2\2\u016c\u016d\7V\2\2\u016d#\3")
        buf.write("\2\2\2\u016e\u0170\5(\25\2\u016f\u0171\5&\24\2\u0170\u016f")
        buf.write("\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u0175\3\2\2\2\u0172")
        buf.write("\u0174\5\62\32\2\u0173\u0172\3\2\2\2\u0174\u0177\3\2\2")
        buf.write("\2\u0175\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u017b")
        buf.write("\3\2\2\2\u0177\u0175\3\2\2\2\u0178\u017a\5D#\2\u0179\u0178")
        buf.write("\3\2\2\2\u017a\u017d\3\2\2\2\u017b\u0179\3\2\2\2\u017b")
        buf.write("\u017c\3\2\2\2\u017c%\3\2\2\2\u017d\u017b\3\2\2\2\u017e")
        buf.write("\u017f\7J\2\2\u017f\u0186\t\3\2\2\u0180\u0182\7+\2\2\u0181")
        buf.write("\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0181\3\2\2\2")
        buf.write("\u0183\u0184\3\2\2\2\u0184\u0187\3\2\2\2\u0185\u0187\7")
        buf.write("\2\2\3\u0186\u0181\3\2\2\2\u0186\u0185\3\2\2\2\u0187\'")
        buf.write("\3\2\2\2\u0188\u018a\7@\2\2\u0189\u018b\5.\30\2\u018a")
        buf.write("\u0189\3\2\2\2\u018a\u018b\3\2\2\2\u018b\u018c\3\2\2\2")
        buf.write("\u018c\u018e\5\60\31\2\u018d\u018f\5*\26\2\u018e\u018d")
        buf.write("\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u0190\3\2\2\2\u0190")
        buf.write("\u0191\7B\2\2\u0191\u0192\7+\2\2\u0192)\3\2\2\2\u0193")
        buf.write("\u0194\7\62\2\2\u0194\u0197\5,\27\2\u0195\u0196\7I\2\2")
        buf.write("\u0196\u0198\5,\27\2\u0197\u0195\3\2\2\2\u0197\u0198\3")
        buf.write("\2\2\2\u0198+\3\2\2\2\u0199\u019d\5\u0086D\2\u019a\u019d")
        buf.write("\7;\2\2\u019b\u019d\7<\2\2\u019c\u0199\3\2\2\2\u019c\u019a")
        buf.write("\3\2\2\2\u019c\u019b\3\2\2\2\u019d-\3\2\2\2\u019e\u019f")
        buf.write("\5\u0086D\2\u019f\u01a0\t\4\2\2\u01a0/\3\2\2\2\u01a1\u01a2")
        buf.write("\5\u0086D\2\u01a2\61\3\2\2\2\u01a3\u01a5\5B\"\2\u01a4")
        buf.write("\u01a3\3\2\2\2\u01a5\u01a8\3\2\2\2\u01a6\u01a4\3\2\2\2")
        buf.write("\u01a6\u01a7\3\2\2\2\u01a7\u01a9\3\2\2\2\u01a8\u01a6\3")
        buf.write("\2\2\2\u01a9\u01ad\5@!\2\u01aa\u01ab\7\62\2\2\u01ab\u01ae")
        buf.write("\5\u0088E\2\u01ac\u01ae\5\64\33\2\u01ad\u01aa\3\2\2\2")
        buf.write("\u01ad\u01ac\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01b0\3")
        buf.write("\2\2\2\u01af\u01b1\5> \2\u01b0\u01af\3\2\2\2\u01b0\u01b1")
        buf.write("\3\2\2\2\u01b1\u01b3\3\2\2\2\u01b2\u01b4\5<\37\2\u01b3")
        buf.write("\u01b2\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01bb\3\2\2\2")
        buf.write("\u01b5\u01b7\7+\2\2\u01b6\u01b5\3\2\2\2\u01b7\u01b8\3")
        buf.write("\2\2\2\u01b8\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01bc")
        buf.write("\3\2\2\2\u01ba\u01bc\7\2\2\3\u01bb\u01b6\3\2\2\2\u01bb")
        buf.write("\u01ba\3\2\2\2\u01bc\63\3\2\2\2\u01bd\u01be\5\66\34\2")
        buf.write("\u01be\u01bf\58\35\2\u01bf\65\3\2\2\2\u01c0\u01c1\t\5")
        buf.write("\2\2\u01c1\67\3\2\2\2\u01c2\u01c3\7V\2\2\u01c39\3\2\2")
        buf.write("\2\u01c4\u01c6\5\u0086D\2\u01c5\u01c4\3\2\2\2\u01c6\u01c7")
        buf.write("\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8")
        buf.write("\u01cc\3\2\2\2\u01c9\u01cc\7;\2\2\u01ca\u01cc\7<\2\2\u01cb")
        buf.write("\u01c5\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cb\u01ca\3\2\2\2")
        buf.write("\u01cc;\3\2\2\2\u01cd\u01ce\78\2\2\u01ce\u01cf\5:\36\2")
        buf.write("\u01cf=\3\2\2\2\u01d0\u01d1\7I\2\2\u01d1\u01d2\5:\36\2")
        buf.write("\u01d2?\3\2\2\2\u01d3\u01d4\5\u0086D\2\u01d4A\3\2\2\2")
        buf.write("\u01d5\u01d6\t\6\2\2\u01d6C\3\2\2\2\u01d7\u01d8\5F$\2")
        buf.write("\u01d8E\3\2\2\2\u01d9\u01f3\7\3\2\2\u01da\u01e6\7\64\2")
        buf.write("\2\u01db\u01e5\5\\/\2\u01dc\u01e5\5^\60\2\u01dd\u01e5")
        buf.write("\5`\61\2\u01de\u01e5\5b\62\2\u01df\u01e5\5d\63\2\u01e0")
        buf.write("\u01e5\5f\64\2\u01e1\u01e5\5H%\2\u01e2\u01e5\7+\2\2\u01e3")
        buf.write("\u01e5\79\2\2\u01e4\u01db\3\2\2\2\u01e4\u01dc\3\2\2\2")
        buf.write("\u01e4\u01dd\3\2\2\2\u01e4\u01de\3\2\2\2\u01e4\u01df\3")
        buf.write("\2\2\2\u01e4\u01e0\3\2\2\2\u01e4\u01e1\3\2\2\2\u01e4\u01e2")
        buf.write("\3\2\2\2\u01e4\u01e3\3\2\2\2\u01e5\u01e8\3\2\2\2\u01e6")
        buf.write("\u01e4\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01ea\3\2\2\2")
        buf.write("\u01e8\u01e6\3\2\2\2\u01e9\u01eb\5T+\2\u01ea\u01e9\3\2")
        buf.write("\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ef\3\2\2\2\u01ec\u01ee")
        buf.write("\7+\2\2\u01ed\u01ec\3\2\2\2\u01ee\u01f1\3\2\2\2\u01ef")
        buf.write("\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01f2\3\2\2\2")
        buf.write("\u01f1\u01ef\3\2\2\2\u01f2\u01f4\7\65\2\2\u01f3\u01da")
        buf.write("\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4\u01f8\3\2\2\2\u01f5")
        buf.write("\u01f7\7+\2\2\u01f6\u01f5\3\2\2\2\u01f7\u01fa\3\2\2\2")
        buf.write("\u01f8\u01f6\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9G\3\2\2")
        buf.write("\2\u01fa\u01f8\3\2\2\2\u01fb\u01fc\7\6\2\2\u01fc\u01fd")
        buf.write("\7\62\2\2\u01fd\u0202\5J&\2\u01fe\u01ff\79\2\2\u01ff\u0201")
        buf.write("\5J&\2\u0200\u01fe\3\2\2\2\u0201\u0204\3\2\2\2\u0202\u0200")
        buf.write("\3\2\2\2\u0202\u0203\3\2\2\2\u0203I\3\2\2\2\u0204\u0202")
        buf.write("\3\2\2\2\u0205\u0212\5L\'\2\u0206\u020e\7\64\2\2\u0207")
        buf.write("\u020d\5N(\2\u0208\u020d\5P)\2\u0209\u020d\5R*\2\u020a")
        buf.write("\u020d\7+\2\2\u020b\u020d\79\2\2\u020c\u0207\3\2\2\2\u020c")
        buf.write("\u0208\3\2\2\2\u020c\u0209\3\2\2\2\u020c\u020a\3\2\2\2")
        buf.write("\u020c\u020b\3\2\2\2\u020d\u0210\3\2\2\2\u020e\u020c\3")
        buf.write("\2\2\2\u020e\u020f\3\2\2\2\u020f\u0211\3\2\2\2\u0210\u020e")
        buf.write("\3\2\2\2\u0211\u0213\7\65\2\2\u0212\u0206\3\2\2\2\u0212")
        buf.write("\u0213\3\2\2\2\u0213K\3\2\2\2\u0214\u0215\5\u0086D\2\u0215")
        buf.write("M\3\2\2\2\u0216\u0217\7\7\2\2\u0217\u0218\7\62\2\2\u0218")
        buf.write("\u0219\7\5\2\2\u0219O\3\2\2\2\u021a\u021b\7\b\2\2\u021b")
        buf.write("\u021c\7\62\2\2\u021c\u021d\7.\2\2\u021dQ\3\2\2\2\u021e")
        buf.write("\u021f\7\17\2\2\u021f\u0220\7\62\2\2\u0220\u0221\5h\65")
        buf.write("\2\u0221S\3\2\2\2\u0222\u0223\7\t\2\2\u0223\u0224\7\62")
        buf.write("\2\2\u0224\u0229\5V,\2\u0225\u0226\79\2\2\u0226\u0228")
        buf.write("\5V,\2\u0227\u0225\3\2\2\2\u0228\u022b\3\2\2\2\u0229\u0227")
        buf.write("\3\2\2\2\u0229\u022a\3\2\2\2\u022aU\3\2\2\2\u022b\u0229")
        buf.write("\3\2\2\2\u022c\u022e\5X-\2\u022d\u022f\5Z.\2\u022e\u022d")
        buf.write("\3\2\2\2\u022e\u022f\3\2\2\2\u022f\u0230\3\2\2\2\u0230")
        buf.write("\u0231\7\64\2\2\u0231\u0232\5h\65\2\u0232\u0233\7\65\2")
        buf.write("\2\u0233W\3\2\2\2\u0234\u0235\5\u0086D\2\u0235Y\3\2\2")
        buf.write("\2\u0236\u0237\t\3\2\2\u0237[\3\2\2\2\u0238\u0239\7\n")
        buf.write("\2\2\u0239\u023a\7\62\2\2\u023a\u023e\5h\65\2\u023b\u023d")
        buf.write("\7+\2\2\u023c\u023b\3\2\2\2\u023d\u0240\3\2\2\2\u023e")
        buf.write("\u023c\3\2\2\2\u023e\u023f\3\2\2\2\u023f]\3\2\2\2\u0240")
        buf.write("\u023e\3\2\2\2\u0241\u0242\7\13\2\2\u0242\u0243\7\62\2")
        buf.write("\2\u0243\u0247\5h\65\2\u0244\u0246\7+\2\2\u0245\u0244")
        buf.write("\3\2\2\2\u0246\u0249\3\2\2\2\u0247\u0245\3\2\2\2\u0247")
        buf.write("\u0248\3\2\2\2\u0248_\3\2\2\2\u0249\u0247\3\2\2\2\u024a")
        buf.write("\u024b\7\f\2\2\u024b\u024c\7\62\2\2\u024c\u0250\5h\65")
        buf.write("\2\u024d\u024f\7+\2\2\u024e\u024d\3\2\2\2\u024f\u0252")
        buf.write("\3\2\2\2\u0250\u024e\3\2\2\2\u0250\u0251\3\2\2\2\u0251")
        buf.write("a\3\2\2\2\u0252\u0250\3\2\2\2\u0253\u0254\7\r\2\2\u0254")
        buf.write("\u0255\7\62\2\2\u0255\u0259\5h\65\2\u0256\u0258\7+\2\2")
        buf.write("\u0257\u0256\3\2\2\2\u0258\u025b\3\2\2\2\u0259\u0257\3")
        buf.write("\2\2\2\u0259\u025a\3\2\2\2\u025ac\3\2\2\2\u025b\u0259")
        buf.write("\3\2\2\2\u025c\u025d\7\16\2\2\u025d\u025e\7\62\2\2\u025e")
        buf.write("\u0262\5h\65\2\u025f\u0261\7+\2\2\u0260\u025f\3\2\2\2")
        buf.write("\u0261\u0264\3\2\2\2\u0262\u0260\3\2\2\2\u0262\u0263\3")
        buf.write("\2\2\2\u0263e\3\2\2\2\u0264\u0262\3\2\2\2\u0265\u0266")
        buf.write("\7\17\2\2\u0266\u0267\7\62\2\2\u0267\u026b\5h\65\2\u0268")
        buf.write("\u026a\7+\2\2\u0269\u0268\3\2\2\2\u026a\u026d\3\2\2\2")
        buf.write("\u026b\u0269\3\2\2\2\u026b\u026c\3\2\2\2\u026cg\3\2\2")
        buf.write("\2\u026d\u026b\3\2\2\2\u026e\u0270\7:\2\2\u026f\u026e")
        buf.write("\3\2\2\2\u026f\u0270\3\2\2\2\u0270\u0271\3\2\2\2\u0271")
        buf.write("\u0277\7N\2\2\u0272\u0273\79\2\2\u0273\u0274\7\63\2\2")
        buf.write("\u0274\u0276\5j\66\2\u0275\u0272\3\2\2\2\u0276\u0279\3")
        buf.write("\2\2\2\u0277\u0275\3\2\2\2\u0277\u0278\3\2\2\2\u0278\u0286")
        buf.write("\3\2\2\2\u0279\u0277\3\2\2\2\u027a\u0282\5\u0086D\2\u027b")
        buf.write("\u027d\79\2\2\u027c\u027e\7\63\2\2\u027d\u027c\3\2\2\2")
        buf.write("\u027d\u027e\3\2\2\2\u027e\u027f\3\2\2\2\u027f\u0281\5")
        buf.write("j\66\2\u0280\u027b\3\2\2\2\u0281\u0284\3\2\2\2\u0282\u0280")
        buf.write("\3\2\2\2\u0282\u0283\3\2\2\2\u0283\u0286\3\2\2\2\u0284")
        buf.write("\u0282\3\2\2\2\u0285\u026f\3\2\2\2\u0285\u027a\3\2\2\2")
        buf.write("\u0286i\3\2\2\2\u0287\u0289\7N\2\2\u0288\u0287\3\2\2\2")
        buf.write("\u0288\u0289\3\2\2\2\u0289\u028a\3\2\2\2\u028a\u028c\5")
        buf.write("\u0086D\2\u028b\u028d\7N\2\2\u028c\u028b\3\2\2\2\u028c")
        buf.write("\u028d\3\2\2\2\u028dk\3\2\2\2\u028e\u0290\7A\2\2\u028f")
        buf.write("\u0291\5n8\2\u0290\u028f\3\2\2\2\u0290\u0291\3\2\2\2\u0291")
        buf.write("\u0293\3\2\2\2\u0292\u0294\5p9\2\u0293\u0292\3\2\2\2\u0293")
        buf.write("\u0294\3\2\2\2\u0294\u0298\3\2\2\2\u0295\u0297\7+\2\2")
        buf.write("\u0296\u0295\3\2\2\2\u0297\u029a\3\2\2\2\u0298\u0296\3")
        buf.write("\2\2\2\u0298\u0299\3\2\2\2\u0299m\3\2\2\2\u029a\u0298")
        buf.write("\3\2\2\2\u029b\u029c\7:\2\2\u029c\u029d\5\u0086D\2\u029d")
        buf.write("o\3\2\2\2\u029e\u029f\5\n\6\2\u029fq\3\2\2\2\u02a0\u02a2")
        buf.write("\5\u0082B\2\u02a1\u02a0\3\2\2\2\u02a1\u02a2\3\2\2\2\u02a2")
        buf.write("\u02ac\3\2\2\2\u02a3\u02a6\5t;\2\u02a4\u02a6\5~@\2\u02a5")
        buf.write("\u02a3\3\2\2\2\u02a5\u02a4\3\2\2\2\u02a6\u02a8\3\2\2\2")
        buf.write("\u02a7\u02a9\5\u0082B\2\u02a8\u02a7\3\2\2\2\u02a8\u02a9")
        buf.write("\3\2\2\2\u02a9\u02ab\3\2\2\2\u02aa\u02a5\3\2\2\2\u02ab")
        buf.write("\u02ae\3\2\2\2\u02ac\u02aa\3\2\2\2\u02ac\u02ad\3\2\2\2")
        buf.write("\u02ads\3\2\2\2\u02ae\u02ac\3\2\2\2\u02af\u02b0\7S\2\2")
        buf.write("\u02b0\u02b4\5v<\2\u02b1\u02b3\5\u0080A\2\u02b2\u02b1")
        buf.write("\3\2\2\2\u02b3\u02b6\3\2\2\2\u02b4\u02b2\3\2\2\2\u02b4")
        buf.write("\u02b5\3\2\2\2\u02b5\u02b7\3\2\2\2\u02b6\u02b4\3\2\2\2")
        buf.write("\u02b7\u02b8\7^\2\2\u02b8\u02b9\5r:\2\u02b9\u02ba\7S\2")
        buf.write("\2\u02ba\u02bb\7a\2\2\u02bb\u02bc\5x=\2\u02bc\u02bd\7")
        buf.write("^\2\2\u02bd\u02c9\3\2\2\2\u02be\u02bf\7S\2\2\u02bf\u02c3")
        buf.write("\5v<\2\u02c0\u02c2\5\u0080A\2\u02c1\u02c0\3\2\2\2\u02c2")
        buf.write("\u02c5\3\2\2\2\u02c3\u02c1\3\2\2\2\u02c3\u02c4\3\2\2\2")
        buf.write("\u02c4\u02c6\3\2\2\2\u02c5\u02c3\3\2\2\2\u02c6\u02c7\7")
        buf.write("`\2\2\u02c7\u02c9\3\2\2\2\u02c8\u02af\3\2\2\2\u02c8\u02be")
        buf.write("\3\2\2\2\u02c9u\3\2\2\2\u02ca\u02cd\5|?\2\u02cb\u02cd")
        buf.write("\5z>\2\u02cc\u02ca\3\2\2\2\u02cc\u02cb\3\2\2\2\u02cdw")
        buf.write("\3\2\2\2\u02ce\u02d1\5|?\2\u02cf\u02d1\5z>\2\u02d0\u02ce")
        buf.write("\3\2\2\2\u02d0\u02cf\3\2\2\2\u02d1y\3\2\2\2\u02d2\u02d3")
        buf.write("\7f\2\2\u02d3{\3\2\2\2\u02d4\u02d5\7e\2\2\u02d5}\3\2\2")
        buf.write("\2\u02d6\u02d7\t\7\2\2\u02d7\177\3\2\2\2\u02d8\u02d9\7")
        buf.write("f\2\2\u02d9\u02da\7b\2\2\u02da\u02db\t\b\2\2\u02db\u0081")
        buf.write("\3\2\2\2\u02dc\u02dd\t\t\2\2\u02dd\u0083\3\2\2\2\u02de")
        buf.write("\u02df\t\n\2\2\u02df\u0085\3\2\2\2\u02e0\u02e1\t\13\2")
        buf.write("\2\u02e1\u0087\3\2\2\2\u02e2\u02f8\5\u008aF\2\u02e3\u02f8")
        buf.write("\5\u008eH\2\u02e4\u02f8\5\u008cG\2\u02e5\u02f8\5\u0090")
        buf.write("I\2\u02e6\u02f8\5\u0092J\2\u02e7\u02f8\5\u0094K\2\u02e8")
        buf.write("\u02f8\5\u0096L\2\u02e9\u02f8\5\u0098M\2\u02ea\u02f8\5")
        buf.write("\u009aN\2\u02eb\u02f8\5\u00a8U\2\u02ec\u02f8\5\u00b4[")
        buf.write("\2\u02ed\u02f8\5\u00be`\2\u02ee\u02f8\5\u00c4c\2\u02ef")
        buf.write("\u02f8\5\u00d8m\2\u02f0\u02f8\5\u009cO\2\u02f1\u02f8\5")
        buf.write("\u00c8e\2\u02f2\u02f8\5\u009eP\2\u02f3\u02f8\5\u00a0Q")
        buf.write("\2\u02f4\u02f8\5\u00a2R\2\u02f5\u02f8\5\u00a4S\2\u02f6")
        buf.write("\u02f8\5\u00a6T\2\u02f7\u02e2\3\2\2\2\u02f7\u02e3\3\2")
        buf.write("\2\2\u02f7\u02e4\3\2\2\2\u02f7\u02e5\3\2\2\2\u02f7\u02e6")
        buf.write("\3\2\2\2\u02f7\u02e7\3\2\2\2\u02f7\u02e8\3\2\2\2\u02f7")
        buf.write("\u02e9\3\2\2\2\u02f7\u02ea\3\2\2\2\u02f7\u02eb\3\2\2\2")
        buf.write("\u02f7\u02ec\3\2\2\2\u02f7\u02ed\3\2\2\2\u02f7\u02ee\3")
        buf.write("\2\2\2\u02f7\u02ef\3\2\2\2\u02f7\u02f0\3\2\2\2\u02f7\u02f1")
        buf.write("\3\2\2\2\u02f7\u02f2\3\2\2\2\u02f7\u02f3\3\2\2\2\u02f7")
        buf.write("\u02f4\3\2\2\2\u02f7\u02f5\3\2\2\2\u02f7\u02f6\3\2\2\2")
        buf.write("\u02f8\u0089\3\2\2\2\u02f9\u02fa\7\22\2\2\u02fa\u008b")
        buf.write("\3\2\2\2\u02fb\u02fc\7\23\2\2\u02fc\u008d\3\2\2\2\u02fd")
        buf.write("\u02fe\7\24\2\2\u02fe\u008f\3\2\2\2\u02ff\u0300\7\25\2")
        buf.write("\2\u0300\u0091\3\2\2\2\u0301\u0302\7\26\2\2\u0302\u0093")
        buf.write("\3\2\2\2\u0303\u0304\7\27\2\2\u0304\u0095\3\2\2\2\u0305")
        buf.write("\u0306\7\30\2\2\u0306\u0097\3\2\2\2\u0307\u0308\7\31\2")
        buf.write("\2\u0308\u0099\3\2\2\2\u0309\u030a\7\32\2\2\u030a\u009b")
        buf.write("\3\2\2\2\u030b\u030c\7\33\2\2\u030c\u009d\3\2\2\2\u030d")
        buf.write("\u030e\7\35\2\2\u030e\u009f\3\2\2\2\u030f\u0310\7\36\2")
        buf.write("\2\u0310\u00a1\3\2\2\2\u0311\u0312\7\37\2\2\u0312\u00a3")
        buf.write("\3\2\2\2\u0313\u0314\7 \2\2\u0314\u00a5\3\2\2\2\u0315")
        buf.write("\u0316\7!\2\2\u0316\u00a7\3\2\2\2\u0317\u0320\7#\2\2\u0318")
        buf.write("\u0319\7\64\2\2\u0319\u031c\5\u00aaV\2\u031a\u031b\79")
        buf.write("\2\2\u031b\u031d\5\u00acW\2\u031c\u031a\3\2\2\2\u031c")
        buf.write("\u031d\3\2\2\2\u031d\u031e\3\2\2\2\u031e\u031f\7\65\2")
        buf.write("\2\u031f\u0321\3\2\2\2\u0320\u0318\3\2\2\2\u0320\u0321")
        buf.write("\3\2\2\2\u0321\u00a9\3\2\2\2\u0322\u0323\t\f\2\2\u0323")
        buf.write("\u00ab\3\2\2\2\u0324\u0325\7*\2\2\u0325\u0326\7J\2\2\u0326")
        buf.write("\u032b\5\u00aeX\2\u0327\u0328\79\2\2\u0328\u032a\5\u00ae")
        buf.write("X\2\u0329\u0327\3\2\2\2\u032a\u032d\3\2\2\2\u032b\u0329")
        buf.write("\3\2\2\2\u032b\u032c\3\2\2\2\u032c\u00ad\3\2\2\2\u032d")
        buf.write("\u032b\3\2\2\2\u032e\u0330\5\u00b2Z\2\u032f\u032e\3\2")
        buf.write("\2\2\u032f\u0330\3\2\2\2\u0330\u0331\3\2\2\2\u0331\u0332")
        buf.write("\5\u00b0Y\2\u0332\u00af\3\2\2\2\u0333\u0334\t\r\2\2\u0334")
        buf.write("\u00b1\3\2\2\2\u0335\u0336\7-\2\2\u0336\u0337\7\62\2\2")
        buf.write("\u0337\u00b3\3\2\2\2\u0338\u033d\7$\2\2\u0339\u033a\7")
        buf.write("\64\2\2\u033a\u033b\5\u00b6\\\2\u033b\u033c\7\65\2\2\u033c")
        buf.write("\u033e\3\2\2\2\u033d\u0339\3\2\2\2\u033d\u033e\3\2\2\2")
        buf.write("\u033e\u00b5\3\2\2\2\u033f\u0340\7*\2\2\u0340\u0341\7")
        buf.write("J\2\2\u0341\u0346\5\u00b8]\2\u0342\u0343\79\2\2\u0343")
        buf.write("\u0345\5\u00b8]\2\u0344\u0342\3\2\2\2\u0345\u0348\3\2")
        buf.write("\2\2\u0346\u0344\3\2\2\2\u0346\u0347\3\2\2\2\u0347\u00b7")
        buf.write("\3\2\2\2\u0348\u0346\3\2\2\2\u0349\u034b\5\u00bc_\2\u034a")
        buf.write("\u0349\3\2\2\2\u034a\u034b\3\2\2\2\u034b\u034c\3\2\2\2")
        buf.write("\u034c\u034d\5\u00ba^\2\u034d\u00b9\3\2\2\2\u034e\u034f")
        buf.write("\t\r\2\2\u034f\u00bb\3\2\2\2\u0350\u0351\7.\2\2\u0351")
        buf.write("\u0352\7\62\2\2\u0352\u00bd\3\2\2\2\u0353\u0354\7%\2\2")
        buf.write("\u0354\u0355\7\64\2\2\u0355\u0356\5\u00c0a\2\u0356\u0357")
        buf.write("\7\65\2\2\u0357\u00bf\3\2\2\2\u0358\u035d\5\u00c2b\2\u0359")
        buf.write("\u035a\79\2\2\u035a\u035c\5\u00c2b\2\u035b\u0359\3\2\2")
        buf.write("\2\u035c\u035f\3\2\2\2\u035d\u035b\3\2\2\2\u035d\u035e")
        buf.write("\3\2\2\2\u035e\u00c1\3\2\2\2\u035f\u035d\3\2\2\2\u0360")
        buf.write("\u0361\7-\2\2\u0361\u00c3\3\2\2\2\u0362\u0367\7&\2\2\u0363")
        buf.write("\u0364\7\64\2\2\u0364\u0365\5\u00c6d\2\u0365\u0366\7\65")
        buf.write("\2\2\u0366\u0368\3\2\2\2\u0367\u0363\3\2\2\2\u0367\u0368")
        buf.write("\3\2\2\2\u0368\u00c5\3\2\2\2\u0369\u036a\7\4\2\2\u036a")
        buf.write("\u00c7\3\2\2\2\u036b\u0370\5\u00caf\2\u036c\u036d\7\64")
        buf.write("\2\2\u036d\u036e\5\u00ccg\2\u036e\u036f\7\65\2\2\u036f")
        buf.write("\u0371\3\2\2\2\u0370\u036c\3\2\2\2\u0370\u0371\3\2\2\2")
        buf.write("\u0371\u00c9\3\2\2\2\u0372\u0373\t\16\2\2\u0373\u00cb")
        buf.write("\3\2\2\2\u0374\u0379\5\u00ceh\2\u0375\u0376\79\2\2\u0376")
        buf.write("\u0378\5\u00ceh\2\u0377\u0375\3\2\2\2\u0378\u037b\3\2")
        buf.write("\2\2\u0379\u0377\3\2\2\2\u0379\u037a\3\2\2\2\u037a\u00cd")
        buf.write("\3\2\2\2\u037b\u0379\3\2\2\2\u037c\u037d\5\u00d2j\2\u037d")
        buf.write("\u037e\5\u00d0i\2\u037e\u037f\5\u00d4k\2\u037f\u00cf\3")
        buf.write("\2\2\2\u0380\u0381\7\60\2\2\u0381\u00d1\3\2\2\2\u0382")
        buf.write("\u0383\7-\2\2\u0383\u0384\7J\2\2\u0384\u00d3\3\2\2\2\u0385")
        buf.write("\u0387\5\u00d6l\2\u0386\u0385\3\2\2\2\u0387\u038a\3\2")
        buf.write("\2\2\u0388\u0386\3\2\2\2\u0388\u0389\3\2\2\2\u0389\u00d5")
        buf.write("\3\2\2\2\u038a\u0388\3\2\2\2\u038b\u038c\7\61\2\2\u038c")
        buf.write("\u00d7\3\2\2\2\u038d\u038e\5\u00dan\2\u038e\u0391\7\64")
        buf.write("\2\2\u038f\u0392\5\u00dco\2\u0390\u0392\5\u00dep\2\u0391")
        buf.write("\u038f\3\2\2\2\u0391\u0390\3\2\2\2\u0392\u0394\3\2\2\2")
        buf.write("\u0393\u0395\5\u00e0q\2\u0394\u0393\3\2\2\2\u0394\u0395")
        buf.write("\3\2\2\2\u0395\u0396\3\2\2\2\u0396\u0397\7\65\2\2\u0397")
        buf.write("\u00d9\3\2\2\2\u0398\u0399\t\17\2\2\u0399\u00db\3\2\2")
        buf.write("\2\u039a\u039b\7@\2\2\u039b\u039c\7-\2\2\u039c\u00dd\3")
        buf.write("\2\2\2\u039d\u039e\7/\2\2\u039e\u00df\3\2\2\2\u039f\u03a0")
        buf.write("\7>\2\2\u03a0\u03a1\7-\2\2\u03a1\u00e1\3\2\2\2]\u00e3")
        buf.write("\u00e8\u00ee\u00f4\u00f8\u00fd\u0103\u0114\u011b\u011f")
        buf.write("\u0123\u0127\u0129\u0130\u0136\u013a\u013f\u0143\u0148")
        buf.write("\u0159\u0165\u0168\u0170\u0175\u017b\u0183\u0186\u018a")
        buf.write("\u018e\u0197\u019c\u01a6\u01ad\u01b0\u01b3\u01b8\u01bb")
        buf.write("\u01c7\u01cb\u01e4\u01e6\u01ea\u01ef\u01f3\u01f8\u0202")
        buf.write("\u020c\u020e\u0212\u0229\u022e\u023e\u0247\u0250\u0259")
        buf.write("\u0262\u026b\u026f\u0277\u027d\u0282\u0285\u0288\u028c")
        buf.write("\u0290\u0293\u0298\u02a1\u02a5\u02a8\u02ac\u02b4\u02c3")
        buf.write("\u02c8\u02cc\u02d0\u02f7\u031c\u0320\u032b\u032f\u033d")
        buf.write("\u0346\u034a\u035d\u0367\u0370\u0379\u0388\u0391\u0394")
        return buf.getvalue()


class ZmeiLangParser ( Parser ):

    grammarFileName = "ZmeiLangParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'@admin'", "<INVALID>", "<INVALID>", 
                     "'inline'", "'type'", "'extra'", "'tabs'", "'list'", 
                     "'read_only'", "'list_editable'", "'list_filter'", 
                     "'list_search'", "'fields'", "'import'", "'as'", "'text'", 
                     "'html'", "'html_media'", "'float'", "'decimal'", "'date'", 
                     "'datetime'", "'create_time'", "'update_time'", "'image_file'", 
                     "'image'", "'filer_image'", "'filer_file'", "'file'", 
                     "'simple_file'", "'folder'", "'image_folder'", "'str'", 
                     "'int'", "'slug'", "'bool'", "'one'", "'one2one'", 
                     "'many'", "'choices'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "':'", "'^'", "'('", "')'", "'['", "']'", "'?'", "','", 
                     "'.'", "<INVALID>", "<INVALID>", "'=>'", "'->'", "'~>'", 
                     "'#'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'$'", "'&'", "'!'", "'*'", 
                     "'~'", "' '", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'}'", "<INVALID>", "<INVALID>", "';'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'?>'", "'/>'" ]

    symbolicNames = [ "<INVALID>", "AN_ADMIN", "BOOL", "KW_INLINE_TYPE", 
                      "KW_INLINE", "KW_TYPE", "KW_EXTRA", "KW_TABS", "KW_LIST", 
                      "KW_READ_ONLY", "KW_LIST_EDITABLE", "KW_LIST_FILTER", 
                      "KW_LIST_SEARCH", "KW_FIELDS", "KW_IMPORT", "KW_AS", 
                      "COL_FIELD_TYPE_LONGTEXT", "COL_FIELD_TYPE_HTML", 
                      "COL_FIELD_TYPE_HTML_MEDIA", "COL_FIELD_TYPE_FLOAT", 
                      "COL_FIELD_TYPE_DECIMAL", "COL_FIELD_TYPE_DATE", "COL_FIELD_TYPE_DATETIME", 
                      "COL_FIELD_TYPE_CREATE_TIME", "COL_FIELD_TYPE_UPDATE_TIME", 
                      "COL_FIELD_TYPE_IMAGE_FILE", "COL_FIELD_TYPE_IMAGE", 
                      "COL_FIELD_TYPE_FILER_IMAGE", "COL_FIELD_TYPE_FILER_FILE", 
                      "COL_FIELD_TYPE_FILE", "COL_FIELD_TYPE_SIMPLE_FILE", 
                      "COL_FIELD_TYPE_FOLDER", "COL_FIELD_TYPE_IMAGE_FOLDER", 
                      "COL_FIELD_TYPE_TEXT", "COL_FIELD_TYPE_INT", "COL_FIELD_TYPE_SLUG", 
                      "COL_FIELD_TYPE_BOOL", "COL_FIELD_TYPE_ONE", "COL_FIELD_TYPE_ONE2ONE", 
                      "COL_FIELD_TYPE_MANY", "COL_FIELD_CHOICES", "NL", 
                      "INLINE_CODE_BLOCK", "ID", "DIGIT", "CLASSNAME", "SIZE2D", 
                      "FILTER", "COLON", "EXCLUDE", "BRACE_OPEN", "BRACE_CLOSE", 
                      "SQ_BRACE_OPEN", "SQ_BRACE_CLOSE", "QUESTION_MARK", 
                      "COMA", "DOT", "STRING_DQ", "STRING_SQ", "FIELD_VNAME", 
                      "RELATED", "RELATED_EXTEND", "REF_SIGN", "ANNOTATION", 
                      "LINE_SEPARATOR", "URL_SEGMENTS", "TEMPLATE_NAME", 
                      "ASSIGN", "ASSIGN_STATIC", "COMMENT_LINE", "COMMENT_BLOCK", 
                      "SLASH", "EQUALS", "DOLLAR", "AMP", "EXCLAM", "STAR", 
                      "APPROX", "WS", "COL_FIELD_CALCULATED", "CODE_BLOCK_START", 
                      "XML_OPEN", "CODE_BLOCK_LINE", "CODE_BLOCK_END", "PYTHON_LINE_CODE", 
                      "PYTHON_LINE_ERRCHAR", "PYTHON_LINE_END", "PYTHON_EXPR_ERRCHAR", 
                      "XML_EntityRef", "XML_CharRef", "XML_TEXT", "XML_ERRCHAR", 
                      "XML_CLOSE", "XML_SPECIAL_CLOSE", "XML_SLASH_CLOSE", 
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
    RULE_model_annotation = 33
    RULE_an_admin = 34
    RULE_an_admin_inlines = 35
    RULE_an_admin_inline = 36
    RULE_inline_name = 37
    RULE_inline_type = 38
    RULE_inline_extra = 39
    RULE_inline_fields = 40
    RULE_an_admin_tabs = 41
    RULE_an_admin_tab = 42
    RULE_tab_name = 43
    RULE_tab_verbose_name = 44
    RULE_an_admin_list = 45
    RULE_an_admin_read_only = 46
    RULE_an_admin_list_editable = 47
    RULE_an_admin_list_filter = 48
    RULE_an_admin_list_search = 49
    RULE_an_admin_fields = 50
    RULE_field_list_expr = 51
    RULE_field_list_expr_field = 52
    RULE_annotation = 53
    RULE_annotation_descr = 54
    RULE_annotation_code = 55
    RULE_xml_content = 56
    RULE_xml_element = 57
    RULE_xml_name = 58
    RULE_xml_name_end = 59
    RULE_xml_tag_name = 60
    RULE_xml_component_name = 61
    RULE_xml_reference = 62
    RULE_xml_attribute = 63
    RULE_xml_chardata = 64
    RULE_xml_misc = 65
    RULE_id_or_kw = 66
    RULE_col_field_def = 67
    RULE_field_longtext = 68
    RULE_field_html = 69
    RULE_field_html_media = 70
    RULE_field_float = 71
    RULE_field_decimal = 72
    RULE_field_date = 73
    RULE_field_datetime = 74
    RULE_field_create_time = 75
    RULE_field_update_time = 76
    RULE_field_image_file = 77
    RULE_field_filer_image = 78
    RULE_field_filer_file = 79
    RULE_field_file = 80
    RULE_field_simple_file = 81
    RULE_field_folder = 82
    RULE_field_text = 83
    RULE_field_text_size = 84
    RULE_field_text_choices = 85
    RULE_field_text_choice = 86
    RULE_field_text_choice_val = 87
    RULE_field_text_choice_key = 88
    RULE_field_int = 89
    RULE_field_int_choices = 90
    RULE_field_int_choice = 91
    RULE_field_int_choice_val = 92
    RULE_field_int_choice_key = 93
    RULE_field_slug = 94
    RULE_field_slug_ref_field = 95
    RULE_field_slug_ref_field_id = 96
    RULE_field_bool = 97
    RULE_field_bool_default = 98
    RULE_field_image = 99
    RULE_filer_image_type = 100
    RULE_field_image_sizes = 101
    RULE_field_image_size = 102
    RULE_field_image_size_dimensions = 103
    RULE_field_image_size_name = 104
    RULE_field_image_filters = 105
    RULE_field_image_filter = 106
    RULE_field_relation = 107
    RULE_field_relation_type = 108
    RULE_field_relation_target_ref = 109
    RULE_field_relation_target_class = 110
    RULE_field_relation_related_name = 111

    ruleNames =  [ "col_file", "page_imports", "model_imports", "import_source", 
                   "code_block", "page", "page_base", "page_alias", "page_alias_name", 
                   "page_element", "page_template", "page_url", "page_code", 
                   "page_name", "page_field", "page_field_name", "page_field_code", 
                   "col", "col_str_expr", "col_header", "col_verbose_name", 
                   "verbose_name_part", "col_base_name", "col_name", "col_field", 
                   "col_field_expr", "col_field_expr_marker", "col_feild_expr_code", 
                   "string_or_quoted", "col_field_help_text", "col_field_vrebose_name", 
                   "col_field_name", "col_modifier", "model_annotation", 
                   "an_admin", "an_admin_inlines", "an_admin_inline", "inline_name", 
                   "inline_type", "inline_extra", "inline_fields", "an_admin_tabs", 
                   "an_admin_tab", "tab_name", "tab_verbose_name", "an_admin_list", 
                   "an_admin_read_only", "an_admin_list_editable", "an_admin_list_filter", 
                   "an_admin_list_search", "an_admin_fields", "field_list_expr", 
                   "field_list_expr_field", "annotation", "annotation_descr", 
                   "annotation_code", "xml_content", "xml_element", "xml_name", 
                   "xml_name_end", "xml_tag_name", "xml_component_name", 
                   "xml_reference", "xml_attribute", "xml_chardata", "xml_misc", 
                   "id_or_kw", "col_field_def", "field_longtext", "field_html", 
                   "field_html_media", "field_float", "field_decimal", "field_date", 
                   "field_datetime", "field_create_time", "field_update_time", 
                   "field_image_file", "field_filer_image", "field_filer_file", 
                   "field_file", "field_simple_file", "field_folder", "field_text", 
                   "field_text_size", "field_text_choices", "field_text_choice", 
                   "field_text_choice_val", "field_text_choice_key", "field_int", 
                   "field_int_choices", "field_int_choice", "field_int_choice_val", 
                   "field_int_choice_key", "field_slug", "field_slug_ref_field", 
                   "field_slug_ref_field_id", "field_bool", "field_bool_default", 
                   "field_image", "filer_image_type", "field_image_sizes", 
                   "field_image_size", "field_image_size_dimensions", "field_image_size_name", 
                   "field_image_filters", "field_image_filter", "field_relation", 
                   "field_relation_type", "field_relation_target_ref", "field_relation_target_class", 
                   "field_relation_related_name" ]

    EOF = Token.EOF
    AN_ADMIN=1
    BOOL=2
    KW_INLINE_TYPE=3
    KW_INLINE=4
    KW_TYPE=5
    KW_EXTRA=6
    KW_TABS=7
    KW_LIST=8
    KW_READ_ONLY=9
    KW_LIST_EDITABLE=10
    KW_LIST_FILTER=11
    KW_LIST_SEARCH=12
    KW_FIELDS=13
    KW_IMPORT=14
    KW_AS=15
    COL_FIELD_TYPE_LONGTEXT=16
    COL_FIELD_TYPE_HTML=17
    COL_FIELD_TYPE_HTML_MEDIA=18
    COL_FIELD_TYPE_FLOAT=19
    COL_FIELD_TYPE_DECIMAL=20
    COL_FIELD_TYPE_DATE=21
    COL_FIELD_TYPE_DATETIME=22
    COL_FIELD_TYPE_CREATE_TIME=23
    COL_FIELD_TYPE_UPDATE_TIME=24
    COL_FIELD_TYPE_IMAGE_FILE=25
    COL_FIELD_TYPE_IMAGE=26
    COL_FIELD_TYPE_FILER_IMAGE=27
    COL_FIELD_TYPE_FILER_FILE=28
    COL_FIELD_TYPE_FILE=29
    COL_FIELD_TYPE_SIMPLE_FILE=30
    COL_FIELD_TYPE_FOLDER=31
    COL_FIELD_TYPE_IMAGE_FOLDER=32
    COL_FIELD_TYPE_TEXT=33
    COL_FIELD_TYPE_INT=34
    COL_FIELD_TYPE_SLUG=35
    COL_FIELD_TYPE_BOOL=36
    COL_FIELD_TYPE_ONE=37
    COL_FIELD_TYPE_ONE2ONE=38
    COL_FIELD_TYPE_MANY=39
    COL_FIELD_CHOICES=40
    NL=41
    INLINE_CODE_BLOCK=42
    ID=43
    DIGIT=44
    CLASSNAME=45
    SIZE2D=46
    FILTER=47
    COLON=48
    EXCLUDE=49
    BRACE_OPEN=50
    BRACE_CLOSE=51
    SQ_BRACE_OPEN=52
    SQ_BRACE_CLOSE=53
    QUESTION_MARK=54
    COMA=55
    DOT=56
    STRING_DQ=57
    STRING_SQ=58
    FIELD_VNAME=59
    RELATED=60
    RELATED_EXTEND=61
    REF_SIGN=62
    ANNOTATION=63
    LINE_SEPARATOR=64
    URL_SEGMENTS=65
    TEMPLATE_NAME=66
    ASSIGN=67
    ASSIGN_STATIC=68
    COMMENT_LINE=69
    COMMENT_BLOCK=70
    SLASH=71
    EQUALS=72
    DOLLAR=73
    AMP=74
    EXCLAM=75
    STAR=76
    APPROX=77
    WS=78
    COL_FIELD_CALCULATED=79
    CODE_BLOCK_START=80
    XML_OPEN=81
    CODE_BLOCK_LINE=82
    CODE_BLOCK_END=83
    PYTHON_LINE_CODE=84
    PYTHON_LINE_ERRCHAR=85
    PYTHON_LINE_END=86
    PYTHON_EXPR_ERRCHAR=87
    XML_EntityRef=88
    XML_CharRef=89
    XML_TEXT=90
    XML_ERRCHAR=91
    XML_CLOSE=92
    XML_SPECIAL_CLOSE=93
    XML_SLASH_CLOSE=94
    XML_SLASH=95
    XML_EQUALS=96
    XML_REACT_ATTR=97
    XML_STRING=98
    XML_CmpName=99
    XML_Name=100
    XML_INSIDE_ERRCHAR=101

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
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 224
                self.page_imports()


            self.state = 230
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 227
                    self.match(ZmeiLangParser.NL) 
                self.state = 232
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.ANNOTATION:
                self.state = 233
                self.annotation()
                self.state = 238
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.SQ_BRACE_OPEN:
                self.state = 239
                self.page()
                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.KW_IMPORT:
                self.state = 245
                self.model_imports()


            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.REF_SIGN:
                self.state = 248
                self.col()
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 254
                self.match(ZmeiLangParser.NL)
                self.state = 259
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 260
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
            self.state = 262
            self.match(ZmeiLangParser.KW_IMPORT)
            self.state = 263
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
            self.state = 265
            self.match(ZmeiLangParser.KW_IMPORT)
            self.state = 266
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
            self.state = 268
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
            self.state = 270
            self.match(ZmeiLangParser.CODE_BLOCK_START)
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.CODE_BLOCK_LINE:
                self.state = 271
                self.match(ZmeiLangParser.CODE_BLOCK_LINE)
                self.state = 276
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 277
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
            self.state = 279
            self.match(ZmeiLangParser.SQ_BRACE_OPEN)
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 280
                self.page_base()


            self.state = 283
            self.page_name()
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.KW_AS:
                self.state = 284
                self.page_alias()


            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COLON:
                self.state = 287
                self.match(ZmeiLangParser.COLON)
                self.state = 289
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 2)) & ~0x3f) == 0 and ((1 << (_la - 2)) & ((1 << (ZmeiLangParser.BOOL - 2)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE - 2)) | (1 << (ZmeiLangParser.KW_INLINE - 2)) | (1 << (ZmeiLangParser.KW_TYPE - 2)) | (1 << (ZmeiLangParser.KW_EXTRA - 2)) | (1 << (ZmeiLangParser.KW_TABS - 2)) | (1 << (ZmeiLangParser.KW_LIST - 2)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 2)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 2)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 2)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 2)) | (1 << (ZmeiLangParser.KW_FIELDS - 2)) | (1 << (ZmeiLangParser.KW_IMPORT - 2)) | (1 << (ZmeiLangParser.KW_AS - 2)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 2)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 2)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 2)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 2)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 2)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 2)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 2)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 2)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 2)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE_FILE - 2)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 2)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 2)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 2)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 2)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SIMPLE_FILE - 2)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FOLDER - 2)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE_FOLDER - 2)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 2)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 2)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 2)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 2)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 2)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 2)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 2)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 2)) | (1 << (ZmeiLangParser.ID - 2)) | (1 << (ZmeiLangParser.URL_SEGMENTS - 2)))) != 0):
                    self.state = 288
                    self.page_url()


                self.state = 293
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.COLON:
                    self.state = 291
                    self.match(ZmeiLangParser.COLON)
                    self.state = 292
                    self.page_template()




            self.state = 297
            self.match(ZmeiLangParser.SQ_BRACE_CLOSE)
            self.state = 298
            self.match(ZmeiLangParser.NL)
            self.state = 302
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 299
                    self.page_field() 
                self.state = 304
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

            self.state = 308
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 305
                    self.annotation() 
                self.state = 310
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK_START:
                self.state = 311
                self.page_code()


            self.state = 317
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.ANNOTATION:
                self.state = 314
                self.annotation()
                self.state = 319
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.XML_OPEN:
                self.state = 320
                self.page_element()


            self.state = 326
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 323
                    self.match(ZmeiLangParser.NL) 
                self.state = 328
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

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


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
            self.state = 329
            self.id_or_kw()
            self.state = 330
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
            self.state = 332
            self.match(ZmeiLangParser.KW_AS)
            self.state = 333
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

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


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
            self.state = 335
            self.id_or_kw()
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
            self.state = 337
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
            self.state = 339
            _la = self._input.LA(1)
            if not(((((_la - 42)) & ~0x3f) == 0 and ((1 << (_la - 42)) & ((1 << (ZmeiLangParser.INLINE_CODE_BLOCK - 42)) | (1 << (ZmeiLangParser.CLASSNAME - 42)) | (1 << (ZmeiLangParser.TEMPLATE_NAME - 42)))) != 0)):
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

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.BOOL, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE_FILE, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_SIMPLE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                self.state = 341
                self.id_or_kw()
                pass
            elif token in [ZmeiLangParser.URL_SEGMENTS]:
                self.state = 342
                self.match(ZmeiLangParser.URL_SEGMENTS)
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
            self.state = 345
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

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


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
            self.state = 347
            self.id_or_kw()
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
            self.state = 349
            self.page_field_name()
            self.state = 350
            self.match(ZmeiLangParser.ASSIGN)
            self.state = 351
            self.page_field_code()
            self.state = 358
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.NL]:
                self.state = 353 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 352
                        self.match(ZmeiLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 355 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

                pass
            elif token in [ZmeiLangParser.EOF]:
                self.state = 357
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

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


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
            self.state = 360
            self.id_or_kw()
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
            self.state = 362
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


        def model_annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Model_annotationContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Model_annotationContext,i)


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
            self.state = 364
            self.col_header()
            self.state = 366
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 365
                self.col_str_expr()


            self.state = 371
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.BOOL) | (1 << ZmeiLangParser.KW_INLINE_TYPE) | (1 << ZmeiLangParser.KW_INLINE) | (1 << ZmeiLangParser.KW_TYPE) | (1 << ZmeiLangParser.KW_EXTRA) | (1 << ZmeiLangParser.KW_TABS) | (1 << ZmeiLangParser.KW_LIST) | (1 << ZmeiLangParser.KW_READ_ONLY) | (1 << ZmeiLangParser.KW_LIST_EDITABLE) | (1 << ZmeiLangParser.KW_LIST_FILTER) | (1 << ZmeiLangParser.KW_LIST_SEARCH) | (1 << ZmeiLangParser.KW_FIELDS) | (1 << ZmeiLangParser.KW_IMPORT) | (1 << ZmeiLangParser.KW_AS) | (1 << ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FLOAT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DECIMAL) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATETIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_IMAGE_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_SIMPLE_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_IMAGE_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_TEXT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_INT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_SLUG) | (1 << ZmeiLangParser.COL_FIELD_TYPE_BOOL) | (1 << ZmeiLangParser.COL_FIELD_TYPE_ONE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_MANY) | (1 << ZmeiLangParser.COL_FIELD_CHOICES) | (1 << ZmeiLangParser.ID))) != 0) or ((((_la - 72)) & ~0x3f) == 0 and ((1 << (_la - 72)) & ((1 << (ZmeiLangParser.EQUALS - 72)) | (1 << (ZmeiLangParser.DOLLAR - 72)) | (1 << (ZmeiLangParser.AMP - 72)) | (1 << (ZmeiLangParser.EXCLAM - 72)) | (1 << (ZmeiLangParser.STAR - 72)) | (1 << (ZmeiLangParser.APPROX - 72)))) != 0):
                self.state = 368
                self.col_field()
                self.state = 373
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 377
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.AN_ADMIN:
                self.state = 374
                self.model_annotation()
                self.state = 379
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
            self.state = 380
            self.match(ZmeiLangParser.EQUALS)
            self.state = 381
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.STRING_DQ or _la==ZmeiLangParser.STRING_SQ):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 388
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.NL]:
                self.state = 383 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 382
                        self.match(ZmeiLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 385 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

                pass
            elif token in [ZmeiLangParser.EOF]:
                self.state = 387
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
            self.state = 390
            self.match(ZmeiLangParser.REF_SIGN)
            self.state = 392
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 391
                self.col_base_name()


            self.state = 394
            self.col_name()
            self.state = 396
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COLON:
                self.state = 395
                self.col_verbose_name()


            self.state = 398
            self.match(ZmeiLangParser.LINE_SEPARATOR)
            self.state = 399
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
            self.state = 401
            self.match(ZmeiLangParser.COLON)
            self.state = 402
            self.verbose_name_part()
            self.state = 405
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.SLASH:
                self.state = 403
                self.match(ZmeiLangParser.SLASH)
                self.state = 404
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

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.BOOL, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE_FILE, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_SIMPLE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                self.state = 407
                self.id_or_kw()
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

    class Col_base_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


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
            self.state = 412
            self.id_or_kw()
            self.state = 413
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

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


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
            self.state = 415
            self.id_or_kw()
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
            self.state = 420
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 72)) & ~0x3f) == 0 and ((1 << (_la - 72)) & ((1 << (ZmeiLangParser.EQUALS - 72)) | (1 << (ZmeiLangParser.DOLLAR - 72)) | (1 << (ZmeiLangParser.AMP - 72)) | (1 << (ZmeiLangParser.EXCLAM - 72)) | (1 << (ZmeiLangParser.STAR - 72)) | (1 << (ZmeiLangParser.APPROX - 72)))) != 0):
                self.state = 417
                self.col_modifier()
                self.state = 422
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 423
            self.col_field_name()
            self.state = 427
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.COLON]:
                self.state = 424
                self.match(ZmeiLangParser.COLON)
                self.state = 425
                self.col_field_def()
                pass
            elif token in [ZmeiLangParser.ASSIGN, ZmeiLangParser.ASSIGN_STATIC]:
                self.state = 426
                self.col_field_expr()
                pass
            elif token in [ZmeiLangParser.EOF, ZmeiLangParser.NL, ZmeiLangParser.QUESTION_MARK, ZmeiLangParser.SLASH]:
                pass
            else:
                pass
            self.state = 430
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.SLASH:
                self.state = 429
                self.col_field_vrebose_name()


            self.state = 433
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.QUESTION_MARK:
                self.state = 432
                self.col_field_help_text()


            self.state = 441
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.NL]:
                self.state = 436 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 435
                        self.match(ZmeiLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 438 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

                pass
            elif token in [ZmeiLangParser.EOF]:
                self.state = 440
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
            self.state = 443
            self.col_field_expr_marker()
            self.state = 444
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
            self.state = 446
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
            self.state = 448
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

        def id_or_kw(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Id_or_kwContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,i)


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
            self.state = 457
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.BOOL, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE_FILE, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_SIMPLE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                self.state = 451 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 450
                    self.id_or_kw()
                    self.state = 453 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.BOOL) | (1 << ZmeiLangParser.KW_INLINE_TYPE) | (1 << ZmeiLangParser.KW_INLINE) | (1 << ZmeiLangParser.KW_TYPE) | (1 << ZmeiLangParser.KW_EXTRA) | (1 << ZmeiLangParser.KW_TABS) | (1 << ZmeiLangParser.KW_LIST) | (1 << ZmeiLangParser.KW_READ_ONLY) | (1 << ZmeiLangParser.KW_LIST_EDITABLE) | (1 << ZmeiLangParser.KW_LIST_FILTER) | (1 << ZmeiLangParser.KW_LIST_SEARCH) | (1 << ZmeiLangParser.KW_FIELDS) | (1 << ZmeiLangParser.KW_IMPORT) | (1 << ZmeiLangParser.KW_AS) | (1 << ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FLOAT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DECIMAL) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATETIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_IMAGE_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_SIMPLE_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_IMAGE_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_TEXT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_INT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_SLUG) | (1 << ZmeiLangParser.COL_FIELD_TYPE_BOOL) | (1 << ZmeiLangParser.COL_FIELD_TYPE_ONE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_MANY) | (1 << ZmeiLangParser.COL_FIELD_CHOICES) | (1 << ZmeiLangParser.ID))) != 0)):
                        break

                pass
            elif token in [ZmeiLangParser.STRING_DQ]:
                self.state = 455
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.state = 456
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
            self.state = 459
            self.match(ZmeiLangParser.QUESTION_MARK)
            self.state = 460
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
            self.state = 462
            self.match(ZmeiLangParser.SLASH)
            self.state = 463
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

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


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
            self.state = 465
            self.id_or_kw()
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
            self.state = 467
            _la = self._input.LA(1)
            if not(((((_la - 72)) & ~0x3f) == 0 and ((1 << (_la - 72)) & ((1 << (ZmeiLangParser.EQUALS - 72)) | (1 << (ZmeiLangParser.DOLLAR - 72)) | (1 << (ZmeiLangParser.AMP - 72)) | (1 << (ZmeiLangParser.EXCLAM - 72)) | (1 << (ZmeiLangParser.STAR - 72)) | (1 << (ZmeiLangParser.APPROX - 72)))) != 0)):
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

    class Model_annotationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_admin(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_adminContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_model_annotation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModel_annotation" ):
                listener.enterModel_annotation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModel_annotation" ):
                listener.exitModel_annotation(self)




    def model_annotation(self):

        localctx = ZmeiLangParser.Model_annotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_model_annotation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self.an_admin()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class An_adminContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_ADMIN(self):
            return self.getToken(ZmeiLangParser.AN_ADMIN, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def an_admin_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_admin_listContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_admin_listContext,i)


        def an_admin_read_only(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_admin_read_onlyContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_admin_read_onlyContext,i)


        def an_admin_list_editable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_admin_list_editableContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_admin_list_editableContext,i)


        def an_admin_list_filter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_admin_list_filterContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_admin_list_filterContext,i)


        def an_admin_list_search(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_admin_list_searchContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_admin_list_searchContext,i)


        def an_admin_fields(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_admin_fieldsContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_admin_fieldsContext,i)


        def an_admin_inlines(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_admin_inlinesContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_admin_inlinesContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def an_admin_tabs(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_admin_tabsContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_admin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_admin" ):
                listener.enterAn_admin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_admin" ):
                listener.exitAn_admin(self)




    def an_admin(self):

        localctx = ZmeiLangParser.An_adminContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_an_admin)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.match(ZmeiLangParser.AN_ADMIN)
            self.state = 497
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 472
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 484
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 482
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [ZmeiLangParser.KW_LIST]:
                            self.state = 473
                            self.an_admin_list()
                            pass
                        elif token in [ZmeiLangParser.KW_READ_ONLY]:
                            self.state = 474
                            self.an_admin_read_only()
                            pass
                        elif token in [ZmeiLangParser.KW_LIST_EDITABLE]:
                            self.state = 475
                            self.an_admin_list_editable()
                            pass
                        elif token in [ZmeiLangParser.KW_LIST_FILTER]:
                            self.state = 476
                            self.an_admin_list_filter()
                            pass
                        elif token in [ZmeiLangParser.KW_LIST_SEARCH]:
                            self.state = 477
                            self.an_admin_list_search()
                            pass
                        elif token in [ZmeiLangParser.KW_FIELDS]:
                            self.state = 478
                            self.an_admin_fields()
                            pass
                        elif token in [ZmeiLangParser.KW_INLINE]:
                            self.state = 479
                            self.an_admin_inlines()
                            pass
                        elif token in [ZmeiLangParser.NL]:
                            self.state = 480
                            self.match(ZmeiLangParser.NL)
                            pass
                        elif token in [ZmeiLangParser.COMA]:
                            self.state = 481
                            self.match(ZmeiLangParser.COMA)
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 486
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

                self.state = 488
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.KW_TABS:
                    self.state = 487
                    self.an_admin_tabs()


                self.state = 493
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZmeiLangParser.NL:
                    self.state = 490
                    self.match(ZmeiLangParser.NL)
                    self.state = 495
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 496
                self.match(ZmeiLangParser.BRACE_CLOSE)


            self.state = 502
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 499
                    self.match(ZmeiLangParser.NL) 
                self.state = 504
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class An_admin_inlinesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_INLINE(self):
            return self.getToken(ZmeiLangParser.KW_INLINE, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_admin_inline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_admin_inlineContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_admin_inlineContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_admin_inlines

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_admin_inlines" ):
                listener.enterAn_admin_inlines(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_admin_inlines" ):
                listener.exitAn_admin_inlines(self)




    def an_admin_inlines(self):

        localctx = ZmeiLangParser.An_admin_inlinesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_an_admin_inlines)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self.match(ZmeiLangParser.KW_INLINE)
            self.state = 506
            self.match(ZmeiLangParser.COLON)
            self.state = 507
            self.an_admin_inline()
            self.state = 512
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 508
                    self.match(ZmeiLangParser.COMA)
                    self.state = 509
                    self.an_admin_inline() 
                self.state = 514
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class An_admin_inlineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inline_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Inline_nameContext,0)


        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def inline_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Inline_typeContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Inline_typeContext,i)


        def inline_extra(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Inline_extraContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Inline_extraContext,i)


        def inline_fields(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Inline_fieldsContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Inline_fieldsContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_admin_inline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_admin_inline" ):
                listener.enterAn_admin_inline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_admin_inline" ):
                listener.exitAn_admin_inline(self)




    def an_admin_inline(self):

        localctx = ZmeiLangParser.An_admin_inlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_an_admin_inline)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self.inline_name()
            self.state = 528
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 516
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 524
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.KW_TYPE) | (1 << ZmeiLangParser.KW_EXTRA) | (1 << ZmeiLangParser.KW_FIELDS) | (1 << ZmeiLangParser.NL) | (1 << ZmeiLangParser.COMA))) != 0):
                    self.state = 522
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [ZmeiLangParser.KW_TYPE]:
                        self.state = 517
                        self.inline_type()
                        pass
                    elif token in [ZmeiLangParser.KW_EXTRA]:
                        self.state = 518
                        self.inline_extra()
                        pass
                    elif token in [ZmeiLangParser.KW_FIELDS]:
                        self.state = 519
                        self.inline_fields()
                        pass
                    elif token in [ZmeiLangParser.NL]:
                        self.state = 520
                        self.match(ZmeiLangParser.NL)
                        pass
                    elif token in [ZmeiLangParser.COMA]:
                        self.state = 521
                        self.match(ZmeiLangParser.COMA)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 526
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 527
                self.match(ZmeiLangParser.BRACE_CLOSE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Inline_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_inline_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInline_name" ):
                listener.enterInline_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInline_name" ):
                listener.exitInline_name(self)




    def inline_name(self):

        localctx = ZmeiLangParser.Inline_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_inline_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Inline_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_TYPE(self):
            return self.getToken(ZmeiLangParser.KW_TYPE, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def KW_INLINE_TYPE(self):
            return self.getToken(ZmeiLangParser.KW_INLINE_TYPE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_inline_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInline_type" ):
                listener.enterInline_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInline_type" ):
                listener.exitInline_type(self)




    def inline_type(self):

        localctx = ZmeiLangParser.Inline_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_inline_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
            self.match(ZmeiLangParser.KW_TYPE)
            self.state = 533
            self.match(ZmeiLangParser.COLON)
            self.state = 534
            self.match(ZmeiLangParser.KW_INLINE_TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Inline_extraContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_EXTRA(self):
            return self.getToken(ZmeiLangParser.KW_EXTRA, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def DIGIT(self):
            return self.getToken(ZmeiLangParser.DIGIT, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_inline_extra

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInline_extra" ):
                listener.enterInline_extra(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInline_extra" ):
                listener.exitInline_extra(self)




    def inline_extra(self):

        localctx = ZmeiLangParser.Inline_extraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_inline_extra)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            self.match(ZmeiLangParser.KW_EXTRA)
            self.state = 537
            self.match(ZmeiLangParser.COLON)
            self.state = 538
            self.match(ZmeiLangParser.DIGIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Inline_fieldsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FIELDS(self):
            return self.getToken(ZmeiLangParser.KW_FIELDS, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def field_list_expr(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_list_exprContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_inline_fields

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInline_fields" ):
                listener.enterInline_fields(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInline_fields" ):
                listener.exitInline_fields(self)




    def inline_fields(self):

        localctx = ZmeiLangParser.Inline_fieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_inline_fields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 540
            self.match(ZmeiLangParser.KW_FIELDS)
            self.state = 541
            self.match(ZmeiLangParser.COLON)
            self.state = 542
            self.field_list_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class An_admin_tabsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_TABS(self):
            return self.getToken(ZmeiLangParser.KW_TABS, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_admin_tab(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_admin_tabContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_admin_tabContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_admin_tabs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_admin_tabs" ):
                listener.enterAn_admin_tabs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_admin_tabs" ):
                listener.exitAn_admin_tabs(self)




    def an_admin_tabs(self):

        localctx = ZmeiLangParser.An_admin_tabsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_an_admin_tabs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544
            self.match(ZmeiLangParser.KW_TABS)
            self.state = 545
            self.match(ZmeiLangParser.COLON)
            self.state = 546
            self.an_admin_tab()
            self.state = 551
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 547
                self.match(ZmeiLangParser.COMA)
                self.state = 548
                self.an_admin_tab()
                self.state = 553
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class An_admin_tabContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tab_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Tab_nameContext,0)


        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def field_list_expr(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_list_exprContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def tab_verbose_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Tab_verbose_nameContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_admin_tab

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_admin_tab" ):
                listener.enterAn_admin_tab(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_admin_tab" ):
                listener.exitAn_admin_tab(self)




    def an_admin_tab(self):

        localctx = ZmeiLangParser.An_admin_tabContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_an_admin_tab)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 554
            self.tab_name()
            self.state = 556
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.STRING_DQ or _la==ZmeiLangParser.STRING_SQ:
                self.state = 555
                self.tab_verbose_name()


            self.state = 558
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 559
            self.field_list_expr()
            self.state = 560
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Tab_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_tab_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTab_name" ):
                listener.enterTab_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTab_name" ):
                listener.exitTab_name(self)




    def tab_name(self):

        localctx = ZmeiLangParser.Tab_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_tab_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 562
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Tab_verbose_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_tab_verbose_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTab_verbose_name" ):
                listener.enterTab_verbose_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTab_verbose_name" ):
                listener.exitTab_verbose_name(self)




    def tab_verbose_name(self):

        localctx = ZmeiLangParser.Tab_verbose_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_tab_verbose_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 564
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.STRING_DQ or _la==ZmeiLangParser.STRING_SQ):
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

    class An_admin_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_LIST(self):
            return self.getToken(ZmeiLangParser.KW_LIST, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def field_list_expr(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_list_exprContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_admin_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_admin_list" ):
                listener.enterAn_admin_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_admin_list" ):
                listener.exitAn_admin_list(self)




    def an_admin_list(self):

        localctx = ZmeiLangParser.An_admin_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_an_admin_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 566
            self.match(ZmeiLangParser.KW_LIST)
            self.state = 567
            self.match(ZmeiLangParser.COLON)
            self.state = 568
            self.field_list_expr()
            self.state = 572
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 569
                    self.match(ZmeiLangParser.NL) 
                self.state = 574
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class An_admin_read_onlyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_READ_ONLY(self):
            return self.getToken(ZmeiLangParser.KW_READ_ONLY, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def field_list_expr(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_list_exprContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_admin_read_only

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_admin_read_only" ):
                listener.enterAn_admin_read_only(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_admin_read_only" ):
                listener.exitAn_admin_read_only(self)




    def an_admin_read_only(self):

        localctx = ZmeiLangParser.An_admin_read_onlyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_an_admin_read_only)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 575
            self.match(ZmeiLangParser.KW_READ_ONLY)
            self.state = 576
            self.match(ZmeiLangParser.COLON)
            self.state = 577
            self.field_list_expr()
            self.state = 581
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 578
                    self.match(ZmeiLangParser.NL) 
                self.state = 583
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class An_admin_list_editableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_LIST_EDITABLE(self):
            return self.getToken(ZmeiLangParser.KW_LIST_EDITABLE, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def field_list_expr(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_list_exprContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_admin_list_editable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_admin_list_editable" ):
                listener.enterAn_admin_list_editable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_admin_list_editable" ):
                listener.exitAn_admin_list_editable(self)




    def an_admin_list_editable(self):

        localctx = ZmeiLangParser.An_admin_list_editableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_an_admin_list_editable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 584
            self.match(ZmeiLangParser.KW_LIST_EDITABLE)
            self.state = 585
            self.match(ZmeiLangParser.COLON)
            self.state = 586
            self.field_list_expr()
            self.state = 590
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,53,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 587
                    self.match(ZmeiLangParser.NL) 
                self.state = 592
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,53,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class An_admin_list_filterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_LIST_FILTER(self):
            return self.getToken(ZmeiLangParser.KW_LIST_FILTER, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def field_list_expr(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_list_exprContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_admin_list_filter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_admin_list_filter" ):
                listener.enterAn_admin_list_filter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_admin_list_filter" ):
                listener.exitAn_admin_list_filter(self)




    def an_admin_list_filter(self):

        localctx = ZmeiLangParser.An_admin_list_filterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_an_admin_list_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 593
            self.match(ZmeiLangParser.KW_LIST_FILTER)
            self.state = 594
            self.match(ZmeiLangParser.COLON)
            self.state = 595
            self.field_list_expr()
            self.state = 599
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,54,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 596
                    self.match(ZmeiLangParser.NL) 
                self.state = 601
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,54,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class An_admin_list_searchContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_LIST_SEARCH(self):
            return self.getToken(ZmeiLangParser.KW_LIST_SEARCH, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def field_list_expr(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_list_exprContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_admin_list_search

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_admin_list_search" ):
                listener.enterAn_admin_list_search(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_admin_list_search" ):
                listener.exitAn_admin_list_search(self)




    def an_admin_list_search(self):

        localctx = ZmeiLangParser.An_admin_list_searchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_an_admin_list_search)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 602
            self.match(ZmeiLangParser.KW_LIST_SEARCH)
            self.state = 603
            self.match(ZmeiLangParser.COLON)
            self.state = 604
            self.field_list_expr()
            self.state = 608
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,55,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 605
                    self.match(ZmeiLangParser.NL) 
                self.state = 610
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,55,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class An_admin_fieldsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FIELDS(self):
            return self.getToken(ZmeiLangParser.KW_FIELDS, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def field_list_expr(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_list_exprContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_admin_fields

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_admin_fields" ):
                listener.enterAn_admin_fields(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_admin_fields" ):
                listener.exitAn_admin_fields(self)




    def an_admin_fields(self):

        localctx = ZmeiLangParser.An_admin_fieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_an_admin_fields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 611
            self.match(ZmeiLangParser.KW_FIELDS)
            self.state = 612
            self.match(ZmeiLangParser.COLON)
            self.state = 613
            self.field_list_expr()
            self.state = 617
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 614
                    self.match(ZmeiLangParser.NL) 
                self.state = 619
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_list_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(ZmeiLangParser.STAR, 0)

        def DOT(self):
            return self.getToken(ZmeiLangParser.DOT, 0)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def EXCLUDE(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.EXCLUDE)
            else:
                return self.getToken(ZmeiLangParser.EXCLUDE, i)

        def field_list_expr_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Field_list_expr_fieldContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Field_list_expr_fieldContext,i)


        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_list_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_list_expr" ):
                listener.enterField_list_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_list_expr" ):
                listener.exitField_list_expr(self)




    def field_list_expr(self):

        localctx = ZmeiLangParser.Field_list_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_field_list_expr)
        self._la = 0 # Token type
        try:
            self.state = 643
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.DOT, ZmeiLangParser.STAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 621
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.DOT:
                    self.state = 620
                    self.match(ZmeiLangParser.DOT)


                self.state = 623
                self.match(ZmeiLangParser.STAR)
                self.state = 629
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,58,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 624
                        self.match(ZmeiLangParser.COMA)
                        self.state = 625
                        self.match(ZmeiLangParser.EXCLUDE)
                        self.state = 626
                        self.field_list_expr_field() 
                    self.state = 631
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,58,self._ctx)

                pass
            elif token in [ZmeiLangParser.BOOL, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE_FILE, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_SIMPLE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 632
                self.id_or_kw()
                self.state = 640
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,60,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 633
                        self.match(ZmeiLangParser.COMA)
                        self.state = 635
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==ZmeiLangParser.EXCLUDE:
                            self.state = 634
                            self.match(ZmeiLangParser.EXCLUDE)


                        self.state = 637
                        self.field_list_expr_field() 
                    self.state = 642
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,60,self._ctx)

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

    class Field_list_expr_fieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.STAR)
            else:
                return self.getToken(ZmeiLangParser.STAR, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_list_expr_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_list_expr_field" ):
                listener.enterField_list_expr_field(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_list_expr_field" ):
                listener.exitField_list_expr_field(self)




    def field_list_expr_field(self):

        localctx = ZmeiLangParser.Field_list_expr_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_field_list_expr_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 646
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.STAR:
                self.state = 645
                self.match(ZmeiLangParser.STAR)


            self.state = 648
            self.id_or_kw()
            self.state = 650
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.STAR:
                self.state = 649
                self.match(ZmeiLangParser.STAR)


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
        self.enterRule(localctx, 106, self.RULE_annotation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 652
            self.match(ZmeiLangParser.ANNOTATION)
            self.state = 654
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 653
                self.annotation_descr()


            self.state = 657
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                self.state = 656
                self.annotation_code()


            self.state = 662
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,66,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 659
                    self.match(ZmeiLangParser.NL) 
                self.state = 664
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,66,self._ctx)

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

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


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
        self.enterRule(localctx, 108, self.RULE_annotation_descr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 665
            self.match(ZmeiLangParser.DOT)
            self.state = 666
            self.id_or_kw()
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
        self.enterRule(localctx, 110, self.RULE_annotation_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 668
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
        self.enterRule(localctx, 112, self.RULE_xml_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 671
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 41)) & ~0x3f) == 0 and ((1 << (_la - 41)) & ((1 << (ZmeiLangParser.NL - 41)) | (1 << (ZmeiLangParser.WS - 41)) | (1 << (ZmeiLangParser.XML_TEXT - 41)))) != 0):
                self.state = 670
                self.xml_chardata()


            self.state = 682
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,70,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 675
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [ZmeiLangParser.XML_OPEN]:
                        self.state = 673
                        self.xml_element()
                        pass
                    elif token in [ZmeiLangParser.XML_EntityRef, ZmeiLangParser.XML_CharRef]:
                        self.state = 674
                        self.xml_reference()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 678
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if ((((_la - 41)) & ~0x3f) == 0 and ((1 << (_la - 41)) & ((1 << (ZmeiLangParser.NL - 41)) | (1 << (ZmeiLangParser.WS - 41)) | (1 << (ZmeiLangParser.XML_TEXT - 41)))) != 0):
                        self.state = 677
                        self.xml_chardata()

             
                self.state = 684
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,70,self._ctx)

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
        self.enterRule(localctx, 114, self.RULE_xml_element)
        self._la = 0 # Token type
        try:
            self.state = 710
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,73,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 685
                self.match(ZmeiLangParser.XML_OPEN)
                self.state = 686
                self.xml_name()
                self.state = 690
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZmeiLangParser.XML_Name:
                    self.state = 687
                    self.xml_attribute()
                    self.state = 692
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 693
                self.match(ZmeiLangParser.XML_CLOSE)
                self.state = 694
                self.xml_content()
                self.state = 695
                self.match(ZmeiLangParser.XML_OPEN)
                self.state = 696
                self.match(ZmeiLangParser.XML_SLASH)
                self.state = 697
                self.xml_name_end()
                self.state = 698
                self.match(ZmeiLangParser.XML_CLOSE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 700
                self.match(ZmeiLangParser.XML_OPEN)
                self.state = 701
                self.xml_name()
                self.state = 705
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZmeiLangParser.XML_Name:
                    self.state = 702
                    self.xml_attribute()
                    self.state = 707
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 708
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
        self.enterRule(localctx, 116, self.RULE_xml_name)
        try:
            self.state = 714
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.XML_CmpName]:
                self.enterOuterAlt(localctx, 1)
                self.state = 712
                self.xml_component_name()
                pass
            elif token in [ZmeiLangParser.XML_Name]:
                self.enterOuterAlt(localctx, 2)
                self.state = 713
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
        self.enterRule(localctx, 118, self.RULE_xml_name_end)
        try:
            self.state = 718
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.XML_CmpName]:
                self.enterOuterAlt(localctx, 1)
                self.state = 716
                self.xml_component_name()
                pass
            elif token in [ZmeiLangParser.XML_Name]:
                self.enterOuterAlt(localctx, 2)
                self.state = 717
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
        self.enterRule(localctx, 120, self.RULE_xml_tag_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 720
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
        self.enterRule(localctx, 122, self.RULE_xml_component_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 722
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
        self.enterRule(localctx, 124, self.RULE_xml_reference)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 724
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
        self.enterRule(localctx, 126, self.RULE_xml_attribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 726
            self.match(ZmeiLangParser.XML_Name)
            self.state = 727
            self.match(ZmeiLangParser.XML_EQUALS)
            self.state = 728
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
        self.enterRule(localctx, 128, self.RULE_xml_chardata)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 730
            _la = self._input.LA(1)
            if not(((((_la - 41)) & ~0x3f) == 0 and ((1 << (_la - 41)) & ((1 << (ZmeiLangParser.NL - 41)) | (1 << (ZmeiLangParser.WS - 41)) | (1 << (ZmeiLangParser.XML_TEXT - 41)))) != 0)):
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
        self.enterRule(localctx, 130, self.RULE_xml_misc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 732
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

    class Id_or_kwContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZmeiLangParser.ID, 0)

        def BOOL(self):
            return self.getToken(ZmeiLangParser.BOOL, 0)

        def KW_INLINE_TYPE(self):
            return self.getToken(ZmeiLangParser.KW_INLINE_TYPE, 0)

        def KW_INLINE(self):
            return self.getToken(ZmeiLangParser.KW_INLINE, 0)

        def KW_TYPE(self):
            return self.getToken(ZmeiLangParser.KW_TYPE, 0)

        def KW_EXTRA(self):
            return self.getToken(ZmeiLangParser.KW_EXTRA, 0)

        def KW_TABS(self):
            return self.getToken(ZmeiLangParser.KW_TABS, 0)

        def KW_LIST(self):
            return self.getToken(ZmeiLangParser.KW_LIST, 0)

        def KW_READ_ONLY(self):
            return self.getToken(ZmeiLangParser.KW_READ_ONLY, 0)

        def KW_LIST_EDITABLE(self):
            return self.getToken(ZmeiLangParser.KW_LIST_EDITABLE, 0)

        def KW_LIST_FILTER(self):
            return self.getToken(ZmeiLangParser.KW_LIST_FILTER, 0)

        def KW_LIST_SEARCH(self):
            return self.getToken(ZmeiLangParser.KW_LIST_SEARCH, 0)

        def KW_FIELDS(self):
            return self.getToken(ZmeiLangParser.KW_FIELDS, 0)

        def KW_IMPORT(self):
            return self.getToken(ZmeiLangParser.KW_IMPORT, 0)

        def KW_AS(self):
            return self.getToken(ZmeiLangParser.KW_AS, 0)

        def COL_FIELD_TYPE_LONGTEXT(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, 0)

        def COL_FIELD_TYPE_HTML(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_HTML, 0)

        def COL_FIELD_TYPE_HTML_MEDIA(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, 0)

        def COL_FIELD_TYPE_FLOAT(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_FLOAT, 0)

        def COL_FIELD_TYPE_DECIMAL(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, 0)

        def COL_FIELD_TYPE_DATE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_DATE, 0)

        def COL_FIELD_TYPE_DATETIME(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_DATETIME, 0)

        def COL_FIELD_TYPE_CREATE_TIME(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, 0)

        def COL_FIELD_TYPE_UPDATE_TIME(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, 0)

        def COL_FIELD_TYPE_IMAGE_FILE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_IMAGE_FILE, 0)

        def COL_FIELD_TYPE_IMAGE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_IMAGE, 0)

        def COL_FIELD_TYPE_FILER_IMAGE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, 0)

        def COL_FIELD_TYPE_FILER_FILE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, 0)

        def COL_FIELD_TYPE_FILE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_FILE, 0)

        def COL_FIELD_TYPE_SIMPLE_FILE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_SIMPLE_FILE, 0)

        def COL_FIELD_TYPE_FOLDER(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_FOLDER, 0)

        def COL_FIELD_TYPE_IMAGE_FOLDER(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_IMAGE_FOLDER, 0)

        def COL_FIELD_TYPE_TEXT(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_TEXT, 0)

        def COL_FIELD_TYPE_INT(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_INT, 0)

        def COL_FIELD_TYPE_SLUG(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_SLUG, 0)

        def COL_FIELD_TYPE_BOOL(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_BOOL, 0)

        def COL_FIELD_TYPE_ONE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_ONE, 0)

        def COL_FIELD_TYPE_ONE2ONE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, 0)

        def COL_FIELD_TYPE_MANY(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_MANY, 0)

        def COL_FIELD_CHOICES(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_CHOICES, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_id_or_kw

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId_or_kw" ):
                listener.enterId_or_kw(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId_or_kw" ):
                listener.exitId_or_kw(self)




    def id_or_kw(self):

        localctx = ZmeiLangParser.Id_or_kwContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_id_or_kw)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 734
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.BOOL) | (1 << ZmeiLangParser.KW_INLINE_TYPE) | (1 << ZmeiLangParser.KW_INLINE) | (1 << ZmeiLangParser.KW_TYPE) | (1 << ZmeiLangParser.KW_EXTRA) | (1 << ZmeiLangParser.KW_TABS) | (1 << ZmeiLangParser.KW_LIST) | (1 << ZmeiLangParser.KW_READ_ONLY) | (1 << ZmeiLangParser.KW_LIST_EDITABLE) | (1 << ZmeiLangParser.KW_LIST_FILTER) | (1 << ZmeiLangParser.KW_LIST_SEARCH) | (1 << ZmeiLangParser.KW_FIELDS) | (1 << ZmeiLangParser.KW_IMPORT) | (1 << ZmeiLangParser.KW_AS) | (1 << ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FLOAT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DECIMAL) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATETIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_IMAGE_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_SIMPLE_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_IMAGE_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_TEXT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_INT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_SLUG) | (1 << ZmeiLangParser.COL_FIELD_TYPE_BOOL) | (1 << ZmeiLangParser.COL_FIELD_TYPE_ONE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_MANY) | (1 << ZmeiLangParser.COL_FIELD_CHOICES) | (1 << ZmeiLangParser.ID))) != 0)):
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
        self.enterRule(localctx, 134, self.RULE_col_field_def)
        try:
            self.state = 757
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 736
                self.field_longtext()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 737
                self.field_html_media()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_HTML]:
                self.enterOuterAlt(localctx, 3)
                self.state = 738
                self.field_html()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_FLOAT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 739
                self.field_float()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_DECIMAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 740
                self.field_decimal()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_DATE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 741
                self.field_date()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_DATETIME]:
                self.enterOuterAlt(localctx, 7)
                self.state = 742
                self.field_datetime()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME]:
                self.enterOuterAlt(localctx, 8)
                self.state = 743
                self.field_create_time()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME]:
                self.enterOuterAlt(localctx, 9)
                self.state = 744
                self.field_update_time()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_TEXT]:
                self.enterOuterAlt(localctx, 10)
                self.state = 745
                self.field_text()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_INT]:
                self.enterOuterAlt(localctx, 11)
                self.state = 746
                self.field_int()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_SLUG]:
                self.enterOuterAlt(localctx, 12)
                self.state = 747
                self.field_slug()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_BOOL]:
                self.enterOuterAlt(localctx, 13)
                self.state = 748
                self.field_bool()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY]:
                self.enterOuterAlt(localctx, 14)
                self.state = 749
                self.field_relation()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_IMAGE_FILE]:
                self.enterOuterAlt(localctx, 15)
                self.state = 750
                self.field_image_file()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_IMAGE_FOLDER]:
                self.enterOuterAlt(localctx, 16)
                self.state = 751
                self.field_image()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE]:
                self.enterOuterAlt(localctx, 17)
                self.state = 752
                self.field_filer_image()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE]:
                self.enterOuterAlt(localctx, 18)
                self.state = 753
                self.field_filer_file()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_FILE]:
                self.enterOuterAlt(localctx, 19)
                self.state = 754
                self.field_file()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_SIMPLE_FILE]:
                self.enterOuterAlt(localctx, 20)
                self.state = 755
                self.field_simple_file()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_FOLDER]:
                self.enterOuterAlt(localctx, 21)
                self.state = 756
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
        self.enterRule(localctx, 136, self.RULE_field_longtext)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 759
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
        self.enterRule(localctx, 138, self.RULE_field_html)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 761
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
        self.enterRule(localctx, 140, self.RULE_field_html_media)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 763
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
        self.enterRule(localctx, 142, self.RULE_field_float)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 765
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
        self.enterRule(localctx, 144, self.RULE_field_decimal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 767
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
        self.enterRule(localctx, 146, self.RULE_field_date)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 769
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
        self.enterRule(localctx, 148, self.RULE_field_datetime)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 771
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
        self.enterRule(localctx, 150, self.RULE_field_create_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 773
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
        self.enterRule(localctx, 152, self.RULE_field_update_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 775
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
        self.enterRule(localctx, 154, self.RULE_field_image_file)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 777
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
        self.enterRule(localctx, 156, self.RULE_field_filer_image)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 779
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
        self.enterRule(localctx, 158, self.RULE_field_filer_file)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 781
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
        self.enterRule(localctx, 160, self.RULE_field_file)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 783
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
        self.enterRule(localctx, 162, self.RULE_field_simple_file)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 785
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
        self.enterRule(localctx, 164, self.RULE_field_folder)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 787
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
        self.enterRule(localctx, 166, self.RULE_field_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 789
            self.match(ZmeiLangParser.COL_FIELD_TYPE_TEXT)
            self.state = 798
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 790
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 791
                self.field_text_size()
                self.state = 794
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.COMA:
                    self.state = 792
                    self.match(ZmeiLangParser.COMA)
                    self.state = 793
                    self.field_text_choices()


                self.state = 796
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
        self.enterRule(localctx, 168, self.RULE_field_text_size)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 800
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
        self.enterRule(localctx, 170, self.RULE_field_text_choices)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 802
            self.match(ZmeiLangParser.COL_FIELD_CHOICES)
            self.state = 803
            self.match(ZmeiLangParser.EQUALS)
            self.state = 804
            self.field_text_choice()
            self.state = 809
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 805
                self.match(ZmeiLangParser.COMA)
                self.state = 806
                self.field_text_choice()
                self.state = 811
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
        self.enterRule(localctx, 172, self.RULE_field_text_choice)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 813
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
            if la_ == 1:
                self.state = 812
                self.field_text_choice_key()


            self.state = 815
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
        self.enterRule(localctx, 174, self.RULE_field_text_choice_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 817
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
        self.enterRule(localctx, 176, self.RULE_field_text_choice_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 819
            self.match(ZmeiLangParser.ID)
            self.state = 820
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
        self.enterRule(localctx, 178, self.RULE_field_int)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 822
            self.match(ZmeiLangParser.COL_FIELD_TYPE_INT)
            self.state = 827
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 823
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 824
                self.field_int_choices()
                self.state = 825
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
        self.enterRule(localctx, 180, self.RULE_field_int_choices)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 829
            self.match(ZmeiLangParser.COL_FIELD_CHOICES)
            self.state = 830
            self.match(ZmeiLangParser.EQUALS)
            self.state = 831
            self.field_int_choice()
            self.state = 836
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 832
                self.match(ZmeiLangParser.COMA)
                self.state = 833
                self.field_int_choice()
                self.state = 838
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
        self.enterRule(localctx, 182, self.RULE_field_int_choice)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 840
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DIGIT:
                self.state = 839
                self.field_int_choice_key()


            self.state = 842
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
        self.enterRule(localctx, 184, self.RULE_field_int_choice_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 844
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
        self.enterRule(localctx, 186, self.RULE_field_int_choice_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 846
            self.match(ZmeiLangParser.DIGIT)
            self.state = 847
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
        self.enterRule(localctx, 188, self.RULE_field_slug)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 849
            self.match(ZmeiLangParser.COL_FIELD_TYPE_SLUG)
            self.state = 850
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 851
            self.field_slug_ref_field()
            self.state = 852
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
        self.enterRule(localctx, 190, self.RULE_field_slug_ref_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 854
            self.field_slug_ref_field_id()
            self.state = 859
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 855
                self.match(ZmeiLangParser.COMA)
                self.state = 856
                self.field_slug_ref_field_id()
                self.state = 861
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
        self.enterRule(localctx, 192, self.RULE_field_slug_ref_field_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 862
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
        self.enterRule(localctx, 194, self.RULE_field_bool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 864
            self.match(ZmeiLangParser.COL_FIELD_TYPE_BOOL)
            self.state = 869
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 865
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 866
                self.field_bool_default()
                self.state = 867
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
        self.enterRule(localctx, 196, self.RULE_field_bool_default)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 871
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
        self.enterRule(localctx, 198, self.RULE_field_image)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 873
            self.filer_image_type()
            self.state = 878
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 874
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 875
                self.field_image_sizes()
                self.state = 876
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
        self.enterRule(localctx, 200, self.RULE_filer_image_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 880
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
        self.enterRule(localctx, 202, self.RULE_field_image_sizes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 882
            self.field_image_size()
            self.state = 887
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 883
                self.match(ZmeiLangParser.COMA)
                self.state = 884
                self.field_image_size()
                self.state = 889
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
        self.enterRule(localctx, 204, self.RULE_field_image_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 890
            self.field_image_size_name()
            self.state = 891
            self.field_image_size_dimensions()
            self.state = 892
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
        self.enterRule(localctx, 206, self.RULE_field_image_size_dimensions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 894
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
        self.enterRule(localctx, 208, self.RULE_field_image_size_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 896
            self.match(ZmeiLangParser.ID)
            self.state = 897
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
        self.enterRule(localctx, 210, self.RULE_field_image_filters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 902
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.FILTER:
                self.state = 899
                self.field_image_filter()
                self.state = 904
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
        self.enterRule(localctx, 212, self.RULE_field_image_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 905
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
        self.enterRule(localctx, 214, self.RULE_field_relation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 907
            self.field_relation_type()
            self.state = 908
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 911
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.REF_SIGN]:
                self.state = 909
                self.field_relation_target_ref()
                pass
            elif token in [ZmeiLangParser.CLASSNAME]:
                self.state = 910
                self.field_relation_target_class()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 914
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.RELATED:
                self.state = 913
                self.field_relation_related_name()


            self.state = 916
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
        self.enterRule(localctx, 216, self.RULE_field_relation_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 918
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
        self.enterRule(localctx, 218, self.RULE_field_relation_target_ref)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 920
            self.match(ZmeiLangParser.REF_SIGN)
            self.state = 921
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
        self.enterRule(localctx, 220, self.RULE_field_relation_target_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 923
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
        self.enterRule(localctx, 222, self.RULE_field_relation_related_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 925
            self.match(ZmeiLangParser.RELATED)
            self.state = 926
            self.match(ZmeiLangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






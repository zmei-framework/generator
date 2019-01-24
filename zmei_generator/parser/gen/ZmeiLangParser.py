# Generated from /Users/aleksandrrudakov/dev/zmei/generator/zmei_generator/parser/gen/grammar/ZmeiLangParser.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\u00a4")
        buf.write("\u09bb\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("q\tq\4r\tr\4s\ts\4t\tt\4u\tu\4v\tv\4w\tw\4x\tx\4y\ty\4")
        buf.write("z\tz\4{\t{\4|\t|\4}\t}\4~\t~\4\177\t\177\4\u0080\t\u0080")
        buf.write("\4\u0081\t\u0081\4\u0082\t\u0082\4\u0083\t\u0083\4\u0084")
        buf.write("\t\u0084\4\u0085\t\u0085\4\u0086\t\u0086\4\u0087\t\u0087")
        buf.write("\4\u0088\t\u0088\4\u0089\t\u0089\4\u008a\t\u008a\4\u008b")
        buf.write("\t\u008b\4\u008c\t\u008c\4\u008d\t\u008d\4\u008e\t\u008e")
        buf.write("\4\u008f\t\u008f\4\u0090\t\u0090\4\u0091\t\u0091\4\u0092")
        buf.write("\t\u0092\4\u0093\t\u0093\4\u0094\t\u0094\4\u0095\t\u0095")
        buf.write("\4\u0096\t\u0096\4\u0097\t\u0097\4\u0098\t\u0098\4\u0099")
        buf.write("\t\u0099\4\u009a\t\u009a\4\u009b\t\u009b\4\u009c\t\u009c")
        buf.write("\4\u009d\t\u009d\4\u009e\t\u009e\4\u009f\t\u009f\4\u00a0")
        buf.write("\t\u00a0\4\u00a1\t\u00a1\4\u00a2\t\u00a2\4\u00a3\t\u00a3")
        buf.write("\4\u00a4\t\u00a4\4\u00a5\t\u00a5\4\u00a6\t\u00a6\4\u00a7")
        buf.write("\t\u00a7\4\u00a8\t\u00a8\4\u00a9\t\u00a9\4\u00aa\t\u00aa")
        buf.write("\4\u00ab\t\u00ab\4\u00ac\t\u00ac\4\u00ad\t\u00ad\4\u00ae")
        buf.write("\t\u00ae\4\u00af\t\u00af\4\u00b0\t\u00b0\4\u00b1\t\u00b1")
        buf.write("\4\u00b2\t\u00b2\4\u00b3\t\u00b3\4\u00b4\t\u00b4\4\u00b5")
        buf.write("\t\u00b5\4\u00b6\t\u00b6\4\u00b7\t\u00b7\4\u00b8\t\u00b8")
        buf.write("\4\u00b9\t\u00b9\4\u00ba\t\u00ba\4\u00bb\t\u00bb\4\u00bc")
        buf.write("\t\u00bc\4\u00bd\t\u00bd\4\u00be\t\u00be\4\u00bf\t\u00bf")
        buf.write("\4\u00c0\t\u00c0\4\u00c1\t\u00c1\4\u00c2\t\u00c2\4\u00c3")
        buf.write("\t\u00c3\4\u00c4\t\u00c4\4\u00c5\t\u00c5\4\u00c6\t\u00c6")
        buf.write("\4\u00c7\t\u00c7\4\u00c8\t\u00c8\4\u00c9\t\u00c9\4\u00ca")
        buf.write("\t\u00ca\4\u00cb\t\u00cb\4\u00cc\t\u00cc\4\u00cd\t\u00cd")
        buf.write("\4\u00ce\t\u00ce\4\u00cf\t\u00cf\4\u00d0\t\u00d0\4\u00d1")
        buf.write("\t\u00d1\4\u00d2\t\u00d2\4\u00d3\t\u00d3\4\u00d4\t\u00d4")
        buf.write("\4\u00d5\t\u00d5\4\u00d6\t\u00d6\4\u00d7\t\u00d7\4\u00d8")
        buf.write("\t\u00d8\4\u00d9\t\u00d9\4\u00da\t\u00da\4\u00db\t\u00db")
        buf.write("\4\u00dc\t\u00dc\4\u00dd\t\u00dd\4\u00de\t\u00de\4\u00df")
        buf.write("\t\u00df\4\u00e0\t\u00e0\4\u00e1\t\u00e1\4\u00e2\t\u00e2")
        buf.write("\4\u00e3\t\u00e3\4\u00e4\t\u00e4\4\u00e5\t\u00e5\4\u00e6")
        buf.write("\t\u00e6\4\u00e7\t\u00e7\4\u00e8\t\u00e8\4\u00e9\t\u00e9")
        buf.write("\4\u00ea\t\u00ea\4\u00eb\t\u00eb\4\u00ec\t\u00ec\4\u00ed")
        buf.write("\t\u00ed\4\u00ee\t\u00ee\4\u00ef\t\u00ef\4\u00f0\t\u00f0")
        buf.write("\4\u00f1\t\u00f1\4\u00f2\t\u00f2\4\u00f3\t\u00f3\4\u00f4")
        buf.write("\t\u00f4\4\u00f5\t\u00f5\4\u00f6\t\u00f6\4\u00f7\t\u00f7")
        buf.write("\4\u00f8\t\u00f8\4\u00f9\t\u00f9\4\u00fa\t\u00fa\4\u00fb")
        buf.write("\t\u00fb\4\u00fc\t\u00fc\4\u00fd\t\u00fd\4\u00fe\t\u00fe")
        buf.write("\4\u00ff\t\u00ff\4\u0100\t\u0100\4\u0101\t\u0101\4\u0102")
        buf.write("\t\u0102\4\u0103\t\u0103\4\u0104\t\u0104\4\u0105\t\u0105")
        buf.write("\4\u0106\t\u0106\4\u0107\t\u0107\4\u0108\t\u0108\4\u0109")
        buf.write("\t\u0109\4\u010a\t\u010a\4\u010b\t\u010b\4\u010c\t\u010c")
        buf.write("\4\u010d\t\u010d\4\u010e\t\u010e\4\u010f\t\u010f\4\u0110")
        buf.write("\t\u0110\4\u0111\t\u0111\4\u0112\t\u0112\4\u0113\t\u0113")
        buf.write("\4\u0114\t\u0114\4\u0115\t\u0115\3\2\7\2\u022c\n\2\f\2")
        buf.write("\16\2\u022f\13\2\3\2\7\2\u0232\n\2\f\2\16\2\u0235\13\2")
        buf.write("\3\2\7\2\u0238\n\2\f\2\16\2\u023b\13\2\3\2\5\2\u023e\n")
        buf.write("\2\3\2\6\2\u0241\n\2\r\2\16\2\u0242\5\2\u0245\n\2\3\2")
        buf.write("\7\2\u0248\n\2\f\2\16\2\u024b\13\2\3\2\5\2\u024e\n\2\3")
        buf.write("\2\6\2\u0251\n\2\r\2\16\2\u0252\5\2\u0255\n\2\3\2\7\2")
        buf.write("\u0258\n\2\f\2\16\2\u025b\13\2\3\2\3\2\3\3\6\3\u0260\n")
        buf.write("\3\r\3\16\3\u0261\3\4\6\4\u0265\n\4\r\4\16\4\u0266\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\5\7\u026f\n\7\3\7\3\7\3\7\6\7\u0274")
        buf.write("\n\7\r\7\16\7\u0275\3\b\5\b\u0279\n\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\7\t\u0280\n\t\f\t\16\t\u0283\13\t\3\n\3\n\3\n\5\n")
        buf.write("\u0288\n\n\3\n\5\n\u028b\n\n\3\13\3\13\3\f\3\f\3\r\3\r")
        buf.write("\3\16\3\16\3\17\3\17\3\17\7\17\u0298\n\17\f\17\16\17\u029b")
        buf.write("\13\17\3\20\3\20\3\20\3\20\5\20\u02a1\n\20\3\20\3\20\3")
        buf.write("\21\5\21\u02a6\n\21\3\21\3\21\3\21\3\21\7\21\u02ac\n\21")
        buf.write("\f\21\16\21\u02af\13\21\3\21\3\21\3\21\5\21\u02b4\n\21")
        buf.write("\3\21\7\21\u02b7\n\21\f\21\16\21\u02ba\13\21\5\21\u02bc")
        buf.write("\n\21\3\22\5\22\u02bf\n\22\3\22\3\22\5\22\u02c3\n\22\3")
        buf.write("\23\3\23\3\23\3\23\3\24\3\24\5\24\u02cb\n\24\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\5\27\u02dd\n\27\3\30\3\30\3\30\3\30\3")
        buf.write("\30\5\30\u02e4\n\30\3\31\3\31\3\32\3\32\3\32\5\32\u02eb")
        buf.write("\n\32\3\33\3\33\3\33\5\33\u02f0\n\33\3\34\3\34\3\34\5")
        buf.write("\34\u02f5\n\34\3\35\3\35\3\35\5\35\u02fa\n\35\3\36\3\36")
        buf.write("\3\36\7\36\u02ff\n\36\f\36\16\36\u0302\13\36\3\36\5\36")
        buf.write("\u0305\n\36\3\36\7\36\u0308\n\36\f\36\16\36\u030b\13\36")
        buf.write("\3\36\6\36\u030e\n\36\r\36\16\36\u030f\3\36\7\36\u0313")
        buf.write("\n\36\f\36\16\36\u0316\13\36\3\36\3\36\3\37\3\37\3 \3")
        buf.write(" \3 \7 \u031f\n \f \16 \u0322\13 \3 \5 \u0325\n \3 \7")
        buf.write(" \u0328\n \f \16 \u032b\13 \3 \3 \5 \u032f\n \7 \u0331")
        buf.write("\n \f \16 \u0334\13 \3 \7 \u0337\n \f \16 \u033a\13 \3")
        buf.write(" \3 \3!\3!\3!\7!\u0341\n!\f!\16!\u0344\13!\3!\3!\3!\7")
        buf.write("!\u0349\n!\f!\16!\u034c\13!\5!\u034e\n!\3!\7!\u0351\n")
        buf.write("!\f!\16!\u0354\13!\3!\3!\3\"\7\"\u0359\n\"\f\"\16\"\u035c")
        buf.write("\13\"\3\"\3\"\3\"\7\"\u0361\n\"\f\"\16\"\u0364\13\"\3")
        buf.write("\"\3\"\5\"\u0368\n\"\7\"\u036a\n\"\f\"\16\"\u036d\13\"")
        buf.write("\3\"\7\"\u0370\n\"\f\"\16\"\u0373\13\"\3\"\5\"\u0376\n")
        buf.write("\"\3#\3#\3$\3$\7$\u037c\n$\f$\16$\u037f\13$\3$\3$\7$\u0383")
        buf.write("\n$\f$\16$\u0386\13$\3$\3$\3$\7$\u038b\n$\f$\16$\u038e")
        buf.write("\13$\3$\3$\3$\7$\u0393\n$\f$\16$\u0396\13$\3$\3$\5$\u039a")
        buf.write("\n$\7$\u039c\n$\f$\16$\u039f\13$\5$\u03a1\n$\3$\7$\u03a4")
        buf.write("\n$\f$\16$\u03a7\13$\3$\3$\7$\u03ab\n$\f$\16$\u03ae\13")
        buf.write("$\3%\3%\3%\3&\3&\3&\3&\6&\u03b7\n&\r&\16&\u03b8\3\'\3")
        buf.write("\'\3\'\3\'\6\'\u03bf\n\'\r\'\16\'\u03c0\3(\3(\3(\3(\6")
        buf.write("(\u03c7\n(\r(\16(\u03c8\3)\7)\u03cc\n)\f)\16)\u03cf\13")
        buf.write(")\3)\3)\3)\3)\3*\3*\3+\3+\3+\3+\5+\u03db\n+\3,\3,\3,\3")
        buf.write(",\3-\3-\3.\3.\3.\3.\3.\3.\3.\5.\u03ea\n.\3.\3.\3/\3/\3")
        buf.write("\60\3\60\3\60\5\60\u03f3\n\60\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\62\3\62\3\62\7\62\u03fd\n\62\f\62\16\62\u0400\13\62")
        buf.write("\3\63\3\63\5\63\u0404\n\63\3\63\7\63\u0407\n\63\f\63\16")
        buf.write("\63\u040a\13\63\3\63\7\63\u040d\n\63\f\63\16\63\u0410")
        buf.write("\13\63\3\63\7\63\u0413\n\63\f\63\16\63\u0416\13\63\3\63")
        buf.write("\7\63\u0419\n\63\f\63\16\63\u041c\13\63\3\63\7\63\u041f")
        buf.write("\n\63\f\63\16\63\u0422\13\63\3\64\3\64\3\64\6\64\u0427")
        buf.write("\n\64\r\64\16\64\u0428\3\64\5\64\u042c\n\64\3\65\3\65")
        buf.write("\5\65\u0430\n\65\3\65\3\65\5\65\u0434\n\65\3\65\3\65\3")
        buf.write("\65\3\66\3\66\3\66\3\66\6\66\u043d\n\66\r\66\16\66\u043e")
        buf.write("\3\67\3\67\3\67\3\67\5\67\u0445\n\67\38\38\38\58\u044a")
        buf.write("\n8\39\39\39\39\39\59\u0451\n9\3:\3:\3;\7;\u0456\n;\f")
        buf.write(";\16;\u0459\13;\3;\3;\5;\u045d\n;\3;\5;\u0460\n;\3;\5")
        buf.write(";\u0463\n;\3;\6;\u0466\n;\r;\16;\u0467\3;\5;\u046b\n;")
        buf.write("\3<\3<\5<\u046f\n<\3<\3<\3<\5<\u0474\n<\3<\3<\3<\5<\u0479")
        buf.write("\n<\3=\3=\3>\5>\u047e\n>\3>\3>\3?\3?\3?\3@\3@\3A\3A\3")
        buf.write("A\3B\3B\3C\3C\3D\6D\u048f\nD\rD\16D\u0490\3D\3D\5D\u0495")
        buf.write("\nD\3E\3E\3E\3F\3F\3F\3G\3G\3H\3H\3I\3I\3I\3I\3I\3I\3")
        buf.write("I\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\5I\u04b3\nI\3J\3J\3")
        buf.write("K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3P\3P\3Q\3Q\3R\3R\3S\3S\3")
        buf.write("T\3T\3U\3U\3V\3V\3V\3V\3V\5V\u04d2\nV\3V\3V\5V\u04d6\n")
        buf.write("V\3W\3W\3X\3X\3X\3X\3X\7X\u04df\nX\fX\16X\u04e2\13X\3")
        buf.write("Y\5Y\u04e5\nY\3Y\3Y\3Z\3Z\3Z\5Z\u04ec\nZ\3[\3[\3[\3\\")
        buf.write("\3\\\3\\\3\\\3\\\5\\\u04f6\n\\\3]\3]\3]\3]\3]\7]\u04fd")
        buf.write("\n]\f]\16]\u0500\13]\3^\5^\u0503\n^\3^\3^\3_\3_\3_\5_")
        buf.write("\u050a\n_\3`\3`\3`\3a\3a\3a\3a\3a\3b\3b\3b\7b\u0517\n")
        buf.write("b\fb\16b\u051a\13b\3c\3c\3d\3d\3d\3d\3d\5d\u0523\nd\3")
        buf.write("e\3e\3f\3f\3f\3f\3f\5f\u052c\nf\3g\3g\3h\3h\3h\7h\u0533")
        buf.write("\nh\fh\16h\u0536\13h\3i\3i\3i\3i\3j\3j\3k\3k\3k\3l\7l")
        buf.write("\u0542\nl\fl\16l\u0545\13l\3m\3m\3m\3n\3n\3n\5n\u054d")
        buf.write("\nn\3n\3n\5n\u0551\nn\3n\5n\u0554\nn\3n\3n\3o\3o\3p\3")
        buf.write("p\3q\3q\3r\3r\3s\3s\3s\3s\3t\3t\3t\3t\3t\3t\3t\3t\3t\3")
        buf.write("t\3t\3t\3t\3t\3t\5t\u0573\nt\3u\3u\3u\3u\3u\3u\3u\3u\3")
        buf.write("u\3u\3u\3u\3u\3u\7u\u0583\nu\fu\16u\u0586\13u\3u\7u\u0589")
        buf.write("\nu\fu\16u\u058c\13u\3u\5u\u058f\nu\3u\7u\u0592\nu\fu")
        buf.write("\16u\u0595\13u\3v\3v\3v\7v\u059a\nv\fv\16v\u059d\13v\3")
        buf.write("v\3v\3v\7v\u05a2\nv\fv\16v\u05a5\13v\3v\7v\u05a8\nv\f")
        buf.write("v\16v\u05ab\13v\3w\3w\3w\3w\3w\7w\u05b2\nw\fw\16w\u05b5")
        buf.write("\13w\3x\3x\3y\3y\3z\3z\3z\3z\3z\7z\u05c0\nz\fz\16z\u05c3")
        buf.write("\13z\3{\3{\3{\3{\3{\3{\3{\7{\u05cc\n{\f{\16{\u05cf\13")
        buf.write("{\3{\5{\u05d2\n{\3|\3|\3}\3}\3}\3}\3~\3~\3~\3~\3\177\3")
        buf.write("\177\3\177\3\177\3\u0080\3\u0080\3\u0080\3\u0080\3\u0080")
        buf.write("\7\u0080\u05e7\n\u0080\f\u0080\16\u0080\u05ea\13\u0080")
        buf.write("\3\u0081\3\u0081\5\u0081\u05ee\n\u0081\3\u0081\3\u0081")
        buf.write("\3\u0081\3\u0081\3\u0082\3\u0082\3\u0083\3\u0083\3\u0084")
        buf.write("\3\u0084\3\u0084\3\u0084\7\u0084\u05fc\n\u0084\f\u0084")
        buf.write("\16\u0084\u05ff\13\u0084\3\u0085\3\u0085\3\u0085\3\u0085")
        buf.write("\7\u0085\u0605\n\u0085\f\u0085\16\u0085\u0608\13\u0085")
        buf.write("\3\u0086\3\u0086\3\u0086\3\u0086\7\u0086\u060e\n\u0086")
        buf.write("\f\u0086\16\u0086\u0611\13\u0086\3\u0087\3\u0087\3\u0087")
        buf.write("\3\u0087\7\u0087\u0617\n\u0087\f\u0087\16\u0087\u061a")
        buf.write("\13\u0087\3\u0088\3\u0088\3\u0088\3\u0088\7\u0088\u0620")
        buf.write("\n\u0088\f\u0088\16\u0088\u0623\13\u0088\3\u0089\3\u0089")
        buf.write("\3\u0089\3\u0089\7\u0089\u0629\n\u0089\f\u0089\16\u0089")
        buf.write("\u062c\13\u0089\3\u008a\3\u008a\3\u008a\3\u008a\3\u008a")
        buf.write("\3\u008a\7\u008a\u0634\n\u008a\f\u008a\16\u008a\u0637")
        buf.write("\13\u008a\5\u008a\u0639\n\u008a\3\u008a\3\u008a\5\u008a")
        buf.write("\u063d\n\u008a\3\u008b\3\u008b\3\u008c\3\u008c\3\u008d")
        buf.write("\3\u008d\3\u008d\5\u008d\u0646\n\u008d\3\u008d\3\u008d")
        buf.write("\3\u008d\3\u008d\5\u008d\u064c\n\u008d\3\u008e\3\u008e")
        buf.write("\3\u008e\3\u008e\7\u008e\u0652\n\u008e\f\u008e\16\u008e")
        buf.write("\u0655\13\u008e\3\u008f\3\u008f\3\u008f\3\u008f\3\u008f")
        buf.write("\3\u008f\3\u008f\3\u008f\3\u008f\3\u008f\3\u008f\3\u008f")
        buf.write("\7\u008f\u0663\n\u008f\f\u008f\16\u008f\u0666\13\u008f")
        buf.write("\3\u0090\3\u0090\3\u0091\3\u0091\3\u0091\3\u0091\7\u0091")
        buf.write("\u066e\n\u0091\f\u0091\16\u0091\u0671\13\u0091\3\u0092")
        buf.write("\3\u0092\3\u0092\7\u0092\u0676\n\u0092\f\u0092\16\u0092")
        buf.write("\u0679\13\u0092\3\u0093\3\u0093\5\u0093\u067d\n\u0093")
        buf.write("\3\u0093\3\u0093\7\u0093\u0681\n\u0093\f\u0093\16\u0093")
        buf.write("\u0684\13\u0093\3\u0094\3\u0094\5\u0094\u0688\n\u0094")
        buf.write("\3\u0094\3\u0094\7\u0094\u068c\n\u0094\f\u0094\16\u0094")
        buf.write("\u068f\13\u0094\3\u0095\3\u0095\5\u0095\u0693\n\u0095")
        buf.write("\3\u0095\3\u0095\7\u0095\u0697\n\u0095\f\u0095\16\u0095")
        buf.write("\u069a\13\u0095\3\u0096\3\u0096\3\u0096\3\u0096\7\u0096")
        buf.write("\u06a0\n\u0096\f\u0096\16\u0096\u06a3\13\u0096\3\u0097")
        buf.write("\3\u0097\3\u0097\3\u0097\7\u0097\u06a9\n\u0097\f\u0097")
        buf.write("\16\u0097\u06ac\13\u0097\3\u0098\3\u0098\3\u0098\3\u0098")
        buf.write("\5\u0098\u06b2\n\u0098\3\u0098\7\u0098\u06b5\n\u0098\f")
        buf.write("\u0098\16\u0098\u06b8\13\u0098\3\u0099\3\u0099\3\u009a")
        buf.write("\3\u009a\3\u009a\3\u009a\3\u009a\7\u009a\u06c1\n\u009a")
        buf.write("\f\u009a\16\u009a\u06c4\13\u009a\3\u009a\3\u009a\3\u009b")
        buf.write("\3\u009b\3\u009b\3\u009b\5\u009b\u06cc\n\u009b\3\u009c")
        buf.write("\3\u009c\3\u009d\3\u009d\3\u009e\3\u009e\3\u009e\3\u009e")
        buf.write("\7\u009e\u06d6\n\u009e\f\u009e\16\u009e\u06d9\13\u009e")
        buf.write("\3\u009f\3\u009f\3\u009f\3\u009f\5\u009f\u06df\n\u009f")
        buf.write("\3\u00a0\3\u00a0\3\u00a1\3\u00a1\3\u00a2\3\u00a2\3\u00a2")
        buf.write("\3\u00a2\3\u00a2\6\u00a2\u06ea\n\u00a2\r\u00a2\16\u00a2")
        buf.write("\u06eb\3\u00a3\3\u00a3\3\u00a3\3\u00a3\3\u00a3\3\u00a4")
        buf.write("\3\u00a4\3\u00a5\3\u00a5\3\u00a5\3\u00a5\3\u00a5\3\u00a6")
        buf.write("\3\u00a6\3\u00a6\7\u00a6\u06fd\n\u00a6\f\u00a6\16\u00a6")
        buf.write("\u0700\13\u00a6\3\u00a7\3\u00a7\3\u00a7\3\u00a8\3\u00a8")
        buf.write("\3\u00a8\3\u00a9\3\u00a9\3\u00a9\3\u00a9\3\u00a9\5\u00a9")
        buf.write("\u070d\n\u00a9\3\u00aa\3\u00aa\3\u00ab\3\u00ab\3\u00ab")
        buf.write("\3\u00ab\3\u00ab\3\u00ac\3\u00ac\3\u00ac\3\u00ac\3\u00ac")
        buf.write("\3\u00ad\3\u00ad\3\u00ae\3\u00ae\3\u00ae\3\u00af\3\u00af")
        buf.write("\3\u00af\3\u00b0\3\u00b0\3\u00b0\3\u00b1\3\u00b1\3\u00b1")
        buf.write("\3\u00b2\3\u00b2\3\u00b2\3\u00b2\3\u00b2\3\u00b3\3\u00b3")
        buf.write("\3\u00b4\3\u00b4\7\u00b4\u0732\n\u00b4\f\u00b4\16\u00b4")
        buf.write("\u0735\13\u00b4\3\u00b4\3\u00b4\7\u00b4\u0739\n\u00b4")
        buf.write("\f\u00b4\16\u00b4\u073c\13\u00b4\3\u00b5\3\u00b5\5\u00b5")
        buf.write("\u0740\n\u00b5\3\u00b5\3\u00b5\5\u00b5\u0744\n\u00b5\3")
        buf.write("\u00b5\3\u00b5\5\u00b5\u0748\n\u00b5\3\u00b5\3\u00b5\5")
        buf.write("\u00b5\u074c\n\u00b5\5\u00b5\u074e\n\u00b5\3\u00b5\3\u00b5")
        buf.write("\5\u00b5\u0752\n\u00b5\3\u00b6\3\u00b6\3\u00b6\5\u00b6")
        buf.write("\u0757\n\u00b6\3\u00b6\3\u00b6\3\u00b6\3\u00b6\3\u00b7")
        buf.write("\3\u00b7\3\u00b7\3\u00b8\3\u00b8\3\u00b9\3\u00b9\5\u00b9")
        buf.write("\u0764\n\u00b9\3\u00ba\3\u00ba\3\u00ba\7\u00ba\u0769\n")
        buf.write("\u00ba\f\u00ba\16\u00ba\u076c\13\u00ba\3\u00bb\3\u00bb")
        buf.write("\3\u00bb\3\u00bb\3\u00bb\6\u00bb\u0773\n\u00bb\r\u00bb")
        buf.write("\16\u00bb\u0774\3\u00bc\5\u00bc\u0778\n\u00bc\3\u00bc")
        buf.write("\3\u00bc\3\u00bd\3\u00bd\3\u00bd\6\u00bd\u077f\n\u00bd")
        buf.write("\r\u00bd\16\u00bd\u0780\3\u00be\3\u00be\3\u00be\3\u00be")
        buf.write("\3\u00bf\3\u00bf\5\u00bf\u0789\n\u00bf\3\u00c0\3\u00c0")
        buf.write("\3\u00c0\6\u00c0\u078e\n\u00c0\r\u00c0\16\u00c0\u078f")
        buf.write("\3\u00c0\5\u00c0\u0793\n\u00c0\5\u00c0\u0795\n\u00c0\3")
        buf.write("\u00c1\3\u00c1\3\u00c2\7\u00c2\u079a\n\u00c2\f\u00c2\16")
        buf.write("\u00c2\u079d\13\u00c2\3\u00c2\7\u00c2\u07a0\n\u00c2\f")
        buf.write("\u00c2\16\u00c2\u07a3\13\u00c2\3\u00c2\5\u00c2\u07a6\n")
        buf.write("\u00c2\3\u00c2\7\u00c2\u07a9\n\u00c2\f\u00c2\16\u00c2")
        buf.write("\u07ac\13\u00c2\3\u00c2\7\u00c2\u07af\n\u00c2\f\u00c2")
        buf.write("\16\u00c2\u07b2\13\u00c2\3\u00c3\3\u00c3\3\u00c4\3\u00c4")
        buf.write("\3\u00c4\3\u00c4\6\u00c4\u07ba\n\u00c4\r\u00c4\16\u00c4")
        buf.write("\u07bb\3\u00c4\5\u00c4\u07bf\n\u00c4\3\u00c5\3\u00c5\3")
        buf.write("\u00c6\3\u00c6\3\u00c7\3\u00c7\3\u00c7\5\u00c7\u07c8\n")
        buf.write("\u00c7\3\u00c7\3\u00c7\5\u00c7\u07cc\n\u00c7\3\u00c7\6")
        buf.write("\u00c7\u07cf\n\u00c7\r\u00c7\16\u00c7\u07d0\3\u00c7\5")
        buf.write("\u00c7\u07d4\n\u00c7\3\u00c8\3\u00c8\3\u00c9\3\u00c9\3")
        buf.write("\u00c9\7\u00c9\u07db\n\u00c9\f\u00c9\16\u00c9\u07de\13")
        buf.write("\u00c9\3\u00ca\3\u00ca\3\u00ca\3\u00ca\3\u00ca\3\u00ca")
        buf.write("\3\u00ca\3\u00ca\3\u00ca\3\u00ca\3\u00ca\3\u00ca\3\u00ca")
        buf.write("\3\u00ca\3\u00ca\3\u00ca\3\u00ca\3\u00ca\5\u00ca\u07f2")
        buf.write("\n\u00ca\3\u00cb\3\u00cb\3\u00cb\3\u00cb\6\u00cb\u07f8")
        buf.write("\n\u00cb\r\u00cb\16\u00cb\u07f9\3\u00cb\3\u00cb\3\u00cc")
        buf.write("\3\u00cc\5\u00cc\u0800\n\u00cc\3\u00cc\5\u00cc\u0803\n")
        buf.write("\u00cc\3\u00cc\5\u00cc\u0806\n\u00cc\3\u00cc\5\u00cc\u0809")
        buf.write("\n\u00cc\3\u00cd\3\u00cd\5\u00cd\u080d\n\u00cd\3\u00ce")
        buf.write("\3\u00ce\3\u00cf\3\u00cf\3\u00cf\3\u00cf\3\u00cf\3\u00cf")
        buf.write("\7\u00cf\u0817\n\u00cf\f\u00cf\16\u00cf\u081a\13\u00cf")
        buf.write("\5\u00cf\u081c\n\u00cf\3\u00d0\3\u00d0\3\u00d1\3\u00d1")
        buf.write("\3\u00d1\5\u00d1\u0823\n\u00d1\3\u00d1\5\u00d1\u0826\n")
        buf.write("\u00d1\3\u00d2\3\u00d2\3\u00d2\3\u00d2\3\u00d3\3\u00d3")
        buf.write("\3\u00d3\5\u00d3\u082f\n\u00d3\3\u00d3\3\u00d3\3\u00d4")
        buf.write("\3\u00d4\3\u00d5\3\u00d5\3\u00d6\3\u00d6\3\u00d6\5\u00d6")
        buf.write("\u083a\n\u00d6\3\u00d6\3\u00d6\3\u00d7\3\u00d7\3\u00d8")
        buf.write("\3\u00d8\3\u00d8\5\u00d8\u0843\n\u00d8\3\u00d8\3\u00d8")
        buf.write("\3\u00d9\3\u00d9\3\u00da\3\u00da\3\u00da\3\u00db\3\u00db")
        buf.write("\3\u00db\3\u00dc\3\u00dc\5\u00dc\u0851\n\u00dc\3\u00dc")
        buf.write("\3\u00dc\7\u00dc\u0855\n\u00dc\f\u00dc\16\u00dc\u0858")
        buf.write("\13\u00dc\3\u00dc\3\u00dc\5\u00dc\u085c\n\u00dc\3\u00dc")
        buf.write("\3\u00dc\3\u00dc\3\u00dc\3\u00dc\3\u00dc\3\u00dc\3\u00dc")
        buf.write("\3\u00dc\3\u00dc\3\u00dc\3\u00dc\3\u00dc\3\u00dc\3\u00dc")
        buf.write("\7\u00dc\u086d\n\u00dc\f\u00dc\16\u00dc\u0870\13\u00dc")
        buf.write("\3\u00dc\7\u00dc\u0873\n\u00dc\f\u00dc\16\u00dc\u0876")
        buf.write("\13\u00dc\3\u00dc\3\u00dc\5\u00dc\u087a\n\u00dc\3\u00dc")
        buf.write("\7\u00dc\u087d\n\u00dc\f\u00dc\16\u00dc\u0880\13\u00dc")
        buf.write("\3\u00dc\7\u00dc\u0883\n\u00dc\f\u00dc\16\u00dc\u0886")
        buf.write("\13\u00dc\3\u00dc\7\u00dc\u0889\n\u00dc\f\u00dc\16\u00dc")
        buf.write("\u088c\13\u00dc\3\u00dc\3\u00dc\3\u00dd\3\u00dd\7\u00dd")
        buf.write("\u0892\n\u00dd\f\u00dd\16\u00dd\u0895\13\u00dd\3\u00dd")
        buf.write("\3\u00dd\7\u00dd\u0899\n\u00dd\f\u00dd\16\u00dd\u089c")
        buf.write("\13\u00dd\3\u00dd\3\u00dd\7\u00dd\u08a0\n\u00dd\f\u00dd")
        buf.write("\16\u00dd\u08a3\13\u00dd\3\u00dd\3\u00dd\7\u00dd\u08a7")
        buf.write("\n\u00dd\f\u00dd\16\u00dd\u08aa\13\u00dd\3\u00de\3\u00de")
        buf.write("\3\u00df\3\u00df\3\u00df\3\u00df\5\u00df\u08b2\n\u00df")
        buf.write("\3\u00df\3\u00df\3\u00df\3\u00df\3\u00e0\3\u00e0\3\u00e1")
        buf.write("\3\u00e1\3\u00e1\3\u00e1\5\u00e1\u08be\n\u00e1\3\u00e1")
        buf.write("\3\u00e1\3\u00e1\3\u00e1\3\u00e2\3\u00e2\3\u00e3\3\u00e3")
        buf.write("\5\u00e3\u08c8\n\u00e3\3\u00e4\3\u00e4\3\u00e5\3\u00e5")
        buf.write("\3\u00e5\3\u00e5\3\u00e6\3\u00e6\3\u00e6\3\u00e6\3\u00e7")
        buf.write("\3\u00e7\3\u00e8\3\u00e8\3\u00e8\3\u00e8\3\u00e9\3\u00e9")
        buf.write("\3\u00ea\3\u00ea\3\u00ea\3\u00ea\3\u00eb\3\u00eb\3\u00eb")
        buf.write("\3\u00eb\5\u00eb\u08e4\n\u00eb\3\u00ec\3\u00ec\3\u00ec")
        buf.write("\3\u00ec\5\u00ec\u08ea\n\u00ec\3\u00ed\3\u00ed\3\u00ed")
        buf.write("\3\u00ed\3\u00ee\3\u00ee\3\u00ee\3\u00ee\3\u00ef\3\u00ef")
        buf.write("\3\u00ef\3\u00ef\3\u00f0\3\u00f0\3\u00f0\7\u00f0\u08fb")
        buf.write("\n\u00f0\f\u00f0\16\u00f0\u08fe\13\u00f0\3\u00f1\3\u00f1")
        buf.write("\3\u00f2\3\u00f2\3\u00f2\3\u00f2\3\u00f3\3\u00f3\3\u00f3")
        buf.write("\3\u00f3\3\u00f4\3\u00f4\3\u00f5\3\u00f5\3\u00f5\3\u00f5")
        buf.write("\3\u00f6\3\u00f6\3\u00f7\3\u00f7\3\u00f7\7\u00f7\u0915")
        buf.write("\n\u00f7\f\u00f7\16\u00f7\u0918\13\u00f7\3\u00f8\3\u00f8")
        buf.write("\5\u00f8\u091c\n\u00f8\3\u00f9\3\u00f9\5\u00f9\u0920\n")
        buf.write("\u00f9\3\u00f9\5\u00f9\u0923\n\u00f9\3\u00fa\3\u00fa\3")
        buf.write("\u00fb\3\u00fb\3\u00fb\3\u00fb\3\u00fc\3\u00fc\3\u00fc")
        buf.write("\7\u00fc\u092e\n\u00fc\f\u00fc\16\u00fc\u0931\13\u00fc")
        buf.write("\3\u00fd\3\u00fd\3\u00fe\3\u00fe\5\u00fe\u0937\n\u00fe")
        buf.write("\3\u00fe\5\u00fe\u093a\n\u00fe\3\u00ff\3\u00ff\5\u00ff")
        buf.write("\u093e\n\u00ff\3\u0100\3\u0100\5\u0100\u0942\n\u0100\3")
        buf.write("\u0101\3\u0101\3\u0101\3\u0102\3\u0102\3\u0102\3\u0103")
        buf.write("\3\u0103\3\u0103\3\u0104\3\u0104\3\u0104\3\u0104\3\u0104")
        buf.write("\7\u0104\u0952\n\u0104\f\u0104\16\u0104\u0955\13\u0104")
        buf.write("\3\u0104\6\u0104\u0958\n\u0104\r\u0104\16\u0104\u0959")
        buf.write("\3\u0104\7\u0104\u095d\n\u0104\f\u0104\16\u0104\u0960")
        buf.write("\13\u0104\3\u0104\3\u0104\3\u0105\3\u0105\3\u0106\5\u0106")
        buf.write("\u0967\n\u0106\3\u0106\7\u0106\u096a\n\u0106\f\u0106\16")
        buf.write("\u0106\u096d\13\u0106\3\u0106\5\u0106\u0970\n\u0106\3")
        buf.write("\u0106\3\u0106\3\u0106\5\u0106\u0975\n\u0106\3\u0106\7")
        buf.write("\u0106\u0978\n\u0106\f\u0106\16\u0106\u097b\13\u0106\3")
        buf.write("\u0107\3\u0107\3\u0107\5\u0107\u0980\n\u0107\3\u0108\3")
        buf.write("\u0108\3\u0109\3\u0109\3\u0109\3\u0109\7\u0109\u0988\n")
        buf.write("\u0109\f\u0109\16\u0109\u098b\13\u0109\3\u0109\3\u0109")
        buf.write("\3\u010a\3\u010a\3\u010a\3\u010a\3\u010b\3\u010b\3\u010c")
        buf.write("\3\u010c\3\u010c\5\u010c\u0998\n\u010c\3\u010d\3\u010d")
        buf.write("\3\u010e\3\u010e\3\u010e\3\u010e\3\u010e\3\u010f\3\u010f")
        buf.write("\3\u010f\5\u010f\u09a4\n\u010f\3\u010f\3\u010f\3\u0110")
        buf.write("\3\u0110\3\u0110\5\u0110\u09ab\n\u0110\3\u0111\3\u0111")
        buf.write("\3\u0111\3\u0112\3\u0112\3\u0113\3\u0113\3\u0114\3\u0114")
        buf.write("\3\u0114\3\u0114\3\u0114\3\u0115\3\u0115\3\u0115\2\2\u0116")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082")
        buf.write("\u0084\u0086\u0088\u008a\u008c\u008e\u0090\u0092\u0094")
        buf.write("\u0096\u0098\u009a\u009c\u009e\u00a0\u00a2\u00a4\u00a6")
        buf.write("\u00a8\u00aa\u00ac\u00ae\u00b0\u00b2\u00b4\u00b6\u00b8")
        buf.write("\u00ba\u00bc\u00be\u00c0\u00c2\u00c4\u00c6\u00c8\u00ca")
        buf.write("\u00cc\u00ce\u00d0\u00d2\u00d4\u00d6\u00d8\u00da\u00dc")
        buf.write("\u00de\u00e0\u00e2\u00e4\u00e6\u00e8\u00ea\u00ec\u00ee")
        buf.write("\u00f0\u00f2\u00f4\u00f6\u00f8\u00fa\u00fc\u00fe\u0100")
        buf.write("\u0102\u0104\u0106\u0108\u010a\u010c\u010e\u0110\u0112")
        buf.write("\u0114\u0116\u0118\u011a\u011c\u011e\u0120\u0122\u0124")
        buf.write("\u0126\u0128\u012a\u012c\u012e\u0130\u0132\u0134\u0136")
        buf.write("\u0138\u013a\u013c\u013e\u0140\u0142\u0144\u0146\u0148")
        buf.write("\u014a\u014c\u014e\u0150\u0152\u0154\u0156\u0158\u015a")
        buf.write("\u015c\u015e\u0160\u0162\u0164\u0166\u0168\u016a\u016c")
        buf.write("\u016e\u0170\u0172\u0174\u0176\u0178\u017a\u017c\u017e")
        buf.write("\u0180\u0182\u0184\u0186\u0188\u018a\u018c\u018e\u0190")
        buf.write("\u0192\u0194\u0196\u0198\u019a\u019c\u019e\u01a0\u01a2")
        buf.write("\u01a4\u01a6\u01a8\u01aa\u01ac\u01ae\u01b0\u01b2\u01b4")
        buf.write("\u01b6\u01b8\u01ba\u01bc\u01be\u01c0\u01c2\u01c4\u01c6")
        buf.write("\u01c8\u01ca\u01cc\u01ce\u01d0\u01d2\u01d4\u01d6\u01d8")
        buf.write("\u01da\u01dc\u01de\u01e0\u01e2\u01e4\u01e6\u01e8\u01ea")
        buf.write("\u01ec\u01ee\u01f0\u01f2\u01f4\u01f6\u01f8\u01fa\u01fc")
        buf.write("\u01fe\u0200\u0202\u0204\u0206\u0208\u020a\u020c\u020e")
        buf.write("\u0210\u0212\u0214\u0216\u0218\u021a\u021c\u021e\u0220")
        buf.write("\u0222\u0224\u0226\u0228\2\21\5\2\3\4\6\6/x\3\2\37 \4")
        buf.write("\2\30\30\35\35\3\2\37\37\3\2&\'\3\2\30\35\4\2\7\7\21\21")
        buf.write("\5\2;;==@@\3\2EG\4\2\33\33\35\35\4\2\23\23\35\35\4\2\25")
        buf.write("\25\31\31\3\2\u0094\u0096\3\2Z\\\4\2Z]ss\2\u0a1c\2\u022d")
        buf.write("\3\2\2\2\4\u025f\3\2\2\2\6\u0264\3\2\2\2\b\u0268\3\2\2")
        buf.write("\2\n\u026a\3\2\2\2\f\u026e\3\2\2\2\16\u0278\3\2\2\2\20")
        buf.write("\u027c\3\2\2\2\22\u028a\3\2\2\2\24\u028c\3\2\2\2\26\u028e")
        buf.write("\3\2\2\2\30\u0290\3\2\2\2\32\u0292\3\2\2\2\34\u0294\3")
        buf.write("\2\2\2\36\u029c\3\2\2\2 \u02bb\3\2\2\2\"\u02be\3\2\2\2")
        buf.write("$\u02c4\3\2\2\2&\u02ca\3\2\2\2(\u02cc\3\2\2\2*\u02d0\3")
        buf.write("\2\2\2,\u02dc\3\2\2\2.\u02de\3\2\2\2\60\u02e5\3\2\2\2")
        buf.write("\62\u02e7\3\2\2\2\64\u02ec\3\2\2\2\66\u02f1\3\2\2\28\u02f6")
        buf.write("\3\2\2\2:\u02fb\3\2\2\2<\u0319\3\2\2\2>\u031b\3\2\2\2")
        buf.write("@\u033d\3\2\2\2B\u035a\3\2\2\2D\u0377\3\2\2\2F\u0379\3")
        buf.write("\2\2\2H\u03af\3\2\2\2J\u03b6\3\2\2\2L\u03be\3\2\2\2N\u03c6")
        buf.write("\3\2\2\2P\u03cd\3\2\2\2R\u03d4\3\2\2\2T\u03da\3\2\2\2")
        buf.write("V\u03dc\3\2\2\2X\u03e0\3\2\2\2Z\u03e2\3\2\2\2\\\u03ed")
        buf.write("\3\2\2\2^\u03f2\3\2\2\2`\u03f4\3\2\2\2b\u03f9\3\2\2\2")
        buf.write("d\u0401\3\2\2\2f\u0423\3\2\2\2h\u042d\3\2\2\2j\u0438\3")
        buf.write("\2\2\2l\u0440\3\2\2\2n\u0449\3\2\2\2p\u044b\3\2\2\2r\u0452")
        buf.write("\3\2\2\2t\u0457\3\2\2\2v\u0478\3\2\2\2x\u047a\3\2\2\2")
        buf.write("z\u047d\3\2\2\2|\u0481\3\2\2\2~\u0484\3\2\2\2\u0080\u0486")
        buf.write("\3\2\2\2\u0082\u0489\3\2\2\2\u0084\u048b\3\2\2\2\u0086")
        buf.write("\u0494\3\2\2\2\u0088\u0496\3\2\2\2\u008a\u0499\3\2\2\2")
        buf.write("\u008c\u049c\3\2\2\2\u008e\u049e\3\2\2\2\u0090\u04b2\3")
        buf.write("\2\2\2\u0092\u04b4\3\2\2\2\u0094\u04b6\3\2\2\2\u0096\u04b8")
        buf.write("\3\2\2\2\u0098\u04ba\3\2\2\2\u009a\u04bc\3\2\2\2\u009c")
        buf.write("\u04be\3\2\2\2\u009e\u04c0\3\2\2\2\u00a0\u04c2\3\2\2\2")
        buf.write("\u00a2\u04c4\3\2\2\2\u00a4\u04c6\3\2\2\2\u00a6\u04c8\3")
        buf.write("\2\2\2\u00a8\u04ca\3\2\2\2\u00aa\u04cc\3\2\2\2\u00ac\u04d7")
        buf.write("\3\2\2\2\u00ae\u04d9\3\2\2\2\u00b0\u04e4\3\2\2\2\u00b2")
        buf.write("\u04eb\3\2\2\2\u00b4\u04ed\3\2\2\2\u00b6\u04f0\3\2\2\2")
        buf.write("\u00b8\u04f7\3\2\2\2\u00ba\u0502\3\2\2\2\u00bc\u0509\3")
        buf.write("\2\2\2\u00be\u050b\3\2\2\2\u00c0\u050e\3\2\2\2\u00c2\u0513")
        buf.write("\3\2\2\2\u00c4\u051b\3\2\2\2\u00c6\u051d\3\2\2\2\u00c8")
        buf.write("\u0524\3\2\2\2\u00ca\u0526\3\2\2\2\u00cc\u052d\3\2\2\2")
        buf.write("\u00ce\u052f\3\2\2\2\u00d0\u0537\3\2\2\2\u00d2\u053b\3")
        buf.write("\2\2\2\u00d4\u053d\3\2\2\2\u00d6\u0543\3\2\2\2\u00d8\u0546")
        buf.write("\3\2\2\2\u00da\u0549\3\2\2\2\u00dc\u0557\3\2\2\2\u00de")
        buf.write("\u0559\3\2\2\2\u00e0\u055b\3\2\2\2\u00e2\u055d\3\2\2\2")
        buf.write("\u00e4\u055f\3\2\2\2\u00e6\u0572\3\2\2\2\u00e8\u0574\3")
        buf.write("\2\2\2\u00ea\u0596\3\2\2\2\u00ec\u05ac\3\2\2\2\u00ee\u05b6")
        buf.write("\3\2\2\2\u00f0\u05b8\3\2\2\2\u00f2\u05ba\3\2\2\2\u00f4")
        buf.write("\u05c4\3\2\2\2\u00f6\u05d3\3\2\2\2\u00f8\u05d5\3\2\2\2")
        buf.write("\u00fa\u05d9\3\2\2\2\u00fc\u05dd\3\2\2\2\u00fe\u05e1\3")
        buf.write("\2\2\2\u0100\u05eb\3\2\2\2\u0102\u05f3\3\2\2\2\u0104\u05f5")
        buf.write("\3\2\2\2\u0106\u05f7\3\2\2\2\u0108\u0600\3\2\2\2\u010a")
        buf.write("\u0609\3\2\2\2\u010c\u0612\3\2\2\2\u010e\u061b\3\2\2\2")
        buf.write("\u0110\u0624\3\2\2\2\u0112\u062d\3\2\2\2\u0114\u063e\3")
        buf.write("\2\2\2\u0116\u0640\3\2\2\2\u0118\u0642\3\2\2\2\u011a\u064d")
        buf.write("\3\2\2\2\u011c\u0664\3\2\2\2\u011e\u0667\3\2\2\2\u0120")
        buf.write("\u0669\3\2\2\2\u0122\u0672\3\2\2\2\u0124\u067a\3\2\2\2")
        buf.write("\u0126\u0685\3\2\2\2\u0128\u0690\3\2\2\2\u012a\u069b\3")
        buf.write("\2\2\2\u012c\u06a4\3\2\2\2\u012e\u06ad\3\2\2\2\u0130\u06b9")
        buf.write("\3\2\2\2\u0132\u06bb\3\2\2\2\u0134\u06c7\3\2\2\2\u0136")
        buf.write("\u06cd\3\2\2\2\u0138\u06cf\3\2\2\2\u013a\u06d1\3\2\2\2")
        buf.write("\u013c\u06da\3\2\2\2\u013e\u06e0\3\2\2\2\u0140\u06e2\3")
        buf.write("\2\2\2\u0142\u06e4\3\2\2\2\u0144\u06ed\3\2\2\2\u0146\u06f2")
        buf.write("\3\2\2\2\u0148\u06f4\3\2\2\2\u014a\u06f9\3\2\2\2\u014c")
        buf.write("\u0701\3\2\2\2\u014e\u0704\3\2\2\2\u0150\u0707\3\2\2\2")
        buf.write("\u0152\u070e\3\2\2\2\u0154\u0710\3\2\2\2\u0156\u0715\3")
        buf.write("\2\2\2\u0158\u071a\3\2\2\2\u015a\u071c\3\2\2\2\u015c\u071f")
        buf.write("\3\2\2\2\u015e\u0722\3\2\2\2\u0160\u0725\3\2\2\2\u0162")
        buf.write("\u0728\3\2\2\2\u0164\u072d\3\2\2\2\u0166\u072f\3\2\2\2")
        buf.write("\u0168\u073d\3\2\2\2\u016a\u0756\3\2\2\2\u016c\u075c\3")
        buf.write("\2\2\2\u016e\u075f\3\2\2\2\u0170\u0763\3\2\2\2\u0172\u0765")
        buf.write("\3\2\2\2\u0174\u0772\3\2\2\2\u0176\u0777\3\2\2\2\u0178")
        buf.write("\u077e\3\2\2\2\u017a\u0782\3\2\2\2\u017c\u0788\3\2\2\2")
        buf.write("\u017e\u0794\3\2\2\2\u0180\u0796\3\2\2\2\u0182\u079b\3")
        buf.write("\2\2\2\u0184\u07b3\3\2\2\2\u0186\u07b5\3\2\2\2\u0188\u07c0")
        buf.write("\3\2\2\2\u018a\u07c2\3\2\2\2\u018c\u07c4\3\2\2\2\u018e")
        buf.write("\u07d5\3\2\2\2\u0190\u07d7\3\2\2\2\u0192\u07f1\3\2\2\2")
        buf.write("\u0194\u07f3\3\2\2\2\u0196\u07fd\3\2\2\2\u0198\u080c\3")
        buf.write("\2\2\2\u019a\u080e\3\2\2\2\u019c\u0810\3\2\2\2\u019e\u081d")
        buf.write("\3\2\2\2\u01a0\u081f\3\2\2\2\u01a2\u0827\3\2\2\2\u01a4")
        buf.write("\u082b\3\2\2\2\u01a6\u0832\3\2\2\2\u01a8\u0834\3\2\2\2")
        buf.write("\u01aa\u0836\3\2\2\2\u01ac\u083d\3\2\2\2\u01ae\u083f\3")
        buf.write("\2\2\2\u01b0\u0846\3\2\2\2\u01b2\u0848\3\2\2\2\u01b4\u084b")
        buf.write("\3\2\2\2\u01b6\u0850\3\2\2\2\u01b8\u088f\3\2\2\2\u01ba")
        buf.write("\u08ab\3\2\2\2\u01bc\u08b1\3\2\2\2\u01be\u08b7\3\2\2\2")
        buf.write("\u01c0\u08bd\3\2\2\2\u01c2\u08c3\3\2\2\2\u01c4\u08c7\3")
        buf.write("\2\2\2\u01c6\u08c9\3\2\2\2\u01c8\u08cb\3\2\2\2\u01ca\u08cf")
        buf.write("\3\2\2\2\u01cc\u08d3\3\2\2\2\u01ce\u08d5\3\2\2\2\u01d0")
        buf.write("\u08d9\3\2\2\2\u01d2\u08db\3\2\2\2\u01d4\u08df\3\2\2\2")
        buf.write("\u01d6\u08e5\3\2\2\2\u01d8\u08eb\3\2\2\2\u01da\u08ef\3")
        buf.write("\2\2\2\u01dc\u08f3\3\2\2\2\u01de\u08f7\3\2\2\2\u01e0\u08ff")
        buf.write("\3\2\2\2\u01e2\u0901\3\2\2\2\u01e4\u0905\3\2\2\2\u01e6")
        buf.write("\u0909\3\2\2\2\u01e8\u090b\3\2\2\2\u01ea\u090f\3\2\2\2")
        buf.write("\u01ec\u0911\3\2\2\2\u01ee\u0919\3\2\2\2\u01f0\u0922\3")
        buf.write("\2\2\2\u01f2\u0924\3\2\2\2\u01f4\u0926\3\2\2\2\u01f6\u092a")
        buf.write("\3\2\2\2\u01f8\u0932\3\2\2\2\u01fa\u0939\3\2\2\2\u01fc")
        buf.write("\u093b\3\2\2\2\u01fe\u093f\3\2\2\2\u0200\u0943\3\2\2\2")
        buf.write("\u0202\u0946\3\2\2\2\u0204\u0949\3\2\2\2\u0206\u094c\3")
        buf.write("\2\2\2\u0208\u0963\3\2\2\2\u020a\u0966\3\2\2\2\u020c\u097c")
        buf.write("\3\2\2\2\u020e\u0981\3\2\2\2\u0210\u0983\3\2\2\2\u0212")
        buf.write("\u098e\3\2\2\2\u0214\u0992\3\2\2\2\u0216\u0997\3\2\2\2")
        buf.write("\u0218\u0999\3\2\2\2\u021a\u099b\3\2\2\2\u021c\u09a3\3")
        buf.write("\2\2\2\u021e\u09aa\3\2\2\2\u0220\u09ac\3\2\2\2\u0222\u09af")
        buf.write("\3\2\2\2\u0224\u09b1\3\2\2\2\u0226\u09b3\3\2\2\2\u0228")
        buf.write("\u09b8\3\2\2\2\u022a\u022c\7\5\2\2\u022b\u022a\3\2\2\2")
        buf.write("\u022c\u022f\3\2\2\2\u022d\u022b\3\2\2\2\u022d\u022e\3")
        buf.write("\2\2\2\u022e\u0233\3\2\2\2\u022f\u022d\3\2\2\2\u0230\u0232")
        buf.write("\5,\27\2\u0231\u0230\3\2\2\2\u0232\u0235\3\2\2\2\u0233")
        buf.write("\u0231\3\2\2\2\u0233\u0234\3\2\2\2\u0234\u0239\3\2\2\2")
        buf.write("\u0235\u0233\3\2\2\2\u0236\u0238\7\5\2\2\u0237\u0236\3")
        buf.write("\2\2\2\u0238\u023b\3\2\2\2\u0239\u0237\3\2\2\2\u0239\u023a")
        buf.write("\3\2\2\2\u023a\u0244\3\2\2\2\u023b\u0239\3\2\2\2\u023c")
        buf.write("\u023e\5\4\3\2\u023d\u023c\3\2\2\2\u023d\u023e\3\2\2\2")
        buf.write("\u023e\u0240\3\2\2\2\u023f\u0241\5\u0166\u00b4\2\u0240")
        buf.write("\u023f\3\2\2\2\u0241\u0242\3\2\2\2\u0242\u0240\3\2\2\2")
        buf.write("\u0242\u0243\3\2\2\2\u0243\u0245\3\2\2\2\u0244\u023d\3")
        buf.write("\2\2\2\u0244\u0245\3\2\2\2\u0245\u0249\3\2\2\2\u0246\u0248")
        buf.write("\7\5\2\2\u0247\u0246\3\2\2\2\u0248\u024b\3\2\2\2\u0249")
        buf.write("\u0247\3\2\2\2\u0249\u024a\3\2\2\2\u024a\u0254\3\2\2\2")
        buf.write("\u024b\u0249\3\2\2\2\u024c\u024e\5\6\4\2\u024d\u024c\3")
        buf.write("\2\2\2\u024d\u024e\3\2\2\2\u024e\u0250\3\2\2\2\u024f\u0251")
        buf.write("\5d\63\2\u0250\u024f\3\2\2\2\u0251\u0252\3\2\2\2\u0252")
        buf.write("\u0250\3\2\2\2\u0252\u0253\3\2\2\2\u0253\u0255\3\2\2\2")
        buf.write("\u0254\u024d\3\2\2\2\u0254\u0255\3\2\2\2\u0255\u0259\3")
        buf.write("\2\2\2\u0256\u0258\7\5\2\2\u0257\u0256\3\2\2\2\u0258\u025b")
        buf.write("\3\2\2\2\u0259\u0257\3\2\2\2\u0259\u025a\3\2\2\2\u025a")
        buf.write("\u025c\3\2\2\2\u025b\u0259\3\2\2\2\u025c\u025d\7\2\2\3")
        buf.write("\u025d\3\3\2\2\2\u025e\u0260\5\b\5\2\u025f\u025e\3\2\2")
        buf.write("\2\u0260\u0261\3\2\2\2\u0261\u025f\3\2\2\2\u0261\u0262")
        buf.write("\3\2\2\2\u0262\5\3\2\2\2\u0263\u0265\5\n\6\2\u0264\u0263")
        buf.write("\3\2\2\2\u0265\u0266\3\2\2\2\u0266\u0264\3\2\2\2\u0266")
        buf.write("\u0267\3\2\2\2\u0267\7\3\2\2\2\u0268\u0269\5\f\7\2\u0269")
        buf.write("\t\3\2\2\2\u026a\u026b\5\f\7\2\u026b\13\3\2\2\2\u026c")
        buf.write("\u026d\7/\2\2\u026d\u026f\5\16\b\2\u026e\u026c\3\2\2\2")
        buf.write("\u026e\u026f\3\2\2\2\u026f\u0270\3\2\2\2\u0270\u0271\7")
        buf.write("\60\2\2\u0271\u0273\5\20\t\2\u0272\u0274\7\5\2\2\u0273")
        buf.write("\u0272\3\2\2\2\u0274\u0275\3\2\2\2\u0275\u0273\3\2\2\2")
        buf.write("\u0275\u0276\3\2\2\2\u0276\r\3\2\2\2\u0277\u0279\7\25")
        buf.write("\2\2\u0278\u0277\3\2\2\2\u0278\u0279\3\2\2\2\u0279\u027a")
        buf.write("\3\2\2\2\u027a\u027b\5\34\17\2\u027b\17\3\2\2\2\u027c")
        buf.write("\u0281\5\22\n\2\u027d\u027e\7\24\2\2\u027e\u0280\5\22")
        buf.write("\n\2\u027f\u027d\3\2\2\2\u0280\u0283\3\2\2\2\u0281\u027f")
        buf.write("\3\2\2\2\u0281\u0282\3\2\2\2\u0282\21\3\2\2\2\u0283\u0281")
        buf.write("\3\2\2\2\u0284\u0287\5\24\13\2\u0285\u0286\7\61\2\2\u0286")
        buf.write("\u0288\5\26\f\2\u0287\u0285\3\2\2\2\u0287\u0288\3\2\2")
        buf.write("\2\u0288\u028b\3\2\2\2\u0289\u028b\5\30\r\2\u028a\u0284")
        buf.write("\3\2\2\2\u028a\u0289\3\2\2\2\u028b\23\3\2\2\2\u028c\u028d")
        buf.write("\5\34\17\2\u028d\25\3\2\2\2\u028e\u028f\5\32\16\2\u028f")
        buf.write("\27\3\2\2\2\u0290\u0291\7\34\2\2\u0291\31\3\2\2\2\u0292")
        buf.write("\u0293\t\2\2\2\u0293\33\3\2\2\2\u0294\u0299\5\32\16\2")
        buf.write("\u0295\u0296\7\25\2\2\u0296\u0298\5\32\16\2\u0297\u0295")
        buf.write("\3\2\2\2\u0298\u029b\3\2\2\2\u0299\u0297\3\2\2\2\u0299")
        buf.write("\u029a\3\2\2\2\u029a\35\3\2\2\2\u029b\u0299\3\2\2\2\u029c")
        buf.write("\u02a0\7\26\2\2\u029d\u029e\5\32\16\2\u029e\u029f\7\25")
        buf.write("\2\2\u029f\u02a1\3\2\2\2\u02a0\u029d\3\2\2\2\u02a0\u02a1")
        buf.write("\3\2\2\2\u02a1\u02a2\3\2\2\2\u02a2\u02a3\5\32\16\2\u02a3")
        buf.write("\37\3\2\2\2\u02a4\u02a6\7\25\2\2\u02a5\u02a4\3\2\2\2\u02a5")
        buf.write("\u02a6\3\2\2\2\u02a6\u02a7\3\2\2\2\u02a7\u02ad\7\34\2")
        buf.write("\2\u02a8\u02a9\7\24\2\2\u02a9\u02aa\7\f\2\2\u02aa\u02ac")
        buf.write("\5\"\22\2\u02ab\u02a8\3\2\2\2\u02ac\u02af\3\2\2\2\u02ad")
        buf.write("\u02ab\3\2\2\2\u02ad\u02ae\3\2\2\2\u02ae\u02bc\3\2\2\2")
        buf.write("\u02af\u02ad\3\2\2\2\u02b0\u02b8\5\32\16\2\u02b1\u02b3")
        buf.write("\7\24\2\2\u02b2\u02b4\7\f\2\2\u02b3\u02b2\3\2\2\2\u02b3")
        buf.write("\u02b4\3\2\2\2\u02b4\u02b5\3\2\2\2\u02b5\u02b7\5\"\22")
        buf.write("\2\u02b6\u02b1\3\2\2\2\u02b7\u02ba\3\2\2\2\u02b8\u02b6")
        buf.write("\3\2\2\2\u02b8\u02b9\3\2\2\2\u02b9\u02bc\3\2\2\2\u02ba")
        buf.write("\u02b8\3\2\2\2\u02bb\u02a5\3\2\2\2\u02bb\u02b0\3\2\2\2")
        buf.write("\u02bc!\3\2\2\2\u02bd\u02bf\7\34\2\2\u02be\u02bd\3\2\2")
        buf.write("\2\u02be\u02bf\3\2\2\2\u02bf\u02c0\3\2\2\2\u02c0\u02c2")
        buf.write("\5\32\16\2\u02c1\u02c3\7\34\2\2\u02c2\u02c1\3\2\2\2\u02c2")
        buf.write("\u02c3\3\2\2\2\u02c3#\3\2\2\2\u02c4\u02c5\7\17\2\2\u02c5")
        buf.write("\u02c6\7\3\2\2\u02c6\u02c7\7\20\2\2\u02c7%\3\2\2\2\u02c8")
        buf.write("\u02cb\5*\26\2\u02c9\u02cb\5(\25\2\u02ca\u02c8\3\2\2\2")
        buf.write("\u02ca\u02c9\3\2\2\2\u02cb\'\3\2\2\2\u02cc\u02cd\7&\2")
        buf.write("\2\u02cd\u02ce\7*\2\2\u02ce\u02cf\7\5\2\2\u02cf)\3\2\2")
        buf.write("\2\u02d0\u02d1\7(\2\2\u02d1+\3\2\2\2\u02d2\u02dd\5.\30")
        buf.write("\2\u02d3\u02dd\5\62\32\2\u02d4\u02dd\5\64\33\2\u02d5\u02dd")
        buf.write("\5\66\34\2\u02d6\u02dd\58\35\2\u02d7\u02dd\5:\36\2\u02d8")
        buf.write("\u02dd\5V,\2\u02d9\u02dd\5Z.\2\u02da\u02dd\5`\61\2\u02db")
        buf.write("\u02dd\7\5\2\2\u02dc\u02d2\3\2\2\2\u02dc\u02d3\3\2\2\2")
        buf.write("\u02dc\u02d4\3\2\2\2\u02dc\u02d5\3\2\2\2\u02dc\u02d6\3")
        buf.write("\2\2\2\u02dc\u02d7\3\2\2\2\u02dc\u02d8\3\2\2\2\u02dc\u02d9")
        buf.write("\3\2\2\2\u02dc\u02da\3\2\2\2\u02dc\u02db\3\2\2\2\u02dd")
        buf.write("-\3\2\2\2\u02de\u02e3\7y\2\2\u02df\u02e0\7\r\2\2\u02e0")
        buf.write("\u02e1\5\60\31\2\u02e1\u02e2\7\16\2\2\u02e2\u02e4\3\2")
        buf.write("\2\2\u02e3\u02df\3\2\2\2\u02e3\u02e4\3\2\2\2\u02e4/\3")
        buf.write("\2\2\2\u02e5\u02e6\t\3\2\2\u02e6\61\3\2\2\2\u02e7\u02ea")
        buf.write("\7z\2\2\u02e8\u02e9\7\r\2\2\u02e9\u02eb\7\16\2\2\u02ea")
        buf.write("\u02e8\3\2\2\2\u02ea\u02eb\3\2\2\2\u02eb\63\3\2\2\2\u02ec")
        buf.write("\u02ef\7{\2\2\u02ed\u02ee\7\r\2\2\u02ee\u02f0\7\16\2\2")
        buf.write("\u02ef\u02ed\3\2\2\2\u02ef\u02f0\3\2\2\2\u02f0\65\3\2")
        buf.write("\2\2\u02f1\u02f4\7|\2\2\u02f2\u02f3\7\r\2\2\u02f3\u02f5")
        buf.write("\7\16\2\2\u02f4\u02f2\3\2\2\2\u02f4\u02f5\3\2\2\2\u02f5")
        buf.write("\67\3\2\2\2\u02f6\u02f9\7}\2\2\u02f7\u02f8\7\r\2\2\u02f8")
        buf.write("\u02fa\7\16\2\2\u02f9\u02f7\3\2\2\2\u02f9\u02fa\3\2\2")
        buf.write("\2\u02fa9\3\2\2\2\u02fb\u02fc\7~\2\2\u02fc\u0300\7\r\2")
        buf.write("\2\u02fd\u02ff\7\5\2\2\u02fe\u02fd\3\2\2\2\u02ff\u0302")
        buf.write("\3\2\2\2\u0300\u02fe\3\2\2\2\u0300\u0301\3\2\2\2\u0301")
        buf.write("\u0304\3\2\2\2\u0302\u0300\3\2\2\2\u0303\u0305\5<\37\2")
        buf.write("\u0304\u0303\3\2\2\2\u0304\u0305\3\2\2\2\u0305\u0309\3")
        buf.write("\2\2\2\u0306\u0308\7\5\2\2\u0307\u0306\3\2\2\2\u0308\u030b")
        buf.write("\3\2\2\2\u0309\u0307\3\2\2\2\u0309\u030a\3\2\2\2\u030a")
        buf.write("\u030d\3\2\2\2\u030b\u0309\3\2\2\2\u030c\u030e\5F$\2\u030d")
        buf.write("\u030c\3\2\2\2\u030e\u030f\3\2\2\2\u030f\u030d\3\2\2\2")
        buf.write("\u030f\u0310\3\2\2\2\u0310\u0314\3\2\2\2\u0311\u0313\7")
        buf.write("\5\2\2\u0312\u0311\3\2\2\2\u0313\u0316\3\2\2\2\u0314\u0312")
        buf.write("\3\2\2\2\u0314\u0315\3\2\2\2\u0315\u0317\3\2\2\2\u0316")
        buf.write("\u0314\3\2\2\2\u0317\u0318\7\16\2\2\u0318;\3\2\2\2\u0319")
        buf.write("\u031a\5> \2\u031a=\3\2\2\2\u031b\u031c\7M\2\2\u031c\u0320")
        buf.write("\7\r\2\2\u031d\u031f\7\5\2\2\u031e\u031d\3\2\2\2\u031f")
        buf.write("\u0322\3\2\2\2\u0320\u031e\3\2\2\2\u0320\u0321\3\2\2\2")
        buf.write("\u0321\u0324\3\2\2\2\u0322\u0320\3\2\2\2\u0323\u0325\5")
        buf.write("@!\2\u0324\u0323\3\2\2\2\u0324\u0325\3\2\2\2\u0325\u0329")
        buf.write("\3\2\2\2\u0326\u0328\7\5\2\2\u0327\u0326\3\2\2\2\u0328")
        buf.write("\u032b\3\2\2\2\u0329\u0327\3\2\2\2\u0329\u032a\3\2\2\2")
        buf.write("\u032a\u0332\3\2\2\2\u032b\u0329\3\2\2\2\u032c\u032e\5")
        buf.write("P)\2\u032d\u032f\7\24\2\2\u032e\u032d\3\2\2\2\u032e\u032f")
        buf.write("\3\2\2\2\u032f\u0331\3\2\2\2\u0330\u032c\3\2\2\2\u0331")
        buf.write("\u0334\3\2\2\2\u0332\u0330\3\2\2\2\u0332\u0333\3\2\2\2")
        buf.write("\u0333\u0338\3\2\2\2\u0334\u0332\3\2\2\2\u0335\u0337\7")
        buf.write("\5\2\2\u0336\u0335\3\2\2\2\u0337\u033a\3\2\2\2\u0338\u0336")
        buf.write("\3\2\2\2\u0338\u0339\3\2\2\2\u0339\u033b\3\2\2\2\u033a")
        buf.write("\u0338\3\2\2\2\u033b\u033c\7\16\2\2\u033c?\3\2\2\2\u033d")
        buf.write("\u033e\7L\2\2\u033e\u0342\7\r\2\2\u033f\u0341\7\5\2\2")
        buf.write("\u0340\u033f\3\2\2\2\u0341\u0344\3\2\2\2\u0342\u0340\3")
        buf.write("\2\2\2\u0342\u0343\3\2\2\2\u0343\u034d\3\2\2\2\u0344\u0342")
        buf.write("\3\2\2\2\u0345\u034a\5B\"\2\u0346\u0347\7\24\2\2\u0347")
        buf.write("\u0349\5B\"\2\u0348\u0346\3\2\2\2\u0349\u034c\3\2\2\2")
        buf.write("\u034a\u0348\3\2\2\2\u034a\u034b\3\2\2\2\u034b\u034e\3")
        buf.write("\2\2\2\u034c\u034a\3\2\2\2\u034d\u0345\3\2\2\2\u034d\u034e")
        buf.write("\3\2\2\2\u034e\u0352\3\2\2\2\u034f\u0351\7\5\2\2\u0350")
        buf.write("\u034f\3\2\2\2\u0351\u0354\3\2\2\2\u0352\u0350\3\2\2\2")
        buf.write("\u0352\u0353\3\2\2\2\u0353\u0355\3\2\2\2\u0354\u0352\3")
        buf.write("\2\2\2\u0355\u0356\7\16\2\2\u0356A\3\2\2\2\u0357\u0359")
        buf.write("\7\5\2\2\u0358\u0357\3\2\2\2\u0359\u035c\3\2\2\2\u035a")
        buf.write("\u0358\3\2\2\2\u035a\u035b\3\2\2\2\u035b\u035d\3\2\2\2")
        buf.write("\u035c\u035a\3\2\2\2\u035d\u0375\5D#\2\u035e\u0362\7\r")
        buf.write("\2\2\u035f\u0361\7\5\2\2\u0360\u035f\3\2\2\2\u0361\u0364")
        buf.write("\3\2\2\2\u0362\u0360\3\2\2\2\u0362\u0363\3\2\2\2\u0363")
        buf.write("\u036b\3\2\2\2\u0364\u0362\3\2\2\2\u0365\u0367\5P)\2\u0366")
        buf.write("\u0368\7\24\2\2\u0367\u0366\3\2\2\2\u0367\u0368\3\2\2")
        buf.write("\2\u0368\u036a\3\2\2\2\u0369\u0365\3\2\2\2\u036a\u036d")
        buf.write("\3\2\2\2\u036b\u0369\3\2\2\2\u036b\u036c\3\2\2\2\u036c")
        buf.write("\u0371\3\2\2\2\u036d\u036b\3\2\2\2\u036e\u0370\7\5\2\2")
        buf.write("\u036f\u036e\3\2\2\2\u0370\u0373\3\2\2\2\u0371\u036f\3")
        buf.write("\2\2\2\u0371\u0372\3\2\2\2\u0372\u0374\3\2\2\2\u0373\u0371")
        buf.write("\3\2\2\2\u0374\u0376\7\16\2\2\u0375\u035e\3\2\2\2\u0375")
        buf.write("\u0376\3\2\2\2\u0376C\3\2\2\2\u0377\u0378\5\32\16\2\u0378")
        buf.write("E\3\2\2\2\u0379\u037d\5J&\2\u037a\u037c\7\5\2\2\u037b")
        buf.write("\u037a\3\2\2\2\u037c\u037f\3\2\2\2\u037d\u037b\3\2\2\2")
        buf.write("\u037d\u037e\3\2\2\2\u037e\u0380\3\2\2\2\u037f\u037d\3")
        buf.write("\2\2\2\u0380\u0384\5H%\2\u0381\u0383\7\5\2\2\u0382\u0381")
        buf.write("\3\2\2\2\u0383\u0386\3\2\2\2\u0384\u0382\3\2\2\2\u0384")
        buf.write("\u0385\3\2\2\2\u0385\u0387\3\2\2\2\u0386\u0384\3\2\2\2")
        buf.write("\u0387\u0388\5L\'\2\u0388\u038c\7\r\2\2\u0389\u038b\7")
        buf.write("\5\2\2\u038a\u0389\3\2\2\2\u038b\u038e\3\2\2\2\u038c\u038a")
        buf.write("\3\2\2\2\u038c\u038d\3\2\2\2\u038d\u038f\3\2\2\2\u038e")
        buf.write("\u038c\3\2\2\2\u038f\u03a0\5N(\2\u0390\u0394\7\13\2\2")
        buf.write("\u0391\u0393\7\5\2\2\u0392\u0391\3\2\2\2\u0393\u0396\3")
        buf.write("\2\2\2\u0394\u0392\3\2\2\2\u0394\u0395\3\2\2\2\u0395\u039d")
        buf.write("\3\2\2\2\u0396\u0394\3\2\2\2\u0397\u0399\5P)\2\u0398\u039a")
        buf.write("\7\24\2\2\u0399\u0398\3\2\2\2\u0399\u039a\3\2\2\2\u039a")
        buf.write("\u039c\3\2\2\2\u039b\u0397\3\2\2\2\u039c\u039f\3\2\2\2")
        buf.write("\u039d\u039b\3\2\2\2\u039d\u039e\3\2\2\2\u039e\u03a1\3")
        buf.write("\2\2\2\u039f\u039d\3\2\2\2\u03a0\u0390\3\2\2\2\u03a0\u03a1")
        buf.write("\3\2\2\2\u03a1\u03a5\3\2\2\2\u03a2\u03a4\7\5\2\2\u03a3")
        buf.write("\u03a2\3\2\2\2\u03a4\u03a7\3\2\2\2\u03a5\u03a3\3\2\2\2")
        buf.write("\u03a5\u03a6\3\2\2\2\u03a6\u03a8\3\2\2\2\u03a7\u03a5\3")
        buf.write("\2\2\2\u03a8\u03ac\7\16\2\2\u03a9\u03ab\7\5\2\2\u03aa")
        buf.write("\u03a9\3\2\2\2\u03ab\u03ae\3\2\2\2\u03ac\u03aa\3\2\2\2")
        buf.write("\u03ac\u03ad\3\2\2\2\u03adG\3\2\2\2\u03ae\u03ac\3\2\2")
        buf.write("\2\u03af\u03b0\t\4\2\2\u03b0\u03b1\7\n\2\2\u03b1I\3\2")
        buf.write("\2\2\u03b2\u03b7\5\32\16\2\u03b3\u03b7\7\23\2\2\u03b4")
        buf.write("\u03b7\7\34\2\2\u03b5\u03b7\7\27\2\2\u03b6\u03b2\3\2\2")
        buf.write("\2\u03b6\u03b3\3\2\2\2\u03b6\u03b4\3\2\2\2\u03b6\u03b5")
        buf.write("\3\2\2\2\u03b7\u03b8\3\2\2\2\u03b8\u03b6\3\2\2\2\u03b8")
        buf.write("\u03b9\3\2\2\2\u03b9K\3\2\2\2\u03ba\u03bf\5\32\16\2\u03bb")
        buf.write("\u03bf\7\23\2\2\u03bc\u03bf\7\27\2\2\u03bd\u03bf\7\34")
        buf.write("\2\2\u03be\u03ba\3\2\2\2\u03be\u03bb\3\2\2\2\u03be\u03bc")
        buf.write("\3\2\2\2\u03be\u03bd\3\2\2\2\u03bf\u03c0\3\2\2\2\u03c0")
        buf.write("\u03be\3\2\2\2\u03c0\u03c1\3\2\2\2\u03c1M\3\2\2\2\u03c2")
        buf.write("\u03c7\5\32\16\2\u03c3\u03c7\7\23\2\2\u03c4\u03c7\7\34")
        buf.write("\2\2\u03c5\u03c7\7\25\2\2\u03c6\u03c2\3\2\2\2\u03c6\u03c3")
        buf.write("\3\2\2\2\u03c6\u03c4\3\2\2\2\u03c6\u03c5\3\2\2\2\u03c7")
        buf.write("\u03c8\3\2\2\2\u03c8\u03c6\3\2\2\2\u03c8\u03c9\3\2\2\2")
        buf.write("\u03c9O\3\2\2\2\u03ca\u03cc\7\5\2\2\u03cb\u03ca\3\2\2")
        buf.write("\2\u03cc\u03cf\3\2\2\2\u03cd\u03cb\3\2\2\2\u03cd\u03ce")
        buf.write("\3\2\2\2\u03ce\u03d0\3\2\2\2\u03cf\u03cd\3\2\2\2\u03d0")
        buf.write("\u03d1\5R*\2\u03d1\u03d2\7\30\2\2\u03d2\u03d3\5T+\2\u03d3")
        buf.write("Q\3\2\2\2\u03d4\u03d5\5\32\16\2\u03d5S\3\2\2\2\u03d6\u03db")
        buf.write("\7\37\2\2\u03d7\u03db\7 \2\2\u03d8\u03db\7\7\2\2\u03d9")
        buf.write("\u03db\5\32\16\2\u03da\u03d6\3\2\2\2\u03da\u03d7\3\2\2")
        buf.write("\2\u03da\u03d8\3\2\2\2\u03da\u03d9\3\2\2\2\u03dbU\3\2")
        buf.write("\2\2\u03dc\u03dd\7\177\2\2\u03dd\u03de\5X-\2\u03de\u03df")
        buf.write("\5&\24\2\u03dfW\3\2\2\2\u03e0\u03e1\t\5\2\2\u03e1Y\3\2")
        buf.write("\2\2\u03e2\u03e3\7\u0080\2\2\u03e3\u03e4\7\r\2\2\u03e4")
        buf.write("\u03e9\5^\60\2\u03e5\u03e6\7\24\2\2\u03e6\u03e7\7J\2\2")
        buf.write("\u03e7\u03e8\7\30\2\2\u03e8\u03ea\5\\/\2\u03e9\u03e5\3")
        buf.write("\2\2\2\u03e9\u03ea\3\2\2\2\u03ea\u03eb\3\2\2\2\u03eb\u03ec")
        buf.write("\7\16\2\2\u03ec[\3\2\2\2\u03ed\u03ee\7\4\2\2\u03ee]\3")
        buf.write("\2\2\2\u03ef\u03f3\5\32\16\2\u03f0\u03f3\7\37\2\2\u03f1")
        buf.write("\u03f3\7 \2\2\u03f2\u03ef\3\2\2\2\u03f2\u03f0\3\2\2\2")
        buf.write("\u03f2\u03f1\3\2\2\2\u03f3_\3\2\2\2\u03f4\u03f5\7\u0081")
        buf.write("\2\2\u03f5\u03f6\7\r\2\2\u03f6\u03f7\5b\62\2\u03f7\u03f8")
        buf.write("\7\16\2\2\u03f8a\3\2\2\2\u03f9\u03fe\7\6\2\2\u03fa\u03fb")
        buf.write("\7\24\2\2\u03fb\u03fd\7\6\2\2\u03fc\u03fa\3\2\2\2\u03fd")
        buf.write("\u0400\3\2\2\2\u03fe\u03fc\3\2\2\2\u03fe\u03ff\3\2\2\2")
        buf.write("\u03ffc\3\2\2\2\u0400\u03fe\3\2\2\2\u0401\u0403\5h\65")
        buf.write("\2\u0402\u0404\5f\64\2\u0403\u0402\3\2\2\2\u0403\u0404")
        buf.write("\3\2\2\2\u0404\u0408\3\2\2\2\u0405\u0407\7\5\2\2\u0406")
        buf.write("\u0405\3\2\2\2\u0407\u040a\3\2\2\2\u0408\u0406\3\2\2\2")
        buf.write("\u0408\u0409\3\2\2\2\u0409\u040e\3\2\2\2\u040a\u0408\3")
        buf.write("\2\2\2\u040b\u040d\5t;\2\u040c\u040b\3\2\2\2\u040d\u0410")
        buf.write("\3\2\2\2\u040e\u040c\3\2\2\2\u040e\u040f\3\2\2\2\u040f")
        buf.write("\u0414\3\2\2\2\u0410\u040e\3\2\2\2\u0411\u0413\7\5\2\2")
        buf.write("\u0412\u0411\3\2\2\2\u0413\u0416\3\2\2\2\u0414\u0412\3")
        buf.write("\2\2\2\u0414\u0415\3\2\2\2\u0415\u041a\3\2\2\2\u0416\u0414")
        buf.write("\3\2\2\2\u0417\u0419\5\u00e6t\2\u0418\u0417\3\2\2\2\u0419")
        buf.write("\u041c\3\2\2\2\u041a\u0418\3\2\2\2\u041a\u041b\3\2\2\2")
        buf.write("\u041b\u0420\3\2\2\2\u041c\u041a\3\2\2\2\u041d\u041f\7")
        buf.write("\5\2\2\u041e\u041d\3\2\2\2\u041f\u0422\3\2\2\2\u0420\u041e")
        buf.write("\3\2\2\2\u0420\u0421\3\2\2\2\u0421e\3\2\2\2\u0422\u0420")
        buf.write("\3\2\2\2\u0423\u0424\7\30\2\2\u0424\u042b\t\3\2\2\u0425")
        buf.write("\u0427\7\5\2\2\u0426\u0425\3\2\2\2\u0427\u0428\3\2\2\2")
        buf.write("\u0428\u0426\3\2\2\2\u0428\u0429\3\2\2\2\u0429\u042c\3")
        buf.write("\2\2\2\u042a\u042c\7\2\2\3\u042b\u0426\3\2\2\2\u042b\u042a")
        buf.write("\3\2\2\2\u042cg\3\2\2\2\u042d\u042f\7\26\2\2\u042e\u0430")
        buf.write("\5p9\2\u042f\u042e\3\2\2\2\u042f\u0430\3\2\2\2\u0430\u0431")
        buf.write("\3\2\2\2\u0431\u0433\5r:\2\u0432\u0434\5l\67\2\u0433\u0432")
        buf.write("\3\2\2\2\u0433\u0434\3\2\2\2\u0434\u0435\3\2\2\2\u0435")
        buf.write("\u0436\5j\66\2\u0436\u0437\7\5\2\2\u0437i\3\2\2\2\u0438")
        buf.write("\u0439\7\5\2\2\u0439\u043a\7\23\2\2\u043a\u043c\7\23\2")
        buf.write("\2\u043b\u043d\7\23\2\2\u043c\u043b\3\2\2\2\u043d\u043e")
        buf.write("\3\2\2\2\u043e\u043c\3\2\2\2\u043e\u043f\3\2\2\2\u043f")
        buf.write("k\3\2\2\2\u0440\u0441\7\13\2\2\u0441\u0444\5n8\2\u0442")
        buf.write("\u0443\7\27\2\2\u0443\u0445\5n8\2\u0444\u0442\3\2\2\2")
        buf.write("\u0444\u0445\3\2\2\2\u0445m\3\2\2\2\u0446\u044a\5\32\16")
        buf.write("\2\u0447\u044a\7\37\2\2\u0448\u044a\7 \2\2\u0449\u0446")
        buf.write("\3\2\2\2\u0449\u0447\3\2\2\2\u0449\u0448\3\2\2\2\u044a")
        buf.write("o\3\2\2\2\u044b\u0450\5\32\16\2\u044c\u044d\7\23\2\2\u044d")
        buf.write("\u0451\7\n\2\2\u044e\u044f\7\35\2\2\u044f\u0451\7\n\2")
        buf.write("\2\u0450\u044c\3\2\2\2\u0450\u044e\3\2\2\2\u0451q\3\2")
        buf.write("\2\2\u0452\u0453\5\32\16\2\u0453s\3\2\2\2\u0454\u0456")
        buf.write("\5\u008eH\2\u0455\u0454\3\2\2\2\u0456\u0459\3\2\2\2\u0457")
        buf.write("\u0455\3\2\2\2\u0457\u0458\3\2\2\2\u0458\u045a\3\2\2\2")
        buf.write("\u0459\u0457\3\2\2\2\u045a\u045c\5\u008cG\2\u045b\u045d")
        buf.write("\5v<\2\u045c\u045b\3\2\2\2\u045c\u045d\3\2\2\2\u045d\u045f")
        buf.write("\3\2\2\2\u045e\u0460\5\u008aF\2\u045f\u045e\3\2\2\2\u045f")
        buf.write("\u0460\3\2\2\2\u0460\u0462\3\2\2\2\u0461\u0463\5\u0088")
        buf.write("E\2\u0462\u0461\3\2\2\2\u0462\u0463\3\2\2\2\u0463\u046a")
        buf.write("\3\2\2\2\u0464\u0466\7\5\2\2\u0465\u0464\3\2\2\2\u0466")
        buf.write("\u0467\3\2\2\2\u0467\u0465\3\2\2\2\u0467\u0468\3\2\2\2")
        buf.write("\u0468\u046b\3\2\2\2\u0469\u046b\7\2\2\3\u046a\u0465\3")
        buf.write("\2\2\2\u046a\u0469\3\2\2\2\u046bu\3\2\2\2\u046c\u046e")
        buf.write("\7\13\2\2\u046d\u046f\5x=\2\u046e\u046d\3\2\2\2\u046e")
        buf.write("\u046f\3\2\2\2\u046f\u0479\3\2\2\2\u0470\u0471\7\13\2")
        buf.write("\2\u0471\u0473\5\u0090I\2\u0472\u0474\5z>\2\u0473\u0472")
        buf.write("\3\2\2\2\u0473\u0474\3\2\2\2\u0474\u0479\3\2\2\2\u0475")
        buf.write("\u0476\7\13\2\2\u0476\u0479\5~@\2\u0477\u0479\5\u0080")
        buf.write("A\2\u0478\u046c\3\2\2\2\u0478\u0470\3\2\2\2\u0478\u0475")
        buf.write("\3\2\2\2\u0478\u0477\3\2\2\2\u0479w\3\2\2\2\u047a\u047b")
        buf.write("\5*\26\2\u047by\3\2\2\2\u047c\u047e\5|?\2\u047d\u047c")
        buf.write("\3\2\2\2\u047d\u047e\3\2\2\2\u047e\u047f\3\2\2\2\u047f")
        buf.write("\u0480\5*\26\2\u0480{\3\2\2\2\u0481\u0482\7\25\2\2\u0482")
        buf.write("\u0483\7\25\2\2\u0483}\3\2\2\2\u0484\u0485\5\32\16\2\u0485")
        buf.write("\177\3\2\2\2\u0486\u0487\5\u0082B\2\u0487\u0488\5\u0084")
        buf.write("C\2\u0488\u0081\3\2\2\2\u0489\u048a\t\6\2\2\u048a\u0083")
        buf.write("\3\2\2\2\u048b\u048c\7*\2\2\u048c\u0085\3\2\2\2\u048d")
        buf.write("\u048f\5\32\16\2\u048e\u048d\3\2\2\2\u048f\u0490\3\2\2")
        buf.write("\2\u0490\u048e\3\2\2\2\u0490\u0491\3\2\2\2\u0491\u0495")
        buf.write("\3\2\2\2\u0492\u0495\7\37\2\2\u0493\u0495\7 \2\2\u0494")
        buf.write("\u048e\3\2\2\2\u0494\u0492\3\2\2\2\u0494\u0493\3\2\2\2")
        buf.write("\u0495\u0087\3\2\2\2\u0496\u0497\7\21\2\2\u0497\u0498")
        buf.write("\5\u0086D\2\u0498\u0089\3\2\2\2\u0499\u049a\7\27\2\2\u049a")
        buf.write("\u049b\5\u0086D\2\u049b\u008b\3\2\2\2\u049c\u049d\5\32")
        buf.write("\16\2\u049d\u008d\3\2\2\2\u049e\u049f\t\7\2\2\u049f\u008f")
        buf.write("\3\2\2\2\u04a0\u04b3\5\u0092J\2\u04a1\u04b3\5\u0096L\2")
        buf.write("\u04a2\u04b3\5\u0094K\2\u04a3\u04b3\5\u0098M\2\u04a4\u04b3")
        buf.write("\5\u009aN\2\u04a5\u04b3\5\u009cO\2\u04a6\u04b3\5\u009e")
        buf.write("P\2\u04a7\u04b3\5\u00a0Q\2\u04a8\u04b3\5\u00a2R\2\u04a9")
        buf.write("\u04b3\5\u00aaV\2\u04aa\u04b3\5\u00b6\\\2\u04ab\u04b3")
        buf.write("\5\u00c0a\2\u04ac\u04b3\5\u00c6d\2\u04ad\u04b3\5\u00da")
        buf.write("n\2\u04ae\u04b3\5\u00caf\2\u04af\u04b3\5\u00a4S\2\u04b0")
        buf.write("\u04b3\5\u00a6T\2\u04b1\u04b3\5\u00a8U\2\u04b2\u04a0\3")
        buf.write("\2\2\2\u04b2\u04a1\3\2\2\2\u04b2\u04a2\3\2\2\2\u04b2\u04a3")
        buf.write("\3\2\2\2\u04b2\u04a4\3\2\2\2\u04b2\u04a5\3\2\2\2\u04b2")
        buf.write("\u04a6\3\2\2\2\u04b2\u04a7\3\2\2\2\u04b2\u04a8\3\2\2\2")
        buf.write("\u04b2\u04a9\3\2\2\2\u04b2\u04aa\3\2\2\2\u04b2\u04ab\3")
        buf.write("\2\2\2\u04b2\u04ac\3\2\2\2\u04b2\u04ad\3\2\2\2\u04b2\u04ae")
        buf.write("\3\2\2\2\u04b2\u04af\3\2\2\2\u04b2\u04b0\3\2\2\2\u04b2")
        buf.write("\u04b1\3\2\2\2\u04b3\u0091\3\2\2\2\u04b4\u04b5\7\62\2")
        buf.write("\2\u04b5\u0093\3\2\2\2\u04b6\u04b7\7\63\2\2\u04b7\u0095")
        buf.write("\3\2\2\2\u04b8\u04b9\7\64\2\2\u04b9\u0097\3\2\2\2\u04ba")
        buf.write("\u04bb\7\65\2\2\u04bb\u0099\3\2\2\2\u04bc\u04bd\7\66\2")
        buf.write("\2\u04bd\u009b\3\2\2\2\u04be\u04bf\7\67\2\2\u04bf\u009d")
        buf.write("\3\2\2\2\u04c0\u04c1\78\2\2\u04c1\u009f\3\2\2\2\u04c2")
        buf.write("\u04c3\79\2\2\u04c3\u00a1\3\2\2\2\u04c4\u04c5\7:\2\2\u04c5")
        buf.write("\u00a3\3\2\2\2\u04c6\u04c7\7<\2\2\u04c7\u00a5\3\2\2\2")
        buf.write("\u04c8\u04c9\7>\2\2\u04c9\u00a7\3\2\2\2\u04ca\u04cb\7")
        buf.write("?\2\2\u04cb\u00a9\3\2\2\2\u04cc\u04d5\7A\2\2\u04cd\u04ce")
        buf.write("\7\r\2\2\u04ce\u04d1\5\u00acW\2\u04cf\u04d0\7\24\2\2\u04d0")
        buf.write("\u04d2\5\u00aeX\2\u04d1\u04cf\3\2\2\2\u04d1\u04d2\3\2")
        buf.write("\2\2\u04d2\u04d3\3\2\2\2\u04d3\u04d4\7\16\2\2\u04d4\u04d6")
        buf.write("\3\2\2\2\u04d5\u04cd\3\2\2\2\u04d5\u04d6\3\2\2\2\u04d6")
        buf.write("\u00ab\3\2\2\2\u04d7\u04d8\t\b\2\2\u04d8\u00ad\3\2\2\2")
        buf.write("\u04d9\u04da\7H\2\2\u04da\u04db\7\30\2\2\u04db\u04e0\5")
        buf.write("\u00b0Y\2\u04dc\u04dd\7\24\2\2\u04dd\u04df\5\u00b0Y\2")
        buf.write("\u04de\u04dc\3\2\2\2\u04df\u04e2\3\2\2\2\u04e0\u04de\3")
        buf.write("\2\2\2\u04e0\u04e1\3\2\2\2\u04e1\u00af\3\2\2\2\u04e2\u04e0")
        buf.write("\3\2\2\2\u04e3\u04e5\5\u00b4[\2\u04e4\u04e3\3\2\2\2\u04e4")
        buf.write("\u04e5\3\2\2\2\u04e5\u04e6\3\2\2\2\u04e6\u04e7\5\u00b2")
        buf.write("Z\2\u04e7\u00b1\3\2\2\2\u04e8\u04ec\5\32\16\2\u04e9\u04ec")
        buf.write("\7\37\2\2\u04ea\u04ec\7 \2\2\u04eb\u04e8\3\2\2\2\u04eb")
        buf.write("\u04e9\3\2\2\2\u04eb\u04ea\3\2\2\2\u04ec\u00b3\3\2\2\2")
        buf.write("\u04ed\u04ee\5\32\16\2\u04ee\u04ef\7\13\2\2\u04ef\u00b5")
        buf.write("\3\2\2\2\u04f0\u04f5\7B\2\2\u04f1\u04f2\7\r\2\2\u04f2")
        buf.write("\u04f3\5\u00b8]\2\u04f3\u04f4\7\16\2\2\u04f4\u04f6\3\2")
        buf.write("\2\2\u04f5\u04f1\3\2\2\2\u04f5\u04f6\3\2\2\2\u04f6\u00b7")
        buf.write("\3\2\2\2\u04f7\u04f8\7H\2\2\u04f8\u04f9\7\30\2\2\u04f9")
        buf.write("\u04fe\5\u00ba^\2\u04fa\u04fb\7\24\2\2\u04fb\u04fd\5\u00ba")
        buf.write("^\2\u04fc\u04fa\3\2\2\2\u04fd\u0500\3\2\2\2\u04fe\u04fc")
        buf.write("\3\2\2\2\u04fe\u04ff\3\2\2\2\u04ff\u00b9\3\2\2\2\u0500")
        buf.write("\u04fe\3\2\2\2\u0501\u0503\5\u00be`\2\u0502\u0501\3\2")
        buf.write("\2\2\u0502\u0503\3\2\2\2\u0503\u0504\3\2\2\2\u0504\u0505")
        buf.write("\5\u00bc_\2\u0505\u00bb\3\2\2\2\u0506\u050a\5\32\16\2")
        buf.write("\u0507\u050a\7\37\2\2\u0508\u050a\7 \2\2\u0509\u0506\3")
        buf.write("\2\2\2\u0509\u0507\3\2\2\2\u0509\u0508\3\2\2\2\u050a\u00bd")
        buf.write("\3\2\2\2\u050b\u050c\7\7\2\2\u050c\u050d\7\13\2\2\u050d")
        buf.write("\u00bf\3\2\2\2\u050e\u050f\7C\2\2\u050f\u0510\7\r\2\2")
        buf.write("\u0510\u0511\5\u00c2b\2\u0511\u0512\7\16\2\2\u0512\u00c1")
        buf.write("\3\2\2\2\u0513\u0518\5\u00c4c\2\u0514\u0515\7\24\2\2\u0515")
        buf.write("\u0517\5\u00c4c\2\u0516\u0514\3\2\2\2\u0517\u051a\3\2")
        buf.write("\2\2\u0518\u0516\3\2\2\2\u0518\u0519\3\2\2\2\u0519\u00c3")
        buf.write("\3\2\2\2\u051a\u0518\3\2\2\2\u051b\u051c\5\32\16\2\u051c")
        buf.write("\u00c5\3\2\2\2\u051d\u0522\7D\2\2\u051e\u051f\7\r\2\2")
        buf.write("\u051f\u0520\5\u00c8e\2\u0520\u0521\7\16\2\2\u0521\u0523")
        buf.write("\3\2\2\2\u0522\u051e\3\2\2\2\u0522\u0523\3\2\2\2\u0523")
        buf.write("\u00c7\3\2\2\2\u0524\u0525\7\4\2\2\u0525\u00c9\3\2\2\2")
        buf.write("\u0526\u052b\5\u00ccg\2\u0527\u0528\7\r\2\2\u0528\u0529")
        buf.write("\5\u00ceh\2\u0529\u052a\7\16\2\2\u052a\u052c\3\2\2\2\u052b")
        buf.write("\u0527\3\2\2\2\u052b\u052c\3\2\2\2\u052c\u00cb\3\2\2\2")
        buf.write("\u052d\u052e\t\t\2\2\u052e\u00cd\3\2\2\2\u052f\u0534\5")
        buf.write("\u00d0i\2\u0530\u0531\7\24\2\2\u0531\u0533\5\u00d0i\2")
        buf.write("\u0532\u0530\3\2\2\2\u0533\u0536\3\2\2\2\u0534\u0532\3")
        buf.write("\2\2\2\u0534\u0535\3\2\2\2\u0535\u00cf\3\2\2\2\u0536\u0534")
        buf.write("\3\2\2\2\u0537\u0538\5\u00d4k\2\u0538\u0539\5\u00d2j\2")
        buf.write("\u0539\u053a\5\u00d6l\2\u053a\u00d1\3\2\2\2\u053b\u053c")
        buf.write("\7\b\2\2\u053c\u00d3\3\2\2\2\u053d\u053e\5\32\16\2\u053e")
        buf.write("\u053f\7\30\2\2\u053f\u00d5\3\2\2\2\u0540\u0542\5\u00d8")
        buf.write("m\2\u0541\u0540\3\2\2\2\u0542\u0545\3\2\2\2\u0543\u0541")
        buf.write("\3\2\2\2\u0543\u0544\3\2\2\2\u0544\u00d7\3\2\2\2\u0545")
        buf.write("\u0543\3\2\2\2\u0546\u0547\7\36\2\2\u0547\u0548\5\32\16")
        buf.write("\2\u0548\u00d9\3\2\2\2\u0549\u054a\5\u00dco\2\u054a\u054c")
        buf.write("\7\r\2\2\u054b\u054d\5\u00dep\2\u054c\u054b\3\2\2\2\u054c")
        buf.write("\u054d\3\2\2\2\u054d\u0550\3\2\2\2\u054e\u0551\5\u00e0")
        buf.write("q\2\u054f\u0551\5\u00e2r\2\u0550\u054e\3\2\2\2\u0550\u054f")
        buf.write("\3\2\2\2\u0551\u0553\3\2\2\2\u0552\u0554\5\u00e4s\2\u0553")
        buf.write("\u0552\3\2\2\2\u0553\u0554\3\2\2\2\u0554\u0555\3\2\2\2")
        buf.write("\u0555\u0556\7\16\2\2\u0556\u00db\3\2\2\2\u0557\u0558")
        buf.write("\t\n\2\2\u0558\u00dd\3\2\2\2\u0559\u055a\t\13\2\2\u055a")
        buf.write("\u00df\3\2\2\2\u055b\u055c\5\36\20\2\u055c\u00e1\3\2\2")
        buf.write("\2\u055d\u055e\5\34\17\2\u055e\u00e3\3\2\2\2\u055f\u0560")
        buf.write("\7\23\2\2\u0560\u0561\7\n\2\2\u0561\u0562\5\32\16\2\u0562")
        buf.write("\u00e5\3\2\2\2\u0563\u0573\5\u00e8u\2\u0564\u0573\5\u0112")
        buf.write("\u008a\2\u0565\u0573\5\u0118\u008d\2\u0566\u0573\5\u0148")
        buf.write("\u00a5\2\u0567\u0573\5\u014c\u00a7\2\u0568\u0573\5\u014e")
        buf.write("\u00a8\2\u0569\u0573\5\u0150\u00a9\2\u056a\u0573\5\u0154")
        buf.write("\u00ab\2\u056b\u0573\5\u0156\u00ac\2\u056c\u0573\5\u015a")
        buf.write("\u00ae\2\u056d\u0573\5\u015c\u00af\2\u056e\u0573\5\u015e")
        buf.write("\u00b0\2\u056f\u0573\5\u0160\u00b1\2\u0570\u0573\5\u0162")
        buf.write("\u00b2\2\u0571\u0573\7\5\2\2\u0572\u0563\3\2\2\2\u0572")
        buf.write("\u0564\3\2\2\2\u0572\u0565\3\2\2\2\u0572\u0566\3\2\2\2")
        buf.write("\u0572\u0567\3\2\2\2\u0572\u0568\3\2\2\2\u0572\u0569\3")
        buf.write("\2\2\2\u0572\u056a\3\2\2\2\u0572\u056b\3\2\2\2\u0572\u056c")
        buf.write("\3\2\2\2\u0572\u056d\3\2\2\2\u0572\u056e\3\2\2\2\u0572")
        buf.write("\u056f\3\2\2\2\u0572\u0570\3\2\2\2\u0572\u0571\3\2\2\2")
        buf.write("\u0573\u00e7\3\2\2\2\u0574\u058e\7\u0082\2\2\u0575\u0584")
        buf.write("\7\r\2\2\u0576\u0583\5\u0106\u0084\2\u0577\u0583\5\u0108")
        buf.write("\u0085\2\u0578\u0583\5\u010a\u0086\2\u0579\u0583\5\u010c")
        buf.write("\u0087\2\u057a\u0583\5\u010e\u0088\2\u057b\u0583\5\u0110")
        buf.write("\u0089\2\u057c\u0583\5\u00fe\u0080\2\u057d\u0583\5\u00f2")
        buf.write("z\2\u057e\u0583\5\u00ecw\2\u057f\u0583\5\u00eav\2\u0580")
        buf.write("\u0583\7\5\2\2\u0581\u0583\7\24\2\2\u0582\u0576\3\2\2")
        buf.write("\2\u0582\u0577\3\2\2\2\u0582\u0578\3\2\2\2\u0582\u0579")
        buf.write("\3\2\2\2\u0582\u057a\3\2\2\2\u0582\u057b\3\2\2\2\u0582")
        buf.write("\u057c\3\2\2\2\u0582\u057d\3\2\2\2\u0582\u057e\3\2\2\2")
        buf.write("\u0582\u057f\3\2\2\2\u0582\u0580\3\2\2\2\u0582\u0581\3")
        buf.write("\2\2\2\u0583\u0586\3\2\2\2\u0584\u0582\3\2\2\2\u0584\u0585")
        buf.write("\3\2\2\2\u0585\u058a\3\2\2\2\u0586\u0584\3\2\2\2\u0587")
        buf.write("\u0589\7\5\2\2\u0588\u0587\3\2\2\2\u0589\u058c\3\2\2\2")
        buf.write("\u058a\u0588\3\2\2\2\u058a\u058b\3\2\2\2\u058b\u058d\3")
        buf.write("\2\2\2\u058c\u058a\3\2\2\2\u058d\u058f\7\16\2\2\u058e")
        buf.write("\u0575\3\2\2\2\u058e\u058f\3\2\2\2\u058f\u0593\3\2\2\2")
        buf.write("\u0590\u0592\7\5\2\2\u0591\u0590\3\2\2\2\u0592\u0595\3")
        buf.write("\2\2\2\u0593\u0591\3\2\2\2\u0593\u0594\3\2\2\2\u0594\u00e9")
        buf.write("\3\2\2\2\u0595\u0593\3\2\2\2\u0596\u0597\7a\2\2\u0597")
        buf.write("\u059b\7\13\2\2\u0598\u059a\7\5\2\2\u0599\u0598\3\2\2")
        buf.write("\2\u059a\u059d\3\2\2\2\u059b\u0599\3\2\2\2\u059b\u059c")
        buf.write("\3\2\2\2\u059c\u059e\3\2\2\2\u059d\u059b\3\2\2\2\u059e")
        buf.write("\u05a9\5\u00f0y\2\u059f\u05a3\7\24\2\2\u05a0\u05a2\7\5")
        buf.write("\2\2\u05a1\u05a0\3\2\2\2\u05a2\u05a5\3\2\2\2\u05a3\u05a1")
        buf.write("\3\2\2\2\u05a3\u05a4\3\2\2\2\u05a4\u05a6\3\2\2\2\u05a5")
        buf.write("\u05a3\3\2\2\2\u05a6\u05a8\5\u00f0y\2\u05a7\u059f\3\2")
        buf.write("\2\2\u05a8\u05ab\3\2\2\2\u05a9\u05a7\3\2\2\2\u05a9\u05aa")
        buf.write("\3\2\2\2\u05aa\u00eb\3\2\2\2\u05ab\u05a9\3\2\2\2\u05ac")
        buf.write("\u05ad\7`\2\2\u05ad\u05ae\7\13\2\2\u05ae\u05b3\5\u00ee")
        buf.write("x\2\u05af\u05b0\7\24\2\2\u05b0\u05b2\5\u00eex\2\u05b1")
        buf.write("\u05af\3\2\2\2\u05b2\u05b5\3\2\2\2\u05b3\u05b1\3\2\2\2")
        buf.write("\u05b3\u05b4\3\2\2\2\u05b4\u00ed\3\2\2\2\u05b5\u05b3\3")
        buf.write("\2\2\2\u05b6\u05b7\t\3\2\2\u05b7\u00ef\3\2\2\2\u05b8\u05b9")
        buf.write("\t\3\2\2\u05b9\u00f1\3\2\2\2\u05ba\u05bb\7h\2\2\u05bb")
        buf.write("\u05bc\7\13\2\2\u05bc\u05c1\5\u00f4{\2\u05bd\u05be\7\24")
        buf.write("\2\2\u05be\u05c0\5\u00f4{\2\u05bf\u05bd\3\2\2\2\u05c0")
        buf.write("\u05c3\3\2\2\2\u05c1\u05bf\3\2\2\2\u05c1\u05c2\3\2\2\2")
        buf.write("\u05c2\u00f3\3\2\2\2\u05c3\u05c1\3\2\2\2\u05c4\u05d1\5")
        buf.write("\u00f6|\2\u05c5\u05cd\7\r\2\2\u05c6\u05cc\5\u00f8}\2\u05c7")
        buf.write("\u05cc\5\u00fa~\2\u05c8\u05cc\5\u00fc\177\2\u05c9\u05cc")
        buf.write("\7\5\2\2\u05ca\u05cc\7\24\2\2\u05cb\u05c6\3\2\2\2\u05cb")
        buf.write("\u05c7\3\2\2\2\u05cb\u05c8\3\2\2\2\u05cb\u05c9\3\2\2\2")
        buf.write("\u05cb\u05ca\3\2\2\2\u05cc\u05cf\3\2\2\2\u05cd\u05cb\3")
        buf.write("\2\2\2\u05cd\u05ce\3\2\2\2\u05ce\u05d0\3\2\2\2\u05cf\u05cd")
        buf.write("\3\2\2\2\u05d0\u05d2\7\16\2\2\u05d1\u05c5\3\2\2\2\u05d1")
        buf.write("\u05d2\3\2\2\2\u05d2\u00f5\3\2\2\2\u05d3\u05d4\5\32\16")
        buf.write("\2\u05d4\u00f7\3\2\2\2\u05d5\u05d6\7i\2\2\u05d6\u05d7")
        buf.write("\7\13\2\2\u05d7\u05d8\7\u0083\2\2\u05d8\u00f9\3\2\2\2")
        buf.write("\u05d9\u05da\7q\2\2\u05da\u05db\7\13\2\2\u05db\u05dc\7")
        buf.write("\7\2\2\u05dc\u00fb\3\2\2\2\u05dd\u05de\7x\2\2\u05de\u05df")
        buf.write("\7\13\2\2\u05df\u05e0\5 \21\2\u05e0\u00fd\3\2\2\2\u05e1")
        buf.write("\u05e2\7r\2\2\u05e2\u05e3\7\13\2\2\u05e3\u05e8\5\u0100")
        buf.write("\u0081\2\u05e4\u05e5\7\24\2\2\u05e5\u05e7\5\u0100\u0081")
        buf.write("\2\u05e6\u05e4\3\2\2\2\u05e7\u05ea\3\2\2\2\u05e8\u05e6")
        buf.write("\3\2\2\2\u05e8\u05e9\3\2\2\2\u05e9\u00ff\3\2\2\2\u05ea")
        buf.write("\u05e8\3\2\2\2\u05eb\u05ed\5\u0102\u0082\2\u05ec\u05ee")
        buf.write("\5\u0104\u0083\2\u05ed\u05ec\3\2\2\2\u05ed\u05ee\3\2\2")
        buf.write("\2\u05ee\u05ef\3\2\2\2\u05ef\u05f0\7\r\2\2\u05f0\u05f1")
        buf.write("\5 \21\2\u05f1\u05f2\7\16\2\2\u05f2\u0101\3\2\2\2\u05f3")
        buf.write("\u05f4\5\32\16\2\u05f4\u0103\3\2\2\2\u05f5\u05f6\t\3\2")
        buf.write("\2\u05f6\u0105\3\2\2\2\u05f7\u05f8\7s\2\2\u05f8\u05f9")
        buf.write("\7\13\2\2\u05f9\u05fd\5 \21\2\u05fa\u05fc\7\5\2\2\u05fb")
        buf.write("\u05fa\3\2\2\2\u05fc\u05ff\3\2\2\2\u05fd\u05fb\3\2\2\2")
        buf.write("\u05fd\u05fe\3\2\2\2\u05fe\u0107\3\2\2\2\u05ff\u05fd\3")
        buf.write("\2\2\2\u0600\u0601\7t\2\2\u0601\u0602\7\13\2\2\u0602\u0606")
        buf.write("\5 \21\2\u0603\u0605\7\5\2\2\u0604\u0603\3\2\2\2\u0605")
        buf.write("\u0608\3\2\2\2\u0606\u0604\3\2\2\2\u0606\u0607\3\2\2\2")
        buf.write("\u0607\u0109\3\2\2\2\u0608\u0606\3\2\2\2\u0609\u060a\7")
        buf.write("u\2\2\u060a\u060b\7\13\2\2\u060b\u060f\5 \21\2\u060c\u060e")
        buf.write("\7\5\2\2\u060d\u060c\3\2\2\2\u060e\u0611\3\2\2\2\u060f")
        buf.write("\u060d\3\2\2\2\u060f\u0610\3\2\2\2\u0610\u010b\3\2\2\2")
        buf.write("\u0611\u060f\3\2\2\2\u0612\u0613\7v\2\2\u0613\u0614\7")
        buf.write("\13\2\2\u0614\u0618\5 \21\2\u0615\u0617\7\5\2\2\u0616")
        buf.write("\u0615\3\2\2\2\u0617\u061a\3\2\2\2\u0618\u0616\3\2\2\2")
        buf.write("\u0618\u0619\3\2\2\2\u0619\u010d\3\2\2\2\u061a\u0618\3")
        buf.write("\2\2\2\u061b\u061c\7w\2\2\u061c\u061d\7\13\2\2\u061d\u0621")
        buf.write("\5 \21\2\u061e\u0620\7\5\2\2\u061f\u061e\3\2\2\2\u0620")
        buf.write("\u0623\3\2\2\2\u0621\u061f\3\2\2\2\u0621\u0622\3\2\2\2")
        buf.write("\u0622\u010f\3\2\2\2\u0623\u0621\3\2\2\2\u0624\u0625\7")
        buf.write("x\2\2\u0625\u0626\7\13\2\2\u0626\u062a\5 \21\2\u0627\u0629")
        buf.write("\7\5\2\2\u0628\u0627\3\2\2\2\u0629\u062c\3\2\2\2\u062a")
        buf.write("\u0628\3\2\2\2\u062a\u062b\3\2\2\2\u062b\u0111\3\2\2\2")
        buf.write("\u062c\u062a\3\2\2\2\u062d\u063c\7\u0084\2\2\u062e\u0638")
        buf.write("\7\r\2\2\u062f\u0639\5\u0114\u008b\2\u0630\u0635\5\u0116")
        buf.write("\u008c\2\u0631\u0632\7\24\2\2\u0632\u0634\5\u0116\u008c")
        buf.write("\2\u0633\u0631\3\2\2\2\u0634\u0637\3\2\2\2\u0635\u0633")
        buf.write("\3\2\2\2\u0635\u0636\3\2\2\2\u0636\u0639\3\2\2\2\u0637")
        buf.write("\u0635\3\2\2\2\u0638\u062f\3\2\2\2\u0638\u0630\3\2\2\2")
        buf.write("\u0639\u063a\3\2\2\2\u063a\u063b\7\16\2\2\u063b\u063d")
        buf.write("\3\2\2\2\u063c\u062e\3\2\2\2\u063c\u063d\3\2\2\2\u063d")
        buf.write("\u0113\3\2\2\2\u063e\u063f\7\34\2\2\u063f\u0115\3\2\2")
        buf.write("\2\u0640\u0641\5\32\16\2\u0641\u0117\3\2\2\2\u0642\u0645")
        buf.write("\7\u0085\2\2\u0643\u0644\7\25\2\2\u0644\u0646\5\u011e")
        buf.write("\u0090\2\u0645\u0643\3\2\2\2\u0645\u0646\3\2\2\2\u0646")
        buf.write("\u064b\3\2\2\2\u0647\u0648\7\r\2\2\u0648\u0649\5\u011a")
        buf.write("\u008e\2\u0649\u064a\7\16\2\2\u064a\u064c\3\2\2\2\u064b")
        buf.write("\u0647\3\2\2\2\u064b\u064c\3\2\2\2\u064c\u0119\3\2\2\2")
        buf.write("\u064d\u0653\5\u011c\u008f\2\u064e\u0652\5\u0142\u00a2")
        buf.write("\2\u064f\u0652\7\5\2\2\u0650\u0652\7\24\2\2\u0651\u064e")
        buf.write("\3\2\2\2\u0651\u064f\3\2\2\2\u0651\u0650\3\2\2\2\u0652")
        buf.write("\u0655\3\2\2\2\u0653\u0651\3\2\2\2\u0653\u0654\3\2\2\2")
        buf.write("\u0654\u011b\3\2\2\2\u0655\u0653\3\2\2\2\u0656\u0663\5")
        buf.write("\u012e\u0098\2\u0657\u0663\5\u0120\u0091\2\u0658\u0663")
        buf.write("\5\u0132\u009a\2\u0659\u0663\5\u0122\u0092\2\u065a\u0663")
        buf.write("\5\u0124\u0093\2\u065b\u0663\5\u0126\u0094\2\u065c\u0663")
        buf.write("\5\u0128\u0095\2\u065d\u0663\5\u012a\u0096\2\u065e\u0663")
        buf.write("\5\u012c\u0097\2\u065f\u0663\5\u013a\u009e\2\u0660\u0663")
        buf.write("\7\5\2\2\u0661\u0663\7\24\2\2\u0662\u0656\3\2\2\2\u0662")
        buf.write("\u0657\3\2\2\2\u0662\u0658\3\2\2\2\u0662\u0659\3\2\2\2")
        buf.write("\u0662\u065a\3\2\2\2\u0662\u065b\3\2\2\2\u0662\u065c\3")
        buf.write("\2\2\2\u0662\u065d\3\2\2\2\u0662\u065e\3\2\2\2\u0662\u065f")
        buf.write("\3\2\2\2\u0662\u0660\3\2\2\2\u0662\u0661\3\2\2\2\u0663")
        buf.write("\u0666\3\2\2\2\u0664\u0662\3\2\2\2\u0664\u0665\3\2\2\2")
        buf.write("\u0665\u011d\3\2\2\2\u0666\u0664\3\2\2\2\u0667\u0668\5")
        buf.write("\32\16\2\u0668\u011f\3\2\2\2\u0669\u066a\7p\2\2\u066a")
        buf.write("\u066b\7\13\2\2\u066b\u066f\7\4\2\2\u066c\u066e\7\5\2")
        buf.write("\2\u066d\u066c\3\2\2\2\u066e\u0671\3\2\2\2\u066f\u066d")
        buf.write("\3\2\2\2\u066f\u0670\3\2\2\2\u0670\u0121\3\2\2\2\u0671")
        buf.write("\u066f\3\2\2\2\u0672\u0673\7m\2\2\u0673\u0677\5&\24\2")
        buf.write("\u0674\u0676\7\5\2\2\u0675\u0674\3\2\2\2\u0676\u0679\3")
        buf.write("\2\2\2\u0677\u0675\3\2\2\2\u0677\u0678\3\2\2\2\u0678\u0123")
        buf.write("\3\2\2\2\u0679\u0677\3\2\2\2\u067a\u067c\7l\2\2\u067b")
        buf.write("\u067d\7\13\2\2\u067c\u067b\3\2\2\2\u067c\u067d\3\2\2")
        buf.write("\2\u067d\u067e\3\2\2\2\u067e\u0682\5&\24\2\u067f\u0681")
        buf.write("\7\5\2\2\u0680\u067f\3\2\2\2\u0681\u0684\3\2\2\2\u0682")
        buf.write("\u0680\3\2\2\2\u0682\u0683\3\2\2\2\u0683\u0125\3\2\2\2")
        buf.write("\u0684\u0682\3\2\2\2\u0685\u0687\7P\2\2\u0686\u0688\7")
        buf.write("\13\2\2\u0687\u0686\3\2\2\2\u0687\u0688\3\2\2\2\u0688")
        buf.write("\u0689\3\2\2\2\u0689\u068d\5&\24\2\u068a\u068c\7\5\2\2")
        buf.write("\u068b\u068a\3\2\2\2\u068c\u068f\3\2\2\2\u068d\u068b\3")
        buf.write("\2\2\2\u068d\u068e\3\2\2\2\u068e\u0127\3\2\2\2\u068f\u068d")
        buf.write("\3\2\2\2\u0690\u0692\7O\2\2\u0691\u0693\7\13\2\2\u0692")
        buf.write("\u0691\3\2\2\2\u0692\u0693\3\2\2\2\u0693\u0694\3\2\2\2")
        buf.write("\u0694\u0698\5&\24\2\u0695\u0697\7\5\2\2\u0696\u0695\3")
        buf.write("\2\2\2\u0697\u069a\3\2\2\2\u0698\u0696\3\2\2\2\u0698\u0699")
        buf.write("\3\2\2\2\u0699\u0129\3\2\2\2\u069a\u0698\3\2\2\2\u069b")
        buf.write("\u069c\7t\2\2\u069c\u069d\7\13\2\2\u069d\u06a1\5 \21\2")
        buf.write("\u069e\u06a0\7\5\2\2\u069f\u069e\3\2\2\2\u06a0\u06a3\3")
        buf.write("\2\2\2\u06a1\u069f\3\2\2\2\u06a1\u06a2\3\2\2\2\u06a2\u012b")
        buf.write("\3\2\2\2\u06a3\u06a1\3\2\2\2\u06a4\u06a5\7j\2\2\u06a5")
        buf.write("\u06a6\7\13\2\2\u06a6\u06aa\5\32\16\2\u06a7\u06a9\7\5")
        buf.write("\2\2\u06a8\u06a7\3\2\2\2\u06a9\u06ac\3\2\2\2\u06aa\u06a8")
        buf.write("\3\2\2\2\u06aa\u06ab\3\2\2\2\u06ab\u012d\3\2\2\2\u06ac")
        buf.write("\u06aa\3\2\2\2\u06ad\u06ae\7x\2\2\u06ae\u06af\7\13\2\2")
        buf.write("\u06af\u06b1\5 \21\2\u06b0\u06b2\5\u0130\u0099\2\u06b1")
        buf.write("\u06b0\3\2\2\2\u06b1\u06b2\3\2\2\2\u06b2\u06b6\3\2\2\2")
        buf.write("\u06b3\u06b5\7\5\2\2\u06b4\u06b3\3\2\2\2\u06b5\u06b8\3")
        buf.write("\2\2\2\u06b6\u06b4\3\2\2\2\u06b6\u06b7\3\2\2\2\u06b7\u012f")
        buf.write("\3\2\2\2\u06b8\u06b6\3\2\2\2\u06b9\u06ba\5$\23\2\u06ba")
        buf.write("\u0131\3\2\2\2\u06bb\u06bc\7n\2\2\u06bc\u06bd\7\r\2\2")
        buf.write("\u06bd\u06c2\5\u0134\u009b\2\u06be\u06bf\7\24\2\2\u06bf")
        buf.write("\u06c1\5\u0134\u009b\2\u06c0\u06be\3\2\2\2\u06c1\u06c4")
        buf.write("\3\2\2\2\u06c2\u06c0\3\2\2\2\u06c2\u06c3\3\2\2\2\u06c3")
        buf.write("\u06c5\3\2\2\2\u06c4\u06c2\3\2\2\2\u06c5\u06c6\7\16\2")
        buf.write("\2\u06c6\u0133\3\2\2\2\u06c7\u06cb\7\u0086\2\2\u06c8\u06c9")
        buf.write("\7\13\2\2\u06c9\u06cc\5\u0136\u009c\2\u06ca\u06cc\5\u0138")
        buf.write("\u009d\2\u06cb\u06c8\3\2\2\2\u06cb\u06ca\3\2\2\2\u06cb")
        buf.write("\u06cc\3\2\2\2\u06cc\u0135\3\2\2\2\u06cd\u06ce\5\36\20")
        buf.write("\2\u06ce\u0137\3\2\2\2\u06cf\u06d0\5\34\17\2\u06d0\u0139")
        buf.write("\3\2\2\2\u06d1\u06d2\7k\2\2\u06d2\u06d3\7\13\2\2\u06d3")
        buf.write("\u06d7\5\u013c\u009f\2\u06d4\u06d6\7\5\2\2\u06d5\u06d4")
        buf.write("\3\2\2\2\u06d6\u06d9\3\2\2\2\u06d7\u06d5\3\2\2\2\u06d7")
        buf.write("\u06d8\3\2\2\2\u06d8\u013b\3\2\2\2\u06d9\u06d7\3\2\2\2")
        buf.write("\u06da\u06db\7o\2\2\u06db\u06de\5\u013e\u00a0\2\u06dc")
        buf.write("\u06dd\7\61\2\2\u06dd\u06df\5\u0140\u00a1\2\u06de\u06dc")
        buf.write("\3\2\2\2\u06de\u06df\3\2\2\2\u06df\u013d\3\2\2\2\u06e0")
        buf.write("\u06e1\5\32\16\2\u06e1\u013f\3\2\2\2\u06e2\u06e3\5\32")
        buf.write("\16\2\u06e3\u0141\3\2\2\2\u06e4\u06e5\7h\2\2\u06e5\u06e9")
        buf.write("\7\13\2\2\u06e6\u06ea\5\u0144\u00a3\2\u06e7\u06ea\7\24")
        buf.write("\2\2\u06e8\u06ea\7\5\2\2\u06e9\u06e6\3\2\2\2\u06e9\u06e7")
        buf.write("\3\2\2\2\u06e9\u06e8\3\2\2\2\u06ea\u06eb\3\2\2\2\u06eb")
        buf.write("\u06e9\3\2\2\2\u06eb\u06ec\3\2\2\2\u06ec\u0143\3\2\2\2")
        buf.write("\u06ed\u06ee\5\u0146\u00a4\2\u06ee\u06ef\7\r\2\2\u06ef")
        buf.write("\u06f0\5\u011a\u008e\2\u06f0\u06f1\7\16\2\2\u06f1\u0145")
        buf.write("\3\2\2\2\u06f2\u06f3\5\32\16\2\u06f3\u0147\3\2\2\2\u06f4")
        buf.write("\u06f5\7\u0087\2\2\u06f5\u06f6\7\r\2\2\u06f6\u06f7\5\u014a")
        buf.write("\u00a6\2\u06f7\u06f8\7\16\2\2\u06f8\u0149\3\2\2\2\u06f9")
        buf.write("\u06fe\5\32\16\2\u06fa\u06fb\7\24\2\2\u06fb\u06fd\5\32")
        buf.write("\16\2\u06fc\u06fa\3\2\2\2\u06fd\u0700\3\2\2\2\u06fe\u06fc")
        buf.write("\3\2\2\2\u06fe\u06ff\3\2\2\2\u06ff\u014b\3\2\2\2\u0700")
        buf.write("\u06fe\3\2\2\2\u0701\u0702\7\u0088\2\2\u0702\u0703\5&")
        buf.write("\24\2\u0703\u014d\3\2\2\2\u0704\u0705\7\u0089\2\2\u0705")
        buf.write("\u0706\5&\24\2\u0706\u014f\3\2\2\2\u0707\u070c\7\u008a")
        buf.write("\2\2\u0708\u0709\7\r\2\2\u0709\u070a\5\u0152\u00aa\2\u070a")
        buf.write("\u070b\7\16\2\2\u070b\u070d\3\2\2\2\u070c\u0708\3\2\2")
        buf.write("\2\u070c\u070d\3\2\2\2\u070d\u0151\3\2\2\2\u070e\u070f")
        buf.write("\7_\2\2\u070f\u0153\3\2\2\2\u0710\u0711\7\u008b\2\2\u0711")
        buf.write("\u0712\7\r\2\2\u0712\u0713\5\34\17\2\u0713\u0714\7\16")
        buf.write("\2\2\u0714\u0155\3\2\2\2\u0715\u0716\7\u008c\2\2\u0716")
        buf.write("\u0717\7\r\2\2\u0717\u0718\5\u0158\u00ad\2\u0718\u0719")
        buf.write("\7\16\2\2\u0719\u0157\3\2\2\2\u071a\u071b\5\32\16\2\u071b")
        buf.write("\u0159\3\2\2\2\u071c\u071d\7\u008d\2\2\u071d\u071e\5&")
        buf.write("\24\2\u071e\u015b\3\2\2\2\u071f\u0720\7\u008e\2\2\u0720")
        buf.write("\u0721\5&\24\2\u0721\u015d\3\2\2\2\u0722\u0723\7\u008f")
        buf.write("\2\2\u0723\u0724\5&\24\2\u0724\u015f\3\2\2\2\u0725\u0726")
        buf.write("\7\u0090\2\2\u0726\u0727\5&\24\2\u0727\u0161\3\2\2\2\u0728")
        buf.write("\u0729\7\u0091\2\2\u0729\u072a\7\r\2\2\u072a\u072b\5\u0164")
        buf.write("\u00b3\2\u072b\u072c\7\16\2\2\u072c\u0163\3\2\2\2\u072d")
        buf.write("\u072e\5\32\16\2\u072e\u0165\3\2\2\2\u072f\u0733\5\u0168")
        buf.write("\u00b5\2\u0730\u0732\7\5\2\2\u0731\u0730\3\2\2\2\u0732")
        buf.write("\u0735\3\2\2\2\u0733\u0731\3\2\2\2\u0733\u0734\3\2\2\2")
        buf.write("\u0734\u0736\3\2\2\2\u0735\u0733\3\2\2\2\u0736\u073a\5")
        buf.write("\u0182\u00c2\2\u0737\u0739\7\5\2\2\u0738\u0737\3\2\2\2")
        buf.write("\u0739\u073c\3\2\2\2\u073a\u0738\3\2\2\2\u073a\u073b\3")
        buf.write("\2\2\2\u073b\u0167\3\2\2\2\u073c\u073a\3\2\2\2\u073d\u073f")
        buf.write("\7\17\2\2\u073e\u0740\5\u016a\u00b6\2\u073f\u073e\3\2")
        buf.write("\2\2\u073f\u0740\3\2\2\2\u0740\u0741\3\2\2\2\u0741\u0743")
        buf.write("\5\u0180\u00c1\2\u0742\u0744\5\u016c\u00b7\2\u0743\u0742")
        buf.write("\3\2\2\2\u0743\u0744\3\2\2\2\u0744\u074d\3\2\2\2\u0745")
        buf.write("\u0747\7\13\2\2\u0746\u0748\5\u0176\u00bc\2\u0747\u0746")
        buf.write("\3\2\2\2\u0747\u0748\3\2\2\2\u0748\u074b\3\2\2\2\u0749")
        buf.write("\u074a\7\13\2\2\u074a\u074c\5\u0170\u00b9\2\u074b\u0749")
        buf.write("\3\2\2\2\u074b\u074c\3\2\2\2\u074c\u074e\3\2\2\2\u074d")
        buf.write("\u0745\3\2\2\2\u074d\u074e\3\2\2\2\u074e\u074f\3\2\2\2")
        buf.write("\u074f\u0751\7\20\2\2\u0750\u0752\7\5\2\2\u0751\u0750")
        buf.write("\3\2\2\2\u0751\u0752\3\2\2\2\u0752\u0169\3\2\2\2\u0753")
        buf.write("\u0754\5\32\16\2\u0754\u0755\7\25\2\2\u0755\u0757\3\2")
        buf.write("\2\2\u0756\u0753\3\2\2\2\u0756\u0757\3\2\2\2\u0757\u0758")
        buf.write("\3\2\2\2\u0758\u0759\5\32\16\2\u0759\u075a\t\f\2\2\u075a")
        buf.write("\u075b\7\n\2\2\u075b\u016b\3\2\2\2\u075c\u075d\7\61\2")
        buf.write("\2\u075d\u075e\5\u016e\u00b8\2\u075e\u016d\3\2\2\2\u075f")
        buf.write("\u0760\5\32\16\2\u0760\u016f\3\2\2\2\u0761\u0764\5\u0172")
        buf.write("\u00ba\2\u0762\u0764\5&\24\2\u0763\u0761\3\2\2\2\u0763")
        buf.write("\u0762\3\2\2\2\u0764\u0171\3\2\2\2\u0765\u076a\5\u0174")
        buf.write("\u00bb\2\u0766\u0767\7\27\2\2\u0767\u0769\5\u0174\u00bb")
        buf.write("\2\u0768\u0766\3\2\2\2\u0769\u076c\3\2\2\2\u076a\u0768")
        buf.write("\3\2\2\2\u076a\u076b\3\2\2\2\u076b\u0173\3\2\2\2\u076c")
        buf.write("\u076a\3\2\2\2\u076d\u0773\5\32\16\2\u076e\u0773\7\7\2")
        buf.write("\2\u076f\u0773\7\23\2\2\u0770\u0773\7\22\2\2\u0771\u0773")
        buf.write("\7\25\2\2\u0772\u076d\3\2\2\2\u0772\u076e\3\2\2\2\u0772")
        buf.write("\u076f\3\2\2\2\u0772\u0770\3\2\2\2\u0772\u0771\3\2\2\2")
        buf.write("\u0773\u0774\3\2\2\2\u0774\u0772\3\2\2\2\u0774\u0775\3")
        buf.write("\2\2\2\u0775\u0175\3\2\2\2\u0776\u0778\t\r\2\2\u0777\u0776")
        buf.write("\3\2\2\2\u0777\u0778\3\2\2\2\u0778\u0779\3\2\2\2\u0779")
        buf.write("\u077a\5\u017e\u00c0\2\u077a\u0177\3\2\2\2\u077b\u077f")
        buf.write("\5\32\16\2\u077c\u077f\7\23\2\2\u077d\u077f\7\7\2\2\u077e")
        buf.write("\u077b\3\2\2\2\u077e\u077c\3\2\2\2\u077e\u077d\3\2\2\2")
        buf.write("\u077f\u0780\3\2\2\2\u0780\u077e\3\2\2\2\u0780\u0781\3")
        buf.write("\2\2\2\u0781\u0179\3\2\2\2\u0782\u0783\7\t\2\2\u0783\u0784")
        buf.write("\5\32\16\2\u0784\u0785\7\n\2\2\u0785\u017b\3\2\2\2\u0786")
        buf.write("\u0789\5\u0178\u00bd\2\u0787\u0789\5\u017a\u00be\2\u0788")
        buf.write("\u0786\3\2\2\2\u0788\u0787\3\2\2\2\u0789\u017d\3\2\2\2")
        buf.write("\u078a\u0795\7\27\2\2\u078b\u078c\7\27\2\2\u078c\u078e")
        buf.write("\5\u017c\u00bf\2\u078d\u078b\3\2\2\2\u078e\u078f\3\2\2")
        buf.write("\2\u078f\u078d\3\2\2\2\u078f\u0790\3\2\2\2\u0790\u0792")
        buf.write("\3\2\2\2\u0791\u0793\7\27\2\2\u0792\u0791\3\2\2\2\u0792")
        buf.write("\u0793\3\2\2\2\u0793\u0795\3\2\2\2\u0794\u078a\3\2\2\2")
        buf.write("\u0794\u078d\3\2\2\2\u0795\u017f\3\2\2\2\u0796\u0797\5")
        buf.write("\32\16\2\u0797\u0181\3\2\2\2\u0798\u079a\5\u0186\u00c4")
        buf.write("\2\u0799\u0798\3\2\2\2\u079a\u079d\3\2\2\2\u079b\u0799")
        buf.write("\3\2\2\2\u079b\u079c\3\2\2\2\u079c\u07a1\3\2\2\2\u079d")
        buf.write("\u079b\3\2\2\2\u079e\u07a0\5\u018c\u00c7\2\u079f\u079e")
        buf.write("\3\2\2\2\u07a0\u07a3\3\2\2\2\u07a1\u079f\3\2\2\2\u07a1")
        buf.write("\u07a2\3\2\2\2\u07a2\u07a5\3\2\2\2\u07a3\u07a1\3\2\2\2")
        buf.write("\u07a4\u07a6\5\u0184\u00c3\2\u07a5\u07a4\3\2\2\2\u07a5")
        buf.write("\u07a6\3\2\2\2\u07a6\u07aa\3\2\2\2\u07a7\u07a9\7\5\2\2")
        buf.write("\u07a8\u07a7\3\2\2\2\u07a9\u07ac\3\2\2\2\u07aa\u07a8\3")
        buf.write("\2\2\2\u07aa\u07ab\3\2\2\2\u07ab\u07b0\3\2\2\2\u07ac\u07aa")
        buf.write("\3\2\2\2\u07ad\u07af\5\u0192\u00ca\2\u07ae\u07ad\3\2\2")
        buf.write("\2\u07af\u07b2\3\2\2\2\u07b0\u07ae\3\2\2\2\u07b0\u07b1")
        buf.write("\3\2\2\2\u07b1\u0183\3\2\2\2\u07b2\u07b0\3\2\2\2\u07b3")
        buf.write("\u07b4\5&\24\2\u07b4\u0185\3\2\2\2\u07b5\u07b6\5\u0188")
        buf.write("\u00c5\2\u07b6\u07b7\7&\2\2\u07b7\u07be\5\u018a\u00c6")
        buf.write("\2\u07b8\u07ba\7\5\2\2\u07b9\u07b8\3\2\2\2\u07ba\u07bb")
        buf.write("\3\2\2\2\u07bb\u07b9\3\2\2\2\u07bb\u07bc\3\2\2\2\u07bc")
        buf.write("\u07bf\3\2\2\2\u07bd\u07bf\7\2\2\3\u07be\u07b9\3\2\2\2")
        buf.write("\u07be\u07bd\3\2\2\2\u07bf\u0187\3\2\2\2\u07c0\u07c1\5")
        buf.write("\32\16\2\u07c1\u0189\3\2\2\2\u07c2\u07c3\7*\2\2\u07c3")
        buf.write("\u018b\3\2\2\2\u07c4\u07c5\5\u018e\u00c8\2\u07c5\u07c7")
        buf.write("\7\r\2\2\u07c6\u07c8\5\u0190\u00c9\2\u07c7\u07c6\3\2\2")
        buf.write("\2\u07c7\u07c8\3\2\2\2\u07c8\u07c9\3\2\2\2\u07c9\u07cb")
        buf.write("\7\16\2\2\u07ca\u07cc\5*\26\2\u07cb\u07ca\3\2\2\2\u07cb")
        buf.write("\u07cc\3\2\2\2\u07cc\u07d3\3\2\2\2\u07cd\u07cf\7\5\2\2")
        buf.write("\u07ce\u07cd\3\2\2\2\u07cf\u07d0\3\2\2\2\u07d0\u07ce\3")
        buf.write("\2\2\2\u07d0\u07d1\3\2\2\2\u07d1\u07d4\3\2\2\2\u07d2\u07d4")
        buf.write("\7\2\2\3\u07d3\u07ce\3\2\2\2\u07d3\u07d2\3\2\2\2\u07d4")
        buf.write("\u018d\3\2\2\2\u07d5\u07d6\5\32\16\2\u07d6\u018f\3\2\2")
        buf.write("\2\u07d7\u07dc\5\32\16\2\u07d8\u07d9\7\24\2\2\u07d9\u07db")
        buf.write("\5\32\16\2\u07da\u07d8\3\2\2\2\u07db\u07de\3\2\2\2\u07dc")
        buf.write("\u07da\3\2\2\2\u07dc\u07dd\3\2\2\2\u07dd\u0191\3\2\2\2")
        buf.write("\u07de\u07dc\3\2\2\2\u07df\u07f2\5\u0194\u00cb\2\u07e0")
        buf.write("\u07f2\5\u01a0\u00d1\2\u07e1\u07f2\5\u01a4\u00d3\2\u07e2")
        buf.write("\u07f2\5\u01aa\u00d6\2\u07e3\u07f2\5\u01ae\u00d8\2\u07e4")
        buf.write("\u07f2\5\u01b2\u00da\2\u07e5\u07f2\5\u01fc\u00ff\2\u07e6")
        buf.write("\u07f2\5\u01fe\u0100\2\u07e7\u07f2\5\u0200\u0101\2\u07e8")
        buf.write("\u07f2\5\u0202\u0102\2\u07e9\u07f2\5\u01b4\u00db\2\u07ea")
        buf.write("\u07f2\5\u0204\u0103\2\u07eb\u07f2\5\u0206\u0104\2\u07ec")
        buf.write("\u07f2\5\u0220\u0111\2\u07ed\u07f2\5\u0222\u0112\2\u07ee")
        buf.write("\u07f2\5\u0224\u0113\2\u07ef\u07f2\5\u0226\u0114\2\u07f0")
        buf.write("\u07f2\7\5\2\2\u07f1\u07df\3\2\2\2\u07f1\u07e0\3\2\2\2")
        buf.write("\u07f1\u07e1\3\2\2\2\u07f1\u07e2\3\2\2\2\u07f1\u07e3\3")
        buf.write("\2\2\2\u07f1\u07e4\3\2\2\2\u07f1\u07e5\3\2\2\2\u07f1\u07e6")
        buf.write("\3\2\2\2\u07f1\u07e7\3\2\2\2\u07f1\u07e8\3\2\2\2\u07f1")
        buf.write("\u07e9\3\2\2\2\u07f1\u07ea\3\2\2\2\u07f1\u07eb\3\2\2\2")
        buf.write("\u07f1\u07ec\3\2\2\2\u07f1\u07ed\3\2\2\2\u07f1\u07ee\3")
        buf.write("\2\2\2\u07f1\u07ef\3\2\2\2\u07f1\u07f0\3\2\2\2\u07f2\u0193")
        buf.write("\3\2\2\2\u07f3\u07f4\7\u0092\2\2\u07f4\u07f7\7\r\2\2\u07f5")
        buf.write("\u07f8\5\u0196\u00cc\2\u07f6\u07f8\7\5\2\2\u07f7\u07f5")
        buf.write("\3\2\2\2\u07f7\u07f6\3\2\2\2\u07f8\u07f9\3\2\2\2\u07f9")
        buf.write("\u07f7\3\2\2\2\u07f9\u07fa\3\2\2\2\u07fa\u07fb\3\2\2\2")
        buf.write("\u07fb\u07fc\7\16\2\2\u07fc\u0195\3\2\2\2\u07fd\u07ff")
        buf.write("\5\u0198\u00cd\2\u07fe\u0800\5\u019a\u00ce\2\u07ff\u07fe")
        buf.write("\3\2\2\2\u07ff\u0800\3\2\2\2\u0800\u0802\3\2\2\2\u0801")
        buf.write("\u0803\5\u019c\u00cf\2\u0802\u0801\3\2\2\2\u0802\u0803")
        buf.write("\3\2\2\2\u0803\u0805\3\2\2\2\u0804\u0806\7\24\2\2\u0805")
        buf.write("\u0804\3\2\2\2\u0805\u0806\3\2\2\2\u0806\u0808\3\2\2\2")
        buf.write("\u0807\u0809\7\5\2\2\u0808\u0807\3\2\2\2\u0808\u0809\3")
        buf.write("\2\2\2\u0809\u0197\3\2\2\2\u080a\u080d\5\36\20\2\u080b")
        buf.write("\u080d\5\34\17\2\u080c\u080a\3\2\2\2\u080c\u080b\3\2\2")
        buf.write("\2\u080d\u0199\3\2\2\2\u080e\u080f\5*\26\2\u080f\u019b")
        buf.write("\3\2\2\2\u0810\u0811\7\30\2\2\u0811\u081b\7\n\2\2\u0812")
        buf.write("\u081c\7\34\2\2\u0813\u0818\5\u019e\u00d0\2\u0814\u0815")
        buf.write("\7\24\2\2\u0815\u0817\5\u019e\u00d0\2\u0816\u0814\3\2")
        buf.write("\2\2\u0817\u081a\3\2\2\2\u0818\u0816\3\2\2\2\u0818\u0819")
        buf.write("\3\2\2\2\u0819\u081c\3\2\2\2\u081a\u0818\3\2\2\2\u081b")
        buf.write("\u0812\3\2\2\2\u081b\u0813\3\2\2\2\u081c\u019d\3\2\2\2")
        buf.write("\u081d\u081e\5\32\16\2\u081e\u019f\3\2\2\2\u081f\u0825")
        buf.write("\7\u0093\2\2\u0820\u0822\7\r\2\2\u0821\u0823\5\u01a2\u00d2")
        buf.write("\2\u0822\u0821\3\2\2\2\u0822\u0823\3\2\2\2\u0823\u0824")
        buf.write("\3\2\2\2\u0824\u0826\7\16\2\2\u0825\u0820\3\2\2\2\u0825")
        buf.write("\u0826\3\2\2\2\u0826\u01a1\3\2\2\2\u0827\u0828\7N\2\2")
        buf.write("\u0828\u0829\7\13\2\2\u0829\u082a\7\4\2\2\u082a\u01a3")
        buf.write("\3\2\2\2\u082b\u082e\5\u01a6\u00d4\2\u082c\u082d\7\25")
        buf.write("\2\2\u082d\u082f\5\u01a8\u00d5\2\u082e\u082c\3\2\2\2\u082e")
        buf.write("\u082f\3\2\2\2\u082f\u0830\3\2\2\2\u0830\u0831\5*\26\2")
        buf.write("\u0831\u01a5\3\2\2\2\u0832\u0833\t\16\2\2\u0833\u01a7")
        buf.write("\3\2\2\2\u0834\u0835\5\32\16\2\u0835\u01a9\3\2\2\2\u0836")
        buf.write("\u0839\7\u0097\2\2\u0837\u0838\7\25\2\2\u0838\u083a\5")
        buf.write("\u01ac\u00d7\2\u0839\u0837\3\2\2\2\u0839\u083a\3\2\2\2")
        buf.write("\u083a\u083b\3\2\2\2\u083b\u083c\5*\26\2\u083c\u01ab\3")
        buf.write("\2\2\2\u083d\u083e\5\32\16\2\u083e\u01ad\3\2\2\2\u083f")
        buf.write("\u0842\7\u0098\2\2\u0840\u0841\7\25\2\2\u0841\u0843\5")
        buf.write("\u01b0\u00d9\2\u0842\u0840\3\2\2\2\u0842\u0843\3\2\2\2")
        buf.write("\u0843\u0844\3\2\2\2\u0844\u0845\5*\26\2\u0845\u01af\3")
        buf.write("\2\2\2\u0846\u0847\5\32\16\2\u0847\u01b1\3\2\2\2\u0848")
        buf.write("\u0849\7\u0099\2\2\u0849\u084a\5\u01b6\u00dc\2\u084a\u01b3")
        buf.write("\3\2\2\2\u084b\u084c\7\u009a\2\2\u084c\u084d\5\u01b6\u00dc")
        buf.write("\2\u084d\u01b5\3\2\2\2\u084e\u084f\7\25\2\2\u084f\u0851")
        buf.write("\5\u01ba\u00de\2\u0850\u084e\3\2\2\2\u0850\u0851\3\2\2")
        buf.write("\2\u0851\u0852\3\2\2\2\u0852\u0856\7\r\2\2\u0853\u0855")
        buf.write("\7\5\2\2\u0854\u0853\3\2\2\2\u0855\u0858\3\2\2\2\u0856")
        buf.write("\u0854\3\2\2\2\u0856\u0857\3\2\2\2\u0857\u0859\3\2\2\2")
        buf.write("\u0858\u0856\3\2\2\2\u0859\u085b\5\u01c4\u00e3\2\u085a")
        buf.write("\u085c\5\u01c6\u00e4\2\u085b\u085a\3\2\2\2\u085b\u085c")
        buf.write("\3\2\2\2\u085c\u086e\3\2\2\2\u085d\u086d\5\u01c8\u00e5")
        buf.write("\2\u085e\u086d\5\u01dc\u00ef\2\u085f\u086d\5\u01e2\u00f2")
        buf.write("\2\u0860\u086d\5\u01f4\u00fb\2\u0861\u086d\5\u01da\u00ee")
        buf.write("\2\u0862\u086d\5\u01d2\u00ea\2\u0863\u086d\5\u01d8\u00ed")
        buf.write("\2\u0864\u086d\5\u01d4\u00eb\2\u0865\u086d\5\u01d6\u00ec")
        buf.write("\2\u0866\u086d\5\u01ca\u00e6\2\u0867\u086d\5\u01ce\u00e8")
        buf.write("\2\u0868\u086d\5\u01e4\u00f3\2\u0869\u086d\5\u01e8\u00f5")
        buf.write("\2\u086a\u086d\7\5\2\2\u086b\u086d\7\24\2\2\u086c\u085d")
        buf.write("\3\2\2\2\u086c\u085e\3\2\2\2\u086c\u085f\3\2\2\2\u086c")
        buf.write("\u0860\3\2\2\2\u086c\u0861\3\2\2\2\u086c\u0862\3\2\2\2")
        buf.write("\u086c\u0863\3\2\2\2\u086c\u0864\3\2\2\2\u086c\u0865\3")
        buf.write("\2\2\2\u086c\u0866\3\2\2\2\u086c\u0867\3\2\2\2\u086c\u0868")
        buf.write("\3\2\2\2\u086c\u0869\3\2\2\2\u086c\u086a\3\2\2\2\u086c")
        buf.write("\u086b\3\2\2\2\u086d\u0870\3\2\2\2\u086e\u086c\3\2\2\2")
        buf.write("\u086e\u086f\3\2\2\2\u086f\u0874\3\2\2\2\u0870\u086e\3")
        buf.write("\2\2\2\u0871\u0873\7\5\2\2\u0872\u0871\3\2\2\2\u0873\u0876")
        buf.write("\3\2\2\2\u0874\u0872\3\2\2\2\u0874\u0875\3\2\2\2\u0875")
        buf.write("\u0879\3\2\2\2\u0876\u0874\3\2\2\2\u0877\u087a\5\u01bc")
        buf.write("\u00df\2\u0878\u087a\5\u01c0\u00e1\2\u0879\u0877\3\2\2")
        buf.write("\2\u0879\u0878\3\2\2\2\u0879\u087a\3\2\2\2\u087a\u087e")
        buf.write("\3\2\2\2\u087b\u087d\7\5\2\2\u087c\u087b\3\2\2\2\u087d")
        buf.write("\u0880\3\2\2\2\u087e\u087c\3\2\2\2\u087e\u087f\3\2\2\2")
        buf.write("\u087f\u0884\3\2\2\2\u0880\u087e\3\2\2\2\u0881\u0883\5")
        buf.write("\u01b8\u00dd\2\u0882\u0881\3\2\2\2\u0883\u0886\3\2\2\2")
        buf.write("\u0884\u0882\3\2\2\2\u0884\u0885\3\2\2\2\u0885\u088a\3")
        buf.write("\2\2\2\u0886\u0884\3\2\2\2\u0887\u0889\7\5\2\2\u0888\u0887")
        buf.write("\3\2\2\2\u0889\u088c\3\2\2\2\u088a\u0888\3\2\2\2\u088a")
        buf.write("\u088b\3\2\2\2\u088b\u088d\3\2\2\2\u088c\u088a\3\2\2\2")
        buf.write("\u088d\u088e\7\16\2\2\u088e\u01b7\3\2\2\2\u088f\u0893")
        buf.write("\5\u01e0\u00f1\2\u0890\u0892\7\5\2\2\u0891\u0890\3\2\2")
        buf.write("\2\u0892\u0895\3\2\2\2\u0893\u0891\3\2\2\2\u0893\u0894")
        buf.write("\3\2\2\2\u0894\u0896\3\2\2\2\u0895\u0893\3\2\2\2\u0896")
        buf.write("\u089a\7\r\2\2\u0897\u0899\7\5\2\2\u0898\u0897\3\2\2\2")
        buf.write("\u0899\u089c\3\2\2\2\u089a\u0898\3\2\2\2\u089a\u089b\3")
        buf.write("\2\2\2\u089b\u089d\3\2\2\2\u089c\u089a\3\2\2\2\u089d\u08a1")
        buf.write("\5\u0182\u00c2\2\u089e\u08a0\7\5\2\2\u089f\u089e\3\2\2")
        buf.write("\2\u08a0\u08a3\3\2\2\2\u08a1\u089f\3\2\2\2\u08a1\u08a2")
        buf.write("\3\2\2\2\u08a2\u08a4\3\2\2\2\u08a3\u08a1\3\2\2\2\u08a4")
        buf.write("\u08a8\7\16\2\2\u08a5\u08a7\7\5\2\2\u08a6\u08a5\3\2\2")
        buf.write("\2\u08a7\u08aa\3\2\2\2\u08a8\u08a6\3\2\2\2\u08a8\u08a9")
        buf.write("\3\2\2\2\u08a9\u01b9\3\2\2\2\u08aa\u08a8\3\2\2\2\u08ab")
        buf.write("\u08ac\5\32\16\2\u08ac\u01bb\3\2\2\2\u08ad\u08ae\7\r\2")
        buf.write("\2\u08ae\u08af\5\u01be\u00e0\2\u08af\u08b0\7\16\2\2\u08b0")
        buf.write("\u08b2\3\2\2\2\u08b1\u08ad\3\2\2\2\u08b1\u08b2\3\2\2\2")
        buf.write("\u08b2\u08b3\3\2\2\2\u08b3\u08b4\7\30\2\2\u08b4\u08b5")
        buf.write("\7\n\2\2\u08b5\u08b6\5*\26\2\u08b6\u01bd\3\2\2\2\u08b7")
        buf.write("\u08b8\t\17\2\2\u08b8\u01bf\3\2\2\2\u08b9\u08ba\7\r\2")
        buf.write("\2\u08ba\u08bb\5\u01be\u00e0\2\u08bb\u08bc\7\16\2\2\u08bc")
        buf.write("\u08be\3\2\2\2\u08bd\u08b9\3\2\2\2\u08bd\u08be\3\2\2\2")
        buf.write("\u08be\u08bf\3\2\2\2\u08bf\u08c0\7\30\2\2\u08c0\u08c1")
        buf.write("\7\n\2\2\u08c1\u08c2\5\u01c2\u00e2\2\u08c2\u01c1\3\2\2")
        buf.write("\2\u08c3\u08c4\t\3\2\2\u08c4\u01c3\3\2\2\2\u08c5\u08c8")
        buf.write("\5\36\20\2\u08c6\u08c8\5\34\17\2\u08c7\u08c5\3\2\2\2\u08c7")
        buf.write("\u08c6\3\2\2\2\u08c8\u01c5\3\2\2\2\u08c9\u08ca\5*\26\2")
        buf.write("\u08ca\u01c7\3\2\2\2\u08cb\u08cc\7I\2\2\u08cc\u08cd\7")
        buf.write("\13\2\2\u08cd\u08ce\5\32\16\2\u08ce\u01c9\3\2\2\2\u08cf")
        buf.write("\u08d0\7S\2\2\u08d0\u08d1\7\13\2\2\u08d1\u08d2\5\u01cc")
        buf.write("\u00e7\2\u08d2\u01cb\3\2\2\2\u08d3\u08d4\t\3\2\2\u08d4")
        buf.write("\u01cd\3\2\2\2\u08d5\u08d6\7R\2\2\u08d6\u08d7\7\13\2\2")
        buf.write("\u08d7\u08d8\5\u01d0\u00e9\2\u08d8\u01cf\3\2\2\2\u08d9")
        buf.write("\u08da\t\3\2\2\u08da\u01d1\3\2\2\2\u08db\u08dc\7W\2\2")
        buf.write("\u08dc\u08dd\7\13\2\2\u08dd\u08de\5\32\16\2\u08de\u01d3")
        buf.write("\3\2\2\2\u08df\u08e3\7U\2\2\u08e0\u08e4\5(\25\2\u08e1")
        buf.write("\u08e2\7\13\2\2\u08e2\u08e4\5*\26\2\u08e3\u08e0\3\2\2")
        buf.write("\2\u08e3\u08e1\3\2\2\2\u08e4\u01d5\3\2\2\2\u08e5\u08e9")
        buf.write("\7T\2\2\u08e6\u08ea\5(\25\2\u08e7\u08e8\7\13\2\2\u08e8")
        buf.write("\u08ea\5*\26\2\u08e9\u08e6\3\2\2\2\u08e9\u08e7\3\2\2\2")
        buf.write("\u08ea\u01d7\3\2\2\2\u08eb\u08ec\7V\2\2\u08ec\u08ed\7")
        buf.write("\13\2\2\u08ed\u08ee\5\32\16\2\u08ee\u01d9\3\2\2\2\u08ef")
        buf.write("\u08f0\7X\2\2\u08f0\u08f1\7\13\2\2\u08f1\u08f2\5\32\16")
        buf.write("\2\u08f2\u01db\3\2\2\2\u08f3\u08f4\7^\2\2\u08f4\u08f5")
        buf.write("\7\13\2\2\u08f5\u08f6\5\u01de\u00f0\2\u08f6\u01dd\3\2")
        buf.write("\2\2\u08f7\u08fc\5\u01e0\u00f1\2\u08f8\u08f9\7\24\2\2")
        buf.write("\u08f9\u08fb\5\u01e0\u00f1\2\u08fa\u08f8\3\2\2\2\u08fb")
        buf.write("\u08fe\3\2\2\2\u08fc\u08fa\3\2\2\2\u08fc\u08fd\3\2\2\2")
        buf.write("\u08fd\u01df\3\2\2\2\u08fe\u08fc\3\2\2\2\u08ff\u0900\t")
        buf.write("\20\2\2\u0900\u01e1\3\2\2\2\u0901\u0902\7x\2\2\u0902\u0903")
        buf.write("\7\13\2\2\u0903\u0904\5\u01ec\u00f7\2\u0904\u01e3\3\2")
        buf.write("\2\2\u0905\u0906\7s\2\2\u0906\u0907\7\13\2\2\u0907\u0908")
        buf.write("\5\u01e6\u00f4\2\u0908\u01e5\3\2\2\2\u0909\u090a\7\u0083")
        buf.write("\2\2\u090a\u01e7\3\2\2\2\u090b\u090c\7K\2\2\u090c\u090d")
        buf.write("\7\13\2\2\u090d\u090e\5\u01ea\u00f6\2\u090e\u01e9\3\2")
        buf.write("\2\2\u090f\u0910\7\4\2\2\u0910\u01eb\3\2\2\2\u0911\u0916")
        buf.write("\5\u01ee\u00f8\2\u0912\u0913\7\24\2\2\u0913\u0915\5\u01ee")
        buf.write("\u00f8\2\u0914\u0912\3\2\2\2\u0915\u0918\3\2\2\2\u0916")
        buf.write("\u0914\3\2\2\2\u0916\u0917\3\2\2\2\u0917\u01ed\3\2\2\2")
        buf.write("\u0918\u0916\3\2\2\2\u0919\u091b\5\u01f0\u00f9\2\u091a")
        buf.write("\u091c\5\u01f2\u00fa\2\u091b\u091a\3\2\2\2\u091b\u091c")
        buf.write("\3\2\2\2\u091c\u01ef\3\2\2\2\u091d\u0923\7\34\2\2\u091e")
        buf.write("\u0920\7\f\2\2\u091f\u091e\3\2\2\2\u091f\u0920\3\2\2\2")
        buf.write("\u0920\u0921\3\2\2\2\u0921\u0923\5\32\16\2\u0922\u091d")
        buf.write("\3\2\2\2\u0922\u091f\3\2\2\2\u0923\u01f1\3\2\2\2\u0924")
        buf.write("\u0925\5*\26\2\u0925\u01f3\3\2\2\2\u0926\u0927\7Y\2\2")
        buf.write("\u0927\u0928\7\13\2\2\u0928\u0929\5\u01f6\u00fc\2\u0929")
        buf.write("\u01f5\3\2\2\2\u092a\u092f\5\u01f8\u00fd\2\u092b\u092c")
        buf.write("\7\24\2\2\u092c\u092e\5\u01f8\u00fd\2\u092d\u092b\3\2")
        buf.write("\2\2\u092e\u0931\3\2\2\2\u092f\u092d\3\2\2\2\u092f\u0930")
        buf.write("\3\2\2\2\u0930\u01f7\3\2\2\2\u0931\u092f\3\2\2\2\u0932")
        buf.write("\u0933\5\u01fa\u00fe\2\u0933\u01f9\3\2\2\2\u0934\u093a")
        buf.write("\7\34\2\2\u0935\u0937\7\f\2\2\u0936\u0935\3\2\2\2\u0936")
        buf.write("\u0937\3\2\2\2\u0937\u0938\3\2\2\2\u0938\u093a\5\32\16")
        buf.write("\2\u0939\u0934\3\2\2\2\u0939\u0936\3\2\2\2\u093a\u01fb")
        buf.write("\3\2\2\2\u093b\u093d\7\u009b\2\2\u093c\u093e\5*\26\2\u093d")
        buf.write("\u093c\3\2\2\2\u093d\u093e\3\2\2\2\u093e\u01fd\3\2\2\2")
        buf.write("\u093f\u0941\7\u009c\2\2\u0940\u0942\5*\26\2\u0941\u0940")
        buf.write("\3\2\2\2\u0941\u0942\3\2\2\2\u0942\u01ff\3\2\2\2\u0943")
        buf.write("\u0944\7\u009d\2\2\u0944\u0945\5\u01b6\u00dc\2\u0945\u0201")
        buf.write("\3\2\2\2\u0946\u0947\7\u009e\2\2\u0947\u0948\5\u01b6\u00dc")
        buf.write("\2\u0948\u0203\3\2\2\2\u0949\u094a\7\u009f\2\2\u094a\u094b")
        buf.write("\5\u01b6\u00dc\2\u094b\u0205\3\2\2\2\u094c\u094d\7\u00a0")
        buf.write("\2\2\u094d\u094e\7\25\2\2\u094e\u094f\5\u0208\u0105\2")
        buf.write("\u094f\u0953\7\r\2\2\u0950\u0952\7\5\2\2\u0951\u0950\3")
        buf.write("\2\2\2\u0952\u0955\3\2\2\2\u0953\u0951\3\2\2\2\u0953\u0954")
        buf.write("\3\2\2\2\u0954\u0957\3\2\2\2\u0955\u0953\3\2\2\2\u0956")
        buf.write("\u0958\5\u020a\u0106\2\u0957\u0956\3\2\2\2\u0958\u0959")
        buf.write("\3\2\2\2\u0959\u0957\3\2\2\2\u0959\u095a\3\2\2\2\u095a")
        buf.write("\u095e\3\2\2\2\u095b\u095d\7\5\2\2\u095c\u095b\3\2\2\2")
        buf.write("\u095d\u0960\3\2\2\2\u095e\u095c\3\2\2\2\u095e\u095f\3")
        buf.write("\2\2\2\u095f\u0961\3\2\2\2\u0960\u095e\3\2\2\2\u0961\u0962")
        buf.write("\7\16\2\2\u0962\u0207\3\2\2\2\u0963\u0964\5\32\16\2\u0964")
        buf.write("\u0209\3\2\2\2\u0965\u0967\7\24\2\2\u0966\u0965\3\2\2")
        buf.write("\2\u0966\u0967\3\2\2\2\u0967\u096b\3\2\2\2\u0968\u096a")
        buf.write("\7\5\2\2\u0969\u0968\3\2\2\2\u096a\u096d\3\2\2\2\u096b")
        buf.write("\u0969\3\2\2\2\u096b\u096c\3\2\2\2\u096c\u096f\3\2\2\2")
        buf.write("\u096d\u096b\3\2\2\2\u096e\u0970\5\u0210\u0109\2\u096f")
        buf.write("\u096e\3\2\2\2\u096f\u0970\3\2\2\2\u0970\u0971\3\2\2\2")
        buf.write("\u0971\u0974\5\u021e\u0110\2\u0972\u0975\5\u020e\u0108")
        buf.write("\2\u0973\u0975\5\u020c\u0107\2\u0974\u0972\3\2\2\2\u0974")
        buf.write("\u0973\3\2\2\2\u0975\u0979\3\2\2\2\u0976\u0978\7\5\2\2")
        buf.write("\u0977\u0976\3\2\2\2\u0978\u097b\3\2\2\2\u0979\u0977\3")
        buf.write("\2\2\2\u0979\u097a\3\2\2\2\u097a\u020b\3\2\2\2\u097b\u0979")
        buf.write("\3\2\2\2\u097c\u097f\7\13\2\2\u097d\u0980\5\u021a\u010e")
        buf.write("\2\u097e\u0980\5\u0218\u010d\2\u097f\u097d\3\2\2\2\u097f")
        buf.write("\u097e\3\2\2\2\u0980\u020d\3\2\2\2\u0981\u0982\5(\25\2")
        buf.write("\u0982\u020f\3\2\2\2\u0983\u0984\7\17\2\2\u0984\u0989")
        buf.write("\5\u0212\u010a\2\u0985\u0986\7\24\2\2\u0986\u0988\5\u0212")
        buf.write("\u010a\2\u0987\u0985\3\2\2\2\u0988\u098b\3\2\2\2\u0989")
        buf.write("\u0987\3\2\2\2\u0989\u098a\3\2\2\2\u098a\u098c\3\2\2\2")
        buf.write("\u098b\u0989\3\2\2\2\u098c\u098d\7\20\2\2\u098d\u0211")
        buf.write("\3\2\2\2\u098e\u098f\5\u0214\u010b\2\u098f\u0990\7\30")
        buf.write("\2\2\u0990\u0991\5\u0216\u010c\2\u0991\u0213\3\2\2\2\u0992")
        buf.write("\u0993\5\32\16\2\u0993\u0215\3\2\2\2\u0994\u0998\7\37")
        buf.write("\2\2\u0995\u0998\7 \2\2\u0996\u0998\5\32\16\2\u0997\u0994")
        buf.write("\3\2\2\2\u0997\u0995\3\2\2\2\u0997\u0996\3\2\2\2\u0998")
        buf.write("\u0217\3\2\2\2\u0999\u099a\t\3\2\2\u099a\u0219\3\2\2\2")
        buf.write("\u099b\u099c\7Q\2\2\u099c\u099d\7\r\2\2\u099d\u099e\5")
        buf.write("\u021c\u010f\2\u099e\u099f\7\16\2\2\u099f\u021b\3\2\2")
        buf.write("\2\u09a0\u09a1\5\32\16\2\u09a1\u09a2\7\25\2\2\u09a2\u09a4")
        buf.write("\3\2\2\2\u09a3\u09a0\3\2\2\2\u09a3\u09a4\3\2\2\2\u09a4")
        buf.write("\u09a5\3\2\2\2\u09a5\u09a6\5\32\16\2\u09a6\u021d\3\2\2")
        buf.write("\2\u09a7\u09ab\7\37\2\2\u09a8\u09ab\7 \2\2\u09a9\u09ab")
        buf.write("\5\32\16\2\u09aa\u09a7\3\2\2\2\u09aa\u09a8\3\2\2\2\u09aa")
        buf.write("\u09a9\3\2\2\2\u09ab\u021f\3\2\2\2\u09ac\u09ad\7\u00a1")
        buf.write("\2\2\u09ad\u09ae\5\u01b6\u00dc\2\u09ae\u0221\3\2\2\2\u09af")
        buf.write("\u09b0\7\u00a2\2\2\u09b0\u0223\3\2\2\2\u09b1\u09b2\7\u00a3")
        buf.write("\2\2\u09b2\u0225\3\2\2\2\u09b3\u09b4\7\u00a4\2\2\u09b4")
        buf.write("\u09b5\7\r\2\2\u09b5\u09b6\5\u0228\u0115\2\u09b6\u09b7")
        buf.write("\7\16\2\2\u09b7\u0227\3\2\2\2\u09b8\u09b9\7\7\2\2\u09b9")
        buf.write("\u0229\3\2\2\2\u0106\u022d\u0233\u0239\u023d\u0242\u0244")
        buf.write("\u0249\u024d\u0252\u0254\u0259\u0261\u0266\u026e\u0275")
        buf.write("\u0278\u0281\u0287\u028a\u0299\u02a0\u02a5\u02ad\u02b3")
        buf.write("\u02b8\u02bb\u02be\u02c2\u02ca\u02dc\u02e3\u02ea\u02ef")
        buf.write("\u02f4\u02f9\u0300\u0304\u0309\u030f\u0314\u0320\u0324")
        buf.write("\u0329\u032e\u0332\u0338\u0342\u034a\u034d\u0352\u035a")
        buf.write("\u0362\u0367\u036b\u0371\u0375\u037d\u0384\u038c\u0394")
        buf.write("\u0399\u039d\u03a0\u03a5\u03ac\u03b6\u03b8\u03be\u03c0")
        buf.write("\u03c6\u03c8\u03cd\u03da\u03e9\u03f2\u03fe\u0403\u0408")
        buf.write("\u040e\u0414\u041a\u0420\u0428\u042b\u042f\u0433\u043e")
        buf.write("\u0444\u0449\u0450\u0457\u045c\u045f\u0462\u0467\u046a")
        buf.write("\u046e\u0473\u0478\u047d\u0490\u0494\u04b2\u04d1\u04d5")
        buf.write("\u04e0\u04e4\u04eb\u04f5\u04fe\u0502\u0509\u0518\u0522")
        buf.write("\u052b\u0534\u0543\u054c\u0550\u0553\u0572\u0582\u0584")
        buf.write("\u058a\u058e\u0593\u059b\u05a3\u05a9\u05b3\u05c1\u05cb")
        buf.write("\u05cd\u05d1\u05e8\u05ed\u05fd\u0606\u060f\u0618\u0621")
        buf.write("\u062a\u0635\u0638\u063c\u0645\u064b\u0651\u0653\u0662")
        buf.write("\u0664\u066f\u0677\u067c\u0682\u0687\u068d\u0692\u0698")
        buf.write("\u06a1\u06aa\u06b1\u06b6\u06c2\u06cb\u06d7\u06de\u06e9")
        buf.write("\u06eb\u06fe\u070c\u0733\u073a\u073f\u0743\u0747\u074b")
        buf.write("\u074d\u0751\u0756\u0763\u076a\u0772\u0774\u0777\u077e")
        buf.write("\u0780\u0788\u078f\u0792\u0794\u079b\u07a1\u07a5\u07aa")
        buf.write("\u07b0\u07bb\u07be\u07c7\u07cb\u07d0\u07d3\u07dc\u07f1")
        buf.write("\u07f7\u07f9\u07ff\u0802\u0805\u0808\u080c\u0818\u081b")
        buf.write("\u0822\u0825\u082e\u0839\u0842\u0850\u0856\u085b\u086c")
        buf.write("\u086e\u0874\u0879\u087e\u0884\u088a\u0893\u089a\u08a1")
        buf.write("\u08a8\u08b1\u08bd\u08c7\u08e3\u08e9\u08fc\u0916\u091b")
        buf.write("\u091f\u0922\u092f\u0936\u0939\u093d\u0941\u0953\u0959")
        buf.write("\u095e\u0966\u096b\u096f\u0974\u0979\u097f\u0989\u0997")
        buf.write("\u09a3\u09aa")
        return buf.getvalue()


class ZmeiLangParser ( Parser ):

    grammarFileName = "ZmeiLangParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'<'", "'>'", 
                     "':'", "'^'", "'('", "')'", "'['", "']'", "'?'", "'_'", 
                     "'-'", "','", "'.'", "'#'", "'/'", "'='", "'$'", "'&'", 
                     "'!'", "'*'", "'~'", "'|'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "' '", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "';'", "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "WRITE_MODE", "BOOL", "NL", "ID", "DIGIT", 
                      "SIZE2D", "LT", "GT", "COLON", "EXCLUDE", "BRACE_OPEN", 
                      "BRACE_CLOSE", "SQ_BRACE_OPEN", "SQ_BRACE_CLOSE", 
                      "QUESTION_MARK", "UNDERSCORE", "DASH", "COMA", "DOT", 
                      "HASH", "SLASH", "EQUALS", "DOLLAR", "AMP", "EXCLAM", 
                      "STAR", "APPROX", "PIPE", "STRING_DQ", "STRING_SQ", 
                      "COMMENT_LINE", "COMMENT_BLOCK", "UNICODE", "WS", 
                      "COL_FIELD_CALCULATED", "ASSIGN", "ASSIGN_STATIC", 
                      "CODE_BLOCK", "ERRCHAR", "PYTHON_CODE", "PYTHON_LINE_ERRCHAR", 
                      "PYTHON_LINE_END", "PYTHON_EXPR_ERRCHAR", "PYTHON_LINE_NL", 
                      "KW_FROM", "KW_IMPORT", "KW_AS", "COL_FIELD_TYPE_LONGTEXT", 
                      "COL_FIELD_TYPE_HTML", "COL_FIELD_TYPE_HTML_MEDIA", 
                      "COL_FIELD_TYPE_FLOAT", "COL_FIELD_TYPE_DECIMAL", 
                      "COL_FIELD_TYPE_DATE", "COL_FIELD_TYPE_DATETIME", 
                      "COL_FIELD_TYPE_CREATE_TIME", "COL_FIELD_TYPE_UPDATE_TIME", 
                      "COL_FIELD_TYPE_IMAGE", "COL_FIELD_TYPE_FILE", "COL_FIELD_TYPE_FILER_IMAGE", 
                      "COL_FIELD_TYPE_FILER_FILE", "COL_FIELD_TYPE_FILER_FOLDER", 
                      "COL_FIELD_TYPE_FILER_IMAGE_FOLDER", "COL_FIELD_TYPE_TEXT", 
                      "COL_FIELD_TYPE_INT", "COL_FIELD_TYPE_SLUG", "COL_FIELD_TYPE_BOOL", 
                      "COL_FIELD_TYPE_ONE", "COL_FIELD_TYPE_ONE2ONE", "COL_FIELD_TYPE_MANY", 
                      "COL_FIELD_CHOICES", "KW_THEME", "KW_INSTALL", "KW_HEADER", 
                      "KW_SERVICES", "KW_SELENIUM_PYTEST", "KW_CHILD", "KW_FILTER_OUT", 
                      "KW_FILTER_IN", "KW_PAGE", "KW_LINK_SUFFIX", "KW_URL_PREFIX", 
                      "KW_CAN_EDIT", "KW_OBJECT_EXPR", "KW_BLOCK", "KW_ITEM_NAME", 
                      "KW_PK_PARAM", "KW_LIST_FIELDS", "KW_DELETE", "KW_EDIT", 
                      "KW_CREATE", "KW_DETAIL", "KW_SKIP", "KW_POLY_LIST", 
                      "KW_CSS", "KW_JS", "KW_INLINE_TYPE_TABULAR", "KW_INLINE_TYPE_STACKED", 
                      "KW_INLINE_TYPE_POLYMORPHIC", "KW_AUTH_TYPE_BASIC", 
                      "KW_AUTH_TYPE_SESSION", "KW_AUTH_TYPE_TOKEN", "KW_INLINE", 
                      "KW_TYPE", "KW_USER_FIELD", "KW_ANNOTATE", "KW_ON_CREATE", 
                      "KW_QUERY", "KW_AUTH", "KW_COUNT", "KW_I18N", "KW_EXTRA", 
                      "KW_TABS", "KW_LIST", "KW_READ_ONLY", "KW_LIST_EDITABLE", 
                      "KW_LIST_FILTER", "KW_LIST_SEARCH", "KW_FIELDS", "AN_SUIT", 
                      "AN_CELERY", "AN_CHANNELS", "AN_DOCKER", "AN_FILER", 
                      "AN_GITLAB", "AN_FILE", "AN_THEME", "AN_LANGS", "AN_ADMIN", 
                      "KW_INLINE_TYPE", "AN_API", "AN_REST", "KW_AUTH_TYPE", 
                      "AN_ORDER", "AN_CLEAN", "AN_PRE_DELETE", "AN_TREE", 
                      "AN_MIXIN", "AN_DATE_TREE", "AN_M2M_CHANGED", "AN_POST_SAVE", 
                      "AN_PRE_SAVE", "AN_POST_DELETE", "AN_SORTABLE", "AN_STREAM", 
                      "AN_FLUTTER", "AN_REACT", "AN_REACT_CLIENT", "AN_REACT_SERVER", 
                      "AN_HTML", "AN_MARKDOWN", "AN_CRUD_DELETE", "AN_CRUD", 
                      "AN_POST", "AN_AUTH", "AN_CRUD_CREATE", "AN_CRUD_EDIT", 
                      "AN_CRUD_LIST", "AN_MENU", "AN_CRUD_DETAIL", "AN_PRIORITY", 
                      "AN_GET", "AN_ERROR" ]

    RULE_col_file = 0
    RULE_page_imports = 1
    RULE_model_imports = 2
    RULE_page_import_statement = 3
    RULE_model_import_statement = 4
    RULE_import_statement = 5
    RULE_import_source = 6
    RULE_import_list = 7
    RULE_import_item = 8
    RULE_import_item_name = 9
    RULE_import_item_alias = 10
    RULE_import_item_all = 11
    RULE_id_or_kw = 12
    RULE_classname = 13
    RULE_model_ref = 14
    RULE_field_list_expr = 15
    RULE_field_list_expr_field = 16
    RULE_write_mode_expr = 17
    RULE_python_code = 18
    RULE_code_line = 19
    RULE_code_block = 20
    RULE_cs_annotation = 21
    RULE_an_suit = 22
    RULE_an_suit_app_name = 23
    RULE_an_celery = 24
    RULE_an_channels = 25
    RULE_an_docker = 26
    RULE_an_filer = 27
    RULE_an_gitlab = 28
    RULE_an_gitlab_test_declaration = 29
    RULE_an_gitlab_test_declaration_selenium_pytest = 30
    RULE_an_gitlab_test_services = 31
    RULE_an_gitlab_test_service = 32
    RULE_an_gitlab_test_service_name = 33
    RULE_an_gitlab_branch_declaration = 34
    RULE_an_gitlab_branch_deploy_type = 35
    RULE_an_gitlab_branch_name = 36
    RULE_an_gitlab_deployment_name = 37
    RULE_an_gitlab_deployment_host = 38
    RULE_an_gitlab_deployment_variable = 39
    RULE_an_gitlab_deployment_variable_name = 40
    RULE_an_gitlab_deployment_variable_value = 41
    RULE_an_file = 42
    RULE_an_file_name = 43
    RULE_an_theme = 44
    RULE_an_theme_install = 45
    RULE_an_theme_name = 46
    RULE_an_langs = 47
    RULE_an_langs_list = 48
    RULE_col = 49
    RULE_col_str_expr = 50
    RULE_col_header = 51
    RULE_col_header_line_separator = 52
    RULE_col_verbose_name = 53
    RULE_verbose_name_part = 54
    RULE_col_base_name = 55
    RULE_col_name = 56
    RULE_col_field = 57
    RULE_col_field_expr_or_def = 58
    RULE_col_field_custom = 59
    RULE_col_field_extend = 60
    RULE_col_field_extend_append = 61
    RULE_wrong_field_type = 62
    RULE_col_field_expr = 63
    RULE_col_field_expr_marker = 64
    RULE_col_feild_expr_code = 65
    RULE_string_or_quoted = 66
    RULE_col_field_help_text = 67
    RULE_col_field_verbose_name = 68
    RULE_col_field_name = 69
    RULE_col_modifier = 70
    RULE_col_field_def = 71
    RULE_field_longtext = 72
    RULE_field_html = 73
    RULE_field_html_media = 74
    RULE_field_float = 75
    RULE_field_decimal = 76
    RULE_field_date = 77
    RULE_field_datetime = 78
    RULE_field_create_time = 79
    RULE_field_update_time = 80
    RULE_field_file = 81
    RULE_field_filer_file = 82
    RULE_field_filer_folder = 83
    RULE_field_text = 84
    RULE_field_text_size = 85
    RULE_field_text_choices = 86
    RULE_field_text_choice = 87
    RULE_field_text_choice_val = 88
    RULE_field_text_choice_key = 89
    RULE_field_int = 90
    RULE_field_int_choices = 91
    RULE_field_int_choice = 92
    RULE_field_int_choice_val = 93
    RULE_field_int_choice_key = 94
    RULE_field_slug = 95
    RULE_field_slug_ref_field = 96
    RULE_field_slug_ref_field_id = 97
    RULE_field_bool = 98
    RULE_field_bool_default = 99
    RULE_field_image = 100
    RULE_filer_image_type = 101
    RULE_field_image_sizes = 102
    RULE_field_image_size = 103
    RULE_field_image_size_dimensions = 104
    RULE_field_image_size_name = 105
    RULE_field_image_filters = 106
    RULE_field_image_filter = 107
    RULE_field_relation = 108
    RULE_field_relation_type = 109
    RULE_field_relation_cascade_marker = 110
    RULE_field_relation_target_ref = 111
    RULE_field_relation_target_class = 112
    RULE_field_relation_related_name = 113
    RULE_model_annotation = 114
    RULE_an_admin = 115
    RULE_an_admin_js = 116
    RULE_an_admin_css = 117
    RULE_an_admin_css_file_name = 118
    RULE_an_admin_js_file_name = 119
    RULE_an_admin_inlines = 120
    RULE_an_admin_inline = 121
    RULE_inline_name = 122
    RULE_inline_type = 123
    RULE_inline_extra = 124
    RULE_inline_fields = 125
    RULE_an_admin_tabs = 126
    RULE_an_admin_tab = 127
    RULE_tab_name = 128
    RULE_tab_verbose_name = 129
    RULE_an_admin_list = 130
    RULE_an_admin_read_only = 131
    RULE_an_admin_list_editable = 132
    RULE_an_admin_list_filter = 133
    RULE_an_admin_list_search = 134
    RULE_an_admin_fields = 135
    RULE_an_api = 136
    RULE_an_api_all = 137
    RULE_an_api_name = 138
    RULE_an_rest = 139
    RULE_an_rest_config = 140
    RULE_an_rest_main_part = 141
    RULE_an_rest_descriptor = 142
    RULE_an_rest_i18n = 143
    RULE_an_rest_query = 144
    RULE_an_rest_on_create = 145
    RULE_an_rest_filter_in = 146
    RULE_an_rest_filter_out = 147
    RULE_an_rest_read_only = 148
    RULE_an_rest_user_field = 149
    RULE_an_rest_fields = 150
    RULE_an_rest_fields_write_mode = 151
    RULE_an_rest_auth = 152
    RULE_an_rest_auth_type = 153
    RULE_an_rest_auth_token_model = 154
    RULE_an_rest_auth_token_class = 155
    RULE_an_rest_annotate = 156
    RULE_an_rest_annotate_count = 157
    RULE_an_rest_annotate_count_field = 158
    RULE_an_rest_annotate_count_alias = 159
    RULE_an_rest_inline = 160
    RULE_an_rest_inline_decl = 161
    RULE_an_rest_inline_name = 162
    RULE_an_order = 163
    RULE_an_order_fields = 164
    RULE_an_clean = 165
    RULE_an_pre_delete = 166
    RULE_an_tree = 167
    RULE_an_tree_poly = 168
    RULE_an_mixin = 169
    RULE_an_date_tree = 170
    RULE_an_date_tree_field = 171
    RULE_an_m2m_changed = 172
    RULE_an_post_save = 173
    RULE_an_pre_save = 174
    RULE_an_post_delete = 175
    RULE_an_sortable = 176
    RULE_an_sortable_field_name = 177
    RULE_page = 178
    RULE_page_header = 179
    RULE_page_base = 180
    RULE_page_alias = 181
    RULE_page_alias_name = 182
    RULE_page_template = 183
    RULE_template_name = 184
    RULE_file_name_part = 185
    RULE_page_url = 186
    RULE_url_part = 187
    RULE_url_param = 188
    RULE_url_segment = 189
    RULE_url_segments = 190
    RULE_page_name = 191
    RULE_page_body = 192
    RULE_page_code = 193
    RULE_page_field = 194
    RULE_page_field_name = 195
    RULE_page_field_code = 196
    RULE_page_function = 197
    RULE_page_function_name = 198
    RULE_page_function_args = 199
    RULE_page_annotation = 200
    RULE_an_stream = 201
    RULE_an_stream_model = 202
    RULE_an_stream_target_model = 203
    RULE_an_stream_target_filter = 204
    RULE_an_stream_field_list = 205
    RULE_an_stream_field_name = 206
    RULE_an_flutter = 207
    RULE_an_flutter_child = 208
    RULE_an_react = 209
    RULE_an_react_type = 210
    RULE_an_react_descriptor = 211
    RULE_an_html = 212
    RULE_an_html_descriptor = 213
    RULE_an_markdown = 214
    RULE_an_markdown_descriptor = 215
    RULE_an_crud_delete = 216
    RULE_an_crud = 217
    RULE_an_crud_params = 218
    RULE_an_crud_page_override = 219
    RULE_an_crud_descriptor = 220
    RULE_an_crud_next_page = 221
    RULE_an_crud_next_page_event_name = 222
    RULE_an_crud_next_page_url = 223
    RULE_an_crud_next_page_url_val = 224
    RULE_an_crud_target_model = 225
    RULE_an_crud_target_filter = 226
    RULE_an_crud_theme = 227
    RULE_an_crud_url_prefix = 228
    RULE_an_crud_url_prefix_val = 229
    RULE_an_crud_link_suffix = 230
    RULE_an_crud_link_suffix_val = 231
    RULE_an_crud_item_name = 232
    RULE_an_crud_object_expr = 233
    RULE_an_crud_can_edit = 234
    RULE_an_crud_block = 235
    RULE_an_crud_pk_param = 236
    RULE_an_crud_skip = 237
    RULE_an_crud_skip_values = 238
    RULE_an_crud_view_name = 239
    RULE_an_crud_fields = 240
    RULE_an_crud_list_type = 241
    RULE_an_crud_list_type_var = 242
    RULE_an_crud_header = 243
    RULE_an_crud_header_enabled = 244
    RULE_an_crud_fields_expr = 245
    RULE_an_crud_field = 246
    RULE_an_crud_field_spec = 247
    RULE_an_crud_field_filter = 248
    RULE_an_crud_list_fields = 249
    RULE_an_crud_list_fields_expr = 250
    RULE_an_crud_list_field = 251
    RULE_an_crud_list_field_spec = 252
    RULE_an_post = 253
    RULE_an_auth = 254
    RULE_an_crud_create = 255
    RULE_an_crud_edit = 256
    RULE_an_crud_list = 257
    RULE_an_menu = 258
    RULE_an_menu_descriptor = 259
    RULE_an_menu_item = 260
    RULE_an_menu_target = 261
    RULE_an_menu_item_code = 262
    RULE_an_menu_item_args = 263
    RULE_an_menu_item_arg = 264
    RULE_an_menu_item_arg_key = 265
    RULE_an_menu_item_arg_val = 266
    RULE_an_menu_item_url = 267
    RULE_an_menu_item_page = 268
    RULE_an_menu_item_page_ref = 269
    RULE_an_menu_label = 270
    RULE_an_crud_detail = 271
    RULE_an_priority_marker = 272
    RULE_an_get = 273
    RULE_an_error = 274
    RULE_an_error_code = 275

    ruleNames =  [ "col_file", "page_imports", "model_imports", "page_import_statement", 
                   "model_import_statement", "import_statement", "import_source", 
                   "import_list", "import_item", "import_item_name", "import_item_alias", 
                   "import_item_all", "id_or_kw", "classname", "model_ref", 
                   "field_list_expr", "field_list_expr_field", "write_mode_expr", 
                   "python_code", "code_line", "code_block", "cs_annotation", 
                   "an_suit", "an_suit_app_name", "an_celery", "an_channels", 
                   "an_docker", "an_filer", "an_gitlab", "an_gitlab_test_declaration", 
                   "an_gitlab_test_declaration_selenium_pytest", "an_gitlab_test_services", 
                   "an_gitlab_test_service", "an_gitlab_test_service_name", 
                   "an_gitlab_branch_declaration", "an_gitlab_branch_deploy_type", 
                   "an_gitlab_branch_name", "an_gitlab_deployment_name", 
                   "an_gitlab_deployment_host", "an_gitlab_deployment_variable", 
                   "an_gitlab_deployment_variable_name", "an_gitlab_deployment_variable_value", 
                   "an_file", "an_file_name", "an_theme", "an_theme_install", 
                   "an_theme_name", "an_langs", "an_langs_list", "col", 
                   "col_str_expr", "col_header", "col_header_line_separator", 
                   "col_verbose_name", "verbose_name_part", "col_base_name", 
                   "col_name", "col_field", "col_field_expr_or_def", "col_field_custom", 
                   "col_field_extend", "col_field_extend_append", "wrong_field_type", 
                   "col_field_expr", "col_field_expr_marker", "col_feild_expr_code", 
                   "string_or_quoted", "col_field_help_text", "col_field_verbose_name", 
                   "col_field_name", "col_modifier", "col_field_def", "field_longtext", 
                   "field_html", "field_html_media", "field_float", "field_decimal", 
                   "field_date", "field_datetime", "field_create_time", 
                   "field_update_time", "field_file", "field_filer_file", 
                   "field_filer_folder", "field_text", "field_text_size", 
                   "field_text_choices", "field_text_choice", "field_text_choice_val", 
                   "field_text_choice_key", "field_int", "field_int_choices", 
                   "field_int_choice", "field_int_choice_val", "field_int_choice_key", 
                   "field_slug", "field_slug_ref_field", "field_slug_ref_field_id", 
                   "field_bool", "field_bool_default", "field_image", "filer_image_type", 
                   "field_image_sizes", "field_image_size", "field_image_size_dimensions", 
                   "field_image_size_name", "field_image_filters", "field_image_filter", 
                   "field_relation", "field_relation_type", "field_relation_cascade_marker", 
                   "field_relation_target_ref", "field_relation_target_class", 
                   "field_relation_related_name", "model_annotation", "an_admin", 
                   "an_admin_js", "an_admin_css", "an_admin_css_file_name", 
                   "an_admin_js_file_name", "an_admin_inlines", "an_admin_inline", 
                   "inline_name", "inline_type", "inline_extra", "inline_fields", 
                   "an_admin_tabs", "an_admin_tab", "tab_name", "tab_verbose_name", 
                   "an_admin_list", "an_admin_read_only", "an_admin_list_editable", 
                   "an_admin_list_filter", "an_admin_list_search", "an_admin_fields", 
                   "an_api", "an_api_all", "an_api_name", "an_rest", "an_rest_config", 
                   "an_rest_main_part", "an_rest_descriptor", "an_rest_i18n", 
                   "an_rest_query", "an_rest_on_create", "an_rest_filter_in", 
                   "an_rest_filter_out", "an_rest_read_only", "an_rest_user_field", 
                   "an_rest_fields", "an_rest_fields_write_mode", "an_rest_auth", 
                   "an_rest_auth_type", "an_rest_auth_token_model", "an_rest_auth_token_class", 
                   "an_rest_annotate", "an_rest_annotate_count", "an_rest_annotate_count_field", 
                   "an_rest_annotate_count_alias", "an_rest_inline", "an_rest_inline_decl", 
                   "an_rest_inline_name", "an_order", "an_order_fields", 
                   "an_clean", "an_pre_delete", "an_tree", "an_tree_poly", 
                   "an_mixin", "an_date_tree", "an_date_tree_field", "an_m2m_changed", 
                   "an_post_save", "an_pre_save", "an_post_delete", "an_sortable", 
                   "an_sortable_field_name", "page", "page_header", "page_base", 
                   "page_alias", "page_alias_name", "page_template", "template_name", 
                   "file_name_part", "page_url", "url_part", "url_param", 
                   "url_segment", "url_segments", "page_name", "page_body", 
                   "page_code", "page_field", "page_field_name", "page_field_code", 
                   "page_function", "page_function_name", "page_function_args", 
                   "page_annotation", "an_stream", "an_stream_model", "an_stream_target_model", 
                   "an_stream_target_filter", "an_stream_field_list", "an_stream_field_name", 
                   "an_flutter", "an_flutter_child", "an_react", "an_react_type", 
                   "an_react_descriptor", "an_html", "an_html_descriptor", 
                   "an_markdown", "an_markdown_descriptor", "an_crud_delete", 
                   "an_crud", "an_crud_params", "an_crud_page_override", 
                   "an_crud_descriptor", "an_crud_next_page", "an_crud_next_page_event_name", 
                   "an_crud_next_page_url", "an_crud_next_page_url_val", 
                   "an_crud_target_model", "an_crud_target_filter", "an_crud_theme", 
                   "an_crud_url_prefix", "an_crud_url_prefix_val", "an_crud_link_suffix", 
                   "an_crud_link_suffix_val", "an_crud_item_name", "an_crud_object_expr", 
                   "an_crud_can_edit", "an_crud_block", "an_crud_pk_param", 
                   "an_crud_skip", "an_crud_skip_values", "an_crud_view_name", 
                   "an_crud_fields", "an_crud_list_type", "an_crud_list_type_var", 
                   "an_crud_header", "an_crud_header_enabled", "an_crud_fields_expr", 
                   "an_crud_field", "an_crud_field_spec", "an_crud_field_filter", 
                   "an_crud_list_fields", "an_crud_list_fields_expr", "an_crud_list_field", 
                   "an_crud_list_field_spec", "an_post", "an_auth", "an_crud_create", 
                   "an_crud_edit", "an_crud_list", "an_menu", "an_menu_descriptor", 
                   "an_menu_item", "an_menu_target", "an_menu_item_code", 
                   "an_menu_item_args", "an_menu_item_arg", "an_menu_item_arg_key", 
                   "an_menu_item_arg_val", "an_menu_item_url", "an_menu_item_page", 
                   "an_menu_item_page_ref", "an_menu_label", "an_crud_detail", 
                   "an_priority_marker", "an_get", "an_error", "an_error_code" ]

    EOF = Token.EOF
    WRITE_MODE=1
    BOOL=2
    NL=3
    ID=4
    DIGIT=5
    SIZE2D=6
    LT=7
    GT=8
    COLON=9
    EXCLUDE=10
    BRACE_OPEN=11
    BRACE_CLOSE=12
    SQ_BRACE_OPEN=13
    SQ_BRACE_CLOSE=14
    QUESTION_MARK=15
    UNDERSCORE=16
    DASH=17
    COMA=18
    DOT=19
    HASH=20
    SLASH=21
    EQUALS=22
    DOLLAR=23
    AMP=24
    EXCLAM=25
    STAR=26
    APPROX=27
    PIPE=28
    STRING_DQ=29
    STRING_SQ=30
    COMMENT_LINE=31
    COMMENT_BLOCK=32
    UNICODE=33
    WS=34
    COL_FIELD_CALCULATED=35
    ASSIGN=36
    ASSIGN_STATIC=37
    CODE_BLOCK=38
    ERRCHAR=39
    PYTHON_CODE=40
    PYTHON_LINE_ERRCHAR=41
    PYTHON_LINE_END=42
    PYTHON_EXPR_ERRCHAR=43
    PYTHON_LINE_NL=44
    KW_FROM=45
    KW_IMPORT=46
    KW_AS=47
    COL_FIELD_TYPE_LONGTEXT=48
    COL_FIELD_TYPE_HTML=49
    COL_FIELD_TYPE_HTML_MEDIA=50
    COL_FIELD_TYPE_FLOAT=51
    COL_FIELD_TYPE_DECIMAL=52
    COL_FIELD_TYPE_DATE=53
    COL_FIELD_TYPE_DATETIME=54
    COL_FIELD_TYPE_CREATE_TIME=55
    COL_FIELD_TYPE_UPDATE_TIME=56
    COL_FIELD_TYPE_IMAGE=57
    COL_FIELD_TYPE_FILE=58
    COL_FIELD_TYPE_FILER_IMAGE=59
    COL_FIELD_TYPE_FILER_FILE=60
    COL_FIELD_TYPE_FILER_FOLDER=61
    COL_FIELD_TYPE_FILER_IMAGE_FOLDER=62
    COL_FIELD_TYPE_TEXT=63
    COL_FIELD_TYPE_INT=64
    COL_FIELD_TYPE_SLUG=65
    COL_FIELD_TYPE_BOOL=66
    COL_FIELD_TYPE_ONE=67
    COL_FIELD_TYPE_ONE2ONE=68
    COL_FIELD_TYPE_MANY=69
    COL_FIELD_CHOICES=70
    KW_THEME=71
    KW_INSTALL=72
    KW_HEADER=73
    KW_SERVICES=74
    KW_SELENIUM_PYTEST=75
    KW_CHILD=76
    KW_FILTER_OUT=77
    KW_FILTER_IN=78
    KW_PAGE=79
    KW_LINK_SUFFIX=80
    KW_URL_PREFIX=81
    KW_CAN_EDIT=82
    KW_OBJECT_EXPR=83
    KW_BLOCK=84
    KW_ITEM_NAME=85
    KW_PK_PARAM=86
    KW_LIST_FIELDS=87
    KW_DELETE=88
    KW_EDIT=89
    KW_CREATE=90
    KW_DETAIL=91
    KW_SKIP=92
    KW_POLY_LIST=93
    KW_CSS=94
    KW_JS=95
    KW_INLINE_TYPE_TABULAR=96
    KW_INLINE_TYPE_STACKED=97
    KW_INLINE_TYPE_POLYMORPHIC=98
    KW_AUTH_TYPE_BASIC=99
    KW_AUTH_TYPE_SESSION=100
    KW_AUTH_TYPE_TOKEN=101
    KW_INLINE=102
    KW_TYPE=103
    KW_USER_FIELD=104
    KW_ANNOTATE=105
    KW_ON_CREATE=106
    KW_QUERY=107
    KW_AUTH=108
    KW_COUNT=109
    KW_I18N=110
    KW_EXTRA=111
    KW_TABS=112
    KW_LIST=113
    KW_READ_ONLY=114
    KW_LIST_EDITABLE=115
    KW_LIST_FILTER=116
    KW_LIST_SEARCH=117
    KW_FIELDS=118
    AN_SUIT=119
    AN_CELERY=120
    AN_CHANNELS=121
    AN_DOCKER=122
    AN_FILER=123
    AN_GITLAB=124
    AN_FILE=125
    AN_THEME=126
    AN_LANGS=127
    AN_ADMIN=128
    KW_INLINE_TYPE=129
    AN_API=130
    AN_REST=131
    KW_AUTH_TYPE=132
    AN_ORDER=133
    AN_CLEAN=134
    AN_PRE_DELETE=135
    AN_TREE=136
    AN_MIXIN=137
    AN_DATE_TREE=138
    AN_M2M_CHANGED=139
    AN_POST_SAVE=140
    AN_PRE_SAVE=141
    AN_POST_DELETE=142
    AN_SORTABLE=143
    AN_STREAM=144
    AN_FLUTTER=145
    AN_REACT=146
    AN_REACT_CLIENT=147
    AN_REACT_SERVER=148
    AN_HTML=149
    AN_MARKDOWN=150
    AN_CRUD_DELETE=151
    AN_CRUD=152
    AN_POST=153
    AN_AUTH=154
    AN_CRUD_CREATE=155
    AN_CRUD_EDIT=156
    AN_CRUD_LIST=157
    AN_MENU=158
    AN_CRUD_DETAIL=159
    AN_PRIORITY=160
    AN_GET=161
    AN_ERROR=162

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Col_fileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ZmeiLangParser.EOF, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def cs_annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Cs_annotationContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Cs_annotationContext,i)


        def page_imports(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_importsContext,0)


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
            self.state = 555
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 552
                    self.match(ZmeiLangParser.NL) 
                self.state = 557
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 561
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 558
                    self.cs_annotation() 
                self.state = 563
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 567
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 564
                    self.match(ZmeiLangParser.NL) 
                self.state = 569
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 578
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 571
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.KW_FROM or _la==ZmeiLangParser.KW_IMPORT:
                    self.state = 570
                    self.page_imports()


                self.state = 574 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 573
                    self.page()
                    self.state = 576 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZmeiLangParser.SQ_BRACE_OPEN):
                        break



            self.state = 583
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 580
                    self.match(ZmeiLangParser.NL) 
                self.state = 585
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 594
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.HASH) | (1 << ZmeiLangParser.KW_FROM) | (1 << ZmeiLangParser.KW_IMPORT))) != 0):
                self.state = 587
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.KW_FROM or _la==ZmeiLangParser.KW_IMPORT:
                    self.state = 586
                    self.model_imports()


                self.state = 590 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 589
                    self.col()
                    self.state = 592 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZmeiLangParser.HASH):
                        break



            self.state = 599
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 596
                self.match(ZmeiLangParser.NL)
                self.state = 601
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 602
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

        def page_import_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Page_import_statementContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Page_import_statementContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 605 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 604
                self.page_import_statement()
                self.state = 607 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZmeiLangParser.KW_FROM or _la==ZmeiLangParser.KW_IMPORT):
                    break

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

        def model_import_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Model_import_statementContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Model_import_statementContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 610 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 609
                self.model_import_statement()
                self.state = 612 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZmeiLangParser.KW_FROM or _la==ZmeiLangParser.KW_IMPORT):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Page_import_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def import_statement(self):
            return self.getTypedRuleContext(ZmeiLangParser.Import_statementContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_import_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_import_statement" ):
                listener.enterPage_import_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_import_statement" ):
                listener.exitPage_import_statement(self)




    def page_import_statement(self):

        localctx = ZmeiLangParser.Page_import_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_page_import_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 614
            self.import_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Model_import_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def import_statement(self):
            return self.getTypedRuleContext(ZmeiLangParser.Import_statementContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_model_import_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModel_import_statement" ):
                listener.enterModel_import_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModel_import_statement" ):
                listener.exitModel_import_statement(self)




    def model_import_statement(self):

        localctx = ZmeiLangParser.Model_import_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_model_import_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 616
            self.import_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_IMPORT(self):
            return self.getToken(ZmeiLangParser.KW_IMPORT, 0)

        def import_list(self):
            return self.getTypedRuleContext(ZmeiLangParser.Import_listContext,0)


        def KW_FROM(self):
            return self.getToken(ZmeiLangParser.KW_FROM, 0)

        def import_source(self):
            return self.getTypedRuleContext(ZmeiLangParser.Import_sourceContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_import_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_statement" ):
                listener.enterImport_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_statement" ):
                listener.exitImport_statement(self)




    def import_statement(self):

        localctx = ZmeiLangParser.Import_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_import_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 620
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.KW_FROM:
                self.state = 618
                self.match(ZmeiLangParser.KW_FROM)
                self.state = 619
                self.import_source()


            self.state = 622
            self.match(ZmeiLangParser.KW_IMPORT)
            self.state = 623
            self.import_list()
            self.state = 625 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 624
                self.match(ZmeiLangParser.NL)
                self.state = 627 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZmeiLangParser.NL):
                    break

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

        def classname(self):
            return self.getTypedRuleContext(ZmeiLangParser.ClassnameContext,0)


        def DOT(self):
            return self.getToken(ZmeiLangParser.DOT, 0)

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
        self.enterRule(localctx, 12, self.RULE_import_source)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 630
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 629
                self.match(ZmeiLangParser.DOT)


            self.state = 632
            self.classname()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def import_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Import_itemContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Import_itemContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_import_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_list" ):
                listener.enterImport_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_list" ):
                listener.exitImport_list(self)




    def import_list(self):

        localctx = ZmeiLangParser.Import_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_import_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 634
            self.import_item()
            self.state = 639
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 635
                self.match(ZmeiLangParser.COMA)
                self.state = 636
                self.import_item()
                self.state = 641
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_itemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def import_item_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Import_item_nameContext,0)


        def KW_AS(self):
            return self.getToken(ZmeiLangParser.KW_AS, 0)

        def import_item_alias(self):
            return self.getTypedRuleContext(ZmeiLangParser.Import_item_aliasContext,0)


        def import_item_all(self):
            return self.getTypedRuleContext(ZmeiLangParser.Import_item_allContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_import_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_item" ):
                listener.enterImport_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_item" ):
                listener.exitImport_item(self)




    def import_item(self):

        localctx = ZmeiLangParser.Import_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_import_item)
        self._la = 0 # Token type
        try:
            self.state = 648
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 642
                self.import_item_name()
                self.state = 645
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.KW_AS:
                    self.state = 643
                    self.match(ZmeiLangParser.KW_AS)
                    self.state = 644
                    self.import_item_alias()


                pass
            elif token in [ZmeiLangParser.STAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 647
                self.import_item_all()
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


    class Import_item_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classname(self):
            return self.getTypedRuleContext(ZmeiLangParser.ClassnameContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_import_item_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_item_name" ):
                listener.enterImport_item_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_item_name" ):
                listener.exitImport_item_name(self)




    def import_item_name(self):

        localctx = ZmeiLangParser.Import_item_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_import_item_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 650
            self.classname()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_item_aliasContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_import_item_alias

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_item_alias" ):
                listener.enterImport_item_alias(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_item_alias" ):
                listener.exitImport_item_alias(self)




    def import_item_alias(self):

        localctx = ZmeiLangParser.Import_item_aliasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_import_item_alias)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 652
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_item_allContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(ZmeiLangParser.STAR, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_import_item_all

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_item_all" ):
                listener.enterImport_item_all(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_item_all" ):
                listener.exitImport_item_all(self)




    def import_item_all(self):

        localctx = ZmeiLangParser.Import_item_allContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_import_item_all)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 654
            self.match(ZmeiLangParser.STAR)
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

        def WRITE_MODE(self):
            return self.getToken(ZmeiLangParser.WRITE_MODE, 0)

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

        def COL_FIELD_TYPE_IMAGE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_IMAGE, 0)

        def COL_FIELD_TYPE_FILE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_FILE, 0)

        def COL_FIELD_TYPE_FILER_IMAGE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, 0)

        def COL_FIELD_TYPE_FILER_FILE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, 0)

        def COL_FIELD_TYPE_FILER_FOLDER(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, 0)

        def COL_FIELD_TYPE_FILER_IMAGE_FOLDER(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, 0)

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

        def KW_THEME(self):
            return self.getToken(ZmeiLangParser.KW_THEME, 0)

        def KW_INSTALL(self):
            return self.getToken(ZmeiLangParser.KW_INSTALL, 0)

        def KW_HEADER(self):
            return self.getToken(ZmeiLangParser.KW_HEADER, 0)

        def KW_SERVICES(self):
            return self.getToken(ZmeiLangParser.KW_SERVICES, 0)

        def KW_SELENIUM_PYTEST(self):
            return self.getToken(ZmeiLangParser.KW_SELENIUM_PYTEST, 0)

        def KW_CHILD(self):
            return self.getToken(ZmeiLangParser.KW_CHILD, 0)

        def KW_FILTER_OUT(self):
            return self.getToken(ZmeiLangParser.KW_FILTER_OUT, 0)

        def KW_FILTER_IN(self):
            return self.getToken(ZmeiLangParser.KW_FILTER_IN, 0)

        def KW_PAGE(self):
            return self.getToken(ZmeiLangParser.KW_PAGE, 0)

        def KW_LINK_SUFFIX(self):
            return self.getToken(ZmeiLangParser.KW_LINK_SUFFIX, 0)

        def KW_URL_PREFIX(self):
            return self.getToken(ZmeiLangParser.KW_URL_PREFIX, 0)

        def KW_CAN_EDIT(self):
            return self.getToken(ZmeiLangParser.KW_CAN_EDIT, 0)

        def KW_OBJECT_EXPR(self):
            return self.getToken(ZmeiLangParser.KW_OBJECT_EXPR, 0)

        def KW_BLOCK(self):
            return self.getToken(ZmeiLangParser.KW_BLOCK, 0)

        def KW_ITEM_NAME(self):
            return self.getToken(ZmeiLangParser.KW_ITEM_NAME, 0)

        def KW_PK_PARAM(self):
            return self.getToken(ZmeiLangParser.KW_PK_PARAM, 0)

        def KW_LIST_FIELDS(self):
            return self.getToken(ZmeiLangParser.KW_LIST_FIELDS, 0)

        def KW_DELETE(self):
            return self.getToken(ZmeiLangParser.KW_DELETE, 0)

        def KW_EDIT(self):
            return self.getToken(ZmeiLangParser.KW_EDIT, 0)

        def KW_CREATE(self):
            return self.getToken(ZmeiLangParser.KW_CREATE, 0)

        def KW_DETAIL(self):
            return self.getToken(ZmeiLangParser.KW_DETAIL, 0)

        def KW_SKIP(self):
            return self.getToken(ZmeiLangParser.KW_SKIP, 0)

        def KW_FROM(self):
            return self.getToken(ZmeiLangParser.KW_FROM, 0)

        def KW_POLY_LIST(self):
            return self.getToken(ZmeiLangParser.KW_POLY_LIST, 0)

        def KW_CSS(self):
            return self.getToken(ZmeiLangParser.KW_CSS, 0)

        def KW_JS(self):
            return self.getToken(ZmeiLangParser.KW_JS, 0)

        def KW_INLINE_TYPE_TABULAR(self):
            return self.getToken(ZmeiLangParser.KW_INLINE_TYPE_TABULAR, 0)

        def KW_INLINE_TYPE_STACKED(self):
            return self.getToken(ZmeiLangParser.KW_INLINE_TYPE_STACKED, 0)

        def KW_INLINE_TYPE_POLYMORPHIC(self):
            return self.getToken(ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, 0)

        def KW_AUTH_TYPE_BASIC(self):
            return self.getToken(ZmeiLangParser.KW_AUTH_TYPE_BASIC, 0)

        def KW_AUTH_TYPE_SESSION(self):
            return self.getToken(ZmeiLangParser.KW_AUTH_TYPE_SESSION, 0)

        def KW_AUTH_TYPE_TOKEN(self):
            return self.getToken(ZmeiLangParser.KW_AUTH_TYPE_TOKEN, 0)

        def KW_INLINE(self):
            return self.getToken(ZmeiLangParser.KW_INLINE, 0)

        def KW_TYPE(self):
            return self.getToken(ZmeiLangParser.KW_TYPE, 0)

        def KW_USER_FIELD(self):
            return self.getToken(ZmeiLangParser.KW_USER_FIELD, 0)

        def KW_ANNOTATE(self):
            return self.getToken(ZmeiLangParser.KW_ANNOTATE, 0)

        def KW_ON_CREATE(self):
            return self.getToken(ZmeiLangParser.KW_ON_CREATE, 0)

        def KW_QUERY(self):
            return self.getToken(ZmeiLangParser.KW_QUERY, 0)

        def KW_AUTH(self):
            return self.getToken(ZmeiLangParser.KW_AUTH, 0)

        def KW_COUNT(self):
            return self.getToken(ZmeiLangParser.KW_COUNT, 0)

        def KW_I18N(self):
            return self.getToken(ZmeiLangParser.KW_I18N, 0)

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
        self.enterRule(localctx, 24, self.RULE_id_or_kw)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 656
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.WRITE_MODE) | (1 << ZmeiLangParser.BOOL) | (1 << ZmeiLangParser.ID) | (1 << ZmeiLangParser.KW_FROM) | (1 << ZmeiLangParser.KW_IMPORT) | (1 << ZmeiLangParser.KW_AS) | (1 << ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FLOAT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DECIMAL) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATETIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_TEXT))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 64)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 64)) | (1 << (ZmeiLangParser.KW_THEME - 64)) | (1 << (ZmeiLangParser.KW_INSTALL - 64)) | (1 << (ZmeiLangParser.KW_HEADER - 64)) | (1 << (ZmeiLangParser.KW_SERVICES - 64)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 64)) | (1 << (ZmeiLangParser.KW_CHILD - 64)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 64)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 64)) | (1 << (ZmeiLangParser.KW_PAGE - 64)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 64)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 64)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 64)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 64)) | (1 << (ZmeiLangParser.KW_BLOCK - 64)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 64)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 64)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 64)) | (1 << (ZmeiLangParser.KW_DELETE - 64)) | (1 << (ZmeiLangParser.KW_EDIT - 64)) | (1 << (ZmeiLangParser.KW_CREATE - 64)) | (1 << (ZmeiLangParser.KW_DETAIL - 64)) | (1 << (ZmeiLangParser.KW_SKIP - 64)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 64)) | (1 << (ZmeiLangParser.KW_CSS - 64)) | (1 << (ZmeiLangParser.KW_JS - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_BASIC - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_SESSION - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_TOKEN - 64)) | (1 << (ZmeiLangParser.KW_INLINE - 64)) | (1 << (ZmeiLangParser.KW_TYPE - 64)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 64)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 64)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 64)) | (1 << (ZmeiLangParser.KW_QUERY - 64)) | (1 << (ZmeiLangParser.KW_AUTH - 64)) | (1 << (ZmeiLangParser.KW_COUNT - 64)) | (1 << (ZmeiLangParser.KW_I18N - 64)) | (1 << (ZmeiLangParser.KW_EXTRA - 64)) | (1 << (ZmeiLangParser.KW_TABS - 64)) | (1 << (ZmeiLangParser.KW_LIST - 64)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 64)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 64)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 64)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 64)) | (1 << (ZmeiLangParser.KW_FIELDS - 64)))) != 0)):
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


    class ClassnameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Id_or_kwContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.DOT)
            else:
                return self.getToken(ZmeiLangParser.DOT, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_classname

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassname" ):
                listener.enterClassname(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassname" ):
                listener.exitClassname(self)




    def classname(self):

        localctx = ZmeiLangParser.ClassnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_classname)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 658
            self.id_or_kw()
            self.state = 663
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.DOT:
                self.state = 659
                self.match(ZmeiLangParser.DOT)
                self.state = 660
                self.id_or_kw()
                self.state = 665
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Model_refContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HASH(self):
            return self.getToken(ZmeiLangParser.HASH, 0)

        def id_or_kw(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Id_or_kwContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,i)


        def DOT(self):
            return self.getToken(ZmeiLangParser.DOT, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_model_ref

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModel_ref" ):
                listener.enterModel_ref(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModel_ref" ):
                listener.exitModel_ref(self)




    def model_ref(self):

        localctx = ZmeiLangParser.Model_refContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_model_ref)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 666
            self.match(ZmeiLangParser.HASH)
            self.state = 670
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 667
                self.id_or_kw()
                self.state = 668
                self.match(ZmeiLangParser.DOT)


            self.state = 672
            self.id_or_kw()
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
        self.enterRule(localctx, 30, self.RULE_field_list_expr)
        self._la = 0 # Token type
        try:
            self.state = 697
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.DOT, ZmeiLangParser.STAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 675
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.DOT:
                    self.state = 674
                    self.match(ZmeiLangParser.DOT)


                self.state = 677
                self.match(ZmeiLangParser.STAR)
                self.state = 683
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 678
                        self.match(ZmeiLangParser.COMA)
                        self.state = 679
                        self.match(ZmeiLangParser.EXCLUDE)
                        self.state = 680
                        self.field_list_expr_field() 
                    self.state = 685
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

                pass
            elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 686
                self.id_or_kw()
                self.state = 694
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 687
                        self.match(ZmeiLangParser.COMA)
                        self.state = 689
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==ZmeiLangParser.EXCLUDE:
                            self.state = 688
                            self.match(ZmeiLangParser.EXCLUDE)


                        self.state = 691
                        self.field_list_expr_field() 
                    self.state = 696
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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
        self.enterRule(localctx, 32, self.RULE_field_list_expr_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 700
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.STAR:
                self.state = 699
                self.match(ZmeiLangParser.STAR)


            self.state = 702
            self.id_or_kw()
            self.state = 704
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.STAR:
                self.state = 703
                self.match(ZmeiLangParser.STAR)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Write_mode_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQ_BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.SQ_BRACE_OPEN, 0)

        def WRITE_MODE(self):
            return self.getToken(ZmeiLangParser.WRITE_MODE, 0)

        def SQ_BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.SQ_BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_write_mode_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite_mode_expr" ):
                listener.enterWrite_mode_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite_mode_expr" ):
                listener.exitWrite_mode_expr(self)




    def write_mode_expr(self):

        localctx = ZmeiLangParser.Write_mode_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_write_mode_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 706
            self.match(ZmeiLangParser.SQ_BRACE_OPEN)
            self.state = 707
            self.match(ZmeiLangParser.WRITE_MODE)
            self.state = 708
            self.match(ZmeiLangParser.SQ_BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Python_codeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def code_line(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_lineContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_python_code

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPython_code" ):
                listener.enterPython_code(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPython_code" ):
                listener.exitPython_code(self)




    def python_code(self):

        localctx = ZmeiLangParser.Python_codeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_python_code)
        try:
            self.state = 712
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.CODE_BLOCK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 710
                self.code_block()
                pass
            elif token in [ZmeiLangParser.ASSIGN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 711
                self.code_line()
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


    class Code_lineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(ZmeiLangParser.ASSIGN, 0)

        def PYTHON_CODE(self):
            return self.getToken(ZmeiLangParser.PYTHON_CODE, 0)

        def NL(self):
            return self.getToken(ZmeiLangParser.NL, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_code_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCode_line" ):
                listener.enterCode_line(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCode_line" ):
                listener.exitCode_line(self)




    def code_line(self):

        localctx = ZmeiLangParser.Code_lineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_code_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 714
            self.match(ZmeiLangParser.ASSIGN)
            self.state = 715
            self.match(ZmeiLangParser.PYTHON_CODE)
            self.state = 716
            self.match(ZmeiLangParser.NL)
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

        def CODE_BLOCK(self):
            return self.getToken(ZmeiLangParser.CODE_BLOCK, 0)

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
        self.enterRule(localctx, 40, self.RULE_code_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 718
            self.match(ZmeiLangParser.CODE_BLOCK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cs_annotationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_suit(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_suitContext,0)


        def an_celery(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_celeryContext,0)


        def an_channels(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_channelsContext,0)


        def an_docker(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_dockerContext,0)


        def an_filer(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_filerContext,0)


        def an_gitlab(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_gitlabContext,0)


        def an_file(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_fileContext,0)


        def an_theme(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_themeContext,0)


        def an_langs(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_langsContext,0)


        def NL(self):
            return self.getToken(ZmeiLangParser.NL, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_cs_annotation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCs_annotation" ):
                listener.enterCs_annotation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCs_annotation" ):
                listener.exitCs_annotation(self)




    def cs_annotation(self):

        localctx = ZmeiLangParser.Cs_annotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_cs_annotation)
        try:
            self.state = 730
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.AN_SUIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 720
                self.an_suit()
                pass
            elif token in [ZmeiLangParser.AN_CELERY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 721
                self.an_celery()
                pass
            elif token in [ZmeiLangParser.AN_CHANNELS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 722
                self.an_channels()
                pass
            elif token in [ZmeiLangParser.AN_DOCKER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 723
                self.an_docker()
                pass
            elif token in [ZmeiLangParser.AN_FILER]:
                self.enterOuterAlt(localctx, 5)
                self.state = 724
                self.an_filer()
                pass
            elif token in [ZmeiLangParser.AN_GITLAB]:
                self.enterOuterAlt(localctx, 6)
                self.state = 725
                self.an_gitlab()
                pass
            elif token in [ZmeiLangParser.AN_FILE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 726
                self.an_file()
                pass
            elif token in [ZmeiLangParser.AN_THEME]:
                self.enterOuterAlt(localctx, 8)
                self.state = 727
                self.an_theme()
                pass
            elif token in [ZmeiLangParser.AN_LANGS]:
                self.enterOuterAlt(localctx, 9)
                self.state = 728
                self.an_langs()
                pass
            elif token in [ZmeiLangParser.NL]:
                self.enterOuterAlt(localctx, 10)
                self.state = 729
                self.match(ZmeiLangParser.NL)
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


    class An_suitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_SUIT(self):
            return self.getToken(ZmeiLangParser.AN_SUIT, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_suit_app_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_suit_app_nameContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_suit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_suit" ):
                listener.enterAn_suit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_suit" ):
                listener.exitAn_suit(self)




    def an_suit(self):

        localctx = ZmeiLangParser.An_suitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_an_suit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 732
            self.match(ZmeiLangParser.AN_SUIT)
            self.state = 737
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 733
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 734
                self.an_suit_app_name()
                self.state = 735
                self.match(ZmeiLangParser.BRACE_CLOSE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_suit_app_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_suit_app_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_suit_app_name" ):
                listener.enterAn_suit_app_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_suit_app_name" ):
                listener.exitAn_suit_app_name(self)




    def an_suit_app_name(self):

        localctx = ZmeiLangParser.An_suit_app_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_an_suit_app_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 739
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


    class An_celeryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_CELERY(self):
            return self.getToken(ZmeiLangParser.AN_CELERY, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_celery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_celery" ):
                listener.enterAn_celery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_celery" ):
                listener.exitAn_celery(self)




    def an_celery(self):

        localctx = ZmeiLangParser.An_celeryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_an_celery)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 741
            self.match(ZmeiLangParser.AN_CELERY)
            self.state = 744
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 742
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 743
                self.match(ZmeiLangParser.BRACE_CLOSE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_channelsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_CHANNELS(self):
            return self.getToken(ZmeiLangParser.AN_CHANNELS, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_channels

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_channels" ):
                listener.enterAn_channels(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_channels" ):
                listener.exitAn_channels(self)




    def an_channels(self):

        localctx = ZmeiLangParser.An_channelsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_an_channels)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 746
            self.match(ZmeiLangParser.AN_CHANNELS)
            self.state = 749
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 747
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 748
                self.match(ZmeiLangParser.BRACE_CLOSE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_dockerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_DOCKER(self):
            return self.getToken(ZmeiLangParser.AN_DOCKER, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_docker

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_docker" ):
                listener.enterAn_docker(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_docker" ):
                listener.exitAn_docker(self)




    def an_docker(self):

        localctx = ZmeiLangParser.An_dockerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_an_docker)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 751
            self.match(ZmeiLangParser.AN_DOCKER)
            self.state = 754
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 752
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 753
                self.match(ZmeiLangParser.BRACE_CLOSE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_filerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_FILER(self):
            return self.getToken(ZmeiLangParser.AN_FILER, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_filer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_filer" ):
                listener.enterAn_filer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_filer" ):
                listener.exitAn_filer(self)




    def an_filer(self):

        localctx = ZmeiLangParser.An_filerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_an_filer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 756
            self.match(ZmeiLangParser.AN_FILER)
            self.state = 759
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 757
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 758
                self.match(ZmeiLangParser.BRACE_CLOSE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_gitlabContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_GITLAB(self):
            return self.getToken(ZmeiLangParser.AN_GITLAB, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def an_gitlab_test_declaration(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_gitlab_test_declarationContext,0)


        def an_gitlab_branch_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_gitlab_branch_declarationContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_gitlab_branch_declarationContext,i)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_gitlab

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_gitlab" ):
                listener.enterAn_gitlab(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_gitlab" ):
                listener.exitAn_gitlab(self)




    def an_gitlab(self):

        localctx = ZmeiLangParser.An_gitlabContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_an_gitlab)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 761
            self.match(ZmeiLangParser.AN_GITLAB)
            self.state = 762
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 766
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 763
                    self.match(ZmeiLangParser.NL) 
                self.state = 768
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

            self.state = 770
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 769
                self.an_gitlab_test_declaration()


            self.state = 775
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 772
                self.match(ZmeiLangParser.NL)
                self.state = 777
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 779 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 778
                self.an_gitlab_branch_declaration()
                self.state = 781 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.WRITE_MODE) | (1 << ZmeiLangParser.BOOL) | (1 << ZmeiLangParser.ID) | (1 << ZmeiLangParser.DASH) | (1 << ZmeiLangParser.SLASH) | (1 << ZmeiLangParser.STAR) | (1 << ZmeiLangParser.KW_FROM) | (1 << ZmeiLangParser.KW_IMPORT) | (1 << ZmeiLangParser.KW_AS) | (1 << ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FLOAT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DECIMAL) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATETIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_TEXT))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 64)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 64)) | (1 << (ZmeiLangParser.KW_THEME - 64)) | (1 << (ZmeiLangParser.KW_INSTALL - 64)) | (1 << (ZmeiLangParser.KW_HEADER - 64)) | (1 << (ZmeiLangParser.KW_SERVICES - 64)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 64)) | (1 << (ZmeiLangParser.KW_CHILD - 64)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 64)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 64)) | (1 << (ZmeiLangParser.KW_PAGE - 64)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 64)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 64)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 64)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 64)) | (1 << (ZmeiLangParser.KW_BLOCK - 64)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 64)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 64)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 64)) | (1 << (ZmeiLangParser.KW_DELETE - 64)) | (1 << (ZmeiLangParser.KW_EDIT - 64)) | (1 << (ZmeiLangParser.KW_CREATE - 64)) | (1 << (ZmeiLangParser.KW_DETAIL - 64)) | (1 << (ZmeiLangParser.KW_SKIP - 64)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 64)) | (1 << (ZmeiLangParser.KW_CSS - 64)) | (1 << (ZmeiLangParser.KW_JS - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_BASIC - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_SESSION - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_TOKEN - 64)) | (1 << (ZmeiLangParser.KW_INLINE - 64)) | (1 << (ZmeiLangParser.KW_TYPE - 64)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 64)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 64)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 64)) | (1 << (ZmeiLangParser.KW_QUERY - 64)) | (1 << (ZmeiLangParser.KW_AUTH - 64)) | (1 << (ZmeiLangParser.KW_COUNT - 64)) | (1 << (ZmeiLangParser.KW_I18N - 64)) | (1 << (ZmeiLangParser.KW_EXTRA - 64)) | (1 << (ZmeiLangParser.KW_TABS - 64)) | (1 << (ZmeiLangParser.KW_LIST - 64)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 64)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 64)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 64)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 64)) | (1 << (ZmeiLangParser.KW_FIELDS - 64)))) != 0)):
                    break

            self.state = 786
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 783
                self.match(ZmeiLangParser.NL)
                self.state = 788
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 789
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_gitlab_test_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_gitlab_test_declaration_selenium_pytest(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_gitlab_test_declaration_selenium_pytestContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_gitlab_test_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_gitlab_test_declaration" ):
                listener.enterAn_gitlab_test_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_gitlab_test_declaration" ):
                listener.exitAn_gitlab_test_declaration(self)




    def an_gitlab_test_declaration(self):

        localctx = ZmeiLangParser.An_gitlab_test_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_an_gitlab_test_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 791
            self.an_gitlab_test_declaration_selenium_pytest()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_gitlab_test_declaration_selenium_pytestContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_SELENIUM_PYTEST(self):
            return self.getToken(ZmeiLangParser.KW_SELENIUM_PYTEST, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def an_gitlab_test_services(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_gitlab_test_servicesContext,0)


        def an_gitlab_deployment_variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_gitlab_deployment_variableContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_gitlab_deployment_variableContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_gitlab_test_declaration_selenium_pytest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_gitlab_test_declaration_selenium_pytest" ):
                listener.enterAn_gitlab_test_declaration_selenium_pytest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_gitlab_test_declaration_selenium_pytest" ):
                listener.exitAn_gitlab_test_declaration_selenium_pytest(self)




    def an_gitlab_test_declaration_selenium_pytest(self):

        localctx = ZmeiLangParser.An_gitlab_test_declaration_selenium_pytestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_an_gitlab_test_declaration_selenium_pytest)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 793
            self.match(ZmeiLangParser.KW_SELENIUM_PYTEST)
            self.state = 794
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 798
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 795
                    self.match(ZmeiLangParser.NL) 
                self.state = 800
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

            self.state = 802
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 801
                self.an_gitlab_test_services()


            self.state = 807
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 804
                    self.match(ZmeiLangParser.NL) 
                self.state = 809
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

            self.state = 816
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 810
                    self.an_gitlab_deployment_variable()
                    self.state = 812
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==ZmeiLangParser.COMA:
                        self.state = 811
                        self.match(ZmeiLangParser.COMA)

             
                self.state = 818
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

            self.state = 822
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 819
                self.match(ZmeiLangParser.NL)
                self.state = 824
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 825
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_gitlab_test_servicesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_SERVICES(self):
            return self.getToken(ZmeiLangParser.KW_SERVICES, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def an_gitlab_test_service(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_gitlab_test_serviceContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_gitlab_test_serviceContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_gitlab_test_services

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_gitlab_test_services" ):
                listener.enterAn_gitlab_test_services(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_gitlab_test_services" ):
                listener.exitAn_gitlab_test_services(self)




    def an_gitlab_test_services(self):

        localctx = ZmeiLangParser.An_gitlab_test_servicesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_an_gitlab_test_services)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 827
            self.match(ZmeiLangParser.KW_SERVICES)
            self.state = 828
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 832
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 829
                    self.match(ZmeiLangParser.NL) 
                self.state = 834
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

            self.state = 843
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.state = 835
                self.an_gitlab_test_service()
                self.state = 840
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZmeiLangParser.COMA:
                    self.state = 836
                    self.match(ZmeiLangParser.COMA)
                    self.state = 837
                    self.an_gitlab_test_service()
                    self.state = 842
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 848
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 845
                self.match(ZmeiLangParser.NL)
                self.state = 850
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 851
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_gitlab_test_serviceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_gitlab_test_service_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_gitlab_test_service_nameContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def an_gitlab_deployment_variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_gitlab_deployment_variableContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_gitlab_deployment_variableContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_gitlab_test_service

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_gitlab_test_service" ):
                listener.enterAn_gitlab_test_service(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_gitlab_test_service" ):
                listener.exitAn_gitlab_test_service(self)




    def an_gitlab_test_service(self):

        localctx = ZmeiLangParser.An_gitlab_test_serviceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_an_gitlab_test_service)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 856
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 853
                self.match(ZmeiLangParser.NL)
                self.state = 858
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 859
            self.an_gitlab_test_service_name()
            self.state = 883
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 860
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 864
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 861
                        self.match(ZmeiLangParser.NL) 
                    self.state = 866
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

                self.state = 873
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,53,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 867
                        self.an_gitlab_deployment_variable()
                        self.state = 869
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==ZmeiLangParser.COMA:
                            self.state = 868
                            self.match(ZmeiLangParser.COMA)

                 
                    self.state = 875
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,53,self._ctx)

                self.state = 879
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZmeiLangParser.NL:
                    self.state = 876
                    self.match(ZmeiLangParser.NL)
                    self.state = 881
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 882
                self.match(ZmeiLangParser.BRACE_CLOSE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_gitlab_test_service_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_gitlab_test_service_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_gitlab_test_service_name" ):
                listener.enterAn_gitlab_test_service_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_gitlab_test_service_name" ):
                listener.exitAn_gitlab_test_service_name(self)




    def an_gitlab_test_service_name(self):

        localctx = ZmeiLangParser.An_gitlab_test_service_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_an_gitlab_test_service_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 885
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_gitlab_branch_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_gitlab_branch_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_gitlab_branch_nameContext,0)


        def an_gitlab_branch_deploy_type(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_gitlab_branch_deploy_typeContext,0)


        def an_gitlab_deployment_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_gitlab_deployment_nameContext,0)


        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_gitlab_deployment_host(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_gitlab_deployment_hostContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_gitlab_deployment_variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_gitlab_deployment_variableContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_gitlab_deployment_variableContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_gitlab_branch_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_gitlab_branch_declaration" ):
                listener.enterAn_gitlab_branch_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_gitlab_branch_declaration" ):
                listener.exitAn_gitlab_branch_declaration(self)




    def an_gitlab_branch_declaration(self):

        localctx = ZmeiLangParser.An_gitlab_branch_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_an_gitlab_branch_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 887
            self.an_gitlab_branch_name()
            self.state = 891
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 888
                self.match(ZmeiLangParser.NL)
                self.state = 893
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 894
            self.an_gitlab_branch_deploy_type()
            self.state = 898
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 895
                self.match(ZmeiLangParser.NL)
                self.state = 900
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 901
            self.an_gitlab_deployment_name()
            self.state = 902
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 906
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 903
                self.match(ZmeiLangParser.NL)
                self.state = 908
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 909
            self.an_gitlab_deployment_host()
            self.state = 926
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COLON:
                self.state = 910
                self.match(ZmeiLangParser.COLON)
                self.state = 914
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,59,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 911
                        self.match(ZmeiLangParser.NL) 
                    self.state = 916
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,59,self._ctx)

                self.state = 923
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,61,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 917
                        self.an_gitlab_deployment_variable()
                        self.state = 919
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==ZmeiLangParser.COMA:
                            self.state = 918
                            self.match(ZmeiLangParser.COMA)

                 
                    self.state = 925
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,61,self._ctx)



            self.state = 931
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 928
                self.match(ZmeiLangParser.NL)
                self.state = 933
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 934
            self.match(ZmeiLangParser.BRACE_CLOSE)
            self.state = 938
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,64,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 935
                    self.match(ZmeiLangParser.NL) 
                self.state = 940
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,64,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_gitlab_branch_deploy_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GT(self):
            return self.getToken(ZmeiLangParser.GT, 0)

        def EQUALS(self):
            return self.getToken(ZmeiLangParser.EQUALS, 0)

        def APPROX(self):
            return self.getToken(ZmeiLangParser.APPROX, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_gitlab_branch_deploy_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_gitlab_branch_deploy_type" ):
                listener.enterAn_gitlab_branch_deploy_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_gitlab_branch_deploy_type" ):
                listener.exitAn_gitlab_branch_deploy_type(self)




    def an_gitlab_branch_deploy_type(self):

        localctx = ZmeiLangParser.An_gitlab_branch_deploy_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_an_gitlab_branch_deploy_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 941
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.EQUALS or _la==ZmeiLangParser.APPROX):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 942
            self.match(ZmeiLangParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_gitlab_branch_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Id_or_kwContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,i)


        def DASH(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.DASH)
            else:
                return self.getToken(ZmeiLangParser.DASH, i)

        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.STAR)
            else:
                return self.getToken(ZmeiLangParser.STAR, i)

        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.SLASH)
            else:
                return self.getToken(ZmeiLangParser.SLASH, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_gitlab_branch_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_gitlab_branch_name" ):
                listener.enterAn_gitlab_branch_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_gitlab_branch_name" ):
                listener.exitAn_gitlab_branch_name(self)




    def an_gitlab_branch_name(self):

        localctx = ZmeiLangParser.An_gitlab_branch_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_an_gitlab_branch_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 948 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 948
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS]:
                    self.state = 944
                    self.id_or_kw()
                    pass
                elif token in [ZmeiLangParser.DASH]:
                    self.state = 945
                    self.match(ZmeiLangParser.DASH)
                    pass
                elif token in [ZmeiLangParser.STAR]:
                    self.state = 946
                    self.match(ZmeiLangParser.STAR)
                    pass
                elif token in [ZmeiLangParser.SLASH]:
                    self.state = 947
                    self.match(ZmeiLangParser.SLASH)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 950 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.WRITE_MODE) | (1 << ZmeiLangParser.BOOL) | (1 << ZmeiLangParser.ID) | (1 << ZmeiLangParser.DASH) | (1 << ZmeiLangParser.SLASH) | (1 << ZmeiLangParser.STAR) | (1 << ZmeiLangParser.KW_FROM) | (1 << ZmeiLangParser.KW_IMPORT) | (1 << ZmeiLangParser.KW_AS) | (1 << ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FLOAT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DECIMAL) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATETIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_TEXT))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 64)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 64)) | (1 << (ZmeiLangParser.KW_THEME - 64)) | (1 << (ZmeiLangParser.KW_INSTALL - 64)) | (1 << (ZmeiLangParser.KW_HEADER - 64)) | (1 << (ZmeiLangParser.KW_SERVICES - 64)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 64)) | (1 << (ZmeiLangParser.KW_CHILD - 64)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 64)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 64)) | (1 << (ZmeiLangParser.KW_PAGE - 64)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 64)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 64)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 64)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 64)) | (1 << (ZmeiLangParser.KW_BLOCK - 64)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 64)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 64)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 64)) | (1 << (ZmeiLangParser.KW_DELETE - 64)) | (1 << (ZmeiLangParser.KW_EDIT - 64)) | (1 << (ZmeiLangParser.KW_CREATE - 64)) | (1 << (ZmeiLangParser.KW_DETAIL - 64)) | (1 << (ZmeiLangParser.KW_SKIP - 64)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 64)) | (1 << (ZmeiLangParser.KW_CSS - 64)) | (1 << (ZmeiLangParser.KW_JS - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_BASIC - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_SESSION - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_TOKEN - 64)) | (1 << (ZmeiLangParser.KW_INLINE - 64)) | (1 << (ZmeiLangParser.KW_TYPE - 64)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 64)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 64)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 64)) | (1 << (ZmeiLangParser.KW_QUERY - 64)) | (1 << (ZmeiLangParser.KW_AUTH - 64)) | (1 << (ZmeiLangParser.KW_COUNT - 64)) | (1 << (ZmeiLangParser.KW_I18N - 64)) | (1 << (ZmeiLangParser.KW_EXTRA - 64)) | (1 << (ZmeiLangParser.KW_TABS - 64)) | (1 << (ZmeiLangParser.KW_LIST - 64)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 64)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 64)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 64)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 64)) | (1 << (ZmeiLangParser.KW_FIELDS - 64)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_gitlab_deployment_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Id_or_kwContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,i)


        def DASH(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.DASH)
            else:
                return self.getToken(ZmeiLangParser.DASH, i)

        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.SLASH)
            else:
                return self.getToken(ZmeiLangParser.SLASH, i)

        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.STAR)
            else:
                return self.getToken(ZmeiLangParser.STAR, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_gitlab_deployment_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_gitlab_deployment_name" ):
                listener.enterAn_gitlab_deployment_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_gitlab_deployment_name" ):
                listener.exitAn_gitlab_deployment_name(self)




    def an_gitlab_deployment_name(self):

        localctx = ZmeiLangParser.An_gitlab_deployment_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_an_gitlab_deployment_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 956 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 956
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS]:
                    self.state = 952
                    self.id_or_kw()
                    pass
                elif token in [ZmeiLangParser.DASH]:
                    self.state = 953
                    self.match(ZmeiLangParser.DASH)
                    pass
                elif token in [ZmeiLangParser.SLASH]:
                    self.state = 954
                    self.match(ZmeiLangParser.SLASH)
                    pass
                elif token in [ZmeiLangParser.STAR]:
                    self.state = 955
                    self.match(ZmeiLangParser.STAR)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 958 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.WRITE_MODE) | (1 << ZmeiLangParser.BOOL) | (1 << ZmeiLangParser.ID) | (1 << ZmeiLangParser.DASH) | (1 << ZmeiLangParser.SLASH) | (1 << ZmeiLangParser.STAR) | (1 << ZmeiLangParser.KW_FROM) | (1 << ZmeiLangParser.KW_IMPORT) | (1 << ZmeiLangParser.KW_AS) | (1 << ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FLOAT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DECIMAL) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATETIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_TEXT))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 64)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 64)) | (1 << (ZmeiLangParser.KW_THEME - 64)) | (1 << (ZmeiLangParser.KW_INSTALL - 64)) | (1 << (ZmeiLangParser.KW_HEADER - 64)) | (1 << (ZmeiLangParser.KW_SERVICES - 64)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 64)) | (1 << (ZmeiLangParser.KW_CHILD - 64)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 64)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 64)) | (1 << (ZmeiLangParser.KW_PAGE - 64)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 64)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 64)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 64)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 64)) | (1 << (ZmeiLangParser.KW_BLOCK - 64)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 64)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 64)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 64)) | (1 << (ZmeiLangParser.KW_DELETE - 64)) | (1 << (ZmeiLangParser.KW_EDIT - 64)) | (1 << (ZmeiLangParser.KW_CREATE - 64)) | (1 << (ZmeiLangParser.KW_DETAIL - 64)) | (1 << (ZmeiLangParser.KW_SKIP - 64)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 64)) | (1 << (ZmeiLangParser.KW_CSS - 64)) | (1 << (ZmeiLangParser.KW_JS - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_BASIC - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_SESSION - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_TOKEN - 64)) | (1 << (ZmeiLangParser.KW_INLINE - 64)) | (1 << (ZmeiLangParser.KW_TYPE - 64)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 64)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 64)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 64)) | (1 << (ZmeiLangParser.KW_QUERY - 64)) | (1 << (ZmeiLangParser.KW_AUTH - 64)) | (1 << (ZmeiLangParser.KW_COUNT - 64)) | (1 << (ZmeiLangParser.KW_I18N - 64)) | (1 << (ZmeiLangParser.KW_EXTRA - 64)) | (1 << (ZmeiLangParser.KW_TABS - 64)) | (1 << (ZmeiLangParser.KW_LIST - 64)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 64)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 64)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 64)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 64)) | (1 << (ZmeiLangParser.KW_FIELDS - 64)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_gitlab_deployment_hostContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Id_or_kwContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,i)


        def DASH(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.DASH)
            else:
                return self.getToken(ZmeiLangParser.DASH, i)

        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.STAR)
            else:
                return self.getToken(ZmeiLangParser.STAR, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.DOT)
            else:
                return self.getToken(ZmeiLangParser.DOT, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_gitlab_deployment_host

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_gitlab_deployment_host" ):
                listener.enterAn_gitlab_deployment_host(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_gitlab_deployment_host" ):
                listener.exitAn_gitlab_deployment_host(self)




    def an_gitlab_deployment_host(self):

        localctx = ZmeiLangParser.An_gitlab_deployment_hostContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_an_gitlab_deployment_host)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 964 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 964
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS]:
                    self.state = 960
                    self.id_or_kw()
                    pass
                elif token in [ZmeiLangParser.DASH]:
                    self.state = 961
                    self.match(ZmeiLangParser.DASH)
                    pass
                elif token in [ZmeiLangParser.STAR]:
                    self.state = 962
                    self.match(ZmeiLangParser.STAR)
                    pass
                elif token in [ZmeiLangParser.DOT]:
                    self.state = 963
                    self.match(ZmeiLangParser.DOT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 966 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.WRITE_MODE) | (1 << ZmeiLangParser.BOOL) | (1 << ZmeiLangParser.ID) | (1 << ZmeiLangParser.DASH) | (1 << ZmeiLangParser.DOT) | (1 << ZmeiLangParser.STAR) | (1 << ZmeiLangParser.KW_FROM) | (1 << ZmeiLangParser.KW_IMPORT) | (1 << ZmeiLangParser.KW_AS) | (1 << ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FLOAT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DECIMAL) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATETIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_TEXT))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 64)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 64)) | (1 << (ZmeiLangParser.KW_THEME - 64)) | (1 << (ZmeiLangParser.KW_INSTALL - 64)) | (1 << (ZmeiLangParser.KW_HEADER - 64)) | (1 << (ZmeiLangParser.KW_SERVICES - 64)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 64)) | (1 << (ZmeiLangParser.KW_CHILD - 64)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 64)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 64)) | (1 << (ZmeiLangParser.KW_PAGE - 64)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 64)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 64)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 64)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 64)) | (1 << (ZmeiLangParser.KW_BLOCK - 64)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 64)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 64)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 64)) | (1 << (ZmeiLangParser.KW_DELETE - 64)) | (1 << (ZmeiLangParser.KW_EDIT - 64)) | (1 << (ZmeiLangParser.KW_CREATE - 64)) | (1 << (ZmeiLangParser.KW_DETAIL - 64)) | (1 << (ZmeiLangParser.KW_SKIP - 64)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 64)) | (1 << (ZmeiLangParser.KW_CSS - 64)) | (1 << (ZmeiLangParser.KW_JS - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_BASIC - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_SESSION - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_TOKEN - 64)) | (1 << (ZmeiLangParser.KW_INLINE - 64)) | (1 << (ZmeiLangParser.KW_TYPE - 64)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 64)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 64)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 64)) | (1 << (ZmeiLangParser.KW_QUERY - 64)) | (1 << (ZmeiLangParser.KW_AUTH - 64)) | (1 << (ZmeiLangParser.KW_COUNT - 64)) | (1 << (ZmeiLangParser.KW_I18N - 64)) | (1 << (ZmeiLangParser.KW_EXTRA - 64)) | (1 << (ZmeiLangParser.KW_TABS - 64)) | (1 << (ZmeiLangParser.KW_LIST - 64)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 64)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 64)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 64)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 64)) | (1 << (ZmeiLangParser.KW_FIELDS - 64)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_gitlab_deployment_variableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_gitlab_deployment_variable_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_gitlab_deployment_variable_nameContext,0)


        def EQUALS(self):
            return self.getToken(ZmeiLangParser.EQUALS, 0)

        def an_gitlab_deployment_variable_value(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_gitlab_deployment_variable_valueContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_gitlab_deployment_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_gitlab_deployment_variable" ):
                listener.enterAn_gitlab_deployment_variable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_gitlab_deployment_variable" ):
                listener.exitAn_gitlab_deployment_variable(self)




    def an_gitlab_deployment_variable(self):

        localctx = ZmeiLangParser.An_gitlab_deployment_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_an_gitlab_deployment_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 971
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 968
                self.match(ZmeiLangParser.NL)
                self.state = 973
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 974
            self.an_gitlab_deployment_variable_name()
            self.state = 975
            self.match(ZmeiLangParser.EQUALS)
            self.state = 976
            self.an_gitlab_deployment_variable_value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_gitlab_deployment_variable_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_gitlab_deployment_variable_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_gitlab_deployment_variable_name" ):
                listener.enterAn_gitlab_deployment_variable_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_gitlab_deployment_variable_name" ):
                listener.exitAn_gitlab_deployment_variable_name(self)




    def an_gitlab_deployment_variable_name(self):

        localctx = ZmeiLangParser.An_gitlab_deployment_variable_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_an_gitlab_deployment_variable_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 978
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_gitlab_deployment_variable_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def DIGIT(self):
            return self.getToken(ZmeiLangParser.DIGIT, 0)

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_gitlab_deployment_variable_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_gitlab_deployment_variable_value" ):
                listener.enterAn_gitlab_deployment_variable_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_gitlab_deployment_variable_value" ):
                listener.exitAn_gitlab_deployment_variable_value(self)




    def an_gitlab_deployment_variable_value(self):

        localctx = ZmeiLangParser.An_gitlab_deployment_variable_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_an_gitlab_deployment_variable_value)
        try:
            self.state = 984
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.STRING_DQ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 980
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.enterOuterAlt(localctx, 2)
                self.state = 981
                self.match(ZmeiLangParser.STRING_SQ)
                pass
            elif token in [ZmeiLangParser.DIGIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 982
                self.match(ZmeiLangParser.DIGIT)
                pass
            elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS]:
                self.enterOuterAlt(localctx, 4)
                self.state = 983
                self.id_or_kw()
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


    class An_fileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_FILE(self):
            return self.getToken(ZmeiLangParser.AN_FILE, 0)

        def an_file_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_file_nameContext,0)


        def python_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Python_codeContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_file" ):
                listener.enterAn_file(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_file" ):
                listener.exitAn_file(self)




    def an_file(self):

        localctx = ZmeiLangParser.An_fileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_an_file)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 986
            self.match(ZmeiLangParser.AN_FILE)
            self.state = 987
            self.an_file_name()
            self.state = 988
            self.python_code()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_file_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_file_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_file_name" ):
                listener.enterAn_file_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_file_name" ):
                listener.exitAn_file_name(self)




    def an_file_name(self):

        localctx = ZmeiLangParser.An_file_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_an_file_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 990
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.STRING_DQ):
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


    class An_themeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_THEME(self):
            return self.getToken(ZmeiLangParser.AN_THEME, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_theme_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_theme_nameContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def COMA(self):
            return self.getToken(ZmeiLangParser.COMA, 0)

        def KW_INSTALL(self):
            return self.getToken(ZmeiLangParser.KW_INSTALL, 0)

        def EQUALS(self):
            return self.getToken(ZmeiLangParser.EQUALS, 0)

        def an_theme_install(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_theme_installContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_theme

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_theme" ):
                listener.enterAn_theme(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_theme" ):
                listener.exitAn_theme(self)




    def an_theme(self):

        localctx = ZmeiLangParser.An_themeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_an_theme)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 992
            self.match(ZmeiLangParser.AN_THEME)
            self.state = 993
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 994
            self.an_theme_name()
            self.state = 999
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COMA:
                self.state = 995
                self.match(ZmeiLangParser.COMA)
                self.state = 996
                self.match(ZmeiLangParser.KW_INSTALL)
                self.state = 997
                self.match(ZmeiLangParser.EQUALS)
                self.state = 998
                self.an_theme_install()


            self.state = 1001
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_theme_installContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(ZmeiLangParser.BOOL, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_theme_install

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_theme_install" ):
                listener.enterAn_theme_install(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_theme_install" ):
                listener.exitAn_theme_install(self)




    def an_theme_install(self):

        localctx = ZmeiLangParser.An_theme_installContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_an_theme_install)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1003
            self.match(ZmeiLangParser.BOOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_theme_nameContext(ParserRuleContext):

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
            return ZmeiLangParser.RULE_an_theme_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_theme_name" ):
                listener.enterAn_theme_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_theme_name" ):
                listener.exitAn_theme_name(self)




    def an_theme_name(self):

        localctx = ZmeiLangParser.An_theme_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_an_theme_name)
        try:
            self.state = 1008
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1005
                self.id_or_kw()
                pass
            elif token in [ZmeiLangParser.STRING_DQ]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1006
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1007
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


    class An_langsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_LANGS(self):
            return self.getToken(ZmeiLangParser.AN_LANGS, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_langs_list(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_langs_listContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_langs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_langs" ):
                listener.enterAn_langs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_langs" ):
                listener.exitAn_langs(self)




    def an_langs(self):

        localctx = ZmeiLangParser.An_langsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_an_langs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1010
            self.match(ZmeiLangParser.AN_LANGS)
            self.state = 1011
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1012
            self.an_langs_list()
            self.state = 1013
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_langs_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.ID)
            else:
                return self.getToken(ZmeiLangParser.ID, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_langs_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_langs_list" ):
                listener.enterAn_langs_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_langs_list" ):
                listener.exitAn_langs_list(self)




    def an_langs_list(self):

        localctx = ZmeiLangParser.An_langs_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_an_langs_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1015
            self.match(ZmeiLangParser.ID)
            self.state = 1020
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 1016
                self.match(ZmeiLangParser.COMA)
                self.state = 1017
                self.match(ZmeiLangParser.ID)
                self.state = 1022
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

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
        self.enterRule(localctx, 98, self.RULE_col)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1023
            self.col_header()
            self.state = 1025
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,76,self._ctx)
            if la_ == 1:
                self.state = 1024
                self.col_str_expr()


            self.state = 1030
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,77,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1027
                    self.match(ZmeiLangParser.NL) 
                self.state = 1032
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,77,self._ctx)

            self.state = 1036
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.WRITE_MODE) | (1 << ZmeiLangParser.BOOL) | (1 << ZmeiLangParser.ID) | (1 << ZmeiLangParser.EQUALS) | (1 << ZmeiLangParser.DOLLAR) | (1 << ZmeiLangParser.AMP) | (1 << ZmeiLangParser.EXCLAM) | (1 << ZmeiLangParser.STAR) | (1 << ZmeiLangParser.APPROX) | (1 << ZmeiLangParser.KW_FROM) | (1 << ZmeiLangParser.KW_IMPORT) | (1 << ZmeiLangParser.KW_AS) | (1 << ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FLOAT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DECIMAL) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATETIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_TEXT))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 64)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 64)) | (1 << (ZmeiLangParser.KW_THEME - 64)) | (1 << (ZmeiLangParser.KW_INSTALL - 64)) | (1 << (ZmeiLangParser.KW_HEADER - 64)) | (1 << (ZmeiLangParser.KW_SERVICES - 64)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 64)) | (1 << (ZmeiLangParser.KW_CHILD - 64)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 64)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 64)) | (1 << (ZmeiLangParser.KW_PAGE - 64)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 64)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 64)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 64)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 64)) | (1 << (ZmeiLangParser.KW_BLOCK - 64)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 64)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 64)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 64)) | (1 << (ZmeiLangParser.KW_DELETE - 64)) | (1 << (ZmeiLangParser.KW_EDIT - 64)) | (1 << (ZmeiLangParser.KW_CREATE - 64)) | (1 << (ZmeiLangParser.KW_DETAIL - 64)) | (1 << (ZmeiLangParser.KW_SKIP - 64)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 64)) | (1 << (ZmeiLangParser.KW_CSS - 64)) | (1 << (ZmeiLangParser.KW_JS - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_BASIC - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_SESSION - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_TOKEN - 64)) | (1 << (ZmeiLangParser.KW_INLINE - 64)) | (1 << (ZmeiLangParser.KW_TYPE - 64)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 64)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 64)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 64)) | (1 << (ZmeiLangParser.KW_QUERY - 64)) | (1 << (ZmeiLangParser.KW_AUTH - 64)) | (1 << (ZmeiLangParser.KW_COUNT - 64)) | (1 << (ZmeiLangParser.KW_I18N - 64)) | (1 << (ZmeiLangParser.KW_EXTRA - 64)) | (1 << (ZmeiLangParser.KW_TABS - 64)) | (1 << (ZmeiLangParser.KW_LIST - 64)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 64)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 64)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 64)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 64)) | (1 << (ZmeiLangParser.KW_FIELDS - 64)))) != 0):
                self.state = 1033
                self.col_field()
                self.state = 1038
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1042
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,79,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1039
                    self.match(ZmeiLangParser.NL) 
                self.state = 1044
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,79,self._ctx)

            self.state = 1048
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,80,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1045
                    self.model_annotation() 
                self.state = 1050
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,80,self._ctx)

            self.state = 1054
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,81,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1051
                    self.match(ZmeiLangParser.NL) 
                self.state = 1056
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,81,self._ctx)

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
        self.enterRule(localctx, 100, self.RULE_col_str_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1057
            self.match(ZmeiLangParser.EQUALS)
            self.state = 1058
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.STRING_DQ or _la==ZmeiLangParser.STRING_SQ):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 1065
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.NL]:
                self.state = 1060 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 1059
                        self.match(ZmeiLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 1062 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,82,self._ctx)

                pass
            elif token in [ZmeiLangParser.EOF]:
                self.state = 1064
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

        def HASH(self):
            return self.getToken(ZmeiLangParser.HASH, 0)

        def col_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_nameContext,0)


        def col_header_line_separator(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_header_line_separatorContext,0)


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
        self.enterRule(localctx, 102, self.RULE_col_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1067
            self.match(ZmeiLangParser.HASH)
            self.state = 1069
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,84,self._ctx)
            if la_ == 1:
                self.state = 1068
                self.col_base_name()


            self.state = 1071
            self.col_name()
            self.state = 1073
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COLON:
                self.state = 1072
                self.col_verbose_name()


            self.state = 1075
            self.col_header_line_separator()
            self.state = 1076
            self.match(ZmeiLangParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Col_header_line_separatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self):
            return self.getToken(ZmeiLangParser.NL, 0)

        def DASH(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.DASH)
            else:
                return self.getToken(ZmeiLangParser.DASH, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_header_line_separator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_header_line_separator" ):
                listener.enterCol_header_line_separator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_header_line_separator" ):
                listener.exitCol_header_line_separator(self)




    def col_header_line_separator(self):

        localctx = ZmeiLangParser.Col_header_line_separatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_col_header_line_separator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1078
            self.match(ZmeiLangParser.NL)
            self.state = 1079
            self.match(ZmeiLangParser.DASH)
            self.state = 1080
            self.match(ZmeiLangParser.DASH)
            self.state = 1082 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1081
                self.match(ZmeiLangParser.DASH)
                self.state = 1084 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZmeiLangParser.DASH):
                    break

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
        self.enterRule(localctx, 106, self.RULE_col_verbose_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1086
            self.match(ZmeiLangParser.COLON)
            self.state = 1087
            self.verbose_name_part()
            self.state = 1090
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.SLASH:
                self.state = 1088
                self.match(ZmeiLangParser.SLASH)
                self.state = 1089
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
        self.enterRule(localctx, 108, self.RULE_verbose_name_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1095
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS]:
                self.state = 1092
                self.id_or_kw()
                pass
            elif token in [ZmeiLangParser.STRING_DQ]:
                self.state = 1093
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.state = 1094
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


        def DASH(self):
            return self.getToken(ZmeiLangParser.DASH, 0)

        def GT(self):
            return self.getToken(ZmeiLangParser.GT, 0)

        def APPROX(self):
            return self.getToken(ZmeiLangParser.APPROX, 0)

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
        self.enterRule(localctx, 110, self.RULE_col_base_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1097
            self.id_or_kw()
            self.state = 1102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.DASH]:
                self.state = 1098
                self.match(ZmeiLangParser.DASH)
                self.state = 1099
                self.match(ZmeiLangParser.GT)
                pass
            elif token in [ZmeiLangParser.APPROX]:
                self.state = 1100
                self.match(ZmeiLangParser.APPROX)
                self.state = 1101
                self.match(ZmeiLangParser.GT)
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
        self.enterRule(localctx, 112, self.RULE_col_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1104
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


        def col_field_expr_or_def(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_field_expr_or_defContext,0)


        def col_field_verbose_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_field_verbose_nameContext,0)


        def col_field_help_text(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_field_help_textContext,0)


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
        self.enterRule(localctx, 114, self.RULE_col_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.EQUALS) | (1 << ZmeiLangParser.DOLLAR) | (1 << ZmeiLangParser.AMP) | (1 << ZmeiLangParser.EXCLAM) | (1 << ZmeiLangParser.STAR) | (1 << ZmeiLangParser.APPROX))) != 0):
                self.state = 1106
                self.col_modifier()
                self.state = 1111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1112
            self.col_field_name()
            self.state = 1114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.COLON) | (1 << ZmeiLangParser.ASSIGN) | (1 << ZmeiLangParser.ASSIGN_STATIC))) != 0):
                self.state = 1113
                self.col_field_expr_or_def()


            self.state = 1117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.SLASH:
                self.state = 1116
                self.col_field_verbose_name()


            self.state = 1120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.QUESTION_MARK:
                self.state = 1119
                self.col_field_help_text()


            self.state = 1128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.NL]:
                self.state = 1123 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 1122
                        self.match(ZmeiLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 1125 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,94,self._ctx)

                pass
            elif token in [ZmeiLangParser.EOF]:
                self.state = 1127
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


    class Col_field_expr_or_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def col_field_expr(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_field_exprContext,0)


        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def col_field_def(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_field_defContext,0)


        def wrong_field_type(self):
            return self.getTypedRuleContext(ZmeiLangParser.Wrong_field_typeContext,0)


        def col_field_custom(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_field_customContext,0)


        def col_field_extend(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_field_extendContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_field_expr_or_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_field_expr_or_def" ):
                listener.enterCol_field_expr_or_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_field_expr_or_def" ):
                listener.exitCol_field_expr_or_def(self)




    def col_field_expr_or_def(self):

        localctx = ZmeiLangParser.Col_field_expr_or_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_col_field_expr_or_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,98,self._ctx)
            if la_ == 1:
                self.state = 1130
                self.match(ZmeiLangParser.COLON)
                self.state = 1132
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.CODE_BLOCK:
                    self.state = 1131
                    self.col_field_custom()


                pass

            elif la_ == 2:
                self.state = 1134
                self.match(ZmeiLangParser.COLON)
                self.state = 1135
                self.col_field_def()
                self.state = 1137
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.DOT or _la==ZmeiLangParser.CODE_BLOCK:
                    self.state = 1136
                    self.col_field_extend()


                pass

            elif la_ == 3:
                self.state = 1139
                self.match(ZmeiLangParser.COLON)
                self.state = 1140
                self.wrong_field_type()
                pass

            elif la_ == 4:
                self.state = 1141
                self.col_field_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Col_field_customContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_field_custom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_field_custom" ):
                listener.enterCol_field_custom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_field_custom" ):
                listener.exitCol_field_custom(self)




    def col_field_custom(self):

        localctx = ZmeiLangParser.Col_field_customContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_col_field_custom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1144
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Col_field_extendContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def col_field_extend_append(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_field_extend_appendContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_field_extend

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_field_extend" ):
                listener.enterCol_field_extend(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_field_extend" ):
                listener.exitCol_field_extend(self)




    def col_field_extend(self):

        localctx = ZmeiLangParser.Col_field_extendContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_col_field_extend)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 1146
                self.col_field_extend_append()


            self.state = 1149
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Col_field_extend_appendContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.DOT)
            else:
                return self.getToken(ZmeiLangParser.DOT, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_field_extend_append

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_field_extend_append" ):
                listener.enterCol_field_extend_append(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_field_extend_append" ):
                listener.exitCol_field_extend_append(self)




    def col_field_extend_append(self):

        localctx = ZmeiLangParser.Col_field_extend_appendContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_col_field_extend_append)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1151
            self.match(ZmeiLangParser.DOT)
            self.state = 1152
            self.match(ZmeiLangParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Wrong_field_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_wrong_field_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrong_field_type" ):
                listener.enterWrong_field_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrong_field_type" ):
                listener.exitWrong_field_type(self)




    def wrong_field_type(self):

        localctx = ZmeiLangParser.Wrong_field_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_wrong_field_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1154
            self.id_or_kw()
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
        self.enterRule(localctx, 126, self.RULE_col_field_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1156
            self.col_field_expr_marker()
            self.state = 1157
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
        self.enterRule(localctx, 128, self.RULE_col_field_expr_marker)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1159
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

        def PYTHON_CODE(self):
            return self.getToken(ZmeiLangParser.PYTHON_CODE, 0)

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
        self.enterRule(localctx, 130, self.RULE_col_feild_expr_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1161
            self.match(ZmeiLangParser.PYTHON_CODE)
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
        self.enterRule(localctx, 132, self.RULE_string_or_quoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS]:
                self.state = 1164 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 1163
                    self.id_or_kw()
                    self.state = 1166 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.WRITE_MODE) | (1 << ZmeiLangParser.BOOL) | (1 << ZmeiLangParser.ID) | (1 << ZmeiLangParser.KW_FROM) | (1 << ZmeiLangParser.KW_IMPORT) | (1 << ZmeiLangParser.KW_AS) | (1 << ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FLOAT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DECIMAL) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATETIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_TEXT))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 64)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 64)) | (1 << (ZmeiLangParser.KW_THEME - 64)) | (1 << (ZmeiLangParser.KW_INSTALL - 64)) | (1 << (ZmeiLangParser.KW_HEADER - 64)) | (1 << (ZmeiLangParser.KW_SERVICES - 64)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 64)) | (1 << (ZmeiLangParser.KW_CHILD - 64)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 64)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 64)) | (1 << (ZmeiLangParser.KW_PAGE - 64)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 64)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 64)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 64)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 64)) | (1 << (ZmeiLangParser.KW_BLOCK - 64)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 64)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 64)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 64)) | (1 << (ZmeiLangParser.KW_DELETE - 64)) | (1 << (ZmeiLangParser.KW_EDIT - 64)) | (1 << (ZmeiLangParser.KW_CREATE - 64)) | (1 << (ZmeiLangParser.KW_DETAIL - 64)) | (1 << (ZmeiLangParser.KW_SKIP - 64)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 64)) | (1 << (ZmeiLangParser.KW_CSS - 64)) | (1 << (ZmeiLangParser.KW_JS - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_BASIC - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_SESSION - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_TOKEN - 64)) | (1 << (ZmeiLangParser.KW_INLINE - 64)) | (1 << (ZmeiLangParser.KW_TYPE - 64)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 64)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 64)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 64)) | (1 << (ZmeiLangParser.KW_QUERY - 64)) | (1 << (ZmeiLangParser.KW_AUTH - 64)) | (1 << (ZmeiLangParser.KW_COUNT - 64)) | (1 << (ZmeiLangParser.KW_I18N - 64)) | (1 << (ZmeiLangParser.KW_EXTRA - 64)) | (1 << (ZmeiLangParser.KW_TABS - 64)) | (1 << (ZmeiLangParser.KW_LIST - 64)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 64)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 64)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 64)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 64)) | (1 << (ZmeiLangParser.KW_FIELDS - 64)))) != 0)):
                        break

                pass
            elif token in [ZmeiLangParser.STRING_DQ]:
                self.state = 1168
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.state = 1169
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
        self.enterRule(localctx, 134, self.RULE_col_field_help_text)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1172
            self.match(ZmeiLangParser.QUESTION_MARK)
            self.state = 1173
            self.string_or_quoted()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Col_field_verbose_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SLASH(self):
            return self.getToken(ZmeiLangParser.SLASH, 0)

        def string_or_quoted(self):
            return self.getTypedRuleContext(ZmeiLangParser.String_or_quotedContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_field_verbose_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_field_verbose_name" ):
                listener.enterCol_field_verbose_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_field_verbose_name" ):
                listener.exitCol_field_verbose_name(self)




    def col_field_verbose_name(self):

        localctx = ZmeiLangParser.Col_field_verbose_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_col_field_verbose_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1175
            self.match(ZmeiLangParser.SLASH)
            self.state = 1176
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
        self.enterRule(localctx, 138, self.RULE_col_field_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1178
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
        self.enterRule(localctx, 140, self.RULE_col_modifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1180
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.EQUALS) | (1 << ZmeiLangParser.DOLLAR) | (1 << ZmeiLangParser.AMP) | (1 << ZmeiLangParser.EXCLAM) | (1 << ZmeiLangParser.STAR) | (1 << ZmeiLangParser.APPROX))) != 0)):
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


        def field_image(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_imageContext,0)


        def field_file(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_fileContext,0)


        def field_filer_file(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_filer_fileContext,0)


        def field_filer_folder(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_filer_folderContext,0)


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
        self.enterRule(localctx, 142, self.RULE_col_field_def)
        try:
            self.state = 1200
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1182
                self.field_longtext()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1183
                self.field_html_media()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_HTML]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1184
                self.field_html()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_FLOAT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1185
                self.field_float()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_DECIMAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1186
                self.field_decimal()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_DATE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 1187
                self.field_date()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_DATETIME]:
                self.enterOuterAlt(localctx, 7)
                self.state = 1188
                self.field_datetime()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME]:
                self.enterOuterAlt(localctx, 8)
                self.state = 1189
                self.field_create_time()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME]:
                self.enterOuterAlt(localctx, 9)
                self.state = 1190
                self.field_update_time()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_TEXT]:
                self.enterOuterAlt(localctx, 10)
                self.state = 1191
                self.field_text()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_INT]:
                self.enterOuterAlt(localctx, 11)
                self.state = 1192
                self.field_int()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_SLUG]:
                self.enterOuterAlt(localctx, 12)
                self.state = 1193
                self.field_slug()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_BOOL]:
                self.enterOuterAlt(localctx, 13)
                self.state = 1194
                self.field_bool()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY]:
                self.enterOuterAlt(localctx, 14)
                self.state = 1195
                self.field_relation()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER]:
                self.enterOuterAlt(localctx, 15)
                self.state = 1196
                self.field_image()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_FILE]:
                self.enterOuterAlt(localctx, 16)
                self.state = 1197
                self.field_file()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE]:
                self.enterOuterAlt(localctx, 17)
                self.state = 1198
                self.field_filer_file()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER]:
                self.enterOuterAlt(localctx, 18)
                self.state = 1199
                self.field_filer_folder()
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
        self.enterRule(localctx, 144, self.RULE_field_longtext)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1202
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
        self.enterRule(localctx, 146, self.RULE_field_html)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1204
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
        self.enterRule(localctx, 148, self.RULE_field_html_media)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1206
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
        self.enterRule(localctx, 150, self.RULE_field_float)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1208
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
        self.enterRule(localctx, 152, self.RULE_field_decimal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1210
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
        self.enterRule(localctx, 154, self.RULE_field_date)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1212
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
        self.enterRule(localctx, 156, self.RULE_field_datetime)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1214
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
        self.enterRule(localctx, 158, self.RULE_field_create_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1216
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
        self.enterRule(localctx, 160, self.RULE_field_update_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1218
            self.match(ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME)
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
        self.enterRule(localctx, 162, self.RULE_field_file)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1220
            self.match(ZmeiLangParser.COL_FIELD_TYPE_FILE)
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
        self.enterRule(localctx, 164, self.RULE_field_filer_file)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1222
            self.match(ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_filer_folderContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_FILER_FOLDER(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_filer_folder

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_filer_folder" ):
                listener.enterField_filer_folder(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_filer_folder" ):
                listener.exitField_filer_folder(self)




    def field_filer_folder(self):

        localctx = ZmeiLangParser.Field_filer_folderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_field_filer_folder)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1224
            self.match(ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER)
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
        self.enterRule(localctx, 168, self.RULE_field_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1226
            self.match(ZmeiLangParser.COL_FIELD_TYPE_TEXT)
            self.state = 1235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1227
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1228
                self.field_text_size()
                self.state = 1231
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.COMA:
                    self.state = 1229
                    self.match(ZmeiLangParser.COMA)
                    self.state = 1230
                    self.field_text_choices()


                self.state = 1233
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
        self.enterRule(localctx, 170, self.RULE_field_text_size)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1237
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
        self.enterRule(localctx, 172, self.RULE_field_text_choices)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1239
            self.match(ZmeiLangParser.COL_FIELD_CHOICES)
            self.state = 1240
            self.match(ZmeiLangParser.EQUALS)
            self.state = 1241
            self.field_text_choice()
            self.state = 1246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 1242
                self.match(ZmeiLangParser.COMA)
                self.state = 1243
                self.field_text_choice()
                self.state = 1248
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
        self.enterRule(localctx, 174, self.RULE_field_text_choice)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,106,self._ctx)
            if la_ == 1:
                self.state = 1249
                self.field_text_choice_key()


            self.state = 1252
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

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


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
        self.enterRule(localctx, 176, self.RULE_field_text_choice_val)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1257
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS]:
                self.state = 1254
                self.id_or_kw()
                pass
            elif token in [ZmeiLangParser.STRING_DQ]:
                self.state = 1255
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.state = 1256
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


    class Field_text_choice_keyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


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
        self.enterRule(localctx, 178, self.RULE_field_text_choice_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1259
            self.id_or_kw()
            self.state = 1260
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
        self.enterRule(localctx, 180, self.RULE_field_int)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1262
            self.match(ZmeiLangParser.COL_FIELD_TYPE_INT)
            self.state = 1267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1263
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1264
                self.field_int_choices()
                self.state = 1265
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
        self.enterRule(localctx, 182, self.RULE_field_int_choices)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1269
            self.match(ZmeiLangParser.COL_FIELD_CHOICES)
            self.state = 1270
            self.match(ZmeiLangParser.EQUALS)
            self.state = 1271
            self.field_int_choice()
            self.state = 1276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 1272
                self.match(ZmeiLangParser.COMA)
                self.state = 1273
                self.field_int_choice()
                self.state = 1278
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
        self.enterRule(localctx, 184, self.RULE_field_int_choice)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DIGIT:
                self.state = 1279
                self.field_int_choice_key()


            self.state = 1282
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

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


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
        self.enterRule(localctx, 186, self.RULE_field_int_choice_val)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1287
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS]:
                self.state = 1284
                self.id_or_kw()
                pass
            elif token in [ZmeiLangParser.STRING_DQ]:
                self.state = 1285
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.state = 1286
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
        self.enterRule(localctx, 188, self.RULE_field_int_choice_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1289
            self.match(ZmeiLangParser.DIGIT)
            self.state = 1290
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
        self.enterRule(localctx, 190, self.RULE_field_slug)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1292
            self.match(ZmeiLangParser.COL_FIELD_TYPE_SLUG)
            self.state = 1293
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1294
            self.field_slug_ref_field()
            self.state = 1295
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
        self.enterRule(localctx, 192, self.RULE_field_slug_ref_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1297
            self.field_slug_ref_field_id()
            self.state = 1302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 1298
                self.match(ZmeiLangParser.COMA)
                self.state = 1299
                self.field_slug_ref_field_id()
                self.state = 1304
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

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


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
        self.enterRule(localctx, 194, self.RULE_field_slug_ref_field_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1305
            self.id_or_kw()
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
        self.enterRule(localctx, 196, self.RULE_field_bool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1307
            self.match(ZmeiLangParser.COL_FIELD_TYPE_BOOL)
            self.state = 1312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1308
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1309
                self.field_bool_default()
                self.state = 1310
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
        self.enterRule(localctx, 198, self.RULE_field_bool_default)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1314
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
        self.enterRule(localctx, 200, self.RULE_field_image)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1316
            self.filer_image_type()
            self.state = 1321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1317
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1318
                self.field_image_sizes()
                self.state = 1319
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

        def COL_FIELD_TYPE_FILER_IMAGE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, 0)

        def COL_FIELD_TYPE_FILER_IMAGE_FOLDER(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, 0)

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
        self.enterRule(localctx, 202, self.RULE_filer_image_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1323
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.COL_FIELD_TYPE_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER))) != 0)):
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
        self.enterRule(localctx, 204, self.RULE_field_image_sizes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1325
            self.field_image_size()
            self.state = 1330
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 1326
                self.match(ZmeiLangParser.COMA)
                self.state = 1327
                self.field_image_size()
                self.state = 1332
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
        self.enterRule(localctx, 206, self.RULE_field_image_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1333
            self.field_image_size_name()
            self.state = 1334
            self.field_image_size_dimensions()
            self.state = 1335
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
        self.enterRule(localctx, 208, self.RULE_field_image_size_dimensions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1337
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

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


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
        self.enterRule(localctx, 210, self.RULE_field_image_size_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1339
            self.id_or_kw()
            self.state = 1340
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
        self.enterRule(localctx, 212, self.RULE_field_image_filters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1345
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.PIPE:
                self.state = 1342
                self.field_image_filter()
                self.state = 1347
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

        def PIPE(self):
            return self.getToken(ZmeiLangParser.PIPE, 0)

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


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
        self.enterRule(localctx, 214, self.RULE_field_image_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1348
            self.match(ZmeiLangParser.PIPE)
            self.state = 1349
            self.id_or_kw()
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


        def field_relation_cascade_marker(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_relation_cascade_markerContext,0)


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
        self.enterRule(localctx, 216, self.RULE_field_relation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1351
            self.field_relation_type()
            self.state = 1352
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1354
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.EXCLAM or _la==ZmeiLangParser.APPROX:
                self.state = 1353
                self.field_relation_cascade_marker()


            self.state = 1358
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.HASH]:
                self.state = 1356
                self.field_relation_target_ref()
                pass
            elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS]:
                self.state = 1357
                self.field_relation_target_class()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 1361
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DASH:
                self.state = 1360
                self.field_relation_related_name()


            self.state = 1363
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
        self.enterRule(localctx, 218, self.RULE_field_relation_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1365
            _la = self._input.LA(1)
            if not(((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & ((1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 67)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 67)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 67)))) != 0)):
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


    class Field_relation_cascade_markerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def APPROX(self):
            return self.getToken(ZmeiLangParser.APPROX, 0)

        def EXCLAM(self):
            return self.getToken(ZmeiLangParser.EXCLAM, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_relation_cascade_marker

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_relation_cascade_marker" ):
                listener.enterField_relation_cascade_marker(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_relation_cascade_marker" ):
                listener.exitField_relation_cascade_marker(self)




    def field_relation_cascade_marker(self):

        localctx = ZmeiLangParser.Field_relation_cascade_markerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 220, self.RULE_field_relation_cascade_marker)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1367
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.EXCLAM or _la==ZmeiLangParser.APPROX):
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

        def model_ref(self):
            return self.getTypedRuleContext(ZmeiLangParser.Model_refContext,0)


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
        self.enterRule(localctx, 222, self.RULE_field_relation_target_ref)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1369
            self.model_ref()
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

        def classname(self):
            return self.getTypedRuleContext(ZmeiLangParser.ClassnameContext,0)


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
        self.enterRule(localctx, 224, self.RULE_field_relation_target_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1371
            self.classname()
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

        def DASH(self):
            return self.getToken(ZmeiLangParser.DASH, 0)

        def GT(self):
            return self.getToken(ZmeiLangParser.GT, 0)

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


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
        self.enterRule(localctx, 226, self.RULE_field_relation_related_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1373
            self.match(ZmeiLangParser.DASH)
            self.state = 1374
            self.match(ZmeiLangParser.GT)
            self.state = 1375
            self.id_or_kw()
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


        def an_api(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_apiContext,0)


        def an_rest(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_restContext,0)


        def an_order(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_orderContext,0)


        def an_clean(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_cleanContext,0)


        def an_pre_delete(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_pre_deleteContext,0)


        def an_tree(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_treeContext,0)


        def an_mixin(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_mixinContext,0)


        def an_date_tree(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_date_treeContext,0)


        def an_m2m_changed(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_m2m_changedContext,0)


        def an_post_save(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_post_saveContext,0)


        def an_pre_save(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_pre_saveContext,0)


        def an_post_delete(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_post_deleteContext,0)


        def an_sortable(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_sortableContext,0)


        def NL(self):
            return self.getToken(ZmeiLangParser.NL, 0)

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
        self.enterRule(localctx, 228, self.RULE_model_annotation)
        try:
            self.state = 1392
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.AN_ADMIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1377
                self.an_admin()
                pass
            elif token in [ZmeiLangParser.AN_API]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1378
                self.an_api()
                pass
            elif token in [ZmeiLangParser.AN_REST]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1379
                self.an_rest()
                pass
            elif token in [ZmeiLangParser.AN_ORDER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1380
                self.an_order()
                pass
            elif token in [ZmeiLangParser.AN_CLEAN]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1381
                self.an_clean()
                pass
            elif token in [ZmeiLangParser.AN_PRE_DELETE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 1382
                self.an_pre_delete()
                pass
            elif token in [ZmeiLangParser.AN_TREE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 1383
                self.an_tree()
                pass
            elif token in [ZmeiLangParser.AN_MIXIN]:
                self.enterOuterAlt(localctx, 8)
                self.state = 1384
                self.an_mixin()
                pass
            elif token in [ZmeiLangParser.AN_DATE_TREE]:
                self.enterOuterAlt(localctx, 9)
                self.state = 1385
                self.an_date_tree()
                pass
            elif token in [ZmeiLangParser.AN_M2M_CHANGED]:
                self.enterOuterAlt(localctx, 10)
                self.state = 1386
                self.an_m2m_changed()
                pass
            elif token in [ZmeiLangParser.AN_POST_SAVE]:
                self.enterOuterAlt(localctx, 11)
                self.state = 1387
                self.an_post_save()
                pass
            elif token in [ZmeiLangParser.AN_PRE_SAVE]:
                self.enterOuterAlt(localctx, 12)
                self.state = 1388
                self.an_pre_save()
                pass
            elif token in [ZmeiLangParser.AN_POST_DELETE]:
                self.enterOuterAlt(localctx, 13)
                self.state = 1389
                self.an_post_delete()
                pass
            elif token in [ZmeiLangParser.AN_SORTABLE]:
                self.enterOuterAlt(localctx, 14)
                self.state = 1390
                self.an_sortable()
                pass
            elif token in [ZmeiLangParser.NL]:
                self.enterOuterAlt(localctx, 15)
                self.state = 1391
                self.match(ZmeiLangParser.NL)
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


        def an_admin_tabs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_admin_tabsContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_admin_tabsContext,i)


        def an_admin_inlines(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_admin_inlinesContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_admin_inlinesContext,i)


        def an_admin_css(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_admin_cssContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_admin_cssContext,i)


        def an_admin_js(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_admin_jsContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_admin_jsContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

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
        self.enterRule(localctx, 230, self.RULE_an_admin)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1394
            self.match(ZmeiLangParser.AN_ADMIN)
            self.state = 1420
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1395
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1410
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,122,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 1408
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [ZmeiLangParser.KW_LIST]:
                            self.state = 1396
                            self.an_admin_list()
                            pass
                        elif token in [ZmeiLangParser.KW_READ_ONLY]:
                            self.state = 1397
                            self.an_admin_read_only()
                            pass
                        elif token in [ZmeiLangParser.KW_LIST_EDITABLE]:
                            self.state = 1398
                            self.an_admin_list_editable()
                            pass
                        elif token in [ZmeiLangParser.KW_LIST_FILTER]:
                            self.state = 1399
                            self.an_admin_list_filter()
                            pass
                        elif token in [ZmeiLangParser.KW_LIST_SEARCH]:
                            self.state = 1400
                            self.an_admin_list_search()
                            pass
                        elif token in [ZmeiLangParser.KW_FIELDS]:
                            self.state = 1401
                            self.an_admin_fields()
                            pass
                        elif token in [ZmeiLangParser.KW_TABS]:
                            self.state = 1402
                            self.an_admin_tabs()
                            pass
                        elif token in [ZmeiLangParser.KW_INLINE]:
                            self.state = 1403
                            self.an_admin_inlines()
                            pass
                        elif token in [ZmeiLangParser.KW_CSS]:
                            self.state = 1404
                            self.an_admin_css()
                            pass
                        elif token in [ZmeiLangParser.KW_JS]:
                            self.state = 1405
                            self.an_admin_js()
                            pass
                        elif token in [ZmeiLangParser.NL]:
                            self.state = 1406
                            self.match(ZmeiLangParser.NL)
                            pass
                        elif token in [ZmeiLangParser.COMA]:
                            self.state = 1407
                            self.match(ZmeiLangParser.COMA)
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 1412
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,122,self._ctx)

                self.state = 1416
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZmeiLangParser.NL:
                    self.state = 1413
                    self.match(ZmeiLangParser.NL)
                    self.state = 1418
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 1419
                self.match(ZmeiLangParser.BRACE_CLOSE)


            self.state = 1425
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,125,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1422
                    self.match(ZmeiLangParser.NL) 
                self.state = 1427
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,125,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_admin_jsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_JS(self):
            return self.getToken(ZmeiLangParser.KW_JS, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_admin_js_file_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_admin_js_file_nameContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_admin_js_file_nameContext,i)


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
            return ZmeiLangParser.RULE_an_admin_js

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_admin_js" ):
                listener.enterAn_admin_js(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_admin_js" ):
                listener.exitAn_admin_js(self)




    def an_admin_js(self):

        localctx = ZmeiLangParser.An_admin_jsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 232, self.RULE_an_admin_js)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1428
            self.match(ZmeiLangParser.KW_JS)
            self.state = 1429
            self.match(ZmeiLangParser.COLON)
            self.state = 1433
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 1430
                self.match(ZmeiLangParser.NL)
                self.state = 1435
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1436
            self.an_admin_js_file_name()
            self.state = 1447
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,128,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1437
                    self.match(ZmeiLangParser.COMA)
                    self.state = 1441
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==ZmeiLangParser.NL:
                        self.state = 1438
                        self.match(ZmeiLangParser.NL)
                        self.state = 1443
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 1444
                    self.an_admin_js_file_name() 
                self.state = 1449
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,128,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_admin_cssContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_CSS(self):
            return self.getToken(ZmeiLangParser.KW_CSS, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_admin_css_file_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_admin_css_file_nameContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_admin_css_file_nameContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_admin_css

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_admin_css" ):
                listener.enterAn_admin_css(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_admin_css" ):
                listener.exitAn_admin_css(self)




    def an_admin_css(self):

        localctx = ZmeiLangParser.An_admin_cssContext(self, self._ctx, self.state)
        self.enterRule(localctx, 234, self.RULE_an_admin_css)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1450
            self.match(ZmeiLangParser.KW_CSS)
            self.state = 1451
            self.match(ZmeiLangParser.COLON)
            self.state = 1452
            self.an_admin_css_file_name()
            self.state = 1457
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,129,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1453
                    self.match(ZmeiLangParser.COMA)
                    self.state = 1454
                    self.an_admin_css_file_name() 
                self.state = 1459
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,129,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_admin_css_file_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_admin_css_file_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_admin_css_file_name" ):
                listener.enterAn_admin_css_file_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_admin_css_file_name" ):
                listener.exitAn_admin_css_file_name(self)




    def an_admin_css_file_name(self):

        localctx = ZmeiLangParser.An_admin_css_file_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 236, self.RULE_an_admin_css_file_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1460
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


    class An_admin_js_file_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_admin_js_file_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_admin_js_file_name" ):
                listener.enterAn_admin_js_file_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_admin_js_file_name" ):
                listener.exitAn_admin_js_file_name(self)




    def an_admin_js_file_name(self):

        localctx = ZmeiLangParser.An_admin_js_file_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 238, self.RULE_an_admin_js_file_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1462
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
        self.enterRule(localctx, 240, self.RULE_an_admin_inlines)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1464
            self.match(ZmeiLangParser.KW_INLINE)
            self.state = 1465
            self.match(ZmeiLangParser.COLON)
            self.state = 1466
            self.an_admin_inline()
            self.state = 1471
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,130,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1467
                    self.match(ZmeiLangParser.COMA)
                    self.state = 1468
                    self.an_admin_inline() 
                self.state = 1473
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,130,self._ctx)

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
        self.enterRule(localctx, 242, self.RULE_an_admin_inline)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1474
            self.inline_name()
            self.state = 1487
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1475
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1483
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZmeiLangParser.NL or _la==ZmeiLangParser.COMA or ((((_la - 103)) & ~0x3f) == 0 and ((1 << (_la - 103)) & ((1 << (ZmeiLangParser.KW_TYPE - 103)) | (1 << (ZmeiLangParser.KW_EXTRA - 103)) | (1 << (ZmeiLangParser.KW_FIELDS - 103)))) != 0):
                    self.state = 1481
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [ZmeiLangParser.KW_TYPE]:
                        self.state = 1476
                        self.inline_type()
                        pass
                    elif token in [ZmeiLangParser.KW_EXTRA]:
                        self.state = 1477
                        self.inline_extra()
                        pass
                    elif token in [ZmeiLangParser.KW_FIELDS]:
                        self.state = 1478
                        self.inline_fields()
                        pass
                    elif token in [ZmeiLangParser.NL]:
                        self.state = 1479
                        self.match(ZmeiLangParser.NL)
                        pass
                    elif token in [ZmeiLangParser.COMA]:
                        self.state = 1480
                        self.match(ZmeiLangParser.COMA)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 1485
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 1486
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
        self.enterRule(localctx, 244, self.RULE_inline_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1489
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
        self.enterRule(localctx, 246, self.RULE_inline_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1491
            self.match(ZmeiLangParser.KW_TYPE)
            self.state = 1492
            self.match(ZmeiLangParser.COLON)
            self.state = 1493
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
        self.enterRule(localctx, 248, self.RULE_inline_extra)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1495
            self.match(ZmeiLangParser.KW_EXTRA)
            self.state = 1496
            self.match(ZmeiLangParser.COLON)
            self.state = 1497
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
        self.enterRule(localctx, 250, self.RULE_inline_fields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1499
            self.match(ZmeiLangParser.KW_FIELDS)
            self.state = 1500
            self.match(ZmeiLangParser.COLON)
            self.state = 1501
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
        self.enterRule(localctx, 252, self.RULE_an_admin_tabs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1503
            self.match(ZmeiLangParser.KW_TABS)
            self.state = 1504
            self.match(ZmeiLangParser.COLON)
            self.state = 1505
            self.an_admin_tab()
            self.state = 1510
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,134,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1506
                    self.match(ZmeiLangParser.COMA)
                    self.state = 1507
                    self.an_admin_tab() 
                self.state = 1512
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,134,self._ctx)

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
        self.enterRule(localctx, 254, self.RULE_an_admin_tab)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1513
            self.tab_name()
            self.state = 1515
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.STRING_DQ or _la==ZmeiLangParser.STRING_SQ:
                self.state = 1514
                self.tab_verbose_name()


            self.state = 1517
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1518
            self.field_list_expr()
            self.state = 1519
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
        self.enterRule(localctx, 256, self.RULE_tab_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1521
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
        self.enterRule(localctx, 258, self.RULE_tab_verbose_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1523
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
        self.enterRule(localctx, 260, self.RULE_an_admin_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1525
            self.match(ZmeiLangParser.KW_LIST)
            self.state = 1526
            self.match(ZmeiLangParser.COLON)
            self.state = 1527
            self.field_list_expr()
            self.state = 1531
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,136,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1528
                    self.match(ZmeiLangParser.NL) 
                self.state = 1533
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,136,self._ctx)

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
        self.enterRule(localctx, 262, self.RULE_an_admin_read_only)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1534
            self.match(ZmeiLangParser.KW_READ_ONLY)
            self.state = 1535
            self.match(ZmeiLangParser.COLON)
            self.state = 1536
            self.field_list_expr()
            self.state = 1540
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,137,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1537
                    self.match(ZmeiLangParser.NL) 
                self.state = 1542
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,137,self._ctx)

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
        self.enterRule(localctx, 264, self.RULE_an_admin_list_editable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1543
            self.match(ZmeiLangParser.KW_LIST_EDITABLE)
            self.state = 1544
            self.match(ZmeiLangParser.COLON)
            self.state = 1545
            self.field_list_expr()
            self.state = 1549
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,138,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1546
                    self.match(ZmeiLangParser.NL) 
                self.state = 1551
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,138,self._ctx)

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
        self.enterRule(localctx, 266, self.RULE_an_admin_list_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1552
            self.match(ZmeiLangParser.KW_LIST_FILTER)
            self.state = 1553
            self.match(ZmeiLangParser.COLON)
            self.state = 1554
            self.field_list_expr()
            self.state = 1558
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,139,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1555
                    self.match(ZmeiLangParser.NL) 
                self.state = 1560
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,139,self._ctx)

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
        self.enterRule(localctx, 268, self.RULE_an_admin_list_search)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1561
            self.match(ZmeiLangParser.KW_LIST_SEARCH)
            self.state = 1562
            self.match(ZmeiLangParser.COLON)
            self.state = 1563
            self.field_list_expr()
            self.state = 1567
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,140,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1564
                    self.match(ZmeiLangParser.NL) 
                self.state = 1569
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,140,self._ctx)

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
        self.enterRule(localctx, 270, self.RULE_an_admin_fields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1570
            self.match(ZmeiLangParser.KW_FIELDS)
            self.state = 1571
            self.match(ZmeiLangParser.COLON)
            self.state = 1572
            self.field_list_expr()
            self.state = 1576
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,141,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1573
                    self.match(ZmeiLangParser.NL) 
                self.state = 1578
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,141,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_apiContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_API(self):
            return self.getToken(ZmeiLangParser.AN_API, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def an_api_all(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_api_allContext,0)


        def an_api_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_api_nameContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_api_nameContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_api

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_api" ):
                listener.enterAn_api(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_api" ):
                listener.exitAn_api(self)




    def an_api(self):

        localctx = ZmeiLangParser.An_apiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 272, self.RULE_an_api)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1579
            self.match(ZmeiLangParser.AN_API)
            self.state = 1594
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1580
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1590
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.STAR]:
                    self.state = 1581
                    self.an_api_all()
                    pass
                elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS]:
                    self.state = 1582
                    self.an_api_name()
                    self.state = 1587
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==ZmeiLangParser.COMA:
                        self.state = 1583
                        self.match(ZmeiLangParser.COMA)
                        self.state = 1584
                        self.an_api_name()
                        self.state = 1589
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1592
                self.match(ZmeiLangParser.BRACE_CLOSE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_api_allContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(ZmeiLangParser.STAR, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_api_all

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_api_all" ):
                listener.enterAn_api_all(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_api_all" ):
                listener.exitAn_api_all(self)




    def an_api_all(self):

        localctx = ZmeiLangParser.An_api_allContext(self, self._ctx, self.state)
        self.enterRule(localctx, 274, self.RULE_an_api_all)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1596
            self.match(ZmeiLangParser.STAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_api_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_api_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_api_name" ):
                listener.enterAn_api_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_api_name" ):
                listener.exitAn_api_name(self)




    def an_api_name(self):

        localctx = ZmeiLangParser.An_api_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 276, self.RULE_an_api_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1598
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_restContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_REST(self):
            return self.getToken(ZmeiLangParser.AN_REST, 0)

        def DOT(self):
            return self.getToken(ZmeiLangParser.DOT, 0)

        def an_rest_descriptor(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_rest_descriptorContext,0)


        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_rest_config(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_rest_configContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest" ):
                listener.enterAn_rest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest" ):
                listener.exitAn_rest(self)




    def an_rest(self):

        localctx = ZmeiLangParser.An_restContext(self, self._ctx, self.state)
        self.enterRule(localctx, 278, self.RULE_an_rest)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1600
            self.match(ZmeiLangParser.AN_REST)
            self.state = 1603
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 1601
                self.match(ZmeiLangParser.DOT)
                self.state = 1602
                self.an_rest_descriptor()


            self.state = 1609
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1605
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1606
                self.an_rest_config()
                self.state = 1607
                self.match(ZmeiLangParser.BRACE_CLOSE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_configContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_rest_main_part(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_rest_main_partContext,0)


        def an_rest_inline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_rest_inlineContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_rest_inlineContext,i)


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
            return ZmeiLangParser.RULE_an_rest_config

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_config" ):
                listener.enterAn_rest_config(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_config" ):
                listener.exitAn_rest_config(self)




    def an_rest_config(self):

        localctx = ZmeiLangParser.An_rest_configContext(self, self._ctx, self.state)
        self.enterRule(localctx, 280, self.RULE_an_rest_config)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1611
            self.an_rest_main_part()
            self.state = 1617
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL or _la==ZmeiLangParser.COMA or _la==ZmeiLangParser.KW_INLINE:
                self.state = 1615
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.KW_INLINE]:
                    self.state = 1612
                    self.an_rest_inline()
                    pass
                elif token in [ZmeiLangParser.NL]:
                    self.state = 1613
                    self.match(ZmeiLangParser.NL)
                    pass
                elif token in [ZmeiLangParser.COMA]:
                    self.state = 1614
                    self.match(ZmeiLangParser.COMA)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1619
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_main_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_rest_fields(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_rest_fieldsContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_rest_fieldsContext,i)


        def an_rest_i18n(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_rest_i18nContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_rest_i18nContext,i)


        def an_rest_auth(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_rest_authContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_rest_authContext,i)


        def an_rest_query(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_rest_queryContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_rest_queryContext,i)


        def an_rest_on_create(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_rest_on_createContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_rest_on_createContext,i)


        def an_rest_filter_in(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_rest_filter_inContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_rest_filter_inContext,i)


        def an_rest_filter_out(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_rest_filter_outContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_rest_filter_outContext,i)


        def an_rest_read_only(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_rest_read_onlyContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_rest_read_onlyContext,i)


        def an_rest_user_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_rest_user_fieldContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_rest_user_fieldContext,i)


        def an_rest_annotate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_rest_annotateContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_rest_annotateContext,i)


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
            return ZmeiLangParser.RULE_an_rest_main_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_main_part" ):
                listener.enterAn_rest_main_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_main_part" ):
                listener.exitAn_rest_main_part(self)




    def an_rest_main_part(self):

        localctx = ZmeiLangParser.An_rest_main_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 282, self.RULE_an_rest_main_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1634
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,150,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1632
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [ZmeiLangParser.KW_FIELDS]:
                        self.state = 1620
                        self.an_rest_fields()
                        pass
                    elif token in [ZmeiLangParser.KW_I18N]:
                        self.state = 1621
                        self.an_rest_i18n()
                        pass
                    elif token in [ZmeiLangParser.KW_AUTH]:
                        self.state = 1622
                        self.an_rest_auth()
                        pass
                    elif token in [ZmeiLangParser.KW_QUERY]:
                        self.state = 1623
                        self.an_rest_query()
                        pass
                    elif token in [ZmeiLangParser.KW_ON_CREATE]:
                        self.state = 1624
                        self.an_rest_on_create()
                        pass
                    elif token in [ZmeiLangParser.KW_FILTER_IN]:
                        self.state = 1625
                        self.an_rest_filter_in()
                        pass
                    elif token in [ZmeiLangParser.KW_FILTER_OUT]:
                        self.state = 1626
                        self.an_rest_filter_out()
                        pass
                    elif token in [ZmeiLangParser.KW_READ_ONLY]:
                        self.state = 1627
                        self.an_rest_read_only()
                        pass
                    elif token in [ZmeiLangParser.KW_USER_FIELD]:
                        self.state = 1628
                        self.an_rest_user_field()
                        pass
                    elif token in [ZmeiLangParser.KW_ANNOTATE]:
                        self.state = 1629
                        self.an_rest_annotate()
                        pass
                    elif token in [ZmeiLangParser.NL]:
                        self.state = 1630
                        self.match(ZmeiLangParser.NL)
                        pass
                    elif token in [ZmeiLangParser.COMA]:
                        self.state = 1631
                        self.match(ZmeiLangParser.COMA)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 1636
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,150,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_descriptorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_descriptor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_descriptor" ):
                listener.enterAn_rest_descriptor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_descriptor" ):
                listener.exitAn_rest_descriptor(self)




    def an_rest_descriptor(self):

        localctx = ZmeiLangParser.An_rest_descriptorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 284, self.RULE_an_rest_descriptor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1637
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_i18nContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_I18N(self):
            return self.getToken(ZmeiLangParser.KW_I18N, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def BOOL(self):
            return self.getToken(ZmeiLangParser.BOOL, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_i18n

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_i18n" ):
                listener.enterAn_rest_i18n(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_i18n" ):
                listener.exitAn_rest_i18n(self)




    def an_rest_i18n(self):

        localctx = ZmeiLangParser.An_rest_i18nContext(self, self._ctx, self.state)
        self.enterRule(localctx, 286, self.RULE_an_rest_i18n)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1639
            self.match(ZmeiLangParser.KW_I18N)
            self.state = 1640
            self.match(ZmeiLangParser.COLON)
            self.state = 1641
            self.match(ZmeiLangParser.BOOL)
            self.state = 1645
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,151,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1642
                    self.match(ZmeiLangParser.NL) 
                self.state = 1647
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,151,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_queryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_QUERY(self):
            return self.getToken(ZmeiLangParser.KW_QUERY, 0)

        def python_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Python_codeContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_query" ):
                listener.enterAn_rest_query(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_query" ):
                listener.exitAn_rest_query(self)




    def an_rest_query(self):

        localctx = ZmeiLangParser.An_rest_queryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 288, self.RULE_an_rest_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1648
            self.match(ZmeiLangParser.KW_QUERY)
            self.state = 1649
            self.python_code()
            self.state = 1653
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,152,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1650
                    self.match(ZmeiLangParser.NL) 
                self.state = 1655
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,152,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_on_createContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_ON_CREATE(self):
            return self.getToken(ZmeiLangParser.KW_ON_CREATE, 0)

        def python_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Python_codeContext,0)


        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_on_create

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_on_create" ):
                listener.enterAn_rest_on_create(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_on_create" ):
                listener.exitAn_rest_on_create(self)




    def an_rest_on_create(self):

        localctx = ZmeiLangParser.An_rest_on_createContext(self, self._ctx, self.state)
        self.enterRule(localctx, 290, self.RULE_an_rest_on_create)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1656
            self.match(ZmeiLangParser.KW_ON_CREATE)
            self.state = 1658
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COLON:
                self.state = 1657
                self.match(ZmeiLangParser.COLON)


            self.state = 1660
            self.python_code()
            self.state = 1664
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,154,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1661
                    self.match(ZmeiLangParser.NL) 
                self.state = 1666
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,154,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_filter_inContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FILTER_IN(self):
            return self.getToken(ZmeiLangParser.KW_FILTER_IN, 0)

        def python_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Python_codeContext,0)


        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_filter_in

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_filter_in" ):
                listener.enterAn_rest_filter_in(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_filter_in" ):
                listener.exitAn_rest_filter_in(self)




    def an_rest_filter_in(self):

        localctx = ZmeiLangParser.An_rest_filter_inContext(self, self._ctx, self.state)
        self.enterRule(localctx, 292, self.RULE_an_rest_filter_in)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1667
            self.match(ZmeiLangParser.KW_FILTER_IN)
            self.state = 1669
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COLON:
                self.state = 1668
                self.match(ZmeiLangParser.COLON)


            self.state = 1671
            self.python_code()
            self.state = 1675
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,156,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1672
                    self.match(ZmeiLangParser.NL) 
                self.state = 1677
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,156,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_filter_outContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FILTER_OUT(self):
            return self.getToken(ZmeiLangParser.KW_FILTER_OUT, 0)

        def python_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Python_codeContext,0)


        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_filter_out

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_filter_out" ):
                listener.enterAn_rest_filter_out(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_filter_out" ):
                listener.exitAn_rest_filter_out(self)




    def an_rest_filter_out(self):

        localctx = ZmeiLangParser.An_rest_filter_outContext(self, self._ctx, self.state)
        self.enterRule(localctx, 294, self.RULE_an_rest_filter_out)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1678
            self.match(ZmeiLangParser.KW_FILTER_OUT)
            self.state = 1680
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COLON:
                self.state = 1679
                self.match(ZmeiLangParser.COLON)


            self.state = 1682
            self.python_code()
            self.state = 1686
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,158,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1683
                    self.match(ZmeiLangParser.NL) 
                self.state = 1688
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,158,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_read_onlyContext(ParserRuleContext):

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
            return ZmeiLangParser.RULE_an_rest_read_only

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_read_only" ):
                listener.enterAn_rest_read_only(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_read_only" ):
                listener.exitAn_rest_read_only(self)




    def an_rest_read_only(self):

        localctx = ZmeiLangParser.An_rest_read_onlyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 296, self.RULE_an_rest_read_only)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1689
            self.match(ZmeiLangParser.KW_READ_ONLY)
            self.state = 1690
            self.match(ZmeiLangParser.COLON)
            self.state = 1691
            self.field_list_expr()
            self.state = 1695
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,159,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1692
                    self.match(ZmeiLangParser.NL) 
                self.state = 1697
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,159,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_user_fieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_USER_FIELD(self):
            return self.getToken(ZmeiLangParser.KW_USER_FIELD, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_user_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_user_field" ):
                listener.enterAn_rest_user_field(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_user_field" ):
                listener.exitAn_rest_user_field(self)




    def an_rest_user_field(self):

        localctx = ZmeiLangParser.An_rest_user_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 298, self.RULE_an_rest_user_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1698
            self.match(ZmeiLangParser.KW_USER_FIELD)
            self.state = 1699
            self.match(ZmeiLangParser.COLON)
            self.state = 1700
            self.id_or_kw()
            self.state = 1704
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,160,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1701
                    self.match(ZmeiLangParser.NL) 
                self.state = 1706
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,160,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_fieldsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FIELDS(self):
            return self.getToken(ZmeiLangParser.KW_FIELDS, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def field_list_expr(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_list_exprContext,0)


        def an_rest_fields_write_mode(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_rest_fields_write_modeContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_fields

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_fields" ):
                listener.enterAn_rest_fields(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_fields" ):
                listener.exitAn_rest_fields(self)




    def an_rest_fields(self):

        localctx = ZmeiLangParser.An_rest_fieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 300, self.RULE_an_rest_fields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1707
            self.match(ZmeiLangParser.KW_FIELDS)
            self.state = 1708
            self.match(ZmeiLangParser.COLON)
            self.state = 1709
            self.field_list_expr()
            self.state = 1711
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.SQ_BRACE_OPEN:
                self.state = 1710
                self.an_rest_fields_write_mode()


            self.state = 1716
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,162,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1713
                    self.match(ZmeiLangParser.NL) 
                self.state = 1718
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,162,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_fields_write_modeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def write_mode_expr(self):
            return self.getTypedRuleContext(ZmeiLangParser.Write_mode_exprContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_fields_write_mode

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_fields_write_mode" ):
                listener.enterAn_rest_fields_write_mode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_fields_write_mode" ):
                listener.exitAn_rest_fields_write_mode(self)




    def an_rest_fields_write_mode(self):

        localctx = ZmeiLangParser.An_rest_fields_write_modeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 302, self.RULE_an_rest_fields_write_mode)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1719
            self.write_mode_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_authContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_AUTH(self):
            return self.getToken(ZmeiLangParser.KW_AUTH, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_rest_auth_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_rest_auth_typeContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_rest_auth_typeContext,i)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_auth

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_auth" ):
                listener.enterAn_rest_auth(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_auth" ):
                listener.exitAn_rest_auth(self)




    def an_rest_auth(self):

        localctx = ZmeiLangParser.An_rest_authContext(self, self._ctx, self.state)
        self.enterRule(localctx, 304, self.RULE_an_rest_auth)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1721
            self.match(ZmeiLangParser.KW_AUTH)
            self.state = 1722
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1723
            self.an_rest_auth_type()
            self.state = 1728
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 1724
                self.match(ZmeiLangParser.COMA)
                self.state = 1725
                self.an_rest_auth_type()
                self.state = 1730
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1731
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_auth_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_AUTH_TYPE(self):
            return self.getToken(ZmeiLangParser.KW_AUTH_TYPE, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_rest_auth_token_model(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_rest_auth_token_modelContext,0)


        def an_rest_auth_token_class(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_rest_auth_token_classContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_auth_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_auth_type" ):
                listener.enterAn_rest_auth_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_auth_type" ):
                listener.exitAn_rest_auth_type(self)




    def an_rest_auth_type(self):

        localctx = ZmeiLangParser.An_rest_auth_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 306, self.RULE_an_rest_auth_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1733
            self.match(ZmeiLangParser.KW_AUTH_TYPE)
            self.state = 1737
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.COLON]:
                self.state = 1734
                self.match(ZmeiLangParser.COLON)
                self.state = 1735
                self.an_rest_auth_token_model()
                pass
            elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS]:
                self.state = 1736
                self.an_rest_auth_token_class()
                pass
            elif token in [ZmeiLangParser.BRACE_CLOSE, ZmeiLangParser.COMA]:
                pass
            else:
                pass
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_auth_token_modelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def model_ref(self):
            return self.getTypedRuleContext(ZmeiLangParser.Model_refContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_auth_token_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_auth_token_model" ):
                listener.enterAn_rest_auth_token_model(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_auth_token_model" ):
                listener.exitAn_rest_auth_token_model(self)




    def an_rest_auth_token_model(self):

        localctx = ZmeiLangParser.An_rest_auth_token_modelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 308, self.RULE_an_rest_auth_token_model)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1739
            self.model_ref()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_auth_token_classContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classname(self):
            return self.getTypedRuleContext(ZmeiLangParser.ClassnameContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_auth_token_class

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_auth_token_class" ):
                listener.enterAn_rest_auth_token_class(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_auth_token_class" ):
                listener.exitAn_rest_auth_token_class(self)




    def an_rest_auth_token_class(self):

        localctx = ZmeiLangParser.An_rest_auth_token_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 310, self.RULE_an_rest_auth_token_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1741
            self.classname()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_annotateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_ANNOTATE(self):
            return self.getToken(ZmeiLangParser.KW_ANNOTATE, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_rest_annotate_count(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_rest_annotate_countContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_annotate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_annotate" ):
                listener.enterAn_rest_annotate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_annotate" ):
                listener.exitAn_rest_annotate(self)




    def an_rest_annotate(self):

        localctx = ZmeiLangParser.An_rest_annotateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 312, self.RULE_an_rest_annotate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1743
            self.match(ZmeiLangParser.KW_ANNOTATE)
            self.state = 1744
            self.match(ZmeiLangParser.COLON)
            self.state = 1745
            self.an_rest_annotate_count()
            self.state = 1749
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,165,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1746
                    self.match(ZmeiLangParser.NL) 
                self.state = 1751
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,165,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_annotate_countContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_COUNT(self):
            return self.getToken(ZmeiLangParser.KW_COUNT, 0)

        def an_rest_annotate_count_field(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_rest_annotate_count_fieldContext,0)


        def KW_AS(self):
            return self.getToken(ZmeiLangParser.KW_AS, 0)

        def an_rest_annotate_count_alias(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_rest_annotate_count_aliasContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_annotate_count

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_annotate_count" ):
                listener.enterAn_rest_annotate_count(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_annotate_count" ):
                listener.exitAn_rest_annotate_count(self)




    def an_rest_annotate_count(self):

        localctx = ZmeiLangParser.An_rest_annotate_countContext(self, self._ctx, self.state)
        self.enterRule(localctx, 314, self.RULE_an_rest_annotate_count)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1752
            self.match(ZmeiLangParser.KW_COUNT)
            self.state = 1753
            self.an_rest_annotate_count_field()
            self.state = 1756
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.KW_AS:
                self.state = 1754
                self.match(ZmeiLangParser.KW_AS)
                self.state = 1755
                self.an_rest_annotate_count_alias()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_annotate_count_fieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_annotate_count_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_annotate_count_field" ):
                listener.enterAn_rest_annotate_count_field(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_annotate_count_field" ):
                listener.exitAn_rest_annotate_count_field(self)




    def an_rest_annotate_count_field(self):

        localctx = ZmeiLangParser.An_rest_annotate_count_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 316, self.RULE_an_rest_annotate_count_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1758
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_annotate_count_aliasContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_annotate_count_alias

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_annotate_count_alias" ):
                listener.enterAn_rest_annotate_count_alias(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_annotate_count_alias" ):
                listener.exitAn_rest_annotate_count_alias(self)




    def an_rest_annotate_count_alias(self):

        localctx = ZmeiLangParser.An_rest_annotate_count_aliasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 318, self.RULE_an_rest_annotate_count_alias)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1760
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_inlineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_INLINE(self):
            return self.getToken(ZmeiLangParser.KW_INLINE, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_rest_inline_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_rest_inline_declContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_rest_inline_declContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_inline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_inline" ):
                listener.enterAn_rest_inline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_inline" ):
                listener.exitAn_rest_inline(self)




    def an_rest_inline(self):

        localctx = ZmeiLangParser.An_rest_inlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 320, self.RULE_an_rest_inline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1762
            self.match(ZmeiLangParser.KW_INLINE)
            self.state = 1763
            self.match(ZmeiLangParser.COLON)
            self.state = 1767 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 1767
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS]:
                        self.state = 1764
                        self.an_rest_inline_decl()
                        pass
                    elif token in [ZmeiLangParser.COMA]:
                        self.state = 1765
                        self.match(ZmeiLangParser.COMA)
                        pass
                    elif token in [ZmeiLangParser.NL]:
                        self.state = 1766
                        self.match(ZmeiLangParser.NL)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 1769 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,168,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_inline_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_rest_inline_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_rest_inline_nameContext,0)


        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_rest_config(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_rest_configContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_inline_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_inline_decl" ):
                listener.enterAn_rest_inline_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_inline_decl" ):
                listener.exitAn_rest_inline_decl(self)




    def an_rest_inline_decl(self):

        localctx = ZmeiLangParser.An_rest_inline_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 322, self.RULE_an_rest_inline_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1771
            self.an_rest_inline_name()
            self.state = 1772
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1773
            self.an_rest_config()
            self.state = 1774
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_inline_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_inline_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_inline_name" ):
                listener.enterAn_rest_inline_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_inline_name" ):
                listener.exitAn_rest_inline_name(self)




    def an_rest_inline_name(self):

        localctx = ZmeiLangParser.An_rest_inline_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 324, self.RULE_an_rest_inline_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1776
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_orderContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_ORDER(self):
            return self.getToken(ZmeiLangParser.AN_ORDER, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_order_fields(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_order_fieldsContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_order

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_order" ):
                listener.enterAn_order(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_order" ):
                listener.exitAn_order(self)




    def an_order(self):

        localctx = ZmeiLangParser.An_orderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 326, self.RULE_an_order)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1778
            self.match(ZmeiLangParser.AN_ORDER)
            self.state = 1779
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1780
            self.an_order_fields()
            self.state = 1781
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_order_fieldsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Id_or_kwContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_order_fields

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_order_fields" ):
                listener.enterAn_order_fields(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_order_fields" ):
                listener.exitAn_order_fields(self)




    def an_order_fields(self):

        localctx = ZmeiLangParser.An_order_fieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 328, self.RULE_an_order_fields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1783
            self.id_or_kw()
            self.state = 1788
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 1784
                self.match(ZmeiLangParser.COMA)
                self.state = 1785
                self.id_or_kw()
                self.state = 1790
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_cleanContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_CLEAN(self):
            return self.getToken(ZmeiLangParser.AN_CLEAN, 0)

        def python_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Python_codeContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_clean

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_clean" ):
                listener.enterAn_clean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_clean" ):
                listener.exitAn_clean(self)




    def an_clean(self):

        localctx = ZmeiLangParser.An_cleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 330, self.RULE_an_clean)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1791
            self.match(ZmeiLangParser.AN_CLEAN)
            self.state = 1792
            self.python_code()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_pre_deleteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_PRE_DELETE(self):
            return self.getToken(ZmeiLangParser.AN_PRE_DELETE, 0)

        def python_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Python_codeContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_pre_delete

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_pre_delete" ):
                listener.enterAn_pre_delete(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_pre_delete" ):
                listener.exitAn_pre_delete(self)




    def an_pre_delete(self):

        localctx = ZmeiLangParser.An_pre_deleteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 332, self.RULE_an_pre_delete)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1794
            self.match(ZmeiLangParser.AN_PRE_DELETE)
            self.state = 1795
            self.python_code()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_treeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_TREE(self):
            return self.getToken(ZmeiLangParser.AN_TREE, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_tree_poly(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_tree_polyContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_tree

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_tree" ):
                listener.enterAn_tree(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_tree" ):
                listener.exitAn_tree(self)




    def an_tree(self):

        localctx = ZmeiLangParser.An_treeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 334, self.RULE_an_tree)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1797
            self.match(ZmeiLangParser.AN_TREE)
            self.state = 1802
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1798
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1799
                self.an_tree_poly()
                self.state = 1800
                self.match(ZmeiLangParser.BRACE_CLOSE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_tree_polyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_POLY_LIST(self):
            return self.getToken(ZmeiLangParser.KW_POLY_LIST, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_tree_poly

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_tree_poly" ):
                listener.enterAn_tree_poly(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_tree_poly" ):
                listener.exitAn_tree_poly(self)




    def an_tree_poly(self):

        localctx = ZmeiLangParser.An_tree_polyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 336, self.RULE_an_tree_poly)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1804
            self.match(ZmeiLangParser.KW_POLY_LIST)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_mixinContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_MIXIN(self):
            return self.getToken(ZmeiLangParser.AN_MIXIN, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def classname(self):
            return self.getTypedRuleContext(ZmeiLangParser.ClassnameContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_mixin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_mixin" ):
                listener.enterAn_mixin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_mixin" ):
                listener.exitAn_mixin(self)




    def an_mixin(self):

        localctx = ZmeiLangParser.An_mixinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 338, self.RULE_an_mixin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1806
            self.match(ZmeiLangParser.AN_MIXIN)

            self.state = 1807
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1808
            self.classname()
            self.state = 1809
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_date_treeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_DATE_TREE(self):
            return self.getToken(ZmeiLangParser.AN_DATE_TREE, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_date_tree_field(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_date_tree_fieldContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_date_tree

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_date_tree" ):
                listener.enterAn_date_tree(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_date_tree" ):
                listener.exitAn_date_tree(self)




    def an_date_tree(self):

        localctx = ZmeiLangParser.An_date_treeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 340, self.RULE_an_date_tree)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1811
            self.match(ZmeiLangParser.AN_DATE_TREE)

            self.state = 1812
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1813
            self.an_date_tree_field()
            self.state = 1814
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_date_tree_fieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_date_tree_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_date_tree_field" ):
                listener.enterAn_date_tree_field(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_date_tree_field" ):
                listener.exitAn_date_tree_field(self)




    def an_date_tree_field(self):

        localctx = ZmeiLangParser.An_date_tree_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 342, self.RULE_an_date_tree_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1816
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_m2m_changedContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_M2M_CHANGED(self):
            return self.getToken(ZmeiLangParser.AN_M2M_CHANGED, 0)

        def python_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Python_codeContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_m2m_changed

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_m2m_changed" ):
                listener.enterAn_m2m_changed(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_m2m_changed" ):
                listener.exitAn_m2m_changed(self)




    def an_m2m_changed(self):

        localctx = ZmeiLangParser.An_m2m_changedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 344, self.RULE_an_m2m_changed)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1818
            self.match(ZmeiLangParser.AN_M2M_CHANGED)
            self.state = 1819
            self.python_code()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_post_saveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_POST_SAVE(self):
            return self.getToken(ZmeiLangParser.AN_POST_SAVE, 0)

        def python_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Python_codeContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_post_save

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_post_save" ):
                listener.enterAn_post_save(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_post_save" ):
                listener.exitAn_post_save(self)




    def an_post_save(self):

        localctx = ZmeiLangParser.An_post_saveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 346, self.RULE_an_post_save)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1821
            self.match(ZmeiLangParser.AN_POST_SAVE)
            self.state = 1822
            self.python_code()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_pre_saveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_PRE_SAVE(self):
            return self.getToken(ZmeiLangParser.AN_PRE_SAVE, 0)

        def python_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Python_codeContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_pre_save

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_pre_save" ):
                listener.enterAn_pre_save(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_pre_save" ):
                listener.exitAn_pre_save(self)




    def an_pre_save(self):

        localctx = ZmeiLangParser.An_pre_saveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 348, self.RULE_an_pre_save)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1824
            self.match(ZmeiLangParser.AN_PRE_SAVE)
            self.state = 1825
            self.python_code()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_post_deleteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_POST_DELETE(self):
            return self.getToken(ZmeiLangParser.AN_POST_DELETE, 0)

        def python_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Python_codeContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_post_delete

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_post_delete" ):
                listener.enterAn_post_delete(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_post_delete" ):
                listener.exitAn_post_delete(self)




    def an_post_delete(self):

        localctx = ZmeiLangParser.An_post_deleteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 350, self.RULE_an_post_delete)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1827
            self.match(ZmeiLangParser.AN_POST_DELETE)
            self.state = 1828
            self.python_code()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_sortableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_SORTABLE(self):
            return self.getToken(ZmeiLangParser.AN_SORTABLE, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_sortable_field_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_sortable_field_nameContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_sortable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_sortable" ):
                listener.enterAn_sortable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_sortable" ):
                listener.exitAn_sortable(self)




    def an_sortable(self):

        localctx = ZmeiLangParser.An_sortableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 352, self.RULE_an_sortable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1830
            self.match(ZmeiLangParser.AN_SORTABLE)
            self.state = 1831
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1832
            self.an_sortable_field_name()
            self.state = 1833
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_sortable_field_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_sortable_field_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_sortable_field_name" ):
                listener.enterAn_sortable_field_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_sortable_field_name" ):
                listener.exitAn_sortable_field_name(self)




    def an_sortable_field_name(self):

        localctx = ZmeiLangParser.An_sortable_field_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 354, self.RULE_an_sortable_field_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1835
            self.id_or_kw()
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

        def page_header(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_headerContext,0)


        def page_body(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_bodyContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

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
        self.enterRule(localctx, 356, self.RULE_page)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1837
            self.page_header()
            self.state = 1841
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,171,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1838
                    self.match(ZmeiLangParser.NL) 
                self.state = 1843
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,171,self._ctx)

            self.state = 1844
            self.page_body()
            self.state = 1848
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,172,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1845
                    self.match(ZmeiLangParser.NL) 
                self.state = 1850
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,172,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Page_headerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQ_BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.SQ_BRACE_OPEN, 0)

        def page_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_nameContext,0)


        def SQ_BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.SQ_BRACE_CLOSE, 0)

        def page_base(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_baseContext,0)


        def page_alias(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_aliasContext,0)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COLON)
            else:
                return self.getToken(ZmeiLangParser.COLON, i)

        def NL(self):
            return self.getToken(ZmeiLangParser.NL, 0)

        def page_url(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_urlContext,0)


        def page_template(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_templateContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_header" ):
                listener.enterPage_header(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_header" ):
                listener.exitPage_header(self)




    def page_header(self):

        localctx = ZmeiLangParser.Page_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 358, self.RULE_page_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1851
            self.match(ZmeiLangParser.SQ_BRACE_OPEN)
            self.state = 1853
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,173,self._ctx)
            if la_ == 1:
                self.state = 1852
                self.page_base()


            self.state = 1855
            self.page_name()
            self.state = 1857
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.KW_AS:
                self.state = 1856
                self.page_alias()


            self.state = 1867
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COLON:
                self.state = 1859
                self.match(ZmeiLangParser.COLON)
                self.state = 1861
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.DOT) | (1 << ZmeiLangParser.SLASH) | (1 << ZmeiLangParser.DOLLAR))) != 0):
                    self.state = 1860
                    self.page_url()


                self.state = 1865
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.COLON:
                    self.state = 1863
                    self.match(ZmeiLangParser.COLON)
                    self.state = 1864
                    self.page_template()




            self.state = 1869
            self.match(ZmeiLangParser.SQ_BRACE_CLOSE)
            self.state = 1871
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,178,self._ctx)
            if la_ == 1:
                self.state = 1870
                self.match(ZmeiLangParser.NL)


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

        def id_or_kw(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Id_or_kwContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,i)


        def GT(self):
            return self.getToken(ZmeiLangParser.GT, 0)

        def DASH(self):
            return self.getToken(ZmeiLangParser.DASH, 0)

        def APPROX(self):
            return self.getToken(ZmeiLangParser.APPROX, 0)

        def DOT(self):
            return self.getToken(ZmeiLangParser.DOT, 0)

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
        self.enterRule(localctx, 360, self.RULE_page_base)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1876
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,179,self._ctx)
            if la_ == 1:
                self.state = 1873
                self.id_or_kw()
                self.state = 1874
                self.match(ZmeiLangParser.DOT)


            self.state = 1878
            self.id_or_kw()
            self.state = 1879
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.DASH or _la==ZmeiLangParser.APPROX):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 1880
            self.match(ZmeiLangParser.GT)
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
        self.enterRule(localctx, 362, self.RULE_page_alias)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1882
            self.match(ZmeiLangParser.KW_AS)
            self.state = 1883
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
        self.enterRule(localctx, 364, self.RULE_page_alias_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1885
            self.id_or_kw()
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

        def template_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Template_nameContext,0)


        def python_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Python_codeContext,0)


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
        self.enterRule(localctx, 366, self.RULE_page_template)
        try:
            self.state = 1889
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.DIGIT, ZmeiLangParser.UNDERSCORE, ZmeiLangParser.DASH, ZmeiLangParser.DOT, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1887
                self.template_name()
                pass
            elif token in [ZmeiLangParser.ASSIGN, ZmeiLangParser.CODE_BLOCK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1888
                self.python_code()
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


    class Template_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def file_name_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.File_name_partContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.File_name_partContext,i)


        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.SLASH)
            else:
                return self.getToken(ZmeiLangParser.SLASH, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_template_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplate_name" ):
                listener.enterTemplate_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplate_name" ):
                listener.exitTemplate_name(self)




    def template_name(self):

        localctx = ZmeiLangParser.Template_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 368, self.RULE_template_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1891
            self.file_name_part()
            self.state = 1896
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.SLASH:
                self.state = 1892
                self.match(ZmeiLangParser.SLASH)
                self.state = 1893
                self.file_name_part()
                self.state = 1898
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class File_name_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Id_or_kwContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,i)


        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.DIGIT)
            else:
                return self.getToken(ZmeiLangParser.DIGIT, i)

        def DASH(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.DASH)
            else:
                return self.getToken(ZmeiLangParser.DASH, i)

        def UNDERSCORE(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.UNDERSCORE)
            else:
                return self.getToken(ZmeiLangParser.UNDERSCORE, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.DOT)
            else:
                return self.getToken(ZmeiLangParser.DOT, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_file_name_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile_name_part" ):
                listener.enterFile_name_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile_name_part" ):
                listener.exitFile_name_part(self)




    def file_name_part(self):

        localctx = ZmeiLangParser.File_name_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 370, self.RULE_file_name_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1904 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1904
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS]:
                    self.state = 1899
                    self.id_or_kw()
                    pass
                elif token in [ZmeiLangParser.DIGIT]:
                    self.state = 1900
                    self.match(ZmeiLangParser.DIGIT)
                    pass
                elif token in [ZmeiLangParser.DASH]:
                    self.state = 1901
                    self.match(ZmeiLangParser.DASH)
                    pass
                elif token in [ZmeiLangParser.UNDERSCORE]:
                    self.state = 1902
                    self.match(ZmeiLangParser.UNDERSCORE)
                    pass
                elif token in [ZmeiLangParser.DOT]:
                    self.state = 1903
                    self.match(ZmeiLangParser.DOT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1906 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.WRITE_MODE) | (1 << ZmeiLangParser.BOOL) | (1 << ZmeiLangParser.ID) | (1 << ZmeiLangParser.DIGIT) | (1 << ZmeiLangParser.UNDERSCORE) | (1 << ZmeiLangParser.DASH) | (1 << ZmeiLangParser.DOT) | (1 << ZmeiLangParser.KW_FROM) | (1 << ZmeiLangParser.KW_IMPORT) | (1 << ZmeiLangParser.KW_AS) | (1 << ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FLOAT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DECIMAL) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATETIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_TEXT))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 64)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 64)) | (1 << (ZmeiLangParser.KW_THEME - 64)) | (1 << (ZmeiLangParser.KW_INSTALL - 64)) | (1 << (ZmeiLangParser.KW_HEADER - 64)) | (1 << (ZmeiLangParser.KW_SERVICES - 64)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 64)) | (1 << (ZmeiLangParser.KW_CHILD - 64)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 64)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 64)) | (1 << (ZmeiLangParser.KW_PAGE - 64)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 64)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 64)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 64)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 64)) | (1 << (ZmeiLangParser.KW_BLOCK - 64)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 64)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 64)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 64)) | (1 << (ZmeiLangParser.KW_DELETE - 64)) | (1 << (ZmeiLangParser.KW_EDIT - 64)) | (1 << (ZmeiLangParser.KW_CREATE - 64)) | (1 << (ZmeiLangParser.KW_DETAIL - 64)) | (1 << (ZmeiLangParser.KW_SKIP - 64)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 64)) | (1 << (ZmeiLangParser.KW_CSS - 64)) | (1 << (ZmeiLangParser.KW_JS - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_BASIC - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_SESSION - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_TOKEN - 64)) | (1 << (ZmeiLangParser.KW_INLINE - 64)) | (1 << (ZmeiLangParser.KW_TYPE - 64)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 64)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 64)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 64)) | (1 << (ZmeiLangParser.KW_QUERY - 64)) | (1 << (ZmeiLangParser.KW_AUTH - 64)) | (1 << (ZmeiLangParser.KW_COUNT - 64)) | (1 << (ZmeiLangParser.KW_I18N - 64)) | (1 << (ZmeiLangParser.KW_EXTRA - 64)) | (1 << (ZmeiLangParser.KW_TABS - 64)) | (1 << (ZmeiLangParser.KW_LIST - 64)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 64)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 64)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 64)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 64)) | (1 << (ZmeiLangParser.KW_FIELDS - 64)))) != 0)):
                    break

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

        def url_segments(self):
            return self.getTypedRuleContext(ZmeiLangParser.Url_segmentsContext,0)


        def DOT(self):
            return self.getToken(ZmeiLangParser.DOT, 0)

        def DOLLAR(self):
            return self.getToken(ZmeiLangParser.DOLLAR, 0)

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
        self.enterRule(localctx, 372, self.RULE_page_url)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1909
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT or _la==ZmeiLangParser.DOLLAR:
                self.state = 1908
                _la = self._input.LA(1)
                if not(_la==ZmeiLangParser.DOT or _la==ZmeiLangParser.DOLLAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 1911
            self.url_segments()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Url_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Id_or_kwContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,i)


        def DASH(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.DASH)
            else:
                return self.getToken(ZmeiLangParser.DASH, i)

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.DIGIT)
            else:
                return self.getToken(ZmeiLangParser.DIGIT, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_url_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUrl_part" ):
                listener.enterUrl_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUrl_part" ):
                listener.exitUrl_part(self)




    def url_part(self):

        localctx = ZmeiLangParser.Url_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 374, self.RULE_url_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1916 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1916
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS]:
                    self.state = 1913
                    self.id_or_kw()
                    pass
                elif token in [ZmeiLangParser.DASH]:
                    self.state = 1914
                    self.match(ZmeiLangParser.DASH)
                    pass
                elif token in [ZmeiLangParser.DIGIT]:
                    self.state = 1915
                    self.match(ZmeiLangParser.DIGIT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1918 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.WRITE_MODE) | (1 << ZmeiLangParser.BOOL) | (1 << ZmeiLangParser.ID) | (1 << ZmeiLangParser.DIGIT) | (1 << ZmeiLangParser.DASH) | (1 << ZmeiLangParser.KW_FROM) | (1 << ZmeiLangParser.KW_IMPORT) | (1 << ZmeiLangParser.KW_AS) | (1 << ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FLOAT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DECIMAL) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATETIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_TEXT))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 64)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 64)) | (1 << (ZmeiLangParser.KW_THEME - 64)) | (1 << (ZmeiLangParser.KW_INSTALL - 64)) | (1 << (ZmeiLangParser.KW_HEADER - 64)) | (1 << (ZmeiLangParser.KW_SERVICES - 64)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 64)) | (1 << (ZmeiLangParser.KW_CHILD - 64)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 64)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 64)) | (1 << (ZmeiLangParser.KW_PAGE - 64)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 64)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 64)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 64)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 64)) | (1 << (ZmeiLangParser.KW_BLOCK - 64)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 64)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 64)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 64)) | (1 << (ZmeiLangParser.KW_DELETE - 64)) | (1 << (ZmeiLangParser.KW_EDIT - 64)) | (1 << (ZmeiLangParser.KW_CREATE - 64)) | (1 << (ZmeiLangParser.KW_DETAIL - 64)) | (1 << (ZmeiLangParser.KW_SKIP - 64)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 64)) | (1 << (ZmeiLangParser.KW_CSS - 64)) | (1 << (ZmeiLangParser.KW_JS - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_BASIC - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_SESSION - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_TOKEN - 64)) | (1 << (ZmeiLangParser.KW_INLINE - 64)) | (1 << (ZmeiLangParser.KW_TYPE - 64)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 64)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 64)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 64)) | (1 << (ZmeiLangParser.KW_QUERY - 64)) | (1 << (ZmeiLangParser.KW_AUTH - 64)) | (1 << (ZmeiLangParser.KW_COUNT - 64)) | (1 << (ZmeiLangParser.KW_I18N - 64)) | (1 << (ZmeiLangParser.KW_EXTRA - 64)) | (1 << (ZmeiLangParser.KW_TABS - 64)) | (1 << (ZmeiLangParser.KW_LIST - 64)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 64)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 64)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 64)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 64)) | (1 << (ZmeiLangParser.KW_FIELDS - 64)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Url_paramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(ZmeiLangParser.LT, 0)

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def GT(self):
            return self.getToken(ZmeiLangParser.GT, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_url_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUrl_param" ):
                listener.enterUrl_param(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUrl_param" ):
                listener.exitUrl_param(self)




    def url_param(self):

        localctx = ZmeiLangParser.Url_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 376, self.RULE_url_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1920
            self.match(ZmeiLangParser.LT)
            self.state = 1921
            self.id_or_kw()
            self.state = 1922
            self.match(ZmeiLangParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Url_segmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def url_part(self):
            return self.getTypedRuleContext(ZmeiLangParser.Url_partContext,0)


        def url_param(self):
            return self.getTypedRuleContext(ZmeiLangParser.Url_paramContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_url_segment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUrl_segment" ):
                listener.enterUrl_segment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUrl_segment" ):
                listener.exitUrl_segment(self)




    def url_segment(self):

        localctx = ZmeiLangParser.Url_segmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 378, self.RULE_url_segment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1926
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.DIGIT, ZmeiLangParser.DASH, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS]:
                self.state = 1924
                self.url_part()
                pass
            elif token in [ZmeiLangParser.LT]:
                self.state = 1925
                self.url_param()
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


    class Url_segmentsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.SLASH)
            else:
                return self.getToken(ZmeiLangParser.SLASH, i)

        def url_segment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Url_segmentContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Url_segmentContext,i)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_url_segments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUrl_segments" ):
                listener.enterUrl_segments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUrl_segments" ):
                listener.exitUrl_segments(self)




    def url_segments(self):

        localctx = ZmeiLangParser.Url_segmentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 380, self.RULE_url_segments)
        self._la = 0 # Token type
        try:
            self.state = 1938
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,190,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1928
                self.match(ZmeiLangParser.SLASH)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1931 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 1929
                        self.match(ZmeiLangParser.SLASH)
                        self.state = 1930
                        self.url_segment()

                    else:
                        raise NoViableAltException(self)
                    self.state = 1933 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,188,self._ctx)

                self.state = 1936
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.SLASH:
                    self.state = 1935
                    self.match(ZmeiLangParser.SLASH)


                pass


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
        self.enterRule(localctx, 382, self.RULE_page_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1940
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Page_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def page_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Page_fieldContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Page_fieldContext,i)


        def page_function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Page_functionContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Page_functionContext,i)


        def page_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_codeContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def page_annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Page_annotationContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Page_annotationContext,i)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_body" ):
                listener.enterPage_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_body" ):
                listener.exitPage_body(self)




    def page_body(self):

        localctx = ZmeiLangParser.Page_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 384, self.RULE_page_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1945
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,191,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1942
                    self.page_field() 
                self.state = 1947
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,191,self._ctx)

            self.state = 1951
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,192,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1948
                    self.page_function() 
                self.state = 1953
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,192,self._ctx)

            self.state = 1955
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.ASSIGN or _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 1954
                self.page_code()


            self.state = 1960
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,194,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1957
                    self.match(ZmeiLangParser.NL) 
                self.state = 1962
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,194,self._ctx)

            self.state = 1966
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,195,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1963
                    self.page_annotation() 
                self.state = 1968
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,195,self._ctx)

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

        def python_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Python_codeContext,0)


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
        self.enterRule(localctx, 386, self.RULE_page_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1969
            self.python_code()
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
        self.enterRule(localctx, 388, self.RULE_page_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1971
            self.page_field_name()
            self.state = 1972
            self.match(ZmeiLangParser.ASSIGN)
            self.state = 1973
            self.page_field_code()
            self.state = 1980
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.NL]:
                self.state = 1975 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 1974
                        self.match(ZmeiLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 1977 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,196,self._ctx)

                pass
            elif token in [ZmeiLangParser.EOF]:
                self.state = 1979
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
        self.enterRule(localctx, 390, self.RULE_page_field_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1982
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

        def PYTHON_CODE(self):
            return self.getToken(ZmeiLangParser.PYTHON_CODE, 0)

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
        self.enterRule(localctx, 392, self.RULE_page_field_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1984
            self.match(ZmeiLangParser.PYTHON_CODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Page_functionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def page_function_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_function_nameContext,0)


        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def EOF(self):
            return self.getToken(ZmeiLangParser.EOF, 0)

        def page_function_args(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_function_argsContext,0)


        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_function" ):
                listener.enterPage_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_function" ):
                listener.exitPage_function(self)




    def page_function(self):

        localctx = ZmeiLangParser.Page_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 394, self.RULE_page_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1986
            self.page_function_name()
            self.state = 1987
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1989
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.WRITE_MODE) | (1 << ZmeiLangParser.BOOL) | (1 << ZmeiLangParser.ID) | (1 << ZmeiLangParser.KW_FROM) | (1 << ZmeiLangParser.KW_IMPORT) | (1 << ZmeiLangParser.KW_AS) | (1 << ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FLOAT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DECIMAL) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATETIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_TEXT))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 64)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 64)) | (1 << (ZmeiLangParser.KW_THEME - 64)) | (1 << (ZmeiLangParser.KW_INSTALL - 64)) | (1 << (ZmeiLangParser.KW_HEADER - 64)) | (1 << (ZmeiLangParser.KW_SERVICES - 64)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 64)) | (1 << (ZmeiLangParser.KW_CHILD - 64)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 64)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 64)) | (1 << (ZmeiLangParser.KW_PAGE - 64)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 64)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 64)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 64)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 64)) | (1 << (ZmeiLangParser.KW_BLOCK - 64)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 64)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 64)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 64)) | (1 << (ZmeiLangParser.KW_DELETE - 64)) | (1 << (ZmeiLangParser.KW_EDIT - 64)) | (1 << (ZmeiLangParser.KW_CREATE - 64)) | (1 << (ZmeiLangParser.KW_DETAIL - 64)) | (1 << (ZmeiLangParser.KW_SKIP - 64)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 64)) | (1 << (ZmeiLangParser.KW_CSS - 64)) | (1 << (ZmeiLangParser.KW_JS - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_BASIC - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_SESSION - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_TOKEN - 64)) | (1 << (ZmeiLangParser.KW_INLINE - 64)) | (1 << (ZmeiLangParser.KW_TYPE - 64)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 64)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 64)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 64)) | (1 << (ZmeiLangParser.KW_QUERY - 64)) | (1 << (ZmeiLangParser.KW_AUTH - 64)) | (1 << (ZmeiLangParser.KW_COUNT - 64)) | (1 << (ZmeiLangParser.KW_I18N - 64)) | (1 << (ZmeiLangParser.KW_EXTRA - 64)) | (1 << (ZmeiLangParser.KW_TABS - 64)) | (1 << (ZmeiLangParser.KW_LIST - 64)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 64)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 64)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 64)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 64)) | (1 << (ZmeiLangParser.KW_FIELDS - 64)))) != 0):
                self.state = 1988
                self.page_function_args()


            self.state = 1991
            self.match(ZmeiLangParser.BRACE_CLOSE)
            self.state = 1993
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 1992
                self.code_block()


            self.state = 2001
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.NL]:
                self.state = 1996 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 1995
                        self.match(ZmeiLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 1998 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,200,self._ctx)

                pass
            elif token in [ZmeiLangParser.EOF]:
                self.state = 2000
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


    class Page_function_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_function_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_function_name" ):
                listener.enterPage_function_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_function_name" ):
                listener.exitPage_function_name(self)




    def page_function_name(self):

        localctx = ZmeiLangParser.Page_function_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 396, self.RULE_page_function_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2003
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Page_function_argsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Id_or_kwContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_function_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_function_args" ):
                listener.enterPage_function_args(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_function_args" ):
                listener.exitPage_function_args(self)




    def page_function_args(self):

        localctx = ZmeiLangParser.Page_function_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 398, self.RULE_page_function_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2005
            self.id_or_kw()
            self.state = 2010
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 2006
                self.match(ZmeiLangParser.COMA)
                self.state = 2007
                self.id_or_kw()
                self.state = 2012
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Page_annotationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_stream(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_streamContext,0)


        def an_flutter(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_flutterContext,0)


        def an_react(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_reactContext,0)


        def an_html(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_htmlContext,0)


        def an_markdown(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_markdownContext,0)


        def an_crud_delete(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_deleteContext,0)


        def an_post(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_postContext,0)


        def an_auth(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_authContext,0)


        def an_crud_create(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_createContext,0)


        def an_crud_edit(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_editContext,0)


        def an_crud(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crudContext,0)


        def an_crud_list(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_listContext,0)


        def an_menu(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_menuContext,0)


        def an_crud_detail(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_detailContext,0)


        def an_priority_marker(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_priority_markerContext,0)


        def an_get(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_getContext,0)


        def an_error(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_errorContext,0)


        def NL(self):
            return self.getToken(ZmeiLangParser.NL, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_annotation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_annotation" ):
                listener.enterPage_annotation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_annotation" ):
                listener.exitPage_annotation(self)




    def page_annotation(self):

        localctx = ZmeiLangParser.Page_annotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 400, self.RULE_page_annotation)
        try:
            self.state = 2031
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.AN_STREAM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2013
                self.an_stream()
                pass
            elif token in [ZmeiLangParser.AN_FLUTTER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2014
                self.an_flutter()
                pass
            elif token in [ZmeiLangParser.AN_REACT, ZmeiLangParser.AN_REACT_CLIENT, ZmeiLangParser.AN_REACT_SERVER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2015
                self.an_react()
                pass
            elif token in [ZmeiLangParser.AN_HTML]:
                self.enterOuterAlt(localctx, 4)
                self.state = 2016
                self.an_html()
                pass
            elif token in [ZmeiLangParser.AN_MARKDOWN]:
                self.enterOuterAlt(localctx, 5)
                self.state = 2017
                self.an_markdown()
                pass
            elif token in [ZmeiLangParser.AN_CRUD_DELETE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 2018
                self.an_crud_delete()
                pass
            elif token in [ZmeiLangParser.AN_POST]:
                self.enterOuterAlt(localctx, 7)
                self.state = 2019
                self.an_post()
                pass
            elif token in [ZmeiLangParser.AN_AUTH]:
                self.enterOuterAlt(localctx, 8)
                self.state = 2020
                self.an_auth()
                pass
            elif token in [ZmeiLangParser.AN_CRUD_CREATE]:
                self.enterOuterAlt(localctx, 9)
                self.state = 2021
                self.an_crud_create()
                pass
            elif token in [ZmeiLangParser.AN_CRUD_EDIT]:
                self.enterOuterAlt(localctx, 10)
                self.state = 2022
                self.an_crud_edit()
                pass
            elif token in [ZmeiLangParser.AN_CRUD]:
                self.enterOuterAlt(localctx, 11)
                self.state = 2023
                self.an_crud()
                pass
            elif token in [ZmeiLangParser.AN_CRUD_LIST]:
                self.enterOuterAlt(localctx, 12)
                self.state = 2024
                self.an_crud_list()
                pass
            elif token in [ZmeiLangParser.AN_MENU]:
                self.enterOuterAlt(localctx, 13)
                self.state = 2025
                self.an_menu()
                pass
            elif token in [ZmeiLangParser.AN_CRUD_DETAIL]:
                self.enterOuterAlt(localctx, 14)
                self.state = 2026
                self.an_crud_detail()
                pass
            elif token in [ZmeiLangParser.AN_PRIORITY]:
                self.enterOuterAlt(localctx, 15)
                self.state = 2027
                self.an_priority_marker()
                pass
            elif token in [ZmeiLangParser.AN_GET]:
                self.enterOuterAlt(localctx, 16)
                self.state = 2028
                self.an_get()
                pass
            elif token in [ZmeiLangParser.AN_ERROR]:
                self.enterOuterAlt(localctx, 17)
                self.state = 2029
                self.an_error()
                pass
            elif token in [ZmeiLangParser.NL]:
                self.enterOuterAlt(localctx, 18)
                self.state = 2030
                self.match(ZmeiLangParser.NL)
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


    class An_streamContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_STREAM(self):
            return self.getToken(ZmeiLangParser.AN_STREAM, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def an_stream_model(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_stream_modelContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_stream_modelContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_stream

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_stream" ):
                listener.enterAn_stream(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_stream" ):
                listener.exitAn_stream(self)




    def an_stream(self):

        localctx = ZmeiLangParser.An_streamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 402, self.RULE_an_stream)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2033
            self.match(ZmeiLangParser.AN_STREAM)

            self.state = 2034
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 2037 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 2037
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.HASH, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS]:
                    self.state = 2035
                    self.an_stream_model()
                    pass
                elif token in [ZmeiLangParser.NL]:
                    self.state = 2036
                    self.match(ZmeiLangParser.NL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 2039 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.WRITE_MODE) | (1 << ZmeiLangParser.BOOL) | (1 << ZmeiLangParser.NL) | (1 << ZmeiLangParser.ID) | (1 << ZmeiLangParser.HASH) | (1 << ZmeiLangParser.KW_FROM) | (1 << ZmeiLangParser.KW_IMPORT) | (1 << ZmeiLangParser.KW_AS) | (1 << ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FLOAT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DECIMAL) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATETIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_TEXT))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 64)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 64)) | (1 << (ZmeiLangParser.KW_THEME - 64)) | (1 << (ZmeiLangParser.KW_INSTALL - 64)) | (1 << (ZmeiLangParser.KW_HEADER - 64)) | (1 << (ZmeiLangParser.KW_SERVICES - 64)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 64)) | (1 << (ZmeiLangParser.KW_CHILD - 64)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 64)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 64)) | (1 << (ZmeiLangParser.KW_PAGE - 64)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 64)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 64)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 64)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 64)) | (1 << (ZmeiLangParser.KW_BLOCK - 64)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 64)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 64)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 64)) | (1 << (ZmeiLangParser.KW_DELETE - 64)) | (1 << (ZmeiLangParser.KW_EDIT - 64)) | (1 << (ZmeiLangParser.KW_CREATE - 64)) | (1 << (ZmeiLangParser.KW_DETAIL - 64)) | (1 << (ZmeiLangParser.KW_SKIP - 64)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 64)) | (1 << (ZmeiLangParser.KW_CSS - 64)) | (1 << (ZmeiLangParser.KW_JS - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_BASIC - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_SESSION - 64)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_TOKEN - 64)) | (1 << (ZmeiLangParser.KW_INLINE - 64)) | (1 << (ZmeiLangParser.KW_TYPE - 64)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 64)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 64)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 64)) | (1 << (ZmeiLangParser.KW_QUERY - 64)) | (1 << (ZmeiLangParser.KW_AUTH - 64)) | (1 << (ZmeiLangParser.KW_COUNT - 64)) | (1 << (ZmeiLangParser.KW_I18N - 64)) | (1 << (ZmeiLangParser.KW_EXTRA - 64)) | (1 << (ZmeiLangParser.KW_TABS - 64)) | (1 << (ZmeiLangParser.KW_LIST - 64)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 64)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 64)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 64)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 64)) | (1 << (ZmeiLangParser.KW_FIELDS - 64)))) != 0)):
                    break

            self.state = 2041
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_stream_modelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_stream_target_model(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_stream_target_modelContext,0)


        def an_stream_target_filter(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_stream_target_filterContext,0)


        def an_stream_field_list(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_stream_field_listContext,0)


        def COMA(self):
            return self.getToken(ZmeiLangParser.COMA, 0)

        def NL(self):
            return self.getToken(ZmeiLangParser.NL, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_stream_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_stream_model" ):
                listener.enterAn_stream_model(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_stream_model" ):
                listener.exitAn_stream_model(self)




    def an_stream_model(self):

        localctx = ZmeiLangParser.An_stream_modelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 404, self.RULE_an_stream_model)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2043
            self.an_stream_target_model()
            self.state = 2045
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 2044
                self.an_stream_target_filter()


            self.state = 2048
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.EQUALS:
                self.state = 2047
                self.an_stream_field_list()


            self.state = 2051
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COMA:
                self.state = 2050
                self.match(ZmeiLangParser.COMA)


            self.state = 2054
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,209,self._ctx)
            if la_ == 1:
                self.state = 2053
                self.match(ZmeiLangParser.NL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_stream_target_modelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def model_ref(self):
            return self.getTypedRuleContext(ZmeiLangParser.Model_refContext,0)


        def classname(self):
            return self.getTypedRuleContext(ZmeiLangParser.ClassnameContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_stream_target_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_stream_target_model" ):
                listener.enterAn_stream_target_model(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_stream_target_model" ):
                listener.exitAn_stream_target_model(self)




    def an_stream_target_model(self):

        localctx = ZmeiLangParser.An_stream_target_modelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 406, self.RULE_an_stream_target_model)
        try:
            self.state = 2058
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.HASH]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2056
                self.model_ref()
                pass
            elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2057
                self.classname()
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


    class An_stream_target_filterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_stream_target_filter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_stream_target_filter" ):
                listener.enterAn_stream_target_filter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_stream_target_filter" ):
                listener.exitAn_stream_target_filter(self)




    def an_stream_target_filter(self):

        localctx = ZmeiLangParser.An_stream_target_filterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 408, self.RULE_an_stream_target_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2060
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_stream_field_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(ZmeiLangParser.EQUALS, 0)

        def GT(self):
            return self.getToken(ZmeiLangParser.GT, 0)

        def STAR(self):
            return self.getToken(ZmeiLangParser.STAR, 0)

        def an_stream_field_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_stream_field_nameContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_stream_field_nameContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_stream_field_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_stream_field_list" ):
                listener.enterAn_stream_field_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_stream_field_list" ):
                listener.exitAn_stream_field_list(self)




    def an_stream_field_list(self):

        localctx = ZmeiLangParser.An_stream_field_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 410, self.RULE_an_stream_field_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2062
            self.match(ZmeiLangParser.EQUALS)
            self.state = 2063
            self.match(ZmeiLangParser.GT)
            self.state = 2073
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.STAR]:
                self.state = 2064
                self.match(ZmeiLangParser.STAR)
                pass
            elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS]:
                self.state = 2065
                self.an_stream_field_name()
                self.state = 2070
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,211,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 2066
                        self.match(ZmeiLangParser.COMA)
                        self.state = 2067
                        self.an_stream_field_name() 
                    self.state = 2072
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,211,self._ctx)

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


    class An_stream_field_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_stream_field_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_stream_field_name" ):
                listener.enterAn_stream_field_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_stream_field_name" ):
                listener.exitAn_stream_field_name(self)




    def an_stream_field_name(self):

        localctx = ZmeiLangParser.An_stream_field_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 412, self.RULE_an_stream_field_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2075
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_flutterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_FLUTTER(self):
            return self.getToken(ZmeiLangParser.AN_FLUTTER, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def an_flutter_child(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_flutter_childContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_flutter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_flutter" ):
                listener.enterAn_flutter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_flutter" ):
                listener.exitAn_flutter(self)




    def an_flutter(self):

        localctx = ZmeiLangParser.An_flutterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 414, self.RULE_an_flutter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2077
            self.match(ZmeiLangParser.AN_FLUTTER)
            self.state = 2083
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 2078
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 2080
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.KW_CHILD:
                    self.state = 2079
                    self.an_flutter_child()


                self.state = 2082
                self.match(ZmeiLangParser.BRACE_CLOSE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_flutter_childContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_CHILD(self):
            return self.getToken(ZmeiLangParser.KW_CHILD, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def BOOL(self):
            return self.getToken(ZmeiLangParser.BOOL, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_flutter_child

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_flutter_child" ):
                listener.enterAn_flutter_child(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_flutter_child" ):
                listener.exitAn_flutter_child(self)




    def an_flutter_child(self):

        localctx = ZmeiLangParser.An_flutter_childContext(self, self._ctx, self.state)
        self.enterRule(localctx, 416, self.RULE_an_flutter_child)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2085
            self.match(ZmeiLangParser.KW_CHILD)
            self.state = 2086
            self.match(ZmeiLangParser.COLON)
            self.state = 2087
            self.match(ZmeiLangParser.BOOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_reactContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def an_react_type(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_react_typeContext,0)


        def DOT(self):
            return self.getToken(ZmeiLangParser.DOT, 0)

        def an_react_descriptor(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_react_descriptorContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_react

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_react" ):
                listener.enterAn_react(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_react" ):
                listener.exitAn_react(self)




    def an_react(self):

        localctx = ZmeiLangParser.An_reactContext(self, self._ctx, self.state)
        self.enterRule(localctx, 418, self.RULE_an_react)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2089
            self.an_react_type()
            self.state = 2092
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 2090
                self.match(ZmeiLangParser.DOT)
                self.state = 2091
                self.an_react_descriptor()


            self.state = 2094
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_react_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_REACT(self):
            return self.getToken(ZmeiLangParser.AN_REACT, 0)

        def AN_REACT_CLIENT(self):
            return self.getToken(ZmeiLangParser.AN_REACT_CLIENT, 0)

        def AN_REACT_SERVER(self):
            return self.getToken(ZmeiLangParser.AN_REACT_SERVER, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_react_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_react_type" ):
                listener.enterAn_react_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_react_type" ):
                listener.exitAn_react_type(self)




    def an_react_type(self):

        localctx = ZmeiLangParser.An_react_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 420, self.RULE_an_react_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2096
            _la = self._input.LA(1)
            if not(((((_la - 146)) & ~0x3f) == 0 and ((1 << (_la - 146)) & ((1 << (ZmeiLangParser.AN_REACT - 146)) | (1 << (ZmeiLangParser.AN_REACT_CLIENT - 146)) | (1 << (ZmeiLangParser.AN_REACT_SERVER - 146)))) != 0)):
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


    class An_react_descriptorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_react_descriptor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_react_descriptor" ):
                listener.enterAn_react_descriptor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_react_descriptor" ):
                listener.exitAn_react_descriptor(self)




    def an_react_descriptor(self):

        localctx = ZmeiLangParser.An_react_descriptorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 422, self.RULE_an_react_descriptor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2098
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_htmlContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_HTML(self):
            return self.getToken(ZmeiLangParser.AN_HTML, 0)

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def DOT(self):
            return self.getToken(ZmeiLangParser.DOT, 0)

        def an_html_descriptor(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_html_descriptorContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_html

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_html" ):
                listener.enterAn_html(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_html" ):
                listener.exitAn_html(self)




    def an_html(self):

        localctx = ZmeiLangParser.An_htmlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 424, self.RULE_an_html)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2100
            self.match(ZmeiLangParser.AN_HTML)
            self.state = 2103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 2101
                self.match(ZmeiLangParser.DOT)
                self.state = 2102
                self.an_html_descriptor()


            self.state = 2105
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_html_descriptorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_html_descriptor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_html_descriptor" ):
                listener.enterAn_html_descriptor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_html_descriptor" ):
                listener.exitAn_html_descriptor(self)




    def an_html_descriptor(self):

        localctx = ZmeiLangParser.An_html_descriptorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 426, self.RULE_an_html_descriptor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2107
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_markdownContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_MARKDOWN(self):
            return self.getToken(ZmeiLangParser.AN_MARKDOWN, 0)

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def DOT(self):
            return self.getToken(ZmeiLangParser.DOT, 0)

        def an_markdown_descriptor(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_markdown_descriptorContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_markdown

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_markdown" ):
                listener.enterAn_markdown(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_markdown" ):
                listener.exitAn_markdown(self)




    def an_markdown(self):

        localctx = ZmeiLangParser.An_markdownContext(self, self._ctx, self.state)
        self.enterRule(localctx, 428, self.RULE_an_markdown)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2109
            self.match(ZmeiLangParser.AN_MARKDOWN)
            self.state = 2112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 2110
                self.match(ZmeiLangParser.DOT)
                self.state = 2111
                self.an_markdown_descriptor()


            self.state = 2114
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_markdown_descriptorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_markdown_descriptor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_markdown_descriptor" ):
                listener.enterAn_markdown_descriptor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_markdown_descriptor" ):
                listener.exitAn_markdown_descriptor(self)




    def an_markdown_descriptor(self):

        localctx = ZmeiLangParser.An_markdown_descriptorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 430, self.RULE_an_markdown_descriptor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2116
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_deleteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_CRUD_DELETE(self):
            return self.getToken(ZmeiLangParser.AN_CRUD_DELETE, 0)

        def an_crud_params(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_paramsContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_delete

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_delete" ):
                listener.enterAn_crud_delete(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_delete" ):
                listener.exitAn_crud_delete(self)




    def an_crud_delete(self):

        localctx = ZmeiLangParser.An_crud_deleteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 432, self.RULE_an_crud_delete)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2118
            self.match(ZmeiLangParser.AN_CRUD_DELETE)
            self.state = 2119
            self.an_crud_params()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crudContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_CRUD(self):
            return self.getToken(ZmeiLangParser.AN_CRUD, 0)

        def an_crud_params(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_paramsContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud" ):
                listener.enterAn_crud(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud" ):
                listener.exitAn_crud(self)




    def an_crud(self):

        localctx = ZmeiLangParser.An_crudContext(self, self._ctx, self.state)
        self.enterRule(localctx, 434, self.RULE_an_crud)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2121
            self.match(ZmeiLangParser.AN_CRUD)
            self.state = 2122
            self.an_crud_params()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_paramsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_crud_target_model(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_target_modelContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def DOT(self):
            return self.getToken(ZmeiLangParser.DOT, 0)

        def an_crud_descriptor(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_descriptorContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def an_crud_target_filter(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_target_filterContext,0)


        def an_crud_theme(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_themeContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_themeContext,i)


        def an_crud_skip(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_skipContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_skipContext,i)


        def an_crud_fields(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_fieldsContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_fieldsContext,i)


        def an_crud_list_fields(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_list_fieldsContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_list_fieldsContext,i)


        def an_crud_pk_param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_pk_paramContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_pk_paramContext,i)


        def an_crud_item_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_item_nameContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_item_nameContext,i)


        def an_crud_block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_blockContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_blockContext,i)


        def an_crud_object_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_object_exprContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_object_exprContext,i)


        def an_crud_can_edit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_can_editContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_can_editContext,i)


        def an_crud_url_prefix(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_url_prefixContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_url_prefixContext,i)


        def an_crud_link_suffix(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_link_suffixContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_link_suffixContext,i)


        def an_crud_list_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_list_typeContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_list_typeContext,i)


        def an_crud_header(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_headerContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_headerContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def an_crud_next_page(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_next_pageContext,0)


        def an_crud_next_page_url(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_next_page_urlContext,0)


        def an_crud_page_override(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_page_overrideContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_page_overrideContext,i)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_params" ):
                listener.enterAn_crud_params(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_params" ):
                listener.exitAn_crud_params(self)




    def an_crud_params(self):

        localctx = ZmeiLangParser.An_crud_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 436, self.RULE_an_crud_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 2124
                self.match(ZmeiLangParser.DOT)
                self.state = 2125
                self.an_crud_descriptor()


            self.state = 2128
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 2132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 2129
                self.match(ZmeiLangParser.NL)
                self.state = 2134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2135
            self.an_crud_target_model()
            self.state = 2137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 2136
                self.an_crud_target_filter()


            self.state = 2156
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,222,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2154
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [ZmeiLangParser.KW_THEME]:
                        self.state = 2139
                        self.an_crud_theme()
                        pass
                    elif token in [ZmeiLangParser.KW_SKIP]:
                        self.state = 2140
                        self.an_crud_skip()
                        pass
                    elif token in [ZmeiLangParser.KW_FIELDS]:
                        self.state = 2141
                        self.an_crud_fields()
                        pass
                    elif token in [ZmeiLangParser.KW_LIST_FIELDS]:
                        self.state = 2142
                        self.an_crud_list_fields()
                        pass
                    elif token in [ZmeiLangParser.KW_PK_PARAM]:
                        self.state = 2143
                        self.an_crud_pk_param()
                        pass
                    elif token in [ZmeiLangParser.KW_ITEM_NAME]:
                        self.state = 2144
                        self.an_crud_item_name()
                        pass
                    elif token in [ZmeiLangParser.KW_BLOCK]:
                        self.state = 2145
                        self.an_crud_block()
                        pass
                    elif token in [ZmeiLangParser.KW_OBJECT_EXPR]:
                        self.state = 2146
                        self.an_crud_object_expr()
                        pass
                    elif token in [ZmeiLangParser.KW_CAN_EDIT]:
                        self.state = 2147
                        self.an_crud_can_edit()
                        pass
                    elif token in [ZmeiLangParser.KW_URL_PREFIX]:
                        self.state = 2148
                        self.an_crud_url_prefix()
                        pass
                    elif token in [ZmeiLangParser.KW_LINK_SUFFIX]:
                        self.state = 2149
                        self.an_crud_link_suffix()
                        pass
                    elif token in [ZmeiLangParser.KW_LIST]:
                        self.state = 2150
                        self.an_crud_list_type()
                        pass
                    elif token in [ZmeiLangParser.KW_HEADER]:
                        self.state = 2151
                        self.an_crud_header()
                        pass
                    elif token in [ZmeiLangParser.NL]:
                        self.state = 2152
                        self.match(ZmeiLangParser.NL)
                        pass
                    elif token in [ZmeiLangParser.COMA]:
                        self.state = 2153
                        self.match(ZmeiLangParser.COMA)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 2158
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,222,self._ctx)

            self.state = 2162
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,223,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2159
                    self.match(ZmeiLangParser.NL) 
                self.state = 2164
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,223,self._ctx)

            self.state = 2167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,224,self._ctx)
            if la_ == 1:
                self.state = 2165
                self.an_crud_next_page()

            elif la_ == 2:
                self.state = 2166
                self.an_crud_next_page_url()


            self.state = 2172
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,225,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2169
                    self.match(ZmeiLangParser.NL) 
                self.state = 2174
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,225,self._ctx)

            self.state = 2178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 88)) & ~0x3f) == 0 and ((1 << (_la - 88)) & ((1 << (ZmeiLangParser.KW_DELETE - 88)) | (1 << (ZmeiLangParser.KW_EDIT - 88)) | (1 << (ZmeiLangParser.KW_CREATE - 88)) | (1 << (ZmeiLangParser.KW_DETAIL - 88)) | (1 << (ZmeiLangParser.KW_LIST - 88)))) != 0):
                self.state = 2175
                self.an_crud_page_override()
                self.state = 2180
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 2181
                self.match(ZmeiLangParser.NL)
                self.state = 2186
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2187
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_page_overrideContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_crud_view_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_view_nameContext,0)


        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def page_body(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_bodyContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_page_override

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_page_override" ):
                listener.enterAn_crud_page_override(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_page_override" ):
                listener.exitAn_crud_page_override(self)




    def an_crud_page_override(self):

        localctx = ZmeiLangParser.An_crud_page_overrideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 438, self.RULE_an_crud_page_override)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2189
            self.an_crud_view_name()
            self.state = 2193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 2190
                self.match(ZmeiLangParser.NL)
                self.state = 2195
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2196
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 2200
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,229,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2197
                    self.match(ZmeiLangParser.NL) 
                self.state = 2202
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,229,self._ctx)

            self.state = 2203
            self.page_body()
            self.state = 2207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 2204
                self.match(ZmeiLangParser.NL)
                self.state = 2209
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2210
            self.match(ZmeiLangParser.BRACE_CLOSE)
            self.state = 2214
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,231,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2211
                    self.match(ZmeiLangParser.NL) 
                self.state = 2216
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,231,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_descriptorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_descriptor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_descriptor" ):
                listener.enterAn_crud_descriptor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_descriptor" ):
                listener.exitAn_crud_descriptor(self)




    def an_crud_descriptor(self):

        localctx = ZmeiLangParser.An_crud_descriptorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 440, self.RULE_an_crud_descriptor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2217
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_next_pageContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(ZmeiLangParser.EQUALS, 0)

        def GT(self):
            return self.getToken(ZmeiLangParser.GT, 0)

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_crud_next_page_event_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_next_page_event_nameContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_next_page

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_next_page" ):
                listener.enterAn_crud_next_page(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_next_page" ):
                listener.exitAn_crud_next_page(self)




    def an_crud_next_page(self):

        localctx = ZmeiLangParser.An_crud_next_pageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 442, self.RULE_an_crud_next_page)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 2219
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 2220
                self.an_crud_next_page_event_name()
                self.state = 2221
                self.match(ZmeiLangParser.BRACE_CLOSE)


            self.state = 2225
            self.match(ZmeiLangParser.EQUALS)
            self.state = 2226
            self.match(ZmeiLangParser.GT)
            self.state = 2227
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_next_page_event_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_DELETE(self):
            return self.getToken(ZmeiLangParser.KW_DELETE, 0)

        def KW_CREATE(self):
            return self.getToken(ZmeiLangParser.KW_CREATE, 0)

        def KW_EDIT(self):
            return self.getToken(ZmeiLangParser.KW_EDIT, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_next_page_event_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_next_page_event_name" ):
                listener.enterAn_crud_next_page_event_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_next_page_event_name" ):
                listener.exitAn_crud_next_page_event_name(self)




    def an_crud_next_page_event_name(self):

        localctx = ZmeiLangParser.An_crud_next_page_event_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 444, self.RULE_an_crud_next_page_event_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2229
            _la = self._input.LA(1)
            if not(((((_la - 88)) & ~0x3f) == 0 and ((1 << (_la - 88)) & ((1 << (ZmeiLangParser.KW_DELETE - 88)) | (1 << (ZmeiLangParser.KW_EDIT - 88)) | (1 << (ZmeiLangParser.KW_CREATE - 88)))) != 0)):
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


    class An_crud_next_page_urlContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(ZmeiLangParser.EQUALS, 0)

        def GT(self):
            return self.getToken(ZmeiLangParser.GT, 0)

        def an_crud_next_page_url_val(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_next_page_url_valContext,0)


        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_crud_next_page_event_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_next_page_event_nameContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_next_page_url

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_next_page_url" ):
                listener.enterAn_crud_next_page_url(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_next_page_url" ):
                listener.exitAn_crud_next_page_url(self)




    def an_crud_next_page_url(self):

        localctx = ZmeiLangParser.An_crud_next_page_urlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 446, self.RULE_an_crud_next_page_url)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 2231
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 2232
                self.an_crud_next_page_event_name()
                self.state = 2233
                self.match(ZmeiLangParser.BRACE_CLOSE)


            self.state = 2237
            self.match(ZmeiLangParser.EQUALS)
            self.state = 2238
            self.match(ZmeiLangParser.GT)
            self.state = 2239
            self.an_crud_next_page_url_val()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_next_page_url_valContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_next_page_url_val

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_next_page_url_val" ):
                listener.enterAn_crud_next_page_url_val(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_next_page_url_val" ):
                listener.exitAn_crud_next_page_url_val(self)




    def an_crud_next_page_url_val(self):

        localctx = ZmeiLangParser.An_crud_next_page_url_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 448, self.RULE_an_crud_next_page_url_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2241
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


    class An_crud_target_modelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def model_ref(self):
            return self.getTypedRuleContext(ZmeiLangParser.Model_refContext,0)


        def classname(self):
            return self.getTypedRuleContext(ZmeiLangParser.ClassnameContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_target_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_target_model" ):
                listener.enterAn_crud_target_model(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_target_model" ):
                listener.exitAn_crud_target_model(self)




    def an_crud_target_model(self):

        localctx = ZmeiLangParser.An_crud_target_modelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 450, self.RULE_an_crud_target_model)
        try:
            self.state = 2245
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.HASH]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2243
                self.model_ref()
                pass
            elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2244
                self.classname()
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


    class An_crud_target_filterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_target_filter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_target_filter" ):
                listener.enterAn_crud_target_filter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_target_filter" ):
                listener.exitAn_crud_target_filter(self)




    def an_crud_target_filter(self):

        localctx = ZmeiLangParser.An_crud_target_filterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 452, self.RULE_an_crud_target_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2247
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_themeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_THEME(self):
            return self.getToken(ZmeiLangParser.KW_THEME, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_theme

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_theme" ):
                listener.enterAn_crud_theme(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_theme" ):
                listener.exitAn_crud_theme(self)




    def an_crud_theme(self):

        localctx = ZmeiLangParser.An_crud_themeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 454, self.RULE_an_crud_theme)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2249
            self.match(ZmeiLangParser.KW_THEME)
            self.state = 2250
            self.match(ZmeiLangParser.COLON)
            self.state = 2251
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_url_prefixContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_URL_PREFIX(self):
            return self.getToken(ZmeiLangParser.KW_URL_PREFIX, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_crud_url_prefix_val(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_url_prefix_valContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_url_prefix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_url_prefix" ):
                listener.enterAn_crud_url_prefix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_url_prefix" ):
                listener.exitAn_crud_url_prefix(self)




    def an_crud_url_prefix(self):

        localctx = ZmeiLangParser.An_crud_url_prefixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 456, self.RULE_an_crud_url_prefix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2253
            self.match(ZmeiLangParser.KW_URL_PREFIX)
            self.state = 2254
            self.match(ZmeiLangParser.COLON)
            self.state = 2255
            self.an_crud_url_prefix_val()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_url_prefix_valContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_url_prefix_val

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_url_prefix_val" ):
                listener.enterAn_crud_url_prefix_val(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_url_prefix_val" ):
                listener.exitAn_crud_url_prefix_val(self)




    def an_crud_url_prefix_val(self):

        localctx = ZmeiLangParser.An_crud_url_prefix_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 458, self.RULE_an_crud_url_prefix_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2257
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


    class An_crud_link_suffixContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_LINK_SUFFIX(self):
            return self.getToken(ZmeiLangParser.KW_LINK_SUFFIX, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_crud_link_suffix_val(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_link_suffix_valContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_link_suffix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_link_suffix" ):
                listener.enterAn_crud_link_suffix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_link_suffix" ):
                listener.exitAn_crud_link_suffix(self)




    def an_crud_link_suffix(self):

        localctx = ZmeiLangParser.An_crud_link_suffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 460, self.RULE_an_crud_link_suffix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2259
            self.match(ZmeiLangParser.KW_LINK_SUFFIX)
            self.state = 2260
            self.match(ZmeiLangParser.COLON)
            self.state = 2261
            self.an_crud_link_suffix_val()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_link_suffix_valContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_link_suffix_val

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_link_suffix_val" ):
                listener.enterAn_crud_link_suffix_val(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_link_suffix_val" ):
                listener.exitAn_crud_link_suffix_val(self)




    def an_crud_link_suffix_val(self):

        localctx = ZmeiLangParser.An_crud_link_suffix_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 462, self.RULE_an_crud_link_suffix_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2263
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


    class An_crud_item_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_ITEM_NAME(self):
            return self.getToken(ZmeiLangParser.KW_ITEM_NAME, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_item_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_item_name" ):
                listener.enterAn_crud_item_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_item_name" ):
                listener.exitAn_crud_item_name(self)




    def an_crud_item_name(self):

        localctx = ZmeiLangParser.An_crud_item_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 464, self.RULE_an_crud_item_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2265
            self.match(ZmeiLangParser.KW_ITEM_NAME)
            self.state = 2266
            self.match(ZmeiLangParser.COLON)
            self.state = 2267
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_object_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_OBJECT_EXPR(self):
            return self.getToken(ZmeiLangParser.KW_OBJECT_EXPR, 0)

        def code_line(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_lineContext,0)


        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_object_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_object_expr" ):
                listener.enterAn_crud_object_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_object_expr" ):
                listener.exitAn_crud_object_expr(self)




    def an_crud_object_expr(self):

        localctx = ZmeiLangParser.An_crud_object_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 466, self.RULE_an_crud_object_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2269
            self.match(ZmeiLangParser.KW_OBJECT_EXPR)
            self.state = 2273
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.ASSIGN]:
                self.state = 2270
                self.code_line()
                pass
            elif token in [ZmeiLangParser.COLON]:
                self.state = 2271
                self.match(ZmeiLangParser.COLON)
                self.state = 2272
                self.code_block()
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


    class An_crud_can_editContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_CAN_EDIT(self):
            return self.getToken(ZmeiLangParser.KW_CAN_EDIT, 0)

        def code_line(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_lineContext,0)


        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_can_edit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_can_edit" ):
                listener.enterAn_crud_can_edit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_can_edit" ):
                listener.exitAn_crud_can_edit(self)




    def an_crud_can_edit(self):

        localctx = ZmeiLangParser.An_crud_can_editContext(self, self._ctx, self.state)
        self.enterRule(localctx, 468, self.RULE_an_crud_can_edit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2275
            self.match(ZmeiLangParser.KW_CAN_EDIT)
            self.state = 2279
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.ASSIGN]:
                self.state = 2276
                self.code_line()
                pass
            elif token in [ZmeiLangParser.COLON]:
                self.state = 2277
                self.match(ZmeiLangParser.COLON)
                self.state = 2278
                self.code_block()
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


    class An_crud_blockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_BLOCK(self):
            return self.getToken(ZmeiLangParser.KW_BLOCK, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_block" ):
                listener.enterAn_crud_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_block" ):
                listener.exitAn_crud_block(self)




    def an_crud_block(self):

        localctx = ZmeiLangParser.An_crud_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 470, self.RULE_an_crud_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2281
            self.match(ZmeiLangParser.KW_BLOCK)
            self.state = 2282
            self.match(ZmeiLangParser.COLON)
            self.state = 2283
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_pk_paramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_PK_PARAM(self):
            return self.getToken(ZmeiLangParser.KW_PK_PARAM, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_pk_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_pk_param" ):
                listener.enterAn_crud_pk_param(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_pk_param" ):
                listener.exitAn_crud_pk_param(self)




    def an_crud_pk_param(self):

        localctx = ZmeiLangParser.An_crud_pk_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 472, self.RULE_an_crud_pk_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2285
            self.match(ZmeiLangParser.KW_PK_PARAM)
            self.state = 2286
            self.match(ZmeiLangParser.COLON)
            self.state = 2287
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_skipContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_SKIP(self):
            return self.getToken(ZmeiLangParser.KW_SKIP, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_crud_skip_values(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_skip_valuesContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_skip

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_skip" ):
                listener.enterAn_crud_skip(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_skip" ):
                listener.exitAn_crud_skip(self)




    def an_crud_skip(self):

        localctx = ZmeiLangParser.An_crud_skipContext(self, self._ctx, self.state)
        self.enterRule(localctx, 474, self.RULE_an_crud_skip)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2289
            self.match(ZmeiLangParser.KW_SKIP)
            self.state = 2290
            self.match(ZmeiLangParser.COLON)
            self.state = 2291
            self.an_crud_skip_values()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_skip_valuesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_crud_view_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_view_nameContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_view_nameContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_skip_values

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_skip_values" ):
                listener.enterAn_crud_skip_values(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_skip_values" ):
                listener.exitAn_crud_skip_values(self)




    def an_crud_skip_values(self):

        localctx = ZmeiLangParser.An_crud_skip_valuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 476, self.RULE_an_crud_skip_values)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2293
            self.an_crud_view_name()
            self.state = 2298
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,237,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2294
                    self.match(ZmeiLangParser.COMA)
                    self.state = 2295
                    self.an_crud_view_name() 
                self.state = 2300
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,237,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_view_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_DELETE(self):
            return self.getToken(ZmeiLangParser.KW_DELETE, 0)

        def KW_LIST(self):
            return self.getToken(ZmeiLangParser.KW_LIST, 0)

        def KW_CREATE(self):
            return self.getToken(ZmeiLangParser.KW_CREATE, 0)

        def KW_EDIT(self):
            return self.getToken(ZmeiLangParser.KW_EDIT, 0)

        def KW_DETAIL(self):
            return self.getToken(ZmeiLangParser.KW_DETAIL, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_view_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_view_name" ):
                listener.enterAn_crud_view_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_view_name" ):
                listener.exitAn_crud_view_name(self)




    def an_crud_view_name(self):

        localctx = ZmeiLangParser.An_crud_view_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 478, self.RULE_an_crud_view_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2301
            _la = self._input.LA(1)
            if not(((((_la - 88)) & ~0x3f) == 0 and ((1 << (_la - 88)) & ((1 << (ZmeiLangParser.KW_DELETE - 88)) | (1 << (ZmeiLangParser.KW_EDIT - 88)) | (1 << (ZmeiLangParser.KW_CREATE - 88)) | (1 << (ZmeiLangParser.KW_DETAIL - 88)) | (1 << (ZmeiLangParser.KW_LIST - 88)))) != 0)):
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


    class An_crud_fieldsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FIELDS(self):
            return self.getToken(ZmeiLangParser.KW_FIELDS, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_crud_fields_expr(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_fields_exprContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_fields

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_fields" ):
                listener.enterAn_crud_fields(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_fields" ):
                listener.exitAn_crud_fields(self)




    def an_crud_fields(self):

        localctx = ZmeiLangParser.An_crud_fieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 480, self.RULE_an_crud_fields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2303
            self.match(ZmeiLangParser.KW_FIELDS)
            self.state = 2304
            self.match(ZmeiLangParser.COLON)
            self.state = 2305
            self.an_crud_fields_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_list_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_LIST(self):
            return self.getToken(ZmeiLangParser.KW_LIST, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_crud_list_type_var(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_list_type_varContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_list_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_list_type" ):
                listener.enterAn_crud_list_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_list_type" ):
                listener.exitAn_crud_list_type(self)




    def an_crud_list_type(self):

        localctx = ZmeiLangParser.An_crud_list_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 482, self.RULE_an_crud_list_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2307
            self.match(ZmeiLangParser.KW_LIST)
            self.state = 2308
            self.match(ZmeiLangParser.COLON)
            self.state = 2309
            self.an_crud_list_type_var()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_list_type_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_INLINE_TYPE(self):
            return self.getToken(ZmeiLangParser.KW_INLINE_TYPE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_list_type_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_list_type_var" ):
                listener.enterAn_crud_list_type_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_list_type_var" ):
                listener.exitAn_crud_list_type_var(self)




    def an_crud_list_type_var(self):

        localctx = ZmeiLangParser.An_crud_list_type_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 484, self.RULE_an_crud_list_type_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2311
            self.match(ZmeiLangParser.KW_INLINE_TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_headerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_HEADER(self):
            return self.getToken(ZmeiLangParser.KW_HEADER, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_crud_header_enabled(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_header_enabledContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_header" ):
                listener.enterAn_crud_header(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_header" ):
                listener.exitAn_crud_header(self)




    def an_crud_header(self):

        localctx = ZmeiLangParser.An_crud_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 486, self.RULE_an_crud_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2313
            self.match(ZmeiLangParser.KW_HEADER)
            self.state = 2314
            self.match(ZmeiLangParser.COLON)
            self.state = 2315
            self.an_crud_header_enabled()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_header_enabledContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(ZmeiLangParser.BOOL, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_header_enabled

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_header_enabled" ):
                listener.enterAn_crud_header_enabled(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_header_enabled" ):
                listener.exitAn_crud_header_enabled(self)




    def an_crud_header_enabled(self):

        localctx = ZmeiLangParser.An_crud_header_enabledContext(self, self._ctx, self.state)
        self.enterRule(localctx, 488, self.RULE_an_crud_header_enabled)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2317
            self.match(ZmeiLangParser.BOOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_fields_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_crud_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_fieldContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_fieldContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_fields_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_fields_expr" ):
                listener.enterAn_crud_fields_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_fields_expr" ):
                listener.exitAn_crud_fields_expr(self)




    def an_crud_fields_expr(self):

        localctx = ZmeiLangParser.An_crud_fields_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 490, self.RULE_an_crud_fields_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2319
            self.an_crud_field()
            self.state = 2324
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,238,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2320
                    self.match(ZmeiLangParser.COMA)
                    self.state = 2321
                    self.an_crud_field() 
                self.state = 2326
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,238,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_fieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_crud_field_spec(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_field_specContext,0)


        def an_crud_field_filter(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_field_filterContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_field" ):
                listener.enterAn_crud_field(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_field" ):
                listener.exitAn_crud_field(self)




    def an_crud_field(self):

        localctx = ZmeiLangParser.An_crud_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 492, self.RULE_an_crud_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2327
            self.an_crud_field_spec()
            self.state = 2329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 2328
                self.an_crud_field_filter()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_field_specContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(ZmeiLangParser.STAR, 0)

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def EXCLUDE(self):
            return self.getToken(ZmeiLangParser.EXCLUDE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_field_spec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_field_spec" ):
                listener.enterAn_crud_field_spec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_field_spec" ):
                listener.exitAn_crud_field_spec(self)




    def an_crud_field_spec(self):

        localctx = ZmeiLangParser.An_crud_field_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 494, self.RULE_an_crud_field_spec)
        self._la = 0 # Token type
        try:
            self.state = 2336
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.STAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2331
                self.match(ZmeiLangParser.STAR)
                pass
            elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.EXCLUDE, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2333
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.EXCLUDE:
                    self.state = 2332
                    self.match(ZmeiLangParser.EXCLUDE)


                self.state = 2335
                self.id_or_kw()
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


    class An_crud_field_filterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_field_filter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_field_filter" ):
                listener.enterAn_crud_field_filter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_field_filter" ):
                listener.exitAn_crud_field_filter(self)




    def an_crud_field_filter(self):

        localctx = ZmeiLangParser.An_crud_field_filterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 496, self.RULE_an_crud_field_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2338
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_list_fieldsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_LIST_FIELDS(self):
            return self.getToken(ZmeiLangParser.KW_LIST_FIELDS, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_crud_list_fields_expr(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_list_fields_exprContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_list_fields

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_list_fields" ):
                listener.enterAn_crud_list_fields(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_list_fields" ):
                listener.exitAn_crud_list_fields(self)




    def an_crud_list_fields(self):

        localctx = ZmeiLangParser.An_crud_list_fieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 498, self.RULE_an_crud_list_fields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2340
            self.match(ZmeiLangParser.KW_LIST_FIELDS)
            self.state = 2341
            self.match(ZmeiLangParser.COLON)
            self.state = 2342
            self.an_crud_list_fields_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_list_fields_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_crud_list_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_list_fieldContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_list_fieldContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_list_fields_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_list_fields_expr" ):
                listener.enterAn_crud_list_fields_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_list_fields_expr" ):
                listener.exitAn_crud_list_fields_expr(self)




    def an_crud_list_fields_expr(self):

        localctx = ZmeiLangParser.An_crud_list_fields_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 500, self.RULE_an_crud_list_fields_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2344
            self.an_crud_list_field()
            self.state = 2349
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,242,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2345
                    self.match(ZmeiLangParser.COMA)
                    self.state = 2346
                    self.an_crud_list_field() 
                self.state = 2351
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,242,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_list_fieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_crud_list_field_spec(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_list_field_specContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_list_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_list_field" ):
                listener.enterAn_crud_list_field(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_list_field" ):
                listener.exitAn_crud_list_field(self)




    def an_crud_list_field(self):

        localctx = ZmeiLangParser.An_crud_list_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 502, self.RULE_an_crud_list_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2352
            self.an_crud_list_field_spec()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_list_field_specContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(ZmeiLangParser.STAR, 0)

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def EXCLUDE(self):
            return self.getToken(ZmeiLangParser.EXCLUDE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_list_field_spec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_list_field_spec" ):
                listener.enterAn_crud_list_field_spec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_list_field_spec" ):
                listener.exitAn_crud_list_field_spec(self)




    def an_crud_list_field_spec(self):

        localctx = ZmeiLangParser.An_crud_list_field_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 504, self.RULE_an_crud_list_field_spec)
        self._la = 0 # Token type
        try:
            self.state = 2359
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.STAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2354
                self.match(ZmeiLangParser.STAR)
                pass
            elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.EXCLUDE, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2356
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.EXCLUDE:
                    self.state = 2355
                    self.match(ZmeiLangParser.EXCLUDE)


                self.state = 2358
                self.id_or_kw()
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


    class An_postContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_POST(self):
            return self.getToken(ZmeiLangParser.AN_POST, 0)

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_post

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_post" ):
                listener.enterAn_post(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_post" ):
                listener.exitAn_post(self)




    def an_post(self):

        localctx = ZmeiLangParser.An_postContext(self, self._ctx, self.state)
        self.enterRule(localctx, 506, self.RULE_an_post)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2361
            self.match(ZmeiLangParser.AN_POST)
            self.state = 2363
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 2362
                self.code_block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_authContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_AUTH(self):
            return self.getToken(ZmeiLangParser.AN_AUTH, 0)

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_auth

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_auth" ):
                listener.enterAn_auth(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_auth" ):
                listener.exitAn_auth(self)




    def an_auth(self):

        localctx = ZmeiLangParser.An_authContext(self, self._ctx, self.state)
        self.enterRule(localctx, 508, self.RULE_an_auth)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2365
            self.match(ZmeiLangParser.AN_AUTH)
            self.state = 2367
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 2366
                self.code_block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_createContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_CRUD_CREATE(self):
            return self.getToken(ZmeiLangParser.AN_CRUD_CREATE, 0)

        def an_crud_params(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_paramsContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_create

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_create" ):
                listener.enterAn_crud_create(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_create" ):
                listener.exitAn_crud_create(self)




    def an_crud_create(self):

        localctx = ZmeiLangParser.An_crud_createContext(self, self._ctx, self.state)
        self.enterRule(localctx, 510, self.RULE_an_crud_create)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2369
            self.match(ZmeiLangParser.AN_CRUD_CREATE)
            self.state = 2370
            self.an_crud_params()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_editContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_CRUD_EDIT(self):
            return self.getToken(ZmeiLangParser.AN_CRUD_EDIT, 0)

        def an_crud_params(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_paramsContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_edit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_edit" ):
                listener.enterAn_crud_edit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_edit" ):
                listener.exitAn_crud_edit(self)




    def an_crud_edit(self):

        localctx = ZmeiLangParser.An_crud_editContext(self, self._ctx, self.state)
        self.enterRule(localctx, 512, self.RULE_an_crud_edit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2372
            self.match(ZmeiLangParser.AN_CRUD_EDIT)
            self.state = 2373
            self.an_crud_params()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_CRUD_LIST(self):
            return self.getToken(ZmeiLangParser.AN_CRUD_LIST, 0)

        def an_crud_params(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_paramsContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_list" ):
                listener.enterAn_crud_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_list" ):
                listener.exitAn_crud_list(self)




    def an_crud_list(self):

        localctx = ZmeiLangParser.An_crud_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 514, self.RULE_an_crud_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2375
            self.match(ZmeiLangParser.AN_CRUD_LIST)
            self.state = 2376
            self.an_crud_params()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_menuContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_MENU(self):
            return self.getToken(ZmeiLangParser.AN_MENU, 0)

        def DOT(self):
            return self.getToken(ZmeiLangParser.DOT, 0)

        def an_menu_descriptor(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_menu_descriptorContext,0)


        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def an_menu_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_menu_itemContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_menu_itemContext,i)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_menu

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_menu" ):
                listener.enterAn_menu(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_menu" ):
                listener.exitAn_menu(self)




    def an_menu(self):

        localctx = ZmeiLangParser.An_menuContext(self, self._ctx, self.state)
        self.enterRule(localctx, 516, self.RULE_an_menu)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2378
            self.match(ZmeiLangParser.AN_MENU)
            self.state = 2379
            self.match(ZmeiLangParser.DOT)
            self.state = 2380
            self.an_menu_descriptor()
            self.state = 2381
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 2385
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,247,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2382
                    self.match(ZmeiLangParser.NL) 
                self.state = 2387
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,247,self._ctx)

            self.state = 2389 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 2388
                    self.an_menu_item()

                else:
                    raise NoViableAltException(self)
                self.state = 2391 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,248,self._ctx)

            self.state = 2396
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 2393
                self.match(ZmeiLangParser.NL)
                self.state = 2398
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2399
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_menu_descriptorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_menu_descriptor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_menu_descriptor" ):
                listener.enterAn_menu_descriptor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_menu_descriptor" ):
                listener.exitAn_menu_descriptor(self)




    def an_menu_descriptor(self):

        localctx = ZmeiLangParser.An_menu_descriptorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 518, self.RULE_an_menu_descriptor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2401
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_menu_itemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_menu_label(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_menu_labelContext,0)


        def an_menu_item_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_menu_item_codeContext,0)


        def an_menu_target(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_menu_targetContext,0)


        def COMA(self):
            return self.getToken(ZmeiLangParser.COMA, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def an_menu_item_args(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_menu_item_argsContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_menu_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_menu_item" ):
                listener.enterAn_menu_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_menu_item" ):
                listener.exitAn_menu_item(self)




    def an_menu_item(self):

        localctx = ZmeiLangParser.An_menu_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 520, self.RULE_an_menu_item)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2404
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COMA:
                self.state = 2403
                self.match(ZmeiLangParser.COMA)


            self.state = 2409
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 2406
                self.match(ZmeiLangParser.NL)
                self.state = 2411
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2413
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.SQ_BRACE_OPEN:
                self.state = 2412
                self.an_menu_item_args()


            self.state = 2415
            self.an_menu_label()
            self.state = 2418
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.ASSIGN]:
                self.state = 2416
                self.an_menu_item_code()
                pass
            elif token in [ZmeiLangParser.COLON]:
                self.state = 2417
                self.an_menu_target()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 2423
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,254,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2420
                    self.match(ZmeiLangParser.NL) 
                self.state = 2425
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,254,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_menu_targetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_menu_item_page(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_menu_item_pageContext,0)


        def an_menu_item_url(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_menu_item_urlContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_menu_target

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_menu_target" ):
                listener.enterAn_menu_target(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_menu_target" ):
                listener.exitAn_menu_target(self)




    def an_menu_target(self):

        localctx = ZmeiLangParser.An_menu_targetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 522, self.RULE_an_menu_target)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2426
            self.match(ZmeiLangParser.COLON)
            self.state = 2429
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.KW_PAGE]:
                self.state = 2427
                self.an_menu_item_page()
                pass
            elif token in [ZmeiLangParser.STRING_DQ, ZmeiLangParser.STRING_SQ]:
                self.state = 2428
                self.an_menu_item_url()
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


    class An_menu_item_codeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_line(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_lineContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_menu_item_code

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_menu_item_code" ):
                listener.enterAn_menu_item_code(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_menu_item_code" ):
                listener.exitAn_menu_item_code(self)




    def an_menu_item_code(self):

        localctx = ZmeiLangParser.An_menu_item_codeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 524, self.RULE_an_menu_item_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2431
            self.code_line()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_menu_item_argsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQ_BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.SQ_BRACE_OPEN, 0)

        def an_menu_item_arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_menu_item_argContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_menu_item_argContext,i)


        def SQ_BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.SQ_BRACE_CLOSE, 0)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_menu_item_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_menu_item_args" ):
                listener.enterAn_menu_item_args(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_menu_item_args" ):
                listener.exitAn_menu_item_args(self)




    def an_menu_item_args(self):

        localctx = ZmeiLangParser.An_menu_item_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 526, self.RULE_an_menu_item_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2433
            self.match(ZmeiLangParser.SQ_BRACE_OPEN)
            self.state = 2434
            self.an_menu_item_arg()
            self.state = 2439
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 2435
                self.match(ZmeiLangParser.COMA)
                self.state = 2436
                self.an_menu_item_arg()
                self.state = 2441
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2442
            self.match(ZmeiLangParser.SQ_BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_menu_item_argContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_menu_item_arg_key(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_menu_item_arg_keyContext,0)


        def EQUALS(self):
            return self.getToken(ZmeiLangParser.EQUALS, 0)

        def an_menu_item_arg_val(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_menu_item_arg_valContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_menu_item_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_menu_item_arg" ):
                listener.enterAn_menu_item_arg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_menu_item_arg" ):
                listener.exitAn_menu_item_arg(self)




    def an_menu_item_arg(self):

        localctx = ZmeiLangParser.An_menu_item_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 528, self.RULE_an_menu_item_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2444
            self.an_menu_item_arg_key()
            self.state = 2445
            self.match(ZmeiLangParser.EQUALS)
            self.state = 2446
            self.an_menu_item_arg_val()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_menu_item_arg_keyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_menu_item_arg_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_menu_item_arg_key" ):
                listener.enterAn_menu_item_arg_key(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_menu_item_arg_key" ):
                listener.exitAn_menu_item_arg_key(self)




    def an_menu_item_arg_key(self):

        localctx = ZmeiLangParser.An_menu_item_arg_keyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 530, self.RULE_an_menu_item_arg_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2448
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_menu_item_arg_valContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_menu_item_arg_val

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_menu_item_arg_val" ):
                listener.enterAn_menu_item_arg_val(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_menu_item_arg_val" ):
                listener.exitAn_menu_item_arg_val(self)




    def an_menu_item_arg_val(self):

        localctx = ZmeiLangParser.An_menu_item_arg_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 532, self.RULE_an_menu_item_arg_val)
        try:
            self.state = 2453
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.STRING_DQ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2450
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2451
                self.match(ZmeiLangParser.STRING_SQ)
                pass
            elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2452
                self.id_or_kw()
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


    class An_menu_item_urlContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_menu_item_url

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_menu_item_url" ):
                listener.enterAn_menu_item_url(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_menu_item_url" ):
                listener.exitAn_menu_item_url(self)




    def an_menu_item_url(self):

        localctx = ZmeiLangParser.An_menu_item_urlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 534, self.RULE_an_menu_item_url)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2455
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


    class An_menu_item_pageContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_PAGE(self):
            return self.getToken(ZmeiLangParser.KW_PAGE, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_menu_item_page_ref(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_menu_item_page_refContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_menu_item_page

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_menu_item_page" ):
                listener.enterAn_menu_item_page(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_menu_item_page" ):
                listener.exitAn_menu_item_page(self)




    def an_menu_item_page(self):

        localctx = ZmeiLangParser.An_menu_item_pageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 536, self.RULE_an_menu_item_page)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2457
            self.match(ZmeiLangParser.KW_PAGE)
            self.state = 2458
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 2459
            self.an_menu_item_page_ref()
            self.state = 2460
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_menu_item_page_refContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Id_or_kwContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,i)


        def DOT(self):
            return self.getToken(ZmeiLangParser.DOT, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_menu_item_page_ref

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_menu_item_page_ref" ):
                listener.enterAn_menu_item_page_ref(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_menu_item_page_ref" ):
                listener.exitAn_menu_item_page_ref(self)




    def an_menu_item_page_ref(self):

        localctx = ZmeiLangParser.An_menu_item_page_refContext(self, self._ctx, self.state)
        self.enterRule(localctx, 538, self.RULE_an_menu_item_page_ref)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2465
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,258,self._ctx)
            if la_ == 1:
                self.state = 2462
                self.id_or_kw()
                self.state = 2463
                self.match(ZmeiLangParser.DOT)


            self.state = 2467
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_menu_labelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_menu_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_menu_label" ):
                listener.enterAn_menu_label(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_menu_label" ):
                listener.exitAn_menu_label(self)




    def an_menu_label(self):

        localctx = ZmeiLangParser.An_menu_labelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 540, self.RULE_an_menu_label)
        try:
            self.state = 2472
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.STRING_DQ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2469
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2470
                self.match(ZmeiLangParser.STRING_SQ)
                pass
            elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2471
                self.id_or_kw()
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


    class An_crud_detailContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_CRUD_DETAIL(self):
            return self.getToken(ZmeiLangParser.AN_CRUD_DETAIL, 0)

        def an_crud_params(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_paramsContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_detail

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_detail" ):
                listener.enterAn_crud_detail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_detail" ):
                listener.exitAn_crud_detail(self)




    def an_crud_detail(self):

        localctx = ZmeiLangParser.An_crud_detailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 542, self.RULE_an_crud_detail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2474
            self.match(ZmeiLangParser.AN_CRUD_DETAIL)
            self.state = 2475
            self.an_crud_params()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_priority_markerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_PRIORITY(self):
            return self.getToken(ZmeiLangParser.AN_PRIORITY, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_priority_marker

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_priority_marker" ):
                listener.enterAn_priority_marker(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_priority_marker" ):
                listener.exitAn_priority_marker(self)




    def an_priority_marker(self):

        localctx = ZmeiLangParser.An_priority_markerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 544, self.RULE_an_priority_marker)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2477
            self.match(ZmeiLangParser.AN_PRIORITY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_getContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_GET(self):
            return self.getToken(ZmeiLangParser.AN_GET, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_get

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_get" ):
                listener.enterAn_get(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_get" ):
                listener.exitAn_get(self)




    def an_get(self):

        localctx = ZmeiLangParser.An_getContext(self, self._ctx, self.state)
        self.enterRule(localctx, 546, self.RULE_an_get)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2479
            self.match(ZmeiLangParser.AN_GET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_errorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_ERROR(self):
            return self.getToken(ZmeiLangParser.AN_ERROR, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_error_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_error_codeContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_error

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_error" ):
                listener.enterAn_error(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_error" ):
                listener.exitAn_error(self)




    def an_error(self):

        localctx = ZmeiLangParser.An_errorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 548, self.RULE_an_error)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2481
            self.match(ZmeiLangParser.AN_ERROR)
            self.state = 2482
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 2483
            self.an_error_code()
            self.state = 2484
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_error_codeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self):
            return self.getToken(ZmeiLangParser.DIGIT, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_error_code

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_error_code" ):
                listener.enterAn_error_code(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_error_code" ):
                listener.exitAn_error_code(self)




    def an_error_code(self):

        localctx = ZmeiLangParser.An_error_codeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 550, self.RULE_an_error_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2486
            self.match(ZmeiLangParser.DIGIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






# Generated from /Users/aleksandrrudakov/dev/zmei/generator/zmei_generator/parser/gen/grammar/ZmeiLangParser.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\u00a1")
        buf.write("\u09d2\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("\4\u0114\t\u0114\4\u0115\t\u0115\4\u0116\t\u0116\4\u0117")
        buf.write("\t\u0117\4\u0118\t\u0118\3\2\7\2\u0232\n\2\f\2\16\2\u0235")
        buf.write("\13\2\3\2\7\2\u0238\n\2\f\2\16\2\u023b\13\2\3\2\7\2\u023e")
        buf.write("\n\2\f\2\16\2\u0241\13\2\3\2\5\2\u0244\n\2\3\2\6\2\u0247")
        buf.write("\n\2\r\2\16\2\u0248\5\2\u024b\n\2\3\2\7\2\u024e\n\2\f")
        buf.write("\2\16\2\u0251\13\2\3\2\5\2\u0254\n\2\3\2\6\2\u0257\n\2")
        buf.write("\r\2\16\2\u0258\5\2\u025b\n\2\3\2\7\2\u025e\n\2\f\2\16")
        buf.write("\2\u0261\13\2\3\2\3\2\3\3\6\3\u0266\n\3\r\3\16\3\u0267")
        buf.write("\3\4\6\4\u026b\n\4\r\4\16\4\u026c\3\5\3\5\3\6\3\6\3\7")
        buf.write("\3\7\5\7\u0275\n\7\3\7\3\7\3\7\6\7\u027a\n\7\r\7\16\7")
        buf.write("\u027b\3\b\5\b\u027f\n\b\3\b\3\b\3\t\3\t\3\t\7\t\u0286")
        buf.write("\n\t\f\t\16\t\u0289\13\t\3\n\3\n\3\n\5\n\u028e\n\n\3\n")
        buf.write("\5\n\u0291\n\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17")
        buf.write("\3\17\3\17\7\17\u029e\n\17\f\17\16\17\u02a1\13\17\3\20")
        buf.write("\3\20\3\20\3\20\5\20\u02a7\n\20\3\20\3\20\3\21\5\21\u02ac")
        buf.write("\n\21\3\21\3\21\3\21\3\21\7\21\u02b2\n\21\f\21\16\21\u02b5")
        buf.write("\13\21\3\21\3\21\3\21\5\21\u02ba\n\21\3\21\7\21\u02bd")
        buf.write("\n\21\f\21\16\21\u02c0\13\21\5\21\u02c2\n\21\3\22\5\22")
        buf.write("\u02c5\n\22\3\22\3\22\5\22\u02c9\n\22\3\23\3\23\3\23\3")
        buf.write("\23\3\24\3\24\5\24\u02d1\n\24\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\5\27\u02e3\n\27\3\30\3\30\3\30\3\30\3\30\5\30\u02ea\n")
        buf.write("\30\3\31\3\31\3\32\3\32\3\32\5\32\u02f1\n\32\3\33\3\33")
        buf.write("\3\33\5\33\u02f6\n\33\3\34\3\34\3\34\5\34\u02fb\n\34\3")
        buf.write("\35\3\35\3\35\5\35\u0300\n\35\3\36\3\36\3\36\7\36\u0305")
        buf.write("\n\36\f\36\16\36\u0308\13\36\3\36\5\36\u030b\n\36\3\36")
        buf.write("\7\36\u030e\n\36\f\36\16\36\u0311\13\36\3\36\6\36\u0314")
        buf.write("\n\36\r\36\16\36\u0315\3\36\7\36\u0319\n\36\f\36\16\36")
        buf.write("\u031c\13\36\3\36\3\36\3\37\3\37\3 \3 \3 \7 \u0325\n ")
        buf.write("\f \16 \u0328\13 \3 \5 \u032b\n \3 \7 \u032e\n \f \16")
        buf.write(" \u0331\13 \3 \3 \5 \u0335\n \7 \u0337\n \f \16 \u033a")
        buf.write("\13 \3 \7 \u033d\n \f \16 \u0340\13 \3 \3 \3!\3!\3!\7")
        buf.write("!\u0347\n!\f!\16!\u034a\13!\3!\3!\3!\7!\u034f\n!\f!\16")
        buf.write("!\u0352\13!\5!\u0354\n!\3!\7!\u0357\n!\f!\16!\u035a\13")
        buf.write("!\3!\3!\3\"\7\"\u035f\n\"\f\"\16\"\u0362\13\"\3\"\3\"")
        buf.write("\3\"\7\"\u0367\n\"\f\"\16\"\u036a\13\"\3\"\3\"\5\"\u036e")
        buf.write("\n\"\7\"\u0370\n\"\f\"\16\"\u0373\13\"\3\"\7\"\u0376\n")
        buf.write("\"\f\"\16\"\u0379\13\"\3\"\5\"\u037c\n\"\3#\3#\3$\3$\7")
        buf.write("$\u0382\n$\f$\16$\u0385\13$\3$\3$\7$\u0389\n$\f$\16$\u038c")
        buf.write("\13$\3$\3$\3$\7$\u0391\n$\f$\16$\u0394\13$\3$\3$\3$\7")
        buf.write("$\u0399\n$\f$\16$\u039c\13$\3$\3$\5$\u03a0\n$\7$\u03a2")
        buf.write("\n$\f$\16$\u03a5\13$\5$\u03a7\n$\3$\7$\u03aa\n$\f$\16")
        buf.write("$\u03ad\13$\3$\3$\7$\u03b1\n$\f$\16$\u03b4\13$\3%\3%\3")
        buf.write("%\3&\3&\3&\3&\6&\u03bd\n&\r&\16&\u03be\3\'\3\'\3\'\3\'")
        buf.write("\6\'\u03c5\n\'\r\'\16\'\u03c6\3(\3(\3(\3(\6(\u03cd\n(")
        buf.write("\r(\16(\u03ce\3)\7)\u03d2\n)\f)\16)\u03d5\13)\3)\3)\3")
        buf.write(")\3)\3*\3*\3+\3+\3+\3+\5+\u03e1\n+\3,\3,\3,\3,\3-\3-\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\5.\u03f0\n.\3.\3.\3/\3/\3\60\3\60")
        buf.write("\3\60\5\60\u03f9\n\60\3\61\3\61\3\61\3\61\3\61\3\62\3")
        buf.write("\62\3\62\7\62\u0403\n\62\f\62\16\62\u0406\13\62\3\63\3")
        buf.write("\63\5\63\u040a\n\63\3\63\7\63\u040d\n\63\f\63\16\63\u0410")
        buf.write("\13\63\3\63\7\63\u0413\n\63\f\63\16\63\u0416\13\63\3\63")
        buf.write("\7\63\u0419\n\63\f\63\16\63\u041c\13\63\3\63\7\63\u041f")
        buf.write("\n\63\f\63\16\63\u0422\13\63\3\63\7\63\u0425\n\63\f\63")
        buf.write("\16\63\u0428\13\63\3\64\3\64\3\64\6\64\u042d\n\64\r\64")
        buf.write("\16\64\u042e\3\64\5\64\u0432\n\64\3\65\3\65\5\65\u0436")
        buf.write("\n\65\3\65\3\65\5\65\u043a\n\65\3\65\3\65\3\65\3\66\3")
        buf.write("\66\3\66\3\66\6\66\u0443\n\66\r\66\16\66\u0444\3\67\3")
        buf.write("\67\3\67\3\67\5\67\u044b\n\67\38\38\38\58\u0450\n8\39")
        buf.write("\39\39\39\39\59\u0457\n9\3:\3:\3;\7;\u045c\n;\f;\16;\u045f")
        buf.write("\13;\3;\3;\5;\u0463\n;\3;\5;\u0466\n;\3;\5;\u0469\n;\3")
        buf.write(";\6;\u046c\n;\r;\16;\u046d\3;\5;\u0471\n;\3<\3<\5<\u0475")
        buf.write("\n<\3<\3<\3<\5<\u047a\n<\3<\3<\3<\5<\u047f\n<\3=\3=\3")
        buf.write(">\5>\u0484\n>\3>\3>\3?\3?\3?\3@\3@\3A\3A\3A\3B\3B\3C\3")
        buf.write("C\3D\6D\u0495\nD\rD\16D\u0496\3D\3D\5D\u049b\nD\3E\3E")
        buf.write("\3E\3F\3F\3F\3G\3G\3H\3H\3I\3I\3I\3I\3I\3I\3I\3I\3I\3")
        buf.write("I\3I\3I\3I\3I\3I\3I\3I\3I\5I\u04b9\nI\3J\3J\3K\3K\3L\3")
        buf.write("L\3M\3M\3N\3N\3O\3O\3P\3P\3Q\3Q\3R\3R\3S\3S\3T\3T\3U\3")
        buf.write("U\3V\3V\3V\3V\3V\5V\u04d8\nV\3V\3V\5V\u04dc\nV\3W\3W\3")
        buf.write("X\3X\3X\3X\3X\7X\u04e5\nX\fX\16X\u04e8\13X\3Y\5Y\u04eb")
        buf.write("\nY\3Y\3Y\3Z\3Z\3Z\5Z\u04f2\nZ\3[\3[\3[\3\\\3\\\3\\\3")
        buf.write("\\\3\\\5\\\u04fc\n\\\3]\3]\3]\3]\3]\7]\u0503\n]\f]\16")
        buf.write("]\u0506\13]\3^\5^\u0509\n^\3^\3^\3_\3_\3_\5_\u0510\n_")
        buf.write("\3`\3`\3`\3a\3a\3a\3a\3a\3b\3b\3b\7b\u051d\nb\fb\16b\u0520")
        buf.write("\13b\3c\3c\3d\3d\3d\3d\3d\5d\u0529\nd\3e\3e\3f\3f\3f\3")
        buf.write("f\3f\5f\u0532\nf\3g\3g\3h\3h\3h\7h\u0539\nh\fh\16h\u053c")
        buf.write("\13h\3i\3i\3i\3i\3j\3j\3k\3k\3k\3l\7l\u0548\nl\fl\16l")
        buf.write("\u054b\13l\3m\3m\3m\3n\3n\3n\5n\u0553\nn\3n\3n\5n\u0557")
        buf.write("\nn\3n\5n\u055a\nn\3n\3n\3o\3o\3p\3p\3q\3q\3r\3r\3s\3")
        buf.write("s\3s\3s\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\5")
        buf.write("t\u0579\nt\3u\3u\3u\3u\3u\3u\3u\3u\3u\3u\3u\3u\3u\3u\7")
        buf.write("u\u0589\nu\fu\16u\u058c\13u\3u\7u\u058f\nu\fu\16u\u0592")
        buf.write("\13u\3u\5u\u0595\nu\3u\7u\u0598\nu\fu\16u\u059b\13u\3")
        buf.write("v\3v\3v\7v\u05a0\nv\fv\16v\u05a3\13v\3v\3v\3v\7v\u05a8")
        buf.write("\nv\fv\16v\u05ab\13v\3v\7v\u05ae\nv\fv\16v\u05b1\13v\3")
        buf.write("w\3w\3w\3w\3w\7w\u05b8\nw\fw\16w\u05bb\13w\3x\3x\3y\3")
        buf.write("y\3z\3z\3z\3z\3z\7z\u05c6\nz\fz\16z\u05c9\13z\3{\3{\3")
        buf.write("{\3{\3{\3{\3{\7{\u05d2\n{\f{\16{\u05d5\13{\3{\5{\u05d8")
        buf.write("\n{\3|\3|\3}\3}\3}\3}\3~\3~\3\177\3\177\3\177\3\177\3")
        buf.write("\u0080\3\u0080\3\u0080\3\u0080\3\u0081\3\u0081\3\u0081")
        buf.write("\3\u0081\3\u0081\7\u0081\u05ef\n\u0081\f\u0081\16\u0081")
        buf.write("\u05f2\13\u0081\3\u0082\3\u0082\5\u0082\u05f6\n\u0082")
        buf.write("\3\u0082\3\u0082\3\u0082\3\u0082\3\u0083\3\u0083\3\u0084")
        buf.write("\3\u0084\3\u0085\3\u0085\3\u0085\3\u0085\7\u0085\u0604")
        buf.write("\n\u0085\f\u0085\16\u0085\u0607\13\u0085\3\u0086\3\u0086")
        buf.write("\3\u0086\3\u0086\7\u0086\u060d\n\u0086\f\u0086\16\u0086")
        buf.write("\u0610\13\u0086\3\u0087\3\u0087\3\u0087\3\u0087\7\u0087")
        buf.write("\u0616\n\u0087\f\u0087\16\u0087\u0619\13\u0087\3\u0088")
        buf.write("\3\u0088\3\u0088\3\u0088\7\u0088\u061f\n\u0088\f\u0088")
        buf.write("\16\u0088\u0622\13\u0088\3\u0089\3\u0089\3\u0089\3\u0089")
        buf.write("\7\u0089\u0628\n\u0089\f\u0089\16\u0089\u062b\13\u0089")
        buf.write("\3\u008a\3\u008a\3\u008a\3\u008a\7\u008a\u0631\n\u008a")
        buf.write("\f\u008a\16\u008a\u0634\13\u008a\3\u008b\3\u008b\3\u008b")
        buf.write("\3\u008b\3\u008b\3\u008b\7\u008b\u063c\n\u008b\f\u008b")
        buf.write("\16\u008b\u063f\13\u008b\5\u008b\u0641\n\u008b\3\u008b")
        buf.write("\3\u008b\5\u008b\u0645\n\u008b\3\u008c\3\u008c\3\u008d")
        buf.write("\3\u008d\3\u008e\3\u008e\3\u008e\5\u008e\u064e\n\u008e")
        buf.write("\3\u008e\3\u008e\3\u008e\3\u008e\5\u008e\u0654\n\u008e")
        buf.write("\3\u008f\3\u008f\3\u008f\3\u008f\7\u008f\u065a\n\u008f")
        buf.write("\f\u008f\16\u008f\u065d\13\u008f\3\u0090\3\u0090\3\u0090")
        buf.write("\3\u0090\3\u0090\3\u0090\3\u0090\3\u0090\3\u0090\3\u0090")
        buf.write("\3\u0090\3\u0090\3\u0090\7\u0090\u066c\n\u0090\f\u0090")
        buf.write("\16\u0090\u066f\13\u0090\3\u0091\3\u0091\3\u0092\3\u0092")
        buf.write("\3\u0092\3\u0092\7\u0092\u0677\n\u0092\f\u0092\16\u0092")
        buf.write("\u067a\13\u0092\3\u0093\3\u0093\3\u0093\3\u0093\7\u0093")
        buf.write("\u0680\n\u0093\f\u0093\16\u0093\u0683\13\u0093\3\u0094")
        buf.write("\3\u0094\3\u0094\7\u0094\u0688\n\u0094\f\u0094\16\u0094")
        buf.write("\u068b\13\u0094\3\u0095\3\u0095\5\u0095\u068f\n\u0095")
        buf.write("\3\u0095\3\u0095\7\u0095\u0693\n\u0095\f\u0095\16\u0095")
        buf.write("\u0696\13\u0095\3\u0096\3\u0096\5\u0096\u069a\n\u0096")
        buf.write("\3\u0096\3\u0096\7\u0096\u069e\n\u0096\f\u0096\16\u0096")
        buf.write("\u06a1\13\u0096\3\u0097\3\u0097\5\u0097\u06a5\n\u0097")
        buf.write("\3\u0097\3\u0097\7\u0097\u06a9\n\u0097\f\u0097\16\u0097")
        buf.write("\u06ac\13\u0097\3\u0098\3\u0098\3\u0098\3\u0098\7\u0098")
        buf.write("\u06b2\n\u0098\f\u0098\16\u0098\u06b5\13\u0098\3\u0099")
        buf.write("\3\u0099\3\u0099\3\u0099\7\u0099\u06bb\n\u0099\f\u0099")
        buf.write("\16\u0099\u06be\13\u0099\3\u009a\3\u009a\3\u009a\3\u009a")
        buf.write("\5\u009a\u06c4\n\u009a\3\u009a\7\u009a\u06c7\n\u009a\f")
        buf.write("\u009a\16\u009a\u06ca\13\u009a\3\u009b\3\u009b\3\u009c")
        buf.write("\3\u009c\3\u009c\3\u009c\3\u009c\7\u009c\u06d3\n\u009c")
        buf.write("\f\u009c\16\u009c\u06d6\13\u009c\3\u009c\3\u009c\3\u009d")
        buf.write("\3\u009d\3\u009d\3\u009d\5\u009d\u06de\n\u009d\3\u009e")
        buf.write("\3\u009e\3\u009f\3\u009f\3\u00a0\3\u00a0\3\u00a1\3\u00a1")
        buf.write("\3\u00a1\3\u00a1\7\u00a1\u06ea\n\u00a1\f\u00a1\16\u00a1")
        buf.write("\u06ed\13\u00a1\3\u00a2\3\u00a2\3\u00a2\3\u00a2\5\u00a2")
        buf.write("\u06f3\n\u00a2\3\u00a3\3\u00a3\3\u00a4\3\u00a4\3\u00a5")
        buf.write("\3\u00a5\3\u00a5\3\u00a5\3\u00a5\6\u00a5\u06fe\n\u00a5")
        buf.write("\r\u00a5\16\u00a5\u06ff\3\u00a6\3\u00a6\3\u00a6\3\u00a6")
        buf.write("\3\u00a6\3\u00a7\3\u00a7\3\u00a8\3\u00a8\3\u00a8\3\u00a8")
        buf.write("\3\u00a8\3\u00a9\3\u00a9\3\u00a9\7\u00a9\u0711\n\u00a9")
        buf.write("\f\u00a9\16\u00a9\u0714\13\u00a9\3\u00aa\3\u00aa\3\u00aa")
        buf.write("\3\u00ab\3\u00ab\3\u00ab\3\u00ac\3\u00ac\3\u00ac\3\u00ac")
        buf.write("\3\u00ac\5\u00ac\u0721\n\u00ac\3\u00ad\3\u00ad\3\u00ae")
        buf.write("\3\u00ae\3\u00ae\3\u00ae\3\u00ae\3\u00af\3\u00af\3\u00af")
        buf.write("\3\u00af\3\u00af\3\u00b0\3\u00b0\3\u00b1\3\u00b1\3\u00b1")
        buf.write("\3\u00b2\3\u00b2\3\u00b2\3\u00b3\3\u00b3\3\u00b3\3\u00b4")
        buf.write("\3\u00b4\3\u00b4\3\u00b5\3\u00b5\3\u00b5\3\u00b5\3\u00b5")
        buf.write("\3\u00b6\3\u00b6\3\u00b7\3\u00b7\7\u00b7\u0746\n\u00b7")
        buf.write("\f\u00b7\16\u00b7\u0749\13\u00b7\3\u00b7\3\u00b7\7\u00b7")
        buf.write("\u074d\n\u00b7\f\u00b7\16\u00b7\u0750\13\u00b7\3\u00b8")
        buf.write("\3\u00b8\5\u00b8\u0754\n\u00b8\3\u00b8\3\u00b8\5\u00b8")
        buf.write("\u0758\n\u00b8\3\u00b8\3\u00b8\5\u00b8\u075c\n\u00b8\3")
        buf.write("\u00b8\3\u00b8\5\u00b8\u0760\n\u00b8\5\u00b8\u0762\n\u00b8")
        buf.write("\3\u00b8\3\u00b8\5\u00b8\u0766\n\u00b8\3\u00b9\3\u00b9")
        buf.write("\3\u00b9\5\u00b9\u076b\n\u00b9\3\u00b9\3\u00b9\3\u00b9")
        buf.write("\3\u00b9\3\u00ba\3\u00ba\3\u00ba\3\u00bb\3\u00bb\3\u00bc")
        buf.write("\3\u00bc\5\u00bc\u0778\n\u00bc\3\u00bd\3\u00bd\3\u00bd")
        buf.write("\7\u00bd\u077d\n\u00bd\f\u00bd\16\u00bd\u0780\13\u00bd")
        buf.write("\3\u00be\3\u00be\3\u00be\3\u00be\3\u00be\6\u00be\u0787")
        buf.write("\n\u00be\r\u00be\16\u00be\u0788\3\u00bf\5\u00bf\u078c")
        buf.write("\n\u00bf\3\u00bf\3\u00bf\3\u00c0\3\u00c0\3\u00c0\6\u00c0")
        buf.write("\u0793\n\u00c0\r\u00c0\16\u00c0\u0794\3\u00c1\3\u00c1")
        buf.write("\3\u00c1\3\u00c1\3\u00c2\3\u00c2\5\u00c2\u079d\n\u00c2")
        buf.write("\3\u00c3\3\u00c3\3\u00c3\6\u00c3\u07a2\n\u00c3\r\u00c3")
        buf.write("\16\u00c3\u07a3\3\u00c3\5\u00c3\u07a7\n\u00c3\5\u00c3")
        buf.write("\u07a9\n\u00c3\3\u00c4\3\u00c4\3\u00c5\7\u00c5\u07ae\n")
        buf.write("\u00c5\f\u00c5\16\u00c5\u07b1\13\u00c5\3\u00c5\7\u00c5")
        buf.write("\u07b4\n\u00c5\f\u00c5\16\u00c5\u07b7\13\u00c5\3\u00c5")
        buf.write("\5\u00c5\u07ba\n\u00c5\3\u00c5\7\u00c5\u07bd\n\u00c5\f")
        buf.write("\u00c5\16\u00c5\u07c0\13\u00c5\3\u00c5\7\u00c5\u07c3\n")
        buf.write("\u00c5\f\u00c5\16\u00c5\u07c6\13\u00c5\3\u00c6\3\u00c6")
        buf.write("\3\u00c7\3\u00c7\3\u00c7\3\u00c7\6\u00c7\u07ce\n\u00c7")
        buf.write("\r\u00c7\16\u00c7\u07cf\3\u00c7\5\u00c7\u07d3\n\u00c7")
        buf.write("\3\u00c8\3\u00c8\3\u00c9\3\u00c9\3\u00ca\3\u00ca\3\u00ca")
        buf.write("\5\u00ca\u07dc\n\u00ca\3\u00ca\3\u00ca\5\u00ca\u07e0\n")
        buf.write("\u00ca\3\u00ca\6\u00ca\u07e3\n\u00ca\r\u00ca\16\u00ca")
        buf.write("\u07e4\3\u00ca\5\u00ca\u07e8\n\u00ca\3\u00cb\3\u00cb\3")
        buf.write("\u00cc\3\u00cc\3\u00cc\7\u00cc\u07ef\n\u00cc\f\u00cc\16")
        buf.write("\u00cc\u07f2\13\u00cc\3\u00cd\5\u00cd\u07f5\n\u00cd\3")
        buf.write("\u00cd\3\u00cd\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce")
        buf.write("\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce")
        buf.write("\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce\5\u00ce\u080a")
        buf.write("\n\u00ce\3\u00cf\3\u00cf\3\u00cf\3\u00cf\6\u00cf\u0810")
        buf.write("\n\u00cf\r\u00cf\16\u00cf\u0811\3\u00cf\3\u00cf\3\u00d0")
        buf.write("\3\u00d0\5\u00d0\u0818\n\u00d0\3\u00d0\5\u00d0\u081b\n")
        buf.write("\u00d0\3\u00d0\5\u00d0\u081e\n\u00d0\3\u00d0\5\u00d0\u0821")
        buf.write("\n\u00d0\3\u00d1\3\u00d1\5\u00d1\u0825\n\u00d1\3\u00d2")
        buf.write("\3\u00d2\3\u00d3\3\u00d3\3\u00d3\3\u00d3\3\u00d3\3\u00d3")
        buf.write("\7\u00d3\u082f\n\u00d3\f\u00d3\16\u00d3\u0832\13\u00d3")
        buf.write("\5\u00d3\u0834\n\u00d3\3\u00d4\3\u00d4\3\u00d5\3\u00d5")
        buf.write("\3\u00d5\5\u00d5\u083b\n\u00d5\3\u00d5\3\u00d5\5\u00d5")
        buf.write("\u083f\n\u00d5\3\u00d5\5\u00d5\u0842\n\u00d5\3\u00d6\3")
        buf.write("\u00d6\3\u00d7\3\u00d7\3\u00d8\3\u00d8\3\u00d8\3\u00d8")
        buf.write("\3\u00d9\3\u00d9\3\u00d9\5\u00d9\u084f\n\u00d9\3\u00d9")
        buf.write("\3\u00d9\3\u00da\3\u00da\3\u00db\3\u00db\3\u00db\5\u00db")
        buf.write("\u0858\n\u00db\3\u00db\3\u00db\3\u00dc\3\u00dc\3\u00dd")
        buf.write("\3\u00dd\3\u00dd\3\u00de\3\u00de\3\u00de\3\u00df\3\u00df")
        buf.write("\5\u00df\u0866\n\u00df\3\u00df\3\u00df\7\u00df\u086a\n")
        buf.write("\u00df\f\u00df\16\u00df\u086d\13\u00df\3\u00df\3\u00df")
        buf.write("\5\u00df\u0871\n\u00df\3\u00df\3\u00df\3\u00df\3\u00df")
        buf.write("\3\u00df\3\u00df\3\u00df\3\u00df\3\u00df\3\u00df\3\u00df")
        buf.write("\3\u00df\3\u00df\3\u00df\3\u00df\7\u00df\u0882\n\u00df")
        buf.write("\f\u00df\16\u00df\u0885\13\u00df\3\u00df\7\u00df\u0888")
        buf.write("\n\u00df\f\u00df\16\u00df\u088b\13\u00df\3\u00df\3\u00df")
        buf.write("\5\u00df\u088f\n\u00df\3\u00df\7\u00df\u0892\n\u00df\f")
        buf.write("\u00df\16\u00df\u0895\13\u00df\3\u00df\7\u00df\u0898\n")
        buf.write("\u00df\f\u00df\16\u00df\u089b\13\u00df\3\u00df\7\u00df")
        buf.write("\u089e\n\u00df\f\u00df\16\u00df\u08a1\13\u00df\3\u00df")
        buf.write("\3\u00df\3\u00e0\3\u00e0\7\u00e0\u08a7\n\u00e0\f\u00e0")
        buf.write("\16\u00e0\u08aa\13\u00e0\3\u00e0\3\u00e0\7\u00e0\u08ae")
        buf.write("\n\u00e0\f\u00e0\16\u00e0\u08b1\13\u00e0\3\u00e0\3\u00e0")
        buf.write("\7\u00e0\u08b5\n\u00e0\f\u00e0\16\u00e0\u08b8\13\u00e0")
        buf.write("\3\u00e0\3\u00e0\7\u00e0\u08bc\n\u00e0\f\u00e0\16\u00e0")
        buf.write("\u08bf\13\u00e0\3\u00e1\3\u00e1\3\u00e2\3\u00e2\3\u00e2")
        buf.write("\3\u00e2\5\u00e2\u08c7\n\u00e2\3\u00e2\3\u00e2\3\u00e2")
        buf.write("\3\u00e2\3\u00e3\3\u00e3\3\u00e4\3\u00e4\3\u00e4\3\u00e4")
        buf.write("\5\u00e4\u08d3\n\u00e4\3\u00e4\3\u00e4\3\u00e4\3\u00e4")
        buf.write("\3\u00e5\3\u00e5\3\u00e6\3\u00e6\5\u00e6\u08dd\n\u00e6")
        buf.write("\3\u00e7\3\u00e7\3\u00e8\3\u00e8\3\u00e8\3\u00e8\3\u00e9")
        buf.write("\3\u00e9\3\u00e9\3\u00e9\3\u00ea\3\u00ea\3\u00eb\3\u00eb")
        buf.write("\3\u00eb\3\u00eb\3\u00ec\3\u00ec\3\u00ed\3\u00ed\3\u00ed")
        buf.write("\3\u00ed\3\u00ee\3\u00ee\3\u00ee\3\u00ee\5\u00ee\u08f9")
        buf.write("\n\u00ee\3\u00ef\3\u00ef\3\u00ef\3\u00ef\5\u00ef\u08ff")
        buf.write("\n\u00ef\3\u00f0\3\u00f0\3\u00f0\3\u00f0\3\u00f1\3\u00f1")
        buf.write("\3\u00f1\3\u00f1\3\u00f2\3\u00f2\3\u00f2\3\u00f2\3\u00f3")
        buf.write("\3\u00f3\3\u00f3\7\u00f3\u0910\n\u00f3\f\u00f3\16\u00f3")
        buf.write("\u0913\13\u00f3\3\u00f4\3\u00f4\3\u00f5\3\u00f5\3\u00f5")
        buf.write("\3\u00f5\3\u00f6\3\u00f6\3\u00f6\3\u00f6\3\u00f7\3\u00f7")
        buf.write("\3\u00f8\3\u00f8\3\u00f8\3\u00f8\3\u00f9\3\u00f9\3\u00fa")
        buf.write("\3\u00fa\3\u00fa\7\u00fa\u092a\n\u00fa\f\u00fa\16\u00fa")
        buf.write("\u092d\13\u00fa\3\u00fb\3\u00fb\5\u00fb\u0931\n\u00fb")
        buf.write("\3\u00fc\3\u00fc\5\u00fc\u0935\n\u00fc\3\u00fc\5\u00fc")
        buf.write("\u0938\n\u00fc\3\u00fd\3\u00fd\3\u00fe\3\u00fe\3\u00fe")
        buf.write("\3\u00fe\3\u00ff\3\u00ff\3\u00ff\7\u00ff\u0943\n\u00ff")
        buf.write("\f\u00ff\16\u00ff\u0946\13\u00ff\3\u0100\3\u0100\3\u0101")
        buf.write("\3\u0101\5\u0101\u094c\n\u0101\3\u0101\5\u0101\u094f\n")
        buf.write("\u0101\3\u0102\3\u0102\5\u0102\u0953\n\u0102\3\u0103\3")
        buf.write("\u0103\5\u0103\u0957\n\u0103\3\u0104\3\u0104\3\u0104\3")
        buf.write("\u0105\3\u0105\3\u0105\3\u0106\3\u0106\3\u0106\3\u0107")
        buf.write("\3\u0107\3\u0107\3\u0107\3\u0107\7\u0107\u0967\n\u0107")
        buf.write("\f\u0107\16\u0107\u096a\13\u0107\3\u0107\6\u0107\u096d")
        buf.write("\n\u0107\r\u0107\16\u0107\u096e\3\u0107\7\u0107\u0972")
        buf.write("\n\u0107\f\u0107\16\u0107\u0975\13\u0107\3\u0107\3\u0107")
        buf.write("\3\u0108\3\u0108\3\u0109\5\u0109\u097c\n\u0109\3\u0109")
        buf.write("\7\u0109\u097f\n\u0109\f\u0109\16\u0109\u0982\13\u0109")
        buf.write("\3\u0109\5\u0109\u0985\n\u0109\3\u0109\3\u0109\3\u0109")
        buf.write("\5\u0109\u098a\n\u0109\3\u0109\7\u0109\u098d\n\u0109\f")
        buf.write("\u0109\16\u0109\u0990\13\u0109\3\u010a\3\u010a\3\u010a")
        buf.write("\5\u010a\u0995\n\u010a\3\u010b\3\u010b\3\u010c\3\u010c")
        buf.write("\3\u010c\3\u010c\7\u010c\u099d\n\u010c\f\u010c\16\u010c")
        buf.write("\u09a0\13\u010c\3\u010c\3\u010c\3\u010d\3\u010d\3\u010d")
        buf.write("\3\u010d\3\u010e\3\u010e\3\u010f\3\u010f\3\u010f\5\u010f")
        buf.write("\u09ad\n\u010f\3\u0110\3\u0110\3\u0111\3\u0111\3\u0111")
        buf.write("\3\u0111\3\u0111\3\u0112\3\u0112\3\u0112\5\u0112\u09b9")
        buf.write("\n\u0112\3\u0112\3\u0112\3\u0113\3\u0113\3\u0113\5\u0113")
        buf.write("\u09c0\n\u0113\3\u0114\3\u0114\3\u0114\3\u0115\3\u0115")
        buf.write("\3\u0116\3\u0116\5\u0116\u09c9\n\u0116\3\u0117\3\u0117")
        buf.write("\3\u0117\3\u0117\3\u0117\3\u0118\3\u0118\3\u0118\2\2\u0119")
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
        buf.write("\u0222\u0224\u0226\u0228\u022a\u022c\u022e\2\23\4\2,w")
        buf.write("yy\3\2\u0092\u0093\4\2\u008b\u008b\u0090\u0090\3\2\u0092")
        buf.write("\u0092\3\2\u0099\u009a\3\2\u008b\u0090\4\2zz\u0084\u0084")
        buf.write("\5\288::==\3\2BD\4\2\u008e\u008e\u0090\u0090\3\2`b\3\2")
        buf.write(",.\4\2\u0086\u0086\u0090\u0090\4\2\u0088\u0088\u008c\u008c")
        buf.write("\3\2\r\17\3\2WY\4\2WZnn\2\u0a33\2\u0233\3\2\2\2\4\u0265")
        buf.write("\3\2\2\2\6\u026a\3\2\2\2\b\u026e\3\2\2\2\n\u0270\3\2\2")
        buf.write("\2\f\u0274\3\2\2\2\16\u027e\3\2\2\2\20\u0282\3\2\2\2\22")
        buf.write("\u0290\3\2\2\2\24\u0292\3\2\2\2\26\u0294\3\2\2\2\30\u0296")
        buf.write("\3\2\2\2\32\u0298\3\2\2\2\34\u029a\3\2\2\2\36\u02a2\3")
        buf.write("\2\2\2 \u02c1\3\2\2\2\"\u02c4\3\2\2\2$\u02ca\3\2\2\2&")
        buf.write("\u02d0\3\2\2\2(\u02d2\3\2\2\2*\u02d6\3\2\2\2,\u02e2\3")
        buf.write("\2\2\2.\u02e4\3\2\2\2\60\u02eb\3\2\2\2\62\u02ed\3\2\2")
        buf.write("\2\64\u02f2\3\2\2\2\66\u02f7\3\2\2\28\u02fc\3\2\2\2:\u0301")
        buf.write("\3\2\2\2<\u031f\3\2\2\2>\u0321\3\2\2\2@\u0343\3\2\2\2")
        buf.write("B\u0360\3\2\2\2D\u037d\3\2\2\2F\u037f\3\2\2\2H\u03b5\3")
        buf.write("\2\2\2J\u03bc\3\2\2\2L\u03c4\3\2\2\2N\u03cc\3\2\2\2P\u03d3")
        buf.write("\3\2\2\2R\u03da\3\2\2\2T\u03e0\3\2\2\2V\u03e2\3\2\2\2")
        buf.write("X\u03e6\3\2\2\2Z\u03e8\3\2\2\2\\\u03f3\3\2\2\2^\u03f8")
        buf.write("\3\2\2\2`\u03fa\3\2\2\2b\u03ff\3\2\2\2d\u0407\3\2\2\2")
        buf.write("f\u0429\3\2\2\2h\u0433\3\2\2\2j\u043e\3\2\2\2l\u0446\3")
        buf.write("\2\2\2n\u044f\3\2\2\2p\u0451\3\2\2\2r\u0458\3\2\2\2t\u045d")
        buf.write("\3\2\2\2v\u047e\3\2\2\2x\u0480\3\2\2\2z\u0483\3\2\2\2")
        buf.write("|\u0487\3\2\2\2~\u048a\3\2\2\2\u0080\u048c\3\2\2\2\u0082")
        buf.write("\u048f\3\2\2\2\u0084\u0491\3\2\2\2\u0086\u049a\3\2\2\2")
        buf.write("\u0088\u049c\3\2\2\2\u008a\u049f\3\2\2\2\u008c\u04a2\3")
        buf.write("\2\2\2\u008e\u04a4\3\2\2\2\u0090\u04b8\3\2\2\2\u0092\u04ba")
        buf.write("\3\2\2\2\u0094\u04bc\3\2\2\2\u0096\u04be\3\2\2\2\u0098")
        buf.write("\u04c0\3\2\2\2\u009a\u04c2\3\2\2\2\u009c\u04c4\3\2\2\2")
        buf.write("\u009e\u04c6\3\2\2\2\u00a0\u04c8\3\2\2\2\u00a2\u04ca\3")
        buf.write("\2\2\2\u00a4\u04cc\3\2\2\2\u00a6\u04ce\3\2\2\2\u00a8\u04d0")
        buf.write("\3\2\2\2\u00aa\u04d2\3\2\2\2\u00ac\u04dd\3\2\2\2\u00ae")
        buf.write("\u04df\3\2\2\2\u00b0\u04ea\3\2\2\2\u00b2\u04f1\3\2\2\2")
        buf.write("\u00b4\u04f3\3\2\2\2\u00b6\u04f6\3\2\2\2\u00b8\u04fd\3")
        buf.write("\2\2\2\u00ba\u0508\3\2\2\2\u00bc\u050f\3\2\2\2\u00be\u0511")
        buf.write("\3\2\2\2\u00c0\u0514\3\2\2\2\u00c2\u0519\3\2\2\2\u00c4")
        buf.write("\u0521\3\2\2\2\u00c6\u0523\3\2\2\2\u00c8\u052a\3\2\2\2")
        buf.write("\u00ca\u052c\3\2\2\2\u00cc\u0533\3\2\2\2\u00ce\u0535\3")
        buf.write("\2\2\2\u00d0\u053d\3\2\2\2\u00d2\u0541\3\2\2\2\u00d4\u0543")
        buf.write("\3\2\2\2\u00d6\u0549\3\2\2\2\u00d8\u054c\3\2\2\2\u00da")
        buf.write("\u054f\3\2\2\2\u00dc\u055d\3\2\2\2\u00de\u055f\3\2\2\2")
        buf.write("\u00e0\u0561\3\2\2\2\u00e2\u0563\3\2\2\2\u00e4\u0565\3")
        buf.write("\2\2\2\u00e6\u0578\3\2\2\2\u00e8\u057a\3\2\2\2\u00ea\u059c")
        buf.write("\3\2\2\2\u00ec\u05b2\3\2\2\2\u00ee\u05bc\3\2\2\2\u00f0")
        buf.write("\u05be\3\2\2\2\u00f2\u05c0\3\2\2\2\u00f4\u05ca\3\2\2\2")
        buf.write("\u00f6\u05d9\3\2\2\2\u00f8\u05db\3\2\2\2\u00fa\u05df\3")
        buf.write("\2\2\2\u00fc\u05e1\3\2\2\2\u00fe\u05e5\3\2\2\2\u0100\u05e9")
        buf.write("\3\2\2\2\u0102\u05f3\3\2\2\2\u0104\u05fb\3\2\2\2\u0106")
        buf.write("\u05fd\3\2\2\2\u0108\u05ff\3\2\2\2\u010a\u0608\3\2\2\2")
        buf.write("\u010c\u0611\3\2\2\2\u010e\u061a\3\2\2\2\u0110\u0623\3")
        buf.write("\2\2\2\u0112\u062c\3\2\2\2\u0114\u0635\3\2\2\2\u0116\u0646")
        buf.write("\3\2\2\2\u0118\u0648\3\2\2\2\u011a\u064a\3\2\2\2\u011c")
        buf.write("\u0655\3\2\2\2\u011e\u066d\3\2\2\2\u0120\u0670\3\2\2\2")
        buf.write("\u0122\u0672\3\2\2\2\u0124\u067b\3\2\2\2\u0126\u0684\3")
        buf.write("\2\2\2\u0128\u068c\3\2\2\2\u012a\u0697\3\2\2\2\u012c\u06a2")
        buf.write("\3\2\2\2\u012e\u06ad\3\2\2\2\u0130\u06b6\3\2\2\2\u0132")
        buf.write("\u06bf\3\2\2\2\u0134\u06cb\3\2\2\2\u0136\u06cd\3\2\2\2")
        buf.write("\u0138\u06d9\3\2\2\2\u013a\u06df\3\2\2\2\u013c\u06e1\3")
        buf.write("\2\2\2\u013e\u06e3\3\2\2\2\u0140\u06e5\3\2\2\2\u0142\u06ee")
        buf.write("\3\2\2\2\u0144\u06f4\3\2\2\2\u0146\u06f6\3\2\2\2\u0148")
        buf.write("\u06f8\3\2\2\2\u014a\u0701\3\2\2\2\u014c\u0706\3\2\2\2")
        buf.write("\u014e\u0708\3\2\2\2\u0150\u070d\3\2\2\2\u0152\u0715\3")
        buf.write("\2\2\2\u0154\u0718\3\2\2\2\u0156\u071b\3\2\2\2\u0158\u0722")
        buf.write("\3\2\2\2\u015a\u0724\3\2\2\2\u015c\u0729\3\2\2\2\u015e")
        buf.write("\u072e\3\2\2\2\u0160\u0730\3\2\2\2\u0162\u0733\3\2\2\2")
        buf.write("\u0164\u0736\3\2\2\2\u0166\u0739\3\2\2\2\u0168\u073c\3")
        buf.write("\2\2\2\u016a\u0741\3\2\2\2\u016c\u0743\3\2\2\2\u016e\u0751")
        buf.write("\3\2\2\2\u0170\u076a\3\2\2\2\u0172\u0770\3\2\2\2\u0174")
        buf.write("\u0773\3\2\2\2\u0176\u0777\3\2\2\2\u0178\u0779\3\2\2\2")
        buf.write("\u017a\u0786\3\2\2\2\u017c\u078b\3\2\2\2\u017e\u0792\3")
        buf.write("\2\2\2\u0180\u0796\3\2\2\2\u0182\u079c\3\2\2\2\u0184\u07a8")
        buf.write("\3\2\2\2\u0186\u07aa\3\2\2\2\u0188\u07af\3\2\2\2\u018a")
        buf.write("\u07c7\3\2\2\2\u018c\u07c9\3\2\2\2\u018e\u07d4\3\2\2\2")
        buf.write("\u0190\u07d6\3\2\2\2\u0192\u07d8\3\2\2\2\u0194\u07e9\3")
        buf.write("\2\2\2\u0196\u07eb\3\2\2\2\u0198\u07f4\3\2\2\2\u019a\u0809")
        buf.write("\3\2\2\2\u019c\u080b\3\2\2\2\u019e\u0815\3\2\2\2\u01a0")
        buf.write("\u0824\3\2\2\2\u01a2\u0826\3\2\2\2\u01a4\u0828\3\2\2\2")
        buf.write("\u01a6\u0835\3\2\2\2\u01a8\u0837\3\2\2\2\u01aa\u0843\3")
        buf.write("\2\2\2\u01ac\u0845\3\2\2\2\u01ae\u0847\3\2\2\2\u01b0\u084b")
        buf.write("\3\2\2\2\u01b2\u0852\3\2\2\2\u01b4\u0854\3\2\2\2\u01b6")
        buf.write("\u085b\3\2\2\2\u01b8\u085d\3\2\2\2\u01ba\u0860\3\2\2\2")
        buf.write("\u01bc\u0865\3\2\2\2\u01be\u08a4\3\2\2\2\u01c0\u08c0\3")
        buf.write("\2\2\2\u01c2\u08c6\3\2\2\2\u01c4\u08cc\3\2\2\2\u01c6\u08d2")
        buf.write("\3\2\2\2\u01c8\u08d8\3\2\2\2\u01ca\u08dc\3\2\2\2\u01cc")
        buf.write("\u08de\3\2\2\2\u01ce\u08e0\3\2\2\2\u01d0\u08e4\3\2\2\2")
        buf.write("\u01d2\u08e8\3\2\2\2\u01d4\u08ea\3\2\2\2\u01d6\u08ee\3")
        buf.write("\2\2\2\u01d8\u08f0\3\2\2\2\u01da\u08f4\3\2\2\2\u01dc\u08fa")
        buf.write("\3\2\2\2\u01de\u0900\3\2\2\2\u01e0\u0904\3\2\2\2\u01e2")
        buf.write("\u0908\3\2\2\2\u01e4\u090c\3\2\2\2\u01e6\u0914\3\2\2\2")
        buf.write("\u01e8\u0916\3\2\2\2\u01ea\u091a\3\2\2\2\u01ec\u091e\3")
        buf.write("\2\2\2\u01ee\u0920\3\2\2\2\u01f0\u0924\3\2\2\2\u01f2\u0926")
        buf.write("\3\2\2\2\u01f4\u092e\3\2\2\2\u01f6\u0937\3\2\2\2\u01f8")
        buf.write("\u0939\3\2\2\2\u01fa\u093b\3\2\2\2\u01fc\u093f\3\2\2\2")
        buf.write("\u01fe\u0947\3\2\2\2\u0200\u094e\3\2\2\2\u0202\u0950\3")
        buf.write("\2\2\2\u0204\u0954\3\2\2\2\u0206\u0958\3\2\2\2\u0208\u095b")
        buf.write("\3\2\2\2\u020a\u095e\3\2\2\2\u020c\u0961\3\2\2\2\u020e")
        buf.write("\u0978\3\2\2\2\u0210\u097b\3\2\2\2\u0212\u0991\3\2\2\2")
        buf.write("\u0214\u0996\3\2\2\2\u0216\u0998\3\2\2\2\u0218\u09a3\3")
        buf.write("\2\2\2\u021a\u09a7\3\2\2\2\u021c\u09ac\3\2\2\2\u021e\u09ae")
        buf.write("\3\2\2\2\u0220\u09b0\3\2\2\2\u0222\u09b8\3\2\2\2\u0224")
        buf.write("\u09bf\3\2\2\2\u0226\u09c1\3\2\2\2\u0228\u09c4\3\2\2\2")
        buf.write("\u022a\u09c6\3\2\2\2\u022c\u09ca\3\2\2\2\u022e\u09cf\3")
        buf.write("\2\2\2\u0230\u0232\7x\2\2\u0231\u0230\3\2\2\2\u0232\u0235")
        buf.write("\3\2\2\2\u0233\u0231\3\2\2\2\u0233\u0234\3\2\2\2\u0234")
        buf.write("\u0239\3\2\2\2\u0235\u0233\3\2\2\2\u0236\u0238\5,\27\2")
        buf.write("\u0237\u0236\3\2\2\2\u0238\u023b\3\2\2\2\u0239\u0237\3")
        buf.write("\2\2\2\u0239\u023a\3\2\2\2\u023a\u023f\3\2\2\2\u023b\u0239")
        buf.write("\3\2\2\2\u023c\u023e\7x\2\2\u023d\u023c\3\2\2\2\u023e")
        buf.write("\u0241\3\2\2\2\u023f\u023d\3\2\2\2\u023f\u0240\3\2\2\2")
        buf.write("\u0240\u024a\3\2\2\2\u0241\u023f\3\2\2\2\u0242\u0244\5")
        buf.write("\4\3\2\u0243\u0242\3\2\2\2\u0243\u0244\3\2\2\2\u0244\u0246")
        buf.write("\3\2\2\2\u0245\u0247\5\u016c\u00b7\2\u0246\u0245\3\2\2")
        buf.write("\2\u0247\u0248\3\2\2\2\u0248\u0246\3\2\2\2\u0248\u0249")
        buf.write("\3\2\2\2\u0249\u024b\3\2\2\2\u024a\u0243\3\2\2\2\u024a")
        buf.write("\u024b\3\2\2\2\u024b\u024f\3\2\2\2\u024c\u024e\7x\2\2")
        buf.write("\u024d\u024c\3\2\2\2\u024e\u0251\3\2\2\2\u024f\u024d\3")
        buf.write("\2\2\2\u024f\u0250\3\2\2\2\u0250\u025a\3\2\2\2\u0251\u024f")
        buf.write("\3\2\2\2\u0252\u0254\5\6\4\2\u0253\u0252\3\2\2\2\u0253")
        buf.write("\u0254\3\2\2\2\u0254\u0256\3\2\2\2\u0255\u0257\5d\63\2")
        buf.write("\u0256\u0255\3\2\2\2\u0257\u0258\3\2\2\2\u0258\u0256\3")
        buf.write("\2\2\2\u0258\u0259\3\2\2\2\u0259\u025b\3\2\2\2\u025a\u0253")
        buf.write("\3\2\2\2\u025a\u025b\3\2\2\2\u025b\u025f\3\2\2\2\u025c")
        buf.write("\u025e\7x\2\2\u025d\u025c\3\2\2\2\u025e\u0261\3\2\2\2")
        buf.write("\u025f\u025d\3\2\2\2\u025f\u0260\3\2\2\2\u0260\u0262\3")
        buf.write("\2\2\2\u0261\u025f\3\2\2\2\u0262\u0263\7\2\2\3\u0263\3")
        buf.write("\3\2\2\2\u0264\u0266\5\b\5\2\u0265\u0264\3\2\2\2\u0266")
        buf.write("\u0267\3\2\2\2\u0267\u0265\3\2\2\2\u0267\u0268\3\2\2\2")
        buf.write("\u0268\5\3\2\2\2\u0269\u026b\5\n\6\2\u026a\u0269\3\2\2")
        buf.write("\2\u026b\u026c\3\2\2\2\u026c\u026a\3\2\2\2\u026c\u026d")
        buf.write("\3\2\2\2\u026d\7\3\2\2\2\u026e\u026f\5\f\7\2\u026f\t\3")
        buf.write("\2\2\2\u0270\u0271\5\f\7\2\u0271\13\3\2\2\2\u0272\u0273")
        buf.write("\7\\\2\2\u0273\u0275\5\16\b\2\u0274\u0272\3\2\2\2\u0274")
        buf.write("\u0275\3\2\2\2\u0275\u0276\3\2\2\2\u0276\u0277\7t\2\2")
        buf.write("\u0277\u0279\5\20\t\2\u0278\u027a\7x\2\2\u0279\u0278\3")
        buf.write("\2\2\2\u027a\u027b\3\2\2\2\u027b\u0279\3\2\2\2\u027b\u027c")
        buf.write("\3\2\2\2\u027c\r\3\2\2\2\u027d\u027f\7\u0088\2\2\u027e")
        buf.write("\u027d\3\2\2\2\u027e\u027f\3\2\2\2\u027f\u0280\3\2\2\2")
        buf.write("\u0280\u0281\5\34\17\2\u0281\17\3\2\2\2\u0282\u0287\5")
        buf.write("\22\n\2\u0283\u0284\7\u0087\2\2\u0284\u0286\5\22\n\2\u0285")
        buf.write("\u0283\3\2\2\2\u0286\u0289\3\2\2\2\u0287\u0285\3\2\2\2")
        buf.write("\u0287\u0288\3\2\2\2\u0288\21\3\2\2\2\u0289\u0287\3\2")
        buf.write("\2\2\u028a\u028d\5\24\13\2\u028b\u028c\7u\2\2\u028c\u028e")
        buf.write("\5\26\f\2\u028d\u028b\3\2\2\2\u028d\u028e\3\2\2\2\u028e")
        buf.write("\u0291\3\2\2\2\u028f\u0291\5\30\r\2\u0290\u028a\3\2\2")
        buf.write("\2\u0290\u028f\3\2\2\2\u0291\23\3\2\2\2\u0292\u0293\5")
        buf.write("\34\17\2\u0293\25\3\2\2\2\u0294\u0295\5\32\16\2\u0295")
        buf.write("\27\3\2\2\2\u0296\u0297\7\u008f\2\2\u0297\31\3\2\2\2\u0298")
        buf.write("\u0299\t\2\2\2\u0299\33\3\2\2\2\u029a\u029f\5\32\16\2")
        buf.write("\u029b\u029c\7\u0088\2\2\u029c\u029e\5\32\16\2\u029d\u029b")
        buf.write("\3\2\2\2\u029e\u02a1\3\2\2\2\u029f\u029d\3\2\2\2\u029f")
        buf.write("\u02a0\3\2\2\2\u02a0\35\3\2\2\2\u02a1\u029f\3\2\2\2\u02a2")
        buf.write("\u02a6\7\u0089\2\2\u02a3\u02a4\5\32\16\2\u02a4\u02a5\7")
        buf.write("\u0088\2\2\u02a5\u02a7\3\2\2\2\u02a6\u02a3\3\2\2\2\u02a6")
        buf.write("\u02a7\3\2\2\2\u02a7\u02a8\3\2\2\2\u02a8\u02a9\5\32\16")
        buf.write("\2\u02a9\37\3\2\2\2\u02aa\u02ac\7\u0088\2\2\u02ab\u02aa")
        buf.write("\3\2\2\2\u02ab\u02ac\3\2\2\2\u02ac\u02ad\3\2\2\2\u02ad")
        buf.write("\u02b3\7\u008f\2\2\u02ae\u02af\7\u0087\2\2\u02af\u02b0")
        buf.write("\7\177\2\2\u02b0\u02b2\5\"\22\2\u02b1\u02ae\3\2\2\2\u02b2")
        buf.write("\u02b5\3\2\2\2\u02b3\u02b1\3\2\2\2\u02b3\u02b4\3\2\2\2")
        buf.write("\u02b4\u02c2\3\2\2\2\u02b5\u02b3\3\2\2\2\u02b6\u02be\5")
        buf.write("\32\16\2\u02b7\u02b9\7\u0087\2\2\u02b8\u02ba\7\177\2\2")
        buf.write("\u02b9\u02b8\3\2\2\2\u02b9\u02ba\3\2\2\2\u02ba\u02bb\3")
        buf.write("\2\2\2\u02bb\u02bd\5\"\22\2\u02bc\u02b7\3\2\2\2\u02bd")
        buf.write("\u02c0\3\2\2\2\u02be\u02bc\3\2\2\2\u02be\u02bf\3\2\2\2")
        buf.write("\u02bf\u02c2\3\2\2\2\u02c0\u02be\3\2\2\2\u02c1\u02ab\3")
        buf.write("\2\2\2\u02c1\u02b6\3\2\2\2\u02c2!\3\2\2\2\u02c3\u02c5")
        buf.write("\7\u008f\2\2\u02c4\u02c3\3\2\2\2\u02c4\u02c5\3\2\2\2\u02c5")
        buf.write("\u02c6\3\2\2\2\u02c6\u02c8\5\32\16\2\u02c7\u02c9\7\u008f")
        buf.write("\2\2\u02c8\u02c7\3\2\2\2\u02c8\u02c9\3\2\2\2\u02c9#\3")
        buf.write("\2\2\2\u02ca\u02cb\7\u0082\2\2\u02cb\u02cc\7v\2\2\u02cc")
        buf.write("\u02cd\7\u0083\2\2\u02cd%\3\2\2\2\u02ce\u02d1\5*\26\2")
        buf.write("\u02cf\u02d1\5(\25\2\u02d0\u02ce\3\2\2\2\u02d0\u02cf\3")
        buf.write("\2\2\2\u02d1\'\3\2\2\2\u02d2\u02d3\7\u0099\2\2\u02d3\u02d4")
        buf.write("\7\u009d\2\2\u02d4\u02d5\7x\2\2\u02d5)\3\2\2\2\u02d6\u02d7")
        buf.write("\7\u009b\2\2\u02d7+\3\2\2\2\u02d8\u02e3\5.\30\2\u02d9")
        buf.write("\u02e3\5\62\32\2\u02da\u02e3\5\64\33\2\u02db\u02e3\5\66")
        buf.write("\34\2\u02dc\u02e3\58\35\2\u02dd\u02e3\5:\36\2\u02de\u02e3")
        buf.write("\5V,\2\u02df\u02e3\5Z.\2\u02e0\u02e3\5`\61\2\u02e1\u02e3")
        buf.write("\7x\2\2\u02e2\u02d8\3\2\2\2\u02e2\u02d9\3\2\2\2\u02e2")
        buf.write("\u02da\3\2\2\2\u02e2\u02db\3\2\2\2\u02e2\u02dc\3\2\2\2")
        buf.write("\u02e2\u02dd\3\2\2\2\u02e2\u02de\3\2\2\2\u02e2\u02df\3")
        buf.write("\2\2\2\u02e2\u02e0\3\2\2\2\u02e2\u02e1\3\2\2\2\u02e3-")
        buf.write("\3\2\2\2\u02e4\u02e9\7\4\2\2\u02e5\u02e6\7\u0080\2\2\u02e6")
        buf.write("\u02e7\5\60\31\2\u02e7\u02e8\7\u0081\2\2\u02e8\u02ea\3")
        buf.write("\2\2\2\u02e9\u02e5\3\2\2\2\u02e9\u02ea\3\2\2\2\u02ea/")
        buf.write("\3\2\2\2\u02eb\u02ec\t\3\2\2\u02ec\61\3\2\2\2\u02ed\u02f0")
        buf.write("\7\5\2\2\u02ee\u02ef\7\u0080\2\2\u02ef\u02f1\7\u0081\2")
        buf.write("\2\u02f0\u02ee\3\2\2\2\u02f0\u02f1\3\2\2\2\u02f1\63\3")
        buf.write("\2\2\2\u02f2\u02f5\7\7\2\2\u02f3\u02f4\7\u0080\2\2\u02f4")
        buf.write("\u02f6\7\u0081\2\2\u02f5\u02f3\3\2\2\2\u02f5\u02f6\3\2")
        buf.write("\2\2\u02f6\65\3\2\2\2\u02f7\u02fa\7\b\2\2\u02f8\u02f9")
        buf.write("\7\u0080\2\2\u02f9\u02fb\7\u0081\2\2\u02fa\u02f8\3\2\2")
        buf.write("\2\u02fa\u02fb\3\2\2\2\u02fb\67\3\2\2\2\u02fc\u02ff\7")
        buf.write("\13\2\2\u02fd\u02fe\7\u0080\2\2\u02fe\u0300\7\u0081\2")
        buf.write("\2\u02ff\u02fd\3\2\2\2\u02ff\u0300\3\2\2\2\u03009\3\2")
        buf.write("\2\2\u0301\u0302\7\f\2\2\u0302\u0306\7\u0080\2\2\u0303")
        buf.write("\u0305\7x\2\2\u0304\u0303\3\2\2\2\u0305\u0308\3\2\2\2")
        buf.write("\u0306\u0304\3\2\2\2\u0306\u0307\3\2\2\2\u0307\u030a\3")
        buf.write("\2\2\2\u0308\u0306\3\2\2\2\u0309\u030b\5<\37\2\u030a\u0309")
        buf.write("\3\2\2\2\u030a\u030b\3\2\2\2\u030b\u030f\3\2\2\2\u030c")
        buf.write("\u030e\7x\2\2\u030d\u030c\3\2\2\2\u030e\u0311\3\2\2\2")
        buf.write("\u030f\u030d\3\2\2\2\u030f\u0310\3\2\2\2\u0310\u0313\3")
        buf.write("\2\2\2\u0311\u030f\3\2\2\2\u0312\u0314\5F$\2\u0313\u0312")
        buf.write("\3\2\2\2\u0314\u0315\3\2\2\2\u0315\u0313\3\2\2\2\u0315")
        buf.write("\u0316\3\2\2\2\u0316\u031a\3\2\2\2\u0317\u0319\7x\2\2")
        buf.write("\u0318\u0317\3\2\2\2\u0319\u031c\3\2\2\2\u031a\u0318\3")
        buf.write("\2\2\2\u031a\u031b\3\2\2\2\u031b\u031d\3\2\2\2\u031c\u031a")
        buf.write("\3\2\2\2\u031d\u031e\7\u0081\2\2\u031e;\3\2\2\2\u031f")
        buf.write("\u0320\5> \2\u0320=\3\2\2\2\u0321\u0322\7J\2\2\u0322\u0326")
        buf.write("\7\u0080\2\2\u0323\u0325\7x\2\2\u0324\u0323\3\2\2\2\u0325")
        buf.write("\u0328\3\2\2\2\u0326\u0324\3\2\2\2\u0326\u0327\3\2\2\2")
        buf.write("\u0327\u032a\3\2\2\2\u0328\u0326\3\2\2\2\u0329\u032b\5")
        buf.write("@!\2\u032a\u0329\3\2\2\2\u032a\u032b\3\2\2\2\u032b\u032f")
        buf.write("\3\2\2\2\u032c\u032e\7x\2\2\u032d\u032c\3\2\2\2\u032e")
        buf.write("\u0331\3\2\2\2\u032f\u032d\3\2\2\2\u032f\u0330\3\2\2\2")
        buf.write("\u0330\u0338\3\2\2\2\u0331\u032f\3\2\2\2\u0332\u0334\5")
        buf.write("P)\2\u0333\u0335\7\u0087\2\2\u0334\u0333\3\2\2\2\u0334")
        buf.write("\u0335\3\2\2\2\u0335\u0337\3\2\2\2\u0336\u0332\3\2\2\2")
        buf.write("\u0337\u033a\3\2\2\2\u0338\u0336\3\2\2\2\u0338\u0339\3")
        buf.write("\2\2\2\u0339\u033e\3\2\2\2\u033a\u0338\3\2\2\2\u033b\u033d")
        buf.write("\7x\2\2\u033c\u033b\3\2\2\2\u033d\u0340\3\2\2\2\u033e")
        buf.write("\u033c\3\2\2\2\u033e\u033f\3\2\2\2\u033f\u0341\3\2\2\2")
        buf.write("\u0340\u033e\3\2\2\2\u0341\u0342\7\u0081\2\2\u0342?\3")
        buf.write("\2\2\2\u0343\u0344\7I\2\2\u0344\u0348\7\u0080\2\2\u0345")
        buf.write("\u0347\7x\2\2\u0346\u0345\3\2\2\2\u0347\u034a\3\2\2\2")
        buf.write("\u0348\u0346\3\2\2\2\u0348\u0349\3\2\2\2\u0349\u0353\3")
        buf.write("\2\2\2\u034a\u0348\3\2\2\2\u034b\u0350\5B\"\2\u034c\u034d")
        buf.write("\7\u0087\2\2\u034d\u034f\5B\"\2\u034e\u034c\3\2\2\2\u034f")
        buf.write("\u0352\3\2\2\2\u0350\u034e\3\2\2\2\u0350\u0351\3\2\2\2")
        buf.write("\u0351\u0354\3\2\2\2\u0352\u0350\3\2\2\2\u0353\u034b\3")
        buf.write("\2\2\2\u0353\u0354\3\2\2\2\u0354\u0358\3\2\2\2\u0355\u0357")
        buf.write("\7x\2\2\u0356\u0355\3\2\2\2\u0357\u035a\3\2\2\2\u0358")
        buf.write("\u0356\3\2\2\2\u0358\u0359\3\2\2\2\u0359\u035b\3\2\2\2")
        buf.write("\u035a\u0358\3\2\2\2\u035b\u035c\7\u0081\2\2\u035cA\3")
        buf.write("\2\2\2\u035d\u035f\7x\2\2\u035e\u035d\3\2\2\2\u035f\u0362")
        buf.write("\3\2\2\2\u0360\u035e\3\2\2\2\u0360\u0361\3\2\2\2\u0361")
        buf.write("\u0363\3\2\2\2\u0362\u0360\3\2\2\2\u0363\u037b\5D#\2\u0364")
        buf.write("\u0368\7\u0080\2\2\u0365\u0367\7x\2\2\u0366\u0365\3\2")
        buf.write("\2\2\u0367\u036a\3\2\2\2\u0368\u0366\3\2\2\2\u0368\u0369")
        buf.write("\3\2\2\2\u0369\u0371\3\2\2\2\u036a\u0368\3\2\2\2\u036b")
        buf.write("\u036d\5P)\2\u036c\u036e\7\u0087\2\2\u036d\u036c\3\2\2")
        buf.write("\2\u036d\u036e\3\2\2\2\u036e\u0370\3\2\2\2\u036f\u036b")
        buf.write("\3\2\2\2\u0370\u0373\3\2\2\2\u0371\u036f\3\2\2\2\u0371")
        buf.write("\u0372\3\2\2\2\u0372\u0377\3\2\2\2\u0373\u0371\3\2\2\2")
        buf.write("\u0374\u0376\7x\2\2\u0375\u0374\3\2\2\2\u0376\u0379\3")
        buf.write("\2\2\2\u0377\u0375\3\2\2\2\u0377\u0378\3\2\2\2\u0378\u037a")
        buf.write("\3\2\2\2\u0379\u0377\3\2\2\2\u037a\u037c\7\u0081\2\2\u037b")
        buf.write("\u0364\3\2\2\2\u037b\u037c\3\2\2\2\u037cC\3\2\2\2\u037d")
        buf.write("\u037e\5\32\16\2\u037eE\3\2\2\2\u037f\u0383\5J&\2\u0380")
        buf.write("\u0382\7x\2\2\u0381\u0380\3\2\2\2\u0382\u0385\3\2\2\2")
        buf.write("\u0383\u0381\3\2\2\2\u0383\u0384\3\2\2\2\u0384\u0386\3")
        buf.write("\2\2\2\u0385\u0383\3\2\2\2\u0386\u038a\5H%\2\u0387\u0389")
        buf.write("\7x\2\2\u0388\u0387\3\2\2\2\u0389\u038c\3\2\2\2\u038a")
        buf.write("\u0388\3\2\2\2\u038a\u038b\3\2\2\2\u038b\u038d\3\2\2\2")
        buf.write("\u038c\u038a\3\2\2\2\u038d\u038e\5L\'\2\u038e\u0392\7")
        buf.write("\u0080\2\2\u038f\u0391\7x\2\2\u0390\u038f\3\2\2\2\u0391")
        buf.write("\u0394\3\2\2\2\u0392\u0390\3\2\2\2\u0392\u0393\3\2\2\2")
        buf.write("\u0393\u0395\3\2\2\2\u0394\u0392\3\2\2\2\u0395\u03a6\5")
        buf.write("N(\2\u0396\u039a\7~\2\2\u0397\u0399\7x\2\2\u0398\u0397")
        buf.write("\3\2\2\2\u0399\u039c\3\2\2\2\u039a\u0398\3\2\2\2\u039a")
        buf.write("\u039b\3\2\2\2\u039b\u03a3\3\2\2\2\u039c\u039a\3\2\2\2")
        buf.write("\u039d\u039f\5P)\2\u039e\u03a0\7\u0087\2\2\u039f\u039e")
        buf.write("\3\2\2\2\u039f\u03a0\3\2\2\2\u03a0\u03a2\3\2\2\2\u03a1")
        buf.write("\u039d\3\2\2\2\u03a2\u03a5\3\2\2\2\u03a3\u03a1\3\2\2\2")
        buf.write("\u03a3\u03a4\3\2\2\2\u03a4\u03a7\3\2\2\2\u03a5\u03a3\3")
        buf.write("\2\2\2\u03a6\u0396\3\2\2\2\u03a6\u03a7\3\2\2\2\u03a7\u03ab")
        buf.write("\3\2\2\2\u03a8\u03aa\7x\2\2\u03a9\u03a8\3\2\2\2\u03aa")
        buf.write("\u03ad\3\2\2\2\u03ab\u03a9\3\2\2\2\u03ab\u03ac\3\2\2\2")
        buf.write("\u03ac\u03ae\3\2\2\2\u03ad\u03ab\3\2\2\2\u03ae\u03b2\7")
        buf.write("\u0081\2\2\u03af\u03b1\7x\2\2\u03b0\u03af\3\2\2\2\u03b1")
        buf.write("\u03b4\3\2\2\2\u03b2\u03b0\3\2\2\2\u03b2\u03b3\3\2\2\2")
        buf.write("\u03b3G\3\2\2\2\u03b4\u03b2\3\2\2\2\u03b5\u03b6\t\4\2")
        buf.write("\2\u03b6\u03b7\7}\2\2\u03b7I\3\2\2\2\u03b8\u03bd\5\32")
        buf.write("\16\2\u03b9\u03bd\7\u0086\2\2\u03ba\u03bd\7\u008f\2\2")
        buf.write("\u03bb\u03bd\7\u008a\2\2\u03bc\u03b8\3\2\2\2\u03bc\u03b9")
        buf.write("\3\2\2\2\u03bc\u03ba\3\2\2\2\u03bc\u03bb\3\2\2\2\u03bd")
        buf.write("\u03be\3\2\2\2\u03be\u03bc\3\2\2\2\u03be\u03bf\3\2\2\2")
        buf.write("\u03bfK\3\2\2\2\u03c0\u03c5\5\32\16\2\u03c1\u03c5\7\u0086")
        buf.write("\2\2\u03c2\u03c5\7\u008a\2\2\u03c3\u03c5\7\u008f\2\2\u03c4")
        buf.write("\u03c0\3\2\2\2\u03c4\u03c1\3\2\2\2\u03c4\u03c2\3\2\2\2")
        buf.write("\u03c4\u03c3\3\2\2\2\u03c5\u03c6\3\2\2\2\u03c6\u03c4\3")
        buf.write("\2\2\2\u03c6\u03c7\3\2\2\2\u03c7M\3\2\2\2\u03c8\u03cd")
        buf.write("\5\32\16\2\u03c9\u03cd\7\u0086\2\2\u03ca\u03cd\7\u008f")
        buf.write("\2\2\u03cb\u03cd\7\u0088\2\2\u03cc\u03c8\3\2\2\2\u03cc")
        buf.write("\u03c9\3\2\2\2\u03cc\u03ca\3\2\2\2\u03cc\u03cb\3\2\2\2")
        buf.write("\u03cd\u03ce\3\2\2\2\u03ce\u03cc\3\2\2\2\u03ce\u03cf\3")
        buf.write("\2\2\2\u03cfO\3\2\2\2\u03d0\u03d2\7x\2\2\u03d1\u03d0\3")
        buf.write("\2\2\2\u03d2\u03d5\3\2\2\2\u03d3\u03d1\3\2\2\2\u03d3\u03d4")
        buf.write("\3\2\2\2\u03d4\u03d6\3\2\2\2\u03d5\u03d3\3\2\2\2\u03d6")
        buf.write("\u03d7\5R*\2\u03d7\u03d8\7\u008b\2\2\u03d8\u03d9\5T+\2")
        buf.write("\u03d9Q\3\2\2\2\u03da\u03db\5\32\16\2\u03dbS\3\2\2\2\u03dc")
        buf.write("\u03e1\7\u0092\2\2\u03dd\u03e1\7\u0093\2\2\u03de\u03e1")
        buf.write("\7z\2\2\u03df\u03e1\5\32\16\2\u03e0\u03dc\3\2\2\2\u03e0")
        buf.write("\u03dd\3\2\2\2\u03e0\u03de\3\2\2\2\u03e0\u03df\3\2\2\2")
        buf.write("\u03e1U\3\2\2\2\u03e2\u03e3\7\22\2\2\u03e3\u03e4\5X-\2")
        buf.write("\u03e4\u03e5\5&\24\2\u03e5W\3\2\2\2\u03e6\u03e7\t\5\2")
        buf.write("\2\u03e7Y\3\2\2\2\u03e8\u03e9\7\20\2\2\u03e9\u03ea\7\u0080")
        buf.write("\2\2\u03ea\u03ef\5^\60\2\u03eb\u03ec\7\u0087\2\2\u03ec")
        buf.write("\u03ed\7G\2\2\u03ed\u03ee\7\u008b\2\2\u03ee\u03f0\5\\")
        buf.write("/\2\u03ef\u03eb\3\2\2\2\u03ef\u03f0\3\2\2\2\u03f0\u03f1")
        buf.write("\3\2\2\2\u03f1\u03f2\7\u0081\2\2\u03f2[\3\2\2\2\u03f3")
        buf.write("\u03f4\7w\2\2\u03f4]\3\2\2\2\u03f5\u03f9\5\32\16\2\u03f6")
        buf.write("\u03f9\7\u0092\2\2\u03f7\u03f9\7\u0093\2\2\u03f8\u03f5")
        buf.write("\3\2\2\2\u03f8\u03f6\3\2\2\2\u03f8\u03f7\3\2\2\2\u03f9")
        buf.write("_\3\2\2\2\u03fa\u03fb\7+\2\2\u03fb\u03fc\7\u0080\2\2\u03fc")
        buf.write("\u03fd\5b\62\2\u03fd\u03fe\7\u0081\2\2\u03fea\3\2\2\2")
        buf.write("\u03ff\u0404\7y\2\2\u0400\u0401\7\u0087\2\2\u0401\u0403")
        buf.write("\7y\2\2\u0402\u0400\3\2\2\2\u0403\u0406\3\2\2\2\u0404")
        buf.write("\u0402\3\2\2\2\u0404\u0405\3\2\2\2\u0405c\3\2\2\2\u0406")
        buf.write("\u0404\3\2\2\2\u0407\u0409\5h\65\2\u0408\u040a\5f\64\2")
        buf.write("\u0409\u0408\3\2\2\2\u0409\u040a\3\2\2\2\u040a\u040e\3")
        buf.write("\2\2\2\u040b\u040d\7x\2\2\u040c\u040b\3\2\2\2\u040d\u0410")
        buf.write("\3\2\2\2\u040e\u040c\3\2\2\2\u040e\u040f\3\2\2\2\u040f")
        buf.write("\u0414\3\2\2\2\u0410\u040e\3\2\2\2\u0411\u0413\5t;\2\u0412")
        buf.write("\u0411\3\2\2\2\u0413\u0416\3\2\2\2\u0414\u0412\3\2\2\2")
        buf.write("\u0414\u0415\3\2\2\2\u0415\u041a\3\2\2\2\u0416\u0414\3")
        buf.write("\2\2\2\u0417\u0419\7x\2\2\u0418\u0417\3\2\2\2\u0419\u041c")
        buf.write("\3\2\2\2\u041a\u0418\3\2\2\2\u041a\u041b\3\2\2\2\u041b")
        buf.write("\u0420\3\2\2\2\u041c\u041a\3\2\2\2\u041d\u041f\5\u00e6")
        buf.write("t\2\u041e\u041d\3\2\2\2\u041f\u0422\3\2\2\2\u0420\u041e")
        buf.write("\3\2\2\2\u0420\u0421\3\2\2\2\u0421\u0426\3\2\2\2\u0422")
        buf.write("\u0420\3\2\2\2\u0423\u0425\7x\2\2\u0424\u0423\3\2\2\2")
        buf.write("\u0425\u0428\3\2\2\2\u0426\u0424\3\2\2\2\u0426\u0427\3")
        buf.write("\2\2\2\u0427e\3\2\2\2\u0428\u0426\3\2\2\2\u0429\u042a")
        buf.write("\7\u008b\2\2\u042a\u0431\t\3\2\2\u042b\u042d\7x\2\2\u042c")
        buf.write("\u042b\3\2\2\2\u042d\u042e\3\2\2\2\u042e\u042c\3\2\2\2")
        buf.write("\u042e\u042f\3\2\2\2\u042f\u0432\3\2\2\2\u0430\u0432\7")
        buf.write("\2\2\3\u0431\u042c\3\2\2\2\u0431\u0430\3\2\2\2\u0432g")
        buf.write("\3\2\2\2\u0433\u0435\7\u0089\2\2\u0434\u0436\5p9\2\u0435")
        buf.write("\u0434\3\2\2\2\u0435\u0436\3\2\2\2\u0436\u0437\3\2\2\2")
        buf.write("\u0437\u0439\5r:\2\u0438\u043a\5l\67\2\u0439\u0438\3\2")
        buf.write("\2\2\u0439\u043a\3\2\2\2\u043a\u043b\3\2\2\2\u043b\u043c")
        buf.write("\5j\66\2\u043c\u043d\7x\2\2\u043di\3\2\2\2\u043e\u043f")
        buf.write("\7x\2\2\u043f\u0440\7\u0086\2\2\u0440\u0442\7\u0086\2")
        buf.write("\2\u0441\u0443\7\u0086\2\2\u0442\u0441\3\2\2\2\u0443\u0444")
        buf.write("\3\2\2\2\u0444\u0442\3\2\2\2\u0444\u0445\3\2\2\2\u0445")
        buf.write("k\3\2\2\2\u0446\u0447\7~\2\2\u0447\u044a\5n8\2\u0448\u0449")
        buf.write("\7\u008a\2\2\u0449\u044b\5n8\2\u044a\u0448\3\2\2\2\u044a")
        buf.write("\u044b\3\2\2\2\u044bm\3\2\2\2\u044c\u0450\5\32\16\2\u044d")
        buf.write("\u0450\7\u0092\2\2\u044e\u0450\7\u0093\2\2\u044f\u044c")
        buf.write("\3\2\2\2\u044f\u044d\3\2\2\2\u044f\u044e\3\2\2\2\u0450")
        buf.write("o\3\2\2\2\u0451\u0456\5\32\16\2\u0452\u0453\7\u0086\2")
        buf.write("\2\u0453\u0457\7}\2\2\u0454\u0455\7\u0090\2\2\u0455\u0457")
        buf.write("\7}\2\2\u0456\u0452\3\2\2\2\u0456\u0454\3\2\2\2\u0457")
        buf.write("q\3\2\2\2\u0458\u0459\5\32\16\2\u0459s\3\2\2\2\u045a\u045c")
        buf.write("\5\u008eH\2\u045b\u045a\3\2\2\2\u045c\u045f\3\2\2\2\u045d")
        buf.write("\u045b\3\2\2\2\u045d\u045e\3\2\2\2\u045e\u0460\3\2\2\2")
        buf.write("\u045f\u045d\3\2\2\2\u0460\u0462\5\u008cG\2\u0461\u0463")
        buf.write("\5v<\2\u0462\u0461\3\2\2\2\u0462\u0463\3\2\2\2\u0463\u0465")
        buf.write("\3\2\2\2\u0464\u0466\5\u008aF\2\u0465\u0464\3\2\2\2\u0465")
        buf.write("\u0466\3\2\2\2\u0466\u0468\3\2\2\2\u0467\u0469\5\u0088")
        buf.write("E\2\u0468\u0467\3\2\2\2\u0468\u0469\3\2\2\2\u0469\u0470")
        buf.write("\3\2\2\2\u046a\u046c\7x\2\2\u046b\u046a\3\2\2\2\u046c")
        buf.write("\u046d\3\2\2\2\u046d\u046b\3\2\2\2\u046d\u046e\3\2\2\2")
        buf.write("\u046e\u0471\3\2\2\2\u046f\u0471\7\2\2\3\u0470\u046b\3")
        buf.write("\2\2\2\u0470\u046f\3\2\2\2\u0471u\3\2\2\2\u0472\u0474")
        buf.write("\7~\2\2\u0473\u0475\5x=\2\u0474\u0473\3\2\2\2\u0474\u0475")
        buf.write("\3\2\2\2\u0475\u047f\3\2\2\2\u0476\u0477\7~\2\2\u0477")
        buf.write("\u0479\5\u0090I\2\u0478\u047a\5z>\2\u0479\u0478\3\2\2")
        buf.write("\2\u0479\u047a\3\2\2\2\u047a\u047f\3\2\2\2\u047b\u047c")
        buf.write("\7~\2\2\u047c\u047f\5~@\2\u047d\u047f\5\u0080A\2\u047e")
        buf.write("\u0472\3\2\2\2\u047e\u0476\3\2\2\2\u047e\u047b\3\2\2\2")
        buf.write("\u047e\u047d\3\2\2\2\u047fw\3\2\2\2\u0480\u0481\5*\26")
        buf.write("\2\u0481y\3\2\2\2\u0482\u0484\5|?\2\u0483\u0482\3\2\2")
        buf.write("\2\u0483\u0484\3\2\2\2\u0484\u0485\3\2\2\2\u0485\u0486")
        buf.write("\5*\26\2\u0486{\3\2\2\2\u0487\u0488\7\u0088\2\2\u0488")
        buf.write("\u0489\7\u0088\2\2\u0489}\3\2\2\2\u048a\u048b\5\32\16")
        buf.write("\2\u048b\177\3\2\2\2\u048c\u048d\5\u0082B\2\u048d\u048e")
        buf.write("\5\u0084C\2\u048e\u0081\3\2\2\2\u048f\u0490\t\6\2\2\u0490")
        buf.write("\u0083\3\2\2\2\u0491\u0492\7\u009d\2\2\u0492\u0085\3\2")
        buf.write("\2\2\u0493\u0495\5\32\16\2\u0494\u0493\3\2\2\2\u0495\u0496")
        buf.write("\3\2\2\2\u0496\u0494\3\2\2\2\u0496\u0497\3\2\2\2\u0497")
        buf.write("\u049b\3\2\2\2\u0498\u049b\7\u0092\2\2\u0499\u049b\7\u0093")
        buf.write("\2\2\u049a\u0494\3\2\2\2\u049a\u0498\3\2\2\2\u049a\u0499")
        buf.write("\3\2\2\2\u049b\u0087\3\2\2\2\u049c\u049d\7\u0084\2\2\u049d")
        buf.write("\u049e\5\u0086D\2\u049e\u0089\3\2\2\2\u049f\u04a0\7\u008a")
        buf.write("\2\2\u04a0\u04a1\5\u0086D\2\u04a1\u008b\3\2\2\2\u04a2")
        buf.write("\u04a3\5\32\16\2\u04a3\u008d\3\2\2\2\u04a4\u04a5\t\7\2")
        buf.write("\2\u04a5\u008f\3\2\2\2\u04a6\u04b9\5\u0092J\2\u04a7\u04b9")
        buf.write("\5\u0096L\2\u04a8\u04b9\5\u0094K\2\u04a9\u04b9\5\u0098")
        buf.write("M\2\u04aa\u04b9\5\u009aN\2\u04ab\u04b9\5\u009cO\2\u04ac")
        buf.write("\u04b9\5\u009eP\2\u04ad\u04b9\5\u00a0Q\2\u04ae\u04b9\5")
        buf.write("\u00a2R\2\u04af\u04b9\5\u00aaV\2\u04b0\u04b9\5\u00b6\\")
        buf.write("\2\u04b1\u04b9\5\u00c0a\2\u04b2\u04b9\5\u00c6d\2\u04b3")
        buf.write("\u04b9\5\u00dan\2\u04b4\u04b9\5\u00caf\2\u04b5\u04b9\5")
        buf.write("\u00a4S\2\u04b6\u04b9\5\u00a6T\2\u04b7\u04b9\5\u00a8U")
        buf.write("\2\u04b8\u04a6\3\2\2\2\u04b8\u04a7\3\2\2\2\u04b8\u04a8")
        buf.write("\3\2\2\2\u04b8\u04a9\3\2\2\2\u04b8\u04aa\3\2\2\2\u04b8")
        buf.write("\u04ab\3\2\2\2\u04b8\u04ac\3\2\2\2\u04b8\u04ad\3\2\2\2")
        buf.write("\u04b8\u04ae\3\2\2\2\u04b8\u04af\3\2\2\2\u04b8\u04b0\3")
        buf.write("\2\2\2\u04b8\u04b1\3\2\2\2\u04b8\u04b2\3\2\2\2\u04b8\u04b3")
        buf.write("\3\2\2\2\u04b8\u04b4\3\2\2\2\u04b8\u04b5\3\2\2\2\u04b8")
        buf.write("\u04b6\3\2\2\2\u04b8\u04b7\3\2\2\2\u04b9\u0091\3\2\2\2")
        buf.write("\u04ba\u04bb\7/\2\2\u04bb\u0093\3\2\2\2\u04bc\u04bd\7")
        buf.write("\60\2\2\u04bd\u0095\3\2\2\2\u04be\u04bf\7\61\2\2\u04bf")
        buf.write("\u0097\3\2\2\2\u04c0\u04c1\7\62\2\2\u04c1\u0099\3\2\2")
        buf.write("\2\u04c2\u04c3\7\63\2\2\u04c3\u009b\3\2\2\2\u04c4\u04c5")
        buf.write("\7\64\2\2\u04c5\u009d\3\2\2\2\u04c6\u04c7\7\65\2\2\u04c7")
        buf.write("\u009f\3\2\2\2\u04c8\u04c9\7\66\2\2\u04c9\u00a1\3\2\2")
        buf.write("\2\u04ca\u04cb\7\67\2\2\u04cb\u00a3\3\2\2\2\u04cc\u04cd")
        buf.write("\79\2\2\u04cd\u00a5\3\2\2\2\u04ce\u04cf\7;\2\2\u04cf\u00a7")
        buf.write("\3\2\2\2\u04d0\u04d1\7<\2\2\u04d1\u00a9\3\2\2\2\u04d2")
        buf.write("\u04db\7>\2\2\u04d3\u04d4\7\u0080\2\2\u04d4\u04d7\5\u00ac")
        buf.write("W\2\u04d5\u04d6\7\u0087\2\2\u04d6\u04d8\5\u00aeX\2\u04d7")
        buf.write("\u04d5\3\2\2\2\u04d7\u04d8\3\2\2\2\u04d8\u04d9\3\2\2\2")
        buf.write("\u04d9\u04da\7\u0081\2\2\u04da\u04dc\3\2\2\2\u04db\u04d3")
        buf.write("\3\2\2\2\u04db\u04dc\3\2\2\2\u04dc\u00ab\3\2\2\2\u04dd")
        buf.write("\u04de\t\b\2\2\u04de\u00ad\3\2\2\2\u04df\u04e0\7E\2\2")
        buf.write("\u04e0\u04e1\7\u008b\2\2\u04e1\u04e6\5\u00b0Y\2\u04e2")
        buf.write("\u04e3\7\u0087\2\2\u04e3\u04e5\5\u00b0Y\2\u04e4\u04e2")
        buf.write("\3\2\2\2\u04e5\u04e8\3\2\2\2\u04e6\u04e4\3\2\2\2\u04e6")
        buf.write("\u04e7\3\2\2\2\u04e7\u00af\3\2\2\2\u04e8\u04e6\3\2\2\2")
        buf.write("\u04e9\u04eb\5\u00b4[\2\u04ea\u04e9\3\2\2\2\u04ea\u04eb")
        buf.write("\3\2\2\2\u04eb\u04ec\3\2\2\2\u04ec\u04ed\5\u00b2Z\2\u04ed")
        buf.write("\u00b1\3\2\2\2\u04ee\u04f2\5\32\16\2\u04ef\u04f2\7\u0092")
        buf.write("\2\2\u04f0\u04f2\7\u0093\2\2\u04f1\u04ee\3\2\2\2\u04f1")
        buf.write("\u04ef\3\2\2\2\u04f1\u04f0\3\2\2\2\u04f2\u00b3\3\2\2\2")
        buf.write("\u04f3\u04f4\5\32\16\2\u04f4\u04f5\7~\2\2\u04f5\u00b5")
        buf.write("\3\2\2\2\u04f6\u04fb\7?\2\2\u04f7\u04f8\7\u0080\2\2\u04f8")
        buf.write("\u04f9\5\u00b8]\2\u04f9\u04fa\7\u0081\2\2\u04fa\u04fc")
        buf.write("\3\2\2\2\u04fb\u04f7\3\2\2\2\u04fb\u04fc\3\2\2\2\u04fc")
        buf.write("\u00b7\3\2\2\2\u04fd\u04fe\7E\2\2\u04fe\u04ff\7\u008b")
        buf.write("\2\2\u04ff\u0504\5\u00ba^\2\u0500\u0501\7\u0087\2\2\u0501")
        buf.write("\u0503\5\u00ba^\2\u0502\u0500\3\2\2\2\u0503\u0506\3\2")
        buf.write("\2\2\u0504\u0502\3\2\2\2\u0504\u0505\3\2\2\2\u0505\u00b9")
        buf.write("\3\2\2\2\u0506\u0504\3\2\2\2\u0507\u0509\5\u00be`\2\u0508")
        buf.write("\u0507\3\2\2\2\u0508\u0509\3\2\2\2\u0509\u050a\3\2\2\2")
        buf.write("\u050a\u050b\5\u00bc_\2\u050b\u00bb\3\2\2\2\u050c\u0510")
        buf.write("\5\32\16\2\u050d\u0510\7\u0092\2\2\u050e\u0510\7\u0093")
        buf.write("\2\2\u050f\u050c\3\2\2\2\u050f\u050d\3\2\2\2\u050f\u050e")
        buf.write("\3\2\2\2\u0510\u00bd\3\2\2\2\u0511\u0512\7z\2\2\u0512")
        buf.write("\u0513\7~\2\2\u0513\u00bf\3\2\2\2\u0514\u0515\7@\2\2\u0515")
        buf.write("\u0516\7\u0080\2\2\u0516\u0517\5\u00c2b\2\u0517\u0518")
        buf.write("\7\u0081\2\2\u0518\u00c1\3\2\2\2\u0519\u051e\5\u00c4c")
        buf.write("\2\u051a\u051b\7\u0087\2\2\u051b\u051d\5\u00c4c\2\u051c")
        buf.write("\u051a\3\2\2\2\u051d\u0520\3\2\2\2\u051e\u051c\3\2\2\2")
        buf.write("\u051e\u051f\3\2\2\2\u051f\u00c3\3\2\2\2\u0520\u051e\3")
        buf.write("\2\2\2\u0521\u0522\5\32\16\2\u0522\u00c5\3\2\2\2\u0523")
        buf.write("\u0528\7A\2\2\u0524\u0525\7\u0080\2\2\u0525\u0526\5\u00c8")
        buf.write("e\2\u0526\u0527\7\u0081\2\2\u0527\u0529\3\2\2\2\u0528")
        buf.write("\u0524\3\2\2\2\u0528\u0529\3\2\2\2\u0529\u00c7\3\2\2\2")
        buf.write("\u052a\u052b\7w\2\2\u052b\u00c9\3\2\2\2\u052c\u0531\5")
        buf.write("\u00ccg\2\u052d\u052e\7\u0080\2\2\u052e\u052f\5\u00ce")
        buf.write("h\2\u052f\u0530\7\u0081\2\2\u0530\u0532\3\2\2\2\u0531")
        buf.write("\u052d\3\2\2\2\u0531\u0532\3\2\2\2\u0532\u00cb\3\2\2\2")
        buf.write("\u0533\u0534\t\t\2\2\u0534\u00cd\3\2\2\2\u0535\u053a\5")
        buf.write("\u00d0i\2\u0536\u0537\7\u0087\2\2\u0537\u0539\5\u00d0")
        buf.write("i\2\u0538\u0536\3\2\2\2\u0539\u053c\3\2\2\2\u053a\u0538")
        buf.write("\3\2\2\2\u053a\u053b\3\2\2\2\u053b\u00cf\3\2\2\2\u053c")
        buf.write("\u053a\3\2\2\2\u053d\u053e\5\u00d4k\2\u053e\u053f\5\u00d2")
        buf.write("j\2\u053f\u0540\5\u00d6l\2\u0540\u00d1\3\2\2\2\u0541\u0542")
        buf.write("\7{\2\2\u0542\u00d3\3\2\2\2\u0543\u0544\5\32\16\2\u0544")
        buf.write("\u0545\7\u008b\2\2\u0545\u00d5\3\2\2\2\u0546\u0548\5\u00d8")
        buf.write("m\2\u0547\u0546\3\2\2\2\u0548\u054b\3\2\2\2\u0549\u0547")
        buf.write("\3\2\2\2\u0549\u054a\3\2\2\2\u054a\u00d7\3\2\2\2\u054b")
        buf.write("\u0549\3\2\2\2\u054c\u054d\7\u0091\2\2\u054d\u054e\5\32")
        buf.write("\16\2\u054e\u00d9\3\2\2\2\u054f\u0550\5\u00dco\2\u0550")
        buf.write("\u0552\7\u0080\2\2\u0551\u0553\5\u00dep\2\u0552\u0551")
        buf.write("\3\2\2\2\u0552\u0553\3\2\2\2\u0553\u0556\3\2\2\2\u0554")
        buf.write("\u0557\5\u00e0q\2\u0555\u0557\5\u00e2r\2\u0556\u0554\3")
        buf.write("\2\2\2\u0556\u0555\3\2\2\2\u0557\u0559\3\2\2\2\u0558\u055a")
        buf.write("\5\u00e4s\2\u0559\u0558\3\2\2\2\u0559\u055a\3\2\2\2\u055a")
        buf.write("\u055b\3\2\2\2\u055b\u055c\7\u0081\2\2\u055c\u00db\3\2")
        buf.write("\2\2\u055d\u055e\t\n\2\2\u055e\u00dd\3\2\2\2\u055f\u0560")
        buf.write("\t\13\2\2\u0560\u00df\3\2\2\2\u0561\u0562\5\36\20\2\u0562")
        buf.write("\u00e1\3\2\2\2\u0563\u0564\5\34\17\2\u0564\u00e3\3\2\2")
        buf.write("\2\u0565\u0566\7\u0086\2\2\u0566\u0567\7}\2\2\u0567\u0568")
        buf.write("\5\32\16\2\u0568\u00e5\3\2\2\2\u0569\u0579\5\u00e8u\2")
        buf.write("\u056a\u0579\5\u0114\u008b\2\u056b\u0579\5\u011a\u008e")
        buf.write("\2\u056c\u0579\5\u014e\u00a8\2\u056d\u0579\5\u0152\u00aa")
        buf.write("\2\u056e\u0579\5\u0154\u00ab\2\u056f\u0579\5\u0156\u00ac")
        buf.write("\2\u0570\u0579\5\u015a\u00ae\2\u0571\u0579\5\u015c\u00af")
        buf.write("\2\u0572\u0579\5\u0160\u00b1\2\u0573\u0579\5\u0162\u00b2")
        buf.write("\2\u0574\u0579\5\u0164\u00b3\2\u0575\u0579\5\u0166\u00b4")
        buf.write("\2\u0576\u0579\5\u0168\u00b5\2\u0577\u0579\7x\2\2\u0578")
        buf.write("\u0569\3\2\2\2\u0578\u056a\3\2\2\2\u0578\u056b\3\2\2\2")
        buf.write("\u0578\u056c\3\2\2\2\u0578\u056d\3\2\2\2\u0578\u056e\3")
        buf.write("\2\2\2\u0578\u056f\3\2\2\2\u0578\u0570\3\2\2\2\u0578\u0571")
        buf.write("\3\2\2\2\u0578\u0572\3\2\2\2\u0578\u0573\3\2\2\2\u0578")
        buf.write("\u0574\3\2\2\2\u0578\u0575\3\2\2\2\u0578\u0576\3\2\2\2")
        buf.write("\u0578\u0577\3\2\2\2\u0579\u00e7\3\2\2\2\u057a\u0594\7")
        buf.write("\3\2\2\u057b\u058a\7\u0080\2\2\u057c\u0589\5\u0108\u0085")
        buf.write("\2\u057d\u0589\5\u010a\u0086\2\u057e\u0589\5\u010c\u0087")
        buf.write("\2\u057f\u0589\5\u010e\u0088\2\u0580\u0589\5\u0110\u0089")
        buf.write("\2\u0581\u0589\5\u0112\u008a\2\u0582\u0589\5\u0100\u0081")
        buf.write("\2\u0583\u0589\5\u00f2z\2\u0584\u0589\5\u00ecw\2\u0585")
        buf.write("\u0589\5\u00eav\2\u0586\u0589\7x\2\2\u0587\u0589\7\u0087")
        buf.write("\2\2\u0588\u057c\3\2\2\2\u0588\u057d\3\2\2\2\u0588\u057e")
        buf.write("\3\2\2\2\u0588\u057f\3\2\2\2\u0588\u0580\3\2\2\2\u0588")
        buf.write("\u0581\3\2\2\2\u0588\u0582\3\2\2\2\u0588\u0583\3\2\2\2")
        buf.write("\u0588\u0584\3\2\2\2\u0588\u0585\3\2\2\2\u0588\u0586\3")
        buf.write("\2\2\2\u0588\u0587\3\2\2\2\u0589\u058c\3\2\2\2\u058a\u0588")
        buf.write("\3\2\2\2\u058a\u058b\3\2\2\2\u058b\u0590\3\2\2\2\u058c")
        buf.write("\u058a\3\2\2\2\u058d\u058f\7x\2\2\u058e\u058d\3\2\2\2")
        buf.write("\u058f\u0592\3\2\2\2\u0590\u058e\3\2\2\2\u0590\u0591\3")
        buf.write("\2\2\2\u0591\u0593\3\2\2\2\u0592\u0590\3\2\2\2\u0593\u0595")
        buf.write("\7\u0081\2\2\u0594\u057b\3\2\2\2\u0594\u0595\3\2\2\2\u0595")
        buf.write("\u0599\3\2\2\2\u0596\u0598\7x\2\2\u0597\u0596\3\2\2\2")
        buf.write("\u0598\u059b\3\2\2\2\u0599\u0597\3\2\2\2\u0599\u059a\3")
        buf.write("\2\2\2\u059a\u00e9\3\2\2\2\u059b\u0599\3\2\2\2\u059c\u059d")
        buf.write("\7_\2\2\u059d\u05a1\7~\2\2\u059e\u05a0\7x\2\2\u059f\u059e")
        buf.write("\3\2\2\2\u05a0\u05a3\3\2\2\2\u05a1\u059f\3\2\2\2\u05a1")
        buf.write("\u05a2\3\2\2\2\u05a2\u05a4\3\2\2\2\u05a3\u05a1\3\2\2\2")
        buf.write("\u05a4\u05af\5\u00f0y\2\u05a5\u05a9\7\u0087\2\2\u05a6")
        buf.write("\u05a8\7x\2\2\u05a7\u05a6\3\2\2\2\u05a8\u05ab\3\2\2\2")
        buf.write("\u05a9\u05a7\3\2\2\2\u05a9\u05aa\3\2\2\2\u05aa\u05ac\3")
        buf.write("\2\2\2\u05ab\u05a9\3\2\2\2\u05ac\u05ae\5\u00f0y\2\u05ad")
        buf.write("\u05a5\3\2\2\2\u05ae\u05b1\3\2\2\2\u05af\u05ad\3\2\2\2")
        buf.write("\u05af\u05b0\3\2\2\2\u05b0\u00eb\3\2\2\2\u05b1\u05af\3")
        buf.write("\2\2\2\u05b2\u05b3\7^\2\2\u05b3\u05b4\7~\2\2\u05b4\u05b9")
        buf.write("\5\u00eex\2\u05b5\u05b6\7\u0087\2\2\u05b6\u05b8\5\u00ee")
        buf.write("x\2\u05b7\u05b5\3\2\2\2\u05b8\u05bb\3\2\2\2\u05b9\u05b7")
        buf.write("\3\2\2\2\u05b9\u05ba\3\2\2\2\u05ba\u00ed\3\2\2\2\u05bb")
        buf.write("\u05b9\3\2\2\2\u05bc\u05bd\t\3\2\2\u05bd\u00ef\3\2\2\2")
        buf.write("\u05be\u05bf\t\3\2\2\u05bf\u00f1\3\2\2\2\u05c0\u05c1\7")
        buf.write("c\2\2\u05c1\u05c2\7~\2\2\u05c2\u05c7\5\u00f4{\2\u05c3")
        buf.write("\u05c4\7\u0087\2\2\u05c4\u05c6\5\u00f4{\2\u05c5\u05c3")
        buf.write("\3\2\2\2\u05c6\u05c9\3\2\2\2\u05c7\u05c5\3\2\2\2\u05c7")
        buf.write("\u05c8\3\2\2\2\u05c8\u00f3\3\2\2\2\u05c9\u05c7\3\2\2\2")
        buf.write("\u05ca\u05d7\5\u00f6|\2\u05cb\u05d3\7\u0080\2\2\u05cc")
        buf.write("\u05d2\5\u00f8}\2\u05cd\u05d2\5\u00fc\177\2\u05ce\u05d2")
        buf.write("\5\u00fe\u0080\2\u05cf\u05d2\7x\2\2\u05d0\u05d2\7\u0087")
        buf.write("\2\2\u05d1\u05cc\3\2\2\2\u05d1\u05cd\3\2\2\2\u05d1\u05ce")
        buf.write("\3\2\2\2\u05d1\u05cf\3\2\2\2\u05d1\u05d0\3\2\2\2\u05d2")
        buf.write("\u05d5\3\2\2\2\u05d3\u05d1\3\2\2\2\u05d3\u05d4\3\2\2\2")
        buf.write("\u05d4\u05d6\3\2\2\2\u05d5\u05d3\3\2\2\2\u05d6\u05d8\7")
        buf.write("\u0081\2\2\u05d7\u05cb\3\2\2\2\u05d7\u05d8\3\2\2\2\u05d8")
        buf.write("\u00f5\3\2\2\2\u05d9\u05da\5\32\16\2\u05da\u00f7\3\2\2")
        buf.write("\2\u05db\u05dc\7d\2\2\u05dc\u05dd\7~\2\2\u05dd\u05de\5")
        buf.write("\u00fa~\2\u05de\u00f9\3\2\2\2\u05df\u05e0\t\f\2\2\u05e0")
        buf.write("\u00fb\3\2\2\2\u05e1\u05e2\7l\2\2\u05e2\u05e3\7~\2\2\u05e3")
        buf.write("\u05e4\7z\2\2\u05e4\u00fd\3\2\2\2\u05e5\u05e6\7s\2\2\u05e6")
        buf.write("\u05e7\7~\2\2\u05e7\u05e8\5 \21\2\u05e8\u00ff\3\2\2\2")
        buf.write("\u05e9\u05ea\7m\2\2\u05ea\u05eb\7~\2\2\u05eb\u05f0\5\u0102")
        buf.write("\u0082\2\u05ec\u05ed\7\u0087\2\2\u05ed\u05ef\5\u0102\u0082")
        buf.write("\2\u05ee\u05ec\3\2\2\2\u05ef\u05f2\3\2\2\2\u05f0\u05ee")
        buf.write("\3\2\2\2\u05f0\u05f1\3\2\2\2\u05f1\u0101\3\2\2\2\u05f2")
        buf.write("\u05f0\3\2\2\2\u05f3\u05f5\5\u0104\u0083\2\u05f4\u05f6")
        buf.write("\5\u0106\u0084\2\u05f5\u05f4\3\2\2\2\u05f5\u05f6\3\2\2")
        buf.write("\2\u05f6\u05f7\3\2\2\2\u05f7\u05f8\7\u0080\2\2\u05f8\u05f9")
        buf.write("\5 \21\2\u05f9\u05fa\7\u0081\2\2\u05fa\u0103\3\2\2\2\u05fb")
        buf.write("\u05fc\5\32\16\2\u05fc\u0105\3\2\2\2\u05fd\u05fe\t\3\2")
        buf.write("\2\u05fe\u0107\3\2\2\2\u05ff\u0600\7n\2\2\u0600\u0601")
        buf.write("\7~\2\2\u0601\u0605\5 \21\2\u0602\u0604\7x\2\2\u0603\u0602")
        buf.write("\3\2\2\2\u0604\u0607\3\2\2\2\u0605\u0603\3\2\2\2\u0605")
        buf.write("\u0606\3\2\2\2\u0606\u0109\3\2\2\2\u0607\u0605\3\2\2\2")
        buf.write("\u0608\u0609\7o\2\2\u0609\u060a\7~\2\2\u060a\u060e\5 ")
        buf.write("\21\2\u060b\u060d\7x\2\2\u060c\u060b\3\2\2\2\u060d\u0610")
        buf.write("\3\2\2\2\u060e\u060c\3\2\2\2\u060e\u060f\3\2\2\2\u060f")
        buf.write("\u010b\3\2\2\2\u0610\u060e\3\2\2\2\u0611\u0612\7p\2\2")
        buf.write("\u0612\u0613\7~\2\2\u0613\u0617\5 \21\2\u0614\u0616\7")
        buf.write("x\2\2\u0615\u0614\3\2\2\2\u0616\u0619\3\2\2\2\u0617\u0615")
        buf.write("\3\2\2\2\u0617\u0618\3\2\2\2\u0618\u010d\3\2\2\2\u0619")
        buf.write("\u0617\3\2\2\2\u061a\u061b\7q\2\2\u061b\u061c\7~\2\2\u061c")
        buf.write("\u0620\5 \21\2\u061d\u061f\7x\2\2\u061e\u061d\3\2\2\2")
        buf.write("\u061f\u0622\3\2\2\2\u0620\u061e\3\2\2\2\u0620\u0621\3")
        buf.write("\2\2\2\u0621\u010f\3\2\2\2\u0622\u0620\3\2\2\2\u0623\u0624")
        buf.write("\7r\2\2\u0624\u0625\7~\2\2\u0625\u0629\5 \21\2\u0626\u0628")
        buf.write("\7x\2\2\u0627\u0626\3\2\2\2\u0628\u062b\3\2\2\2\u0629")
        buf.write("\u0627\3\2\2\2\u0629\u062a\3\2\2\2\u062a\u0111\3\2\2\2")
        buf.write("\u062b\u0629\3\2\2\2\u062c\u062d\7s\2\2\u062d\u062e\7")
        buf.write("~\2\2\u062e\u0632\5 \21\2\u062f\u0631\7x\2\2\u0630\u062f")
        buf.write("\3\2\2\2\u0631\u0634\3\2\2\2\u0632\u0630\3\2\2\2\u0632")
        buf.write("\u0633\3\2\2\2\u0633\u0113\3\2\2\2\u0634\u0632\3\2\2\2")
        buf.write("\u0635\u0644\7\t\2\2\u0636\u0640\7\u0080\2\2\u0637\u0641")
        buf.write("\5\u0116\u008c\2\u0638\u063d\5\u0118\u008d\2\u0639\u063a")
        buf.write("\7\u0087\2\2\u063a\u063c\5\u0118\u008d\2\u063b\u0639\3")
        buf.write("\2\2\2\u063c\u063f\3\2\2\2\u063d\u063b\3\2\2\2\u063d\u063e")
        buf.write("\3\2\2\2\u063e\u0641\3\2\2\2\u063f\u063d\3\2\2\2\u0640")
        buf.write("\u0637\3\2\2\2\u0640\u0638\3\2\2\2\u0641\u0642\3\2\2\2")
        buf.write("\u0642\u0643\7\u0081\2\2\u0643\u0645\3\2\2\2\u0644\u0636")
        buf.write("\3\2\2\2\u0644\u0645\3\2\2\2\u0645\u0115\3\2\2\2\u0646")
        buf.write("\u0647\7\u008f\2\2\u0647\u0117\3\2\2\2\u0648\u0649\5\32")
        buf.write("\16\2\u0649\u0119\3\2\2\2\u064a\u064d\7\n\2\2\u064b\u064c")
        buf.write("\7\u0088\2\2\u064c\u064e\5\u0120\u0091\2\u064d\u064b\3")
        buf.write("\2\2\2\u064d\u064e\3\2\2\2\u064e\u0653\3\2\2\2\u064f\u0650")
        buf.write("\7\u0080\2\2\u0650\u0651\5\u011c\u008f\2\u0651\u0652\7")
        buf.write("\u0081\2\2\u0652\u0654\3\2\2\2\u0653\u064f\3\2\2\2\u0653")
        buf.write("\u0654\3\2\2\2\u0654\u011b\3\2\2\2\u0655\u065b\5\u011e")
        buf.write("\u0090\2\u0656\u065a\5\u0148\u00a5\2\u0657\u065a\7x\2")
        buf.write("\2\u0658\u065a\7\u0087\2\2\u0659\u0656\3\2\2\2\u0659\u0657")
        buf.write("\3\2\2\2\u0659\u0658\3\2\2\2\u065a\u065d\3\2\2\2\u065b")
        buf.write("\u0659\3\2\2\2\u065b\u065c\3\2\2\2\u065c\u011d\3\2\2\2")
        buf.write("\u065d\u065b\3\2\2\2\u065e\u066c\5\u0132\u009a\2\u065f")
        buf.write("\u066c\5\u0122\u0092\2\u0660\u066c\5\u0124\u0093\2\u0661")
        buf.write("\u066c\5\u0136\u009c\2\u0662\u066c\5\u0126\u0094\2\u0663")
        buf.write("\u066c\5\u0128\u0095\2\u0664\u066c\5\u012a\u0096\2\u0665")
        buf.write("\u066c\5\u012c\u0097\2\u0666\u066c\5\u012e\u0098\2\u0667")
        buf.write("\u066c\5\u0130\u0099\2\u0668\u066c\5\u0140\u00a1\2\u0669")
        buf.write("\u066c\7x\2\2\u066a\u066c\7\u0087\2\2\u066b\u065e\3\2")
        buf.write("\2\2\u066b\u065f\3\2\2\2\u066b\u0660\3\2\2\2\u066b\u0661")
        buf.write("\3\2\2\2\u066b\u0662\3\2\2\2\u066b\u0663\3\2\2\2\u066b")
        buf.write("\u0664\3\2\2\2\u066b\u0665\3\2\2\2\u066b\u0666\3\2\2\2")
        buf.write("\u066b\u0667\3\2\2\2\u066b\u0668\3\2\2\2\u066b\u0669\3")
        buf.write("\2\2\2\u066b\u066a\3\2\2\2\u066c\u066f\3\2\2\2\u066d\u066b")
        buf.write("\3\2\2\2\u066d\u066e\3\2\2\2\u066e\u011f\3\2\2\2\u066f")
        buf.write("\u066d\3\2\2\2\u0670\u0671\5\32\16\2\u0671\u0121\3\2\2")
        buf.write("\2\u0672\u0673\7k\2\2\u0673\u0674\7~\2\2\u0674\u0678\7")
        buf.write("w\2\2\u0675\u0677\7x\2\2\u0676\u0675\3\2\2\2\u0677\u067a")
        buf.write("\3\2\2\2\u0678\u0676\3\2\2\2\u0678\u0679\3\2\2\2\u0679")
        buf.write("\u0123\3\2\2\2\u067a\u0678\3\2\2\2\u067b\u067c\7>\2\2")
        buf.write("\u067c\u067d\7~\2\2\u067d\u0681\7w\2\2\u067e\u0680\7x")
        buf.write("\2\2\u067f\u067e\3\2\2\2\u0680\u0683\3\2\2\2\u0681\u067f")
        buf.write("\3\2\2\2\u0681\u0682\3\2\2\2\u0682\u0125\3\2\2\2\u0683")
        buf.write("\u0681\3\2\2\2\u0684\u0685\7h\2\2\u0685\u0689\5&\24\2")
        buf.write("\u0686\u0688\7x\2\2\u0687\u0686\3\2\2\2\u0688\u068b\3")
        buf.write("\2\2\2\u0689\u0687\3\2\2\2\u0689\u068a\3\2\2\2\u068a\u0127")
        buf.write("\3\2\2\2\u068b\u0689\3\2\2\2\u068c\u068e\7g\2\2\u068d")
        buf.write("\u068f\7~\2\2\u068e\u068d\3\2\2\2\u068e\u068f\3\2\2\2")
        buf.write("\u068f\u0690\3\2\2\2\u0690\u0694\5&\24\2\u0691\u0693\7")
        buf.write("x\2\2\u0692\u0691\3\2\2\2\u0693\u0696\3\2\2\2\u0694\u0692")
        buf.write("\3\2\2\2\u0694\u0695\3\2\2\2\u0695\u0129\3\2\2\2\u0696")
        buf.write("\u0694\3\2\2\2\u0697\u0699\7M\2\2\u0698\u069a\7~\2\2\u0699")
        buf.write("\u0698\3\2\2\2\u0699\u069a\3\2\2\2\u069a\u069b\3\2\2\2")
        buf.write("\u069b\u069f\5&\24\2\u069c\u069e\7x\2\2\u069d\u069c\3")
        buf.write("\2\2\2\u069e\u06a1\3\2\2\2\u069f\u069d\3\2\2\2\u069f\u06a0")
        buf.write("\3\2\2\2\u06a0\u012b\3\2\2\2\u06a1\u069f\3\2\2\2\u06a2")
        buf.write("\u06a4\7L\2\2\u06a3\u06a5\7~\2\2\u06a4\u06a3\3\2\2\2\u06a4")
        buf.write("\u06a5\3\2\2\2\u06a5\u06a6\3\2\2\2\u06a6\u06aa\5&\24\2")
        buf.write("\u06a7\u06a9\7x\2\2\u06a8\u06a7\3\2\2\2\u06a9\u06ac\3")
        buf.write("\2\2\2\u06aa\u06a8\3\2\2\2\u06aa\u06ab\3\2\2\2\u06ab\u012d")
        buf.write("\3\2\2\2\u06ac\u06aa\3\2\2\2\u06ad\u06ae\7o\2\2\u06ae")
        buf.write("\u06af\7~\2\2\u06af\u06b3\5 \21\2\u06b0\u06b2\7x\2\2\u06b1")
        buf.write("\u06b0\3\2\2\2\u06b2\u06b5\3\2\2\2\u06b3\u06b1\3\2\2\2")
        buf.write("\u06b3\u06b4\3\2\2\2\u06b4\u012f\3\2\2\2\u06b5\u06b3\3")
        buf.write("\2\2\2\u06b6\u06b7\7e\2\2\u06b7\u06b8\7~\2\2\u06b8\u06bc")
        buf.write("\5\32\16\2\u06b9\u06bb\7x\2\2\u06ba\u06b9\3\2\2\2\u06bb")
        buf.write("\u06be\3\2\2\2\u06bc\u06ba\3\2\2\2\u06bc\u06bd\3\2\2\2")
        buf.write("\u06bd\u0131\3\2\2\2\u06be\u06bc\3\2\2\2\u06bf\u06c0\7")
        buf.write("s\2\2\u06c0\u06c1\7~\2\2\u06c1\u06c3\5 \21\2\u06c2\u06c4")
        buf.write("\5\u0134\u009b\2\u06c3\u06c2\3\2\2\2\u06c3\u06c4\3\2\2")
        buf.write("\2\u06c4\u06c8\3\2\2\2\u06c5\u06c7\7x\2\2\u06c6\u06c5")
        buf.write("\3\2\2\2\u06c7\u06ca\3\2\2\2\u06c8\u06c6\3\2\2\2\u06c8")
        buf.write("\u06c9\3\2\2\2\u06c9\u0133\3\2\2\2\u06ca\u06c8\3\2\2\2")
        buf.write("\u06cb\u06cc\5$\23\2\u06cc\u0135\3\2\2\2\u06cd\u06ce\7")
        buf.write("i\2\2\u06ce\u06cf\7\u0080\2\2\u06cf\u06d4\5\u0138\u009d")
        buf.write("\2\u06d0\u06d1\7\u0087\2\2\u06d1\u06d3\5\u0138\u009d\2")
        buf.write("\u06d2\u06d0\3\2\2\2\u06d3\u06d6\3\2\2\2\u06d4\u06d2\3")
        buf.write("\2\2\2\u06d4\u06d5\3\2\2\2\u06d5\u06d7\3\2\2\2\u06d6\u06d4")
        buf.write("\3\2\2\2\u06d7\u06d8\7\u0081\2\2\u06d8\u0137\3\2\2\2\u06d9")
        buf.write("\u06dd\5\u013a\u009e\2\u06da\u06db\7~\2\2\u06db\u06de")
        buf.write("\5\u013c\u009f\2\u06dc\u06de\5\u013e\u00a0\2\u06dd\u06da")
        buf.write("\3\2\2\2\u06dd\u06dc\3\2\2\2\u06dd\u06de\3\2\2\2\u06de")
        buf.write("\u0139\3\2\2\2\u06df\u06e0\t\r\2\2\u06e0\u013b\3\2\2\2")
        buf.write("\u06e1\u06e2\5\36\20\2\u06e2\u013d\3\2\2\2\u06e3\u06e4")
        buf.write("\5\34\17\2\u06e4\u013f\3\2\2\2\u06e5\u06e6\7f\2\2\u06e6")
        buf.write("\u06e7\7~\2\2\u06e7\u06eb\5\u0142\u00a2\2\u06e8\u06ea")
        buf.write("\7x\2\2\u06e9\u06e8\3\2\2\2\u06ea\u06ed\3\2\2\2\u06eb")
        buf.write("\u06e9\3\2\2\2\u06eb\u06ec\3\2\2\2\u06ec\u0141\3\2\2\2")
        buf.write("\u06ed\u06eb\3\2\2\2\u06ee\u06ef\7j\2\2\u06ef\u06f2\5")
        buf.write("\u0144\u00a3\2\u06f0\u06f1\7u\2\2\u06f1\u06f3\5\u0146")
        buf.write("\u00a4\2\u06f2\u06f0\3\2\2\2\u06f2\u06f3\3\2\2\2\u06f3")
        buf.write("\u0143\3\2\2\2\u06f4\u06f5\5\32\16\2\u06f5\u0145\3\2\2")
        buf.write("\2\u06f6\u06f7\5\32\16\2\u06f7\u0147\3\2\2\2\u06f8\u06f9")
        buf.write("\7c\2\2\u06f9\u06fd\7~\2\2\u06fa\u06fe\5\u014a\u00a6\2")
        buf.write("\u06fb\u06fe\7\u0087\2\2\u06fc\u06fe\7x\2\2\u06fd\u06fa")
        buf.write("\3\2\2\2\u06fd\u06fb\3\2\2\2\u06fd\u06fc\3\2\2\2\u06fe")
        buf.write("\u06ff\3\2\2\2\u06ff\u06fd\3\2\2\2\u06ff\u0700\3\2\2\2")
        buf.write("\u0700\u0149\3\2\2\2\u0701\u0702\5\u014c\u00a7\2\u0702")
        buf.write("\u0703\7\u0080\2\2\u0703\u0704\5\u011c\u008f\2\u0704\u0705")
        buf.write("\7\u0081\2\2\u0705\u014b\3\2\2\2\u0706\u0707\5\32\16\2")
        buf.write("\u0707\u014d\3\2\2\2\u0708\u0709\7)\2\2\u0709\u070a\7")
        buf.write("\u0080\2\2\u070a\u070b\5\u0150\u00a9\2\u070b\u070c\7\u0081")
        buf.write("\2\2\u070c\u014f\3\2\2\2\u070d\u0712\5\32\16\2\u070e\u070f")
        buf.write("\7\u0087\2\2\u070f\u0711\5\32\16\2\u0710\u070e\3\2\2\2")
        buf.write("\u0711\u0714\3\2\2\2\u0712\u0710\3\2\2\2\u0712\u0713\3")
        buf.write("\2\2\2\u0713\u0151\3\2\2\2\u0714\u0712\3\2\2\2\u0715\u0716")
        buf.write("\7(\2\2\u0716\u0717\5&\24\2\u0717\u0153\3\2\2\2\u0718")
        buf.write("\u0719\7%\2\2\u0719\u071a\5&\24\2\u071a\u0155\3\2\2\2")
        buf.write("\u071b\u0720\7 \2\2\u071c\u071d\7\u0080\2\2\u071d\u071e")
        buf.write("\5\u0158\u00ad\2\u071e\u071f\7\u0081\2\2\u071f\u0721\3")
        buf.write("\2\2\2\u0720\u071c\3\2\2\2\u0720\u0721\3\2\2\2\u0721\u0157")
        buf.write("\3\2\2\2\u0722\u0723\7]\2\2\u0723\u0159\3\2\2\2\u0724")
        buf.write("\u0725\7\"\2\2\u0725\u0726\7\u0080\2\2\u0726\u0727\5\34")
        buf.write("\17\2\u0727\u0728\7\u0081\2\2\u0728\u015b\3\2\2\2\u0729")
        buf.write("\u072a\7!\2\2\u072a\u072b\7\u0080\2\2\u072b\u072c\5\u015e")
        buf.write("\u00b0\2\u072c\u072d\7\u0081\2\2\u072d\u015d\3\2\2\2\u072e")
        buf.write("\u072f\5\32\16\2\u072f\u015f\3\2\2\2\u0730\u0731\7#\2")
        buf.write("\2\u0731\u0732\5&\24\2\u0732\u0161\3\2\2\2\u0733\u0734")
        buf.write("\7&\2\2\u0734\u0735\5&\24\2\u0735\u0163\3\2\2\2\u0736")
        buf.write("\u0737\7\'\2\2\u0737\u0738\5&\24\2\u0738\u0165\3\2\2\2")
        buf.write("\u0739\u073a\7$\2\2\u073a\u073b\5&\24\2\u073b\u0167\3")
        buf.write("\2\2\2\u073c\u073d\7*\2\2\u073d\u073e\7\u0080\2\2\u073e")
        buf.write("\u073f\5\u016a\u00b6\2\u073f\u0740\7\u0081\2\2\u0740\u0169")
        buf.write("\3\2\2\2\u0741\u0742\5\32\16\2\u0742\u016b\3\2\2\2\u0743")
        buf.write("\u0747\5\u016e\u00b8\2\u0744\u0746\7x\2\2\u0745\u0744")
        buf.write("\3\2\2\2\u0746\u0749\3\2\2\2\u0747\u0745\3\2\2\2\u0747")
        buf.write("\u0748\3\2\2\2\u0748\u074a\3\2\2\2\u0749\u0747\3\2\2\2")
        buf.write("\u074a\u074e\5\u0188\u00c5\2\u074b\u074d\7x\2\2\u074c")
        buf.write("\u074b\3\2\2\2\u074d\u0750\3\2\2\2\u074e\u074c\3\2\2\2")
        buf.write("\u074e\u074f\3\2\2\2\u074f\u016d\3\2\2\2\u0750\u074e\3")
        buf.write("\2\2\2\u0751\u0753\7\u0082\2\2\u0752\u0754\5\u0170\u00b9")
        buf.write("\2\u0753\u0752\3\2\2\2\u0753\u0754\3\2\2\2\u0754\u0755")
        buf.write("\3\2\2\2\u0755\u0757\5\u0186\u00c4\2\u0756\u0758\5\u0172")
        buf.write("\u00ba\2\u0757\u0756\3\2\2\2\u0757\u0758\3\2\2\2\u0758")
        buf.write("\u0761\3\2\2\2\u0759\u075b\7~\2\2\u075a\u075c\5\u017c")
        buf.write("\u00bf\2\u075b\u075a\3\2\2\2\u075b\u075c\3\2\2\2\u075c")
        buf.write("\u075f\3\2\2\2\u075d\u075e\7~\2\2\u075e\u0760\5\u0176")
        buf.write("\u00bc\2\u075f\u075d\3\2\2\2\u075f\u0760\3\2\2\2\u0760")
        buf.write("\u0762\3\2\2\2\u0761\u0759\3\2\2\2\u0761\u0762\3\2\2\2")
        buf.write("\u0762\u0763\3\2\2\2\u0763\u0765\7\u0083\2\2\u0764\u0766")
        buf.write("\7x\2\2\u0765\u0764\3\2\2\2\u0765\u0766\3\2\2\2\u0766")
        buf.write("\u016f\3\2\2\2\u0767\u0768\5\32\16\2\u0768\u0769\7\u0088")
        buf.write("\2\2\u0769\u076b\3\2\2\2\u076a\u0767\3\2\2\2\u076a\u076b")
        buf.write("\3\2\2\2\u076b\u076c\3\2\2\2\u076c\u076d\5\32\16\2\u076d")
        buf.write("\u076e\t\16\2\2\u076e\u076f\7}\2\2\u076f\u0171\3\2\2\2")
        buf.write("\u0770\u0771\7u\2\2\u0771\u0772\5\u0174\u00bb\2\u0772")
        buf.write("\u0173\3\2\2\2\u0773\u0774\5\32\16\2\u0774\u0175\3\2\2")
        buf.write("\2\u0775\u0778\5\u0178\u00bd\2\u0776\u0778\5&\24\2\u0777")
        buf.write("\u0775\3\2\2\2\u0777\u0776\3\2\2\2\u0778\u0177\3\2\2\2")
        buf.write("\u0779\u077e\5\u017a\u00be\2\u077a\u077b\7\u008a\2\2\u077b")
        buf.write("\u077d\5\u017a\u00be\2\u077c\u077a\3\2\2\2\u077d\u0780")
        buf.write("\3\2\2\2\u077e\u077c\3\2\2\2\u077e\u077f\3\2\2\2\u077f")
        buf.write("\u0179\3\2\2\2\u0780\u077e\3\2\2\2\u0781\u0787\5\32\16")
        buf.write("\2\u0782\u0787\7z\2\2\u0783\u0787\7\u0086\2\2\u0784\u0787")
        buf.write("\7\u0085\2\2\u0785\u0787\7\u0088\2\2\u0786\u0781\3\2\2")
        buf.write("\2\u0786\u0782\3\2\2\2\u0786\u0783\3\2\2\2\u0786\u0784")
        buf.write("\3\2\2\2\u0786\u0785\3\2\2\2\u0787\u0788\3\2\2\2\u0788")
        buf.write("\u0786\3\2\2\2\u0788\u0789\3\2\2\2\u0789\u017b\3\2\2\2")
        buf.write("\u078a\u078c\t\17\2\2\u078b\u078a\3\2\2\2\u078b\u078c")
        buf.write("\3\2\2\2\u078c\u078d\3\2\2\2\u078d\u078e\5\u0184\u00c3")
        buf.write("\2\u078e\u017d\3\2\2\2\u078f\u0793\5\32\16\2\u0790\u0793")
        buf.write("\7\u0086\2\2\u0791\u0793\7z\2\2\u0792\u078f\3\2\2\2\u0792")
        buf.write("\u0790\3\2\2\2\u0792\u0791\3\2\2\2\u0793\u0794\3\2\2\2")
        buf.write("\u0794\u0792\3\2\2\2\u0794\u0795\3\2\2\2\u0795\u017f\3")
        buf.write("\2\2\2\u0796\u0797\7|\2\2\u0797\u0798\5\32\16\2\u0798")
        buf.write("\u0799\7}\2\2\u0799\u0181\3\2\2\2\u079a\u079d\5\u017e")
        buf.write("\u00c0\2\u079b\u079d\5\u0180\u00c1\2\u079c\u079a\3\2\2")
        buf.write("\2\u079c\u079b\3\2\2\2\u079d\u0183\3\2\2\2\u079e\u07a9")
        buf.write("\7\u008a\2\2\u079f\u07a0\7\u008a\2\2\u07a0\u07a2\5\u0182")
        buf.write("\u00c2\2\u07a1\u079f\3\2\2\2\u07a2\u07a3\3\2\2\2\u07a3")
        buf.write("\u07a1\3\2\2\2\u07a3\u07a4\3\2\2\2\u07a4\u07a6\3\2\2\2")
        buf.write("\u07a5\u07a7\7\u008a\2\2\u07a6\u07a5\3\2\2\2\u07a6\u07a7")
        buf.write("\3\2\2\2\u07a7\u07a9\3\2\2\2\u07a8\u079e\3\2\2\2\u07a8")
        buf.write("\u07a1\3\2\2\2\u07a9\u0185\3\2\2\2\u07aa\u07ab\5\32\16")
        buf.write("\2\u07ab\u0187\3\2\2\2\u07ac\u07ae\5\u018c\u00c7\2\u07ad")
        buf.write("\u07ac\3\2\2\2\u07ae\u07b1\3\2\2\2\u07af\u07ad\3\2\2\2")
        buf.write("\u07af\u07b0\3\2\2\2\u07b0\u07b5\3\2\2\2\u07b1\u07af\3")
        buf.write("\2\2\2\u07b2\u07b4\5\u0192\u00ca\2\u07b3\u07b2\3\2\2\2")
        buf.write("\u07b4\u07b7\3\2\2\2\u07b5\u07b3\3\2\2\2\u07b5\u07b6\3")
        buf.write("\2\2\2\u07b6\u07b9\3\2\2\2\u07b7\u07b5\3\2\2\2\u07b8\u07ba")
        buf.write("\5\u018a\u00c6\2\u07b9\u07b8\3\2\2\2\u07b9\u07ba\3\2\2")
        buf.write("\2\u07ba\u07be\3\2\2\2\u07bb\u07bd\7x\2\2\u07bc\u07bb")
        buf.write("\3\2\2\2\u07bd\u07c0\3\2\2\2\u07be\u07bc\3\2\2\2\u07be")
        buf.write("\u07bf\3\2\2\2\u07bf\u07c4\3\2\2\2\u07c0\u07be\3\2\2\2")
        buf.write("\u07c1\u07c3\5\u019a\u00ce\2\u07c2\u07c1\3\2\2\2\u07c3")
        buf.write("\u07c6\3\2\2\2\u07c4\u07c2\3\2\2\2\u07c4\u07c5\3\2\2\2")
        buf.write("\u07c5\u0189\3\2\2\2\u07c6\u07c4\3\2\2\2\u07c7\u07c8\5")
        buf.write("&\24\2\u07c8\u018b\3\2\2\2\u07c9\u07ca\5\u018e\u00c8\2")
        buf.write("\u07ca\u07cb\7\u0099\2\2\u07cb\u07d2\5\u0190\u00c9\2\u07cc")
        buf.write("\u07ce\7x\2\2\u07cd\u07cc\3\2\2\2\u07ce\u07cf\3\2\2\2")
        buf.write("\u07cf\u07cd\3\2\2\2\u07cf\u07d0\3\2\2\2\u07d0\u07d3\3")
        buf.write("\2\2\2\u07d1\u07d3\7\2\2\3\u07d2\u07cd\3\2\2\2\u07d2\u07d1")
        buf.write("\3\2\2\2\u07d3\u018d\3\2\2\2\u07d4\u07d5\5\32\16\2\u07d5")
        buf.write("\u018f\3\2\2\2\u07d6\u07d7\7\u009d\2\2\u07d7\u0191\3\2")
        buf.write("\2\2\u07d8\u07d9\5\u0194\u00cb\2\u07d9\u07db\7\u0080\2")
        buf.write("\2\u07da\u07dc\5\u0196\u00cc\2\u07db\u07da\3\2\2\2\u07db")
        buf.write("\u07dc\3\2\2\2\u07dc\u07dd\3\2\2\2\u07dd\u07df\7\u0081")
        buf.write("\2\2\u07de\u07e0\5*\26\2\u07df\u07de\3\2\2\2\u07df\u07e0")
        buf.write("\3\2\2\2\u07e0\u07e7\3\2\2\2\u07e1\u07e3\7x\2\2\u07e2")
        buf.write("\u07e1\3\2\2\2\u07e3\u07e4\3\2\2\2\u07e4\u07e2\3\2\2\2")
        buf.write("\u07e4\u07e5\3\2\2\2\u07e5\u07e8\3\2\2\2\u07e6\u07e8\7")
        buf.write("\2\2\3\u07e7\u07e2\3\2\2\2\u07e7\u07e6\3\2\2\2\u07e8\u0193")
        buf.write("\3\2\2\2\u07e9\u07ea\5\32\16\2\u07ea\u0195\3\2\2\2\u07eb")
        buf.write("\u07f0\5\u0198\u00cd\2\u07ec\u07ed\7\u0087\2\2\u07ed\u07ef")
        buf.write("\5\u0198\u00cd\2\u07ee\u07ec\3\2\2\2\u07ef\u07f2\3\2\2")
        buf.write("\2\u07f0\u07ee\3\2\2\2\u07f0\u07f1\3\2\2\2\u07f1\u0197")
        buf.write("\3\2\2\2\u07f2\u07f0\3\2\2\2\u07f3\u07f5\7\u0088\2\2\u07f4")
        buf.write("\u07f3\3\2\2\2\u07f4\u07f5\3\2\2\2\u07f5\u07f6\3\2\2\2")
        buf.write("\u07f6\u07f7\5\32\16\2\u07f7\u0199\3\2\2\2\u07f8\u080a")
        buf.write("\5\u019c\u00cf\2\u07f9\u080a\5\u01a8\u00d5\2\u07fa\u080a")
        buf.write("\5\u01b0\u00d9\2\u07fb\u080a\5\u01b4\u00db\2\u07fc\u080a")
        buf.write("\5\u01b8\u00dd\2\u07fd\u080a\5\u0202\u0102\2\u07fe\u080a")
        buf.write("\5\u0204\u0103\2\u07ff\u080a\5\u0206\u0104\2\u0800\u080a")
        buf.write("\5\u0208\u0105\2\u0801\u080a\5\u01ba\u00de\2\u0802\u080a")
        buf.write("\5\u020a\u0106\2\u0803\u080a\5\u020c\u0107\2\u0804\u080a")
        buf.write("\5\u0226\u0114\2\u0805\u080a\5\u0228\u0115\2\u0806\u080a")
        buf.write("\5\u022a\u0116\2\u0807\u080a\5\u022c\u0117\2\u0808\u080a")
        buf.write("\7x\2\2\u0809\u07f8\3\2\2\2\u0809\u07f9\3\2\2\2\u0809")
        buf.write("\u07fa\3\2\2\2\u0809\u07fb\3\2\2\2\u0809\u07fc\3\2\2\2")
        buf.write("\u0809\u07fd\3\2\2\2\u0809\u07fe\3\2\2\2\u0809\u07ff\3")
        buf.write("\2\2\2\u0809\u0800\3\2\2\2\u0809\u0801\3\2\2\2\u0809\u0802")
        buf.write("\3\2\2\2\u0809\u0803\3\2\2\2\u0809\u0804\3\2\2\2\u0809")
        buf.write("\u0805\3\2\2\2\u0809\u0806\3\2\2\2\u0809\u0807\3\2\2\2")
        buf.write("\u0809\u0808\3\2\2\2\u080a\u019b\3\2\2\2\u080b\u080c\7")
        buf.write("\6\2\2\u080c\u080f\7\u0080\2\2\u080d\u0810\5\u019e\u00d0")
        buf.write("\2\u080e\u0810\7x\2\2\u080f\u080d\3\2\2\2\u080f\u080e")
        buf.write("\3\2\2\2\u0810\u0811\3\2\2\2\u0811\u080f\3\2\2\2\u0811")
        buf.write("\u0812\3\2\2\2\u0812\u0813\3\2\2\2\u0813\u0814\7\u0081")
        buf.write("\2\2\u0814\u019d\3\2\2\2\u0815\u0817\5\u01a0\u00d1\2\u0816")
        buf.write("\u0818\5\u01a2\u00d2\2\u0817\u0816\3\2\2\2\u0817\u0818")
        buf.write("\3\2\2\2\u0818\u081a\3\2\2\2\u0819\u081b\5\u01a4\u00d3")
        buf.write("\2\u081a\u0819\3\2\2\2\u081a\u081b\3\2\2\2\u081b\u081d")
        buf.write("\3\2\2\2\u081c\u081e\7\u0087\2\2\u081d\u081c\3\2\2\2\u081d")
        buf.write("\u081e\3\2\2\2\u081e\u0820\3\2\2\2\u081f\u0821\7x\2\2")
        buf.write("\u0820\u081f\3\2\2\2\u0820\u0821\3\2\2\2\u0821\u019f\3")
        buf.write("\2\2\2\u0822\u0825\5\36\20\2\u0823\u0825\5\34\17\2\u0824")
        buf.write("\u0822\3\2\2\2\u0824\u0823\3\2\2\2\u0825\u01a1\3\2\2\2")
        buf.write("\u0826\u0827\5*\26\2\u0827\u01a3\3\2\2\2\u0828\u0829\7")
        buf.write("\u008b\2\2\u0829\u0833\7}\2\2\u082a\u0834\7\u008f\2\2")
        buf.write("\u082b\u0830\5\u01a6\u00d4\2\u082c\u082d\7\u0087\2\2\u082d")
        buf.write("\u082f\5\u01a6\u00d4\2\u082e\u082c\3\2\2\2\u082f\u0832")
        buf.write("\3\2\2\2\u0830\u082e\3\2\2\2\u0830\u0831\3\2\2\2\u0831")
        buf.write("\u0834\3\2\2\2\u0832\u0830\3\2\2\2\u0833\u082a\3\2\2\2")
        buf.write("\u0833\u082b\3\2\2\2\u0834\u01a5\3\2\2\2\u0835\u0836\5")
        buf.write("\32\16\2\u0836\u01a7\3\2\2\2\u0837\u083a\5\u01aa\u00d6")
        buf.write("\2\u0838\u0839\7\u0088\2\2\u0839\u083b\5\u01ac\u00d7\2")
        buf.write("\u083a\u0838\3\2\2\2\u083a\u083b\3\2\2\2\u083b\u0841\3")
        buf.write("\2\2\2\u083c\u083e\7\u0080\2\2\u083d\u083f\5\u01ae\u00d8")
        buf.write("\2\u083e\u083d\3\2\2\2\u083e\u083f\3\2\2\2\u083f\u0840")
        buf.write("\3\2\2\2\u0840\u0842\7\u0081\2\2\u0841\u083c\3\2\2\2\u0841")
        buf.write("\u0842\3\2\2\2\u0842\u01a9\3\2\2\2\u0843\u0844\t\20\2")
        buf.write("\2\u0844\u01ab\3\2\2\2\u0845\u0846\5\32\16\2\u0846\u01ad")
        buf.write("\3\2\2\2\u0847\u0848\7K\2\2\u0848\u0849\7~\2\2\u0849\u084a")
        buf.write("\7w\2\2\u084a\u01af\3\2\2\2\u084b\u084e\7\37\2\2\u084c")
        buf.write("\u084d\7\u0088\2\2\u084d\u084f\5\u01b2\u00da\2\u084e\u084c")
        buf.write("\3\2\2\2\u084e\u084f\3\2\2\2\u084f\u0850\3\2\2\2\u0850")
        buf.write("\u0851\5*\26\2\u0851\u01b1\3\2\2\2\u0852\u0853\5\32\16")
        buf.write("\2\u0853\u01b3\3\2\2\2\u0854\u0857\7\36\2\2\u0855\u0856")
        buf.write("\7\u0088\2\2\u0856\u0858\5\u01b6\u00dc\2\u0857\u0855\3")
        buf.write("\2\2\2\u0857\u0858\3\2\2\2\u0858\u0859\3\2\2\2\u0859\u085a")
        buf.write("\5*\26\2\u085a\u01b5\3\2\2\2\u085b\u085c\5\32\16\2\u085c")
        buf.write("\u01b7\3\2\2\2\u085d\u085e\7\30\2\2\u085e\u085f\5\u01bc")
        buf.write("\u00df\2\u085f\u01b9\3\2\2\2\u0860\u0861\7\25\2\2\u0861")
        buf.write("\u0862\5\u01bc\u00df\2\u0862\u01bb\3\2\2\2\u0863\u0864")
        buf.write("\7\u0088\2\2\u0864\u0866\5\u01c0\u00e1\2\u0865\u0863\3")
        buf.write("\2\2\2\u0865\u0866\3\2\2\2\u0866\u0867\3\2\2\2\u0867\u086b")
        buf.write("\7\u0080\2\2\u0868\u086a\7x\2\2\u0869\u0868\3\2\2\2\u086a")
        buf.write("\u086d\3\2\2\2\u086b\u0869\3\2\2\2\u086b\u086c\3\2\2\2")
        buf.write("\u086c\u086e\3\2\2\2\u086d\u086b\3\2\2\2\u086e\u0870\5")
        buf.write("\u01ca\u00e6\2\u086f\u0871\5\u01cc\u00e7\2\u0870\u086f")
        buf.write("\3\2\2\2\u0870\u0871\3\2\2\2\u0871\u0883\3\2\2\2\u0872")
        buf.write("\u0882\5\u01ce\u00e8\2\u0873\u0882\5\u01e2\u00f2\2\u0874")
        buf.write("\u0882\5\u01e8\u00f5\2\u0875\u0882\5\u01fa\u00fe\2\u0876")
        buf.write("\u0882\5\u01e0\u00f1\2\u0877\u0882\5\u01d8\u00ed\2\u0878")
        buf.write("\u0882\5\u01de\u00f0\2\u0879\u0882\5\u01da\u00ee\2\u087a")
        buf.write("\u0882\5\u01dc\u00ef\2\u087b\u0882\5\u01d0\u00e9\2\u087c")
        buf.write("\u0882\5\u01d4\u00eb\2\u087d\u0882\5\u01ea\u00f6\2\u087e")
        buf.write("\u0882\5\u01ee\u00f8\2\u087f\u0882\7x\2\2\u0880\u0882")
        buf.write("\7\u0087\2\2\u0881\u0872\3\2\2\2\u0881\u0873\3\2\2\2\u0881")
        buf.write("\u0874\3\2\2\2\u0881\u0875\3\2\2\2\u0881\u0876\3\2\2\2")
        buf.write("\u0881\u0877\3\2\2\2\u0881\u0878\3\2\2\2\u0881\u0879\3")
        buf.write("\2\2\2\u0881\u087a\3\2\2\2\u0881\u087b\3\2\2\2\u0881\u087c")
        buf.write("\3\2\2\2\u0881\u087d\3\2\2\2\u0881\u087e\3\2\2\2\u0881")
        buf.write("\u087f\3\2\2\2\u0881\u0880\3\2\2\2\u0882\u0885\3\2\2\2")
        buf.write("\u0883\u0881\3\2\2\2\u0883\u0884\3\2\2\2\u0884\u0889\3")
        buf.write("\2\2\2\u0885\u0883\3\2\2\2\u0886\u0888\7x\2\2\u0887\u0886")
        buf.write("\3\2\2\2\u0888\u088b\3\2\2\2\u0889\u0887\3\2\2\2\u0889")
        buf.write("\u088a\3\2\2\2\u088a\u088e\3\2\2\2\u088b\u0889\3\2\2\2")
        buf.write("\u088c\u088f\5\u01c2\u00e2\2\u088d\u088f\5\u01c6\u00e4")
        buf.write("\2\u088e\u088c\3\2\2\2\u088e\u088d\3\2\2\2\u088e\u088f")
        buf.write("\3\2\2\2\u088f\u0893\3\2\2\2\u0890\u0892\7x\2\2\u0891")
        buf.write("\u0890\3\2\2\2\u0892\u0895\3\2\2\2\u0893\u0891\3\2\2\2")
        buf.write("\u0893\u0894\3\2\2\2\u0894\u0899\3\2\2\2\u0895\u0893\3")
        buf.write("\2\2\2\u0896\u0898\5\u01be\u00e0\2\u0897\u0896\3\2\2\2")
        buf.write("\u0898\u089b\3\2\2\2\u0899\u0897\3\2\2\2\u0899\u089a\3")
        buf.write("\2\2\2\u089a\u089f\3\2\2\2\u089b\u0899\3\2\2\2\u089c\u089e")
        buf.write("\7x\2\2\u089d\u089c\3\2\2\2\u089e\u08a1\3\2\2\2\u089f")
        buf.write("\u089d\3\2\2\2\u089f\u08a0\3\2\2\2\u08a0\u08a2\3\2\2\2")
        buf.write("\u08a1\u089f\3\2\2\2\u08a2\u08a3\7\u0081\2\2\u08a3\u01bd")
        buf.write("\3\2\2\2\u08a4\u08a8\5\u01e6\u00f4\2\u08a5\u08a7\7x\2")
        buf.write("\2\u08a6\u08a5\3\2\2\2\u08a7\u08aa\3\2\2\2\u08a8\u08a6")
        buf.write("\3\2\2\2\u08a8\u08a9\3\2\2\2\u08a9\u08ab\3\2\2\2\u08aa")
        buf.write("\u08a8\3\2\2\2\u08ab\u08af\7\u0080\2\2\u08ac\u08ae\7x")
        buf.write("\2\2\u08ad\u08ac\3\2\2\2\u08ae\u08b1\3\2\2\2\u08af\u08ad")
        buf.write("\3\2\2\2\u08af\u08b0\3\2\2\2\u08b0\u08b2\3\2\2\2\u08b1")
        buf.write("\u08af\3\2\2\2\u08b2\u08b6\5\u0188\u00c5\2\u08b3\u08b5")
        buf.write("\7x\2\2\u08b4\u08b3\3\2\2\2\u08b5\u08b8\3\2\2\2\u08b6")
        buf.write("\u08b4\3\2\2\2\u08b6\u08b7\3\2\2\2\u08b7\u08b9\3\2\2\2")
        buf.write("\u08b8\u08b6\3\2\2\2\u08b9\u08bd\7\u0081\2\2\u08ba\u08bc")
        buf.write("\7x\2\2\u08bb\u08ba\3\2\2\2\u08bc\u08bf\3\2\2\2\u08bd")
        buf.write("\u08bb\3\2\2\2\u08bd\u08be\3\2\2\2\u08be\u01bf\3\2\2\2")
        buf.write("\u08bf\u08bd\3\2\2\2\u08c0\u08c1\5\32\16\2\u08c1\u01c1")
        buf.write("\3\2\2\2\u08c2\u08c3\7\u0080\2\2\u08c3\u08c4\5\u01c4\u00e3")
        buf.write("\2\u08c4\u08c5\7\u0081\2\2\u08c5\u08c7\3\2\2\2\u08c6\u08c2")
        buf.write("\3\2\2\2\u08c6\u08c7\3\2\2\2\u08c7\u08c8\3\2\2\2\u08c8")
        buf.write("\u08c9\7\u008b\2\2\u08c9\u08ca\7}\2\2\u08ca\u08cb\5*\26")
        buf.write("\2\u08cb\u01c3\3\2\2\2\u08cc\u08cd\t\21\2\2\u08cd\u01c5")
        buf.write("\3\2\2\2\u08ce\u08cf\7\u0080\2\2\u08cf\u08d0\5\u01c4\u00e3")
        buf.write("\2\u08d0\u08d1\7\u0081\2\2\u08d1\u08d3\3\2\2\2\u08d2\u08ce")
        buf.write("\3\2\2\2\u08d2\u08d3\3\2\2\2\u08d3\u08d4\3\2\2\2\u08d4")
        buf.write("\u08d5\7\u008b\2\2\u08d5\u08d6\7}\2\2\u08d6\u08d7\5\u01c8")
        buf.write("\u00e5\2\u08d7\u01c7\3\2\2\2\u08d8\u08d9\t\3\2\2\u08d9")
        buf.write("\u01c9\3\2\2\2\u08da\u08dd\5\36\20\2\u08db\u08dd\5\34")
        buf.write("\17\2\u08dc\u08da\3\2\2\2\u08dc\u08db\3\2\2\2\u08dd\u01cb")
        buf.write("\3\2\2\2\u08de\u08df\5*\26\2\u08df\u01cd\3\2\2\2\u08e0")
        buf.write("\u08e1\7F\2\2\u08e1\u08e2\7~\2\2\u08e2\u08e3\5\32\16\2")
        buf.write("\u08e3\u01cf\3\2\2\2\u08e4\u08e5\7P\2\2\u08e5\u08e6\7")
        buf.write("~\2\2\u08e6\u08e7\5\u01d2\u00ea\2\u08e7\u01d1\3\2\2\2")
        buf.write("\u08e8\u08e9\t\3\2\2\u08e9\u01d3\3\2\2\2\u08ea\u08eb\7")
        buf.write("O\2\2\u08eb\u08ec\7~\2\2\u08ec\u08ed\5\u01d6\u00ec\2\u08ed")
        buf.write("\u01d5\3\2\2\2\u08ee\u08ef\t\3\2\2\u08ef\u01d7\3\2\2\2")
        buf.write("\u08f0\u08f1\7T\2\2\u08f1\u08f2\7~\2\2\u08f2\u08f3\5\32")
        buf.write("\16\2\u08f3\u01d9\3\2\2\2\u08f4\u08f8\7R\2\2\u08f5\u08f9")
        buf.write("\5(\25\2\u08f6\u08f7\7~\2\2\u08f7\u08f9\5*\26\2\u08f8")
        buf.write("\u08f5\3\2\2\2\u08f8\u08f6\3\2\2\2\u08f9\u01db\3\2\2\2")
        buf.write("\u08fa\u08fe\7Q\2\2\u08fb\u08ff\5(\25\2\u08fc\u08fd\7")
        buf.write("~\2\2\u08fd\u08ff\5*\26\2\u08fe\u08fb\3\2\2\2\u08fe\u08fc")
        buf.write("\3\2\2\2\u08ff\u01dd\3\2\2\2\u0900\u0901\7S\2\2\u0901")
        buf.write("\u0902\7~\2\2\u0902\u0903\5\32\16\2\u0903\u01df\3\2\2")
        buf.write("\2\u0904\u0905\7U\2\2\u0905\u0906\7~\2\2\u0906\u0907\5")
        buf.write("\32\16\2\u0907\u01e1\3\2\2\2\u0908\u0909\7[\2\2\u0909")
        buf.write("\u090a\7~\2\2\u090a\u090b\5\u01e4\u00f3\2\u090b\u01e3")
        buf.write("\3\2\2\2\u090c\u0911\5\u01e6\u00f4\2\u090d\u090e\7\u0087")
        buf.write("\2\2\u090e\u0910\5\u01e6\u00f4\2\u090f\u090d\3\2\2\2\u0910")
        buf.write("\u0913\3\2\2\2\u0911\u090f\3\2\2\2\u0911\u0912\3\2\2\2")
        buf.write("\u0912\u01e5\3\2\2\2\u0913\u0911\3\2\2\2\u0914\u0915\t")
        buf.write("\22\2\2\u0915\u01e7\3\2\2\2\u0916\u0917\7s\2\2\u0917\u0918")
        buf.write("\7~\2\2\u0918\u0919\5\u01f2\u00fa\2\u0919\u01e9\3\2\2")
        buf.write("\2\u091a\u091b\7n\2\2\u091b\u091c\7~\2\2\u091c\u091d\5")
        buf.write("\u01ec\u00f7\2\u091d\u01eb\3\2\2\2\u091e\u091f\t\f\2\2")
        buf.write("\u091f\u01ed\3\2\2\2\u0920\u0921\7H\2\2\u0921\u0922\7")
        buf.write("~\2\2\u0922\u0923\5\u01f0\u00f9\2\u0923\u01ef\3\2\2\2")
        buf.write("\u0924\u0925\7w\2\2\u0925\u01f1\3\2\2\2\u0926\u092b\5")
        buf.write("\u01f4\u00fb\2\u0927\u0928\7\u0087\2\2\u0928\u092a\5\u01f4")
        buf.write("\u00fb\2\u0929\u0927\3\2\2\2\u092a\u092d\3\2\2\2\u092b")
        buf.write("\u0929\3\2\2\2\u092b\u092c\3\2\2\2\u092c\u01f3\3\2\2\2")
        buf.write("\u092d\u092b\3\2\2\2\u092e\u0930\5\u01f6\u00fc\2\u092f")
        buf.write("\u0931\5\u01f8\u00fd\2\u0930\u092f\3\2\2\2\u0930\u0931")
        buf.write("\3\2\2\2\u0931\u01f5\3\2\2\2\u0932\u0938\7\u008f\2\2\u0933")
        buf.write("\u0935\7\177\2\2\u0934\u0933\3\2\2\2\u0934\u0935\3\2\2")
        buf.write("\2\u0935\u0936\3\2\2\2\u0936\u0938\5\32\16\2\u0937\u0932")
        buf.write("\3\2\2\2\u0937\u0934\3\2\2\2\u0938\u01f7\3\2\2\2\u0939")
        buf.write("\u093a\5*\26\2\u093a\u01f9\3\2\2\2\u093b\u093c\7V\2\2")
        buf.write("\u093c\u093d\7~\2\2\u093d\u093e\5\u01fc\u00ff\2\u093e")
        buf.write("\u01fb\3\2\2\2\u093f\u0944\5\u01fe\u0100\2\u0940\u0941")
        buf.write("\7\u0087\2\2\u0941\u0943\5\u01fe\u0100\2\u0942\u0940\3")
        buf.write("\2\2\2\u0943\u0946\3\2\2\2\u0944\u0942\3\2\2\2\u0944\u0945")
        buf.write("\3\2\2\2\u0945\u01fd\3\2\2\2\u0946\u0944\3\2\2\2\u0947")
        buf.write("\u0948\5\u0200\u0101\2\u0948\u01ff\3\2\2\2\u0949\u094f")
        buf.write("\7\u008f\2\2\u094a\u094c\7\177\2\2\u094b\u094a\3\2\2\2")
        buf.write("\u094b\u094c\3\2\2\2\u094c\u094d\3\2\2\2\u094d\u094f\5")
        buf.write("\32\16\2\u094e\u0949\3\2\2\2\u094e\u094b\3\2\2\2\u094f")
        buf.write("\u0201\3\2\2\2\u0950\u0952\7\33\2\2\u0951\u0953\5*\26")
        buf.write("\2\u0952\u0951\3\2\2\2\u0952\u0953\3\2\2\2\u0953\u0203")
        buf.write("\3\2\2\2\u0954\u0956\7\35\2\2\u0955\u0957\5*\26\2\u0956")
        buf.write("\u0955\3\2\2\2\u0956\u0957\3\2\2\2\u0957\u0205\3\2\2\2")
        buf.write("\u0958\u0959\7\32\2\2\u0959\u095a\5\u01bc\u00df\2\u095a")
        buf.write("\u0207\3\2\2\2\u095b\u095c\7\31\2\2\u095c\u095d\5\u01bc")
        buf.write("\u00df\2\u095d\u0209\3\2\2\2\u095e\u095f\7\27\2\2\u095f")
        buf.write("\u0960\5\u01bc\u00df\2\u0960\u020b\3\2\2\2\u0961\u0962")
        buf.write("\7\24\2\2\u0962\u0963\7\u0088\2\2\u0963\u0964\5\u020e")
        buf.write("\u0108\2\u0964\u0968\7\u0080\2\2\u0965\u0967\7x\2\2\u0966")
        buf.write("\u0965\3\2\2\2\u0967\u096a\3\2\2\2\u0968\u0966\3\2\2\2")
        buf.write("\u0968\u0969\3\2\2\2\u0969\u096c\3\2\2\2\u096a\u0968\3")
        buf.write("\2\2\2\u096b\u096d\5\u0210\u0109\2\u096c\u096b\3\2\2\2")
        buf.write("\u096d\u096e\3\2\2\2\u096e\u096c\3\2\2\2\u096e\u096f\3")
        buf.write("\2\2\2\u096f\u0973\3\2\2\2\u0970\u0972\7x\2\2\u0971\u0970")
        buf.write("\3\2\2\2\u0972\u0975\3\2\2\2\u0973\u0971\3\2\2\2\u0973")
        buf.write("\u0974\3\2\2\2\u0974\u0976\3\2\2\2\u0975\u0973\3\2\2\2")
        buf.write("\u0976\u0977\7\u0081\2\2\u0977\u020d\3\2\2\2\u0978\u0979")
        buf.write("\5\32\16\2\u0979\u020f\3\2\2\2\u097a\u097c\7\u0087\2\2")
        buf.write("\u097b\u097a\3\2\2\2\u097b\u097c\3\2\2\2\u097c\u0980\3")
        buf.write("\2\2\2\u097d\u097f\7x\2\2\u097e\u097d\3\2\2\2\u097f\u0982")
        buf.write("\3\2\2\2\u0980\u097e\3\2\2\2\u0980\u0981\3\2\2\2\u0981")
        buf.write("\u0984\3\2\2\2\u0982\u0980\3\2\2\2\u0983\u0985\5\u0216")
        buf.write("\u010c\2\u0984\u0983\3\2\2\2\u0984\u0985\3\2\2\2\u0985")
        buf.write("\u0986\3\2\2\2\u0986\u0989\5\u0224\u0113\2\u0987\u098a")
        buf.write("\5\u0214\u010b\2\u0988\u098a\5\u0212\u010a\2\u0989\u0987")
        buf.write("\3\2\2\2\u0989\u0988\3\2\2\2\u098a\u098e\3\2\2\2\u098b")
        buf.write("\u098d\7x\2\2\u098c\u098b\3\2\2\2\u098d\u0990\3\2\2\2")
        buf.write("\u098e\u098c\3\2\2\2\u098e\u098f\3\2\2\2\u098f\u0211\3")
        buf.write("\2\2\2\u0990\u098e\3\2\2\2\u0991\u0994\7~\2\2\u0992\u0995")
        buf.write("\5\u0220\u0111\2\u0993\u0995\5\u021e\u0110\2\u0994\u0992")
        buf.write("\3\2\2\2\u0994\u0993\3\2\2\2\u0995\u0213\3\2\2\2\u0996")
        buf.write("\u0997\5(\25\2\u0997\u0215\3\2\2\2\u0998\u0999\7\u0082")
        buf.write("\2\2\u0999\u099e\5\u0218\u010d\2\u099a\u099b\7\u0087\2")
        buf.write("\2\u099b\u099d\5\u0218\u010d\2\u099c\u099a\3\2\2\2\u099d")
        buf.write("\u09a0\3\2\2\2\u099e\u099c\3\2\2\2\u099e\u099f\3\2\2\2")
        buf.write("\u099f\u09a1\3\2\2\2\u09a0\u099e\3\2\2\2\u09a1\u09a2\7")
        buf.write("\u0083\2\2\u09a2\u0217\3\2\2\2\u09a3\u09a4\5\u021a\u010e")
        buf.write("\2\u09a4\u09a5\7\u008b\2\2\u09a5\u09a6\5\u021c\u010f\2")
        buf.write("\u09a6\u0219\3\2\2\2\u09a7\u09a8\5\32\16\2\u09a8\u021b")
        buf.write("\3\2\2\2\u09a9\u09ad\7\u0092\2\2\u09aa\u09ad\7\u0093\2")
        buf.write("\2\u09ab\u09ad\5\32\16\2\u09ac\u09a9\3\2\2\2\u09ac\u09aa")
        buf.write("\3\2\2\2\u09ac\u09ab\3\2\2\2\u09ad\u021d\3\2\2\2\u09ae")
        buf.write("\u09af\t\3\2\2\u09af\u021f\3\2\2\2\u09b0\u09b1\7N\2\2")
        buf.write("\u09b1\u09b2\7\u0080\2\2\u09b2\u09b3\5\u0222\u0112\2\u09b3")
        buf.write("\u09b4\7\u0081\2\2\u09b4\u0221\3\2\2\2\u09b5\u09b6\5\32")
        buf.write("\16\2\u09b6\u09b7\7\u0088\2\2\u09b7\u09b9\3\2\2\2\u09b8")
        buf.write("\u09b5\3\2\2\2\u09b8\u09b9\3\2\2\2\u09b9\u09ba\3\2\2\2")
        buf.write("\u09ba\u09bb\5\32\16\2\u09bb\u0223\3\2\2\2\u09bc\u09c0")
        buf.write("\7\u0092\2\2\u09bd\u09c0\7\u0093\2\2\u09be\u09c0\5\32")
        buf.write("\16\2\u09bf\u09bc\3\2\2\2\u09bf\u09bd\3\2\2\2\u09bf\u09be")
        buf.write("\3\2\2\2\u09c0\u0225\3\2\2\2\u09c1\u09c2\7\26\2\2\u09c2")
        buf.write("\u09c3\5\u01bc\u00df\2\u09c3\u0227\3\2\2\2\u09c4\u09c5")
        buf.write("\7\21\2\2\u09c5\u0229\3\2\2\2\u09c6\u09c8\7\23\2\2\u09c7")
        buf.write("\u09c9\5*\26\2\u09c8\u09c7\3\2\2\2\u09c8\u09c9\3\2\2\2")
        buf.write("\u09c9\u022b\3\2\2\2\u09ca\u09cb\7\34\2\2\u09cb\u09cc")
        buf.write("\7\u0080\2\2\u09cc\u09cd\5\u022e\u0118\2\u09cd\u09ce\7")
        buf.write("\u0081\2\2\u09ce\u022d\3\2\2\2\u09cf\u09d0\7z\2\2\u09d0")
        buf.write("\u022f\3\2\2\2\u0109\u0233\u0239\u023f\u0243\u0248\u024a")
        buf.write("\u024f\u0253\u0258\u025a\u025f\u0267\u026c\u0274\u027b")
        buf.write("\u027e\u0287\u028d\u0290\u029f\u02a6\u02ab\u02b3\u02b9")
        buf.write("\u02be\u02c1\u02c4\u02c8\u02d0\u02e2\u02e9\u02f0\u02f5")
        buf.write("\u02fa\u02ff\u0306\u030a\u030f\u0315\u031a\u0326\u032a")
        buf.write("\u032f\u0334\u0338\u033e\u0348\u0350\u0353\u0358\u0360")
        buf.write("\u0368\u036d\u0371\u0377\u037b\u0383\u038a\u0392\u039a")
        buf.write("\u039f\u03a3\u03a6\u03ab\u03b2\u03bc\u03be\u03c4\u03c6")
        buf.write("\u03cc\u03ce\u03d3\u03e0\u03ef\u03f8\u0404\u0409\u040e")
        buf.write("\u0414\u041a\u0420\u0426\u042e\u0431\u0435\u0439\u0444")
        buf.write("\u044a\u044f\u0456\u045d\u0462\u0465\u0468\u046d\u0470")
        buf.write("\u0474\u0479\u047e\u0483\u0496\u049a\u04b8\u04d7\u04db")
        buf.write("\u04e6\u04ea\u04f1\u04fb\u0504\u0508\u050f\u051e\u0528")
        buf.write("\u0531\u053a\u0549\u0552\u0556\u0559\u0578\u0588\u058a")
        buf.write("\u0590\u0594\u0599\u05a1\u05a9\u05af\u05b9\u05c7\u05d1")
        buf.write("\u05d3\u05d7\u05f0\u05f5\u0605\u060e\u0617\u0620\u0629")
        buf.write("\u0632\u063d\u0640\u0644\u064d\u0653\u0659\u065b\u066b")
        buf.write("\u066d\u0678\u0681\u0689\u068e\u0694\u0699\u069f\u06a4")
        buf.write("\u06aa\u06b3\u06bc\u06c3\u06c8\u06d4\u06dd\u06eb\u06f2")
        buf.write("\u06fd\u06ff\u0712\u0720\u0747\u074e\u0753\u0757\u075b")
        buf.write("\u075f\u0761\u0765\u076a\u0777\u077e\u0786\u0788\u078b")
        buf.write("\u0792\u0794\u079c\u07a3\u07a6\u07a8\u07af\u07b5\u07b9")
        buf.write("\u07be\u07c4\u07cf\u07d2\u07db\u07df\u07e4\u07e7\u07f0")
        buf.write("\u07f4\u0809\u080f\u0811\u0817\u081a\u081d\u0820\u0824")
        buf.write("\u0830\u0833\u083a\u083e\u0841\u084e\u0857\u0865\u086b")
        buf.write("\u0870\u0881\u0883\u0889\u088e\u0893\u0899\u089f\u08a8")
        buf.write("\u08af\u08b6\u08bd\u08c6\u08d2\u08dc\u08f8\u08fe\u0911")
        buf.write("\u092b\u0930\u0934\u0937\u0944\u094b\u094e\u0952\u0956")
        buf.write("\u0968\u096e\u0973\u097b\u0980\u0984\u0989\u098e\u0994")
        buf.write("\u099e\u09ac\u09b8\u09bf\u09c8")
        return buf.getvalue()


class ZmeiLangParser ( Parser ):

    grammarFileName = "ZmeiLangParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'@admin'", "'@suit'", "'@celery'", "'@stream'", 
                     "'@channels'", "'@docker'", "'@api'", "'@rest'", "'@filer'", 
                     "'@gitlab'", "'@react'", "'@react_client'", "'@react_server'", 
                     "'@theme'", "'@@'", "'@file'", "'@get'", "'@menu'", 
                     "'@crud'", "'@crud_detail'", "'@crud_list'", "'@crud_delete'", 
                     "'@crud_edit'", "'@crud_create'", "'@post'", "'@error'", 
                     "'@auth'", "'@markdown'", "'@html'", "'@tree'", "'@date_tree'", 
                     "'@mixin'", "'@m2m_changed'", "'@post_delete'", "'@pre_delete'", 
                     "'@post_save'", "'@pre_save'", "'@clean'", "'@order'", 
                     "'@sortable'", "'@langs'", "'basic'", "'session'", 
                     "'token'", "'text'", "'html'", "'html_media'", "'float'", 
                     "'decimal'", "'date'", "'datetime'", "'create_time'", 
                     "'update_time'", "'image'", "'file'", "'filer_image'", 
                     "'filer_file'", "'filer_folder'", "'filer_image_folder'", 
                     "'str'", "'int'", "'slug'", "'bool'", "'one'", "'one2one'", 
                     "'many'", "'choices'", "'theme'", "'install'", "'header'", 
                     "'services'", "'selenium_pytest'", "'child'", "'filter_out'", 
                     "'filter_in'", "'page'", "'link_suffix'", "'url_prefix'", 
                     "'can_edit'", "'object_expr'", "'block'", "'item_name'", 
                     "'pk_param'", "'list_fields'", "'delete'", "'edit'", 
                     "'create'", "'detail'", "'skip'", "'from'", "'+polymorphic_list'", 
                     "'css'", "'js'", "'tabular'", "'stacked'", "'polymorphic'", 
                     "'inline'", "'type'", "'user_field'", "'annotate'", 
                     "'on_create'", "'query'", "'auth'", "'count'", "'i18n'", 
                     "'extension'", "'tabs'", "'list'", "'read_only'", "'list_editable'", 
                     "'list_filter'", "'list_search'", "'fields'", "'import'", 
                     "'as'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'<'", "'>'", "':'", "'^'", 
                     "'('", "')'", "'['", "']'", "'?'", "'_'", "'-'", "','", 
                     "'.'", "'#'", "'/'", "'='", "'$'", "'&'", "'!'", "'*'", 
                     "'~'", "'|'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "' '", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "';'", "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "AN_ADMIN", "AN_SUIT", "AN_CELERY", "AN_STREAM", 
                      "AN_CHANNELS", "AN_DOCKER", "AN_API", "AN_REST", "AN_FILER", 
                      "AN_GITLAB", "AN_REACT", "AN_REACT_CLIENT", "AN_REACT_SERVER", 
                      "AN_THEME", "AN_PRIORITY", "AN_FILE", "AN_GET", "AN_MENU", 
                      "AN_CRUD", "AN_CRUD_DETAIL", "AN_CRUD_LIST", "AN_CRUD_DELETE", 
                      "AN_CRUD_EDIT", "AN_CRUD_CREATE", "AN_POST", "AN_ERROR", 
                      "AN_AUTH", "AN_MARKDOWN", "AN_HTML", "AN_TREE", "AN_DATE_TREE", 
                      "AN_MIXIN", "AN_M2M_CHANGED", "AN_POST_DELETE", "AN_PRE_DELETE", 
                      "AN_POST_SAVE", "AN_PRE_SAVE", "AN_CLEAN", "AN_ORDER", 
                      "AN_SORTABLE", "AN_LANGS", "KW_AUTH_TYPE_BASIC", "KW_AUTH_TYPE_SESSION", 
                      "KW_AUTH_TYPE_TOKEN", "COL_FIELD_TYPE_LONGTEXT", "COL_FIELD_TYPE_HTML", 
                      "COL_FIELD_TYPE_HTML_MEDIA", "COL_FIELD_TYPE_FLOAT", 
                      "COL_FIELD_TYPE_DECIMAL", "COL_FIELD_TYPE_DATE", "COL_FIELD_TYPE_DATETIME", 
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
                      "KW_CREATE", "KW_DETAIL", "KW_SKIP", "KW_FROM", "KW_POLY_LIST", 
                      "KW_CSS", "KW_JS", "KW_INLINE_TYPE_TABULAR", "KW_INLINE_TYPE_STACKED", 
                      "KW_INLINE_TYPE_POLYMORPHIC", "KW_INLINE", "KW_TYPE", 
                      "KW_USER_FIELD", "KW_ANNOTATE", "KW_ON_CREATE", "KW_QUERY", 
                      "KW_AUTH", "KW_COUNT", "KW_I18N", "KW_EXTENSION", 
                      "KW_TABS", "KW_LIST", "KW_READ_ONLY", "KW_LIST_EDITABLE", 
                      "KW_LIST_FILTER", "KW_LIST_SEARCH", "KW_FIELDS", "KW_IMPORT", 
                      "KW_AS", "WRITE_MODE", "BOOL", "NL", "ID", "DIGIT", 
                      "SIZE2D", "LT", "GT", "COLON", "EXCLUDE", "BRACE_OPEN", 
                      "BRACE_CLOSE", "SQ_BRACE_OPEN", "SQ_BRACE_CLOSE", 
                      "QUESTION_MARK", "UNDERSCORE", "DASH", "COMA", "DOT", 
                      "HASH", "SLASH", "EQUALS", "DOLLAR", "AMP", "EXCLAM", 
                      "STAR", "APPROX", "PIPE", "STRING_DQ", "STRING_SQ", 
                      "COMMENT_LINE", "COMMENT_BLOCK", "UNICODE", "WS", 
                      "COL_FIELD_CALCULATED", "ASSIGN", "ASSIGN_STATIC", 
                      "CODE_BLOCK", "ERRCHAR", "PYTHON_CODE", "PYTHON_LINE_ERRCHAR", 
                      "PYTHON_LINE_END", "PYTHON_EXPR_ERRCHAR", "PYTHON_LINE_NL" ]

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
    RULE_inline_type_name = 124
    RULE_inline_extension = 125
    RULE_inline_fields = 126
    RULE_an_admin_tabs = 127
    RULE_an_admin_tab = 128
    RULE_tab_name = 129
    RULE_tab_verbose_name = 130
    RULE_an_admin_list = 131
    RULE_an_admin_read_only = 132
    RULE_an_admin_list_editable = 133
    RULE_an_admin_list_filter = 134
    RULE_an_admin_list_search = 135
    RULE_an_admin_fields = 136
    RULE_an_api = 137
    RULE_an_api_all = 138
    RULE_an_api_name = 139
    RULE_an_rest = 140
    RULE_an_rest_config = 141
    RULE_an_rest_main_part = 142
    RULE_an_rest_descriptor = 143
    RULE_an_rest_i18n = 144
    RULE_an_rest_str = 145
    RULE_an_rest_query = 146
    RULE_an_rest_on_create = 147
    RULE_an_rest_filter_in = 148
    RULE_an_rest_filter_out = 149
    RULE_an_rest_read_only = 150
    RULE_an_rest_user_field = 151
    RULE_an_rest_fields = 152
    RULE_an_rest_fields_write_mode = 153
    RULE_an_rest_auth = 154
    RULE_an_rest_auth_type = 155
    RULE_an_rest_auth_type_name = 156
    RULE_an_rest_auth_token_model = 157
    RULE_an_rest_auth_token_class = 158
    RULE_an_rest_annotate = 159
    RULE_an_rest_annotate_count = 160
    RULE_an_rest_annotate_count_field = 161
    RULE_an_rest_annotate_count_alias = 162
    RULE_an_rest_inline = 163
    RULE_an_rest_inline_decl = 164
    RULE_an_rest_inline_name = 165
    RULE_an_order = 166
    RULE_an_order_fields = 167
    RULE_an_clean = 168
    RULE_an_pre_delete = 169
    RULE_an_tree = 170
    RULE_an_tree_poly = 171
    RULE_an_mixin = 172
    RULE_an_date_tree = 173
    RULE_an_date_tree_field = 174
    RULE_an_m2m_changed = 175
    RULE_an_post_save = 176
    RULE_an_pre_save = 177
    RULE_an_post_delete = 178
    RULE_an_sortable = 179
    RULE_an_sortable_field_name = 180
    RULE_page = 181
    RULE_page_header = 182
    RULE_page_base = 183
    RULE_page_alias = 184
    RULE_page_alias_name = 185
    RULE_page_template = 186
    RULE_template_name = 187
    RULE_file_name_part = 188
    RULE_page_url = 189
    RULE_url_part = 190
    RULE_url_param = 191
    RULE_url_segment = 192
    RULE_url_segments = 193
    RULE_page_name = 194
    RULE_page_body = 195
    RULE_page_code = 196
    RULE_page_field = 197
    RULE_page_field_name = 198
    RULE_page_field_code = 199
    RULE_page_function = 200
    RULE_page_function_name = 201
    RULE_page_function_args = 202
    RULE_page_function_arg = 203
    RULE_page_annotation = 204
    RULE_an_stream = 205
    RULE_an_stream_model = 206
    RULE_an_stream_target_model = 207
    RULE_an_stream_target_filter = 208
    RULE_an_stream_field_list = 209
    RULE_an_stream_field_name = 210
    RULE_an_react = 211
    RULE_an_react_type = 212
    RULE_an_react_descriptor = 213
    RULE_an_react_child = 214
    RULE_an_html = 215
    RULE_an_html_descriptor = 216
    RULE_an_markdown = 217
    RULE_an_markdown_descriptor = 218
    RULE_an_crud_delete = 219
    RULE_an_crud = 220
    RULE_an_crud_params = 221
    RULE_an_crud_page_override = 222
    RULE_an_crud_descriptor = 223
    RULE_an_crud_next_page = 224
    RULE_an_crud_next_page_event_name = 225
    RULE_an_crud_next_page_url = 226
    RULE_an_crud_next_page_url_val = 227
    RULE_an_crud_target_model = 228
    RULE_an_crud_target_filter = 229
    RULE_an_crud_theme = 230
    RULE_an_crud_url_prefix = 231
    RULE_an_crud_url_prefix_val = 232
    RULE_an_crud_link_suffix = 233
    RULE_an_crud_link_suffix_val = 234
    RULE_an_crud_item_name = 235
    RULE_an_crud_object_expr = 236
    RULE_an_crud_can_edit = 237
    RULE_an_crud_block = 238
    RULE_an_crud_pk_param = 239
    RULE_an_crud_skip = 240
    RULE_an_crud_skip_values = 241
    RULE_an_crud_view_name = 242
    RULE_an_crud_fields = 243
    RULE_an_crud_list_type = 244
    RULE_an_crud_list_type_var = 245
    RULE_an_crud_header = 246
    RULE_an_crud_header_enabled = 247
    RULE_an_crud_fields_expr = 248
    RULE_an_crud_field = 249
    RULE_an_crud_field_spec = 250
    RULE_an_crud_field_filter = 251
    RULE_an_crud_list_fields = 252
    RULE_an_crud_list_fields_expr = 253
    RULE_an_crud_list_field = 254
    RULE_an_crud_list_field_spec = 255
    RULE_an_post = 256
    RULE_an_auth = 257
    RULE_an_crud_create = 258
    RULE_an_crud_edit = 259
    RULE_an_crud_list = 260
    RULE_an_menu = 261
    RULE_an_menu_descriptor = 262
    RULE_an_menu_item = 263
    RULE_an_menu_target = 264
    RULE_an_menu_item_code = 265
    RULE_an_menu_item_args = 266
    RULE_an_menu_item_arg = 267
    RULE_an_menu_item_arg_key = 268
    RULE_an_menu_item_arg_val = 269
    RULE_an_menu_item_url = 270
    RULE_an_menu_item_page = 271
    RULE_an_menu_item_page_ref = 272
    RULE_an_menu_label = 273
    RULE_an_crud_detail = 274
    RULE_an_priority_marker = 275
    RULE_an_get = 276
    RULE_an_error = 277
    RULE_an_error_code = 278

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
                   "inline_name", "inline_type", "inline_type_name", "inline_extension", 
                   "inline_fields", "an_admin_tabs", "an_admin_tab", "tab_name", 
                   "tab_verbose_name", "an_admin_list", "an_admin_read_only", 
                   "an_admin_list_editable", "an_admin_list_filter", "an_admin_list_search", 
                   "an_admin_fields", "an_api", "an_api_all", "an_api_name", 
                   "an_rest", "an_rest_config", "an_rest_main_part", "an_rest_descriptor", 
                   "an_rest_i18n", "an_rest_str", "an_rest_query", "an_rest_on_create", 
                   "an_rest_filter_in", "an_rest_filter_out", "an_rest_read_only", 
                   "an_rest_user_field", "an_rest_fields", "an_rest_fields_write_mode", 
                   "an_rest_auth", "an_rest_auth_type", "an_rest_auth_type_name", 
                   "an_rest_auth_token_model", "an_rest_auth_token_class", 
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
                   "page_function_arg", "page_annotation", "an_stream", 
                   "an_stream_model", "an_stream_target_model", "an_stream_target_filter", 
                   "an_stream_field_list", "an_stream_field_name", "an_react", 
                   "an_react_type", "an_react_descriptor", "an_react_child", 
                   "an_html", "an_html_descriptor", "an_markdown", "an_markdown_descriptor", 
                   "an_crud_delete", "an_crud", "an_crud_params", "an_crud_page_override", 
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
    AN_ADMIN=1
    AN_SUIT=2
    AN_CELERY=3
    AN_STREAM=4
    AN_CHANNELS=5
    AN_DOCKER=6
    AN_API=7
    AN_REST=8
    AN_FILER=9
    AN_GITLAB=10
    AN_REACT=11
    AN_REACT_CLIENT=12
    AN_REACT_SERVER=13
    AN_THEME=14
    AN_PRIORITY=15
    AN_FILE=16
    AN_GET=17
    AN_MENU=18
    AN_CRUD=19
    AN_CRUD_DETAIL=20
    AN_CRUD_LIST=21
    AN_CRUD_DELETE=22
    AN_CRUD_EDIT=23
    AN_CRUD_CREATE=24
    AN_POST=25
    AN_ERROR=26
    AN_AUTH=27
    AN_MARKDOWN=28
    AN_HTML=29
    AN_TREE=30
    AN_DATE_TREE=31
    AN_MIXIN=32
    AN_M2M_CHANGED=33
    AN_POST_DELETE=34
    AN_PRE_DELETE=35
    AN_POST_SAVE=36
    AN_PRE_SAVE=37
    AN_CLEAN=38
    AN_ORDER=39
    AN_SORTABLE=40
    AN_LANGS=41
    KW_AUTH_TYPE_BASIC=42
    KW_AUTH_TYPE_SESSION=43
    KW_AUTH_TYPE_TOKEN=44
    COL_FIELD_TYPE_LONGTEXT=45
    COL_FIELD_TYPE_HTML=46
    COL_FIELD_TYPE_HTML_MEDIA=47
    COL_FIELD_TYPE_FLOAT=48
    COL_FIELD_TYPE_DECIMAL=49
    COL_FIELD_TYPE_DATE=50
    COL_FIELD_TYPE_DATETIME=51
    COL_FIELD_TYPE_CREATE_TIME=52
    COL_FIELD_TYPE_UPDATE_TIME=53
    COL_FIELD_TYPE_IMAGE=54
    COL_FIELD_TYPE_FILE=55
    COL_FIELD_TYPE_FILER_IMAGE=56
    COL_FIELD_TYPE_FILER_FILE=57
    COL_FIELD_TYPE_FILER_FOLDER=58
    COL_FIELD_TYPE_FILER_IMAGE_FOLDER=59
    COL_FIELD_TYPE_TEXT=60
    COL_FIELD_TYPE_INT=61
    COL_FIELD_TYPE_SLUG=62
    COL_FIELD_TYPE_BOOL=63
    COL_FIELD_TYPE_ONE=64
    COL_FIELD_TYPE_ONE2ONE=65
    COL_FIELD_TYPE_MANY=66
    COL_FIELD_CHOICES=67
    KW_THEME=68
    KW_INSTALL=69
    KW_HEADER=70
    KW_SERVICES=71
    KW_SELENIUM_PYTEST=72
    KW_CHILD=73
    KW_FILTER_OUT=74
    KW_FILTER_IN=75
    KW_PAGE=76
    KW_LINK_SUFFIX=77
    KW_URL_PREFIX=78
    KW_CAN_EDIT=79
    KW_OBJECT_EXPR=80
    KW_BLOCK=81
    KW_ITEM_NAME=82
    KW_PK_PARAM=83
    KW_LIST_FIELDS=84
    KW_DELETE=85
    KW_EDIT=86
    KW_CREATE=87
    KW_DETAIL=88
    KW_SKIP=89
    KW_FROM=90
    KW_POLY_LIST=91
    KW_CSS=92
    KW_JS=93
    KW_INLINE_TYPE_TABULAR=94
    KW_INLINE_TYPE_STACKED=95
    KW_INLINE_TYPE_POLYMORPHIC=96
    KW_INLINE=97
    KW_TYPE=98
    KW_USER_FIELD=99
    KW_ANNOTATE=100
    KW_ON_CREATE=101
    KW_QUERY=102
    KW_AUTH=103
    KW_COUNT=104
    KW_I18N=105
    KW_EXTENSION=106
    KW_TABS=107
    KW_LIST=108
    KW_READ_ONLY=109
    KW_LIST_EDITABLE=110
    KW_LIST_FILTER=111
    KW_LIST_SEARCH=112
    KW_FIELDS=113
    KW_IMPORT=114
    KW_AS=115
    WRITE_MODE=116
    BOOL=117
    NL=118
    ID=119
    DIGIT=120
    SIZE2D=121
    LT=122
    GT=123
    COLON=124
    EXCLUDE=125
    BRACE_OPEN=126
    BRACE_CLOSE=127
    SQ_BRACE_OPEN=128
    SQ_BRACE_CLOSE=129
    QUESTION_MARK=130
    UNDERSCORE=131
    DASH=132
    COMA=133
    DOT=134
    HASH=135
    SLASH=136
    EQUALS=137
    DOLLAR=138
    AMP=139
    EXCLAM=140
    STAR=141
    APPROX=142
    PIPE=143
    STRING_DQ=144
    STRING_SQ=145
    COMMENT_LINE=146
    COMMENT_BLOCK=147
    UNICODE=148
    WS=149
    COL_FIELD_CALCULATED=150
    ASSIGN=151
    ASSIGN_STATIC=152
    CODE_BLOCK=153
    ERRCHAR=154
    PYTHON_CODE=155
    PYTHON_LINE_ERRCHAR=156
    PYTHON_LINE_END=157
    PYTHON_EXPR_ERRCHAR=158
    PYTHON_LINE_NL=159

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
            self.state = 561
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 558
                    self.match(ZmeiLangParser.NL) 
                self.state = 563
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 567
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 564
                    self.cs_annotation() 
                self.state = 569
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 573
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 570
                    self.match(ZmeiLangParser.NL) 
                self.state = 575
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 584
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 577
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.KW_FROM or _la==ZmeiLangParser.KW_IMPORT:
                    self.state = 576
                    self.page_imports()


                self.state = 580 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 579
                    self.page()
                    self.state = 582 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZmeiLangParser.SQ_BRACE_OPEN):
                        break



            self.state = 589
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 586
                    self.match(ZmeiLangParser.NL) 
                self.state = 591
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 600
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 90)) & ~0x3f) == 0 and ((1 << (_la - 90)) & ((1 << (ZmeiLangParser.KW_FROM - 90)) | (1 << (ZmeiLangParser.KW_IMPORT - 90)) | (1 << (ZmeiLangParser.HASH - 90)))) != 0):
                self.state = 593
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.KW_FROM or _la==ZmeiLangParser.KW_IMPORT:
                    self.state = 592
                    self.model_imports()


                self.state = 596 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 595
                    self.col()
                    self.state = 598 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZmeiLangParser.HASH):
                        break



            self.state = 605
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 602
                self.match(ZmeiLangParser.NL)
                self.state = 607
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 608
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
            self.state = 611 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 610
                self.page_import_statement()
                self.state = 613 
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
            self.state = 616 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 615
                self.model_import_statement()
                self.state = 618 
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
            self.state = 620
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
            self.state = 622
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
            self.state = 626
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.KW_FROM:
                self.state = 624
                self.match(ZmeiLangParser.KW_FROM)
                self.state = 625
                self.import_source()


            self.state = 628
            self.match(ZmeiLangParser.KW_IMPORT)
            self.state = 629
            self.import_list()
            self.state = 631 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 630
                self.match(ZmeiLangParser.NL)
                self.state = 633 
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
            self.state = 636
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 635
                self.match(ZmeiLangParser.DOT)


            self.state = 638
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
            self.state = 640
            self.import_item()
            self.state = 645
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 641
                self.match(ZmeiLangParser.COMA)
                self.state = 642
                self.import_item()
                self.state = 647
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
            self.state = 654
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 648
                self.import_item_name()
                self.state = 651
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.KW_AS:
                    self.state = 649
                    self.match(ZmeiLangParser.KW_AS)
                    self.state = 650
                    self.import_item_alias()


                pass
            elif token in [ZmeiLangParser.STAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 653
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
            self.state = 656
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
            self.state = 658
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
            self.state = 660
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

        def KW_AUTH_TYPE_BASIC(self):
            return self.getToken(ZmeiLangParser.KW_AUTH_TYPE_BASIC, 0)

        def KW_AUTH_TYPE_SESSION(self):
            return self.getToken(ZmeiLangParser.KW_AUTH_TYPE_SESSION, 0)

        def KW_AUTH_TYPE_TOKEN(self):
            return self.getToken(ZmeiLangParser.KW_AUTH_TYPE_TOKEN, 0)

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

        def KW_EXTENSION(self):
            return self.getToken(ZmeiLangParser.KW_EXTENSION, 0)

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
            self.state = 662
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.KW_AUTH_TYPE_BASIC) | (1 << ZmeiLangParser.KW_AUTH_TYPE_SESSION) | (1 << ZmeiLangParser.KW_AUTH_TYPE_TOKEN) | (1 << ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FLOAT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DECIMAL) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATETIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_TEXT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_INT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_SLUG) | (1 << ZmeiLangParser.COL_FIELD_TYPE_BOOL))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 64)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 64)) | (1 << (ZmeiLangParser.KW_THEME - 64)) | (1 << (ZmeiLangParser.KW_INSTALL - 64)) | (1 << (ZmeiLangParser.KW_HEADER - 64)) | (1 << (ZmeiLangParser.KW_SERVICES - 64)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 64)) | (1 << (ZmeiLangParser.KW_CHILD - 64)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 64)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 64)) | (1 << (ZmeiLangParser.KW_PAGE - 64)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 64)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 64)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 64)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 64)) | (1 << (ZmeiLangParser.KW_BLOCK - 64)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 64)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 64)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 64)) | (1 << (ZmeiLangParser.KW_DELETE - 64)) | (1 << (ZmeiLangParser.KW_EDIT - 64)) | (1 << (ZmeiLangParser.KW_CREATE - 64)) | (1 << (ZmeiLangParser.KW_DETAIL - 64)) | (1 << (ZmeiLangParser.KW_SKIP - 64)) | (1 << (ZmeiLangParser.KW_FROM - 64)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 64)) | (1 << (ZmeiLangParser.KW_CSS - 64)) | (1 << (ZmeiLangParser.KW_JS - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 64)) | (1 << (ZmeiLangParser.KW_INLINE - 64)) | (1 << (ZmeiLangParser.KW_TYPE - 64)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 64)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 64)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 64)) | (1 << (ZmeiLangParser.KW_QUERY - 64)) | (1 << (ZmeiLangParser.KW_AUTH - 64)) | (1 << (ZmeiLangParser.KW_COUNT - 64)) | (1 << (ZmeiLangParser.KW_I18N - 64)) | (1 << (ZmeiLangParser.KW_EXTENSION - 64)) | (1 << (ZmeiLangParser.KW_TABS - 64)) | (1 << (ZmeiLangParser.KW_LIST - 64)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 64)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 64)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 64)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 64)) | (1 << (ZmeiLangParser.KW_FIELDS - 64)) | (1 << (ZmeiLangParser.KW_IMPORT - 64)) | (1 << (ZmeiLangParser.KW_AS - 64)) | (1 << (ZmeiLangParser.WRITE_MODE - 64)) | (1 << (ZmeiLangParser.BOOL - 64)) | (1 << (ZmeiLangParser.ID - 64)))) != 0)):
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
            self.state = 664
            self.id_or_kw()
            self.state = 669
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.DOT:
                self.state = 665
                self.match(ZmeiLangParser.DOT)
                self.state = 666
                self.id_or_kw()
                self.state = 671
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
            self.state = 672
            self.match(ZmeiLangParser.HASH)
            self.state = 676
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 673
                self.id_or_kw()
                self.state = 674
                self.match(ZmeiLangParser.DOT)


            self.state = 678
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
            self.state = 703
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.DOT, ZmeiLangParser.STAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 681
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.DOT:
                    self.state = 680
                    self.match(ZmeiLangParser.DOT)


                self.state = 683
                self.match(ZmeiLangParser.STAR)
                self.state = 689
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 684
                        self.match(ZmeiLangParser.COMA)
                        self.state = 685
                        self.match(ZmeiLangParser.EXCLUDE)
                        self.state = 686
                        self.field_list_expr_field() 
                    self.state = 691
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

                pass
            elif token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 692
                self.id_or_kw()
                self.state = 700
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 693
                        self.match(ZmeiLangParser.COMA)
                        self.state = 695
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==ZmeiLangParser.EXCLUDE:
                            self.state = 694
                            self.match(ZmeiLangParser.EXCLUDE)


                        self.state = 697
                        self.field_list_expr_field() 
                    self.state = 702
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
            self.state = 706
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.STAR:
                self.state = 705
                self.match(ZmeiLangParser.STAR)


            self.state = 708
            self.id_or_kw()
            self.state = 710
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.STAR:
                self.state = 709
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
            self.state = 712
            self.match(ZmeiLangParser.SQ_BRACE_OPEN)
            self.state = 713
            self.match(ZmeiLangParser.WRITE_MODE)
            self.state = 714
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
            self.state = 718
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.CODE_BLOCK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 716
                self.code_block()
                pass
            elif token in [ZmeiLangParser.ASSIGN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 717
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
            self.state = 720
            self.match(ZmeiLangParser.ASSIGN)
            self.state = 721
            self.match(ZmeiLangParser.PYTHON_CODE)
            self.state = 722
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
            self.state = 724
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
            self.state = 736
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.AN_SUIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 726
                self.an_suit()
                pass
            elif token in [ZmeiLangParser.AN_CELERY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 727
                self.an_celery()
                pass
            elif token in [ZmeiLangParser.AN_CHANNELS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 728
                self.an_channels()
                pass
            elif token in [ZmeiLangParser.AN_DOCKER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 729
                self.an_docker()
                pass
            elif token in [ZmeiLangParser.AN_FILER]:
                self.enterOuterAlt(localctx, 5)
                self.state = 730
                self.an_filer()
                pass
            elif token in [ZmeiLangParser.AN_GITLAB]:
                self.enterOuterAlt(localctx, 6)
                self.state = 731
                self.an_gitlab()
                pass
            elif token in [ZmeiLangParser.AN_FILE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 732
                self.an_file()
                pass
            elif token in [ZmeiLangParser.AN_THEME]:
                self.enterOuterAlt(localctx, 8)
                self.state = 733
                self.an_theme()
                pass
            elif token in [ZmeiLangParser.AN_LANGS]:
                self.enterOuterAlt(localctx, 9)
                self.state = 734
                self.an_langs()
                pass
            elif token in [ZmeiLangParser.NL]:
                self.enterOuterAlt(localctx, 10)
                self.state = 735
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
            self.state = 738
            self.match(ZmeiLangParser.AN_SUIT)
            self.state = 743
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 739
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 740
                self.an_suit_app_name()
                self.state = 741
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
            self.state = 745
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
            self.state = 747
            self.match(ZmeiLangParser.AN_CELERY)
            self.state = 750
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 748
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 749
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
            self.state = 752
            self.match(ZmeiLangParser.AN_CHANNELS)
            self.state = 755
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 753
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 754
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
            self.state = 757
            self.match(ZmeiLangParser.AN_DOCKER)
            self.state = 760
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 758
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 759
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
            self.state = 762
            self.match(ZmeiLangParser.AN_FILER)
            self.state = 765
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 763
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 764
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
            self.state = 767
            self.match(ZmeiLangParser.AN_GITLAB)
            self.state = 768
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 772
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 769
                    self.match(ZmeiLangParser.NL) 
                self.state = 774
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

            self.state = 776
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 775
                self.an_gitlab_test_declaration()


            self.state = 781
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 778
                self.match(ZmeiLangParser.NL)
                self.state = 783
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 785 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 784
                self.an_gitlab_branch_declaration()
                self.state = 787 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 42)) & ~0x3f) == 0 and ((1 << (_la - 42)) & ((1 << (ZmeiLangParser.KW_AUTH_TYPE_BASIC - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_SESSION - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_TOKEN - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 42)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 42)) | (1 << (ZmeiLangParser.KW_THEME - 42)) | (1 << (ZmeiLangParser.KW_INSTALL - 42)) | (1 << (ZmeiLangParser.KW_HEADER - 42)) | (1 << (ZmeiLangParser.KW_SERVICES - 42)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 42)) | (1 << (ZmeiLangParser.KW_CHILD - 42)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 42)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 42)) | (1 << (ZmeiLangParser.KW_PAGE - 42)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 42)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 42)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 42)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 42)) | (1 << (ZmeiLangParser.KW_BLOCK - 42)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 42)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 42)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 42)) | (1 << (ZmeiLangParser.KW_DELETE - 42)) | (1 << (ZmeiLangParser.KW_EDIT - 42)) | (1 << (ZmeiLangParser.KW_CREATE - 42)) | (1 << (ZmeiLangParser.KW_DETAIL - 42)) | (1 << (ZmeiLangParser.KW_SKIP - 42)) | (1 << (ZmeiLangParser.KW_FROM - 42)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 42)) | (1 << (ZmeiLangParser.KW_CSS - 42)) | (1 << (ZmeiLangParser.KW_JS - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 42)) | (1 << (ZmeiLangParser.KW_INLINE - 42)) | (1 << (ZmeiLangParser.KW_TYPE - 42)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 42)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 42)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 42)) | (1 << (ZmeiLangParser.KW_QUERY - 42)) | (1 << (ZmeiLangParser.KW_AUTH - 42)) | (1 << (ZmeiLangParser.KW_COUNT - 42)) | (1 << (ZmeiLangParser.KW_I18N - 42)))) != 0) or ((((_la - 106)) & ~0x3f) == 0 and ((1 << (_la - 106)) & ((1 << (ZmeiLangParser.KW_EXTENSION - 106)) | (1 << (ZmeiLangParser.KW_TABS - 106)) | (1 << (ZmeiLangParser.KW_LIST - 106)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 106)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 106)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 106)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 106)) | (1 << (ZmeiLangParser.KW_FIELDS - 106)) | (1 << (ZmeiLangParser.KW_IMPORT - 106)) | (1 << (ZmeiLangParser.KW_AS - 106)) | (1 << (ZmeiLangParser.WRITE_MODE - 106)) | (1 << (ZmeiLangParser.BOOL - 106)) | (1 << (ZmeiLangParser.ID - 106)) | (1 << (ZmeiLangParser.DASH - 106)) | (1 << (ZmeiLangParser.SLASH - 106)) | (1 << (ZmeiLangParser.STAR - 106)))) != 0)):
                    break

            self.state = 792
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 789
                self.match(ZmeiLangParser.NL)
                self.state = 794
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 795
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
            self.state = 797
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
            self.state = 799
            self.match(ZmeiLangParser.KW_SELENIUM_PYTEST)
            self.state = 800
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 804
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 801
                    self.match(ZmeiLangParser.NL) 
                self.state = 806
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

            self.state = 808
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 807
                self.an_gitlab_test_services()


            self.state = 813
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 810
                    self.match(ZmeiLangParser.NL) 
                self.state = 815
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

            self.state = 822
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 816
                    self.an_gitlab_deployment_variable()
                    self.state = 818
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==ZmeiLangParser.COMA:
                        self.state = 817
                        self.match(ZmeiLangParser.COMA)

             
                self.state = 824
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

            self.state = 828
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 825
                self.match(ZmeiLangParser.NL)
                self.state = 830
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 831
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
            self.state = 833
            self.match(ZmeiLangParser.KW_SERVICES)
            self.state = 834
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 838
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 835
                    self.match(ZmeiLangParser.NL) 
                self.state = 840
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

            self.state = 849
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.state = 841
                self.an_gitlab_test_service()
                self.state = 846
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZmeiLangParser.COMA:
                    self.state = 842
                    self.match(ZmeiLangParser.COMA)
                    self.state = 843
                    self.an_gitlab_test_service()
                    self.state = 848
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 854
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 851
                self.match(ZmeiLangParser.NL)
                self.state = 856
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 857
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
            self.state = 862
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 859
                self.match(ZmeiLangParser.NL)
                self.state = 864
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 865
            self.an_gitlab_test_service_name()
            self.state = 889
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 866
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 870
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 867
                        self.match(ZmeiLangParser.NL) 
                    self.state = 872
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

                self.state = 879
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,53,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 873
                        self.an_gitlab_deployment_variable()
                        self.state = 875
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==ZmeiLangParser.COMA:
                            self.state = 874
                            self.match(ZmeiLangParser.COMA)

                 
                    self.state = 881
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,53,self._ctx)

                self.state = 885
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZmeiLangParser.NL:
                    self.state = 882
                    self.match(ZmeiLangParser.NL)
                    self.state = 887
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 888
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
            self.state = 891
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
            self.state = 893
            self.an_gitlab_branch_name()
            self.state = 897
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 894
                self.match(ZmeiLangParser.NL)
                self.state = 899
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 900
            self.an_gitlab_branch_deploy_type()
            self.state = 904
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 901
                self.match(ZmeiLangParser.NL)
                self.state = 906
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 907
            self.an_gitlab_deployment_name()
            self.state = 908
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 912
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 909
                self.match(ZmeiLangParser.NL)
                self.state = 914
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 915
            self.an_gitlab_deployment_host()
            self.state = 932
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COLON:
                self.state = 916
                self.match(ZmeiLangParser.COLON)
                self.state = 920
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,59,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 917
                        self.match(ZmeiLangParser.NL) 
                    self.state = 922
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,59,self._ctx)

                self.state = 929
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,61,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 923
                        self.an_gitlab_deployment_variable()
                        self.state = 925
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==ZmeiLangParser.COMA:
                            self.state = 924
                            self.match(ZmeiLangParser.COMA)

                 
                    self.state = 931
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,61,self._ctx)



            self.state = 937
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 934
                self.match(ZmeiLangParser.NL)
                self.state = 939
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 940
            self.match(ZmeiLangParser.BRACE_CLOSE)
            self.state = 944
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,64,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 941
                    self.match(ZmeiLangParser.NL) 
                self.state = 946
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
            self.state = 947
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.EQUALS or _la==ZmeiLangParser.APPROX):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 948
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
            self.state = 954 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 954
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                    self.state = 950
                    self.id_or_kw()
                    pass
                elif token in [ZmeiLangParser.DASH]:
                    self.state = 951
                    self.match(ZmeiLangParser.DASH)
                    pass
                elif token in [ZmeiLangParser.STAR]:
                    self.state = 952
                    self.match(ZmeiLangParser.STAR)
                    pass
                elif token in [ZmeiLangParser.SLASH]:
                    self.state = 953
                    self.match(ZmeiLangParser.SLASH)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 956 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 42)) & ~0x3f) == 0 and ((1 << (_la - 42)) & ((1 << (ZmeiLangParser.KW_AUTH_TYPE_BASIC - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_SESSION - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_TOKEN - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 42)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 42)) | (1 << (ZmeiLangParser.KW_THEME - 42)) | (1 << (ZmeiLangParser.KW_INSTALL - 42)) | (1 << (ZmeiLangParser.KW_HEADER - 42)) | (1 << (ZmeiLangParser.KW_SERVICES - 42)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 42)) | (1 << (ZmeiLangParser.KW_CHILD - 42)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 42)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 42)) | (1 << (ZmeiLangParser.KW_PAGE - 42)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 42)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 42)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 42)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 42)) | (1 << (ZmeiLangParser.KW_BLOCK - 42)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 42)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 42)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 42)) | (1 << (ZmeiLangParser.KW_DELETE - 42)) | (1 << (ZmeiLangParser.KW_EDIT - 42)) | (1 << (ZmeiLangParser.KW_CREATE - 42)) | (1 << (ZmeiLangParser.KW_DETAIL - 42)) | (1 << (ZmeiLangParser.KW_SKIP - 42)) | (1 << (ZmeiLangParser.KW_FROM - 42)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 42)) | (1 << (ZmeiLangParser.KW_CSS - 42)) | (1 << (ZmeiLangParser.KW_JS - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 42)) | (1 << (ZmeiLangParser.KW_INLINE - 42)) | (1 << (ZmeiLangParser.KW_TYPE - 42)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 42)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 42)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 42)) | (1 << (ZmeiLangParser.KW_QUERY - 42)) | (1 << (ZmeiLangParser.KW_AUTH - 42)) | (1 << (ZmeiLangParser.KW_COUNT - 42)) | (1 << (ZmeiLangParser.KW_I18N - 42)))) != 0) or ((((_la - 106)) & ~0x3f) == 0 and ((1 << (_la - 106)) & ((1 << (ZmeiLangParser.KW_EXTENSION - 106)) | (1 << (ZmeiLangParser.KW_TABS - 106)) | (1 << (ZmeiLangParser.KW_LIST - 106)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 106)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 106)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 106)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 106)) | (1 << (ZmeiLangParser.KW_FIELDS - 106)) | (1 << (ZmeiLangParser.KW_IMPORT - 106)) | (1 << (ZmeiLangParser.KW_AS - 106)) | (1 << (ZmeiLangParser.WRITE_MODE - 106)) | (1 << (ZmeiLangParser.BOOL - 106)) | (1 << (ZmeiLangParser.ID - 106)) | (1 << (ZmeiLangParser.DASH - 106)) | (1 << (ZmeiLangParser.SLASH - 106)) | (1 << (ZmeiLangParser.STAR - 106)))) != 0)):
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
            self.state = 962 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 962
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                    self.state = 958
                    self.id_or_kw()
                    pass
                elif token in [ZmeiLangParser.DASH]:
                    self.state = 959
                    self.match(ZmeiLangParser.DASH)
                    pass
                elif token in [ZmeiLangParser.SLASH]:
                    self.state = 960
                    self.match(ZmeiLangParser.SLASH)
                    pass
                elif token in [ZmeiLangParser.STAR]:
                    self.state = 961
                    self.match(ZmeiLangParser.STAR)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 964 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 42)) & ~0x3f) == 0 and ((1 << (_la - 42)) & ((1 << (ZmeiLangParser.KW_AUTH_TYPE_BASIC - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_SESSION - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_TOKEN - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 42)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 42)) | (1 << (ZmeiLangParser.KW_THEME - 42)) | (1 << (ZmeiLangParser.KW_INSTALL - 42)) | (1 << (ZmeiLangParser.KW_HEADER - 42)) | (1 << (ZmeiLangParser.KW_SERVICES - 42)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 42)) | (1 << (ZmeiLangParser.KW_CHILD - 42)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 42)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 42)) | (1 << (ZmeiLangParser.KW_PAGE - 42)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 42)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 42)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 42)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 42)) | (1 << (ZmeiLangParser.KW_BLOCK - 42)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 42)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 42)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 42)) | (1 << (ZmeiLangParser.KW_DELETE - 42)) | (1 << (ZmeiLangParser.KW_EDIT - 42)) | (1 << (ZmeiLangParser.KW_CREATE - 42)) | (1 << (ZmeiLangParser.KW_DETAIL - 42)) | (1 << (ZmeiLangParser.KW_SKIP - 42)) | (1 << (ZmeiLangParser.KW_FROM - 42)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 42)) | (1 << (ZmeiLangParser.KW_CSS - 42)) | (1 << (ZmeiLangParser.KW_JS - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 42)) | (1 << (ZmeiLangParser.KW_INLINE - 42)) | (1 << (ZmeiLangParser.KW_TYPE - 42)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 42)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 42)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 42)) | (1 << (ZmeiLangParser.KW_QUERY - 42)) | (1 << (ZmeiLangParser.KW_AUTH - 42)) | (1 << (ZmeiLangParser.KW_COUNT - 42)) | (1 << (ZmeiLangParser.KW_I18N - 42)))) != 0) or ((((_la - 106)) & ~0x3f) == 0 and ((1 << (_la - 106)) & ((1 << (ZmeiLangParser.KW_EXTENSION - 106)) | (1 << (ZmeiLangParser.KW_TABS - 106)) | (1 << (ZmeiLangParser.KW_LIST - 106)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 106)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 106)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 106)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 106)) | (1 << (ZmeiLangParser.KW_FIELDS - 106)) | (1 << (ZmeiLangParser.KW_IMPORT - 106)) | (1 << (ZmeiLangParser.KW_AS - 106)) | (1 << (ZmeiLangParser.WRITE_MODE - 106)) | (1 << (ZmeiLangParser.BOOL - 106)) | (1 << (ZmeiLangParser.ID - 106)) | (1 << (ZmeiLangParser.DASH - 106)) | (1 << (ZmeiLangParser.SLASH - 106)) | (1 << (ZmeiLangParser.STAR - 106)))) != 0)):
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
            self.state = 970 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 970
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                    self.state = 966
                    self.id_or_kw()
                    pass
                elif token in [ZmeiLangParser.DASH]:
                    self.state = 967
                    self.match(ZmeiLangParser.DASH)
                    pass
                elif token in [ZmeiLangParser.STAR]:
                    self.state = 968
                    self.match(ZmeiLangParser.STAR)
                    pass
                elif token in [ZmeiLangParser.DOT]:
                    self.state = 969
                    self.match(ZmeiLangParser.DOT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 972 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 42)) & ~0x3f) == 0 and ((1 << (_la - 42)) & ((1 << (ZmeiLangParser.KW_AUTH_TYPE_BASIC - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_SESSION - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_TOKEN - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 42)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 42)) | (1 << (ZmeiLangParser.KW_THEME - 42)) | (1 << (ZmeiLangParser.KW_INSTALL - 42)) | (1 << (ZmeiLangParser.KW_HEADER - 42)) | (1 << (ZmeiLangParser.KW_SERVICES - 42)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 42)) | (1 << (ZmeiLangParser.KW_CHILD - 42)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 42)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 42)) | (1 << (ZmeiLangParser.KW_PAGE - 42)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 42)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 42)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 42)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 42)) | (1 << (ZmeiLangParser.KW_BLOCK - 42)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 42)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 42)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 42)) | (1 << (ZmeiLangParser.KW_DELETE - 42)) | (1 << (ZmeiLangParser.KW_EDIT - 42)) | (1 << (ZmeiLangParser.KW_CREATE - 42)) | (1 << (ZmeiLangParser.KW_DETAIL - 42)) | (1 << (ZmeiLangParser.KW_SKIP - 42)) | (1 << (ZmeiLangParser.KW_FROM - 42)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 42)) | (1 << (ZmeiLangParser.KW_CSS - 42)) | (1 << (ZmeiLangParser.KW_JS - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 42)) | (1 << (ZmeiLangParser.KW_INLINE - 42)) | (1 << (ZmeiLangParser.KW_TYPE - 42)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 42)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 42)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 42)) | (1 << (ZmeiLangParser.KW_QUERY - 42)) | (1 << (ZmeiLangParser.KW_AUTH - 42)) | (1 << (ZmeiLangParser.KW_COUNT - 42)) | (1 << (ZmeiLangParser.KW_I18N - 42)))) != 0) or ((((_la - 106)) & ~0x3f) == 0 and ((1 << (_la - 106)) & ((1 << (ZmeiLangParser.KW_EXTENSION - 106)) | (1 << (ZmeiLangParser.KW_TABS - 106)) | (1 << (ZmeiLangParser.KW_LIST - 106)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 106)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 106)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 106)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 106)) | (1 << (ZmeiLangParser.KW_FIELDS - 106)) | (1 << (ZmeiLangParser.KW_IMPORT - 106)) | (1 << (ZmeiLangParser.KW_AS - 106)) | (1 << (ZmeiLangParser.WRITE_MODE - 106)) | (1 << (ZmeiLangParser.BOOL - 106)) | (1 << (ZmeiLangParser.ID - 106)) | (1 << (ZmeiLangParser.DASH - 106)) | (1 << (ZmeiLangParser.DOT - 106)) | (1 << (ZmeiLangParser.STAR - 106)))) != 0)):
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
            self.state = 977
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 974
                self.match(ZmeiLangParser.NL)
                self.state = 979
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 980
            self.an_gitlab_deployment_variable_name()
            self.state = 981
            self.match(ZmeiLangParser.EQUALS)
            self.state = 982
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
            self.state = 984
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
            self.state = 990
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.STRING_DQ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 986
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.enterOuterAlt(localctx, 2)
                self.state = 987
                self.match(ZmeiLangParser.STRING_SQ)
                pass
            elif token in [ZmeiLangParser.DIGIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 988
                self.match(ZmeiLangParser.DIGIT)
                pass
            elif token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                self.enterOuterAlt(localctx, 4)
                self.state = 989
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
            self.state = 992
            self.match(ZmeiLangParser.AN_FILE)
            self.state = 993
            self.an_file_name()
            self.state = 994
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
            self.state = 996
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
            self.state = 998
            self.match(ZmeiLangParser.AN_THEME)
            self.state = 999
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1000
            self.an_theme_name()
            self.state = 1005
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COMA:
                self.state = 1001
                self.match(ZmeiLangParser.COMA)
                self.state = 1002
                self.match(ZmeiLangParser.KW_INSTALL)
                self.state = 1003
                self.match(ZmeiLangParser.EQUALS)
                self.state = 1004
                self.an_theme_install()


            self.state = 1007
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
            self.state = 1009
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
            self.state = 1014
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1011
                self.id_or_kw()
                pass
            elif token in [ZmeiLangParser.STRING_DQ]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1012
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1013
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
            self.state = 1016
            self.match(ZmeiLangParser.AN_LANGS)
            self.state = 1017
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1018
            self.an_langs_list()
            self.state = 1019
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
            self.state = 1021
            self.match(ZmeiLangParser.ID)
            self.state = 1026
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 1022
                self.match(ZmeiLangParser.COMA)
                self.state = 1023
                self.match(ZmeiLangParser.ID)
                self.state = 1028
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
            self.state = 1029
            self.col_header()
            self.state = 1031
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,76,self._ctx)
            if la_ == 1:
                self.state = 1030
                self.col_str_expr()


            self.state = 1036
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,77,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1033
                    self.match(ZmeiLangParser.NL) 
                self.state = 1038
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,77,self._ctx)

            self.state = 1042
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 42)) & ~0x3f) == 0 and ((1 << (_la - 42)) & ((1 << (ZmeiLangParser.KW_AUTH_TYPE_BASIC - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_SESSION - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_TOKEN - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 42)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 42)) | (1 << (ZmeiLangParser.KW_THEME - 42)) | (1 << (ZmeiLangParser.KW_INSTALL - 42)) | (1 << (ZmeiLangParser.KW_HEADER - 42)) | (1 << (ZmeiLangParser.KW_SERVICES - 42)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 42)) | (1 << (ZmeiLangParser.KW_CHILD - 42)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 42)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 42)) | (1 << (ZmeiLangParser.KW_PAGE - 42)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 42)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 42)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 42)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 42)) | (1 << (ZmeiLangParser.KW_BLOCK - 42)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 42)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 42)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 42)) | (1 << (ZmeiLangParser.KW_DELETE - 42)) | (1 << (ZmeiLangParser.KW_EDIT - 42)) | (1 << (ZmeiLangParser.KW_CREATE - 42)) | (1 << (ZmeiLangParser.KW_DETAIL - 42)) | (1 << (ZmeiLangParser.KW_SKIP - 42)) | (1 << (ZmeiLangParser.KW_FROM - 42)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 42)) | (1 << (ZmeiLangParser.KW_CSS - 42)) | (1 << (ZmeiLangParser.KW_JS - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 42)) | (1 << (ZmeiLangParser.KW_INLINE - 42)) | (1 << (ZmeiLangParser.KW_TYPE - 42)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 42)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 42)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 42)) | (1 << (ZmeiLangParser.KW_QUERY - 42)) | (1 << (ZmeiLangParser.KW_AUTH - 42)) | (1 << (ZmeiLangParser.KW_COUNT - 42)) | (1 << (ZmeiLangParser.KW_I18N - 42)))) != 0) or ((((_la - 106)) & ~0x3f) == 0 and ((1 << (_la - 106)) & ((1 << (ZmeiLangParser.KW_EXTENSION - 106)) | (1 << (ZmeiLangParser.KW_TABS - 106)) | (1 << (ZmeiLangParser.KW_LIST - 106)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 106)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 106)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 106)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 106)) | (1 << (ZmeiLangParser.KW_FIELDS - 106)) | (1 << (ZmeiLangParser.KW_IMPORT - 106)) | (1 << (ZmeiLangParser.KW_AS - 106)) | (1 << (ZmeiLangParser.WRITE_MODE - 106)) | (1 << (ZmeiLangParser.BOOL - 106)) | (1 << (ZmeiLangParser.ID - 106)) | (1 << (ZmeiLangParser.EQUALS - 106)) | (1 << (ZmeiLangParser.DOLLAR - 106)) | (1 << (ZmeiLangParser.AMP - 106)) | (1 << (ZmeiLangParser.EXCLAM - 106)) | (1 << (ZmeiLangParser.STAR - 106)) | (1 << (ZmeiLangParser.APPROX - 106)))) != 0):
                self.state = 1039
                self.col_field()
                self.state = 1044
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1048
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,79,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1045
                    self.match(ZmeiLangParser.NL) 
                self.state = 1050
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,79,self._ctx)

            self.state = 1054
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,80,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1051
                    self.model_annotation() 
                self.state = 1056
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,80,self._ctx)

            self.state = 1060
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,81,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1057
                    self.match(ZmeiLangParser.NL) 
                self.state = 1062
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
            self.state = 1063
            self.match(ZmeiLangParser.EQUALS)
            self.state = 1064
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.STRING_DQ or _la==ZmeiLangParser.STRING_SQ):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 1071
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.NL]:
                self.state = 1066 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 1065
                        self.match(ZmeiLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 1068 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,82,self._ctx)

                pass
            elif token in [ZmeiLangParser.EOF]:
                self.state = 1070
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
            self.state = 1073
            self.match(ZmeiLangParser.HASH)
            self.state = 1075
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,84,self._ctx)
            if la_ == 1:
                self.state = 1074
                self.col_base_name()


            self.state = 1077
            self.col_name()
            self.state = 1079
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COLON:
                self.state = 1078
                self.col_verbose_name()


            self.state = 1081
            self.col_header_line_separator()
            self.state = 1082
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
            self.state = 1084
            self.match(ZmeiLangParser.NL)
            self.state = 1085
            self.match(ZmeiLangParser.DASH)
            self.state = 1086
            self.match(ZmeiLangParser.DASH)
            self.state = 1088 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1087
                self.match(ZmeiLangParser.DASH)
                self.state = 1090 
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
            self.state = 1092
            self.match(ZmeiLangParser.COLON)
            self.state = 1093
            self.verbose_name_part()
            self.state = 1096
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.SLASH:
                self.state = 1094
                self.match(ZmeiLangParser.SLASH)
                self.state = 1095
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
            self.state = 1101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                self.state = 1098
                self.id_or_kw()
                pass
            elif token in [ZmeiLangParser.STRING_DQ]:
                self.state = 1099
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.state = 1100
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
            self.state = 1103
            self.id_or_kw()
            self.state = 1108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.DASH]:
                self.state = 1104
                self.match(ZmeiLangParser.DASH)
                self.state = 1105
                self.match(ZmeiLangParser.GT)
                pass
            elif token in [ZmeiLangParser.APPROX]:
                self.state = 1106
                self.match(ZmeiLangParser.APPROX)
                self.state = 1107
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
            self.state = 1110
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
            self.state = 1115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 137)) & ~0x3f) == 0 and ((1 << (_la - 137)) & ((1 << (ZmeiLangParser.EQUALS - 137)) | (1 << (ZmeiLangParser.DOLLAR - 137)) | (1 << (ZmeiLangParser.AMP - 137)) | (1 << (ZmeiLangParser.EXCLAM - 137)) | (1 << (ZmeiLangParser.STAR - 137)) | (1 << (ZmeiLangParser.APPROX - 137)))) != 0):
                self.state = 1112
                self.col_modifier()
                self.state = 1117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1118
            self.col_field_name()
            self.state = 1120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 124)) & ~0x3f) == 0 and ((1 << (_la - 124)) & ((1 << (ZmeiLangParser.COLON - 124)) | (1 << (ZmeiLangParser.ASSIGN - 124)) | (1 << (ZmeiLangParser.ASSIGN_STATIC - 124)))) != 0):
                self.state = 1119
                self.col_field_expr_or_def()


            self.state = 1123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.SLASH:
                self.state = 1122
                self.col_field_verbose_name()


            self.state = 1126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.QUESTION_MARK:
                self.state = 1125
                self.col_field_help_text()


            self.state = 1134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.NL]:
                self.state = 1129 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 1128
                        self.match(ZmeiLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 1131 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,94,self._ctx)

                pass
            elif token in [ZmeiLangParser.EOF]:
                self.state = 1133
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
            self.state = 1148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,98,self._ctx)
            if la_ == 1:
                self.state = 1136
                self.match(ZmeiLangParser.COLON)
                self.state = 1138
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.CODE_BLOCK:
                    self.state = 1137
                    self.col_field_custom()


                pass

            elif la_ == 2:
                self.state = 1140
                self.match(ZmeiLangParser.COLON)
                self.state = 1141
                self.col_field_def()
                self.state = 1143
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.DOT or _la==ZmeiLangParser.CODE_BLOCK:
                    self.state = 1142
                    self.col_field_extend()


                pass

            elif la_ == 3:
                self.state = 1145
                self.match(ZmeiLangParser.COLON)
                self.state = 1146
                self.wrong_field_type()
                pass

            elif la_ == 4:
                self.state = 1147
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
            self.state = 1150
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
            self.state = 1153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 1152
                self.col_field_extend_append()


            self.state = 1155
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
            self.state = 1157
            self.match(ZmeiLangParser.DOT)
            self.state = 1158
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
            self.state = 1160
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
            self.state = 1162
            self.col_field_expr_marker()
            self.state = 1163
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
            self.state = 1165
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
            self.state = 1167
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
            self.state = 1176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                self.state = 1170 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 1169
                    self.id_or_kw()
                    self.state = 1172 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.KW_AUTH_TYPE_BASIC) | (1 << ZmeiLangParser.KW_AUTH_TYPE_SESSION) | (1 << ZmeiLangParser.KW_AUTH_TYPE_TOKEN) | (1 << ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FLOAT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DECIMAL) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATETIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_TEXT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_INT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_SLUG) | (1 << ZmeiLangParser.COL_FIELD_TYPE_BOOL))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 64)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 64)) | (1 << (ZmeiLangParser.KW_THEME - 64)) | (1 << (ZmeiLangParser.KW_INSTALL - 64)) | (1 << (ZmeiLangParser.KW_HEADER - 64)) | (1 << (ZmeiLangParser.KW_SERVICES - 64)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 64)) | (1 << (ZmeiLangParser.KW_CHILD - 64)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 64)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 64)) | (1 << (ZmeiLangParser.KW_PAGE - 64)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 64)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 64)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 64)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 64)) | (1 << (ZmeiLangParser.KW_BLOCK - 64)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 64)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 64)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 64)) | (1 << (ZmeiLangParser.KW_DELETE - 64)) | (1 << (ZmeiLangParser.KW_EDIT - 64)) | (1 << (ZmeiLangParser.KW_CREATE - 64)) | (1 << (ZmeiLangParser.KW_DETAIL - 64)) | (1 << (ZmeiLangParser.KW_SKIP - 64)) | (1 << (ZmeiLangParser.KW_FROM - 64)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 64)) | (1 << (ZmeiLangParser.KW_CSS - 64)) | (1 << (ZmeiLangParser.KW_JS - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 64)) | (1 << (ZmeiLangParser.KW_INLINE - 64)) | (1 << (ZmeiLangParser.KW_TYPE - 64)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 64)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 64)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 64)) | (1 << (ZmeiLangParser.KW_QUERY - 64)) | (1 << (ZmeiLangParser.KW_AUTH - 64)) | (1 << (ZmeiLangParser.KW_COUNT - 64)) | (1 << (ZmeiLangParser.KW_I18N - 64)) | (1 << (ZmeiLangParser.KW_EXTENSION - 64)) | (1 << (ZmeiLangParser.KW_TABS - 64)) | (1 << (ZmeiLangParser.KW_LIST - 64)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 64)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 64)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 64)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 64)) | (1 << (ZmeiLangParser.KW_FIELDS - 64)) | (1 << (ZmeiLangParser.KW_IMPORT - 64)) | (1 << (ZmeiLangParser.KW_AS - 64)) | (1 << (ZmeiLangParser.WRITE_MODE - 64)) | (1 << (ZmeiLangParser.BOOL - 64)) | (1 << (ZmeiLangParser.ID - 64)))) != 0)):
                        break

                pass
            elif token in [ZmeiLangParser.STRING_DQ]:
                self.state = 1174
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.state = 1175
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
            self.state = 1178
            self.match(ZmeiLangParser.QUESTION_MARK)
            self.state = 1179
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
            self.state = 1181
            self.match(ZmeiLangParser.SLASH)
            self.state = 1182
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
            self.state = 1184
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
            self.state = 1186
            _la = self._input.LA(1)
            if not(((((_la - 137)) & ~0x3f) == 0 and ((1 << (_la - 137)) & ((1 << (ZmeiLangParser.EQUALS - 137)) | (1 << (ZmeiLangParser.DOLLAR - 137)) | (1 << (ZmeiLangParser.AMP - 137)) | (1 << (ZmeiLangParser.EXCLAM - 137)) | (1 << (ZmeiLangParser.STAR - 137)) | (1 << (ZmeiLangParser.APPROX - 137)))) != 0)):
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
            self.state = 1206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1188
                self.field_longtext()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1189
                self.field_html_media()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_HTML]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1190
                self.field_html()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_FLOAT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1191
                self.field_float()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_DECIMAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1192
                self.field_decimal()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_DATE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 1193
                self.field_date()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_DATETIME]:
                self.enterOuterAlt(localctx, 7)
                self.state = 1194
                self.field_datetime()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME]:
                self.enterOuterAlt(localctx, 8)
                self.state = 1195
                self.field_create_time()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME]:
                self.enterOuterAlt(localctx, 9)
                self.state = 1196
                self.field_update_time()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_TEXT]:
                self.enterOuterAlt(localctx, 10)
                self.state = 1197
                self.field_text()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_INT]:
                self.enterOuterAlt(localctx, 11)
                self.state = 1198
                self.field_int()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_SLUG]:
                self.enterOuterAlt(localctx, 12)
                self.state = 1199
                self.field_slug()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_BOOL]:
                self.enterOuterAlt(localctx, 13)
                self.state = 1200
                self.field_bool()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY]:
                self.enterOuterAlt(localctx, 14)
                self.state = 1201
                self.field_relation()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER]:
                self.enterOuterAlt(localctx, 15)
                self.state = 1202
                self.field_image()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_FILE]:
                self.enterOuterAlt(localctx, 16)
                self.state = 1203
                self.field_file()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE]:
                self.enterOuterAlt(localctx, 17)
                self.state = 1204
                self.field_filer_file()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER]:
                self.enterOuterAlt(localctx, 18)
                self.state = 1205
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
            self.state = 1208
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
            self.state = 1210
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
            self.state = 1212
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
            self.state = 1214
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
            self.state = 1216
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
            self.state = 1218
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
            self.state = 1220
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
            self.state = 1222
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
            self.state = 1224
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
            self.state = 1226
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
            self.state = 1228
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
            self.state = 1230
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
            self.state = 1232
            self.match(ZmeiLangParser.COL_FIELD_TYPE_TEXT)
            self.state = 1241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1233
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1234
                self.field_text_size()
                self.state = 1237
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.COMA:
                    self.state = 1235
                    self.match(ZmeiLangParser.COMA)
                    self.state = 1236
                    self.field_text_choices()


                self.state = 1239
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
            self.state = 1243
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
            self.state = 1245
            self.match(ZmeiLangParser.COL_FIELD_CHOICES)
            self.state = 1246
            self.match(ZmeiLangParser.EQUALS)
            self.state = 1247
            self.field_text_choice()
            self.state = 1252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 1248
                self.match(ZmeiLangParser.COMA)
                self.state = 1249
                self.field_text_choice()
                self.state = 1254
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
            self.state = 1256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,106,self._ctx)
            if la_ == 1:
                self.state = 1255
                self.field_text_choice_key()


            self.state = 1258
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
            self.state = 1263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                self.state = 1260
                self.id_or_kw()
                pass
            elif token in [ZmeiLangParser.STRING_DQ]:
                self.state = 1261
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.state = 1262
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
            self.state = 1265
            self.id_or_kw()
            self.state = 1266
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
            self.state = 1268
            self.match(ZmeiLangParser.COL_FIELD_TYPE_INT)
            self.state = 1273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1269
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1270
                self.field_int_choices()
                self.state = 1271
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
            self.state = 1275
            self.match(ZmeiLangParser.COL_FIELD_CHOICES)
            self.state = 1276
            self.match(ZmeiLangParser.EQUALS)
            self.state = 1277
            self.field_int_choice()
            self.state = 1282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 1278
                self.match(ZmeiLangParser.COMA)
                self.state = 1279
                self.field_int_choice()
                self.state = 1284
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
            self.state = 1286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DIGIT:
                self.state = 1285
                self.field_int_choice_key()


            self.state = 1288
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
            self.state = 1293
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                self.state = 1290
                self.id_or_kw()
                pass
            elif token in [ZmeiLangParser.STRING_DQ]:
                self.state = 1291
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.state = 1292
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
            self.state = 1295
            self.match(ZmeiLangParser.DIGIT)
            self.state = 1296
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
            self.state = 1298
            self.match(ZmeiLangParser.COL_FIELD_TYPE_SLUG)
            self.state = 1299
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1300
            self.field_slug_ref_field()
            self.state = 1301
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
            self.state = 1303
            self.field_slug_ref_field_id()
            self.state = 1308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 1304
                self.match(ZmeiLangParser.COMA)
                self.state = 1305
                self.field_slug_ref_field_id()
                self.state = 1310
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
            self.state = 1311
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
            self.state = 1313
            self.match(ZmeiLangParser.COL_FIELD_TYPE_BOOL)
            self.state = 1318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1314
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1315
                self.field_bool_default()
                self.state = 1316
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
            self.state = 1320
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
            self.state = 1322
            self.filer_image_type()
            self.state = 1327
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1323
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1324
                self.field_image_sizes()
                self.state = 1325
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
            self.state = 1329
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
            self.state = 1331
            self.field_image_size()
            self.state = 1336
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 1332
                self.match(ZmeiLangParser.COMA)
                self.state = 1333
                self.field_image_size()
                self.state = 1338
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
            self.state = 1339
            self.field_image_size_name()
            self.state = 1340
            self.field_image_size_dimensions()
            self.state = 1341
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
            self.state = 1343
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
            self.state = 1345
            self.id_or_kw()
            self.state = 1346
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
            self.state = 1351
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.PIPE:
                self.state = 1348
                self.field_image_filter()
                self.state = 1353
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
            self.state = 1354
            self.match(ZmeiLangParser.PIPE)
            self.state = 1355
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
            self.state = 1357
            self.field_relation_type()
            self.state = 1358
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1360
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.EXCLAM or _la==ZmeiLangParser.APPROX:
                self.state = 1359
                self.field_relation_cascade_marker()


            self.state = 1364
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.HASH]:
                self.state = 1362
                self.field_relation_target_ref()
                pass
            elif token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                self.state = 1363
                self.field_relation_target_class()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 1367
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DASH:
                self.state = 1366
                self.field_relation_related_name()


            self.state = 1369
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
            self.state = 1371
            _la = self._input.LA(1)
            if not(((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 64)))) != 0)):
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
            self.state = 1373
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
            self.state = 1375
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
            self.state = 1377
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
            self.state = 1379
            self.match(ZmeiLangParser.DASH)
            self.state = 1380
            self.match(ZmeiLangParser.GT)
            self.state = 1381
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
            self.state = 1398
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.AN_ADMIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1383
                self.an_admin()
                pass
            elif token in [ZmeiLangParser.AN_API]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1384
                self.an_api()
                pass
            elif token in [ZmeiLangParser.AN_REST]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1385
                self.an_rest()
                pass
            elif token in [ZmeiLangParser.AN_ORDER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1386
                self.an_order()
                pass
            elif token in [ZmeiLangParser.AN_CLEAN]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1387
                self.an_clean()
                pass
            elif token in [ZmeiLangParser.AN_PRE_DELETE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 1388
                self.an_pre_delete()
                pass
            elif token in [ZmeiLangParser.AN_TREE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 1389
                self.an_tree()
                pass
            elif token in [ZmeiLangParser.AN_MIXIN]:
                self.enterOuterAlt(localctx, 8)
                self.state = 1390
                self.an_mixin()
                pass
            elif token in [ZmeiLangParser.AN_DATE_TREE]:
                self.enterOuterAlt(localctx, 9)
                self.state = 1391
                self.an_date_tree()
                pass
            elif token in [ZmeiLangParser.AN_M2M_CHANGED]:
                self.enterOuterAlt(localctx, 10)
                self.state = 1392
                self.an_m2m_changed()
                pass
            elif token in [ZmeiLangParser.AN_POST_SAVE]:
                self.enterOuterAlt(localctx, 11)
                self.state = 1393
                self.an_post_save()
                pass
            elif token in [ZmeiLangParser.AN_PRE_SAVE]:
                self.enterOuterAlt(localctx, 12)
                self.state = 1394
                self.an_pre_save()
                pass
            elif token in [ZmeiLangParser.AN_POST_DELETE]:
                self.enterOuterAlt(localctx, 13)
                self.state = 1395
                self.an_post_delete()
                pass
            elif token in [ZmeiLangParser.AN_SORTABLE]:
                self.enterOuterAlt(localctx, 14)
                self.state = 1396
                self.an_sortable()
                pass
            elif token in [ZmeiLangParser.NL]:
                self.enterOuterAlt(localctx, 15)
                self.state = 1397
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
            self.state = 1400
            self.match(ZmeiLangParser.AN_ADMIN)
            self.state = 1426
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1401
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1416
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,122,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 1414
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [ZmeiLangParser.KW_LIST]:
                            self.state = 1402
                            self.an_admin_list()
                            pass
                        elif token in [ZmeiLangParser.KW_READ_ONLY]:
                            self.state = 1403
                            self.an_admin_read_only()
                            pass
                        elif token in [ZmeiLangParser.KW_LIST_EDITABLE]:
                            self.state = 1404
                            self.an_admin_list_editable()
                            pass
                        elif token in [ZmeiLangParser.KW_LIST_FILTER]:
                            self.state = 1405
                            self.an_admin_list_filter()
                            pass
                        elif token in [ZmeiLangParser.KW_LIST_SEARCH]:
                            self.state = 1406
                            self.an_admin_list_search()
                            pass
                        elif token in [ZmeiLangParser.KW_FIELDS]:
                            self.state = 1407
                            self.an_admin_fields()
                            pass
                        elif token in [ZmeiLangParser.KW_TABS]:
                            self.state = 1408
                            self.an_admin_tabs()
                            pass
                        elif token in [ZmeiLangParser.KW_INLINE]:
                            self.state = 1409
                            self.an_admin_inlines()
                            pass
                        elif token in [ZmeiLangParser.KW_CSS]:
                            self.state = 1410
                            self.an_admin_css()
                            pass
                        elif token in [ZmeiLangParser.KW_JS]:
                            self.state = 1411
                            self.an_admin_js()
                            pass
                        elif token in [ZmeiLangParser.NL]:
                            self.state = 1412
                            self.match(ZmeiLangParser.NL)
                            pass
                        elif token in [ZmeiLangParser.COMA]:
                            self.state = 1413
                            self.match(ZmeiLangParser.COMA)
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 1418
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,122,self._ctx)

                self.state = 1422
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZmeiLangParser.NL:
                    self.state = 1419
                    self.match(ZmeiLangParser.NL)
                    self.state = 1424
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 1425
                self.match(ZmeiLangParser.BRACE_CLOSE)


            self.state = 1431
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,125,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1428
                    self.match(ZmeiLangParser.NL) 
                self.state = 1433
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
            self.state = 1434
            self.match(ZmeiLangParser.KW_JS)
            self.state = 1435
            self.match(ZmeiLangParser.COLON)
            self.state = 1439
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 1436
                self.match(ZmeiLangParser.NL)
                self.state = 1441
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1442
            self.an_admin_js_file_name()
            self.state = 1453
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,128,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1443
                    self.match(ZmeiLangParser.COMA)
                    self.state = 1447
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==ZmeiLangParser.NL:
                        self.state = 1444
                        self.match(ZmeiLangParser.NL)
                        self.state = 1449
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 1450
                    self.an_admin_js_file_name() 
                self.state = 1455
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
            self.state = 1456
            self.match(ZmeiLangParser.KW_CSS)
            self.state = 1457
            self.match(ZmeiLangParser.COLON)
            self.state = 1458
            self.an_admin_css_file_name()
            self.state = 1463
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,129,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1459
                    self.match(ZmeiLangParser.COMA)
                    self.state = 1460
                    self.an_admin_css_file_name() 
                self.state = 1465
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
            self.state = 1466
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
            self.state = 1468
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
            self.state = 1470
            self.match(ZmeiLangParser.KW_INLINE)
            self.state = 1471
            self.match(ZmeiLangParser.COLON)
            self.state = 1472
            self.an_admin_inline()
            self.state = 1477
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,130,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1473
                    self.match(ZmeiLangParser.COMA)
                    self.state = 1474
                    self.an_admin_inline() 
                self.state = 1479
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


        def inline_extension(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Inline_extensionContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Inline_extensionContext,i)


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
            self.state = 1480
            self.inline_name()
            self.state = 1493
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1481
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1489
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (ZmeiLangParser.KW_TYPE - 98)) | (1 << (ZmeiLangParser.KW_EXTENSION - 98)) | (1 << (ZmeiLangParser.KW_FIELDS - 98)) | (1 << (ZmeiLangParser.NL - 98)) | (1 << (ZmeiLangParser.COMA - 98)))) != 0):
                    self.state = 1487
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [ZmeiLangParser.KW_TYPE]:
                        self.state = 1482
                        self.inline_type()
                        pass
                    elif token in [ZmeiLangParser.KW_EXTENSION]:
                        self.state = 1483
                        self.inline_extension()
                        pass
                    elif token in [ZmeiLangParser.KW_FIELDS]:
                        self.state = 1484
                        self.inline_fields()
                        pass
                    elif token in [ZmeiLangParser.NL]:
                        self.state = 1485
                        self.match(ZmeiLangParser.NL)
                        pass
                    elif token in [ZmeiLangParser.COMA]:
                        self.state = 1486
                        self.match(ZmeiLangParser.COMA)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 1491
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 1492
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
            self.state = 1495
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

        def inline_type_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Inline_type_nameContext,0)


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
            self.state = 1497
            self.match(ZmeiLangParser.KW_TYPE)
            self.state = 1498
            self.match(ZmeiLangParser.COLON)
            self.state = 1499
            self.inline_type_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inline_type_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_INLINE_TYPE_TABULAR(self):
            return self.getToken(ZmeiLangParser.KW_INLINE_TYPE_TABULAR, 0)

        def KW_INLINE_TYPE_STACKED(self):
            return self.getToken(ZmeiLangParser.KW_INLINE_TYPE_STACKED, 0)

        def KW_INLINE_TYPE_POLYMORPHIC(self):
            return self.getToken(ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_inline_type_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInline_type_name" ):
                listener.enterInline_type_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInline_type_name" ):
                listener.exitInline_type_name(self)




    def inline_type_name(self):

        localctx = ZmeiLangParser.Inline_type_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 248, self.RULE_inline_type_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1501
            _la = self._input.LA(1)
            if not(((((_la - 94)) & ~0x3f) == 0 and ((1 << (_la - 94)) & ((1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 94)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 94)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 94)))) != 0)):
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


    class Inline_extensionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_EXTENSION(self):
            return self.getToken(ZmeiLangParser.KW_EXTENSION, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def DIGIT(self):
            return self.getToken(ZmeiLangParser.DIGIT, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_inline_extension

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInline_extension" ):
                listener.enterInline_extension(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInline_extension" ):
                listener.exitInline_extension(self)




    def inline_extension(self):

        localctx = ZmeiLangParser.Inline_extensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 250, self.RULE_inline_extension)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1503
            self.match(ZmeiLangParser.KW_EXTENSION)
            self.state = 1504
            self.match(ZmeiLangParser.COLON)
            self.state = 1505
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
        self.enterRule(localctx, 252, self.RULE_inline_fields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1507
            self.match(ZmeiLangParser.KW_FIELDS)
            self.state = 1508
            self.match(ZmeiLangParser.COLON)
            self.state = 1509
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
        self.enterRule(localctx, 254, self.RULE_an_admin_tabs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1511
            self.match(ZmeiLangParser.KW_TABS)
            self.state = 1512
            self.match(ZmeiLangParser.COLON)
            self.state = 1513
            self.an_admin_tab()
            self.state = 1518
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,134,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1514
                    self.match(ZmeiLangParser.COMA)
                    self.state = 1515
                    self.an_admin_tab() 
                self.state = 1520
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
        self.enterRule(localctx, 256, self.RULE_an_admin_tab)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1521
            self.tab_name()
            self.state = 1523
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.STRING_DQ or _la==ZmeiLangParser.STRING_SQ:
                self.state = 1522
                self.tab_verbose_name()


            self.state = 1525
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1526
            self.field_list_expr()
            self.state = 1527
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
        self.enterRule(localctx, 258, self.RULE_tab_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1529
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
        self.enterRule(localctx, 260, self.RULE_tab_verbose_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1531
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
        self.enterRule(localctx, 262, self.RULE_an_admin_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1533
            self.match(ZmeiLangParser.KW_LIST)
            self.state = 1534
            self.match(ZmeiLangParser.COLON)
            self.state = 1535
            self.field_list_expr()
            self.state = 1539
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,136,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1536
                    self.match(ZmeiLangParser.NL) 
                self.state = 1541
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
        self.enterRule(localctx, 264, self.RULE_an_admin_read_only)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1542
            self.match(ZmeiLangParser.KW_READ_ONLY)
            self.state = 1543
            self.match(ZmeiLangParser.COLON)
            self.state = 1544
            self.field_list_expr()
            self.state = 1548
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,137,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1545
                    self.match(ZmeiLangParser.NL) 
                self.state = 1550
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
        self.enterRule(localctx, 266, self.RULE_an_admin_list_editable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1551
            self.match(ZmeiLangParser.KW_LIST_EDITABLE)
            self.state = 1552
            self.match(ZmeiLangParser.COLON)
            self.state = 1553
            self.field_list_expr()
            self.state = 1557
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,138,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1554
                    self.match(ZmeiLangParser.NL) 
                self.state = 1559
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
        self.enterRule(localctx, 268, self.RULE_an_admin_list_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1560
            self.match(ZmeiLangParser.KW_LIST_FILTER)
            self.state = 1561
            self.match(ZmeiLangParser.COLON)
            self.state = 1562
            self.field_list_expr()
            self.state = 1566
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,139,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1563
                    self.match(ZmeiLangParser.NL) 
                self.state = 1568
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
        self.enterRule(localctx, 270, self.RULE_an_admin_list_search)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1569
            self.match(ZmeiLangParser.KW_LIST_SEARCH)
            self.state = 1570
            self.match(ZmeiLangParser.COLON)
            self.state = 1571
            self.field_list_expr()
            self.state = 1575
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,140,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1572
                    self.match(ZmeiLangParser.NL) 
                self.state = 1577
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
        self.enterRule(localctx, 272, self.RULE_an_admin_fields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1578
            self.match(ZmeiLangParser.KW_FIELDS)
            self.state = 1579
            self.match(ZmeiLangParser.COLON)
            self.state = 1580
            self.field_list_expr()
            self.state = 1584
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,141,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1581
                    self.match(ZmeiLangParser.NL) 
                self.state = 1586
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
        self.enterRule(localctx, 274, self.RULE_an_api)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1587
            self.match(ZmeiLangParser.AN_API)
            self.state = 1602
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1588
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1598
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.STAR]:
                    self.state = 1589
                    self.an_api_all()
                    pass
                elif token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                    self.state = 1590
                    self.an_api_name()
                    self.state = 1595
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==ZmeiLangParser.COMA:
                        self.state = 1591
                        self.match(ZmeiLangParser.COMA)
                        self.state = 1592
                        self.an_api_name()
                        self.state = 1597
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1600
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
        self.enterRule(localctx, 276, self.RULE_an_api_all)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1604
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
        self.enterRule(localctx, 278, self.RULE_an_api_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1606
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
        self.enterRule(localctx, 280, self.RULE_an_rest)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1608
            self.match(ZmeiLangParser.AN_REST)
            self.state = 1611
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 1609
                self.match(ZmeiLangParser.DOT)
                self.state = 1610
                self.an_rest_descriptor()


            self.state = 1617
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1613
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1614
                self.an_rest_config()
                self.state = 1615
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
        self.enterRule(localctx, 282, self.RULE_an_rest_config)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1619
            self.an_rest_main_part()
            self.state = 1625
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 97)) & ~0x3f) == 0 and ((1 << (_la - 97)) & ((1 << (ZmeiLangParser.KW_INLINE - 97)) | (1 << (ZmeiLangParser.NL - 97)) | (1 << (ZmeiLangParser.COMA - 97)))) != 0):
                self.state = 1623
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.KW_INLINE]:
                    self.state = 1620
                    self.an_rest_inline()
                    pass
                elif token in [ZmeiLangParser.NL]:
                    self.state = 1621
                    self.match(ZmeiLangParser.NL)
                    pass
                elif token in [ZmeiLangParser.COMA]:
                    self.state = 1622
                    self.match(ZmeiLangParser.COMA)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1627
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


        def an_rest_str(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_rest_strContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_rest_strContext,i)


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
        self.enterRule(localctx, 284, self.RULE_an_rest_main_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1643
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,150,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1641
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [ZmeiLangParser.KW_FIELDS]:
                        self.state = 1628
                        self.an_rest_fields()
                        pass
                    elif token in [ZmeiLangParser.KW_I18N]:
                        self.state = 1629
                        self.an_rest_i18n()
                        pass
                    elif token in [ZmeiLangParser.COL_FIELD_TYPE_TEXT]:
                        self.state = 1630
                        self.an_rest_str()
                        pass
                    elif token in [ZmeiLangParser.KW_AUTH]:
                        self.state = 1631
                        self.an_rest_auth()
                        pass
                    elif token in [ZmeiLangParser.KW_QUERY]:
                        self.state = 1632
                        self.an_rest_query()
                        pass
                    elif token in [ZmeiLangParser.KW_ON_CREATE]:
                        self.state = 1633
                        self.an_rest_on_create()
                        pass
                    elif token in [ZmeiLangParser.KW_FILTER_IN]:
                        self.state = 1634
                        self.an_rest_filter_in()
                        pass
                    elif token in [ZmeiLangParser.KW_FILTER_OUT]:
                        self.state = 1635
                        self.an_rest_filter_out()
                        pass
                    elif token in [ZmeiLangParser.KW_READ_ONLY]:
                        self.state = 1636
                        self.an_rest_read_only()
                        pass
                    elif token in [ZmeiLangParser.KW_USER_FIELD]:
                        self.state = 1637
                        self.an_rest_user_field()
                        pass
                    elif token in [ZmeiLangParser.KW_ANNOTATE]:
                        self.state = 1638
                        self.an_rest_annotate()
                        pass
                    elif token in [ZmeiLangParser.NL]:
                        self.state = 1639
                        self.match(ZmeiLangParser.NL)
                        pass
                    elif token in [ZmeiLangParser.COMA]:
                        self.state = 1640
                        self.match(ZmeiLangParser.COMA)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 1645
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
        self.enterRule(localctx, 286, self.RULE_an_rest_descriptor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1646
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
        self.enterRule(localctx, 288, self.RULE_an_rest_i18n)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1648
            self.match(ZmeiLangParser.KW_I18N)
            self.state = 1649
            self.match(ZmeiLangParser.COLON)
            self.state = 1650
            self.match(ZmeiLangParser.BOOL)
            self.state = 1654
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,151,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1651
                    self.match(ZmeiLangParser.NL) 
                self.state = 1656
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,151,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_strContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_TEXT(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_TEXT, 0)

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
            return ZmeiLangParser.RULE_an_rest_str

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_str" ):
                listener.enterAn_rest_str(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_str" ):
                listener.exitAn_rest_str(self)




    def an_rest_str(self):

        localctx = ZmeiLangParser.An_rest_strContext(self, self._ctx, self.state)
        self.enterRule(localctx, 290, self.RULE_an_rest_str)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1657
            self.match(ZmeiLangParser.COL_FIELD_TYPE_TEXT)
            self.state = 1658
            self.match(ZmeiLangParser.COLON)
            self.state = 1659
            self.match(ZmeiLangParser.BOOL)
            self.state = 1663
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,152,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1660
                    self.match(ZmeiLangParser.NL) 
                self.state = 1665
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,152,self._ctx)

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
        self.enterRule(localctx, 292, self.RULE_an_rest_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1666
            self.match(ZmeiLangParser.KW_QUERY)
            self.state = 1667
            self.python_code()
            self.state = 1671
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,153,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1668
                    self.match(ZmeiLangParser.NL) 
                self.state = 1673
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,153,self._ctx)

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
        self.enterRule(localctx, 294, self.RULE_an_rest_on_create)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1674
            self.match(ZmeiLangParser.KW_ON_CREATE)
            self.state = 1676
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COLON:
                self.state = 1675
                self.match(ZmeiLangParser.COLON)


            self.state = 1678
            self.python_code()
            self.state = 1682
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,155,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1679
                    self.match(ZmeiLangParser.NL) 
                self.state = 1684
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,155,self._ctx)

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
        self.enterRule(localctx, 296, self.RULE_an_rest_filter_in)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1685
            self.match(ZmeiLangParser.KW_FILTER_IN)
            self.state = 1687
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COLON:
                self.state = 1686
                self.match(ZmeiLangParser.COLON)


            self.state = 1689
            self.python_code()
            self.state = 1693
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,157,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1690
                    self.match(ZmeiLangParser.NL) 
                self.state = 1695
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,157,self._ctx)

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
        self.enterRule(localctx, 298, self.RULE_an_rest_filter_out)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1696
            self.match(ZmeiLangParser.KW_FILTER_OUT)
            self.state = 1698
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COLON:
                self.state = 1697
                self.match(ZmeiLangParser.COLON)


            self.state = 1700
            self.python_code()
            self.state = 1704
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,159,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1701
                    self.match(ZmeiLangParser.NL) 
                self.state = 1706
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,159,self._ctx)

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
        self.enterRule(localctx, 300, self.RULE_an_rest_read_only)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1707
            self.match(ZmeiLangParser.KW_READ_ONLY)
            self.state = 1708
            self.match(ZmeiLangParser.COLON)
            self.state = 1709
            self.field_list_expr()
            self.state = 1713
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,160,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1710
                    self.match(ZmeiLangParser.NL) 
                self.state = 1715
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,160,self._ctx)

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
        self.enterRule(localctx, 302, self.RULE_an_rest_user_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1716
            self.match(ZmeiLangParser.KW_USER_FIELD)
            self.state = 1717
            self.match(ZmeiLangParser.COLON)
            self.state = 1718
            self.id_or_kw()
            self.state = 1722
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,161,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1719
                    self.match(ZmeiLangParser.NL) 
                self.state = 1724
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,161,self._ctx)

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
        self.enterRule(localctx, 304, self.RULE_an_rest_fields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1725
            self.match(ZmeiLangParser.KW_FIELDS)
            self.state = 1726
            self.match(ZmeiLangParser.COLON)
            self.state = 1727
            self.field_list_expr()
            self.state = 1729
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.SQ_BRACE_OPEN:
                self.state = 1728
                self.an_rest_fields_write_mode()


            self.state = 1734
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,163,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1731
                    self.match(ZmeiLangParser.NL) 
                self.state = 1736
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,163,self._ctx)

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
        self.enterRule(localctx, 306, self.RULE_an_rest_fields_write_mode)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1737
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
        self.enterRule(localctx, 308, self.RULE_an_rest_auth)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1739
            self.match(ZmeiLangParser.KW_AUTH)
            self.state = 1740
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1741
            self.an_rest_auth_type()
            self.state = 1746
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 1742
                self.match(ZmeiLangParser.COMA)
                self.state = 1743
                self.an_rest_auth_type()
                self.state = 1748
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1749
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

        def an_rest_auth_type_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_rest_auth_type_nameContext,0)


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
        self.enterRule(localctx, 310, self.RULE_an_rest_auth_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1751
            self.an_rest_auth_type_name()
            self.state = 1755
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.COLON]:
                self.state = 1752
                self.match(ZmeiLangParser.COLON)
                self.state = 1753
                self.an_rest_auth_token_model()
                pass
            elif token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                self.state = 1754
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


    class An_rest_auth_type_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_AUTH_TYPE_BASIC(self):
            return self.getToken(ZmeiLangParser.KW_AUTH_TYPE_BASIC, 0)

        def KW_AUTH_TYPE_SESSION(self):
            return self.getToken(ZmeiLangParser.KW_AUTH_TYPE_SESSION, 0)

        def KW_AUTH_TYPE_TOKEN(self):
            return self.getToken(ZmeiLangParser.KW_AUTH_TYPE_TOKEN, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_auth_type_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_auth_type_name" ):
                listener.enterAn_rest_auth_type_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_auth_type_name" ):
                listener.exitAn_rest_auth_type_name(self)




    def an_rest_auth_type_name(self):

        localctx = ZmeiLangParser.An_rest_auth_type_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 312, self.RULE_an_rest_auth_type_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1757
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.KW_AUTH_TYPE_BASIC) | (1 << ZmeiLangParser.KW_AUTH_TYPE_SESSION) | (1 << ZmeiLangParser.KW_AUTH_TYPE_TOKEN))) != 0)):
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
        self.enterRule(localctx, 314, self.RULE_an_rest_auth_token_model)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1759
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
        self.enterRule(localctx, 316, self.RULE_an_rest_auth_token_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1761
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
        self.enterRule(localctx, 318, self.RULE_an_rest_annotate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1763
            self.match(ZmeiLangParser.KW_ANNOTATE)
            self.state = 1764
            self.match(ZmeiLangParser.COLON)
            self.state = 1765
            self.an_rest_annotate_count()
            self.state = 1769
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,166,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1766
                    self.match(ZmeiLangParser.NL) 
                self.state = 1771
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,166,self._ctx)

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
        self.enterRule(localctx, 320, self.RULE_an_rest_annotate_count)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1772
            self.match(ZmeiLangParser.KW_COUNT)
            self.state = 1773
            self.an_rest_annotate_count_field()
            self.state = 1776
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.KW_AS:
                self.state = 1774
                self.match(ZmeiLangParser.KW_AS)
                self.state = 1775
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
        self.enterRule(localctx, 322, self.RULE_an_rest_annotate_count_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1778
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
        self.enterRule(localctx, 324, self.RULE_an_rest_annotate_count_alias)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1780
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
        self.enterRule(localctx, 326, self.RULE_an_rest_inline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1782
            self.match(ZmeiLangParser.KW_INLINE)
            self.state = 1783
            self.match(ZmeiLangParser.COLON)
            self.state = 1787 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 1787
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                        self.state = 1784
                        self.an_rest_inline_decl()
                        pass
                    elif token in [ZmeiLangParser.COMA]:
                        self.state = 1785
                        self.match(ZmeiLangParser.COMA)
                        pass
                    elif token in [ZmeiLangParser.NL]:
                        self.state = 1786
                        self.match(ZmeiLangParser.NL)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 1789 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,169,self._ctx)

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
        self.enterRule(localctx, 328, self.RULE_an_rest_inline_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1791
            self.an_rest_inline_name()
            self.state = 1792
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1793
            self.an_rest_config()
            self.state = 1794
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
        self.enterRule(localctx, 330, self.RULE_an_rest_inline_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1796
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
        self.enterRule(localctx, 332, self.RULE_an_order)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1798
            self.match(ZmeiLangParser.AN_ORDER)
            self.state = 1799
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1800
            self.an_order_fields()
            self.state = 1801
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
        self.enterRule(localctx, 334, self.RULE_an_order_fields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1803
            self.id_or_kw()
            self.state = 1808
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 1804
                self.match(ZmeiLangParser.COMA)
                self.state = 1805
                self.id_or_kw()
                self.state = 1810
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
        self.enterRule(localctx, 336, self.RULE_an_clean)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1811
            self.match(ZmeiLangParser.AN_CLEAN)
            self.state = 1812
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
        self.enterRule(localctx, 338, self.RULE_an_pre_delete)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1814
            self.match(ZmeiLangParser.AN_PRE_DELETE)
            self.state = 1815
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
        self.enterRule(localctx, 340, self.RULE_an_tree)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1817
            self.match(ZmeiLangParser.AN_TREE)
            self.state = 1822
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1818
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1819
                self.an_tree_poly()
                self.state = 1820
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
        self.enterRule(localctx, 342, self.RULE_an_tree_poly)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1824
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
        self.enterRule(localctx, 344, self.RULE_an_mixin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1826
            self.match(ZmeiLangParser.AN_MIXIN)

            self.state = 1827
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1828
            self.classname()
            self.state = 1829
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
        self.enterRule(localctx, 346, self.RULE_an_date_tree)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1831
            self.match(ZmeiLangParser.AN_DATE_TREE)

            self.state = 1832
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1833
            self.an_date_tree_field()
            self.state = 1834
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
        self.enterRule(localctx, 348, self.RULE_an_date_tree_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1836
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
        self.enterRule(localctx, 350, self.RULE_an_m2m_changed)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1838
            self.match(ZmeiLangParser.AN_M2M_CHANGED)
            self.state = 1839
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
        self.enterRule(localctx, 352, self.RULE_an_post_save)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1841
            self.match(ZmeiLangParser.AN_POST_SAVE)
            self.state = 1842
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
        self.enterRule(localctx, 354, self.RULE_an_pre_save)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1844
            self.match(ZmeiLangParser.AN_PRE_SAVE)
            self.state = 1845
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
        self.enterRule(localctx, 356, self.RULE_an_post_delete)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1847
            self.match(ZmeiLangParser.AN_POST_DELETE)
            self.state = 1848
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
        self.enterRule(localctx, 358, self.RULE_an_sortable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1850
            self.match(ZmeiLangParser.AN_SORTABLE)
            self.state = 1851
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1852
            self.an_sortable_field_name()
            self.state = 1853
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
        self.enterRule(localctx, 360, self.RULE_an_sortable_field_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1855
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
        self.enterRule(localctx, 362, self.RULE_page)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1857
            self.page_header()
            self.state = 1861
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,172,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1858
                    self.match(ZmeiLangParser.NL) 
                self.state = 1863
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,172,self._ctx)

            self.state = 1864
            self.page_body()
            self.state = 1868
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,173,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1865
                    self.match(ZmeiLangParser.NL) 
                self.state = 1870
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,173,self._ctx)

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
        self.enterRule(localctx, 364, self.RULE_page_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1871
            self.match(ZmeiLangParser.SQ_BRACE_OPEN)
            self.state = 1873
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,174,self._ctx)
            if la_ == 1:
                self.state = 1872
                self.page_base()


            self.state = 1875
            self.page_name()
            self.state = 1877
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.KW_AS:
                self.state = 1876
                self.page_alias()


            self.state = 1887
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COLON:
                self.state = 1879
                self.match(ZmeiLangParser.COLON)
                self.state = 1881
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (ZmeiLangParser.DOT - 134)) | (1 << (ZmeiLangParser.SLASH - 134)) | (1 << (ZmeiLangParser.DOLLAR - 134)))) != 0):
                    self.state = 1880
                    self.page_url()


                self.state = 1885
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.COLON:
                    self.state = 1883
                    self.match(ZmeiLangParser.COLON)
                    self.state = 1884
                    self.page_template()




            self.state = 1889
            self.match(ZmeiLangParser.SQ_BRACE_CLOSE)
            self.state = 1891
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,179,self._ctx)
            if la_ == 1:
                self.state = 1890
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
        self.enterRule(localctx, 366, self.RULE_page_base)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1896
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,180,self._ctx)
            if la_ == 1:
                self.state = 1893
                self.id_or_kw()
                self.state = 1894
                self.match(ZmeiLangParser.DOT)


            self.state = 1898
            self.id_or_kw()
            self.state = 1899
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.DASH or _la==ZmeiLangParser.APPROX):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 1900
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
        self.enterRule(localctx, 368, self.RULE_page_alias)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1902
            self.match(ZmeiLangParser.KW_AS)
            self.state = 1903
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
        self.enterRule(localctx, 370, self.RULE_page_alias_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1905
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
        self.enterRule(localctx, 372, self.RULE_page_template)
        try:
            self.state = 1909
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.DIGIT, ZmeiLangParser.UNDERSCORE, ZmeiLangParser.DASH, ZmeiLangParser.DOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1907
                self.template_name()
                pass
            elif token in [ZmeiLangParser.ASSIGN, ZmeiLangParser.CODE_BLOCK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1908
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
        self.enterRule(localctx, 374, self.RULE_template_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1911
            self.file_name_part()
            self.state = 1916
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.SLASH:
                self.state = 1912
                self.match(ZmeiLangParser.SLASH)
                self.state = 1913
                self.file_name_part()
                self.state = 1918
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
        self.enterRule(localctx, 376, self.RULE_file_name_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1924 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1924
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                    self.state = 1919
                    self.id_or_kw()
                    pass
                elif token in [ZmeiLangParser.DIGIT]:
                    self.state = 1920
                    self.match(ZmeiLangParser.DIGIT)
                    pass
                elif token in [ZmeiLangParser.DASH]:
                    self.state = 1921
                    self.match(ZmeiLangParser.DASH)
                    pass
                elif token in [ZmeiLangParser.UNDERSCORE]:
                    self.state = 1922
                    self.match(ZmeiLangParser.UNDERSCORE)
                    pass
                elif token in [ZmeiLangParser.DOT]:
                    self.state = 1923
                    self.match(ZmeiLangParser.DOT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1926 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 42)) & ~0x3f) == 0 and ((1 << (_la - 42)) & ((1 << (ZmeiLangParser.KW_AUTH_TYPE_BASIC - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_SESSION - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_TOKEN - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 42)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 42)) | (1 << (ZmeiLangParser.KW_THEME - 42)) | (1 << (ZmeiLangParser.KW_INSTALL - 42)) | (1 << (ZmeiLangParser.KW_HEADER - 42)) | (1 << (ZmeiLangParser.KW_SERVICES - 42)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 42)) | (1 << (ZmeiLangParser.KW_CHILD - 42)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 42)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 42)) | (1 << (ZmeiLangParser.KW_PAGE - 42)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 42)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 42)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 42)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 42)) | (1 << (ZmeiLangParser.KW_BLOCK - 42)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 42)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 42)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 42)) | (1 << (ZmeiLangParser.KW_DELETE - 42)) | (1 << (ZmeiLangParser.KW_EDIT - 42)) | (1 << (ZmeiLangParser.KW_CREATE - 42)) | (1 << (ZmeiLangParser.KW_DETAIL - 42)) | (1 << (ZmeiLangParser.KW_SKIP - 42)) | (1 << (ZmeiLangParser.KW_FROM - 42)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 42)) | (1 << (ZmeiLangParser.KW_CSS - 42)) | (1 << (ZmeiLangParser.KW_JS - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 42)) | (1 << (ZmeiLangParser.KW_INLINE - 42)) | (1 << (ZmeiLangParser.KW_TYPE - 42)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 42)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 42)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 42)) | (1 << (ZmeiLangParser.KW_QUERY - 42)) | (1 << (ZmeiLangParser.KW_AUTH - 42)) | (1 << (ZmeiLangParser.KW_COUNT - 42)) | (1 << (ZmeiLangParser.KW_I18N - 42)))) != 0) or ((((_la - 106)) & ~0x3f) == 0 and ((1 << (_la - 106)) & ((1 << (ZmeiLangParser.KW_EXTENSION - 106)) | (1 << (ZmeiLangParser.KW_TABS - 106)) | (1 << (ZmeiLangParser.KW_LIST - 106)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 106)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 106)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 106)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 106)) | (1 << (ZmeiLangParser.KW_FIELDS - 106)) | (1 << (ZmeiLangParser.KW_IMPORT - 106)) | (1 << (ZmeiLangParser.KW_AS - 106)) | (1 << (ZmeiLangParser.WRITE_MODE - 106)) | (1 << (ZmeiLangParser.BOOL - 106)) | (1 << (ZmeiLangParser.ID - 106)) | (1 << (ZmeiLangParser.DIGIT - 106)) | (1 << (ZmeiLangParser.UNDERSCORE - 106)) | (1 << (ZmeiLangParser.DASH - 106)) | (1 << (ZmeiLangParser.DOT - 106)))) != 0)):
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
        self.enterRule(localctx, 378, self.RULE_page_url)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1929
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT or _la==ZmeiLangParser.DOLLAR:
                self.state = 1928
                _la = self._input.LA(1)
                if not(_la==ZmeiLangParser.DOT or _la==ZmeiLangParser.DOLLAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 1931
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
        self.enterRule(localctx, 380, self.RULE_url_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1936 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1936
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                    self.state = 1933
                    self.id_or_kw()
                    pass
                elif token in [ZmeiLangParser.DASH]:
                    self.state = 1934
                    self.match(ZmeiLangParser.DASH)
                    pass
                elif token in [ZmeiLangParser.DIGIT]:
                    self.state = 1935
                    self.match(ZmeiLangParser.DIGIT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1938 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 42)) & ~0x3f) == 0 and ((1 << (_la - 42)) & ((1 << (ZmeiLangParser.KW_AUTH_TYPE_BASIC - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_SESSION - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_TOKEN - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 42)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 42)) | (1 << (ZmeiLangParser.KW_THEME - 42)) | (1 << (ZmeiLangParser.KW_INSTALL - 42)) | (1 << (ZmeiLangParser.KW_HEADER - 42)) | (1 << (ZmeiLangParser.KW_SERVICES - 42)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 42)) | (1 << (ZmeiLangParser.KW_CHILD - 42)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 42)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 42)) | (1 << (ZmeiLangParser.KW_PAGE - 42)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 42)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 42)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 42)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 42)) | (1 << (ZmeiLangParser.KW_BLOCK - 42)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 42)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 42)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 42)) | (1 << (ZmeiLangParser.KW_DELETE - 42)) | (1 << (ZmeiLangParser.KW_EDIT - 42)) | (1 << (ZmeiLangParser.KW_CREATE - 42)) | (1 << (ZmeiLangParser.KW_DETAIL - 42)) | (1 << (ZmeiLangParser.KW_SKIP - 42)) | (1 << (ZmeiLangParser.KW_FROM - 42)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 42)) | (1 << (ZmeiLangParser.KW_CSS - 42)) | (1 << (ZmeiLangParser.KW_JS - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 42)) | (1 << (ZmeiLangParser.KW_INLINE - 42)) | (1 << (ZmeiLangParser.KW_TYPE - 42)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 42)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 42)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 42)) | (1 << (ZmeiLangParser.KW_QUERY - 42)) | (1 << (ZmeiLangParser.KW_AUTH - 42)) | (1 << (ZmeiLangParser.KW_COUNT - 42)) | (1 << (ZmeiLangParser.KW_I18N - 42)))) != 0) or ((((_la - 106)) & ~0x3f) == 0 and ((1 << (_la - 106)) & ((1 << (ZmeiLangParser.KW_EXTENSION - 106)) | (1 << (ZmeiLangParser.KW_TABS - 106)) | (1 << (ZmeiLangParser.KW_LIST - 106)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 106)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 106)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 106)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 106)) | (1 << (ZmeiLangParser.KW_FIELDS - 106)) | (1 << (ZmeiLangParser.KW_IMPORT - 106)) | (1 << (ZmeiLangParser.KW_AS - 106)) | (1 << (ZmeiLangParser.WRITE_MODE - 106)) | (1 << (ZmeiLangParser.BOOL - 106)) | (1 << (ZmeiLangParser.ID - 106)) | (1 << (ZmeiLangParser.DIGIT - 106)) | (1 << (ZmeiLangParser.DASH - 106)))) != 0)):
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
        self.enterRule(localctx, 382, self.RULE_url_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1940
            self.match(ZmeiLangParser.LT)
            self.state = 1941
            self.id_or_kw()
            self.state = 1942
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
        self.enterRule(localctx, 384, self.RULE_url_segment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1946
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.DIGIT, ZmeiLangParser.DASH]:
                self.state = 1944
                self.url_part()
                pass
            elif token in [ZmeiLangParser.LT]:
                self.state = 1945
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
        self.enterRule(localctx, 386, self.RULE_url_segments)
        self._la = 0 # Token type
        try:
            self.state = 1958
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,191,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1948
                self.match(ZmeiLangParser.SLASH)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1951 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 1949
                        self.match(ZmeiLangParser.SLASH)
                        self.state = 1950
                        self.url_segment()

                    else:
                        raise NoViableAltException(self)
                    self.state = 1953 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,189,self._ctx)

                self.state = 1956
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.SLASH:
                    self.state = 1955
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
        self.enterRule(localctx, 388, self.RULE_page_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1960
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
        self.enterRule(localctx, 390, self.RULE_page_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1965
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,192,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1962
                    self.page_field() 
                self.state = 1967
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,192,self._ctx)

            self.state = 1971
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,193,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1968
                    self.page_function() 
                self.state = 1973
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,193,self._ctx)

            self.state = 1975
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.ASSIGN or _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 1974
                self.page_code()


            self.state = 1980
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,195,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1977
                    self.match(ZmeiLangParser.NL) 
                self.state = 1982
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,195,self._ctx)

            self.state = 1986
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,196,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1983
                    self.page_annotation() 
                self.state = 1988
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,196,self._ctx)

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
        self.enterRule(localctx, 392, self.RULE_page_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1989
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
        self.enterRule(localctx, 394, self.RULE_page_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1991
            self.page_field_name()
            self.state = 1992
            self.match(ZmeiLangParser.ASSIGN)
            self.state = 1993
            self.page_field_code()
            self.state = 2000
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.NL]:
                self.state = 1995 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 1994
                        self.match(ZmeiLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 1997 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,197,self._ctx)

                pass
            elif token in [ZmeiLangParser.EOF]:
                self.state = 1999
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
        self.enterRule(localctx, 396, self.RULE_page_field_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2002
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
        self.enterRule(localctx, 398, self.RULE_page_field_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2004
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
        self.enterRule(localctx, 400, self.RULE_page_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2006
            self.page_function_name()
            self.state = 2007
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 2009
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 42)) & ~0x3f) == 0 and ((1 << (_la - 42)) & ((1 << (ZmeiLangParser.KW_AUTH_TYPE_BASIC - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_SESSION - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_TOKEN - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 42)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 42)) | (1 << (ZmeiLangParser.KW_THEME - 42)) | (1 << (ZmeiLangParser.KW_INSTALL - 42)) | (1 << (ZmeiLangParser.KW_HEADER - 42)) | (1 << (ZmeiLangParser.KW_SERVICES - 42)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 42)) | (1 << (ZmeiLangParser.KW_CHILD - 42)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 42)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 42)) | (1 << (ZmeiLangParser.KW_PAGE - 42)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 42)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 42)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 42)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 42)) | (1 << (ZmeiLangParser.KW_BLOCK - 42)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 42)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 42)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 42)) | (1 << (ZmeiLangParser.KW_DELETE - 42)) | (1 << (ZmeiLangParser.KW_EDIT - 42)) | (1 << (ZmeiLangParser.KW_CREATE - 42)) | (1 << (ZmeiLangParser.KW_DETAIL - 42)) | (1 << (ZmeiLangParser.KW_SKIP - 42)) | (1 << (ZmeiLangParser.KW_FROM - 42)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 42)) | (1 << (ZmeiLangParser.KW_CSS - 42)) | (1 << (ZmeiLangParser.KW_JS - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 42)) | (1 << (ZmeiLangParser.KW_INLINE - 42)) | (1 << (ZmeiLangParser.KW_TYPE - 42)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 42)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 42)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 42)) | (1 << (ZmeiLangParser.KW_QUERY - 42)) | (1 << (ZmeiLangParser.KW_AUTH - 42)) | (1 << (ZmeiLangParser.KW_COUNT - 42)) | (1 << (ZmeiLangParser.KW_I18N - 42)))) != 0) or ((((_la - 106)) & ~0x3f) == 0 and ((1 << (_la - 106)) & ((1 << (ZmeiLangParser.KW_EXTENSION - 106)) | (1 << (ZmeiLangParser.KW_TABS - 106)) | (1 << (ZmeiLangParser.KW_LIST - 106)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 106)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 106)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 106)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 106)) | (1 << (ZmeiLangParser.KW_FIELDS - 106)) | (1 << (ZmeiLangParser.KW_IMPORT - 106)) | (1 << (ZmeiLangParser.KW_AS - 106)) | (1 << (ZmeiLangParser.WRITE_MODE - 106)) | (1 << (ZmeiLangParser.BOOL - 106)) | (1 << (ZmeiLangParser.ID - 106)) | (1 << (ZmeiLangParser.DOT - 106)))) != 0):
                self.state = 2008
                self.page_function_args()


            self.state = 2011
            self.match(ZmeiLangParser.BRACE_CLOSE)
            self.state = 2013
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 2012
                self.code_block()


            self.state = 2021
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.NL]:
                self.state = 2016 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 2015
                        self.match(ZmeiLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 2018 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,201,self._ctx)

                pass
            elif token in [ZmeiLangParser.EOF]:
                self.state = 2020
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
        self.enterRule(localctx, 402, self.RULE_page_function_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2023
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

        def page_function_arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Page_function_argContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Page_function_argContext,i)


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
        self.enterRule(localctx, 404, self.RULE_page_function_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2025
            self.page_function_arg()
            self.state = 2030
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 2026
                self.match(ZmeiLangParser.COMA)
                self.state = 2027
                self.page_function_arg()
                self.state = 2032
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Page_function_argContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def DOT(self):
            return self.getToken(ZmeiLangParser.DOT, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_function_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_function_arg" ):
                listener.enterPage_function_arg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_function_arg" ):
                listener.exitPage_function_arg(self)




    def page_function_arg(self):

        localctx = ZmeiLangParser.Page_function_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 406, self.RULE_page_function_arg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2034
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 2033
                self.match(ZmeiLangParser.DOT)


            self.state = 2036
            self.id_or_kw()
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
        self.enterRule(localctx, 408, self.RULE_page_annotation)
        try:
            self.state = 2055
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.AN_STREAM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2038
                self.an_stream()
                pass
            elif token in [ZmeiLangParser.AN_REACT, ZmeiLangParser.AN_REACT_CLIENT, ZmeiLangParser.AN_REACT_SERVER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2039
                self.an_react()
                pass
            elif token in [ZmeiLangParser.AN_HTML]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2040
                self.an_html()
                pass
            elif token in [ZmeiLangParser.AN_MARKDOWN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 2041
                self.an_markdown()
                pass
            elif token in [ZmeiLangParser.AN_CRUD_DELETE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 2042
                self.an_crud_delete()
                pass
            elif token in [ZmeiLangParser.AN_POST]:
                self.enterOuterAlt(localctx, 6)
                self.state = 2043
                self.an_post()
                pass
            elif token in [ZmeiLangParser.AN_AUTH]:
                self.enterOuterAlt(localctx, 7)
                self.state = 2044
                self.an_auth()
                pass
            elif token in [ZmeiLangParser.AN_CRUD_CREATE]:
                self.enterOuterAlt(localctx, 8)
                self.state = 2045
                self.an_crud_create()
                pass
            elif token in [ZmeiLangParser.AN_CRUD_EDIT]:
                self.enterOuterAlt(localctx, 9)
                self.state = 2046
                self.an_crud_edit()
                pass
            elif token in [ZmeiLangParser.AN_CRUD]:
                self.enterOuterAlt(localctx, 10)
                self.state = 2047
                self.an_crud()
                pass
            elif token in [ZmeiLangParser.AN_CRUD_LIST]:
                self.enterOuterAlt(localctx, 11)
                self.state = 2048
                self.an_crud_list()
                pass
            elif token in [ZmeiLangParser.AN_MENU]:
                self.enterOuterAlt(localctx, 12)
                self.state = 2049
                self.an_menu()
                pass
            elif token in [ZmeiLangParser.AN_CRUD_DETAIL]:
                self.enterOuterAlt(localctx, 13)
                self.state = 2050
                self.an_crud_detail()
                pass
            elif token in [ZmeiLangParser.AN_PRIORITY]:
                self.enterOuterAlt(localctx, 14)
                self.state = 2051
                self.an_priority_marker()
                pass
            elif token in [ZmeiLangParser.AN_GET]:
                self.enterOuterAlt(localctx, 15)
                self.state = 2052
                self.an_get()
                pass
            elif token in [ZmeiLangParser.AN_ERROR]:
                self.enterOuterAlt(localctx, 16)
                self.state = 2053
                self.an_error()
                pass
            elif token in [ZmeiLangParser.NL]:
                self.enterOuterAlt(localctx, 17)
                self.state = 2054
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
        self.enterRule(localctx, 410, self.RULE_an_stream)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2057
            self.match(ZmeiLangParser.AN_STREAM)

            self.state = 2058
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 2061 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 2061
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.HASH]:
                    self.state = 2059
                    self.an_stream_model()
                    pass
                elif token in [ZmeiLangParser.NL]:
                    self.state = 2060
                    self.match(ZmeiLangParser.NL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 2063 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 42)) & ~0x3f) == 0 and ((1 << (_la - 42)) & ((1 << (ZmeiLangParser.KW_AUTH_TYPE_BASIC - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_SESSION - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_TOKEN - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 42)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 42)) | (1 << (ZmeiLangParser.KW_THEME - 42)) | (1 << (ZmeiLangParser.KW_INSTALL - 42)) | (1 << (ZmeiLangParser.KW_HEADER - 42)) | (1 << (ZmeiLangParser.KW_SERVICES - 42)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 42)) | (1 << (ZmeiLangParser.KW_CHILD - 42)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 42)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 42)) | (1 << (ZmeiLangParser.KW_PAGE - 42)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 42)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 42)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 42)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 42)) | (1 << (ZmeiLangParser.KW_BLOCK - 42)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 42)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 42)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 42)) | (1 << (ZmeiLangParser.KW_DELETE - 42)) | (1 << (ZmeiLangParser.KW_EDIT - 42)) | (1 << (ZmeiLangParser.KW_CREATE - 42)) | (1 << (ZmeiLangParser.KW_DETAIL - 42)) | (1 << (ZmeiLangParser.KW_SKIP - 42)) | (1 << (ZmeiLangParser.KW_FROM - 42)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 42)) | (1 << (ZmeiLangParser.KW_CSS - 42)) | (1 << (ZmeiLangParser.KW_JS - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 42)) | (1 << (ZmeiLangParser.KW_INLINE - 42)) | (1 << (ZmeiLangParser.KW_TYPE - 42)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 42)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 42)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 42)) | (1 << (ZmeiLangParser.KW_QUERY - 42)) | (1 << (ZmeiLangParser.KW_AUTH - 42)) | (1 << (ZmeiLangParser.KW_COUNT - 42)) | (1 << (ZmeiLangParser.KW_I18N - 42)))) != 0) or ((((_la - 106)) & ~0x3f) == 0 and ((1 << (_la - 106)) & ((1 << (ZmeiLangParser.KW_EXTENSION - 106)) | (1 << (ZmeiLangParser.KW_TABS - 106)) | (1 << (ZmeiLangParser.KW_LIST - 106)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 106)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 106)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 106)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 106)) | (1 << (ZmeiLangParser.KW_FIELDS - 106)) | (1 << (ZmeiLangParser.KW_IMPORT - 106)) | (1 << (ZmeiLangParser.KW_AS - 106)) | (1 << (ZmeiLangParser.WRITE_MODE - 106)) | (1 << (ZmeiLangParser.BOOL - 106)) | (1 << (ZmeiLangParser.NL - 106)) | (1 << (ZmeiLangParser.ID - 106)) | (1 << (ZmeiLangParser.HASH - 106)))) != 0)):
                    break

            self.state = 2065
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
        self.enterRule(localctx, 412, self.RULE_an_stream_model)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2067
            self.an_stream_target_model()
            self.state = 2069
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 2068
                self.an_stream_target_filter()


            self.state = 2072
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.EQUALS:
                self.state = 2071
                self.an_stream_field_list()


            self.state = 2075
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COMA:
                self.state = 2074
                self.match(ZmeiLangParser.COMA)


            self.state = 2078
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,211,self._ctx)
            if la_ == 1:
                self.state = 2077
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
        self.enterRule(localctx, 414, self.RULE_an_stream_target_model)
        try:
            self.state = 2082
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.HASH]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2080
                self.model_ref()
                pass
            elif token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2081
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
        self.enterRule(localctx, 416, self.RULE_an_stream_target_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2084
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
        self.enterRule(localctx, 418, self.RULE_an_stream_field_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2086
            self.match(ZmeiLangParser.EQUALS)
            self.state = 2087
            self.match(ZmeiLangParser.GT)
            self.state = 2097
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.STAR]:
                self.state = 2088
                self.match(ZmeiLangParser.STAR)
                pass
            elif token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                self.state = 2089
                self.an_stream_field_name()
                self.state = 2094
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,213,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 2090
                        self.match(ZmeiLangParser.COMA)
                        self.state = 2091
                        self.an_stream_field_name() 
                    self.state = 2096
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,213,self._ctx)

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
        self.enterRule(localctx, 420, self.RULE_an_stream_field_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2099
            self.id_or_kw()
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

        def an_react_type(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_react_typeContext,0)


        def DOT(self):
            return self.getToken(ZmeiLangParser.DOT, 0)

        def an_react_descriptor(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_react_descriptorContext,0)


        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def an_react_child(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_react_childContext,0)


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
        self.enterRule(localctx, 422, self.RULE_an_react)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2101
            self.an_react_type()
            self.state = 2104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 2102
                self.match(ZmeiLangParser.DOT)
                self.state = 2103
                self.an_react_descriptor()


            self.state = 2111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 2106
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 2108
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.KW_CHILD:
                    self.state = 2107
                    self.an_react_child()


                self.state = 2110
                self.match(ZmeiLangParser.BRACE_CLOSE)


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
        self.enterRule(localctx, 424, self.RULE_an_react_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2113
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.AN_REACT) | (1 << ZmeiLangParser.AN_REACT_CLIENT) | (1 << ZmeiLangParser.AN_REACT_SERVER))) != 0)):
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
        self.enterRule(localctx, 426, self.RULE_an_react_descriptor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2115
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_react_childContext(ParserRuleContext):

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
            return ZmeiLangParser.RULE_an_react_child

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_react_child" ):
                listener.enterAn_react_child(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_react_child" ):
                listener.exitAn_react_child(self)




    def an_react_child(self):

        localctx = ZmeiLangParser.An_react_childContext(self, self._ctx, self.state)
        self.enterRule(localctx, 428, self.RULE_an_react_child)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2117
            self.match(ZmeiLangParser.KW_CHILD)
            self.state = 2118
            self.match(ZmeiLangParser.COLON)
            self.state = 2119
            self.match(ZmeiLangParser.BOOL)
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
        self.enterRule(localctx, 430, self.RULE_an_html)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2121
            self.match(ZmeiLangParser.AN_HTML)
            self.state = 2124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 2122
                self.match(ZmeiLangParser.DOT)
                self.state = 2123
                self.an_html_descriptor()


            self.state = 2126
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
        self.enterRule(localctx, 432, self.RULE_an_html_descriptor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2128
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
        self.enterRule(localctx, 434, self.RULE_an_markdown)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2130
            self.match(ZmeiLangParser.AN_MARKDOWN)
            self.state = 2133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 2131
                self.match(ZmeiLangParser.DOT)
                self.state = 2132
                self.an_markdown_descriptor()


            self.state = 2135
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
        self.enterRule(localctx, 436, self.RULE_an_markdown_descriptor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2137
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
        self.enterRule(localctx, 438, self.RULE_an_crud_delete)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2139
            self.match(ZmeiLangParser.AN_CRUD_DELETE)
            self.state = 2140
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
        self.enterRule(localctx, 440, self.RULE_an_crud)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2142
            self.match(ZmeiLangParser.AN_CRUD)
            self.state = 2143
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
        self.enterRule(localctx, 442, self.RULE_an_crud_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 2145
                self.match(ZmeiLangParser.DOT)
                self.state = 2146
                self.an_crud_descriptor()


            self.state = 2149
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 2153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 2150
                self.match(ZmeiLangParser.NL)
                self.state = 2155
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2156
            self.an_crud_target_model()
            self.state = 2158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 2157
                self.an_crud_target_filter()


            self.state = 2177
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,224,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2175
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [ZmeiLangParser.KW_THEME]:
                        self.state = 2160
                        self.an_crud_theme()
                        pass
                    elif token in [ZmeiLangParser.KW_SKIP]:
                        self.state = 2161
                        self.an_crud_skip()
                        pass
                    elif token in [ZmeiLangParser.KW_FIELDS]:
                        self.state = 2162
                        self.an_crud_fields()
                        pass
                    elif token in [ZmeiLangParser.KW_LIST_FIELDS]:
                        self.state = 2163
                        self.an_crud_list_fields()
                        pass
                    elif token in [ZmeiLangParser.KW_PK_PARAM]:
                        self.state = 2164
                        self.an_crud_pk_param()
                        pass
                    elif token in [ZmeiLangParser.KW_ITEM_NAME]:
                        self.state = 2165
                        self.an_crud_item_name()
                        pass
                    elif token in [ZmeiLangParser.KW_BLOCK]:
                        self.state = 2166
                        self.an_crud_block()
                        pass
                    elif token in [ZmeiLangParser.KW_OBJECT_EXPR]:
                        self.state = 2167
                        self.an_crud_object_expr()
                        pass
                    elif token in [ZmeiLangParser.KW_CAN_EDIT]:
                        self.state = 2168
                        self.an_crud_can_edit()
                        pass
                    elif token in [ZmeiLangParser.KW_URL_PREFIX]:
                        self.state = 2169
                        self.an_crud_url_prefix()
                        pass
                    elif token in [ZmeiLangParser.KW_LINK_SUFFIX]:
                        self.state = 2170
                        self.an_crud_link_suffix()
                        pass
                    elif token in [ZmeiLangParser.KW_LIST]:
                        self.state = 2171
                        self.an_crud_list_type()
                        pass
                    elif token in [ZmeiLangParser.KW_HEADER]:
                        self.state = 2172
                        self.an_crud_header()
                        pass
                    elif token in [ZmeiLangParser.NL]:
                        self.state = 2173
                        self.match(ZmeiLangParser.NL)
                        pass
                    elif token in [ZmeiLangParser.COMA]:
                        self.state = 2174
                        self.match(ZmeiLangParser.COMA)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 2179
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,224,self._ctx)

            self.state = 2183
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,225,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2180
                    self.match(ZmeiLangParser.NL) 
                self.state = 2185
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,225,self._ctx)

            self.state = 2188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,226,self._ctx)
            if la_ == 1:
                self.state = 2186
                self.an_crud_next_page()

            elif la_ == 2:
                self.state = 2187
                self.an_crud_next_page_url()


            self.state = 2193
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,227,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2190
                    self.match(ZmeiLangParser.NL) 
                self.state = 2195
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,227,self._ctx)

            self.state = 2199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 85)) & ~0x3f) == 0 and ((1 << (_la - 85)) & ((1 << (ZmeiLangParser.KW_DELETE - 85)) | (1 << (ZmeiLangParser.KW_EDIT - 85)) | (1 << (ZmeiLangParser.KW_CREATE - 85)) | (1 << (ZmeiLangParser.KW_DETAIL - 85)) | (1 << (ZmeiLangParser.KW_LIST - 85)))) != 0):
                self.state = 2196
                self.an_crud_page_override()
                self.state = 2201
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 2202
                self.match(ZmeiLangParser.NL)
                self.state = 2207
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2208
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
        self.enterRule(localctx, 444, self.RULE_an_crud_page_override)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2210
            self.an_crud_view_name()
            self.state = 2214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 2211
                self.match(ZmeiLangParser.NL)
                self.state = 2216
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2217
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 2221
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,231,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2218
                    self.match(ZmeiLangParser.NL) 
                self.state = 2223
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,231,self._ctx)

            self.state = 2224
            self.page_body()
            self.state = 2228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 2225
                self.match(ZmeiLangParser.NL)
                self.state = 2230
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2231
            self.match(ZmeiLangParser.BRACE_CLOSE)
            self.state = 2235
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,233,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2232
                    self.match(ZmeiLangParser.NL) 
                self.state = 2237
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,233,self._ctx)

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
        self.enterRule(localctx, 446, self.RULE_an_crud_descriptor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2238
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
        self.enterRule(localctx, 448, self.RULE_an_crud_next_page)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 2240
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 2241
                self.an_crud_next_page_event_name()
                self.state = 2242
                self.match(ZmeiLangParser.BRACE_CLOSE)


            self.state = 2246
            self.match(ZmeiLangParser.EQUALS)
            self.state = 2247
            self.match(ZmeiLangParser.GT)
            self.state = 2248
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
        self.enterRule(localctx, 450, self.RULE_an_crud_next_page_event_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2250
            _la = self._input.LA(1)
            if not(((((_la - 85)) & ~0x3f) == 0 and ((1 << (_la - 85)) & ((1 << (ZmeiLangParser.KW_DELETE - 85)) | (1 << (ZmeiLangParser.KW_EDIT - 85)) | (1 << (ZmeiLangParser.KW_CREATE - 85)))) != 0)):
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
        self.enterRule(localctx, 452, self.RULE_an_crud_next_page_url)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 2252
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 2253
                self.an_crud_next_page_event_name()
                self.state = 2254
                self.match(ZmeiLangParser.BRACE_CLOSE)


            self.state = 2258
            self.match(ZmeiLangParser.EQUALS)
            self.state = 2259
            self.match(ZmeiLangParser.GT)
            self.state = 2260
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
        self.enterRule(localctx, 454, self.RULE_an_crud_next_page_url_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2262
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
        self.enterRule(localctx, 456, self.RULE_an_crud_target_model)
        try:
            self.state = 2266
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.HASH]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2264
                self.model_ref()
                pass
            elif token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2265
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
        self.enterRule(localctx, 458, self.RULE_an_crud_target_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2268
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
        self.enterRule(localctx, 460, self.RULE_an_crud_theme)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2270
            self.match(ZmeiLangParser.KW_THEME)
            self.state = 2271
            self.match(ZmeiLangParser.COLON)
            self.state = 2272
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
        self.enterRule(localctx, 462, self.RULE_an_crud_url_prefix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2274
            self.match(ZmeiLangParser.KW_URL_PREFIX)
            self.state = 2275
            self.match(ZmeiLangParser.COLON)
            self.state = 2276
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
        self.enterRule(localctx, 464, self.RULE_an_crud_url_prefix_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2278
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
        self.enterRule(localctx, 466, self.RULE_an_crud_link_suffix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2280
            self.match(ZmeiLangParser.KW_LINK_SUFFIX)
            self.state = 2281
            self.match(ZmeiLangParser.COLON)
            self.state = 2282
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
        self.enterRule(localctx, 468, self.RULE_an_crud_link_suffix_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2284
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
        self.enterRule(localctx, 470, self.RULE_an_crud_item_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2286
            self.match(ZmeiLangParser.KW_ITEM_NAME)
            self.state = 2287
            self.match(ZmeiLangParser.COLON)
            self.state = 2288
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
        self.enterRule(localctx, 472, self.RULE_an_crud_object_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2290
            self.match(ZmeiLangParser.KW_OBJECT_EXPR)
            self.state = 2294
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.ASSIGN]:
                self.state = 2291
                self.code_line()
                pass
            elif token in [ZmeiLangParser.COLON]:
                self.state = 2292
                self.match(ZmeiLangParser.COLON)
                self.state = 2293
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
        self.enterRule(localctx, 474, self.RULE_an_crud_can_edit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2296
            self.match(ZmeiLangParser.KW_CAN_EDIT)
            self.state = 2300
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.ASSIGN]:
                self.state = 2297
                self.code_line()
                pass
            elif token in [ZmeiLangParser.COLON]:
                self.state = 2298
                self.match(ZmeiLangParser.COLON)
                self.state = 2299
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
        self.enterRule(localctx, 476, self.RULE_an_crud_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2302
            self.match(ZmeiLangParser.KW_BLOCK)
            self.state = 2303
            self.match(ZmeiLangParser.COLON)
            self.state = 2304
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
        self.enterRule(localctx, 478, self.RULE_an_crud_pk_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2306
            self.match(ZmeiLangParser.KW_PK_PARAM)
            self.state = 2307
            self.match(ZmeiLangParser.COLON)
            self.state = 2308
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
        self.enterRule(localctx, 480, self.RULE_an_crud_skip)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2310
            self.match(ZmeiLangParser.KW_SKIP)
            self.state = 2311
            self.match(ZmeiLangParser.COLON)
            self.state = 2312
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
        self.enterRule(localctx, 482, self.RULE_an_crud_skip_values)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2314
            self.an_crud_view_name()
            self.state = 2319
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,239,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2315
                    self.match(ZmeiLangParser.COMA)
                    self.state = 2316
                    self.an_crud_view_name() 
                self.state = 2321
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,239,self._ctx)

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
        self.enterRule(localctx, 484, self.RULE_an_crud_view_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2322
            _la = self._input.LA(1)
            if not(((((_la - 85)) & ~0x3f) == 0 and ((1 << (_la - 85)) & ((1 << (ZmeiLangParser.KW_DELETE - 85)) | (1 << (ZmeiLangParser.KW_EDIT - 85)) | (1 << (ZmeiLangParser.KW_CREATE - 85)) | (1 << (ZmeiLangParser.KW_DETAIL - 85)) | (1 << (ZmeiLangParser.KW_LIST - 85)))) != 0)):
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
        self.enterRule(localctx, 486, self.RULE_an_crud_fields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2324
            self.match(ZmeiLangParser.KW_FIELDS)
            self.state = 2325
            self.match(ZmeiLangParser.COLON)
            self.state = 2326
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
        self.enterRule(localctx, 488, self.RULE_an_crud_list_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2328
            self.match(ZmeiLangParser.KW_LIST)
            self.state = 2329
            self.match(ZmeiLangParser.COLON)
            self.state = 2330
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

        def KW_INLINE_TYPE_TABULAR(self):
            return self.getToken(ZmeiLangParser.KW_INLINE_TYPE_TABULAR, 0)

        def KW_INLINE_TYPE_STACKED(self):
            return self.getToken(ZmeiLangParser.KW_INLINE_TYPE_STACKED, 0)

        def KW_INLINE_TYPE_POLYMORPHIC(self):
            return self.getToken(ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, 0)

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
        self.enterRule(localctx, 490, self.RULE_an_crud_list_type_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2332
            _la = self._input.LA(1)
            if not(((((_la - 94)) & ~0x3f) == 0 and ((1 << (_la - 94)) & ((1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 94)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 94)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 94)))) != 0)):
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
        self.enterRule(localctx, 492, self.RULE_an_crud_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2334
            self.match(ZmeiLangParser.KW_HEADER)
            self.state = 2335
            self.match(ZmeiLangParser.COLON)
            self.state = 2336
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
        self.enterRule(localctx, 494, self.RULE_an_crud_header_enabled)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2338
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
        self.enterRule(localctx, 496, self.RULE_an_crud_fields_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2340
            self.an_crud_field()
            self.state = 2345
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,240,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2341
                    self.match(ZmeiLangParser.COMA)
                    self.state = 2342
                    self.an_crud_field() 
                self.state = 2347
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,240,self._ctx)

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
        self.enterRule(localctx, 498, self.RULE_an_crud_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2348
            self.an_crud_field_spec()
            self.state = 2350
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 2349
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
        self.enterRule(localctx, 500, self.RULE_an_crud_field_spec)
        self._la = 0 # Token type
        try:
            self.state = 2357
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.STAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2352
                self.match(ZmeiLangParser.STAR)
                pass
            elif token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.EXCLUDE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2354
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.EXCLUDE:
                    self.state = 2353
                    self.match(ZmeiLangParser.EXCLUDE)


                self.state = 2356
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
        self.enterRule(localctx, 502, self.RULE_an_crud_field_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2359
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
        self.enterRule(localctx, 504, self.RULE_an_crud_list_fields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2361
            self.match(ZmeiLangParser.KW_LIST_FIELDS)
            self.state = 2362
            self.match(ZmeiLangParser.COLON)
            self.state = 2363
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
        self.enterRule(localctx, 506, self.RULE_an_crud_list_fields_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2365
            self.an_crud_list_field()
            self.state = 2370
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,244,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2366
                    self.match(ZmeiLangParser.COMA)
                    self.state = 2367
                    self.an_crud_list_field() 
                self.state = 2372
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,244,self._ctx)

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
        self.enterRule(localctx, 508, self.RULE_an_crud_list_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2373
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
        self.enterRule(localctx, 510, self.RULE_an_crud_list_field_spec)
        self._la = 0 # Token type
        try:
            self.state = 2380
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.STAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2375
                self.match(ZmeiLangParser.STAR)
                pass
            elif token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.EXCLUDE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2377
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.EXCLUDE:
                    self.state = 2376
                    self.match(ZmeiLangParser.EXCLUDE)


                self.state = 2379
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
        self.enterRule(localctx, 512, self.RULE_an_post)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2382
            self.match(ZmeiLangParser.AN_POST)
            self.state = 2384
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 2383
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
        self.enterRule(localctx, 514, self.RULE_an_auth)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2386
            self.match(ZmeiLangParser.AN_AUTH)
            self.state = 2388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 2387
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
        self.enterRule(localctx, 516, self.RULE_an_crud_create)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2390
            self.match(ZmeiLangParser.AN_CRUD_CREATE)
            self.state = 2391
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
        self.enterRule(localctx, 518, self.RULE_an_crud_edit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2393
            self.match(ZmeiLangParser.AN_CRUD_EDIT)
            self.state = 2394
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
        self.enterRule(localctx, 520, self.RULE_an_crud_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2396
            self.match(ZmeiLangParser.AN_CRUD_LIST)
            self.state = 2397
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
        self.enterRule(localctx, 522, self.RULE_an_menu)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2399
            self.match(ZmeiLangParser.AN_MENU)
            self.state = 2400
            self.match(ZmeiLangParser.DOT)
            self.state = 2401
            self.an_menu_descriptor()
            self.state = 2402
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 2406
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,249,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2403
                    self.match(ZmeiLangParser.NL) 
                self.state = 2408
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,249,self._ctx)

            self.state = 2410 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 2409
                    self.an_menu_item()

                else:
                    raise NoViableAltException(self)
                self.state = 2412 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,250,self._ctx)

            self.state = 2417
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 2414
                self.match(ZmeiLangParser.NL)
                self.state = 2419
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2420
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
        self.enterRule(localctx, 524, self.RULE_an_menu_descriptor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2422
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
        self.enterRule(localctx, 526, self.RULE_an_menu_item)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2425
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COMA:
                self.state = 2424
                self.match(ZmeiLangParser.COMA)


            self.state = 2430
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 2427
                self.match(ZmeiLangParser.NL)
                self.state = 2432
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2434
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.SQ_BRACE_OPEN:
                self.state = 2433
                self.an_menu_item_args()


            self.state = 2436
            self.an_menu_label()
            self.state = 2439
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.ASSIGN]:
                self.state = 2437
                self.an_menu_item_code()
                pass
            elif token in [ZmeiLangParser.COLON]:
                self.state = 2438
                self.an_menu_target()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 2444
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,256,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2441
                    self.match(ZmeiLangParser.NL) 
                self.state = 2446
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,256,self._ctx)

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
        self.enterRule(localctx, 528, self.RULE_an_menu_target)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2447
            self.match(ZmeiLangParser.COLON)
            self.state = 2450
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.KW_PAGE]:
                self.state = 2448
                self.an_menu_item_page()
                pass
            elif token in [ZmeiLangParser.STRING_DQ, ZmeiLangParser.STRING_SQ]:
                self.state = 2449
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
        self.enterRule(localctx, 530, self.RULE_an_menu_item_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2452
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
        self.enterRule(localctx, 532, self.RULE_an_menu_item_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2454
            self.match(ZmeiLangParser.SQ_BRACE_OPEN)
            self.state = 2455
            self.an_menu_item_arg()
            self.state = 2460
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 2456
                self.match(ZmeiLangParser.COMA)
                self.state = 2457
                self.an_menu_item_arg()
                self.state = 2462
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2463
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
        self.enterRule(localctx, 534, self.RULE_an_menu_item_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2465
            self.an_menu_item_arg_key()
            self.state = 2466
            self.match(ZmeiLangParser.EQUALS)
            self.state = 2467
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
        self.enterRule(localctx, 536, self.RULE_an_menu_item_arg_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2469
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
        self.enterRule(localctx, 538, self.RULE_an_menu_item_arg_val)
        try:
            self.state = 2474
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.STRING_DQ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2471
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2472
                self.match(ZmeiLangParser.STRING_SQ)
                pass
            elif token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2473
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
        self.enterRule(localctx, 540, self.RULE_an_menu_item_url)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2476
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
        self.enterRule(localctx, 542, self.RULE_an_menu_item_page)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2478
            self.match(ZmeiLangParser.KW_PAGE)
            self.state = 2479
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 2480
            self.an_menu_item_page_ref()
            self.state = 2481
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
        self.enterRule(localctx, 544, self.RULE_an_menu_item_page_ref)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2486
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,260,self._ctx)
            if la_ == 1:
                self.state = 2483
                self.id_or_kw()
                self.state = 2484
                self.match(ZmeiLangParser.DOT)


            self.state = 2488
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
        self.enterRule(localctx, 546, self.RULE_an_menu_label)
        try:
            self.state = 2493
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.STRING_DQ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2490
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2491
                self.match(ZmeiLangParser.STRING_SQ)
                pass
            elif token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2492
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
        self.enterRule(localctx, 548, self.RULE_an_crud_detail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2495
            self.match(ZmeiLangParser.AN_CRUD_DETAIL)
            self.state = 2496
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
        self.enterRule(localctx, 550, self.RULE_an_priority_marker)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2498
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

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


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
        self.enterRule(localctx, 552, self.RULE_an_get)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2500
            self.match(ZmeiLangParser.AN_GET)
            self.state = 2502
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 2501
                self.code_block()


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
        self.enterRule(localctx, 554, self.RULE_an_error)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2504
            self.match(ZmeiLangParser.AN_ERROR)
            self.state = 2505
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 2506
            self.an_error_code()
            self.state = 2507
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
        self.enterRule(localctx, 556, self.RULE_an_error_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2509
            self.match(ZmeiLangParser.DIGIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






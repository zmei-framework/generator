# Generated from /Users/aleksandrrudakov/dev/zmei/generator/grammar/ZmeiLangParser.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\u0095")
        buf.write("\u0875\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("\t\u00fb\4\u00fc\t\u00fc\3\2\7\2\u01fa\n\2\f\2\16\2\u01fd")
        buf.write("\13\2\3\2\7\2\u0200\n\2\f\2\16\2\u0203\13\2\3\2\7\2\u0206")
        buf.write("\n\2\f\2\16\2\u0209\13\2\3\2\5\2\u020c\n\2\3\2\6\2\u020f")
        buf.write("\n\2\r\2\16\2\u0210\5\2\u0213\n\2\3\2\7\2\u0216\n\2\f")
        buf.write("\2\16\2\u0219\13\2\3\2\5\2\u021c\n\2\3\2\6\2\u021f\n\2")
        buf.write("\r\2\16\2\u0220\5\2\u0223\n\2\3\2\7\2\u0226\n\2\f\2\16")
        buf.write("\2\u0229\13\2\3\2\3\2\3\3\6\3\u022e\n\3\r\3\16\3\u022f")
        buf.write("\3\4\6\4\u0233\n\4\r\4\16\4\u0234\3\5\3\5\3\6\3\6\3\7")
        buf.write("\3\7\5\7\u023d\n\7\3\7\3\7\3\7\6\7\u0242\n\7\r\7\16\7")
        buf.write("\u0243\3\b\5\b\u0247\n\b\3\b\3\b\3\t\3\t\3\t\7\t\u024e")
        buf.write("\n\t\f\t\16\t\u0251\13\t\3\n\3\n\3\n\5\n\u0256\n\n\3\n")
        buf.write("\5\n\u0259\n\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17")
        buf.write("\3\17\3\17\7\17\u0266\n\17\f\17\16\17\u0269\13\17\3\20")
        buf.write("\3\20\3\20\3\20\5\20\u026f\n\20\3\20\3\20\3\21\5\21\u0274")
        buf.write("\n\21\3\21\3\21\3\21\3\21\7\21\u027a\n\21\f\21\16\21\u027d")
        buf.write("\13\21\3\21\3\21\3\21\5\21\u0282\n\21\3\21\7\21\u0285")
        buf.write("\n\21\f\21\16\21\u0288\13\21\5\21\u028a\n\21\3\22\5\22")
        buf.write("\u028d\n\22\3\22\3\22\5\22\u0291\n\22\3\23\3\23\3\23\3")
        buf.write("\23\3\24\3\24\5\24\u0299\n\24\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u02a7\n\27\3")
        buf.write("\30\3\30\3\30\5\30\u02ac\n\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\7\32\u02b6\n\32\f\32\16\32\u02b9\13\32")
        buf.write("\3\33\3\33\3\33\5\33\u02be\n\33\3\34\3\34\3\34\5\34\u02c3")
        buf.write("\n\34\3\35\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\5\37\u02d0\n\37\3 \3 \3!\3!\5!\u02d6\n!\3!\7!\u02d9")
        buf.write("\n!\f!\16!\u02dc\13!\3!\7!\u02df\n!\f!\16!\u02e2\13!\3")
        buf.write("!\7!\u02e5\n!\f!\16!\u02e8\13!\3!\7!\u02eb\n!\f!\16!\u02ee")
        buf.write("\13!\3!\7!\u02f1\n!\f!\16!\u02f4\13!\3\"\3\"\3\"\6\"\u02f9")
        buf.write("\n\"\r\"\16\"\u02fa\3\"\5\"\u02fe\n\"\3#\3#\5#\u0302\n")
        buf.write("#\3#\3#\5#\u0306\n#\3#\3#\3#\3$\3$\3$\3$\6$\u030f\n$\r")
        buf.write("$\16$\u0310\3%\3%\3%\3%\5%\u0317\n%\3&\3&\3&\5&\u031c")
        buf.write("\n&\3\'\3\'\3\'\3\'\3\'\5\'\u0323\n\'\3(\3(\3)\7)\u0328")
        buf.write("\n)\f)\16)\u032b\13)\3)\3)\5)\u032f\n)\3)\5)\u0332\n)")
        buf.write("\3)\5)\u0335\n)\3)\6)\u0338\n)\r)\16)\u0339\3)\5)\u033d")
        buf.write("\n)\3*\3*\5*\u0341\n*\3*\3*\3*\5*\u0346\n*\3*\3*\3*\5")
        buf.write("*\u034b\n*\3+\3+\3,\5,\u0350\n,\3,\3,\3-\3-\3-\3.\3.\3")
        buf.write("/\3/\3/\3\60\3\60\3\61\3\61\3\62\6\62\u0361\n\62\r\62")
        buf.write("\16\62\u0362\3\62\3\62\5\62\u0367\n\62\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\5\67\u0385\n\67\38\38\39\39\3:\3:\3;\3")
        buf.write(";\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3")
        buf.write("D\3D\3D\3D\5D\u03a4\nD\3D\3D\5D\u03a8\nD\3E\3E\3F\3F\3")
        buf.write("F\3F\3F\7F\u03b1\nF\fF\16F\u03b4\13F\3G\5G\u03b7\nG\3")
        buf.write("G\3G\3H\3H\3H\5H\u03be\nH\3I\3I\3I\3J\3J\3J\3J\3J\5J\u03c8")
        buf.write("\nJ\3K\3K\3K\3K\3K\7K\u03cf\nK\fK\16K\u03d2\13K\3L\5L")
        buf.write("\u03d5\nL\3L\3L\3M\3M\3M\5M\u03dc\nM\3N\3N\3N\3O\3O\3")
        buf.write("O\3O\3O\3P\3P\3P\7P\u03e9\nP\fP\16P\u03ec\13P\3Q\3Q\3")
        buf.write("R\3R\3R\3R\3R\5R\u03f5\nR\3S\3S\3T\3T\3T\3T\3T\5T\u03fe")
        buf.write("\nT\3U\3U\3V\3V\3V\7V\u0405\nV\fV\16V\u0408\13V\3W\3W")
        buf.write("\3W\3W\3X\3X\3Y\3Y\3Y\3Z\7Z\u0414\nZ\fZ\16Z\u0417\13Z")
        buf.write("\3[\3[\3[\3\\\3\\\3\\\3\\\5\\\u0420\n\\\3\\\5\\\u0423")
        buf.write("\n\\\3\\\3\\\3]\3]\3^\3^\3_\3_\3`\3`\3`\3`\3a\3a\3a\3")
        buf.write("a\3a\3a\3a\3a\3a\3a\3a\3a\3a\3a\3a\5a\u0440\na\3b\3b\3")
        buf.write("b\3b\3b\3c\3c\3d\3d\3d\3d\3d\3e\3e\3e\7e\u0451\ne\fe\16")
        buf.write("e\u0454\13e\3f\3f\3f\5f\u0459\nf\3f\3f\3f\3f\5f\u045f")
        buf.write("\nf\3g\3g\3g\3g\7g\u0465\ng\fg\16g\u0468\13g\3h\3h\3h")
        buf.write("\3h\3h\3h\3h\3h\3h\3h\3h\3h\7h\u0476\nh\fh\16h\u0479\13")
        buf.write("h\3i\3i\3j\3j\3j\3j\7j\u0481\nj\fj\16j\u0484\13j\3k\3")
        buf.write("k\3k\7k\u0489\nk\fk\16k\u048c\13k\3l\3l\5l\u0490\nl\3")
        buf.write("l\3l\7l\u0494\nl\fl\16l\u0497\13l\3m\3m\5m\u049b\nm\3")
        buf.write("m\3m\7m\u049f\nm\fm\16m\u04a2\13m\3n\3n\5n\u04a6\nn\3")
        buf.write("n\3n\7n\u04aa\nn\fn\16n\u04ad\13n\3o\3o\3o\3o\7o\u04b3")
        buf.write("\no\fo\16o\u04b6\13o\3p\3p\3p\3p\7p\u04bc\np\fp\16p\u04bf")
        buf.write("\13p\3q\3q\3q\3q\5q\u04c5\nq\3q\7q\u04c8\nq\fq\16q\u04cb")
        buf.write("\13q\3r\3r\3s\3s\3s\3s\3s\7s\u04d4\ns\fs\16s\u04d7\13")
        buf.write("s\3s\3s\3t\3t\3t\3t\5t\u04df\nt\3u\3u\3v\3v\3w\3w\3w\3")
        buf.write("w\7w\u04e9\nw\fw\16w\u04ec\13w\3x\3x\3x\3x\5x\u04f2\n")
        buf.write("x\3y\3y\3z\3z\3{\3{\3{\3{\3{\6{\u04fd\n{\r{\16{\u04fe")
        buf.write("\3|\3|\3|\3|\3|\3}\3}\3~\3~\3~\3~\3~\3~\7~\u050e\n~\f")
        buf.write("~\16~\u0511\13~\5~\u0513\n~\3~\3~\5~\u0517\n~\3\177\3")
        buf.write("\177\3\u0080\3\u0080\3\u0081\3\u0081\3\u0081\3\u0082\3")
        buf.write("\u0082\3\u0082\3\u0083\3\u0083\3\u0083\3\u0084\3\u0084")
        buf.write("\3\u0084\3\u0085\3\u0085\3\u0085\3\u0086\3\u0086\3\u0086")
        buf.write("\3\u0087\3\u0087\3\u0087\3\u0087\3\u0087\3\u0088\3\u0088")
        buf.write("\3\u0088\3\u0088\3\u0088\3\u0089\3\u0089\3\u008a\3\u008a")
        buf.write("\3\u008a\3\u008a\3\u008a\5\u008a\u0540\n\u008a\3\u008b")
        buf.write("\3\u008b\3\u008c\3\u008c\3\u008c\3\u008c\3\u008c\3\u008c")
        buf.write("\3\u008c\3\u008c\3\u008c\3\u008c\3\u008c\3\u008c\3\u008c")
        buf.write("\3\u008c\7\u008c\u0552\n\u008c\f\u008c\16\u008c\u0555")
        buf.write("\13\u008c\3\u008c\7\u008c\u0558\n\u008c\f\u008c\16\u008c")
        buf.write("\u055b\13\u008c\3\u008c\5\u008c\u055e\n\u008c\3\u008c")
        buf.write("\7\u008c\u0561\n\u008c\f\u008c\16\u008c\u0564\13\u008c")
        buf.write("\3\u008d\3\u008d\3\u008d\7\u008d\u0569\n\u008d\f\u008d")
        buf.write("\16\u008d\u056c\13\u008d\3\u008d\3\u008d\3\u008d\7\u008d")
        buf.write("\u0571\n\u008d\f\u008d\16\u008d\u0574\13\u008d\3\u008d")
        buf.write("\7\u008d\u0577\n\u008d\f\u008d\16\u008d\u057a\13\u008d")
        buf.write("\3\u008e\3\u008e\3\u008e\3\u008e\3\u008e\7\u008e\u0581")
        buf.write("\n\u008e\f\u008e\16\u008e\u0584\13\u008e\3\u008f\3\u008f")
        buf.write("\3\u0090\3\u0090\3\u0091\3\u0091\3\u0091\3\u0091\3\u0091")
        buf.write("\7\u0091\u058f\n\u0091\f\u0091\16\u0091\u0592\13\u0091")
        buf.write("\3\u0092\3\u0092\3\u0092\3\u0092\3\u0092\3\u0092\3\u0092")
        buf.write("\7\u0092\u059b\n\u0092\f\u0092\16\u0092\u059e\13\u0092")
        buf.write("\3\u0092\5\u0092\u05a1\n\u0092\3\u0093\3\u0093\3\u0094")
        buf.write("\3\u0094\3\u0094\3\u0094\3\u0095\3\u0095\3\u0095\3\u0095")
        buf.write("\3\u0096\3\u0096\3\u0096\3\u0096\3\u0097\3\u0097\3\u0097")
        buf.write("\3\u0097\3\u0097\7\u0097\u05b6\n\u0097\f\u0097\16\u0097")
        buf.write("\u05b9\13\u0097\3\u0098\3\u0098\5\u0098\u05bd\n\u0098")
        buf.write("\3\u0098\3\u0098\3\u0098\3\u0098\3\u0099\3\u0099\3\u009a")
        buf.write("\3\u009a\3\u009b\3\u009b\3\u009b\3\u009b\7\u009b\u05cb")
        buf.write("\n\u009b\f\u009b\16\u009b\u05ce\13\u009b\3\u009c\3\u009c")
        buf.write("\3\u009c\3\u009c\7\u009c\u05d4\n\u009c\f\u009c\16\u009c")
        buf.write("\u05d7\13\u009c\3\u009d\3\u009d\3\u009d\3\u009d\7\u009d")
        buf.write("\u05dd\n\u009d\f\u009d\16\u009d\u05e0\13\u009d\3\u009e")
        buf.write("\3\u009e\3\u009e\3\u009e\7\u009e\u05e6\n\u009e\f\u009e")
        buf.write("\16\u009e\u05e9\13\u009e\3\u009f\3\u009f\3\u009f\3\u009f")
        buf.write("\7\u009f\u05ef\n\u009f\f\u009f\16\u009f\u05f2\13\u009f")
        buf.write("\3\u00a0\3\u00a0\3\u00a0\3\u00a0\7\u00a0\u05f8\n\u00a0")
        buf.write("\f\u00a0\16\u00a0\u05fb\13\u00a0\3\u00a1\3\u00a1\7\u00a1")
        buf.write("\u05ff\n\u00a1\f\u00a1\16\u00a1\u0602\13\u00a1\3\u00a1")
        buf.write("\3\u00a1\7\u00a1\u0606\n\u00a1\f\u00a1\16\u00a1\u0609")
        buf.write("\13\u00a1\3\u00a2\3\u00a2\5\u00a2\u060d\n\u00a2\3\u00a2")
        buf.write("\3\u00a2\5\u00a2\u0611\n\u00a2\3\u00a2\3\u00a2\5\u00a2")
        buf.write("\u0615\n\u00a2\3\u00a2\3\u00a2\5\u00a2\u0619\n\u00a2\5")
        buf.write("\u00a2\u061b\n\u00a2\3\u00a2\3\u00a2\5\u00a2\u061f\n\u00a2")
        buf.write("\3\u00a3\3\u00a3\3\u00a3\5\u00a3\u0624\n\u00a3\3\u00a3")
        buf.write("\3\u00a3\3\u00a3\3\u00a3\3\u00a4\3\u00a4\3\u00a4\3\u00a5")
        buf.write("\3\u00a5\3\u00a6\3\u00a6\5\u00a6\u0631\n\u00a6\3\u00a7")
        buf.write("\3\u00a7\3\u00a7\7\u00a7\u0636\n\u00a7\f\u00a7\16\u00a7")
        buf.write("\u0639\13\u00a7\3\u00a8\3\u00a8\3\u00a8\3\u00a8\3\u00a8")
        buf.write("\6\u00a8\u0640\n\u00a8\r\u00a8\16\u00a8\u0641\3\u00a9")
        buf.write("\5\u00a9\u0645\n\u00a9\3\u00a9\3\u00a9\3\u00aa\3\u00aa")
        buf.write("\3\u00aa\6\u00aa\u064c\n\u00aa\r\u00aa\16\u00aa\u064d")
        buf.write("\3\u00ab\3\u00ab\3\u00ab\3\u00ab\3\u00ac\3\u00ac\5\u00ac")
        buf.write("\u0656\n\u00ac\3\u00ad\3\u00ad\3\u00ad\6\u00ad\u065b\n")
        buf.write("\u00ad\r\u00ad\16\u00ad\u065c\3\u00ad\5\u00ad\u0660\n")
        buf.write("\u00ad\5\u00ad\u0662\n\u00ad\3\u00ae\3\u00ae\3\u00af\7")
        buf.write("\u00af\u0667\n\u00af\f\u00af\16\u00af\u066a\13\u00af\3")
        buf.write("\u00af\7\u00af\u066d\n\u00af\f\u00af\16\u00af\u0670\13")
        buf.write("\u00af\3\u00af\5\u00af\u0673\n\u00af\3\u00af\7\u00af\u0676")
        buf.write("\n\u00af\f\u00af\16\u00af\u0679\13\u00af\3\u00af\7\u00af")
        buf.write("\u067c\n\u00af\f\u00af\16\u00af\u067f\13\u00af\3\u00b0")
        buf.write("\3\u00b0\3\u00b1\3\u00b1\3\u00b1\3\u00b1\6\u00b1\u0687")
        buf.write("\n\u00b1\r\u00b1\16\u00b1\u0688\3\u00b1\5\u00b1\u068c")
        buf.write("\n\u00b1\3\u00b2\3\u00b2\3\u00b3\3\u00b3\3\u00b4\3\u00b4")
        buf.write("\3\u00b4\5\u00b4\u0695\n\u00b4\3\u00b4\3\u00b4\5\u00b4")
        buf.write("\u0699\n\u00b4\3\u00b4\6\u00b4\u069c\n\u00b4\r\u00b4\16")
        buf.write("\u00b4\u069d\3\u00b4\5\u00b4\u06a1\n\u00b4\3\u00b5\3\u00b5")
        buf.write("\3\u00b6\3\u00b6\3\u00b6\7\u00b6\u06a8\n\u00b6\f\u00b6")
        buf.write("\16\u00b6\u06ab\13\u00b6\3\u00b7\3\u00b7\3\u00b7\3\u00b7")
        buf.write("\3\u00b7\3\u00b7\3\u00b7\3\u00b7\3\u00b7\3\u00b7\3\u00b7")
        buf.write("\3\u00b7\3\u00b7\3\u00b7\3\u00b7\3\u00b7\5\u00b7\u06bd")
        buf.write("\n\u00b7\3\u00b8\3\u00b8\3\u00b8\5\u00b8\u06c2\n\u00b8")
        buf.write("\3\u00b8\3\u00b8\3\u00b9\3\u00b9\3\u00ba\3\u00ba\3\u00bb")
        buf.write("\3\u00bb\3\u00bb\5\u00bb\u06cd\n\u00bb\3\u00bb\3\u00bb")
        buf.write("\3\u00bc\3\u00bc\3\u00bd\3\u00bd\5\u00bd\u06d5\n\u00bd")
        buf.write("\3\u00be\3\u00be\3\u00be\3\u00be\3\u00be\3\u00bf\3\u00bf")
        buf.write("\3\u00c0\3\u00c0\5\u00c0\u06e0\n\u00c0\3\u00c1\3\u00c1")
        buf.write("\3\u00c1\3\u00c2\3\u00c2\3\u00c2\3\u00c3\3\u00c3\5\u00c3")
        buf.write("\u06ea\n\u00c3\3\u00c3\3\u00c3\7\u00c3\u06ee\n\u00c3\f")
        buf.write("\u00c3\16\u00c3\u06f1\13\u00c3\3\u00c3\3\u00c3\5\u00c3")
        buf.write("\u06f5\n\u00c3\3\u00c3\3\u00c3\3\u00c3\3\u00c3\3\u00c3")
        buf.write("\3\u00c3\3\u00c3\3\u00c3\3\u00c3\3\u00c3\3\u00c3\3\u00c3")
        buf.write("\3\u00c3\7\u00c3\u0704\n\u00c3\f\u00c3\16\u00c3\u0707")
        buf.write("\13\u00c3\3\u00c3\7\u00c3\u070a\n\u00c3\f\u00c3\16\u00c3")
        buf.write("\u070d\13\u00c3\3\u00c3\3\u00c3\5\u00c3\u0711\n\u00c3")
        buf.write("\3\u00c3\7\u00c3\u0714\n\u00c3\f\u00c3\16\u00c3\u0717")
        buf.write("\13\u00c3\3\u00c3\7\u00c3\u071a\n\u00c3\f\u00c3\16\u00c3")
        buf.write("\u071d\13\u00c3\3\u00c3\7\u00c3\u0720\n\u00c3\f\u00c3")
        buf.write("\16\u00c3\u0723\13\u00c3\3\u00c3\3\u00c3\3\u00c4\3\u00c4")
        buf.write("\7\u00c4\u0729\n\u00c4\f\u00c4\16\u00c4\u072c\13\u00c4")
        buf.write("\3\u00c4\3\u00c4\7\u00c4\u0730\n\u00c4\f\u00c4\16\u00c4")
        buf.write("\u0733\13\u00c4\3\u00c4\3\u00c4\7\u00c4\u0737\n\u00c4")
        buf.write("\f\u00c4\16\u00c4\u073a\13\u00c4\3\u00c4\3\u00c4\7\u00c4")
        buf.write("\u073e\n\u00c4\f\u00c4\16\u00c4\u0741\13\u00c4\3\u00c5")
        buf.write("\3\u00c5\3\u00c6\3\u00c6\3\u00c6\3\u00c6\5\u00c6\u0749")
        buf.write("\n\u00c6\3\u00c6\3\u00c6\3\u00c6\3\u00c6\3\u00c7\3\u00c7")
        buf.write("\3\u00c8\3\u00c8\3\u00c8\3\u00c8\5\u00c8\u0755\n\u00c8")
        buf.write("\3\u00c8\3\u00c8\3\u00c8\3\u00c8\3\u00c9\3\u00c9\3\u00ca")
        buf.write("\3\u00ca\5\u00ca\u075f\n\u00ca\3\u00cb\3\u00cb\3\u00cc")
        buf.write("\3\u00cc\3\u00cc\3\u00cc\3\u00cd\3\u00cd\3\u00cd\3\u00cd")
        buf.write("\3\u00ce\3\u00ce\3\u00cf\3\u00cf\3\u00cf\3\u00cf\3\u00d0")
        buf.write("\3\u00d0\3\u00d1\3\u00d1\3\u00d1\3\u00d1\3\u00d2\3\u00d2")
        buf.write("\3\u00d2\3\u00d2\5\u00d2\u077b\n\u00d2\3\u00d3\3\u00d3")
        buf.write("\3\u00d3\3\u00d3\5\u00d3\u0781\n\u00d3\3\u00d4\3\u00d4")
        buf.write("\3\u00d4\3\u00d4\3\u00d5\3\u00d5\3\u00d5\3\u00d5\3\u00d6")
        buf.write("\3\u00d6\3\u00d6\3\u00d6\3\u00d7\3\u00d7\3\u00d7\7\u00d7")
        buf.write("\u0792\n\u00d7\f\u00d7\16\u00d7\u0795\13\u00d7\3\u00d8")
        buf.write("\3\u00d8\3\u00d9\3\u00d9\3\u00d9\3\u00d9\3\u00da\3\u00da")
        buf.write("\3\u00da\7\u00da\u07a0\n\u00da\f\u00da\16\u00da\u07a3")
        buf.write("\13\u00da\3\u00db\3\u00db\5\u00db\u07a7\n\u00db\3\u00dc")
        buf.write("\3\u00dc\5\u00dc\u07ab\n\u00dc\3\u00dc\5\u00dc\u07ae\n")
        buf.write("\u00dc\3\u00dd\3\u00dd\3\u00de\3\u00de\3\u00de\3\u00de")
        buf.write("\3\u00df\3\u00df\3\u00df\7\u00df\u07b9\n\u00df\f\u00df")
        buf.write("\16\u00df\u07bc\13\u00df\3\u00e0\3\u00e0\3\u00e1\3\u00e1")
        buf.write("\5\u00e1\u07c2\n\u00e1\3\u00e1\5\u00e1\u07c5\n\u00e1\3")
        buf.write("\u00e2\3\u00e2\3\u00e2\3\u00e3\3\u00e3\3\u00e3\3\u00e4")
        buf.write("\3\u00e4\3\u00e4\3\u00e5\3\u00e5\3\u00e5\3\u00e5\3\u00e5")
        buf.write("\7\u00e5\u07d5\n\u00e5\f\u00e5\16\u00e5\u07d8\13\u00e5")
        buf.write("\3\u00e5\6\u00e5\u07db\n\u00e5\r\u00e5\16\u00e5\u07dc")
        buf.write("\3\u00e5\7\u00e5\u07e0\n\u00e5\f\u00e5\16\u00e5\u07e3")
        buf.write("\13\u00e5\3\u00e5\3\u00e5\3\u00e6\3\u00e6\3\u00e7\5\u00e7")
        buf.write("\u07ea\n\u00e7\3\u00e7\7\u00e7\u07ed\n\u00e7\f\u00e7\16")
        buf.write("\u00e7\u07f0\13\u00e7\3\u00e7\5\u00e7\u07f3\n\u00e7\3")
        buf.write("\u00e7\3\u00e7\3\u00e7\5\u00e7\u07f8\n\u00e7\3\u00e7\7")
        buf.write("\u00e7\u07fb\n\u00e7\f\u00e7\16\u00e7\u07fe\13\u00e7\3")
        buf.write("\u00e8\3\u00e8\3\u00e8\5\u00e8\u0803\n\u00e8\3\u00e9\3")
        buf.write("\u00e9\3\u00ea\3\u00ea\3\u00ea\3\u00ea\7\u00ea\u080b\n")
        buf.write("\u00ea\f\u00ea\16\u00ea\u080e\13\u00ea\3\u00ea\3\u00ea")
        buf.write("\3\u00eb\3\u00eb\3\u00eb\3\u00eb\3\u00ec\3\u00ec\3\u00ed")
        buf.write("\3\u00ed\3\u00ed\5\u00ed\u081b\n\u00ed\3\u00ee\3\u00ee")
        buf.write("\3\u00ef\3\u00ef\3\u00ef\3\u00ef\3\u00ef\3\u00f0\3\u00f0")
        buf.write("\3\u00f0\5\u00f0\u0827\n\u00f0\3\u00f0\3\u00f0\3\u00f1")
        buf.write("\3\u00f1\3\u00f1\5\u00f1\u082e\n\u00f1\3\u00f2\3\u00f2")
        buf.write("\5\u00f2\u0832\n\u00f2\3\u00f3\3\u00f3\3\u00f3\3\u00f3")
        buf.write("\6\u00f3\u0838\n\u00f3\r\u00f3\16\u00f3\u0839\3\u00f3")
        buf.write("\3\u00f3\3\u00f4\3\u00f4\5\u00f4\u0840\n\u00f4\3\u00f4")
        buf.write("\5\u00f4\u0843\n\u00f4\3\u00f4\5\u00f4\u0846\n\u00f4\3")
        buf.write("\u00f4\5\u00f4\u0849\n\u00f4\3\u00f5\3\u00f5\5\u00f5\u084d")
        buf.write("\n\u00f5\3\u00f6\3\u00f6\3\u00f7\3\u00f7\3\u00f7\3\u00f7")
        buf.write("\3\u00f7\3\u00f7\7\u00f7\u0857\n\u00f7\f\u00f7\16\u00f7")
        buf.write("\u085a\13\u00f7\5\u00f7\u085c\n\u00f7\3\u00f8\3\u00f8")
        buf.write("\3\u00f9\3\u00f9\3\u00f9\5\u00f9\u0863\n\u00f9\3\u00f9")
        buf.write("\5\u00f9\u0866\n\u00f9\3\u00fa\3\u00fa\3\u00fa\3\u00fa")
        buf.write("\3\u00fb\3\u00fb\3\u00fb\5\u00fb\u086f\n\u00fb\3\u00fb")
        buf.write("\3\u00fb\3\u00fc\3\u00fc\3\u00fc\2\2\u00fd\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@")
        buf.write("BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086")
        buf.write("\u0088\u008a\u008c\u008e\u0090\u0092\u0094\u0096\u0098")
        buf.write("\u009a\u009c\u009e\u00a0\u00a2\u00a4\u00a6\u00a8\u00aa")
        buf.write("\u00ac\u00ae\u00b0\u00b2\u00b4\u00b6\u00b8\u00ba\u00bc")
        buf.write("\u00be\u00c0\u00c2\u00c4\u00c6\u00c8\u00ca\u00cc\u00ce")
        buf.write("\u00d0\u00d2\u00d4\u00d6\u00d8\u00da\u00dc\u00de\u00e0")
        buf.write("\u00e2\u00e4\u00e6\u00e8\u00ea\u00ec\u00ee\u00f0\u00f2")
        buf.write("\u00f4\u00f6\u00f8\u00fa\u00fc\u00fe\u0100\u0102\u0104")
        buf.write("\u0106\u0108\u010a\u010c\u010e\u0110\u0112\u0114\u0116")
        buf.write("\u0118\u011a\u011c\u011e\u0120\u0122\u0124\u0126\u0128")
        buf.write("\u012a\u012c\u012e\u0130\u0132\u0134\u0136\u0138\u013a")
        buf.write("\u013c\u013e\u0140\u0142\u0144\u0146\u0148\u014a\u014c")
        buf.write("\u014e\u0150\u0152\u0154\u0156\u0158\u015a\u015c\u015e")
        buf.write("\u0160\u0162\u0164\u0166\u0168\u016a\u016c\u016e\u0170")
        buf.write("\u0172\u0174\u0176\u0178\u017a\u017c\u017e\u0180\u0182")
        buf.write("\u0184\u0186\u0188\u018a\u018c\u018e\u0190\u0192\u0194")
        buf.write("\u0196\u0198\u019a\u019c\u019e\u01a0\u01a2\u01a4\u01a6")
        buf.write("\u01a8\u01aa\u01ac\u01ae\u01b0\u01b2\u01b4\u01b6\u01b8")
        buf.write("\u01ba\u01bc\u01be\u01c0\u01c2\u01c4\u01c6\u01c8\u01ca")
        buf.write("\u01cc\u01ce\u01d0\u01d2\u01d4\u01d6\u01d8\u01da\u01dc")
        buf.write("\u01de\u01e0\u01e2\u01e4\u01e6\u01e8\u01ea\u01ec\u01ee")
        buf.write("\u01f0\u01f2\u01f4\u01f6\2\17\4\2(kmm\3\2\u0086\u0086")
        buf.write("\3\2\u0086\u0087\3\2\u008d\u008e\3\2\177\u0084\4\2nnx")
        buf.write("x\5\2^^``cc\3\2hj\4\2zz\u0084\u0084\4\2||\u0080\u0080")
        buf.write("\3\2\23\25\3\2\679\4\2\67:MM\2\u08b5\2\u01fb\3\2\2\2\4")
        buf.write("\u022d\3\2\2\2\6\u0232\3\2\2\2\b\u0236\3\2\2\2\n\u0238")
        buf.write("\3\2\2\2\f\u023c\3\2\2\2\16\u0246\3\2\2\2\20\u024a\3\2")
        buf.write("\2\2\22\u0258\3\2\2\2\24\u025a\3\2\2\2\26\u025c\3\2\2")
        buf.write("\2\30\u025e\3\2\2\2\32\u0260\3\2\2\2\34\u0262\3\2\2\2")
        buf.write("\36\u026a\3\2\2\2 \u0289\3\2\2\2\"\u028c\3\2\2\2$\u0292")
        buf.write("\3\2\2\2&\u0298\3\2\2\2(\u029a\3\2\2\2*\u029e\3\2\2\2")
        buf.write(",\u02a6\3\2\2\2.\u02a8\3\2\2\2\60\u02ad\3\2\2\2\62\u02b2")
        buf.write("\3\2\2\2\64\u02ba\3\2\2\2\66\u02bf\3\2\2\28\u02c4\3\2")
        buf.write("\2\2:\u02c8\3\2\2\2<\u02ca\3\2\2\2>\u02d1\3\2\2\2@\u02d3")
        buf.write("\3\2\2\2B\u02f5\3\2\2\2D\u02ff\3\2\2\2F\u030a\3\2\2\2")
        buf.write("H\u0312\3\2\2\2J\u031b\3\2\2\2L\u031d\3\2\2\2N\u0324\3")
        buf.write("\2\2\2P\u0329\3\2\2\2R\u034a\3\2\2\2T\u034c\3\2\2\2V\u034f")
        buf.write("\3\2\2\2X\u0353\3\2\2\2Z\u0356\3\2\2\2\\\u0358\3\2\2\2")
        buf.write("^\u035b\3\2\2\2`\u035d\3\2\2\2b\u0366\3\2\2\2d\u0368\3")
        buf.write("\2\2\2f\u036b\3\2\2\2h\u036e\3\2\2\2j\u0370\3\2\2\2l\u0384")
        buf.write("\3\2\2\2n\u0386\3\2\2\2p\u0388\3\2\2\2r\u038a\3\2\2\2")
        buf.write("t\u038c\3\2\2\2v\u038e\3\2\2\2x\u0390\3\2\2\2z\u0392\3")
        buf.write("\2\2\2|\u0394\3\2\2\2~\u0396\3\2\2\2\u0080\u0398\3\2\2")
        buf.write("\2\u0082\u039a\3\2\2\2\u0084\u039c\3\2\2\2\u0086\u039e")
        buf.write("\3\2\2\2\u0088\u03a9\3\2\2\2\u008a\u03ab\3\2\2\2\u008c")
        buf.write("\u03b6\3\2\2\2\u008e\u03bd\3\2\2\2\u0090\u03bf\3\2\2\2")
        buf.write("\u0092\u03c2\3\2\2\2\u0094\u03c9\3\2\2\2\u0096\u03d4\3")
        buf.write("\2\2\2\u0098\u03db\3\2\2\2\u009a\u03dd\3\2\2\2\u009c\u03e0")
        buf.write("\3\2\2\2\u009e\u03e5\3\2\2\2\u00a0\u03ed\3\2\2\2\u00a2")
        buf.write("\u03ef\3\2\2\2\u00a4\u03f6\3\2\2\2\u00a6\u03f8\3\2\2\2")
        buf.write("\u00a8\u03ff\3\2\2\2\u00aa\u0401\3\2\2\2\u00ac\u0409\3")
        buf.write("\2\2\2\u00ae\u040d\3\2\2\2\u00b0\u040f\3\2\2\2\u00b2\u0415")
        buf.write("\3\2\2\2\u00b4\u0418\3\2\2\2\u00b6\u041b\3\2\2\2\u00b8")
        buf.write("\u0426\3\2\2\2\u00ba\u0428\3\2\2\2\u00bc\u042a\3\2\2\2")
        buf.write("\u00be\u042c\3\2\2\2\u00c0\u043f\3\2\2\2\u00c2\u0441\3")
        buf.write("\2\2\2\u00c4\u0446\3\2\2\2\u00c6\u0448\3\2\2\2\u00c8\u044d")
        buf.write("\3\2\2\2\u00ca\u0455\3\2\2\2\u00cc\u0460\3\2\2\2\u00ce")
        buf.write("\u0477\3\2\2\2\u00d0\u047a\3\2\2\2\u00d2\u047c\3\2\2\2")
        buf.write("\u00d4\u0485\3\2\2\2\u00d6\u048d\3\2\2\2\u00d8\u0498\3")
        buf.write("\2\2\2\u00da\u04a3\3\2\2\2\u00dc\u04ae\3\2\2\2\u00de\u04b7")
        buf.write("\3\2\2\2\u00e0\u04c0\3\2\2\2\u00e2\u04cc\3\2\2\2\u00e4")
        buf.write("\u04ce\3\2\2\2\u00e6\u04da\3\2\2\2\u00e8\u04e0\3\2\2\2")
        buf.write("\u00ea\u04e2\3\2\2\2\u00ec\u04e4\3\2\2\2\u00ee\u04ed\3")
        buf.write("\2\2\2\u00f0\u04f3\3\2\2\2\u00f2\u04f5\3\2\2\2\u00f4\u04f7")
        buf.write("\3\2\2\2\u00f6\u0500\3\2\2\2\u00f8\u0505\3\2\2\2\u00fa")
        buf.write("\u0507\3\2\2\2\u00fc\u0518\3\2\2\2\u00fe\u051a\3\2\2\2")
        buf.write("\u0100\u051c\3\2\2\2\u0102\u051f\3\2\2\2\u0104\u0522\3")
        buf.write("\2\2\2\u0106\u0525\3\2\2\2\u0108\u0528\3\2\2\2\u010a\u052b")
        buf.write("\3\2\2\2\u010c\u052e\3\2\2\2\u010e\u0533\3\2\2\2\u0110")
        buf.write("\u0538\3\2\2\2\u0112\u053a\3\2\2\2\u0114\u0541\3\2\2\2")
        buf.write("\u0116\u0543\3\2\2\2\u0118\u0565\3\2\2\2\u011a\u057b\3")
        buf.write("\2\2\2\u011c\u0585\3\2\2\2\u011e\u0587\3\2\2\2\u0120\u0589")
        buf.write("\3\2\2\2\u0122\u0593\3\2\2\2\u0124\u05a2\3\2\2\2\u0126")
        buf.write("\u05a4\3\2\2\2\u0128\u05a8\3\2\2\2\u012a\u05ac\3\2\2\2")
        buf.write("\u012c\u05b0\3\2\2\2\u012e\u05ba\3\2\2\2\u0130\u05c2\3")
        buf.write("\2\2\2\u0132\u05c4\3\2\2\2\u0134\u05c6\3\2\2\2\u0136\u05cf")
        buf.write("\3\2\2\2\u0138\u05d8\3\2\2\2\u013a\u05e1\3\2\2\2\u013c")
        buf.write("\u05ea\3\2\2\2\u013e\u05f3\3\2\2\2\u0140\u05fc\3\2\2\2")
        buf.write("\u0142\u060a\3\2\2\2\u0144\u0623\3\2\2\2\u0146\u0629\3")
        buf.write("\2\2\2\u0148\u062c\3\2\2\2\u014a\u0630\3\2\2\2\u014c\u0632")
        buf.write("\3\2\2\2\u014e\u063f\3\2\2\2\u0150\u0644\3\2\2\2\u0152")
        buf.write("\u064b\3\2\2\2\u0154\u064f\3\2\2\2\u0156\u0655\3\2\2\2")
        buf.write("\u0158\u0661\3\2\2\2\u015a\u0663\3\2\2\2\u015c\u0668\3")
        buf.write("\2\2\2\u015e\u0680\3\2\2\2\u0160\u0682\3\2\2\2\u0162\u068d")
        buf.write("\3\2\2\2\u0164\u068f\3\2\2\2\u0166\u0691\3\2\2\2\u0168")
        buf.write("\u06a2\3\2\2\2\u016a\u06a4\3\2\2\2\u016c\u06bc\3\2\2\2")
        buf.write("\u016e\u06be\3\2\2\2\u0170\u06c5\3\2\2\2\u0172\u06c7\3")
        buf.write("\2\2\2\u0174\u06c9\3\2\2\2\u0176\u06d0\3\2\2\2\u0178\u06d2")
        buf.write("\3\2\2\2\u017a\u06d6\3\2\2\2\u017c\u06db\3\2\2\2\u017e")
        buf.write("\u06dd\3\2\2\2\u0180\u06e1\3\2\2\2\u0182\u06e4\3\2\2\2")
        buf.write("\u0184\u06e9\3\2\2\2\u0186\u0726\3\2\2\2\u0188\u0742\3")
        buf.write("\2\2\2\u018a\u0748\3\2\2\2\u018c\u074e\3\2\2\2\u018e\u0754")
        buf.write("\3\2\2\2\u0190\u075a\3\2\2\2\u0192\u075e\3\2\2\2\u0194")
        buf.write("\u0760\3\2\2\2\u0196\u0762\3\2\2\2\u0198\u0766\3\2\2\2")
        buf.write("\u019a\u076a\3\2\2\2\u019c\u076c\3\2\2\2\u019e\u0770\3")
        buf.write("\2\2\2\u01a0\u0772\3\2\2\2\u01a2\u0776\3\2\2\2\u01a4\u077c")
        buf.write("\3\2\2\2\u01a6\u0782\3\2\2\2\u01a8\u0786\3\2\2\2\u01aa")
        buf.write("\u078a\3\2\2\2\u01ac\u078e\3\2\2\2\u01ae\u0796\3\2\2\2")
        buf.write("\u01b0\u0798\3\2\2\2\u01b2\u079c\3\2\2\2\u01b4\u07a4\3")
        buf.write("\2\2\2\u01b6\u07ad\3\2\2\2\u01b8\u07af\3\2\2\2\u01ba\u07b1")
        buf.write("\3\2\2\2\u01bc\u07b5\3\2\2\2\u01be\u07bd\3\2\2\2\u01c0")
        buf.write("\u07c4\3\2\2\2\u01c2\u07c6\3\2\2\2\u01c4\u07c9\3\2\2\2")
        buf.write("\u01c6\u07cc\3\2\2\2\u01c8\u07cf\3\2\2\2\u01ca\u07e6\3")
        buf.write("\2\2\2\u01cc\u07e9\3\2\2\2\u01ce\u07ff\3\2\2\2\u01d0\u0804")
        buf.write("\3\2\2\2\u01d2\u0806\3\2\2\2\u01d4\u0811\3\2\2\2\u01d6")
        buf.write("\u0815\3\2\2\2\u01d8\u081a\3\2\2\2\u01da\u081c\3\2\2\2")
        buf.write("\u01dc\u081e\3\2\2\2\u01de\u0826\3\2\2\2\u01e0\u082d\3")
        buf.write("\2\2\2\u01e2\u082f\3\2\2\2\u01e4\u0833\3\2\2\2\u01e6\u083d")
        buf.write("\3\2\2\2\u01e8\u084c\3\2\2\2\u01ea\u084e\3\2\2\2\u01ec")
        buf.write("\u0850\3\2\2\2\u01ee\u085d\3\2\2\2\u01f0\u085f\3\2\2\2")
        buf.write("\u01f2\u0867\3\2\2\2\u01f4\u086b\3\2\2\2\u01f6\u0872\3")
        buf.write("\2\2\2\u01f8\u01fa\7l\2\2\u01f9\u01f8\3\2\2\2\u01fa\u01fd")
        buf.write("\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc")
        buf.write("\u0201\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fe\u0200\5,\27\2")
        buf.write("\u01ff\u01fe\3\2\2\2\u0200\u0203\3\2\2\2\u0201\u01ff\3")
        buf.write("\2\2\2\u0201\u0202\3\2\2\2\u0202\u0207\3\2\2\2\u0203\u0201")
        buf.write("\3\2\2\2\u0204\u0206\7l\2\2\u0205\u0204\3\2\2\2\u0206")
        buf.write("\u0209\3\2\2\2\u0207\u0205\3\2\2\2\u0207\u0208\3\2\2\2")
        buf.write("\u0208\u0212\3\2\2\2\u0209\u0207\3\2\2\2\u020a\u020c\5")
        buf.write("\4\3\2\u020b\u020a\3\2\2\2\u020b\u020c\3\2\2\2\u020c\u020e")
        buf.write("\3\2\2\2\u020d\u020f\5\u0140\u00a1\2\u020e\u020d\3\2\2")
        buf.write("\2\u020f\u0210\3\2\2\2\u0210\u020e\3\2\2\2\u0210\u0211")
        buf.write("\3\2\2\2\u0211\u0213\3\2\2\2\u0212\u020b\3\2\2\2\u0212")
        buf.write("\u0213\3\2\2\2\u0213\u0217\3\2\2\2\u0214\u0216\7l\2\2")
        buf.write("\u0215\u0214\3\2\2\2\u0216\u0219\3\2\2\2\u0217\u0215\3")
        buf.write("\2\2\2\u0217\u0218\3\2\2\2\u0218\u0222\3\2\2\2\u0219\u0217")
        buf.write("\3\2\2\2\u021a\u021c\5\6\4\2\u021b\u021a\3\2\2\2\u021b")
        buf.write("\u021c\3\2\2\2\u021c\u021e\3\2\2\2\u021d\u021f\5@!\2\u021e")
        buf.write("\u021d\3\2\2\2\u021f\u0220\3\2\2\2\u0220\u021e\3\2\2\2")
        buf.write("\u0220\u0221\3\2\2\2\u0221\u0223\3\2\2\2\u0222\u021b\3")
        buf.write("\2\2\2\u0222\u0223\3\2\2\2\u0223\u0227\3\2\2\2\u0224\u0226")
        buf.write("\7l\2\2\u0225\u0224\3\2\2\2\u0226\u0229\3\2\2\2\u0227")
        buf.write("\u0225\3\2\2\2\u0227\u0228\3\2\2\2\u0228\u022a\3\2\2\2")
        buf.write("\u0229\u0227\3\2\2\2\u022a\u022b\7\2\2\3\u022b\3\3\2\2")
        buf.write("\2\u022c\u022e\5\b\5\2\u022d\u022c\3\2\2\2\u022e\u022f")
        buf.write("\3\2\2\2\u022f\u022d\3\2\2\2\u022f\u0230\3\2\2\2\u0230")
        buf.write("\5\3\2\2\2\u0231\u0233\5\n\6\2\u0232\u0231\3\2\2\2\u0233")
        buf.write("\u0234\3\2\2\2\u0234\u0232\3\2\2\2\u0234\u0235\3\2\2\2")
        buf.write("\u0235\7\3\2\2\2\u0236\u0237\5\f\7\2\u0237\t\3\2\2\2\u0238")
        buf.write("\u0239\5\f\7\2\u0239\13\3\2\2\2\u023a\u023b\7<\2\2\u023b")
        buf.write("\u023d\5\16\b\2\u023c\u023a\3\2\2\2\u023c\u023d\3\2\2")
        buf.write("\2\u023d\u023e\3\2\2\2\u023e\u023f\7S\2\2\u023f\u0241")
        buf.write("\5\20\t\2\u0240\u0242\7l\2\2\u0241\u0240\3\2\2\2\u0242")
        buf.write("\u0243\3\2\2\2\u0243\u0241\3\2\2\2\u0243\u0244\3\2\2\2")
        buf.write("\u0244\r\3\2\2\2\u0245\u0247\7|\2\2\u0246\u0245\3\2\2")
        buf.write("\2\u0246\u0247\3\2\2\2\u0247\u0248\3\2\2\2\u0248\u0249")
        buf.write("\5\34\17\2\u0249\17\3\2\2\2\u024a\u024f\5\22\n\2\u024b")
        buf.write("\u024c\7{\2\2\u024c\u024e\5\22\n\2\u024d\u024b\3\2\2\2")
        buf.write("\u024e\u0251\3\2\2\2\u024f\u024d\3\2\2\2\u024f\u0250\3")
        buf.write("\2\2\2\u0250\21\3\2\2\2\u0251\u024f\3\2\2\2\u0252\u0255")
        buf.write("\5\24\13\2\u0253\u0254\7T\2\2\u0254\u0256\5\26\f\2\u0255")
        buf.write("\u0253\3\2\2\2\u0255\u0256\3\2\2\2\u0256\u0259\3\2\2\2")
        buf.write("\u0257\u0259\5\30\r\2\u0258\u0252\3\2\2\2\u0258\u0257")
        buf.write("\3\2\2\2\u0259\23\3\2\2\2\u025a\u025b\5\34\17\2\u025b")
        buf.write("\25\3\2\2\2\u025c\u025d\5\32\16\2\u025d\27\3\2\2\2\u025e")
        buf.write("\u025f\7\u0083\2\2\u025f\31\3\2\2\2\u0260\u0261\t\2\2")
        buf.write("\2\u0261\33\3\2\2\2\u0262\u0267\5\32\16\2\u0263\u0264")
        buf.write("\7|\2\2\u0264\u0266\5\32\16\2\u0265\u0263\3\2\2\2\u0266")
        buf.write("\u0269\3\2\2\2\u0267\u0265\3\2\2\2\u0267\u0268\3\2\2\2")
        buf.write("\u0268\35\3\2\2\2\u0269\u0267\3\2\2\2\u026a\u026e\7}\2")
        buf.write("\2\u026b\u026c\5\32\16\2\u026c\u026d\7|\2\2\u026d\u026f")
        buf.write("\3\2\2\2\u026e\u026b\3\2\2\2\u026e\u026f\3\2\2\2\u026f")
        buf.write("\u0270\3\2\2\2\u0270\u0271\5\32\16\2\u0271\37\3\2\2\2")
        buf.write("\u0272\u0274\7|\2\2\u0273\u0272\3\2\2\2\u0273\u0274\3")
        buf.write("\2\2\2\u0274\u0275\3\2\2\2\u0275\u027b\7\u0083\2\2\u0276")
        buf.write("\u0277\7{\2\2\u0277\u0278\7s\2\2\u0278\u027a\5\"\22\2")
        buf.write("\u0279\u0276\3\2\2\2\u027a\u027d\3\2\2\2\u027b\u0279\3")
        buf.write("\2\2\2\u027b\u027c\3\2\2\2\u027c\u028a\3\2\2\2\u027d\u027b")
        buf.write("\3\2\2\2\u027e\u0286\5\32\16\2\u027f\u0281\7{\2\2\u0280")
        buf.write("\u0282\7s\2\2\u0281\u0280\3\2\2\2\u0281\u0282\3\2\2\2")
        buf.write("\u0282\u0283\3\2\2\2\u0283\u0285\5\"\22\2\u0284\u027f")
        buf.write("\3\2\2\2\u0285\u0288\3\2\2\2\u0286\u0284\3\2\2\2\u0286")
        buf.write("\u0287\3\2\2\2\u0287\u028a\3\2\2\2\u0288\u0286\3\2\2\2")
        buf.write("\u0289\u0273\3\2\2\2\u0289\u027e\3\2\2\2\u028a!\3\2\2")
        buf.write("\2\u028b\u028d\7\u0083\2\2\u028c\u028b\3\2\2\2\u028c\u028d")
        buf.write("\3\2\2\2\u028d\u028e\3\2\2\2\u028e\u0290\5\32\16\2\u028f")
        buf.write("\u0291\7\u0083\2\2\u0290\u028f\3\2\2\2\u0290\u0291\3\2")
        buf.write("\2\2\u0291#\3\2\2\2\u0292\u0293\7v\2\2\u0293\u0294\7(")
        buf.write("\2\2\u0294\u0295\7w\2\2\u0295%\3\2\2\2\u0296\u0299\5*")
        buf.write("\26\2\u0297\u0299\5(\25\2\u0298\u0296\3\2\2\2\u0298\u0297")
        buf.write("\3\2\2\2\u0299\'\3\2\2\2\u029a\u029b\7\u008d\2\2\u029b")
        buf.write("\u029c\7\u0091\2\2\u029c\u029d\7l\2\2\u029d)\3\2\2\2\u029e")
        buf.write("\u029f\7\u008f\2\2\u029f+\3\2\2\2\u02a0\u02a7\5<\37\2")
        buf.write("\u02a1\u02a7\58\35\2\u02a2\u02a7\5\66\34\2\u02a3\u02a7")
        buf.write("\5\64\33\2\u02a4\u02a7\5\60\31\2\u02a5\u02a7\7l\2\2\u02a6")
        buf.write("\u02a0\3\2\2\2\u02a6\u02a1\3\2\2\2\u02a6\u02a2\3\2\2\2")
        buf.write("\u02a6\u02a3\3\2\2\2\u02a6\u02a4\3\2\2\2\u02a6\u02a5\3")
        buf.write("\2\2\2\u02a7-\3\2\2\2\u02a8\u02ab\7%\2\2\u02a9\u02aa\7")
        buf.write("t\2\2\u02aa\u02ac\7u\2\2\u02ab\u02a9\3\2\2\2\u02ab\u02ac")
        buf.write("\3\2\2\2\u02ac/\3\2\2\2\u02ad\u02ae\7$\2\2\u02ae\u02af")
        buf.write("\7t\2\2\u02af\u02b0\5\62\32\2\u02b0\u02b1\7u\2\2\u02b1")
        buf.write("\61\3\2\2\2\u02b2\u02b7\7m\2\2\u02b3\u02b4\7{\2\2\u02b4")
        buf.write("\u02b6\7m\2\2\u02b5\u02b3\3\2\2\2\u02b6\u02b9\3\2\2\2")
        buf.write("\u02b7\u02b5\3\2\2\2\u02b7\u02b8\3\2\2\2\u02b8\63\3\2")
        buf.write("\2\2\u02b9\u02b7\3\2\2\2\u02ba\u02bd\7\16\2\2\u02bb\u02bc")
        buf.write("\7t\2\2\u02bc\u02be\7u\2\2\u02bd\u02bb\3\2\2\2\u02bd\u02be")
        buf.write("\3\2\2\2\u02be\65\3\2\2\2\u02bf\u02c2\7\6\2\2\u02c0\u02c1")
        buf.write("\7t\2\2\u02c1\u02c3\7u\2\2\u02c2\u02c0\3\2\2\2\u02c2\u02c3")
        buf.write("\3\2\2\2\u02c3\67\3\2\2\2\u02c4\u02c5\7\4\2\2\u02c5\u02c6")
        buf.write("\5:\36\2\u02c6\u02c7\5&\24\2\u02c79\3\2\2\2\u02c8\u02c9")
        buf.write("\t\3\2\2\u02c9;\3\2\2\2\u02ca\u02cf\7\'\2\2\u02cb\u02cc")
        buf.write("\7t\2\2\u02cc\u02cd\5> \2\u02cd\u02ce\7u\2\2\u02ce\u02d0")
        buf.write("\3\2\2\2\u02cf\u02cb\3\2\2\2\u02cf\u02d0\3\2\2\2\u02d0")
        buf.write("=\3\2\2\2\u02d1\u02d2\t\4\2\2\u02d2?\3\2\2\2\u02d3\u02d5")
        buf.write("\5D#\2\u02d4\u02d6\5B\"\2\u02d5\u02d4\3\2\2\2\u02d5\u02d6")
        buf.write("\3\2\2\2\u02d6\u02da\3\2\2\2\u02d7\u02d9\7l\2\2\u02d8")
        buf.write("\u02d7\3\2\2\2\u02d9\u02dc\3\2\2\2\u02da\u02d8\3\2\2\2")
        buf.write("\u02da\u02db\3\2\2\2\u02db\u02e0\3\2\2\2\u02dc\u02da\3")
        buf.write("\2\2\2\u02dd\u02df\5P)\2\u02de\u02dd\3\2\2\2\u02df\u02e2")
        buf.write("\3\2\2\2\u02e0\u02de\3\2\2\2\u02e0\u02e1\3\2\2\2\u02e1")
        buf.write("\u02e6\3\2\2\2\u02e2\u02e0\3\2\2\2\u02e3\u02e5\7l\2\2")
        buf.write("\u02e4\u02e3\3\2\2\2\u02e5\u02e8\3\2\2\2\u02e6\u02e4\3")
        buf.write("\2\2\2\u02e6\u02e7\3\2\2\2\u02e7\u02ec\3\2\2\2\u02e8\u02e6")
        buf.write("\3\2\2\2\u02e9\u02eb\5\u00c0a\2\u02ea\u02e9\3\2\2\2\u02eb")
        buf.write("\u02ee\3\2\2\2\u02ec\u02ea\3\2\2\2\u02ec\u02ed\3\2\2\2")
        buf.write("\u02ed\u02f2\3\2\2\2\u02ee\u02ec\3\2\2\2\u02ef\u02f1\7")
        buf.write("l\2\2\u02f0\u02ef\3\2\2\2\u02f1\u02f4\3\2\2\2\u02f2\u02f0")
        buf.write("\3\2\2\2\u02f2\u02f3\3\2\2\2\u02f3A\3\2\2\2\u02f4\u02f2")
        buf.write("\3\2\2\2\u02f5\u02f6\7\177\2\2\u02f6\u02fd\t\4\2\2\u02f7")
        buf.write("\u02f9\7l\2\2\u02f8\u02f7\3\2\2\2\u02f9\u02fa\3\2\2\2")
        buf.write("\u02fa\u02f8\3\2\2\2\u02fa\u02fb\3\2\2\2\u02fb\u02fe\3")
        buf.write("\2\2\2\u02fc\u02fe\7\2\2\3\u02fd\u02f8\3\2\2\2\u02fd\u02fc")
        buf.write("\3\2\2\2\u02feC\3\2\2\2\u02ff\u0301\7}\2\2\u0300\u0302")
        buf.write("\5L\'\2\u0301\u0300\3\2\2\2\u0301\u0302\3\2\2\2\u0302")
        buf.write("\u0303\3\2\2\2\u0303\u0305\5N(\2\u0304\u0306\5H%\2\u0305")
        buf.write("\u0304\3\2\2\2\u0305\u0306\3\2\2\2\u0306\u0307\3\2\2\2")
        buf.write("\u0307\u0308\5F$\2\u0308\u0309\7l\2\2\u0309E\3\2\2\2\u030a")
        buf.write("\u030b\7l\2\2\u030b\u030c\7z\2\2\u030c\u030e\7z\2\2\u030d")
        buf.write("\u030f\7z\2\2\u030e\u030d\3\2\2\2\u030f\u0310\3\2\2\2")
        buf.write("\u0310\u030e\3\2\2\2\u0310\u0311\3\2\2\2\u0311G\3\2\2")
        buf.write("\2\u0312\u0313\7r\2\2\u0313\u0316\5J&\2\u0314\u0315\7")
        buf.write("~\2\2\u0315\u0317\5J&\2\u0316\u0314\3\2\2\2\u0316\u0317")
        buf.write("\3\2\2\2\u0317I\3\2\2\2\u0318\u031c\5\32\16\2\u0319\u031c")
        buf.write("\7\u0086\2\2\u031a\u031c\7\u0087\2\2\u031b\u0318\3\2\2")
        buf.write("\2\u031b\u0319\3\2\2\2\u031b\u031a\3\2\2\2\u031cK\3\2")
        buf.write("\2\2\u031d\u0322\5\32\16\2\u031e\u031f\7z\2\2\u031f\u0323")
        buf.write("\7q\2\2\u0320\u0321\7\u0084\2\2\u0321\u0323\7q\2\2\u0322")
        buf.write("\u031e\3\2\2\2\u0322\u0320\3\2\2\2\u0323M\3\2\2\2\u0324")
        buf.write("\u0325\5\32\16\2\u0325O\3\2\2\2\u0326\u0328\5j\66\2\u0327")
        buf.write("\u0326\3\2\2\2\u0328\u032b\3\2\2\2\u0329\u0327\3\2\2\2")
        buf.write("\u0329\u032a\3\2\2\2\u032a\u032c\3\2\2\2\u032b\u0329\3")
        buf.write("\2\2\2\u032c\u032e\5h\65\2\u032d\u032f\5R*\2\u032e\u032d")
        buf.write("\3\2\2\2\u032e\u032f\3\2\2\2\u032f\u0331\3\2\2\2\u0330")
        buf.write("\u0332\5f\64\2\u0331\u0330\3\2\2\2\u0331\u0332\3\2\2\2")
        buf.write("\u0332\u0334\3\2\2\2\u0333\u0335\5d\63\2\u0334\u0333\3")
        buf.write("\2\2\2\u0334\u0335\3\2\2\2\u0335\u033c\3\2\2\2\u0336\u0338")
        buf.write("\7l\2\2\u0337\u0336\3\2\2\2\u0338\u0339\3\2\2\2\u0339")
        buf.write("\u0337\3\2\2\2\u0339\u033a\3\2\2\2\u033a\u033d\3\2\2\2")
        buf.write("\u033b\u033d\7\2\2\3\u033c\u0337\3\2\2\2\u033c\u033b\3")
        buf.write("\2\2\2\u033dQ\3\2\2\2\u033e\u0340\7r\2\2\u033f\u0341\5")
        buf.write("T+\2\u0340\u033f\3\2\2\2\u0340\u0341\3\2\2\2\u0341\u034b")
        buf.write("\3\2\2\2\u0342\u0343\7r\2\2\u0343\u0345\5l\67\2\u0344")
        buf.write("\u0346\5V,\2\u0345\u0344\3\2\2\2\u0345\u0346\3\2\2\2\u0346")
        buf.write("\u034b\3\2\2\2\u0347\u0348\7r\2\2\u0348\u034b\5Z.\2\u0349")
        buf.write("\u034b\5\\/\2\u034a\u033e\3\2\2\2\u034a\u0342\3\2\2\2")
        buf.write("\u034a\u0347\3\2\2\2\u034a\u0349\3\2\2\2\u034bS\3\2\2")
        buf.write("\2\u034c\u034d\5*\26\2\u034dU\3\2\2\2\u034e\u0350\5X-")
        buf.write("\2\u034f\u034e\3\2\2\2\u034f\u0350\3\2\2\2\u0350\u0351")
        buf.write("\3\2\2\2\u0351\u0352\5*\26\2\u0352W\3\2\2\2\u0353\u0354")
        buf.write("\7|\2\2\u0354\u0355\7|\2\2\u0355Y\3\2\2\2\u0356\u0357")
        buf.write("\5\32\16\2\u0357[\3\2\2\2\u0358\u0359\5^\60\2\u0359\u035a")
        buf.write("\5`\61\2\u035a]\3\2\2\2\u035b\u035c\t\5\2\2\u035c_\3\2")
        buf.write("\2\2\u035d\u035e\7\u0091\2\2\u035ea\3\2\2\2\u035f\u0361")
        buf.write("\5\32\16\2\u0360\u035f\3\2\2\2\u0361\u0362\3\2\2\2\u0362")
        buf.write("\u0360\3\2\2\2\u0362\u0363\3\2\2\2\u0363\u0367\3\2\2\2")
        buf.write("\u0364\u0367\7\u0086\2\2\u0365\u0367\7\u0087\2\2\u0366")
        buf.write("\u0360\3\2\2\2\u0366\u0364\3\2\2\2\u0366\u0365\3\2\2\2")
        buf.write("\u0367c\3\2\2\2\u0368\u0369\7x\2\2\u0369\u036a\5b\62\2")
        buf.write("\u036ae\3\2\2\2\u036b\u036c\7~\2\2\u036c\u036d\5b\62\2")
        buf.write("\u036dg\3\2\2\2\u036e\u036f\5\32\16\2\u036fi\3\2\2\2\u0370")
        buf.write("\u0371\t\6\2\2\u0371k\3\2\2\2\u0372\u0385\5n8\2\u0373")
        buf.write("\u0385\5r:\2\u0374\u0385\5p9\2\u0375\u0385\5t;\2\u0376")
        buf.write("\u0385\5v<\2\u0377\u0385\5x=\2\u0378\u0385\5z>\2\u0379")
        buf.write("\u0385\5|?\2\u037a\u0385\5~@\2\u037b\u0385\5\u0086D\2")
        buf.write("\u037c\u0385\5\u0092J\2\u037d\u0385\5\u009cO\2\u037e\u0385")
        buf.write("\5\u00a2R\2\u037f\u0385\5\u00b6\\\2\u0380\u0385\5\u00a6")
        buf.write("T\2\u0381\u0385\5\u0080A\2\u0382\u0385\5\u0082B\2\u0383")
        buf.write("\u0385\5\u0084C\2\u0384\u0372\3\2\2\2\u0384\u0373\3\2")
        buf.write("\2\2\u0384\u0374\3\2\2\2\u0384\u0375\3\2\2\2\u0384\u0376")
        buf.write("\3\2\2\2\u0384\u0377\3\2\2\2\u0384\u0378\3\2\2\2\u0384")
        buf.write("\u0379\3\2\2\2\u0384\u037a\3\2\2\2\u0384\u037b\3\2\2\2")
        buf.write("\u0384\u037c\3\2\2\2\u0384\u037d\3\2\2\2\u0384\u037e\3")
        buf.write("\2\2\2\u0384\u037f\3\2\2\2\u0384\u0380\3\2\2\2\u0384\u0381")
        buf.write("\3\2\2\2\u0384\u0382\3\2\2\2\u0384\u0383\3\2\2\2\u0385")
        buf.write("m\3\2\2\2\u0386\u0387\7U\2\2\u0387o\3\2\2\2\u0388\u0389")
        buf.write("\7V\2\2\u0389q\3\2\2\2\u038a\u038b\7W\2\2\u038bs\3\2\2")
        buf.write("\2\u038c\u038d\7X\2\2\u038du\3\2\2\2\u038e\u038f\7Y\2")
        buf.write("\2\u038fw\3\2\2\2\u0390\u0391\7Z\2\2\u0391y\3\2\2\2\u0392")
        buf.write("\u0393\7[\2\2\u0393{\3\2\2\2\u0394\u0395\7\\\2\2\u0395")
        buf.write("}\3\2\2\2\u0396\u0397\7]\2\2\u0397\177\3\2\2\2\u0398\u0399")
        buf.write("\7_\2\2\u0399\u0081\3\2\2\2\u039a\u039b\7a\2\2\u039b\u0083")
        buf.write("\3\2\2\2\u039c\u039d\7b\2\2\u039d\u0085\3\2\2\2\u039e")
        buf.write("\u03a7\7d\2\2\u039f\u03a0\7t\2\2\u03a0\u03a3\5\u0088E")
        buf.write("\2\u03a1\u03a2\7{\2\2\u03a2\u03a4\5\u008aF\2\u03a3\u03a1")
        buf.write("\3\2\2\2\u03a3\u03a4\3\2\2\2\u03a4\u03a5\3\2\2\2\u03a5")
        buf.write("\u03a6\7u\2\2\u03a6\u03a8\3\2\2\2\u03a7\u039f\3\2\2\2")
        buf.write("\u03a7\u03a8\3\2\2\2\u03a8\u0087\3\2\2\2\u03a9\u03aa\t")
        buf.write("\7\2\2\u03aa\u0089\3\2\2\2\u03ab\u03ac\7k\2\2\u03ac\u03ad")
        buf.write("\7\177\2\2\u03ad\u03b2\5\u008cG\2\u03ae\u03af\7{\2\2\u03af")
        buf.write("\u03b1\5\u008cG\2\u03b0\u03ae\3\2\2\2\u03b1\u03b4\3\2")
        buf.write("\2\2\u03b2\u03b0\3\2\2\2\u03b2\u03b3\3\2\2\2\u03b3\u008b")
        buf.write("\3\2\2\2\u03b4\u03b2\3\2\2\2\u03b5\u03b7\5\u0090I\2\u03b6")
        buf.write("\u03b5\3\2\2\2\u03b6\u03b7\3\2\2\2\u03b7\u03b8\3\2\2\2")
        buf.write("\u03b8\u03b9\5\u008eH\2\u03b9\u008d\3\2\2\2\u03ba\u03be")
        buf.write("\5\32\16\2\u03bb\u03be\7\u0086\2\2\u03bc\u03be\7\u0087")
        buf.write("\2\2\u03bd\u03ba\3\2\2\2\u03bd\u03bb\3\2\2\2\u03bd\u03bc")
        buf.write("\3\2\2\2\u03be\u008f\3\2\2\2\u03bf\u03c0\5\32\16\2\u03c0")
        buf.write("\u03c1\7r\2\2\u03c1\u0091\3\2\2\2\u03c2\u03c7\7e\2\2\u03c3")
        buf.write("\u03c4\7t\2\2\u03c4\u03c5\5\u0094K\2\u03c5\u03c6\7u\2")
        buf.write("\2\u03c6\u03c8\3\2\2\2\u03c7\u03c3\3\2\2\2\u03c7\u03c8")
        buf.write("\3\2\2\2\u03c8\u0093\3\2\2\2\u03c9\u03ca\7k\2\2\u03ca")
        buf.write("\u03cb\7\177\2\2\u03cb\u03d0\5\u0096L\2\u03cc\u03cd\7")
        buf.write("{\2\2\u03cd\u03cf\5\u0096L\2\u03ce\u03cc\3\2\2\2\u03cf")
        buf.write("\u03d2\3\2\2\2\u03d0\u03ce\3\2\2\2\u03d0\u03d1\3\2\2\2")
        buf.write("\u03d1\u0095\3\2\2\2\u03d2\u03d0\3\2\2\2\u03d3\u03d5\5")
        buf.write("\u009aN\2\u03d4\u03d3\3\2\2\2\u03d4\u03d5\3\2\2\2\u03d5")
        buf.write("\u03d6\3\2\2\2\u03d6\u03d7\5\u0098M\2\u03d7\u0097\3\2")
        buf.write("\2\2\u03d8\u03dc\5\32\16\2\u03d9\u03dc\7\u0086\2\2\u03da")
        buf.write("\u03dc\7\u0087\2\2\u03db\u03d8\3\2\2\2\u03db\u03d9\3\2")
        buf.write("\2\2\u03db\u03da\3\2\2\2\u03dc\u0099\3\2\2\2\u03dd\u03de")
        buf.write("\7n\2\2\u03de\u03df\7r\2\2\u03df\u009b\3\2\2\2\u03e0\u03e1")
        buf.write("\7f\2\2\u03e1\u03e2\7t\2\2\u03e2\u03e3\5\u009eP\2\u03e3")
        buf.write("\u03e4\7u\2\2\u03e4\u009d\3\2\2\2\u03e5\u03ea\5\u00a0")
        buf.write("Q\2\u03e6\u03e7\7{\2\2\u03e7\u03e9\5\u00a0Q\2\u03e8\u03e6")
        buf.write("\3\2\2\2\u03e9\u03ec\3\2\2\2\u03ea\u03e8\3\2\2\2\u03ea")
        buf.write("\u03eb\3\2\2\2\u03eb\u009f\3\2\2\2\u03ec\u03ea\3\2\2\2")
        buf.write("\u03ed\u03ee\5\32\16\2\u03ee\u00a1\3\2\2\2\u03ef\u03f4")
        buf.write("\7g\2\2\u03f0\u03f1\7t\2\2\u03f1\u03f2\5\u00a4S\2\u03f2")
        buf.write("\u03f3\7u\2\2\u03f3\u03f5\3\2\2\2\u03f4\u03f0\3\2\2\2")
        buf.write("\u03f4\u03f5\3\2\2\2\u03f5\u00a3\3\2\2\2\u03f6\u03f7\7")
        buf.write(")\2\2\u03f7\u00a5\3\2\2\2\u03f8\u03fd\5\u00a8U\2\u03f9")
        buf.write("\u03fa\7t\2\2\u03fa\u03fb\5\u00aaV\2\u03fb\u03fc\7u\2")
        buf.write("\2\u03fc\u03fe\3\2\2\2\u03fd\u03f9\3\2\2\2\u03fd\u03fe")
        buf.write("\3\2\2\2\u03fe\u00a7\3\2\2\2\u03ff\u0400\t\b\2\2\u0400")
        buf.write("\u00a9\3\2\2\2\u0401\u0406\5\u00acW\2\u0402\u0403\7{\2")
        buf.write("\2\u0403\u0405\5\u00acW\2\u0404\u0402\3\2\2\2\u0405\u0408")
        buf.write("\3\2\2\2\u0406\u0404\3\2\2\2\u0406\u0407\3\2\2\2\u0407")
        buf.write("\u00ab\3\2\2\2\u0408\u0406\3\2\2\2\u0409\u040a\5\u00b0")
        buf.write("Y\2\u040a\u040b\5\u00aeX\2\u040b\u040c\5\u00b2Z\2\u040c")
        buf.write("\u00ad\3\2\2\2\u040d\u040e\7o\2\2\u040e\u00af\3\2\2\2")
        buf.write("\u040f\u0410\5\32\16\2\u0410\u0411\7\177\2\2\u0411\u00b1")
        buf.write("\3\2\2\2\u0412\u0414\5\u00b4[\2\u0413\u0412\3\2\2\2\u0414")
        buf.write("\u0417\3\2\2\2\u0415\u0413\3\2\2\2\u0415\u0416\3\2\2\2")
        buf.write("\u0416\u00b3\3\2\2\2\u0417\u0415\3\2\2\2\u0418\u0419\7")
        buf.write("\u0085\2\2\u0419\u041a\5\32\16\2\u041a\u00b5\3\2\2\2\u041b")
        buf.write("\u041c\5\u00b8]\2\u041c\u041f\7t\2\2\u041d\u0420\5\u00ba")
        buf.write("^\2\u041e\u0420\5\u00bc_\2\u041f\u041d\3\2\2\2\u041f\u041e")
        buf.write("\3\2\2\2\u0420\u0422\3\2\2\2\u0421\u0423\5\u00be`\2\u0422")
        buf.write("\u0421\3\2\2\2\u0422\u0423\3\2\2\2\u0423\u0424\3\2\2\2")
        buf.write("\u0424\u0425\7u\2\2\u0425\u00b7\3\2\2\2\u0426\u0427\t")
        buf.write("\t\2\2\u0427\u00b9\3\2\2\2\u0428\u0429\5\36\20\2\u0429")
        buf.write("\u00bb\3\2\2\2\u042a\u042b\5\34\17\2\u042b\u00bd\3\2\2")
        buf.write("\2\u042c\u042d\7z\2\2\u042d\u042e\7q\2\2\u042e\u042f\5")
        buf.write("\32\16\2\u042f\u00bf\3\2\2\2\u0430\u0440\5\u0116\u008c")
        buf.write("\2\u0431\u0440\5\u0112\u008a\2\u0432\u0440\5\u010e\u0088")
        buf.write("\2\u0433\u0440\5\u010c\u0087\2\u0434\u0440\5\u010a\u0086")
        buf.write("\2\u0435\u0440\5\u0108\u0085\2\u0436\u0440\5\u0106\u0084")
        buf.write("\2\u0437\u0440\5\u0104\u0083\2\u0438\u0440\5\u0102\u0082")
        buf.write("\2\u0439\u0440\5\u0100\u0081\2\u043a\u0440\5\u00fa~\2")
        buf.write("\u043b\u0440\5\u00caf\2\u043c\u0440\5\u00c6d\2\u043d\u0440")
        buf.write("\5\u00c2b\2\u043e\u0440\7l\2\2\u043f\u0430\3\2\2\2\u043f")
        buf.write("\u0431\3\2\2\2\u043f\u0432\3\2\2\2\u043f\u0433\3\2\2\2")
        buf.write("\u043f\u0434\3\2\2\2\u043f\u0435\3\2\2\2\u043f\u0436\3")
        buf.write("\2\2\2\u043f\u0437\3\2\2\2\u043f\u0438\3\2\2\2\u043f\u0439")
        buf.write("\3\2\2\2\u043f\u043a\3\2\2\2\u043f\u043b\3\2\2\2\u043f")
        buf.write("\u043c\3\2\2\2\u043f\u043d\3\2\2\2\u043f\u043e\3\2\2\2")
        buf.write("\u0440\u00c1\3\2\2\2\u0441\u0442\7#\2\2\u0442\u0443\7")
        buf.write("t\2\2\u0443\u0444\5\u00c4c\2\u0444\u0445\7u\2\2\u0445")
        buf.write("\u00c3\3\2\2\2\u0446\u0447\5\32\16\2\u0447\u00c5\3\2\2")
        buf.write("\2\u0448\u0449\7\"\2\2\u0449\u044a\7t\2\2\u044a\u044b")
        buf.write("\5\u00c8e\2\u044b\u044c\7u\2\2\u044c\u00c7\3\2\2\2\u044d")
        buf.write("\u0452\5\32\16\2\u044e\u044f\7{\2\2\u044f\u0451\5\32\16")
        buf.write("\2\u0450\u044e\3\2\2\2\u0451\u0454\3\2\2\2\u0452\u0450")
        buf.write("\3\2\2\2\u0452\u0453\3\2\2\2\u0453\u00c9\3\2\2\2\u0454")
        buf.write("\u0452\3\2\2\2\u0455\u0458\7!\2\2\u0456\u0457\7|\2\2\u0457")
        buf.write("\u0459\5\u00d0i\2\u0458\u0456\3\2\2\2\u0458\u0459\3\2")
        buf.write("\2\2\u0459\u045e\3\2\2\2\u045a\u045b\7t\2\2\u045b\u045c")
        buf.write("\5\u00ccg\2\u045c\u045d\7u\2\2\u045d\u045f\3\2\2\2\u045e")
        buf.write("\u045a\3\2\2\2\u045e\u045f\3\2\2\2\u045f\u00cb\3\2\2\2")
        buf.write("\u0460\u0466\5\u00ceh\2\u0461\u0465\5\u00f4{\2\u0462\u0465")
        buf.write("\7l\2\2\u0463\u0465\7{\2\2\u0464\u0461\3\2\2\2\u0464\u0462")
        buf.write("\3\2\2\2\u0464\u0463\3\2\2\2\u0465\u0468\3\2\2\2\u0466")
        buf.write("\u0464\3\2\2\2\u0466\u0467\3\2\2\2\u0467\u00cd\3\2\2\2")
        buf.write("\u0468\u0466\3\2\2\2\u0469\u0476\5\u00e0q\2\u046a\u0476")
        buf.write("\5\u00d2j\2\u046b\u0476\5\u00e4s\2\u046c\u0476\5\u00d4")
        buf.write("k\2\u046d\u0476\5\u00d6l\2\u046e\u0476\5\u00d8m\2\u046f")
        buf.write("\u0476\5\u00dan\2\u0470\u0476\5\u00dco\2\u0471\u0476\5")
        buf.write("\u00dep\2\u0472\u0476\5\u00ecw\2\u0473\u0476\7l\2\2\u0474")
        buf.write("\u0476\7{\2\2\u0475\u0469\3\2\2\2\u0475\u046a\3\2\2\2")
        buf.write("\u0475\u046b\3\2\2\2\u0475\u046c\3\2\2\2\u0475\u046d\3")
        buf.write("\2\2\2\u0475\u046e\3\2\2\2\u0475\u046f\3\2\2\2\u0475\u0470")
        buf.write("\3\2\2\2\u0475\u0471\3\2\2\2\u0475\u0472\3\2\2\2\u0475")
        buf.write("\u0473\3\2\2\2\u0475\u0474\3\2\2\2\u0476\u0479\3\2\2\2")
        buf.write("\u0477\u0475\3\2\2\2\u0477\u0478\3\2\2\2\u0478\u00cf\3")
        buf.write("\2\2\2\u0479\u0477\3\2\2\2\u047a\u047b\5\32\16\2\u047b")
        buf.write("\u00d1\3\2\2\2\u047c\u047d\7J\2\2\u047d\u047e\7r\2\2\u047e")
        buf.write("\u0482\7)\2\2\u047f\u0481\7l\2\2\u0480\u047f\3\2\2\2\u0481")
        buf.write("\u0484\3\2\2\2\u0482\u0480\3\2\2\2\u0482\u0483\3\2\2\2")
        buf.write("\u0483\u00d3\3\2\2\2\u0484\u0482\3\2\2\2\u0485\u0486\7")
        buf.write("G\2\2\u0486\u048a\5&\24\2\u0487\u0489\7l\2\2\u0488\u0487")
        buf.write("\3\2\2\2\u0489\u048c\3\2\2\2\u048a\u0488\3\2\2\2\u048a")
        buf.write("\u048b\3\2\2\2\u048b\u00d5\3\2\2\2\u048c\u048a\3\2\2\2")
        buf.write("\u048d\u048f\7F\2\2\u048e\u0490\7r\2\2\u048f\u048e\3\2")
        buf.write("\2\2\u048f\u0490\3\2\2\2\u0490\u0491\3\2\2\2\u0491\u0495")
        buf.write("\5&\24\2\u0492\u0494\7l\2\2\u0493\u0492\3\2\2\2\u0494")
        buf.write("\u0497\3\2\2\2\u0495\u0493\3\2\2\2\u0495\u0496\3\2\2\2")
        buf.write("\u0496\u00d7\3\2\2\2\u0497\u0495\3\2\2\2\u0498\u049a\7")
        buf.write("-\2\2\u0499\u049b\7r\2\2\u049a\u0499\3\2\2\2\u049a\u049b")
        buf.write("\3\2\2\2\u049b\u049c\3\2\2\2\u049c\u04a0\5&\24\2\u049d")
        buf.write("\u049f\7l\2\2\u049e\u049d\3\2\2\2\u049f\u04a2\3\2\2\2")
        buf.write("\u04a0\u049e\3\2\2\2\u04a0\u04a1\3\2\2\2\u04a1\u00d9\3")
        buf.write("\2\2\2\u04a2\u04a0\3\2\2\2\u04a3\u04a5\7,\2\2\u04a4\u04a6")
        buf.write("\7r\2\2\u04a5\u04a4\3\2\2\2\u04a5\u04a6\3\2\2\2\u04a6")
        buf.write("\u04a7\3\2\2\2\u04a7\u04ab\5&\24\2\u04a8\u04aa\7l\2\2")
        buf.write("\u04a9\u04a8\3\2\2\2\u04aa\u04ad\3\2\2\2\u04ab\u04a9\3")
        buf.write("\2\2\2\u04ab\u04ac\3\2\2\2\u04ac\u00db\3\2\2\2\u04ad\u04ab")
        buf.write("\3\2\2\2\u04ae\u04af\7N\2\2\u04af\u04b0\7r\2\2\u04b0\u04b4")
        buf.write("\5 \21\2\u04b1\u04b3\7l\2\2\u04b2\u04b1\3\2\2\2\u04b3")
        buf.write("\u04b6\3\2\2\2\u04b4\u04b2\3\2\2\2\u04b4\u04b5\3\2\2\2")
        buf.write("\u04b5\u00dd\3\2\2\2\u04b6\u04b4\3\2\2\2\u04b7\u04b8\7")
        buf.write("D\2\2\u04b8\u04b9\7r\2\2\u04b9\u04bd\5\32\16\2\u04ba\u04bc")
        buf.write("\7l\2\2\u04bb\u04ba\3\2\2\2\u04bc\u04bf\3\2\2\2\u04bd")
        buf.write("\u04bb\3\2\2\2\u04bd\u04be\3\2\2\2\u04be\u00df\3\2\2\2")
        buf.write("\u04bf\u04bd\3\2\2\2\u04c0\u04c1\7R\2\2\u04c1\u04c2\7")
        buf.write("r\2\2\u04c2\u04c4\5 \21\2\u04c3\u04c5\5\u00e2r\2\u04c4")
        buf.write("\u04c3\3\2\2\2\u04c4\u04c5\3\2\2\2\u04c5\u04c9\3\2\2\2")
        buf.write("\u04c6\u04c8\7l\2\2\u04c7\u04c6\3\2\2\2\u04c8\u04cb\3")
        buf.write("\2\2\2\u04c9\u04c7\3\2\2\2\u04c9\u04ca\3\2\2\2\u04ca\u00e1")
        buf.write("\3\2\2\2\u04cb\u04c9\3\2\2\2\u04cc\u04cd\5$\23\2\u04cd")
        buf.write("\u00e3\3\2\2\2\u04ce\u04cf\7H\2\2\u04cf\u04d0\7t\2\2\u04d0")
        buf.write("\u04d5\5\u00e6t\2\u04d1\u04d2\7{\2\2\u04d2\u04d4\5\u00e6")
        buf.write("t\2\u04d3\u04d1\3\2\2\2\u04d4\u04d7\3\2\2\2\u04d5\u04d3")
        buf.write("\3\2\2\2\u04d5\u04d6\3\2\2\2\u04d6\u04d8\3\2\2\2\u04d7")
        buf.write("\u04d5\3\2\2\2\u04d8\u04d9\7u\2\2\u04d9\u00e5\3\2\2\2")
        buf.write("\u04da\u04de\7A\2\2\u04db\u04dc\7r\2\2\u04dc\u04df\5\u00e8")
        buf.write("u\2\u04dd\u04df\5\u00eav\2\u04de\u04db\3\2\2\2\u04de\u04dd")
        buf.write("\3\2\2\2\u04de\u04df\3\2\2\2\u04df\u00e7\3\2\2\2\u04e0")
        buf.write("\u04e1\5\36\20\2\u04e1\u00e9\3\2\2\2\u04e2\u04e3\5\34")
        buf.write("\17\2\u04e3\u00eb\3\2\2\2\u04e4\u04e5\7E\2\2\u04e5\u04e6")
        buf.write("\7r\2\2\u04e6\u04ea\5\u00eex\2\u04e7\u04e9\7l\2\2\u04e8")
        buf.write("\u04e7\3\2\2\2\u04e9\u04ec\3\2\2\2\u04ea\u04e8\3\2\2\2")
        buf.write("\u04ea\u04eb\3\2\2\2\u04eb\u00ed\3\2\2\2\u04ec\u04ea\3")
        buf.write("\2\2\2\u04ed\u04ee\7I\2\2\u04ee\u04f1\5\u00f0y\2\u04ef")
        buf.write("\u04f0\7T\2\2\u04f0\u04f2\5\u00f2z\2\u04f1\u04ef\3\2\2")
        buf.write("\2\u04f1\u04f2\3\2\2\2\u04f2\u00ef\3\2\2\2\u04f3\u04f4")
        buf.write("\5\32\16\2\u04f4\u00f1\3\2\2\2\u04f5\u04f6\5\32\16\2\u04f6")
        buf.write("\u00f3\3\2\2\2\u04f7\u04f8\7B\2\2\u04f8\u04fc\7r\2\2\u04f9")
        buf.write("\u04fd\5\u00f6|\2\u04fa\u04fd\7{\2\2\u04fb\u04fd\7l\2")
        buf.write("\2\u04fc\u04f9\3\2\2\2\u04fc\u04fa\3\2\2\2\u04fc\u04fb")
        buf.write("\3\2\2\2\u04fd\u04fe\3\2\2\2\u04fe\u04fc\3\2\2\2\u04fe")
        buf.write("\u04ff\3\2\2\2\u04ff\u00f5\3\2\2\2\u0500\u0501\5\u00f8")
        buf.write("}\2\u0501\u0502\7t\2\2\u0502\u0503\5\u00ccg\2\u0503\u0504")
        buf.write("\7u\2\2\u0504\u00f7\3\2\2\2\u0505\u0506\5\32\16\2\u0506")
        buf.write("\u00f9\3\2\2\2\u0507\u0516\7 \2\2\u0508\u0512\7t\2\2\u0509")
        buf.write("\u0513\5\u00fc\177\2\u050a\u050f\5\u00fe\u0080\2\u050b")
        buf.write("\u050c\7{\2\2\u050c\u050e\5\u00fe\u0080\2\u050d\u050b")
        buf.write("\3\2\2\2\u050e\u0511\3\2\2\2\u050f\u050d\3\2\2\2\u050f")
        buf.write("\u0510\3\2\2\2\u0510\u0513\3\2\2\2\u0511\u050f\3\2\2\2")
        buf.write("\u0512\u0509\3\2\2\2\u0512\u050a\3\2\2\2\u0513\u0514\3")
        buf.write("\2\2\2\u0514\u0515\7u\2\2\u0515\u0517\3\2\2\2\u0516\u0508")
        buf.write("\3\2\2\2\u0516\u0517\3\2\2\2\u0517\u00fb\3\2\2\2\u0518")
        buf.write("\u0519\7\u0083\2\2\u0519\u00fd\3\2\2\2\u051a\u051b\5\32")
        buf.write("\16\2\u051b\u00ff\3\2\2\2\u051c\u051d\7\37\2\2\u051d\u051e")
        buf.write("\5&\24\2\u051e\u0101\3\2\2\2\u051f\u0520\7\36\2\2\u0520")
        buf.write("\u0521\5&\24\2\u0521\u0103\3\2\2\2\u0522\u0523\7\35\2")
        buf.write("\2\u0523\u0524\5&\24\2\u0524\u0105\3\2\2\2\u0525\u0526")
        buf.write("\7\34\2\2\u0526\u0527\5&\24\2\u0527\u0107\3\2\2\2\u0528")
        buf.write("\u0529\7\33\2\2\u0529\u052a\5&\24\2\u052a\u0109\3\2\2")
        buf.write("\2\u052b\u052c\7\32\2\2\u052c\u052d\5&\24\2\u052d\u010b")
        buf.write("\3\2\2\2\u052e\u052f\7\31\2\2\u052f\u0530\7t\2\2\u0530")
        buf.write("\u0531\5\34\17\2\u0531\u0532\7u\2\2\u0532\u010d\3\2\2")
        buf.write("\2\u0533\u0534\7\30\2\2\u0534\u0535\7t\2\2\u0535\u0536")
        buf.write("\5\u0110\u0089\2\u0536\u0537\7u\2\2\u0537\u010f\3\2\2")
        buf.write("\2\u0538\u0539\5\32\16\2\u0539\u0111\3\2\2\2\u053a\u053f")
        buf.write("\7\27\2\2\u053b\u053c\7t\2\2\u053c\u053d\5\u0114\u008b")
        buf.write("\2\u053d\u053e\7u\2\2\u053e\u0540\3\2\2\2\u053f\u053b")
        buf.write("\3\2\2\2\u053f\u0540\3\2\2\2\u0540\u0113\3\2\2\2\u0541")
        buf.write("\u0542\7=\2\2\u0542\u0115\3\2\2\2\u0543\u055d\7&\2\2\u0544")
        buf.write("\u0553\7t\2\2\u0545\u0552\5\u0134\u009b\2\u0546\u0552")
        buf.write("\5\u0136\u009c\2\u0547\u0552\5\u0138\u009d\2\u0548\u0552")
        buf.write("\5\u013a\u009e\2\u0549\u0552\5\u013c\u009f\2\u054a\u0552")
        buf.write("\5\u013e\u00a0\2\u054b\u0552\5\u012c\u0097\2\u054c\u0552")
        buf.write("\5\u0120\u0091\2\u054d\u0552\5\u011a\u008e\2\u054e\u0552")
        buf.write("\5\u0118\u008d\2\u054f\u0552\7l\2\2\u0550\u0552\7{\2\2")
        buf.write("\u0551\u0545\3\2\2\2\u0551\u0546\3\2\2\2\u0551\u0547\3")
        buf.write("\2\2\2\u0551\u0548\3\2\2\2\u0551\u0549\3\2\2\2\u0551\u054a")
        buf.write("\3\2\2\2\u0551\u054b\3\2\2\2\u0551\u054c\3\2\2\2\u0551")
        buf.write("\u054d\3\2\2\2\u0551\u054e\3\2\2\2\u0551\u054f\3\2\2\2")
        buf.write("\u0551\u0550\3\2\2\2\u0552\u0555\3\2\2\2\u0553\u0551\3")
        buf.write("\2\2\2\u0553\u0554\3\2\2\2\u0554\u0559\3\2\2\2\u0555\u0553")
        buf.write("\3\2\2\2\u0556\u0558\7l\2\2\u0557\u0556\3\2\2\2\u0558")
        buf.write("\u055b\3\2\2\2\u0559\u0557\3\2\2\2\u0559\u055a\3\2\2\2")
        buf.write("\u055a\u055c\3\2\2\2\u055b\u0559\3\2\2\2\u055c\u055e\7")
        buf.write("u\2\2\u055d\u0544\3\2\2\2\u055d\u055e\3\2\2\2\u055e\u0562")
        buf.write("\3\2\2\2\u055f\u0561\7l\2\2\u0560\u055f\3\2\2\2\u0561")
        buf.write("\u0564\3\2\2\2\u0562\u0560\3\2\2\2\u0562\u0563\3\2\2\2")
        buf.write("\u0563\u0117\3\2\2\2\u0564\u0562\3\2\2\2\u0565\u0566\7")
        buf.write("?\2\2\u0566\u056a\7r\2\2\u0567\u0569\7l\2\2\u0568\u0567")
        buf.write("\3\2\2\2\u0569\u056c\3\2\2\2\u056a\u0568\3\2\2\2\u056a")
        buf.write("\u056b\3\2\2\2\u056b\u056d\3\2\2\2\u056c\u056a\3\2\2\2")
        buf.write("\u056d\u0578\5\u011e\u0090\2\u056e\u0572\7{\2\2\u056f")
        buf.write("\u0571\7l\2\2\u0570\u056f\3\2\2\2\u0571\u0574\3\2\2\2")
        buf.write("\u0572\u0570\3\2\2\2\u0572\u0573\3\2\2\2\u0573\u0575\3")
        buf.write("\2\2\2\u0574\u0572\3\2\2\2\u0575\u0577\5\u011e\u0090\2")
        buf.write("\u0576\u056e\3\2\2\2\u0577\u057a\3\2\2\2\u0578\u0576\3")
        buf.write("\2\2\2\u0578\u0579\3\2\2\2\u0579\u0119\3\2\2\2\u057a\u0578")
        buf.write("\3\2\2\2\u057b\u057c\7>\2\2\u057c\u057d\7r\2\2\u057d\u0582")
        buf.write("\5\u011c\u008f\2\u057e\u057f\7{\2\2\u057f\u0581\5\u011c")
        buf.write("\u008f\2\u0580\u057e\3\2\2\2\u0581\u0584\3\2\2\2\u0582")
        buf.write("\u0580\3\2\2\2\u0582\u0583\3\2\2\2\u0583\u011b\3\2\2\2")
        buf.write("\u0584\u0582\3\2\2\2\u0585\u0586\t\4\2\2\u0586\u011d\3")
        buf.write("\2\2\2\u0587\u0588\t\4\2\2\u0588\u011f\3\2\2\2\u0589\u058a")
        buf.write("\7B\2\2\u058a\u058b\7r\2\2\u058b\u0590\5\u0122\u0092\2")
        buf.write("\u058c\u058d\7{\2\2\u058d\u058f\5\u0122\u0092\2\u058e")
        buf.write("\u058c\3\2\2\2\u058f\u0592\3\2\2\2\u0590\u058e\3\2\2\2")
        buf.write("\u0590\u0591\3\2\2\2\u0591\u0121\3\2\2\2\u0592\u0590\3")
        buf.write("\2\2\2\u0593\u05a0\5\u0124\u0093\2\u0594\u059c\7t\2\2")
        buf.write("\u0595\u059b\5\u0126\u0094\2\u0596\u059b\5\u0128\u0095")
        buf.write("\2\u0597\u059b\5\u012a\u0096\2\u0598\u059b\7l\2\2\u0599")
        buf.write("\u059b\7{\2\2\u059a\u0595\3\2\2\2\u059a\u0596\3\2\2\2")
        buf.write("\u059a\u0597\3\2\2\2\u059a\u0598\3\2\2\2\u059a\u0599\3")
        buf.write("\2\2\2\u059b\u059e\3\2\2\2\u059c\u059a\3\2\2\2\u059c\u059d")
        buf.write("\3\2\2\2\u059d\u059f\3\2\2\2\u059e\u059c\3\2\2\2\u059f")
        buf.write("\u05a1\7u\2\2\u05a0\u0594\3\2\2\2\u05a0\u05a1\3\2\2\2")
        buf.write("\u05a1\u0123\3\2\2\2\u05a2\u05a3\5\32\16\2\u05a3\u0125")
        buf.write("\3\2\2\2\u05a4\u05a5\7C\2\2\u05a5\u05a6\7r\2\2\u05a6\u05a7")
        buf.write("\7@\2\2\u05a7\u0127\3\2\2\2\u05a8\u05a9\7K\2\2\u05a9\u05aa")
        buf.write("\7r\2\2\u05aa\u05ab\7n\2\2\u05ab\u0129\3\2\2\2\u05ac\u05ad")
        buf.write("\7R\2\2\u05ad\u05ae\7r\2\2\u05ae\u05af\5 \21\2\u05af\u012b")
        buf.write("\3\2\2\2\u05b0\u05b1\7L\2\2\u05b1\u05b2\7r\2\2\u05b2\u05b7")
        buf.write("\5\u012e\u0098\2\u05b3\u05b4\7{\2\2\u05b4\u05b6\5\u012e")
        buf.write("\u0098\2\u05b5\u05b3\3\2\2\2\u05b6\u05b9\3\2\2\2\u05b7")
        buf.write("\u05b5\3\2\2\2\u05b7\u05b8\3\2\2\2\u05b8\u012d\3\2\2\2")
        buf.write("\u05b9\u05b7\3\2\2\2\u05ba\u05bc\5\u0130\u0099\2\u05bb")
        buf.write("\u05bd\5\u0132\u009a\2\u05bc\u05bb\3\2\2\2\u05bc\u05bd")
        buf.write("\3\2\2\2\u05bd\u05be\3\2\2\2\u05be\u05bf\7t\2\2\u05bf")
        buf.write("\u05c0\5 \21\2\u05c0\u05c1\7u\2\2\u05c1\u012f\3\2\2\2")
        buf.write("\u05c2\u05c3\5\32\16\2\u05c3\u0131\3\2\2\2\u05c4\u05c5")
        buf.write("\t\4\2\2\u05c5\u0133\3\2\2\2\u05c6\u05c7\7M\2\2\u05c7")
        buf.write("\u05c8\7r\2\2\u05c8\u05cc\5 \21\2\u05c9\u05cb\7l\2\2\u05ca")
        buf.write("\u05c9\3\2\2\2\u05cb\u05ce\3\2\2\2\u05cc\u05ca\3\2\2\2")
        buf.write("\u05cc\u05cd\3\2\2\2\u05cd\u0135\3\2\2\2\u05ce\u05cc\3")
        buf.write("\2\2\2\u05cf\u05d0\7N\2\2\u05d0\u05d1\7r\2\2\u05d1\u05d5")
        buf.write("\5 \21\2\u05d2\u05d4\7l\2\2\u05d3\u05d2\3\2\2\2\u05d4")
        buf.write("\u05d7\3\2\2\2\u05d5\u05d3\3\2\2\2\u05d5\u05d6\3\2\2\2")
        buf.write("\u05d6\u0137\3\2\2\2\u05d7\u05d5\3\2\2\2\u05d8\u05d9\7")
        buf.write("O\2\2\u05d9\u05da\7r\2\2\u05da\u05de\5 \21\2\u05db\u05dd")
        buf.write("\7l\2\2\u05dc\u05db\3\2\2\2\u05dd\u05e0\3\2\2\2\u05de")
        buf.write("\u05dc\3\2\2\2\u05de\u05df\3\2\2\2\u05df\u0139\3\2\2\2")
        buf.write("\u05e0\u05de\3\2\2\2\u05e1\u05e2\7P\2\2\u05e2\u05e3\7")
        buf.write("r\2\2\u05e3\u05e7\5 \21\2\u05e4\u05e6\7l\2\2\u05e5\u05e4")
        buf.write("\3\2\2\2\u05e6\u05e9\3\2\2\2\u05e7\u05e5\3\2\2\2\u05e7")
        buf.write("\u05e8\3\2\2\2\u05e8\u013b\3\2\2\2\u05e9\u05e7\3\2\2\2")
        buf.write("\u05ea\u05eb\7Q\2\2\u05eb\u05ec\7r\2\2\u05ec\u05f0\5 ")
        buf.write("\21\2\u05ed\u05ef\7l\2\2\u05ee\u05ed\3\2\2\2\u05ef\u05f2")
        buf.write("\3\2\2\2\u05f0\u05ee\3\2\2\2\u05f0\u05f1\3\2\2\2\u05f1")
        buf.write("\u013d\3\2\2\2\u05f2\u05f0\3\2\2\2\u05f3\u05f4\7R\2\2")
        buf.write("\u05f4\u05f5\7r\2\2\u05f5\u05f9\5 \21\2\u05f6\u05f8\7")
        buf.write("l\2\2\u05f7\u05f6\3\2\2\2\u05f8\u05fb\3\2\2\2\u05f9\u05f7")
        buf.write("\3\2\2\2\u05f9\u05fa\3\2\2\2\u05fa\u013f\3\2\2\2\u05fb")
        buf.write("\u05f9\3\2\2\2\u05fc\u0600\5\u0142\u00a2\2\u05fd\u05ff")
        buf.write("\7l\2\2\u05fe\u05fd\3\2\2\2\u05ff\u0602\3\2\2\2\u0600")
        buf.write("\u05fe\3\2\2\2\u0600\u0601\3\2\2\2\u0601\u0603\3\2\2\2")
        buf.write("\u0602\u0600\3\2\2\2\u0603\u0607\5\u015c\u00af\2\u0604")
        buf.write("\u0606\7l\2\2\u0605\u0604\3\2\2\2\u0606\u0609\3\2\2\2")
        buf.write("\u0607\u0605\3\2\2\2\u0607\u0608\3\2\2\2\u0608\u0141\3")
        buf.write("\2\2\2\u0609\u0607\3\2\2\2\u060a\u060c\7v\2\2\u060b\u060d")
        buf.write("\5\u0144\u00a3\2\u060c\u060b\3\2\2\2\u060c\u060d\3\2\2")
        buf.write("\2\u060d\u060e\3\2\2\2\u060e\u0610\5\u015a\u00ae\2\u060f")
        buf.write("\u0611\5\u0146\u00a4\2\u0610\u060f\3\2\2\2\u0610\u0611")
        buf.write("\3\2\2\2\u0611\u061a\3\2\2\2\u0612\u0614\7r\2\2\u0613")
        buf.write("\u0615\5\u0150\u00a9\2\u0614\u0613\3\2\2\2\u0614\u0615")
        buf.write("\3\2\2\2\u0615\u0618\3\2\2\2\u0616\u0617\7r\2\2\u0617")
        buf.write("\u0619\5\u014a\u00a6\2\u0618\u0616\3\2\2\2\u0618\u0619")
        buf.write("\3\2\2\2\u0619\u061b\3\2\2\2\u061a\u0612\3\2\2\2\u061a")
        buf.write("\u061b\3\2\2\2\u061b\u061c\3\2\2\2\u061c\u061e\7w\2\2")
        buf.write("\u061d\u061f\7l\2\2\u061e\u061d\3\2\2\2\u061e\u061f\3")
        buf.write("\2\2\2\u061f\u0143\3\2\2\2\u0620\u0621\5\32\16\2\u0621")
        buf.write("\u0622\7|\2\2\u0622\u0624\3\2\2\2\u0623\u0620\3\2\2\2")
        buf.write("\u0623\u0624\3\2\2\2\u0624\u0625\3\2\2\2\u0625\u0626\5")
        buf.write("\32\16\2\u0626\u0627\t\n\2\2\u0627\u0628\7q\2\2\u0628")
        buf.write("\u0145\3\2\2\2\u0629\u062a\7T\2\2\u062a\u062b\5\u0148")
        buf.write("\u00a5\2\u062b\u0147\3\2\2\2\u062c\u062d\5\32\16\2\u062d")
        buf.write("\u0149\3\2\2\2\u062e\u0631\5\u014c\u00a7\2\u062f\u0631")
        buf.write("\5&\24\2\u0630\u062e\3\2\2\2\u0630\u062f\3\2\2\2\u0631")
        buf.write("\u014b\3\2\2\2\u0632\u0637\5\u014e\u00a8\2\u0633\u0634")
        buf.write("\7~\2\2\u0634\u0636\5\u014e\u00a8\2\u0635\u0633\3\2\2")
        buf.write("\2\u0636\u0639\3\2\2\2\u0637\u0635\3\2\2\2\u0637\u0638")
        buf.write("\3\2\2\2\u0638\u014d\3\2\2\2\u0639\u0637\3\2\2\2\u063a")
        buf.write("\u0640\5\32\16\2\u063b\u0640\7n\2\2\u063c\u0640\7z\2\2")
        buf.write("\u063d\u0640\7y\2\2\u063e\u0640\7|\2\2\u063f\u063a\3\2")
        buf.write("\2\2\u063f\u063b\3\2\2\2\u063f\u063c\3\2\2\2\u063f\u063d")
        buf.write("\3\2\2\2\u063f\u063e\3\2\2\2\u0640\u0641\3\2\2\2\u0641")
        buf.write("\u063f\3\2\2\2\u0641\u0642\3\2\2\2\u0642\u014f\3\2\2\2")
        buf.write("\u0643\u0645\t\13\2\2\u0644\u0643\3\2\2\2\u0644\u0645")
        buf.write("\3\2\2\2\u0645\u0646\3\2\2\2\u0646\u0647\5\u0158\u00ad")
        buf.write("\2\u0647\u0151\3\2\2\2\u0648\u064c\5\32\16\2\u0649\u064c")
        buf.write("\7z\2\2\u064a\u064c\7n\2\2\u064b\u0648\3\2\2\2\u064b\u0649")
        buf.write("\3\2\2\2\u064b\u064a\3\2\2\2\u064c\u064d\3\2\2\2\u064d")
        buf.write("\u064b\3\2\2\2\u064d\u064e\3\2\2\2\u064e\u0153\3\2\2\2")
        buf.write("\u064f\u0650\7p\2\2\u0650\u0651\5\32\16\2\u0651\u0652")
        buf.write("\7q\2\2\u0652\u0155\3\2\2\2\u0653\u0656\5\u0152\u00aa")
        buf.write("\2\u0654\u0656\5\u0154\u00ab\2\u0655\u0653\3\2\2\2\u0655")
        buf.write("\u0654\3\2\2\2\u0656\u0157\3\2\2\2\u0657\u0662\7~\2\2")
        buf.write("\u0658\u0659\7~\2\2\u0659\u065b\5\u0156\u00ac\2\u065a")
        buf.write("\u0658\3\2\2\2\u065b\u065c\3\2\2\2\u065c\u065a\3\2\2\2")
        buf.write("\u065c\u065d\3\2\2\2\u065d\u065f\3\2\2\2\u065e\u0660\7")
        buf.write("~\2\2\u065f\u065e\3\2\2\2\u065f\u0660\3\2\2\2\u0660\u0662")
        buf.write("\3\2\2\2\u0661\u0657\3\2\2\2\u0661\u065a\3\2\2\2\u0662")
        buf.write("\u0159\3\2\2\2\u0663\u0664\5\32\16\2\u0664\u015b\3\2\2")
        buf.write("\2\u0665\u0667\5\u0160\u00b1\2\u0666\u0665\3\2\2\2\u0667")
        buf.write("\u066a\3\2\2\2\u0668\u0666\3\2\2\2\u0668\u0669\3\2\2\2")
        buf.write("\u0669\u066e\3\2\2\2\u066a\u0668\3\2\2\2\u066b\u066d\5")
        buf.write("\u0166\u00b4\2\u066c\u066b\3\2\2\2\u066d\u0670\3\2\2\2")
        buf.write("\u066e\u066c\3\2\2\2\u066e\u066f\3\2\2\2\u066f\u0672\3")
        buf.write("\2\2\2\u0670\u066e\3\2\2\2\u0671\u0673\5\u015e\u00b0\2")
        buf.write("\u0672\u0671\3\2\2\2\u0672\u0673\3\2\2\2\u0673\u0677\3")
        buf.write("\2\2\2\u0674\u0676\7l\2\2\u0675\u0674\3\2\2\2\u0676\u0679")
        buf.write("\3\2\2\2\u0677\u0675\3\2\2\2\u0677\u0678\3\2\2\2\u0678")
        buf.write("\u067d\3\2\2\2\u0679\u0677\3\2\2\2\u067a\u067c\5\u016c")
        buf.write("\u00b7\2\u067b\u067a\3\2\2\2\u067c\u067f\3\2\2\2\u067d")
        buf.write("\u067b\3\2\2\2\u067d\u067e\3\2\2\2\u067e\u015d\3\2\2\2")
        buf.write("\u067f\u067d\3\2\2\2\u0680\u0681\5&\24\2\u0681\u015f\3")
        buf.write("\2\2\2\u0682\u0683\5\u0162\u00b2\2\u0683\u0684\7\u008d")
        buf.write("\2\2\u0684\u068b\5\u0164\u00b3\2\u0685\u0687\7l\2\2\u0686")
        buf.write("\u0685\3\2\2\2\u0687\u0688\3\2\2\2\u0688\u0686\3\2\2\2")
        buf.write("\u0688\u0689\3\2\2\2\u0689\u068c\3\2\2\2\u068a\u068c\7")
        buf.write("\2\2\3\u068b\u0686\3\2\2\2\u068b\u068a\3\2\2\2\u068c\u0161")
        buf.write("\3\2\2\2\u068d\u068e\5\32\16\2\u068e\u0163\3\2\2\2\u068f")
        buf.write("\u0690\7\u0091\2\2\u0690\u0165\3\2\2\2\u0691\u0692\5\u0168")
        buf.write("\u00b5\2\u0692\u0694\7t\2\2\u0693\u0695\5\u016a\u00b6")
        buf.write("\2\u0694\u0693\3\2\2\2\u0694\u0695\3\2\2\2\u0695\u0696")
        buf.write("\3\2\2\2\u0696\u0698\7u\2\2\u0697\u0699\5*\26\2\u0698")
        buf.write("\u0697\3\2\2\2\u0698\u0699\3\2\2\2\u0699\u06a0\3\2\2\2")
        buf.write("\u069a\u069c\7l\2\2\u069b\u069a\3\2\2\2\u069c\u069d\3")
        buf.write("\2\2\2\u069d\u069b\3\2\2\2\u069d\u069e\3\2\2\2\u069e\u06a1")
        buf.write("\3\2\2\2\u069f\u06a1\7\2\2\3\u06a0\u069b\3\2\2\2\u06a0")
        buf.write("\u069f\3\2\2\2\u06a1\u0167\3\2\2\2\u06a2\u06a3\5\32\16")
        buf.write("\2\u06a3\u0169\3\2\2\2\u06a4\u06a9\5\32\16\2\u06a5\u06a6")
        buf.write("\7{\2\2\u06a6\u06a8\5\32\16\2\u06a7\u06a5\3\2\2\2\u06a8")
        buf.write("\u06ab\3\2\2\2\u06a9\u06a7\3\2\2\2\u06a9\u06aa\3\2\2\2")
        buf.write("\u06aa\u016b\3\2\2\2\u06ab\u06a9\3\2\2\2\u06ac\u06bd\5")
        buf.write("\u01f4\u00fb\2\u06ad\u06bd\5\u016e\u00b8\2\u06ae\u06bd")
        buf.write("\5\u01f0\u00f9\2\u06af\u06bd\5\u01e4\u00f3\2\u06b0\u06bd")
        buf.write("\5\u01e2\u00f2\2\u06b1\u06bd\5\u01c8\u00e5\2\u06b2\u06bd")
        buf.write("\5\u0182\u00c2\2\u06b3\u06bd\5\u01c6\u00e4\2\u06b4\u06bd")
        buf.write("\5\u01c4\u00e3\2\u06b5\u06bd\5\u01c2\u00e2\2\u06b6\u06bd")
        buf.write("\5\u0180\u00c1\2\u06b7\u06bd\5\u017e\u00c0\2\u06b8\u06bd")
        buf.write("\5\u017a\u00be\2\u06b9\u06bd\5\u0178\u00bd\2\u06ba\u06bd")
        buf.write("\5\u0174\u00bb\2\u06bb\u06bd\7l\2\2\u06bc\u06ac\3\2\2")
        buf.write("\2\u06bc\u06ad\3\2\2\2\u06bc\u06ae\3\2\2\2\u06bc\u06af")
        buf.write("\3\2\2\2\u06bc\u06b0\3\2\2\2\u06bc\u06b1\3\2\2\2\u06bc")
        buf.write("\u06b2\3\2\2\2\u06bc\u06b3\3\2\2\2\u06bc\u06b4\3\2\2\2")
        buf.write("\u06bc\u06b5\3\2\2\2\u06bc\u06b6\3\2\2\2\u06bc\u06b7\3")
        buf.write("\2\2\2\u06bc\u06b8\3\2\2\2\u06bc\u06b9\3\2\2\2\u06bc\u06ba")
        buf.write("\3\2\2\2\u06bc\u06bb\3\2\2\2\u06bd\u016d\3\2\2\2\u06be")
        buf.write("\u06c1\5\u0170\u00b9\2\u06bf\u06c0\7|\2\2\u06c0\u06c2")
        buf.write("\5\u0172\u00ba\2\u06c1\u06bf\3\2\2\2\u06c1\u06c2\3\2\2")
        buf.write("\2\u06c2\u06c3\3\2\2\2\u06c3\u06c4\5*\26\2\u06c4\u016f")
        buf.write("\3\2\2\2\u06c5\u06c6\t\f\2\2\u06c6\u0171\3\2\2\2\u06c7")
        buf.write("\u06c8\5\32\16\2\u06c8\u0173\3\2\2\2\u06c9\u06cc\7\22")
        buf.write("\2\2\u06ca\u06cb\7|\2\2\u06cb\u06cd\5\u0176\u00bc\2\u06cc")
        buf.write("\u06ca\3\2\2\2\u06cc\u06cd\3\2\2\2\u06cd\u06ce\3\2\2\2")
        buf.write("\u06ce\u06cf\5*\26\2\u06cf\u0175\3\2\2\2\u06d0\u06d1\5")
        buf.write("\32\16\2\u06d1\u0177\3\2\2\2\u06d2\u06d4\7\21\2\2\u06d3")
        buf.write("\u06d5\5*\26\2\u06d4\u06d3\3\2\2\2\u06d4\u06d5\3\2\2\2")
        buf.write("\u06d5\u0179\3\2\2\2\u06d6\u06d7\7\20\2\2\u06d7\u06d8")
        buf.write("\7t\2\2\u06d8\u06d9\5\u017c\u00bf\2\u06d9\u06da\7u\2\2")
        buf.write("\u06da\u017b\3\2\2\2\u06db\u06dc\7n\2\2\u06dc\u017d\3")
        buf.write("\2\2\2\u06dd\u06df\7\17\2\2\u06de\u06e0\5*\26\2\u06df")
        buf.write("\u06de\3\2\2\2\u06df\u06e0\3\2\2\2\u06e0\u017f\3\2\2\2")
        buf.write("\u06e1\u06e2\7\r\2\2\u06e2\u06e3\5\u0184\u00c3\2\u06e3")
        buf.write("\u0181\3\2\2\2\u06e4\u06e5\7\t\2\2\u06e5\u06e6\5\u0184")
        buf.write("\u00c3\2\u06e6\u0183\3\2\2\2\u06e7\u06e8\7|\2\2\u06e8")
        buf.write("\u06ea\5\u0188\u00c5\2\u06e9\u06e7\3\2\2\2\u06e9\u06ea")
        buf.write("\3\2\2\2\u06ea\u06eb\3\2\2\2\u06eb\u06ef\7t\2\2\u06ec")
        buf.write("\u06ee\7l\2\2\u06ed\u06ec\3\2\2\2\u06ee\u06f1\3\2\2\2")
        buf.write("\u06ef\u06ed\3\2\2\2\u06ef\u06f0\3\2\2\2\u06f0\u06f2\3")
        buf.write("\2\2\2\u06f1\u06ef\3\2\2\2\u06f2\u06f4\5\u0192\u00ca\2")
        buf.write("\u06f3\u06f5\5\u0194\u00cb\2\u06f4\u06f3\3\2\2\2\u06f4")
        buf.write("\u06f5\3\2\2\2\u06f5\u0705\3\2\2\2\u06f6\u0704\5\u0196")
        buf.write("\u00cc\2\u06f7\u0704\5\u01aa\u00d6\2\u06f8\u0704\5\u01b0")
        buf.write("\u00d9\2\u06f9\u0704\5\u01ba\u00de\2\u06fa\u0704\5\u01a8")
        buf.write("\u00d5\2\u06fb\u0704\5\u01a0\u00d1\2\u06fc\u0704\5\u01a6")
        buf.write("\u00d4\2\u06fd\u0704\5\u01a2\u00d2\2\u06fe\u0704\5\u01a4")
        buf.write("\u00d3\2\u06ff\u0704\5\u0198\u00cd\2\u0700\u0704\5\u019c")
        buf.write("\u00cf\2\u0701\u0704\7l\2\2\u0702\u0704\7{\2\2\u0703\u06f6")
        buf.write("\3\2\2\2\u0703\u06f7\3\2\2\2\u0703\u06f8\3\2\2\2\u0703")
        buf.write("\u06f9\3\2\2\2\u0703\u06fa\3\2\2\2\u0703\u06fb\3\2\2\2")
        buf.write("\u0703\u06fc\3\2\2\2\u0703\u06fd\3\2\2\2\u0703\u06fe\3")
        buf.write("\2\2\2\u0703\u06ff\3\2\2\2\u0703\u0700\3\2\2\2\u0703\u0701")
        buf.write("\3\2\2\2\u0703\u0702\3\2\2\2\u0704\u0707\3\2\2\2\u0705")
        buf.write("\u0703\3\2\2\2\u0705\u0706\3\2\2\2\u0706\u070b\3\2\2\2")
        buf.write("\u0707\u0705\3\2\2\2\u0708\u070a\7l\2\2\u0709\u0708\3")
        buf.write("\2\2\2\u070a\u070d\3\2\2\2\u070b\u0709\3\2\2\2\u070b\u070c")
        buf.write("\3\2\2\2\u070c\u0710\3\2\2\2\u070d\u070b\3\2\2\2\u070e")
        buf.write("\u0711\5\u018a\u00c6\2\u070f\u0711\5\u018e\u00c8\2\u0710")
        buf.write("\u070e\3\2\2\2\u0710\u070f\3\2\2\2\u0710\u0711\3\2\2\2")
        buf.write("\u0711\u0715\3\2\2\2\u0712\u0714\7l\2\2\u0713\u0712\3")
        buf.write("\2\2\2\u0714\u0717\3\2\2\2\u0715\u0713\3\2\2\2\u0715\u0716")
        buf.write("\3\2\2\2\u0716\u071b\3\2\2\2\u0717\u0715\3\2\2\2\u0718")
        buf.write("\u071a\5\u0186\u00c4\2\u0719\u0718\3\2\2\2\u071a\u071d")
        buf.write("\3\2\2\2\u071b\u0719\3\2\2\2\u071b\u071c\3\2\2\2\u071c")
        buf.write("\u0721\3\2\2\2\u071d\u071b\3\2\2\2\u071e\u0720\7l\2\2")
        buf.write("\u071f\u071e\3\2\2\2\u0720\u0723\3\2\2\2\u0721\u071f\3")
        buf.write("\2\2\2\u0721\u0722\3\2\2\2\u0722\u0724\3\2\2\2\u0723\u0721")
        buf.write("\3\2\2\2\u0724\u0725\7u\2\2\u0725\u0185\3\2\2\2\u0726")
        buf.write("\u072a\5\u01ae\u00d8\2\u0727\u0729\7l\2\2\u0728\u0727")
        buf.write("\3\2\2\2\u0729\u072c\3\2\2\2\u072a\u0728\3\2\2\2\u072a")
        buf.write("\u072b\3\2\2\2\u072b\u072d\3\2\2\2\u072c\u072a\3\2\2\2")
        buf.write("\u072d\u0731\7t\2\2\u072e\u0730\7l\2\2\u072f\u072e\3\2")
        buf.write("\2\2\u0730\u0733\3\2\2\2\u0731\u072f\3\2\2\2\u0731\u0732")
        buf.write("\3\2\2\2\u0732\u0734\3\2\2\2\u0733\u0731\3\2\2\2\u0734")
        buf.write("\u0738\5\u015c\u00af\2\u0735\u0737\7l\2\2\u0736\u0735")
        buf.write("\3\2\2\2\u0737\u073a\3\2\2\2\u0738\u0736\3\2\2\2\u0738")
        buf.write("\u0739\3\2\2\2\u0739\u073b\3\2\2\2\u073a\u0738\3\2\2\2")
        buf.write("\u073b\u073f\7u\2\2\u073c\u073e\7l\2\2\u073d\u073c\3\2")
        buf.write("\2\2\u073e\u0741\3\2\2\2\u073f\u073d\3\2\2\2\u073f\u0740")
        buf.write("\3\2\2\2\u0740\u0187\3\2\2\2\u0741\u073f\3\2\2\2\u0742")
        buf.write("\u0743\5\32\16\2\u0743\u0189\3\2\2\2\u0744\u0745\7t\2")
        buf.write("\2\u0745\u0746\5\u018c\u00c7\2\u0746\u0747\7u\2\2\u0747")
        buf.write("\u0749\3\2\2\2\u0748\u0744\3\2\2\2\u0748\u0749\3\2\2\2")
        buf.write("\u0749\u074a\3\2\2\2\u074a\u074b\7\177\2\2\u074b\u074c")
        buf.write("\7q\2\2\u074c\u074d\5*\26\2\u074d\u018b\3\2\2\2\u074e")
        buf.write("\u074f\t\r\2\2\u074f\u018d\3\2\2\2\u0750\u0751\7t\2\2")
        buf.write("\u0751\u0752\5\u018c\u00c7\2\u0752\u0753\7u\2\2\u0753")
        buf.write("\u0755\3\2\2\2\u0754\u0750\3\2\2\2\u0754\u0755\3\2\2\2")
        buf.write("\u0755\u0756\3\2\2\2\u0756\u0757\7\177\2\2\u0757\u0758")
        buf.write("\7q\2\2\u0758\u0759\5\u0190\u00c9\2\u0759\u018f\3\2\2")
        buf.write("\2\u075a\u075b\t\4\2\2\u075b\u0191\3\2\2\2\u075c\u075f")
        buf.write("\5\36\20\2\u075d\u075f\5\34\17\2\u075e\u075c\3\2\2\2\u075e")
        buf.write("\u075d\3\2\2\2\u075f\u0193\3\2\2\2\u0760\u0761\5*\26\2")
        buf.write("\u0761\u0195\3\2\2\2\u0762\u0763\7*\2\2\u0763\u0764\7")
        buf.write("r\2\2\u0764\u0765\5\32\16\2\u0765\u0197\3\2\2\2\u0766")
        buf.write("\u0767\7\60\2\2\u0767\u0768\7r\2\2\u0768\u0769\5\u019a")
        buf.write("\u00ce\2\u0769\u0199\3\2\2\2\u076a\u076b\t\4\2\2\u076b")
        buf.write("\u019b\3\2\2\2\u076c\u076d\7/\2\2\u076d\u076e\7r\2\2\u076e")
        buf.write("\u076f\5\u019e\u00d0\2\u076f\u019d\3\2\2\2\u0770\u0771")
        buf.write("\t\4\2\2\u0771\u019f\3\2\2\2\u0772\u0773\7\64\2\2\u0773")
        buf.write("\u0774\7r\2\2\u0774\u0775\5\32\16\2\u0775\u01a1\3\2\2")
        buf.write("\2\u0776\u077a\7\62\2\2\u0777\u077b\5(\25\2\u0778\u0779")
        buf.write("\7r\2\2\u0779\u077b\5*\26\2\u077a\u0777\3\2\2\2\u077a")
        buf.write("\u0778\3\2\2\2\u077b\u01a3\3\2\2\2\u077c\u0780\7\61\2")
        buf.write("\2\u077d\u0781\5(\25\2\u077e\u077f\7r\2\2\u077f\u0781")
        buf.write("\5*\26\2\u0780\u077d\3\2\2\2\u0780\u077e\3\2\2\2\u0781")
        buf.write("\u01a5\3\2\2\2\u0782\u0783\7\63\2\2\u0783\u0784\7r\2\2")
        buf.write("\u0784\u0785\5\32\16\2\u0785\u01a7\3\2\2\2\u0786\u0787")
        buf.write("\7\65\2\2\u0787\u0788\7r\2\2\u0788\u0789\5\32\16\2\u0789")
        buf.write("\u01a9\3\2\2\2\u078a\u078b\7;\2\2\u078b\u078c\7r\2\2\u078c")
        buf.write("\u078d\5\u01ac\u00d7\2\u078d\u01ab\3\2\2\2\u078e\u0793")
        buf.write("\5\u01ae\u00d8\2\u078f\u0790\7{\2\2\u0790\u0792\5\u01ae")
        buf.write("\u00d8\2\u0791\u078f\3\2\2\2\u0792\u0795\3\2\2\2\u0793")
        buf.write("\u0791\3\2\2\2\u0793\u0794\3\2\2\2\u0794\u01ad\3\2\2\2")
        buf.write("\u0795\u0793\3\2\2\2\u0796\u0797\t\16\2\2\u0797\u01af")
        buf.write("\3\2\2\2\u0798\u0799\7R\2\2\u0799\u079a\7r\2\2\u079a\u079b")
        buf.write("\5\u01b2\u00da\2\u079b\u01b1\3\2\2\2\u079c\u07a1\5\u01b4")
        buf.write("\u00db\2\u079d\u079e\7{\2\2\u079e\u07a0\5\u01b4\u00db")
        buf.write("\2\u079f\u079d\3\2\2\2\u07a0\u07a3\3\2\2\2\u07a1\u079f")
        buf.write("\3\2\2\2\u07a1\u07a2\3\2\2\2\u07a2\u01b3\3\2\2\2\u07a3")
        buf.write("\u07a1\3\2\2\2\u07a4\u07a6\5\u01b6\u00dc\2\u07a5\u07a7")
        buf.write("\5\u01b8\u00dd\2\u07a6\u07a5\3\2\2\2\u07a6\u07a7\3\2\2")
        buf.write("\2\u07a7\u01b5\3\2\2\2\u07a8\u07ae\7\u0083\2\2\u07a9\u07ab")
        buf.write("\7s\2\2\u07aa\u07a9\3\2\2\2\u07aa\u07ab\3\2\2\2\u07ab")
        buf.write("\u07ac\3\2\2\2\u07ac\u07ae\5\32\16\2\u07ad\u07a8\3\2\2")
        buf.write("\2\u07ad\u07aa\3\2\2\2\u07ae\u01b7\3\2\2\2\u07af\u07b0")
        buf.write("\5*\26\2\u07b0\u01b9\3\2\2\2\u07b1\u07b2\7\66\2\2\u07b2")
        buf.write("\u07b3\7r\2\2\u07b3\u07b4\5\u01bc\u00df\2\u07b4\u01bb")
        buf.write("\3\2\2\2\u07b5\u07ba\5\u01be\u00e0\2\u07b6\u07b7\7{\2")
        buf.write("\2\u07b7\u07b9\5\u01be\u00e0\2\u07b8\u07b6\3\2\2\2\u07b9")
        buf.write("\u07bc\3\2\2\2\u07ba\u07b8\3\2\2\2\u07ba\u07bb\3\2\2\2")
        buf.write("\u07bb\u01bd\3\2\2\2\u07bc\u07ba\3\2\2\2\u07bd\u07be\5")
        buf.write("\u01c0\u00e1\2\u07be\u01bf\3\2\2\2\u07bf\u07c5\7\u0083")
        buf.write("\2\2\u07c0\u07c2\7s\2\2\u07c1\u07c0\3\2\2\2\u07c1\u07c2")
        buf.write("\3\2\2\2\u07c2\u07c3\3\2\2\2\u07c3\u07c5\5\32\16\2\u07c4")
        buf.write("\u07bf\3\2\2\2\u07c4\u07c1\3\2\2\2\u07c5\u01c1\3\2\2\2")
        buf.write("\u07c6\u07c7\7\f\2\2\u07c7\u07c8\5\u0184\u00c3\2\u07c8")
        buf.write("\u01c3\3\2\2\2\u07c9\u07ca\7\13\2\2\u07ca\u07cb\5\u0184")
        buf.write("\u00c3\2\u07cb\u01c5\3\2\2\2\u07cc\u07cd\7\n\2\2\u07cd")
        buf.write("\u07ce\5\u0184\u00c3\2\u07ce\u01c7\3\2\2\2\u07cf\u07d0")
        buf.write("\7\b\2\2\u07d0\u07d1\7|\2\2\u07d1\u07d2\5\u01ca\u00e6")
        buf.write("\2\u07d2\u07d6\7t\2\2\u07d3\u07d5\7l\2\2\u07d4\u07d3\3")
        buf.write("\2\2\2\u07d5\u07d8\3\2\2\2\u07d6\u07d4\3\2\2\2\u07d6\u07d7")
        buf.write("\3\2\2\2\u07d7\u07da\3\2\2\2\u07d8\u07d6\3\2\2\2\u07d9")
        buf.write("\u07db\5\u01cc\u00e7\2\u07da\u07d9\3\2\2\2\u07db\u07dc")
        buf.write("\3\2\2\2\u07dc\u07da\3\2\2\2\u07dc\u07dd\3\2\2\2\u07dd")
        buf.write("\u07e1\3\2\2\2\u07de\u07e0\7l\2\2\u07df\u07de\3\2\2\2")
        buf.write("\u07e0\u07e3\3\2\2\2\u07e1\u07df\3\2\2\2\u07e1\u07e2\3")
        buf.write("\2\2\2\u07e2\u07e4\3\2\2\2\u07e3\u07e1\3\2\2\2\u07e4\u07e5")
        buf.write("\7u\2\2\u07e5\u01c9\3\2\2\2\u07e6\u07e7\5\32\16\2\u07e7")
        buf.write("\u01cb\3\2\2\2\u07e8\u07ea\7{\2\2\u07e9\u07e8\3\2\2\2")
        buf.write("\u07e9\u07ea\3\2\2\2\u07ea\u07ee\3\2\2\2\u07eb\u07ed\7")
        buf.write("l\2\2\u07ec\u07eb\3\2\2\2\u07ed\u07f0\3\2\2\2\u07ee\u07ec")
        buf.write("\3\2\2\2\u07ee\u07ef\3\2\2\2\u07ef\u07f2\3\2\2\2\u07f0")
        buf.write("\u07ee\3\2\2\2\u07f1\u07f3\5\u01d2\u00ea\2\u07f2\u07f1")
        buf.write("\3\2\2\2\u07f2\u07f3\3\2\2\2\u07f3\u07f4\3\2\2\2\u07f4")
        buf.write("\u07f7\5\u01e0\u00f1\2\u07f5\u07f8\5\u01d0\u00e9\2\u07f6")
        buf.write("\u07f8\5\u01ce\u00e8\2\u07f7\u07f5\3\2\2\2\u07f7\u07f6")
        buf.write("\3\2\2\2\u07f8\u07fc\3\2\2\2\u07f9\u07fb\7l\2\2\u07fa")
        buf.write("\u07f9\3\2\2\2\u07fb\u07fe\3\2\2\2\u07fc\u07fa\3\2\2\2")
        buf.write("\u07fc\u07fd\3\2\2\2\u07fd\u01cd\3\2\2\2\u07fe\u07fc\3")
        buf.write("\2\2\2\u07ff\u0802\7r\2\2\u0800\u0803\5\u01dc\u00ef\2")
        buf.write("\u0801\u0803\5\u01da\u00ee\2\u0802\u0800\3\2\2\2\u0802")
        buf.write("\u0801\3\2\2\2\u0803\u01cf\3\2\2\2\u0804\u0805\5(\25\2")
        buf.write("\u0805\u01d1\3\2\2\2\u0806\u0807\7v\2\2\u0807\u080c\5")
        buf.write("\u01d4\u00eb\2\u0808\u0809\7{\2\2\u0809\u080b\5\u01d4")
        buf.write("\u00eb\2\u080a\u0808\3\2\2\2\u080b\u080e\3\2\2\2\u080c")
        buf.write("\u080a\3\2\2\2\u080c\u080d\3\2\2\2\u080d\u080f\3\2\2\2")
        buf.write("\u080e\u080c\3\2\2\2\u080f\u0810\7w\2\2\u0810\u01d3\3")
        buf.write("\2\2\2\u0811\u0812\5\u01d6\u00ec\2\u0812\u0813\7\177\2")
        buf.write("\2\u0813\u0814\5\u01d8\u00ed\2\u0814\u01d5\3\2\2\2\u0815")
        buf.write("\u0816\5\32\16\2\u0816\u01d7\3\2\2\2\u0817\u081b\7\u0086")
        buf.write("\2\2\u0818\u081b\7\u0087\2\2\u0819\u081b\5\32\16\2\u081a")
        buf.write("\u0817\3\2\2\2\u081a\u0818\3\2\2\2\u081a\u0819\3\2\2\2")
        buf.write("\u081b\u01d9\3\2\2\2\u081c\u081d\t\4\2\2\u081d\u01db\3")
        buf.write("\2\2\2\u081e\u081f\7.\2\2\u081f\u0820\7t\2\2\u0820\u0821")
        buf.write("\5\u01de\u00f0\2\u0821\u0822\7u\2\2\u0822\u01dd\3\2\2")
        buf.write("\2\u0823\u0824\5\32\16\2\u0824\u0825\7|\2\2\u0825\u0827")
        buf.write("\3\2\2\2\u0826\u0823\3\2\2\2\u0826\u0827\3\2\2\2\u0827")
        buf.write("\u0828\3\2\2\2\u0828\u0829\5\32\16\2\u0829\u01df\3\2\2")
        buf.write("\2\u082a\u082e\7\u0086\2\2\u082b\u082e\7\u0087\2\2\u082c")
        buf.write("\u082e\5\32\16\2\u082d\u082a\3\2\2\2\u082d\u082b\3\2\2")
        buf.write("\2\u082d\u082c\3\2\2\2\u082e\u01e1\3\2\2\2\u082f\u0831")
        buf.write("\7\7\2\2\u0830\u0832\5*\26\2\u0831\u0830\3\2\2\2\u0831")
        buf.write("\u0832\3\2\2\2\u0832\u01e3\3\2\2\2\u0833\u0834\7\5\2\2")
        buf.write("\u0834\u0837\7t\2\2\u0835\u0838\5\u01e6\u00f4\2\u0836")
        buf.write("\u0838\7l\2\2\u0837\u0835\3\2\2\2\u0837\u0836\3\2\2\2")
        buf.write("\u0838\u0839\3\2\2\2\u0839\u0837\3\2\2\2\u0839\u083a\3")
        buf.write("\2\2\2\u083a\u083b\3\2\2\2\u083b\u083c\7u\2\2\u083c\u01e5")
        buf.write("\3\2\2\2\u083d\u083f\5\u01e8\u00f5\2\u083e\u0840\5\u01ea")
        buf.write("\u00f6\2\u083f\u083e\3\2\2\2\u083f\u0840\3\2\2\2\u0840")
        buf.write("\u0842\3\2\2\2\u0841\u0843\5\u01ec\u00f7\2\u0842\u0841")
        buf.write("\3\2\2\2\u0842\u0843\3\2\2\2\u0843\u0845\3\2\2\2\u0844")
        buf.write("\u0846\7{\2\2\u0845\u0844\3\2\2\2\u0845\u0846\3\2\2\2")
        buf.write("\u0846\u0848\3\2\2\2\u0847\u0849\7l\2\2\u0848\u0847\3")
        buf.write("\2\2\2\u0848\u0849\3\2\2\2\u0849\u01e7\3\2\2\2\u084a\u084d")
        buf.write("\5\36\20\2\u084b\u084d\5\34\17\2\u084c\u084a\3\2\2\2\u084c")
        buf.write("\u084b\3\2\2\2\u084d\u01e9\3\2\2\2\u084e\u084f\5*\26\2")
        buf.write("\u084f\u01eb\3\2\2\2\u0850\u0851\7\177\2\2\u0851\u085b")
        buf.write("\7q\2\2\u0852\u085c\7\u0083\2\2\u0853\u0858\5\u01ee\u00f8")
        buf.write("\2\u0854\u0855\7{\2\2\u0855\u0857\5\u01ee\u00f8\2\u0856")
        buf.write("\u0854\3\2\2\2\u0857\u085a\3\2\2\2\u0858\u0856\3\2\2\2")
        buf.write("\u0858\u0859\3\2\2\2\u0859\u085c\3\2\2\2\u085a\u0858\3")
        buf.write("\2\2\2\u085b\u0852\3\2\2\2\u085b\u0853\3\2\2\2\u085c\u01ed")
        buf.write("\3\2\2\2\u085d\u085e\5\32\16\2\u085e\u01ef\3\2\2\2\u085f")
        buf.write("\u0865\7\3\2\2\u0860\u0862\7t\2\2\u0861\u0863\5\u01f2")
        buf.write("\u00fa\2\u0862\u0861\3\2\2\2\u0862\u0863\3\2\2\2\u0863")
        buf.write("\u0864\3\2\2\2\u0864\u0866\7u\2\2\u0865\u0860\3\2\2\2")
        buf.write("\u0865\u0866\3\2\2\2\u0866\u01f1\3\2\2\2\u0867\u0868\7")
        buf.write("+\2\2\u0868\u0869\7r\2\2\u0869\u086a\7)\2\2\u086a\u01f3")
        buf.write("\3\2\2\2\u086b\u086e\7\26\2\2\u086c\u086d\7|\2\2\u086d")
        buf.write("\u086f\5\u01f6\u00fc\2\u086e\u086c\3\2\2\2\u086e\u086f")
        buf.write("\3\2\2\2\u086f\u0870\3\2\2\2\u0870\u0871\5*\26\2\u0871")
        buf.write("\u01f5\3\2\2\2\u0872\u0873\5\32\16\2\u0873\u01f7\3\2\2")
        buf.write("\2\u00dd\u01fb\u0201\u0207\u020b\u0210\u0212\u0217\u021b")
        buf.write("\u0220\u0222\u0227\u022f\u0234\u023c\u0243\u0246\u024f")
        buf.write("\u0255\u0258\u0267\u026e\u0273\u027b\u0281\u0286\u0289")
        buf.write("\u028c\u0290\u0298\u02a6\u02ab\u02b7\u02bd\u02c2\u02cf")
        buf.write("\u02d5\u02da\u02e0\u02e6\u02ec\u02f2\u02fa\u02fd\u0301")
        buf.write("\u0305\u0310\u0316\u031b\u0322\u0329\u032e\u0331\u0334")
        buf.write("\u0339\u033c\u0340\u0345\u034a\u034f\u0362\u0366\u0384")
        buf.write("\u03a3\u03a7\u03b2\u03b6\u03bd\u03c7\u03d0\u03d4\u03db")
        buf.write("\u03ea\u03f4\u03fd\u0406\u0415\u041f\u0422\u043f\u0452")
        buf.write("\u0458\u045e\u0464\u0466\u0475\u0477\u0482\u048a\u048f")
        buf.write("\u0495\u049a\u04a0\u04a5\u04ab\u04b4\u04bd\u04c4\u04c9")
        buf.write("\u04d5\u04de\u04ea\u04f1\u04fc\u04fe\u050f\u0512\u0516")
        buf.write("\u053f\u0551\u0553\u0559\u055d\u0562\u056a\u0572\u0578")
        buf.write("\u0582\u0590\u059a\u059c\u05a0\u05b7\u05bc\u05cc\u05d5")
        buf.write("\u05de\u05e7\u05f0\u05f9\u0600\u0607\u060c\u0610\u0614")
        buf.write("\u0618\u061a\u061e\u0623\u0630\u0637\u063f\u0641\u0644")
        buf.write("\u064b\u064d\u0655\u065c\u065f\u0661\u0668\u066e\u0672")
        buf.write("\u0677\u067d\u0688\u068b\u0694\u0698\u069d\u06a0\u06a9")
        buf.write("\u06bc\u06c1\u06cc\u06d4\u06df\u06e9\u06ef\u06f4\u0703")
        buf.write("\u0705\u070b\u0710\u0715\u071b\u0721\u072a\u0731\u0738")
        buf.write("\u073f\u0748\u0754\u075e\u077a\u0780\u0793\u07a1\u07a6")
        buf.write("\u07aa\u07ad\u07ba\u07c1\u07c4\u07d6\u07dc\u07e1\u07e9")
        buf.write("\u07ee\u07f2\u07f7\u07fc\u0802\u080c\u081a\u0826\u082d")
        buf.write("\u0831\u0837\u0839\u083f\u0842\u0845\u0848\u084c\u0858")
        buf.write("\u085b\u0862\u0865\u086e")
        return buf.getvalue()


class ZmeiLangParser ( Parser ):

    grammarFileName = "ZmeiLangParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'@flutter'", "'@file'", "'@stream'", 
                     "'@channels'", "'@get'", "'@menu'", "'@crud'", "'@crud_detail'", 
                     "'@crud_delete'", "'@crud_edit'", "'@crud_create'", 
                     "'@celery'", "'@post'", "'@error'", "'@auth'", "'@markdown'", 
                     "'@react'", "'@react_client'", "'@react_server'", "'@html'", 
                     "'@tree'", "'@date_tree'", "'@mixin'", "'@m2m_changed'", 
                     "'@post_delete'", "'@pre_delete'", "'@post_save'", 
                     "'@pre_save'", "'@clean'", "'@api'", "'@rest'", "'@order'", 
                     "'@sortable'", "'@langs'", "'@filer'", "'@admin'", 
                     "'@suit'", "<INVALID>", "<INVALID>", "'theme'", "'child'", 
                     "'filter_out'", "'filter_in'", "'page'", "'link_suffix'", 
                     "'url_prefix'", "'can_edit'", "'object_expr'", "'block'", 
                     "'item_name'", "'pk_param'", "'list_fields'", "'delete'", 
                     "'edit'", "'create'", "'detail'", "'skip'", "'from'", 
                     "'+polymorphic_list'", "'css'", "'js'", "<INVALID>", 
                     "<INVALID>", "'inline'", "'type'", "'user_field'", 
                     "'annotate'", "'on_create'", "'query'", "'auth'", "'count'", 
                     "'i18n'", "'extra'", "'tabs'", "'list'", "'read_only'", 
                     "'list_editable'", "'list_filter'", "'list_search'", 
                     "'fields'", "'import'", "'as'", "'text'", "'html'", 
                     "'html_media'", "'float'", "'decimal'", "'date'", "'datetime'", 
                     "'create_time'", "'update_time'", "'image'", "'file'", 
                     "'filer_image'", "'filer_file'", "'filer_folder'", 
                     "'filer_image_folder'", "'str'", "'int'", "'slug'", 
                     "'bool'", "'one'", "'one2one'", "'many'", "'choices'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'<'", "'>'", "':'", "'^'", "'('", "')'", "'['", "']'", 
                     "'?'", "'_'", "'-'", "','", "'.'", "'#'", "'/'", "'='", 
                     "'$'", "'&'", "'!'", "'*'", "'~'", "'|'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "' '", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "';'", "<INVALID>", 
                     "'\n'" ]

    symbolicNames = [ "<INVALID>", "AN_FLUTTER", "AN_FILE", "AN_STREAM", 
                      "AN_CHANNELS", "AN_GET", "AN_MENU", "AN_CRUD", "AN_CRUD_DETAIL", 
                      "AN_CRUD_DELETE", "AN_CRUD_EDIT", "AN_CRUD_CREATE", 
                      "AN_CELERY", "AN_POST", "AN_ERROR", "AN_AUTH", "AN_MARKDOWN", 
                      "AN_REACT", "AN_REACT_CLIENT", "AN_REACT_SERVER", 
                      "AN_HTML", "AN_TREE", "AN_DATE_TREE", "AN_MIXIN", 
                      "AN_M2M_CHANGED", "AN_POST_DELETE", "AN_PRE_DELETE", 
                      "AN_POST_SAVE", "AN_PRE_SAVE", "AN_CLEAN", "AN_API", 
                      "AN_REST", "AN_ORDER", "AN_SORTABLE", "AN_LANGS", 
                      "AN_FILER", "AN_ADMIN", "AN_SUIT", "WRITE_MODE", "BOOL", 
                      "KW_THEME", "KW_CHILD", "KW_FILTER_OUT", "KW_FILTER_IN", 
                      "KW_PAGE", "KW_LINK_SUFFIX", "KW_URL_PREFIX", "KW_CAN_EDIT", 
                      "KW_OBJECT_EXPR", "KW_BLOCK", "KW_ITEM_NAME", "KW_PK_PARAM", 
                      "KW_LIST_FIELDS", "KW_DELETE", "KW_EDIT", "KW_CREATE", 
                      "KW_DETAIL", "KW_SKIP", "KW_FROM", "KW_POLY_LIST", 
                      "KW_CSS", "KW_JS", "KW_INLINE_TYPE", "KW_AUTH_TYPE", 
                      "KW_INLINE", "KW_TYPE", "KW_USER_FIELD", "KW_ANNOTATE", 
                      "KW_ON_CREATE", "KW_QUERY", "KW_AUTH", "KW_COUNT", 
                      "KW_I18N", "KW_EXTRA", "KW_TABS", "KW_LIST", "KW_READ_ONLY", 
                      "KW_LIST_EDITABLE", "KW_LIST_FILTER", "KW_LIST_SEARCH", 
                      "KW_FIELDS", "KW_IMPORT", "KW_AS", "COL_FIELD_TYPE_LONGTEXT", 
                      "COL_FIELD_TYPE_HTML", "COL_FIELD_TYPE_HTML_MEDIA", 
                      "COL_FIELD_TYPE_FLOAT", "COL_FIELD_TYPE_DECIMAL", 
                      "COL_FIELD_TYPE_DATE", "COL_FIELD_TYPE_DATETIME", 
                      "COL_FIELD_TYPE_CREATE_TIME", "COL_FIELD_TYPE_UPDATE_TIME", 
                      "COL_FIELD_TYPE_IMAGE", "COL_FIELD_TYPE_FILE", "COL_FIELD_TYPE_FILER_IMAGE", 
                      "COL_FIELD_TYPE_FILER_FILE", "COL_FIELD_TYPE_FILER_FOLDER", 
                      "COL_FIELD_TYPE_FILER_IMAGE_FOLDER", "COL_FIELD_TYPE_TEXT", 
                      "COL_FIELD_TYPE_INT", "COL_FIELD_TYPE_SLUG", "COL_FIELD_TYPE_BOOL", 
                      "COL_FIELD_TYPE_ONE", "COL_FIELD_TYPE_ONE2ONE", "COL_FIELD_TYPE_MANY", 
                      "COL_FIELD_CHOICES", "NL", "ID", "DIGIT", "SIZE2D", 
                      "LT", "GT", "COLON", "EXCLUDE", "BRACE_OPEN", "BRACE_CLOSE", 
                      "SQ_BRACE_OPEN", "SQ_BRACE_CLOSE", "QUESTION_MARK", 
                      "UNDERSCORE", "DASH", "COMA", "DOT", "HASH", "SLASH", 
                      "EQUALS", "DOLLAR", "AMP", "EXCLAM", "STAR", "APPROX", 
                      "PIPE", "STRING_DQ", "STRING_SQ", "COMMENT_LINE", 
                      "COMMENT_BLOCK", "UNICODE", "WS", "COL_FIELD_CALCULATED", 
                      "ASSIGN", "ASSIGN_STATIC", "CODE_BLOCK", "ERRCHAR", 
                      "PYTHON_CODE", "PYTHON_LINE_ERRCHAR", "PYTHON_LINE_END", 
                      "PYTHON_EXPR_ERRCHAR", "PYTHON_LINE_NL" ]

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
    RULE_an_filer = 22
    RULE_an_langs = 23
    RULE_an_langs_list = 24
    RULE_an_celery = 25
    RULE_an_channels = 26
    RULE_an_file = 27
    RULE_an_file_name = 28
    RULE_an_suit = 29
    RULE_an_suit_app_name = 30
    RULE_col = 31
    RULE_col_str_expr = 32
    RULE_col_header = 33
    RULE_col_header_line_separator = 34
    RULE_col_verbose_name = 35
    RULE_verbose_name_part = 36
    RULE_col_base_name = 37
    RULE_col_name = 38
    RULE_col_field = 39
    RULE_col_field_expr_or_def = 40
    RULE_col_field_custom = 41
    RULE_col_field_extend = 42
    RULE_col_field_extend_append = 43
    RULE_wrong_field_type = 44
    RULE_col_field_expr = 45
    RULE_col_field_expr_marker = 46
    RULE_col_feild_expr_code = 47
    RULE_string_or_quoted = 48
    RULE_col_field_help_text = 49
    RULE_col_field_verbose_name = 50
    RULE_col_field_name = 51
    RULE_col_modifier = 52
    RULE_col_field_def = 53
    RULE_field_longtext = 54
    RULE_field_html = 55
    RULE_field_html_media = 56
    RULE_field_float = 57
    RULE_field_decimal = 58
    RULE_field_date = 59
    RULE_field_datetime = 60
    RULE_field_create_time = 61
    RULE_field_update_time = 62
    RULE_field_file = 63
    RULE_field_filer_file = 64
    RULE_field_filer_folder = 65
    RULE_field_text = 66
    RULE_field_text_size = 67
    RULE_field_text_choices = 68
    RULE_field_text_choice = 69
    RULE_field_text_choice_val = 70
    RULE_field_text_choice_key = 71
    RULE_field_int = 72
    RULE_field_int_choices = 73
    RULE_field_int_choice = 74
    RULE_field_int_choice_val = 75
    RULE_field_int_choice_key = 76
    RULE_field_slug = 77
    RULE_field_slug_ref_field = 78
    RULE_field_slug_ref_field_id = 79
    RULE_field_bool = 80
    RULE_field_bool_default = 81
    RULE_field_image = 82
    RULE_filer_image_type = 83
    RULE_field_image_sizes = 84
    RULE_field_image_size = 85
    RULE_field_image_size_dimensions = 86
    RULE_field_image_size_name = 87
    RULE_field_image_filters = 88
    RULE_field_image_filter = 89
    RULE_field_relation = 90
    RULE_field_relation_type = 91
    RULE_field_relation_target_ref = 92
    RULE_field_relation_target_class = 93
    RULE_field_relation_related_name = 94
    RULE_model_annotation = 95
    RULE_an_sortable = 96
    RULE_an_sortable_field_name = 97
    RULE_an_order = 98
    RULE_an_order_fields = 99
    RULE_an_rest = 100
    RULE_an_rest_config = 101
    RULE_an_rest_main_part = 102
    RULE_an_rest_descriptor = 103
    RULE_an_rest_i18n = 104
    RULE_an_rest_query = 105
    RULE_an_rest_on_create = 106
    RULE_an_rest_filter_in = 107
    RULE_an_rest_filter_out = 108
    RULE_an_rest_read_only = 109
    RULE_an_rest_user_field = 110
    RULE_an_rest_fields = 111
    RULE_an_rest_fields_write_mode = 112
    RULE_an_rest_auth = 113
    RULE_an_rest_auth_type = 114
    RULE_an_rest_auth_token_model = 115
    RULE_an_rest_auth_token_class = 116
    RULE_an_rest_annotate = 117
    RULE_an_rest_annotate_count = 118
    RULE_an_rest_annotate_count_field = 119
    RULE_an_rest_annotate_count_alias = 120
    RULE_an_rest_inline = 121
    RULE_an_rest_inline_decl = 122
    RULE_an_rest_inline_name = 123
    RULE_an_api = 124
    RULE_an_api_all = 125
    RULE_an_api_name = 126
    RULE_an_clean = 127
    RULE_an_pre_save = 128
    RULE_an_post_save = 129
    RULE_an_pre_delete = 130
    RULE_an_post_delete = 131
    RULE_an_m2m_changed = 132
    RULE_an_mixin = 133
    RULE_an_date_tree = 134
    RULE_an_date_tree_field = 135
    RULE_an_tree = 136
    RULE_an_tree_poly = 137
    RULE_an_admin = 138
    RULE_an_admin_js = 139
    RULE_an_admin_css = 140
    RULE_an_admin_css_file_name = 141
    RULE_an_admin_js_file_name = 142
    RULE_an_admin_inlines = 143
    RULE_an_admin_inline = 144
    RULE_inline_name = 145
    RULE_inline_type = 146
    RULE_inline_extra = 147
    RULE_inline_fields = 148
    RULE_an_admin_tabs = 149
    RULE_an_admin_tab = 150
    RULE_tab_name = 151
    RULE_tab_verbose_name = 152
    RULE_an_admin_list = 153
    RULE_an_admin_read_only = 154
    RULE_an_admin_list_editable = 155
    RULE_an_admin_list_filter = 156
    RULE_an_admin_list_search = 157
    RULE_an_admin_fields = 158
    RULE_page = 159
    RULE_page_header = 160
    RULE_page_base = 161
    RULE_page_alias = 162
    RULE_page_alias_name = 163
    RULE_page_template = 164
    RULE_template_name = 165
    RULE_file_name_part = 166
    RULE_page_url = 167
    RULE_url_part = 168
    RULE_url_param = 169
    RULE_url_segment = 170
    RULE_url_segments = 171
    RULE_page_name = 172
    RULE_page_body = 173
    RULE_page_code = 174
    RULE_page_field = 175
    RULE_page_field_name = 176
    RULE_page_field_code = 177
    RULE_page_function = 178
    RULE_page_function_name = 179
    RULE_page_function_args = 180
    RULE_page_annotation = 181
    RULE_an_react = 182
    RULE_an_react_type = 183
    RULE_an_react_descriptor = 184
    RULE_an_markdown = 185
    RULE_an_markdown_descriptor = 186
    RULE_an_auth = 187
    RULE_an_error = 188
    RULE_an_error_code = 189
    RULE_an_post = 190
    RULE_an_crud_create = 191
    RULE_an_crud = 192
    RULE_an_crud_params = 193
    RULE_an_crud_page_override = 194
    RULE_an_crud_descriptor = 195
    RULE_an_crud_next_page = 196
    RULE_an_crud_next_page_event_name = 197
    RULE_an_crud_next_page_url = 198
    RULE_an_crud_next_page_url_val = 199
    RULE_an_crud_target_model = 200
    RULE_an_crud_target_filter = 201
    RULE_an_crud_theme = 202
    RULE_an_crud_url_prefix = 203
    RULE_an_crud_url_prefix_val = 204
    RULE_an_crud_link_suffix = 205
    RULE_an_crud_link_suffix_val = 206
    RULE_an_crud_item_name = 207
    RULE_an_crud_object_expr = 208
    RULE_an_crud_can_edit = 209
    RULE_an_crud_block = 210
    RULE_an_crud_pk_param = 211
    RULE_an_crud_skip = 212
    RULE_an_crud_skip_values = 213
    RULE_an_crud_view_name = 214
    RULE_an_crud_fields = 215
    RULE_an_crud_fields_expr = 216
    RULE_an_crud_field = 217
    RULE_an_crud_field_spec = 218
    RULE_an_crud_field_filter = 219
    RULE_an_crud_list_fields = 220
    RULE_an_crud_list_fields_expr = 221
    RULE_an_crud_list_field = 222
    RULE_an_crud_list_field_spec = 223
    RULE_an_crud_edit = 224
    RULE_an_crud_delete = 225
    RULE_an_crud_detail = 226
    RULE_an_menu = 227
    RULE_an_menu_descriptor = 228
    RULE_an_menu_item = 229
    RULE_an_menu_target = 230
    RULE_an_menu_item_code = 231
    RULE_an_menu_item_args = 232
    RULE_an_menu_item_arg = 233
    RULE_an_menu_item_arg_key = 234
    RULE_an_menu_item_arg_val = 235
    RULE_an_menu_item_url = 236
    RULE_an_menu_item_page = 237
    RULE_an_menu_item_page_ref = 238
    RULE_an_menu_label = 239
    RULE_an_get = 240
    RULE_an_stream = 241
    RULE_an_stream_model = 242
    RULE_an_stream_target_model = 243
    RULE_an_stream_target_filter = 244
    RULE_an_stream_field_list = 245
    RULE_an_stream_field_name = 246
    RULE_an_flutter = 247
    RULE_an_flutter_child = 248
    RULE_an_html = 249
    RULE_an_html_descriptor = 250

    ruleNames =  [ "col_file", "page_imports", "model_imports", "page_import_statement", 
                   "model_import_statement", "import_statement", "import_source", 
                   "import_list", "import_item", "import_item_name", "import_item_alias", 
                   "import_item_all", "id_or_kw", "classname", "model_ref", 
                   "field_list_expr", "field_list_expr_field", "write_mode_expr", 
                   "python_code", "code_line", "code_block", "cs_annotation", 
                   "an_filer", "an_langs", "an_langs_list", "an_celery", 
                   "an_channels", "an_file", "an_file_name", "an_suit", 
                   "an_suit_app_name", "col", "col_str_expr", "col_header", 
                   "col_header_line_separator", "col_verbose_name", "verbose_name_part", 
                   "col_base_name", "col_name", "col_field", "col_field_expr_or_def", 
                   "col_field_custom", "col_field_extend", "col_field_extend_append", 
                   "wrong_field_type", "col_field_expr", "col_field_expr_marker", 
                   "col_feild_expr_code", "string_or_quoted", "col_field_help_text", 
                   "col_field_verbose_name", "col_field_name", "col_modifier", 
                   "col_field_def", "field_longtext", "field_html", "field_html_media", 
                   "field_float", "field_decimal", "field_date", "field_datetime", 
                   "field_create_time", "field_update_time", "field_file", 
                   "field_filer_file", "field_filer_folder", "field_text", 
                   "field_text_size", "field_text_choices", "field_text_choice", 
                   "field_text_choice_val", "field_text_choice_key", "field_int", 
                   "field_int_choices", "field_int_choice", "field_int_choice_val", 
                   "field_int_choice_key", "field_slug", "field_slug_ref_field", 
                   "field_slug_ref_field_id", "field_bool", "field_bool_default", 
                   "field_image", "filer_image_type", "field_image_sizes", 
                   "field_image_size", "field_image_size_dimensions", "field_image_size_name", 
                   "field_image_filters", "field_image_filter", "field_relation", 
                   "field_relation_type", "field_relation_target_ref", "field_relation_target_class", 
                   "field_relation_related_name", "model_annotation", "an_sortable", 
                   "an_sortable_field_name", "an_order", "an_order_fields", 
                   "an_rest", "an_rest_config", "an_rest_main_part", "an_rest_descriptor", 
                   "an_rest_i18n", "an_rest_query", "an_rest_on_create", 
                   "an_rest_filter_in", "an_rest_filter_out", "an_rest_read_only", 
                   "an_rest_user_field", "an_rest_fields", "an_rest_fields_write_mode", 
                   "an_rest_auth", "an_rest_auth_type", "an_rest_auth_token_model", 
                   "an_rest_auth_token_class", "an_rest_annotate", "an_rest_annotate_count", 
                   "an_rest_annotate_count_field", "an_rest_annotate_count_alias", 
                   "an_rest_inline", "an_rest_inline_decl", "an_rest_inline_name", 
                   "an_api", "an_api_all", "an_api_name", "an_clean", "an_pre_save", 
                   "an_post_save", "an_pre_delete", "an_post_delete", "an_m2m_changed", 
                   "an_mixin", "an_date_tree", "an_date_tree_field", "an_tree", 
                   "an_tree_poly", "an_admin", "an_admin_js", "an_admin_css", 
                   "an_admin_css_file_name", "an_admin_js_file_name", "an_admin_inlines", 
                   "an_admin_inline", "inline_name", "inline_type", "inline_extra", 
                   "inline_fields", "an_admin_tabs", "an_admin_tab", "tab_name", 
                   "tab_verbose_name", "an_admin_list", "an_admin_read_only", 
                   "an_admin_list_editable", "an_admin_list_filter", "an_admin_list_search", 
                   "an_admin_fields", "page", "page_header", "page_base", 
                   "page_alias", "page_alias_name", "page_template", "template_name", 
                   "file_name_part", "page_url", "url_part", "url_param", 
                   "url_segment", "url_segments", "page_name", "page_body", 
                   "page_code", "page_field", "page_field_name", "page_field_code", 
                   "page_function", "page_function_name", "page_function_args", 
                   "page_annotation", "an_react", "an_react_type", "an_react_descriptor", 
                   "an_markdown", "an_markdown_descriptor", "an_auth", "an_error", 
                   "an_error_code", "an_post", "an_crud_create", "an_crud", 
                   "an_crud_params", "an_crud_page_override", "an_crud_descriptor", 
                   "an_crud_next_page", "an_crud_next_page_event_name", 
                   "an_crud_next_page_url", "an_crud_next_page_url_val", 
                   "an_crud_target_model", "an_crud_target_filter", "an_crud_theme", 
                   "an_crud_url_prefix", "an_crud_url_prefix_val", "an_crud_link_suffix", 
                   "an_crud_link_suffix_val", "an_crud_item_name", "an_crud_object_expr", 
                   "an_crud_can_edit", "an_crud_block", "an_crud_pk_param", 
                   "an_crud_skip", "an_crud_skip_values", "an_crud_view_name", 
                   "an_crud_fields", "an_crud_fields_expr", "an_crud_field", 
                   "an_crud_field_spec", "an_crud_field_filter", "an_crud_list_fields", 
                   "an_crud_list_fields_expr", "an_crud_list_field", "an_crud_list_field_spec", 
                   "an_crud_edit", "an_crud_delete", "an_crud_detail", "an_menu", 
                   "an_menu_descriptor", "an_menu_item", "an_menu_target", 
                   "an_menu_item_code", "an_menu_item_args", "an_menu_item_arg", 
                   "an_menu_item_arg_key", "an_menu_item_arg_val", "an_menu_item_url", 
                   "an_menu_item_page", "an_menu_item_page_ref", "an_menu_label", 
                   "an_get", "an_stream", "an_stream_model", "an_stream_target_model", 
                   "an_stream_target_filter", "an_stream_field_list", "an_stream_field_name", 
                   "an_flutter", "an_flutter_child", "an_html", "an_html_descriptor" ]

    EOF = Token.EOF
    AN_FLUTTER=1
    AN_FILE=2
    AN_STREAM=3
    AN_CHANNELS=4
    AN_GET=5
    AN_MENU=6
    AN_CRUD=7
    AN_CRUD_DETAIL=8
    AN_CRUD_DELETE=9
    AN_CRUD_EDIT=10
    AN_CRUD_CREATE=11
    AN_CELERY=12
    AN_POST=13
    AN_ERROR=14
    AN_AUTH=15
    AN_MARKDOWN=16
    AN_REACT=17
    AN_REACT_CLIENT=18
    AN_REACT_SERVER=19
    AN_HTML=20
    AN_TREE=21
    AN_DATE_TREE=22
    AN_MIXIN=23
    AN_M2M_CHANGED=24
    AN_POST_DELETE=25
    AN_PRE_DELETE=26
    AN_POST_SAVE=27
    AN_PRE_SAVE=28
    AN_CLEAN=29
    AN_API=30
    AN_REST=31
    AN_ORDER=32
    AN_SORTABLE=33
    AN_LANGS=34
    AN_FILER=35
    AN_ADMIN=36
    AN_SUIT=37
    WRITE_MODE=38
    BOOL=39
    KW_THEME=40
    KW_CHILD=41
    KW_FILTER_OUT=42
    KW_FILTER_IN=43
    KW_PAGE=44
    KW_LINK_SUFFIX=45
    KW_URL_PREFIX=46
    KW_CAN_EDIT=47
    KW_OBJECT_EXPR=48
    KW_BLOCK=49
    KW_ITEM_NAME=50
    KW_PK_PARAM=51
    KW_LIST_FIELDS=52
    KW_DELETE=53
    KW_EDIT=54
    KW_CREATE=55
    KW_DETAIL=56
    KW_SKIP=57
    KW_FROM=58
    KW_POLY_LIST=59
    KW_CSS=60
    KW_JS=61
    KW_INLINE_TYPE=62
    KW_AUTH_TYPE=63
    KW_INLINE=64
    KW_TYPE=65
    KW_USER_FIELD=66
    KW_ANNOTATE=67
    KW_ON_CREATE=68
    KW_QUERY=69
    KW_AUTH=70
    KW_COUNT=71
    KW_I18N=72
    KW_EXTRA=73
    KW_TABS=74
    KW_LIST=75
    KW_READ_ONLY=76
    KW_LIST_EDITABLE=77
    KW_LIST_FILTER=78
    KW_LIST_SEARCH=79
    KW_FIELDS=80
    KW_IMPORT=81
    KW_AS=82
    COL_FIELD_TYPE_LONGTEXT=83
    COL_FIELD_TYPE_HTML=84
    COL_FIELD_TYPE_HTML_MEDIA=85
    COL_FIELD_TYPE_FLOAT=86
    COL_FIELD_TYPE_DECIMAL=87
    COL_FIELD_TYPE_DATE=88
    COL_FIELD_TYPE_DATETIME=89
    COL_FIELD_TYPE_CREATE_TIME=90
    COL_FIELD_TYPE_UPDATE_TIME=91
    COL_FIELD_TYPE_IMAGE=92
    COL_FIELD_TYPE_FILE=93
    COL_FIELD_TYPE_FILER_IMAGE=94
    COL_FIELD_TYPE_FILER_FILE=95
    COL_FIELD_TYPE_FILER_FOLDER=96
    COL_FIELD_TYPE_FILER_IMAGE_FOLDER=97
    COL_FIELD_TYPE_TEXT=98
    COL_FIELD_TYPE_INT=99
    COL_FIELD_TYPE_SLUG=100
    COL_FIELD_TYPE_BOOL=101
    COL_FIELD_TYPE_ONE=102
    COL_FIELD_TYPE_ONE2ONE=103
    COL_FIELD_TYPE_MANY=104
    COL_FIELD_CHOICES=105
    NL=106
    ID=107
    DIGIT=108
    SIZE2D=109
    LT=110
    GT=111
    COLON=112
    EXCLUDE=113
    BRACE_OPEN=114
    BRACE_CLOSE=115
    SQ_BRACE_OPEN=116
    SQ_BRACE_CLOSE=117
    QUESTION_MARK=118
    UNDERSCORE=119
    DASH=120
    COMA=121
    DOT=122
    HASH=123
    SLASH=124
    EQUALS=125
    DOLLAR=126
    AMP=127
    EXCLAM=128
    STAR=129
    APPROX=130
    PIPE=131
    STRING_DQ=132
    STRING_SQ=133
    COMMENT_LINE=134
    COMMENT_BLOCK=135
    UNICODE=136
    WS=137
    COL_FIELD_CALCULATED=138
    ASSIGN=139
    ASSIGN_STATIC=140
    CODE_BLOCK=141
    ERRCHAR=142
    PYTHON_CODE=143
    PYTHON_LINE_ERRCHAR=144
    PYTHON_LINE_END=145
    PYTHON_EXPR_ERRCHAR=146
    PYTHON_LINE_NL=147

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
            self.state = 505
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 502
                    self.match(ZmeiLangParser.NL) 
                self.state = 507
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 511
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 508
                    self.cs_annotation() 
                self.state = 513
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 517
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 514
                    self.match(ZmeiLangParser.NL) 
                self.state = 519
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 528
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 521
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.KW_FROM or _la==ZmeiLangParser.KW_IMPORT:
                    self.state = 520
                    self.page_imports()


                self.state = 524 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 523
                    self.page()
                    self.state = 526 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZmeiLangParser.SQ_BRACE_OPEN):
                        break



            self.state = 533
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 530
                    self.match(ZmeiLangParser.NL) 
                self.state = 535
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 544
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.KW_FROM or _la==ZmeiLangParser.KW_IMPORT or _la==ZmeiLangParser.HASH:
                self.state = 537
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.KW_FROM or _la==ZmeiLangParser.KW_IMPORT:
                    self.state = 536
                    self.model_imports()


                self.state = 540 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 539
                    self.col()
                    self.state = 542 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZmeiLangParser.HASH):
                        break



            self.state = 549
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 546
                self.match(ZmeiLangParser.NL)
                self.state = 551
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 552
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
            self.state = 555 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 554
                self.page_import_statement()
                self.state = 557 
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
            self.state = 560 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 559
                self.model_import_statement()
                self.state = 562 
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
            self.state = 564
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
            self.state = 566
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
            self.state = 570
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.KW_FROM:
                self.state = 568
                self.match(ZmeiLangParser.KW_FROM)
                self.state = 569
                self.import_source()


            self.state = 572
            self.match(ZmeiLangParser.KW_IMPORT)
            self.state = 573
            self.import_list()
            self.state = 575 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 574
                self.match(ZmeiLangParser.NL)
                self.state = 577 
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
            self.state = 580
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 579
                self.match(ZmeiLangParser.DOT)


            self.state = 582
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
            self.state = 584
            self.import_item()
            self.state = 589
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 585
                self.match(ZmeiLangParser.COMA)
                self.state = 586
                self.import_item()
                self.state = 591
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
            self.state = 598
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 592
                self.import_item_name()
                self.state = 595
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.KW_AS:
                    self.state = 593
                    self.match(ZmeiLangParser.KW_AS)
                    self.state = 594
                    self.import_item_alias()


                pass
            elif token in [ZmeiLangParser.STAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 597
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
            self.state = 600
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
            self.state = 602
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
            self.state = 604
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

        def KW_THEME(self):
            return self.getToken(ZmeiLangParser.KW_THEME, 0)

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

        def KW_INLINE_TYPE(self):
            return self.getToken(ZmeiLangParser.KW_INLINE_TYPE, 0)

        def KW_AUTH_TYPE(self):
            return self.getToken(ZmeiLangParser.KW_AUTH_TYPE, 0)

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
            self.state = 606
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.WRITE_MODE) | (1 << ZmeiLangParser.BOOL) | (1 << ZmeiLangParser.KW_THEME) | (1 << ZmeiLangParser.KW_CHILD) | (1 << ZmeiLangParser.KW_FILTER_OUT) | (1 << ZmeiLangParser.KW_FILTER_IN) | (1 << ZmeiLangParser.KW_PAGE) | (1 << ZmeiLangParser.KW_LINK_SUFFIX) | (1 << ZmeiLangParser.KW_URL_PREFIX) | (1 << ZmeiLangParser.KW_CAN_EDIT) | (1 << ZmeiLangParser.KW_OBJECT_EXPR) | (1 << ZmeiLangParser.KW_BLOCK) | (1 << ZmeiLangParser.KW_ITEM_NAME) | (1 << ZmeiLangParser.KW_PK_PARAM) | (1 << ZmeiLangParser.KW_LIST_FIELDS) | (1 << ZmeiLangParser.KW_DELETE) | (1 << ZmeiLangParser.KW_EDIT) | (1 << ZmeiLangParser.KW_CREATE) | (1 << ZmeiLangParser.KW_DETAIL) | (1 << ZmeiLangParser.KW_SKIP) | (1 << ZmeiLangParser.KW_FROM) | (1 << ZmeiLangParser.KW_POLY_LIST) | (1 << ZmeiLangParser.KW_CSS) | (1 << ZmeiLangParser.KW_JS) | (1 << ZmeiLangParser.KW_INLINE_TYPE) | (1 << ZmeiLangParser.KW_AUTH_TYPE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ZmeiLangParser.KW_INLINE - 64)) | (1 << (ZmeiLangParser.KW_TYPE - 64)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 64)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 64)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 64)) | (1 << (ZmeiLangParser.KW_QUERY - 64)) | (1 << (ZmeiLangParser.KW_AUTH - 64)) | (1 << (ZmeiLangParser.KW_COUNT - 64)) | (1 << (ZmeiLangParser.KW_I18N - 64)) | (1 << (ZmeiLangParser.KW_EXTRA - 64)) | (1 << (ZmeiLangParser.KW_TABS - 64)) | (1 << (ZmeiLangParser.KW_LIST - 64)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 64)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 64)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 64)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 64)) | (1 << (ZmeiLangParser.KW_FIELDS - 64)) | (1 << (ZmeiLangParser.KW_IMPORT - 64)) | (1 << (ZmeiLangParser.KW_AS - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 64)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 64)) | (1 << (ZmeiLangParser.ID - 64)))) != 0)):
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
            self.state = 608
            self.id_or_kw()
            self.state = 613
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.DOT:
                self.state = 609
                self.match(ZmeiLangParser.DOT)
                self.state = 610
                self.id_or_kw()
                self.state = 615
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
            self.state = 616
            self.match(ZmeiLangParser.HASH)
            self.state = 620
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 617
                self.id_or_kw()
                self.state = 618
                self.match(ZmeiLangParser.DOT)


            self.state = 622
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
            self.state = 647
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.DOT, ZmeiLangParser.STAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 625
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.DOT:
                    self.state = 624
                    self.match(ZmeiLangParser.DOT)


                self.state = 627
                self.match(ZmeiLangParser.STAR)
                self.state = 633
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 628
                        self.match(ZmeiLangParser.COMA)
                        self.state = 629
                        self.match(ZmeiLangParser.EXCLUDE)
                        self.state = 630
                        self.field_list_expr_field() 
                    self.state = 635
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

                pass
            elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 636
                self.id_or_kw()
                self.state = 644
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 637
                        self.match(ZmeiLangParser.COMA)
                        self.state = 639
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==ZmeiLangParser.EXCLUDE:
                            self.state = 638
                            self.match(ZmeiLangParser.EXCLUDE)


                        self.state = 641
                        self.field_list_expr_field() 
                    self.state = 646
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
            self.state = 650
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.STAR:
                self.state = 649
                self.match(ZmeiLangParser.STAR)


            self.state = 652
            self.id_or_kw()
            self.state = 654
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.STAR:
                self.state = 653
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
            self.state = 656
            self.match(ZmeiLangParser.SQ_BRACE_OPEN)
            self.state = 657
            self.match(ZmeiLangParser.WRITE_MODE)
            self.state = 658
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
            self.state = 662
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.CODE_BLOCK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 660
                self.code_block()
                pass
            elif token in [ZmeiLangParser.ASSIGN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 661
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
            self.state = 664
            self.match(ZmeiLangParser.ASSIGN)
            self.state = 665
            self.match(ZmeiLangParser.PYTHON_CODE)
            self.state = 666
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
            self.state = 668
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


        def an_file(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_fileContext,0)


        def an_channels(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_channelsContext,0)


        def an_celery(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_celeryContext,0)


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
            self.state = 676
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.AN_SUIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 670
                self.an_suit()
                pass
            elif token in [ZmeiLangParser.AN_FILE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 671
                self.an_file()
                pass
            elif token in [ZmeiLangParser.AN_CHANNELS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 672
                self.an_channels()
                pass
            elif token in [ZmeiLangParser.AN_CELERY]:
                self.enterOuterAlt(localctx, 4)
                self.state = 673
                self.an_celery()
                pass
            elif token in [ZmeiLangParser.AN_LANGS]:
                self.enterOuterAlt(localctx, 5)
                self.state = 674
                self.an_langs()
                pass
            elif token in [ZmeiLangParser.NL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 675
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
        self.enterRule(localctx, 44, self.RULE_an_filer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 678
            self.match(ZmeiLangParser.AN_FILER)
            self.state = 681
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 679
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 680
                self.match(ZmeiLangParser.BRACE_CLOSE)


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
        self.enterRule(localctx, 46, self.RULE_an_langs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 683
            self.match(ZmeiLangParser.AN_LANGS)
            self.state = 684
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 685
            self.an_langs_list()
            self.state = 686
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
        self.enterRule(localctx, 48, self.RULE_an_langs_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 688
            self.match(ZmeiLangParser.ID)
            self.state = 693
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 689
                self.match(ZmeiLangParser.COMA)
                self.state = 690
                self.match(ZmeiLangParser.ID)
                self.state = 695
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 50, self.RULE_an_celery)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 696
            self.match(ZmeiLangParser.AN_CELERY)
            self.state = 699
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 697
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 698
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
        self.enterRule(localctx, 52, self.RULE_an_channels)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 701
            self.match(ZmeiLangParser.AN_CHANNELS)
            self.state = 704
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 702
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 703
                self.match(ZmeiLangParser.BRACE_CLOSE)


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
        self.enterRule(localctx, 54, self.RULE_an_file)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 706
            self.match(ZmeiLangParser.AN_FILE)
            self.state = 707
            self.an_file_name()
            self.state = 708
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
        self.enterRule(localctx, 56, self.RULE_an_file_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 710
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
        self.enterRule(localctx, 58, self.RULE_an_suit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 712
            self.match(ZmeiLangParser.AN_SUIT)
            self.state = 717
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 713
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 714
                self.an_suit_app_name()
                self.state = 715
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
        self.enterRule(localctx, 60, self.RULE_an_suit_app_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 719
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
        self.enterRule(localctx, 62, self.RULE_col)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 721
            self.col_header()
            self.state = 723
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 722
                self.col_str_expr()


            self.state = 728
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 725
                    self.match(ZmeiLangParser.NL) 
                self.state = 730
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

            self.state = 734
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 38)) & ~0x3f) == 0 and ((1 << (_la - 38)) & ((1 << (ZmeiLangParser.WRITE_MODE - 38)) | (1 << (ZmeiLangParser.BOOL - 38)) | (1 << (ZmeiLangParser.KW_THEME - 38)) | (1 << (ZmeiLangParser.KW_CHILD - 38)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 38)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 38)) | (1 << (ZmeiLangParser.KW_PAGE - 38)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 38)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 38)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 38)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 38)) | (1 << (ZmeiLangParser.KW_BLOCK - 38)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 38)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 38)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 38)) | (1 << (ZmeiLangParser.KW_DELETE - 38)) | (1 << (ZmeiLangParser.KW_EDIT - 38)) | (1 << (ZmeiLangParser.KW_CREATE - 38)) | (1 << (ZmeiLangParser.KW_DETAIL - 38)) | (1 << (ZmeiLangParser.KW_SKIP - 38)) | (1 << (ZmeiLangParser.KW_FROM - 38)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 38)) | (1 << (ZmeiLangParser.KW_CSS - 38)) | (1 << (ZmeiLangParser.KW_JS - 38)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE - 38)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE - 38)) | (1 << (ZmeiLangParser.KW_INLINE - 38)) | (1 << (ZmeiLangParser.KW_TYPE - 38)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 38)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 38)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 38)) | (1 << (ZmeiLangParser.KW_QUERY - 38)) | (1 << (ZmeiLangParser.KW_AUTH - 38)) | (1 << (ZmeiLangParser.KW_COUNT - 38)) | (1 << (ZmeiLangParser.KW_I18N - 38)) | (1 << (ZmeiLangParser.KW_EXTRA - 38)) | (1 << (ZmeiLangParser.KW_TABS - 38)) | (1 << (ZmeiLangParser.KW_LIST - 38)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 38)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 38)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 38)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 38)) | (1 << (ZmeiLangParser.KW_FIELDS - 38)) | (1 << (ZmeiLangParser.KW_IMPORT - 38)) | (1 << (ZmeiLangParser.KW_AS - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 38)))) != 0) or ((((_la - 102)) & ~0x3f) == 0 and ((1 << (_la - 102)) & ((1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 102)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 102)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 102)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 102)) | (1 << (ZmeiLangParser.ID - 102)) | (1 << (ZmeiLangParser.EQUALS - 102)) | (1 << (ZmeiLangParser.DOLLAR - 102)) | (1 << (ZmeiLangParser.AMP - 102)) | (1 << (ZmeiLangParser.EXCLAM - 102)) | (1 << (ZmeiLangParser.STAR - 102)) | (1 << (ZmeiLangParser.APPROX - 102)))) != 0):
                self.state = 731
                self.col_field()
                self.state = 736
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 740
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 737
                    self.match(ZmeiLangParser.NL) 
                self.state = 742
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

            self.state = 746
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 743
                    self.model_annotation() 
                self.state = 748
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

            self.state = 752
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 749
                    self.match(ZmeiLangParser.NL) 
                self.state = 754
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

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
        self.enterRule(localctx, 64, self.RULE_col_str_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 755
            self.match(ZmeiLangParser.EQUALS)
            self.state = 756
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.STRING_DQ or _la==ZmeiLangParser.STRING_SQ):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 763
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.NL]:
                self.state = 758 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 757
                        self.match(ZmeiLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 760 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

                pass
            elif token in [ZmeiLangParser.EOF]:
                self.state = 762
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
        self.enterRule(localctx, 66, self.RULE_col_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 765
            self.match(ZmeiLangParser.HASH)
            self.state = 767
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 766
                self.col_base_name()


            self.state = 769
            self.col_name()
            self.state = 771
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COLON:
                self.state = 770
                self.col_verbose_name()


            self.state = 773
            self.col_header_line_separator()
            self.state = 774
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
        self.enterRule(localctx, 68, self.RULE_col_header_line_separator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 776
            self.match(ZmeiLangParser.NL)
            self.state = 777
            self.match(ZmeiLangParser.DASH)
            self.state = 778
            self.match(ZmeiLangParser.DASH)
            self.state = 780 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 779
                self.match(ZmeiLangParser.DASH)
                self.state = 782 
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
        self.enterRule(localctx, 70, self.RULE_col_verbose_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 784
            self.match(ZmeiLangParser.COLON)
            self.state = 785
            self.verbose_name_part()
            self.state = 788
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.SLASH:
                self.state = 786
                self.match(ZmeiLangParser.SLASH)
                self.state = 787
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
        self.enterRule(localctx, 72, self.RULE_verbose_name_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 793
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                self.state = 790
                self.id_or_kw()
                pass
            elif token in [ZmeiLangParser.STRING_DQ]:
                self.state = 791
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.state = 792
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
        self.enterRule(localctx, 74, self.RULE_col_base_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 795
            self.id_or_kw()
            self.state = 800
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.DASH]:
                self.state = 796
                self.match(ZmeiLangParser.DASH)
                self.state = 797
                self.match(ZmeiLangParser.GT)
                pass
            elif token in [ZmeiLangParser.APPROX]:
                self.state = 798
                self.match(ZmeiLangParser.APPROX)
                self.state = 799
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
        self.enterRule(localctx, 76, self.RULE_col_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 802
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
        self.enterRule(localctx, 78, self.RULE_col_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 807
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 125)) & ~0x3f) == 0 and ((1 << (_la - 125)) & ((1 << (ZmeiLangParser.EQUALS - 125)) | (1 << (ZmeiLangParser.DOLLAR - 125)) | (1 << (ZmeiLangParser.AMP - 125)) | (1 << (ZmeiLangParser.EXCLAM - 125)) | (1 << (ZmeiLangParser.STAR - 125)) | (1 << (ZmeiLangParser.APPROX - 125)))) != 0):
                self.state = 804
                self.col_modifier()
                self.state = 809
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 810
            self.col_field_name()
            self.state = 812
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 112)) & ~0x3f) == 0 and ((1 << (_la - 112)) & ((1 << (ZmeiLangParser.COLON - 112)) | (1 << (ZmeiLangParser.ASSIGN - 112)) | (1 << (ZmeiLangParser.ASSIGN_STATIC - 112)))) != 0):
                self.state = 811
                self.col_field_expr_or_def()


            self.state = 815
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.SLASH:
                self.state = 814
                self.col_field_verbose_name()


            self.state = 818
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.QUESTION_MARK:
                self.state = 817
                self.col_field_help_text()


            self.state = 826
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.NL]:
                self.state = 821 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 820
                        self.match(ZmeiLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 823 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,53,self._ctx)

                pass
            elif token in [ZmeiLangParser.EOF]:
                self.state = 825
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
        self.enterRule(localctx, 80, self.RULE_col_field_expr_or_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 840
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.state = 828
                self.match(ZmeiLangParser.COLON)
                self.state = 830
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.CODE_BLOCK:
                    self.state = 829
                    self.col_field_custom()


                pass

            elif la_ == 2:
                self.state = 832
                self.match(ZmeiLangParser.COLON)
                self.state = 833
                self.col_field_def()
                self.state = 835
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.DOT or _la==ZmeiLangParser.CODE_BLOCK:
                    self.state = 834
                    self.col_field_extend()


                pass

            elif la_ == 3:
                self.state = 837
                self.match(ZmeiLangParser.COLON)
                self.state = 838
                self.wrong_field_type()
                pass

            elif la_ == 4:
                self.state = 839
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
        self.enterRule(localctx, 82, self.RULE_col_field_custom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 842
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
        self.enterRule(localctx, 84, self.RULE_col_field_extend)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 845
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 844
                self.col_field_extend_append()


            self.state = 847
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
        self.enterRule(localctx, 86, self.RULE_col_field_extend_append)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 849
            self.match(ZmeiLangParser.DOT)
            self.state = 850
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
        self.enterRule(localctx, 88, self.RULE_wrong_field_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 852
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
        self.enterRule(localctx, 90, self.RULE_col_field_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 854
            self.col_field_expr_marker()
            self.state = 855
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
        self.enterRule(localctx, 92, self.RULE_col_field_expr_marker)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 857
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
        self.enterRule(localctx, 94, self.RULE_col_feild_expr_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 859
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
        self.enterRule(localctx, 96, self.RULE_string_or_quoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 868
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                self.state = 862 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 861
                    self.id_or_kw()
                    self.state = 864 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.WRITE_MODE) | (1 << ZmeiLangParser.BOOL) | (1 << ZmeiLangParser.KW_THEME) | (1 << ZmeiLangParser.KW_CHILD) | (1 << ZmeiLangParser.KW_FILTER_OUT) | (1 << ZmeiLangParser.KW_FILTER_IN) | (1 << ZmeiLangParser.KW_PAGE) | (1 << ZmeiLangParser.KW_LINK_SUFFIX) | (1 << ZmeiLangParser.KW_URL_PREFIX) | (1 << ZmeiLangParser.KW_CAN_EDIT) | (1 << ZmeiLangParser.KW_OBJECT_EXPR) | (1 << ZmeiLangParser.KW_BLOCK) | (1 << ZmeiLangParser.KW_ITEM_NAME) | (1 << ZmeiLangParser.KW_PK_PARAM) | (1 << ZmeiLangParser.KW_LIST_FIELDS) | (1 << ZmeiLangParser.KW_DELETE) | (1 << ZmeiLangParser.KW_EDIT) | (1 << ZmeiLangParser.KW_CREATE) | (1 << ZmeiLangParser.KW_DETAIL) | (1 << ZmeiLangParser.KW_SKIP) | (1 << ZmeiLangParser.KW_FROM) | (1 << ZmeiLangParser.KW_POLY_LIST) | (1 << ZmeiLangParser.KW_CSS) | (1 << ZmeiLangParser.KW_JS) | (1 << ZmeiLangParser.KW_INLINE_TYPE) | (1 << ZmeiLangParser.KW_AUTH_TYPE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ZmeiLangParser.KW_INLINE - 64)) | (1 << (ZmeiLangParser.KW_TYPE - 64)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 64)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 64)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 64)) | (1 << (ZmeiLangParser.KW_QUERY - 64)) | (1 << (ZmeiLangParser.KW_AUTH - 64)) | (1 << (ZmeiLangParser.KW_COUNT - 64)) | (1 << (ZmeiLangParser.KW_I18N - 64)) | (1 << (ZmeiLangParser.KW_EXTRA - 64)) | (1 << (ZmeiLangParser.KW_TABS - 64)) | (1 << (ZmeiLangParser.KW_LIST - 64)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 64)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 64)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 64)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 64)) | (1 << (ZmeiLangParser.KW_FIELDS - 64)) | (1 << (ZmeiLangParser.KW_IMPORT - 64)) | (1 << (ZmeiLangParser.KW_AS - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 64)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 64)) | (1 << (ZmeiLangParser.ID - 64)))) != 0)):
                        break

                pass
            elif token in [ZmeiLangParser.STRING_DQ]:
                self.state = 866
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.state = 867
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
        self.enterRule(localctx, 98, self.RULE_col_field_help_text)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 870
            self.match(ZmeiLangParser.QUESTION_MARK)
            self.state = 871
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
        self.enterRule(localctx, 100, self.RULE_col_field_verbose_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 873
            self.match(ZmeiLangParser.SLASH)
            self.state = 874
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
        self.enterRule(localctx, 102, self.RULE_col_field_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 876
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
        self.enterRule(localctx, 104, self.RULE_col_modifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 878
            _la = self._input.LA(1)
            if not(((((_la - 125)) & ~0x3f) == 0 and ((1 << (_la - 125)) & ((1 << (ZmeiLangParser.EQUALS - 125)) | (1 << (ZmeiLangParser.DOLLAR - 125)) | (1 << (ZmeiLangParser.AMP - 125)) | (1 << (ZmeiLangParser.EXCLAM - 125)) | (1 << (ZmeiLangParser.STAR - 125)) | (1 << (ZmeiLangParser.APPROX - 125)))) != 0)):
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
        self.enterRule(localctx, 106, self.RULE_col_field_def)
        try:
            self.state = 898
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 880
                self.field_longtext()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 881
                self.field_html_media()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_HTML]:
                self.enterOuterAlt(localctx, 3)
                self.state = 882
                self.field_html()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_FLOAT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 883
                self.field_float()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_DECIMAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 884
                self.field_decimal()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_DATE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 885
                self.field_date()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_DATETIME]:
                self.enterOuterAlt(localctx, 7)
                self.state = 886
                self.field_datetime()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME]:
                self.enterOuterAlt(localctx, 8)
                self.state = 887
                self.field_create_time()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME]:
                self.enterOuterAlt(localctx, 9)
                self.state = 888
                self.field_update_time()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_TEXT]:
                self.enterOuterAlt(localctx, 10)
                self.state = 889
                self.field_text()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_INT]:
                self.enterOuterAlt(localctx, 11)
                self.state = 890
                self.field_int()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_SLUG]:
                self.enterOuterAlt(localctx, 12)
                self.state = 891
                self.field_slug()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_BOOL]:
                self.enterOuterAlt(localctx, 13)
                self.state = 892
                self.field_bool()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY]:
                self.enterOuterAlt(localctx, 14)
                self.state = 893
                self.field_relation()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER]:
                self.enterOuterAlt(localctx, 15)
                self.state = 894
                self.field_image()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_FILE]:
                self.enterOuterAlt(localctx, 16)
                self.state = 895
                self.field_file()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE]:
                self.enterOuterAlt(localctx, 17)
                self.state = 896
                self.field_filer_file()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER]:
                self.enterOuterAlt(localctx, 18)
                self.state = 897
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
        self.enterRule(localctx, 108, self.RULE_field_longtext)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 900
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
        self.enterRule(localctx, 110, self.RULE_field_html)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 902
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
        self.enterRule(localctx, 112, self.RULE_field_html_media)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 904
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
        self.enterRule(localctx, 114, self.RULE_field_float)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 906
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
        self.enterRule(localctx, 116, self.RULE_field_decimal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 908
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
        self.enterRule(localctx, 118, self.RULE_field_date)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 910
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
        self.enterRule(localctx, 120, self.RULE_field_datetime)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 912
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
        self.enterRule(localctx, 122, self.RULE_field_create_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 914
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
        self.enterRule(localctx, 124, self.RULE_field_update_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 916
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
        self.enterRule(localctx, 126, self.RULE_field_file)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 918
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
        self.enterRule(localctx, 128, self.RULE_field_filer_file)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 920
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
        self.enterRule(localctx, 130, self.RULE_field_filer_folder)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 922
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
        self.enterRule(localctx, 132, self.RULE_field_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 924
            self.match(ZmeiLangParser.COL_FIELD_TYPE_TEXT)
            self.state = 933
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 925
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 926
                self.field_text_size()
                self.state = 929
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.COMA:
                    self.state = 927
                    self.match(ZmeiLangParser.COMA)
                    self.state = 928
                    self.field_text_choices()


                self.state = 931
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
        self.enterRule(localctx, 134, self.RULE_field_text_size)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 935
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
        self.enterRule(localctx, 136, self.RULE_field_text_choices)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 937
            self.match(ZmeiLangParser.COL_FIELD_CHOICES)
            self.state = 938
            self.match(ZmeiLangParser.EQUALS)
            self.state = 939
            self.field_text_choice()
            self.state = 944
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 940
                self.match(ZmeiLangParser.COMA)
                self.state = 941
                self.field_text_choice()
                self.state = 946
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
        self.enterRule(localctx, 138, self.RULE_field_text_choice)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 948
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                self.state = 947
                self.field_text_choice_key()


            self.state = 950
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
        self.enterRule(localctx, 140, self.RULE_field_text_choice_val)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 955
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                self.state = 952
                self.id_or_kw()
                pass
            elif token in [ZmeiLangParser.STRING_DQ]:
                self.state = 953
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.state = 954
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
        self.enterRule(localctx, 142, self.RULE_field_text_choice_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 957
            self.id_or_kw()
            self.state = 958
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
        self.enterRule(localctx, 144, self.RULE_field_int)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 960
            self.match(ZmeiLangParser.COL_FIELD_TYPE_INT)
            self.state = 965
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 961
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 962
                self.field_int_choices()
                self.state = 963
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
        self.enterRule(localctx, 146, self.RULE_field_int_choices)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 967
            self.match(ZmeiLangParser.COL_FIELD_CHOICES)
            self.state = 968
            self.match(ZmeiLangParser.EQUALS)
            self.state = 969
            self.field_int_choice()
            self.state = 974
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 970
                self.match(ZmeiLangParser.COMA)
                self.state = 971
                self.field_int_choice()
                self.state = 976
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
        self.enterRule(localctx, 148, self.RULE_field_int_choice)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 978
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DIGIT:
                self.state = 977
                self.field_int_choice_key()


            self.state = 980
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
        self.enterRule(localctx, 150, self.RULE_field_int_choice_val)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 985
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                self.state = 982
                self.id_or_kw()
                pass
            elif token in [ZmeiLangParser.STRING_DQ]:
                self.state = 983
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.state = 984
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
        self.enterRule(localctx, 152, self.RULE_field_int_choice_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 987
            self.match(ZmeiLangParser.DIGIT)
            self.state = 988
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
        self.enterRule(localctx, 154, self.RULE_field_slug)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 990
            self.match(ZmeiLangParser.COL_FIELD_TYPE_SLUG)
            self.state = 991
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 992
            self.field_slug_ref_field()
            self.state = 993
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
        self.enterRule(localctx, 156, self.RULE_field_slug_ref_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 995
            self.field_slug_ref_field_id()
            self.state = 1000
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 996
                self.match(ZmeiLangParser.COMA)
                self.state = 997
                self.field_slug_ref_field_id()
                self.state = 1002
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
        self.enterRule(localctx, 158, self.RULE_field_slug_ref_field_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1003
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
        self.enterRule(localctx, 160, self.RULE_field_bool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1005
            self.match(ZmeiLangParser.COL_FIELD_TYPE_BOOL)
            self.state = 1010
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1006
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1007
                self.field_bool_default()
                self.state = 1008
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
        self.enterRule(localctx, 162, self.RULE_field_bool_default)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1012
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
        self.enterRule(localctx, 164, self.RULE_field_image)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1014
            self.filer_image_type()
            self.state = 1019
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1015
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1016
                self.field_image_sizes()
                self.state = 1017
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
        self.enterRule(localctx, 166, self.RULE_filer_image_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1021
            _la = self._input.LA(1)
            if not(((((_la - 92)) & ~0x3f) == 0 and ((1 << (_la - 92)) & ((1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 92)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 92)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 92)))) != 0)):
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
        self.enterRule(localctx, 168, self.RULE_field_image_sizes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1023
            self.field_image_size()
            self.state = 1028
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 1024
                self.match(ZmeiLangParser.COMA)
                self.state = 1025
                self.field_image_size()
                self.state = 1030
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
        self.enterRule(localctx, 170, self.RULE_field_image_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1031
            self.field_image_size_name()
            self.state = 1032
            self.field_image_size_dimensions()
            self.state = 1033
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
        self.enterRule(localctx, 172, self.RULE_field_image_size_dimensions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1035
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
        self.enterRule(localctx, 174, self.RULE_field_image_size_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1037
            self.id_or_kw()
            self.state = 1038
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
        self.enterRule(localctx, 176, self.RULE_field_image_filters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1043
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.PIPE:
                self.state = 1040
                self.field_image_filter()
                self.state = 1045
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
        self.enterRule(localctx, 178, self.RULE_field_image_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1046
            self.match(ZmeiLangParser.PIPE)
            self.state = 1047
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
        self.enterRule(localctx, 180, self.RULE_field_relation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1049
            self.field_relation_type()
            self.state = 1050
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1053
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.HASH]:
                self.state = 1051
                self.field_relation_target_ref()
                pass
            elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                self.state = 1052
                self.field_relation_target_class()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 1056
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DASH:
                self.state = 1055
                self.field_relation_related_name()


            self.state = 1058
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
        self.enterRule(localctx, 182, self.RULE_field_relation_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1060
            _la = self._input.LA(1)
            if not(((((_la - 102)) & ~0x3f) == 0 and ((1 << (_la - 102)) & ((1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 102)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 102)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 102)))) != 0)):
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
        self.enterRule(localctx, 184, self.RULE_field_relation_target_ref)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1062
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
        self.enterRule(localctx, 186, self.RULE_field_relation_target_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1064
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
        self.enterRule(localctx, 188, self.RULE_field_relation_related_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1066
            self.match(ZmeiLangParser.DASH)
            self.state = 1067
            self.match(ZmeiLangParser.GT)
            self.state = 1068
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


        def an_tree(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_treeContext,0)


        def an_date_tree(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_date_treeContext,0)


        def an_mixin(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_mixinContext,0)


        def an_m2m_changed(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_m2m_changedContext,0)


        def an_post_delete(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_post_deleteContext,0)


        def an_pre_delete(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_pre_deleteContext,0)


        def an_post_save(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_post_saveContext,0)


        def an_pre_save(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_pre_saveContext,0)


        def an_clean(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_cleanContext,0)


        def an_api(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_apiContext,0)


        def an_rest(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_restContext,0)


        def an_order(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_orderContext,0)


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
        self.enterRule(localctx, 190, self.RULE_model_annotation)
        try:
            self.state = 1085
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.AN_ADMIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1070
                self.an_admin()
                pass
            elif token in [ZmeiLangParser.AN_TREE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1071
                self.an_tree()
                pass
            elif token in [ZmeiLangParser.AN_DATE_TREE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1072
                self.an_date_tree()
                pass
            elif token in [ZmeiLangParser.AN_MIXIN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1073
                self.an_mixin()
                pass
            elif token in [ZmeiLangParser.AN_M2M_CHANGED]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1074
                self.an_m2m_changed()
                pass
            elif token in [ZmeiLangParser.AN_POST_DELETE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 1075
                self.an_post_delete()
                pass
            elif token in [ZmeiLangParser.AN_PRE_DELETE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 1076
                self.an_pre_delete()
                pass
            elif token in [ZmeiLangParser.AN_POST_SAVE]:
                self.enterOuterAlt(localctx, 8)
                self.state = 1077
                self.an_post_save()
                pass
            elif token in [ZmeiLangParser.AN_PRE_SAVE]:
                self.enterOuterAlt(localctx, 9)
                self.state = 1078
                self.an_pre_save()
                pass
            elif token in [ZmeiLangParser.AN_CLEAN]:
                self.enterOuterAlt(localctx, 10)
                self.state = 1079
                self.an_clean()
                pass
            elif token in [ZmeiLangParser.AN_API]:
                self.enterOuterAlt(localctx, 11)
                self.state = 1080
                self.an_api()
                pass
            elif token in [ZmeiLangParser.AN_REST]:
                self.enterOuterAlt(localctx, 12)
                self.state = 1081
                self.an_rest()
                pass
            elif token in [ZmeiLangParser.AN_ORDER]:
                self.enterOuterAlt(localctx, 13)
                self.state = 1082
                self.an_order()
                pass
            elif token in [ZmeiLangParser.AN_SORTABLE]:
                self.enterOuterAlt(localctx, 14)
                self.state = 1083
                self.an_sortable()
                pass
            elif token in [ZmeiLangParser.NL]:
                self.enterOuterAlt(localctx, 15)
                self.state = 1084
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
        self.enterRule(localctx, 192, self.RULE_an_sortable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1087
            self.match(ZmeiLangParser.AN_SORTABLE)
            self.state = 1088
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1089
            self.an_sortable_field_name()
            self.state = 1090
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
        self.enterRule(localctx, 194, self.RULE_an_sortable_field_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1092
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
        self.enterRule(localctx, 196, self.RULE_an_order)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1094
            self.match(ZmeiLangParser.AN_ORDER)
            self.state = 1095
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1096
            self.an_order_fields()
            self.state = 1097
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
        self.enterRule(localctx, 198, self.RULE_an_order_fields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1099
            self.id_or_kw()
            self.state = 1104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 1100
                self.match(ZmeiLangParser.COMA)
                self.state = 1101
                self.id_or_kw()
                self.state = 1106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 200, self.RULE_an_rest)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1107
            self.match(ZmeiLangParser.AN_REST)
            self.state = 1110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 1108
                self.match(ZmeiLangParser.DOT)
                self.state = 1109
                self.an_rest_descriptor()


            self.state = 1116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1112
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1113
                self.an_rest_config()
                self.state = 1114
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
        self.enterRule(localctx, 202, self.RULE_an_rest_config)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1118
            self.an_rest_main_part()
            self.state = 1124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ZmeiLangParser.KW_INLINE - 64)) | (1 << (ZmeiLangParser.NL - 64)) | (1 << (ZmeiLangParser.COMA - 64)))) != 0):
                self.state = 1122
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.KW_INLINE]:
                    self.state = 1119
                    self.an_rest_inline()
                    pass
                elif token in [ZmeiLangParser.NL]:
                    self.state = 1120
                    self.match(ZmeiLangParser.NL)
                    pass
                elif token in [ZmeiLangParser.COMA]:
                    self.state = 1121
                    self.match(ZmeiLangParser.COMA)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1126
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
        self.enterRule(localctx, 204, self.RULE_an_rest_main_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1141
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,85,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1139
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [ZmeiLangParser.KW_FIELDS]:
                        self.state = 1127
                        self.an_rest_fields()
                        pass
                    elif token in [ZmeiLangParser.KW_I18N]:
                        self.state = 1128
                        self.an_rest_i18n()
                        pass
                    elif token in [ZmeiLangParser.KW_AUTH]:
                        self.state = 1129
                        self.an_rest_auth()
                        pass
                    elif token in [ZmeiLangParser.KW_QUERY]:
                        self.state = 1130
                        self.an_rest_query()
                        pass
                    elif token in [ZmeiLangParser.KW_ON_CREATE]:
                        self.state = 1131
                        self.an_rest_on_create()
                        pass
                    elif token in [ZmeiLangParser.KW_FILTER_IN]:
                        self.state = 1132
                        self.an_rest_filter_in()
                        pass
                    elif token in [ZmeiLangParser.KW_FILTER_OUT]:
                        self.state = 1133
                        self.an_rest_filter_out()
                        pass
                    elif token in [ZmeiLangParser.KW_READ_ONLY]:
                        self.state = 1134
                        self.an_rest_read_only()
                        pass
                    elif token in [ZmeiLangParser.KW_USER_FIELD]:
                        self.state = 1135
                        self.an_rest_user_field()
                        pass
                    elif token in [ZmeiLangParser.KW_ANNOTATE]:
                        self.state = 1136
                        self.an_rest_annotate()
                        pass
                    elif token in [ZmeiLangParser.NL]:
                        self.state = 1137
                        self.match(ZmeiLangParser.NL)
                        pass
                    elif token in [ZmeiLangParser.COMA]:
                        self.state = 1138
                        self.match(ZmeiLangParser.COMA)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 1143
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,85,self._ctx)

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
        self.enterRule(localctx, 206, self.RULE_an_rest_descriptor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1144
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
        self.enterRule(localctx, 208, self.RULE_an_rest_i18n)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1146
            self.match(ZmeiLangParser.KW_I18N)
            self.state = 1147
            self.match(ZmeiLangParser.COLON)
            self.state = 1148
            self.match(ZmeiLangParser.BOOL)
            self.state = 1152
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,86,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1149
                    self.match(ZmeiLangParser.NL) 
                self.state = 1154
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,86,self._ctx)

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
        self.enterRule(localctx, 210, self.RULE_an_rest_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1155
            self.match(ZmeiLangParser.KW_QUERY)
            self.state = 1156
            self.python_code()
            self.state = 1160
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,87,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1157
                    self.match(ZmeiLangParser.NL) 
                self.state = 1162
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,87,self._ctx)

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
        self.enterRule(localctx, 212, self.RULE_an_rest_on_create)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1163
            self.match(ZmeiLangParser.KW_ON_CREATE)
            self.state = 1165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COLON:
                self.state = 1164
                self.match(ZmeiLangParser.COLON)


            self.state = 1167
            self.python_code()
            self.state = 1171
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,89,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1168
                    self.match(ZmeiLangParser.NL) 
                self.state = 1173
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,89,self._ctx)

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
        self.enterRule(localctx, 214, self.RULE_an_rest_filter_in)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1174
            self.match(ZmeiLangParser.KW_FILTER_IN)
            self.state = 1176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COLON:
                self.state = 1175
                self.match(ZmeiLangParser.COLON)


            self.state = 1178
            self.python_code()
            self.state = 1182
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,91,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1179
                    self.match(ZmeiLangParser.NL) 
                self.state = 1184
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,91,self._ctx)

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
        self.enterRule(localctx, 216, self.RULE_an_rest_filter_out)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1185
            self.match(ZmeiLangParser.KW_FILTER_OUT)
            self.state = 1187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COLON:
                self.state = 1186
                self.match(ZmeiLangParser.COLON)


            self.state = 1189
            self.python_code()
            self.state = 1193
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,93,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1190
                    self.match(ZmeiLangParser.NL) 
                self.state = 1195
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,93,self._ctx)

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
        self.enterRule(localctx, 218, self.RULE_an_rest_read_only)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1196
            self.match(ZmeiLangParser.KW_READ_ONLY)
            self.state = 1197
            self.match(ZmeiLangParser.COLON)
            self.state = 1198
            self.field_list_expr()
            self.state = 1202
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,94,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1199
                    self.match(ZmeiLangParser.NL) 
                self.state = 1204
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,94,self._ctx)

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
        self.enterRule(localctx, 220, self.RULE_an_rest_user_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1205
            self.match(ZmeiLangParser.KW_USER_FIELD)
            self.state = 1206
            self.match(ZmeiLangParser.COLON)
            self.state = 1207
            self.id_or_kw()
            self.state = 1211
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,95,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1208
                    self.match(ZmeiLangParser.NL) 
                self.state = 1213
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,95,self._ctx)

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
        self.enterRule(localctx, 222, self.RULE_an_rest_fields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1214
            self.match(ZmeiLangParser.KW_FIELDS)
            self.state = 1215
            self.match(ZmeiLangParser.COLON)
            self.state = 1216
            self.field_list_expr()
            self.state = 1218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.SQ_BRACE_OPEN:
                self.state = 1217
                self.an_rest_fields_write_mode()


            self.state = 1223
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,97,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1220
                    self.match(ZmeiLangParser.NL) 
                self.state = 1225
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,97,self._ctx)

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
        self.enterRule(localctx, 224, self.RULE_an_rest_fields_write_mode)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1226
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
        self.enterRule(localctx, 226, self.RULE_an_rest_auth)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1228
            self.match(ZmeiLangParser.KW_AUTH)
            self.state = 1229
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1230
            self.an_rest_auth_type()
            self.state = 1235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 1231
                self.match(ZmeiLangParser.COMA)
                self.state = 1232
                self.an_rest_auth_type()
                self.state = 1237
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1238
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
        self.enterRule(localctx, 228, self.RULE_an_rest_auth_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1240
            self.match(ZmeiLangParser.KW_AUTH_TYPE)
            self.state = 1244
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.COLON]:
                self.state = 1241
                self.match(ZmeiLangParser.COLON)
                self.state = 1242
                self.an_rest_auth_token_model()
                pass
            elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                self.state = 1243
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
        self.enterRule(localctx, 230, self.RULE_an_rest_auth_token_model)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1246
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
        self.enterRule(localctx, 232, self.RULE_an_rest_auth_token_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1248
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
        self.enterRule(localctx, 234, self.RULE_an_rest_annotate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1250
            self.match(ZmeiLangParser.KW_ANNOTATE)
            self.state = 1251
            self.match(ZmeiLangParser.COLON)
            self.state = 1252
            self.an_rest_annotate_count()
            self.state = 1256
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,100,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1253
                    self.match(ZmeiLangParser.NL) 
                self.state = 1258
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,100,self._ctx)

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
        self.enterRule(localctx, 236, self.RULE_an_rest_annotate_count)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1259
            self.match(ZmeiLangParser.KW_COUNT)
            self.state = 1260
            self.an_rest_annotate_count_field()
            self.state = 1263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.KW_AS:
                self.state = 1261
                self.match(ZmeiLangParser.KW_AS)
                self.state = 1262
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
        self.enterRule(localctx, 238, self.RULE_an_rest_annotate_count_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1265
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
        self.enterRule(localctx, 240, self.RULE_an_rest_annotate_count_alias)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1267
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
        self.enterRule(localctx, 242, self.RULE_an_rest_inline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1269
            self.match(ZmeiLangParser.KW_INLINE)
            self.state = 1270
            self.match(ZmeiLangParser.COLON)
            self.state = 1274 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 1274
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                        self.state = 1271
                        self.an_rest_inline_decl()
                        pass
                    elif token in [ZmeiLangParser.COMA]:
                        self.state = 1272
                        self.match(ZmeiLangParser.COMA)
                        pass
                    elif token in [ZmeiLangParser.NL]:
                        self.state = 1273
                        self.match(ZmeiLangParser.NL)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 1276 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,103,self._ctx)

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
        self.enterRule(localctx, 244, self.RULE_an_rest_inline_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1278
            self.an_rest_inline_name()
            self.state = 1279
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1280
            self.an_rest_config()
            self.state = 1281
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
        self.enterRule(localctx, 246, self.RULE_an_rest_inline_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1283
            self.id_or_kw()
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
        self.enterRule(localctx, 248, self.RULE_an_api)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1285
            self.match(ZmeiLangParser.AN_API)
            self.state = 1300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1286
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1296
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.STAR]:
                    self.state = 1287
                    self.an_api_all()
                    pass
                elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                    self.state = 1288
                    self.an_api_name()
                    self.state = 1293
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==ZmeiLangParser.COMA:
                        self.state = 1289
                        self.match(ZmeiLangParser.COMA)
                        self.state = 1290
                        self.an_api_name()
                        self.state = 1295
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1298
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
        self.enterRule(localctx, 250, self.RULE_an_api_all)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1302
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
        self.enterRule(localctx, 252, self.RULE_an_api_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1304
            self.id_or_kw()
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
        self.enterRule(localctx, 254, self.RULE_an_clean)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1306
            self.match(ZmeiLangParser.AN_CLEAN)
            self.state = 1307
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
        self.enterRule(localctx, 256, self.RULE_an_pre_save)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1309
            self.match(ZmeiLangParser.AN_PRE_SAVE)
            self.state = 1310
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
        self.enterRule(localctx, 258, self.RULE_an_post_save)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1312
            self.match(ZmeiLangParser.AN_POST_SAVE)
            self.state = 1313
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
        self.enterRule(localctx, 260, self.RULE_an_pre_delete)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1315
            self.match(ZmeiLangParser.AN_PRE_DELETE)
            self.state = 1316
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
        self.enterRule(localctx, 262, self.RULE_an_post_delete)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1318
            self.match(ZmeiLangParser.AN_POST_DELETE)
            self.state = 1319
            self.python_code()
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
        self.enterRule(localctx, 264, self.RULE_an_m2m_changed)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1321
            self.match(ZmeiLangParser.AN_M2M_CHANGED)
            self.state = 1322
            self.python_code()
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
        self.enterRule(localctx, 266, self.RULE_an_mixin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1324
            self.match(ZmeiLangParser.AN_MIXIN)

            self.state = 1325
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1326
            self.classname()
            self.state = 1327
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
        self.enterRule(localctx, 268, self.RULE_an_date_tree)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1329
            self.match(ZmeiLangParser.AN_DATE_TREE)

            self.state = 1330
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1331
            self.an_date_tree_field()
            self.state = 1332
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
        self.enterRule(localctx, 270, self.RULE_an_date_tree_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1334
            self.id_or_kw()
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
        self.enterRule(localctx, 272, self.RULE_an_tree)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1336
            self.match(ZmeiLangParser.AN_TREE)
            self.state = 1341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1337
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1338
                self.an_tree_poly()
                self.state = 1339
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
        self.enterRule(localctx, 274, self.RULE_an_tree_poly)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1343
            self.match(ZmeiLangParser.KW_POLY_LIST)
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
        self.enterRule(localctx, 276, self.RULE_an_admin)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1345
            self.match(ZmeiLangParser.AN_ADMIN)
            self.state = 1371
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1346
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1361
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,109,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 1359
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [ZmeiLangParser.KW_LIST]:
                            self.state = 1347
                            self.an_admin_list()
                            pass
                        elif token in [ZmeiLangParser.KW_READ_ONLY]:
                            self.state = 1348
                            self.an_admin_read_only()
                            pass
                        elif token in [ZmeiLangParser.KW_LIST_EDITABLE]:
                            self.state = 1349
                            self.an_admin_list_editable()
                            pass
                        elif token in [ZmeiLangParser.KW_LIST_FILTER]:
                            self.state = 1350
                            self.an_admin_list_filter()
                            pass
                        elif token in [ZmeiLangParser.KW_LIST_SEARCH]:
                            self.state = 1351
                            self.an_admin_list_search()
                            pass
                        elif token in [ZmeiLangParser.KW_FIELDS]:
                            self.state = 1352
                            self.an_admin_fields()
                            pass
                        elif token in [ZmeiLangParser.KW_TABS]:
                            self.state = 1353
                            self.an_admin_tabs()
                            pass
                        elif token in [ZmeiLangParser.KW_INLINE]:
                            self.state = 1354
                            self.an_admin_inlines()
                            pass
                        elif token in [ZmeiLangParser.KW_CSS]:
                            self.state = 1355
                            self.an_admin_css()
                            pass
                        elif token in [ZmeiLangParser.KW_JS]:
                            self.state = 1356
                            self.an_admin_js()
                            pass
                        elif token in [ZmeiLangParser.NL]:
                            self.state = 1357
                            self.match(ZmeiLangParser.NL)
                            pass
                        elif token in [ZmeiLangParser.COMA]:
                            self.state = 1358
                            self.match(ZmeiLangParser.COMA)
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 1363
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,109,self._ctx)

                self.state = 1367
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZmeiLangParser.NL:
                    self.state = 1364
                    self.match(ZmeiLangParser.NL)
                    self.state = 1369
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 1370
                self.match(ZmeiLangParser.BRACE_CLOSE)


            self.state = 1376
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,112,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1373
                    self.match(ZmeiLangParser.NL) 
                self.state = 1378
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,112,self._ctx)

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
        self.enterRule(localctx, 278, self.RULE_an_admin_js)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1379
            self.match(ZmeiLangParser.KW_JS)
            self.state = 1380
            self.match(ZmeiLangParser.COLON)
            self.state = 1384
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 1381
                self.match(ZmeiLangParser.NL)
                self.state = 1386
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1387
            self.an_admin_js_file_name()
            self.state = 1398
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,115,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1388
                    self.match(ZmeiLangParser.COMA)
                    self.state = 1392
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==ZmeiLangParser.NL:
                        self.state = 1389
                        self.match(ZmeiLangParser.NL)
                        self.state = 1394
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 1395
                    self.an_admin_js_file_name() 
                self.state = 1400
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,115,self._ctx)

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
        self.enterRule(localctx, 280, self.RULE_an_admin_css)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1401
            self.match(ZmeiLangParser.KW_CSS)
            self.state = 1402
            self.match(ZmeiLangParser.COLON)
            self.state = 1403
            self.an_admin_css_file_name()
            self.state = 1408
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,116,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1404
                    self.match(ZmeiLangParser.COMA)
                    self.state = 1405
                    self.an_admin_css_file_name() 
                self.state = 1410
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,116,self._ctx)

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
        self.enterRule(localctx, 282, self.RULE_an_admin_css_file_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1411
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
        self.enterRule(localctx, 284, self.RULE_an_admin_js_file_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1413
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
        self.enterRule(localctx, 286, self.RULE_an_admin_inlines)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1415
            self.match(ZmeiLangParser.KW_INLINE)
            self.state = 1416
            self.match(ZmeiLangParser.COLON)
            self.state = 1417
            self.an_admin_inline()
            self.state = 1422
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,117,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1418
                    self.match(ZmeiLangParser.COMA)
                    self.state = 1419
                    self.an_admin_inline() 
                self.state = 1424
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,117,self._ctx)

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
        self.enterRule(localctx, 288, self.RULE_an_admin_inline)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1425
            self.inline_name()
            self.state = 1438
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1426
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1434
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (ZmeiLangParser.KW_TYPE - 65)) | (1 << (ZmeiLangParser.KW_EXTRA - 65)) | (1 << (ZmeiLangParser.KW_FIELDS - 65)) | (1 << (ZmeiLangParser.NL - 65)) | (1 << (ZmeiLangParser.COMA - 65)))) != 0):
                    self.state = 1432
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [ZmeiLangParser.KW_TYPE]:
                        self.state = 1427
                        self.inline_type()
                        pass
                    elif token in [ZmeiLangParser.KW_EXTRA]:
                        self.state = 1428
                        self.inline_extra()
                        pass
                    elif token in [ZmeiLangParser.KW_FIELDS]:
                        self.state = 1429
                        self.inline_fields()
                        pass
                    elif token in [ZmeiLangParser.NL]:
                        self.state = 1430
                        self.match(ZmeiLangParser.NL)
                        pass
                    elif token in [ZmeiLangParser.COMA]:
                        self.state = 1431
                        self.match(ZmeiLangParser.COMA)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 1436
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 1437
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
        self.enterRule(localctx, 290, self.RULE_inline_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1440
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
        self.enterRule(localctx, 292, self.RULE_inline_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1442
            self.match(ZmeiLangParser.KW_TYPE)
            self.state = 1443
            self.match(ZmeiLangParser.COLON)
            self.state = 1444
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
        self.enterRule(localctx, 294, self.RULE_inline_extra)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1446
            self.match(ZmeiLangParser.KW_EXTRA)
            self.state = 1447
            self.match(ZmeiLangParser.COLON)
            self.state = 1448
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
        self.enterRule(localctx, 296, self.RULE_inline_fields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1450
            self.match(ZmeiLangParser.KW_FIELDS)
            self.state = 1451
            self.match(ZmeiLangParser.COLON)
            self.state = 1452
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
        self.enterRule(localctx, 298, self.RULE_an_admin_tabs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1454
            self.match(ZmeiLangParser.KW_TABS)
            self.state = 1455
            self.match(ZmeiLangParser.COLON)
            self.state = 1456
            self.an_admin_tab()
            self.state = 1461
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,121,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1457
                    self.match(ZmeiLangParser.COMA)
                    self.state = 1458
                    self.an_admin_tab() 
                self.state = 1463
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,121,self._ctx)

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
        self.enterRule(localctx, 300, self.RULE_an_admin_tab)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1464
            self.tab_name()
            self.state = 1466
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.STRING_DQ or _la==ZmeiLangParser.STRING_SQ:
                self.state = 1465
                self.tab_verbose_name()


            self.state = 1468
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1469
            self.field_list_expr()
            self.state = 1470
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
        self.enterRule(localctx, 302, self.RULE_tab_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1472
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
        self.enterRule(localctx, 304, self.RULE_tab_verbose_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1474
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
        self.enterRule(localctx, 306, self.RULE_an_admin_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1476
            self.match(ZmeiLangParser.KW_LIST)
            self.state = 1477
            self.match(ZmeiLangParser.COLON)
            self.state = 1478
            self.field_list_expr()
            self.state = 1482
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,123,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1479
                    self.match(ZmeiLangParser.NL) 
                self.state = 1484
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,123,self._ctx)

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
        self.enterRule(localctx, 308, self.RULE_an_admin_read_only)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1485
            self.match(ZmeiLangParser.KW_READ_ONLY)
            self.state = 1486
            self.match(ZmeiLangParser.COLON)
            self.state = 1487
            self.field_list_expr()
            self.state = 1491
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,124,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1488
                    self.match(ZmeiLangParser.NL) 
                self.state = 1493
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,124,self._ctx)

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
        self.enterRule(localctx, 310, self.RULE_an_admin_list_editable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1494
            self.match(ZmeiLangParser.KW_LIST_EDITABLE)
            self.state = 1495
            self.match(ZmeiLangParser.COLON)
            self.state = 1496
            self.field_list_expr()
            self.state = 1500
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,125,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1497
                    self.match(ZmeiLangParser.NL) 
                self.state = 1502
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,125,self._ctx)

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
        self.enterRule(localctx, 312, self.RULE_an_admin_list_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1503
            self.match(ZmeiLangParser.KW_LIST_FILTER)
            self.state = 1504
            self.match(ZmeiLangParser.COLON)
            self.state = 1505
            self.field_list_expr()
            self.state = 1509
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,126,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1506
                    self.match(ZmeiLangParser.NL) 
                self.state = 1511
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,126,self._ctx)

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
        self.enterRule(localctx, 314, self.RULE_an_admin_list_search)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1512
            self.match(ZmeiLangParser.KW_LIST_SEARCH)
            self.state = 1513
            self.match(ZmeiLangParser.COLON)
            self.state = 1514
            self.field_list_expr()
            self.state = 1518
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,127,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1515
                    self.match(ZmeiLangParser.NL) 
                self.state = 1520
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,127,self._ctx)

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
        self.enterRule(localctx, 316, self.RULE_an_admin_fields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1521
            self.match(ZmeiLangParser.KW_FIELDS)
            self.state = 1522
            self.match(ZmeiLangParser.COLON)
            self.state = 1523
            self.field_list_expr()
            self.state = 1527
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,128,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1524
                    self.match(ZmeiLangParser.NL) 
                self.state = 1529
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,128,self._ctx)

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
        self.enterRule(localctx, 318, self.RULE_page)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1530
            self.page_header()
            self.state = 1534
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,129,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1531
                    self.match(ZmeiLangParser.NL) 
                self.state = 1536
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,129,self._ctx)

            self.state = 1537
            self.page_body()
            self.state = 1541
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,130,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1538
                    self.match(ZmeiLangParser.NL) 
                self.state = 1543
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,130,self._ctx)

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
        self.enterRule(localctx, 320, self.RULE_page_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1544
            self.match(ZmeiLangParser.SQ_BRACE_OPEN)
            self.state = 1546
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,131,self._ctx)
            if la_ == 1:
                self.state = 1545
                self.page_base()


            self.state = 1548
            self.page_name()
            self.state = 1550
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.KW_AS:
                self.state = 1549
                self.page_alias()


            self.state = 1560
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COLON:
                self.state = 1552
                self.match(ZmeiLangParser.COLON)
                self.state = 1554
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 122)) & ~0x3f) == 0 and ((1 << (_la - 122)) & ((1 << (ZmeiLangParser.DOT - 122)) | (1 << (ZmeiLangParser.SLASH - 122)) | (1 << (ZmeiLangParser.DOLLAR - 122)))) != 0):
                    self.state = 1553
                    self.page_url()


                self.state = 1558
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.COLON:
                    self.state = 1556
                    self.match(ZmeiLangParser.COLON)
                    self.state = 1557
                    self.page_template()




            self.state = 1562
            self.match(ZmeiLangParser.SQ_BRACE_CLOSE)
            self.state = 1564
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,136,self._ctx)
            if la_ == 1:
                self.state = 1563
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
        self.enterRule(localctx, 322, self.RULE_page_base)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1569
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,137,self._ctx)
            if la_ == 1:
                self.state = 1566
                self.id_or_kw()
                self.state = 1567
                self.match(ZmeiLangParser.DOT)


            self.state = 1571
            self.id_or_kw()
            self.state = 1572
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.DASH or _la==ZmeiLangParser.APPROX):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 1573
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
        self.enterRule(localctx, 324, self.RULE_page_alias)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1575
            self.match(ZmeiLangParser.KW_AS)
            self.state = 1576
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
        self.enterRule(localctx, 326, self.RULE_page_alias_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1578
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
        self.enterRule(localctx, 328, self.RULE_page_template)
        try:
            self.state = 1582
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID, ZmeiLangParser.DIGIT, ZmeiLangParser.UNDERSCORE, ZmeiLangParser.DASH, ZmeiLangParser.DOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1580
                self.template_name()
                pass
            elif token in [ZmeiLangParser.ASSIGN, ZmeiLangParser.CODE_BLOCK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1581
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
        self.enterRule(localctx, 330, self.RULE_template_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1584
            self.file_name_part()
            self.state = 1589
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.SLASH:
                self.state = 1585
                self.match(ZmeiLangParser.SLASH)
                self.state = 1586
                self.file_name_part()
                self.state = 1591
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
        self.enterRule(localctx, 332, self.RULE_file_name_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1597 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1597
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                    self.state = 1592
                    self.id_or_kw()
                    pass
                elif token in [ZmeiLangParser.DIGIT]:
                    self.state = 1593
                    self.match(ZmeiLangParser.DIGIT)
                    pass
                elif token in [ZmeiLangParser.DASH]:
                    self.state = 1594
                    self.match(ZmeiLangParser.DASH)
                    pass
                elif token in [ZmeiLangParser.UNDERSCORE]:
                    self.state = 1595
                    self.match(ZmeiLangParser.UNDERSCORE)
                    pass
                elif token in [ZmeiLangParser.DOT]:
                    self.state = 1596
                    self.match(ZmeiLangParser.DOT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1599 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.WRITE_MODE) | (1 << ZmeiLangParser.BOOL) | (1 << ZmeiLangParser.KW_THEME) | (1 << ZmeiLangParser.KW_CHILD) | (1 << ZmeiLangParser.KW_FILTER_OUT) | (1 << ZmeiLangParser.KW_FILTER_IN) | (1 << ZmeiLangParser.KW_PAGE) | (1 << ZmeiLangParser.KW_LINK_SUFFIX) | (1 << ZmeiLangParser.KW_URL_PREFIX) | (1 << ZmeiLangParser.KW_CAN_EDIT) | (1 << ZmeiLangParser.KW_OBJECT_EXPR) | (1 << ZmeiLangParser.KW_BLOCK) | (1 << ZmeiLangParser.KW_ITEM_NAME) | (1 << ZmeiLangParser.KW_PK_PARAM) | (1 << ZmeiLangParser.KW_LIST_FIELDS) | (1 << ZmeiLangParser.KW_DELETE) | (1 << ZmeiLangParser.KW_EDIT) | (1 << ZmeiLangParser.KW_CREATE) | (1 << ZmeiLangParser.KW_DETAIL) | (1 << ZmeiLangParser.KW_SKIP) | (1 << ZmeiLangParser.KW_FROM) | (1 << ZmeiLangParser.KW_POLY_LIST) | (1 << ZmeiLangParser.KW_CSS) | (1 << ZmeiLangParser.KW_JS) | (1 << ZmeiLangParser.KW_INLINE_TYPE) | (1 << ZmeiLangParser.KW_AUTH_TYPE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ZmeiLangParser.KW_INLINE - 64)) | (1 << (ZmeiLangParser.KW_TYPE - 64)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 64)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 64)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 64)) | (1 << (ZmeiLangParser.KW_QUERY - 64)) | (1 << (ZmeiLangParser.KW_AUTH - 64)) | (1 << (ZmeiLangParser.KW_COUNT - 64)) | (1 << (ZmeiLangParser.KW_I18N - 64)) | (1 << (ZmeiLangParser.KW_EXTRA - 64)) | (1 << (ZmeiLangParser.KW_TABS - 64)) | (1 << (ZmeiLangParser.KW_LIST - 64)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 64)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 64)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 64)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 64)) | (1 << (ZmeiLangParser.KW_FIELDS - 64)) | (1 << (ZmeiLangParser.KW_IMPORT - 64)) | (1 << (ZmeiLangParser.KW_AS - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 64)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 64)) | (1 << (ZmeiLangParser.ID - 64)) | (1 << (ZmeiLangParser.DIGIT - 64)) | (1 << (ZmeiLangParser.UNDERSCORE - 64)) | (1 << (ZmeiLangParser.DASH - 64)) | (1 << (ZmeiLangParser.DOT - 64)))) != 0)):
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
        self.enterRule(localctx, 334, self.RULE_page_url)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1602
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT or _la==ZmeiLangParser.DOLLAR:
                self.state = 1601
                _la = self._input.LA(1)
                if not(_la==ZmeiLangParser.DOT or _la==ZmeiLangParser.DOLLAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 1604
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
        self.enterRule(localctx, 336, self.RULE_url_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1609 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1609
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                    self.state = 1606
                    self.id_or_kw()
                    pass
                elif token in [ZmeiLangParser.DASH]:
                    self.state = 1607
                    self.match(ZmeiLangParser.DASH)
                    pass
                elif token in [ZmeiLangParser.DIGIT]:
                    self.state = 1608
                    self.match(ZmeiLangParser.DIGIT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1611 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.WRITE_MODE) | (1 << ZmeiLangParser.BOOL) | (1 << ZmeiLangParser.KW_THEME) | (1 << ZmeiLangParser.KW_CHILD) | (1 << ZmeiLangParser.KW_FILTER_OUT) | (1 << ZmeiLangParser.KW_FILTER_IN) | (1 << ZmeiLangParser.KW_PAGE) | (1 << ZmeiLangParser.KW_LINK_SUFFIX) | (1 << ZmeiLangParser.KW_URL_PREFIX) | (1 << ZmeiLangParser.KW_CAN_EDIT) | (1 << ZmeiLangParser.KW_OBJECT_EXPR) | (1 << ZmeiLangParser.KW_BLOCK) | (1 << ZmeiLangParser.KW_ITEM_NAME) | (1 << ZmeiLangParser.KW_PK_PARAM) | (1 << ZmeiLangParser.KW_LIST_FIELDS) | (1 << ZmeiLangParser.KW_DELETE) | (1 << ZmeiLangParser.KW_EDIT) | (1 << ZmeiLangParser.KW_CREATE) | (1 << ZmeiLangParser.KW_DETAIL) | (1 << ZmeiLangParser.KW_SKIP) | (1 << ZmeiLangParser.KW_FROM) | (1 << ZmeiLangParser.KW_POLY_LIST) | (1 << ZmeiLangParser.KW_CSS) | (1 << ZmeiLangParser.KW_JS) | (1 << ZmeiLangParser.KW_INLINE_TYPE) | (1 << ZmeiLangParser.KW_AUTH_TYPE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ZmeiLangParser.KW_INLINE - 64)) | (1 << (ZmeiLangParser.KW_TYPE - 64)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 64)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 64)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 64)) | (1 << (ZmeiLangParser.KW_QUERY - 64)) | (1 << (ZmeiLangParser.KW_AUTH - 64)) | (1 << (ZmeiLangParser.KW_COUNT - 64)) | (1 << (ZmeiLangParser.KW_I18N - 64)) | (1 << (ZmeiLangParser.KW_EXTRA - 64)) | (1 << (ZmeiLangParser.KW_TABS - 64)) | (1 << (ZmeiLangParser.KW_LIST - 64)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 64)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 64)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 64)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 64)) | (1 << (ZmeiLangParser.KW_FIELDS - 64)) | (1 << (ZmeiLangParser.KW_IMPORT - 64)) | (1 << (ZmeiLangParser.KW_AS - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 64)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 64)) | (1 << (ZmeiLangParser.ID - 64)) | (1 << (ZmeiLangParser.DIGIT - 64)) | (1 << (ZmeiLangParser.DASH - 64)))) != 0)):
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
        self.enterRule(localctx, 338, self.RULE_url_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1613
            self.match(ZmeiLangParser.LT)
            self.state = 1614
            self.id_or_kw()
            self.state = 1615
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
        self.enterRule(localctx, 340, self.RULE_url_segment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1619
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID, ZmeiLangParser.DIGIT, ZmeiLangParser.DASH]:
                self.state = 1617
                self.url_part()
                pass
            elif token in [ZmeiLangParser.LT]:
                self.state = 1618
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
        self.enterRule(localctx, 342, self.RULE_url_segments)
        self._la = 0 # Token type
        try:
            self.state = 1631
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,148,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1621
                self.match(ZmeiLangParser.SLASH)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1624 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 1622
                        self.match(ZmeiLangParser.SLASH)
                        self.state = 1623
                        self.url_segment()

                    else:
                        raise NoViableAltException(self)
                    self.state = 1626 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,146,self._ctx)

                self.state = 1629
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.SLASH:
                    self.state = 1628
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
        self.enterRule(localctx, 344, self.RULE_page_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1633
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
        self.enterRule(localctx, 346, self.RULE_page_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1638
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,149,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1635
                    self.page_field() 
                self.state = 1640
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,149,self._ctx)

            self.state = 1644
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,150,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1641
                    self.page_function() 
                self.state = 1646
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,150,self._ctx)

            self.state = 1648
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.ASSIGN or _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 1647
                self.page_code()


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

            self.state = 1659
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,153,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1656
                    self.page_annotation() 
                self.state = 1661
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,153,self._ctx)

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
        self.enterRule(localctx, 348, self.RULE_page_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1662
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
        self.enterRule(localctx, 350, self.RULE_page_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1664
            self.page_field_name()
            self.state = 1665
            self.match(ZmeiLangParser.ASSIGN)
            self.state = 1666
            self.page_field_code()
            self.state = 1673
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.NL]:
                self.state = 1668 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 1667
                        self.match(ZmeiLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 1670 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,154,self._ctx)

                pass
            elif token in [ZmeiLangParser.EOF]:
                self.state = 1672
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
        self.enterRule(localctx, 352, self.RULE_page_field_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1675
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
        self.enterRule(localctx, 354, self.RULE_page_field_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1677
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
        self.enterRule(localctx, 356, self.RULE_page_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1679
            self.page_function_name()
            self.state = 1680
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1682
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.WRITE_MODE) | (1 << ZmeiLangParser.BOOL) | (1 << ZmeiLangParser.KW_THEME) | (1 << ZmeiLangParser.KW_CHILD) | (1 << ZmeiLangParser.KW_FILTER_OUT) | (1 << ZmeiLangParser.KW_FILTER_IN) | (1 << ZmeiLangParser.KW_PAGE) | (1 << ZmeiLangParser.KW_LINK_SUFFIX) | (1 << ZmeiLangParser.KW_URL_PREFIX) | (1 << ZmeiLangParser.KW_CAN_EDIT) | (1 << ZmeiLangParser.KW_OBJECT_EXPR) | (1 << ZmeiLangParser.KW_BLOCK) | (1 << ZmeiLangParser.KW_ITEM_NAME) | (1 << ZmeiLangParser.KW_PK_PARAM) | (1 << ZmeiLangParser.KW_LIST_FIELDS) | (1 << ZmeiLangParser.KW_DELETE) | (1 << ZmeiLangParser.KW_EDIT) | (1 << ZmeiLangParser.KW_CREATE) | (1 << ZmeiLangParser.KW_DETAIL) | (1 << ZmeiLangParser.KW_SKIP) | (1 << ZmeiLangParser.KW_FROM) | (1 << ZmeiLangParser.KW_POLY_LIST) | (1 << ZmeiLangParser.KW_CSS) | (1 << ZmeiLangParser.KW_JS) | (1 << ZmeiLangParser.KW_INLINE_TYPE) | (1 << ZmeiLangParser.KW_AUTH_TYPE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ZmeiLangParser.KW_INLINE - 64)) | (1 << (ZmeiLangParser.KW_TYPE - 64)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 64)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 64)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 64)) | (1 << (ZmeiLangParser.KW_QUERY - 64)) | (1 << (ZmeiLangParser.KW_AUTH - 64)) | (1 << (ZmeiLangParser.KW_COUNT - 64)) | (1 << (ZmeiLangParser.KW_I18N - 64)) | (1 << (ZmeiLangParser.KW_EXTRA - 64)) | (1 << (ZmeiLangParser.KW_TABS - 64)) | (1 << (ZmeiLangParser.KW_LIST - 64)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 64)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 64)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 64)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 64)) | (1 << (ZmeiLangParser.KW_FIELDS - 64)) | (1 << (ZmeiLangParser.KW_IMPORT - 64)) | (1 << (ZmeiLangParser.KW_AS - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 64)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 64)) | (1 << (ZmeiLangParser.ID - 64)))) != 0):
                self.state = 1681
                self.page_function_args()


            self.state = 1684
            self.match(ZmeiLangParser.BRACE_CLOSE)
            self.state = 1686
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 1685
                self.code_block()


            self.state = 1694
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.NL]:
                self.state = 1689 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 1688
                        self.match(ZmeiLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 1691 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,158,self._ctx)

                pass
            elif token in [ZmeiLangParser.EOF]:
                self.state = 1693
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
        self.enterRule(localctx, 358, self.RULE_page_function_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1696
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
        self.enterRule(localctx, 360, self.RULE_page_function_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1698
            self.id_or_kw()
            self.state = 1703
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 1699
                self.match(ZmeiLangParser.COMA)
                self.state = 1700
                self.id_or_kw()
                self.state = 1705
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

        def an_html(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_htmlContext,0)


        def an_react(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_reactContext,0)


        def an_flutter(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_flutterContext,0)


        def an_stream(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_streamContext,0)


        def an_get(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_getContext,0)


        def an_menu(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_menuContext,0)


        def an_crud(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crudContext,0)


        def an_crud_detail(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_detailContext,0)


        def an_crud_delete(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_deleteContext,0)


        def an_crud_edit(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_editContext,0)


        def an_crud_create(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_createContext,0)


        def an_post(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_postContext,0)


        def an_error(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_errorContext,0)


        def an_auth(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_authContext,0)


        def an_markdown(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_markdownContext,0)


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
        self.enterRule(localctx, 362, self.RULE_page_annotation)
        try:
            self.state = 1722
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.AN_HTML]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1706
                self.an_html()
                pass
            elif token in [ZmeiLangParser.AN_REACT, ZmeiLangParser.AN_REACT_CLIENT, ZmeiLangParser.AN_REACT_SERVER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1707
                self.an_react()
                pass
            elif token in [ZmeiLangParser.AN_FLUTTER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1708
                self.an_flutter()
                pass
            elif token in [ZmeiLangParser.AN_STREAM]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1709
                self.an_stream()
                pass
            elif token in [ZmeiLangParser.AN_GET]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1710
                self.an_get()
                pass
            elif token in [ZmeiLangParser.AN_MENU]:
                self.enterOuterAlt(localctx, 6)
                self.state = 1711
                self.an_menu()
                pass
            elif token in [ZmeiLangParser.AN_CRUD]:
                self.enterOuterAlt(localctx, 7)
                self.state = 1712
                self.an_crud()
                pass
            elif token in [ZmeiLangParser.AN_CRUD_DETAIL]:
                self.enterOuterAlt(localctx, 8)
                self.state = 1713
                self.an_crud_detail()
                pass
            elif token in [ZmeiLangParser.AN_CRUD_DELETE]:
                self.enterOuterAlt(localctx, 9)
                self.state = 1714
                self.an_crud_delete()
                pass
            elif token in [ZmeiLangParser.AN_CRUD_EDIT]:
                self.enterOuterAlt(localctx, 10)
                self.state = 1715
                self.an_crud_edit()
                pass
            elif token in [ZmeiLangParser.AN_CRUD_CREATE]:
                self.enterOuterAlt(localctx, 11)
                self.state = 1716
                self.an_crud_create()
                pass
            elif token in [ZmeiLangParser.AN_POST]:
                self.enterOuterAlt(localctx, 12)
                self.state = 1717
                self.an_post()
                pass
            elif token in [ZmeiLangParser.AN_ERROR]:
                self.enterOuterAlt(localctx, 13)
                self.state = 1718
                self.an_error()
                pass
            elif token in [ZmeiLangParser.AN_AUTH]:
                self.enterOuterAlt(localctx, 14)
                self.state = 1719
                self.an_auth()
                pass
            elif token in [ZmeiLangParser.AN_MARKDOWN]:
                self.enterOuterAlt(localctx, 15)
                self.state = 1720
                self.an_markdown()
                pass
            elif token in [ZmeiLangParser.NL]:
                self.enterOuterAlt(localctx, 16)
                self.state = 1721
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
        self.enterRule(localctx, 364, self.RULE_an_react)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1724
            self.an_react_type()
            self.state = 1727
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 1725
                self.match(ZmeiLangParser.DOT)
                self.state = 1726
                self.an_react_descriptor()


            self.state = 1729
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
        self.enterRule(localctx, 366, self.RULE_an_react_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1731
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
        self.enterRule(localctx, 368, self.RULE_an_react_descriptor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1733
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
        self.enterRule(localctx, 370, self.RULE_an_markdown)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1735
            self.match(ZmeiLangParser.AN_MARKDOWN)
            self.state = 1738
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 1736
                self.match(ZmeiLangParser.DOT)
                self.state = 1737
                self.an_markdown_descriptor()


            self.state = 1740
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
        self.enterRule(localctx, 372, self.RULE_an_markdown_descriptor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1742
            self.id_or_kw()
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
        self.enterRule(localctx, 374, self.RULE_an_auth)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1744
            self.match(ZmeiLangParser.AN_AUTH)
            self.state = 1746
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 1745
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
        self.enterRule(localctx, 376, self.RULE_an_error)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1748
            self.match(ZmeiLangParser.AN_ERROR)
            self.state = 1749
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1750
            self.an_error_code()
            self.state = 1751
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
        self.enterRule(localctx, 378, self.RULE_an_error_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1753
            self.match(ZmeiLangParser.DIGIT)
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
        self.enterRule(localctx, 380, self.RULE_an_post)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1755
            self.match(ZmeiLangParser.AN_POST)
            self.state = 1757
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 1756
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
        self.enterRule(localctx, 382, self.RULE_an_crud_create)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1759
            self.match(ZmeiLangParser.AN_CRUD_CREATE)
            self.state = 1760
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
        self.enterRule(localctx, 384, self.RULE_an_crud)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1762
            self.match(ZmeiLangParser.AN_CRUD)
            self.state = 1763
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
        self.enterRule(localctx, 386, self.RULE_an_crud_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1767
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 1765
                self.match(ZmeiLangParser.DOT)
                self.state = 1766
                self.an_crud_descriptor()


            self.state = 1769
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1773
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 1770
                self.match(ZmeiLangParser.NL)
                self.state = 1775
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1776
            self.an_crud_target_model()
            self.state = 1778
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 1777
                self.an_crud_target_filter()


            self.state = 1795
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,170,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1793
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [ZmeiLangParser.KW_THEME]:
                        self.state = 1780
                        self.an_crud_theme()
                        pass
                    elif token in [ZmeiLangParser.KW_SKIP]:
                        self.state = 1781
                        self.an_crud_skip()
                        pass
                    elif token in [ZmeiLangParser.KW_FIELDS]:
                        self.state = 1782
                        self.an_crud_fields()
                        pass
                    elif token in [ZmeiLangParser.KW_LIST_FIELDS]:
                        self.state = 1783
                        self.an_crud_list_fields()
                        pass
                    elif token in [ZmeiLangParser.KW_PK_PARAM]:
                        self.state = 1784
                        self.an_crud_pk_param()
                        pass
                    elif token in [ZmeiLangParser.KW_ITEM_NAME]:
                        self.state = 1785
                        self.an_crud_item_name()
                        pass
                    elif token in [ZmeiLangParser.KW_BLOCK]:
                        self.state = 1786
                        self.an_crud_block()
                        pass
                    elif token in [ZmeiLangParser.KW_OBJECT_EXPR]:
                        self.state = 1787
                        self.an_crud_object_expr()
                        pass
                    elif token in [ZmeiLangParser.KW_CAN_EDIT]:
                        self.state = 1788
                        self.an_crud_can_edit()
                        pass
                    elif token in [ZmeiLangParser.KW_URL_PREFIX]:
                        self.state = 1789
                        self.an_crud_url_prefix()
                        pass
                    elif token in [ZmeiLangParser.KW_LINK_SUFFIX]:
                        self.state = 1790
                        self.an_crud_link_suffix()
                        pass
                    elif token in [ZmeiLangParser.NL]:
                        self.state = 1791
                        self.match(ZmeiLangParser.NL)
                        pass
                    elif token in [ZmeiLangParser.COMA]:
                        self.state = 1792
                        self.match(ZmeiLangParser.COMA)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 1797
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,170,self._ctx)

            self.state = 1801
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,171,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1798
                    self.match(ZmeiLangParser.NL) 
                self.state = 1803
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,171,self._ctx)

            self.state = 1806
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,172,self._ctx)
            if la_ == 1:
                self.state = 1804
                self.an_crud_next_page()

            elif la_ == 2:
                self.state = 1805
                self.an_crud_next_page_url()


            self.state = 1811
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,173,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1808
                    self.match(ZmeiLangParser.NL) 
                self.state = 1813
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,173,self._ctx)

            self.state = 1817
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 53)) & ~0x3f) == 0 and ((1 << (_la - 53)) & ((1 << (ZmeiLangParser.KW_DELETE - 53)) | (1 << (ZmeiLangParser.KW_EDIT - 53)) | (1 << (ZmeiLangParser.KW_CREATE - 53)) | (1 << (ZmeiLangParser.KW_DETAIL - 53)) | (1 << (ZmeiLangParser.KW_LIST - 53)))) != 0):
                self.state = 1814
                self.an_crud_page_override()
                self.state = 1819
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1823
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 1820
                self.match(ZmeiLangParser.NL)
                self.state = 1825
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1826
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
        self.enterRule(localctx, 388, self.RULE_an_crud_page_override)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1828
            self.an_crud_view_name()
            self.state = 1832
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 1829
                self.match(ZmeiLangParser.NL)
                self.state = 1834
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1835
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1839
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,177,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1836
                    self.match(ZmeiLangParser.NL) 
                self.state = 1841
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,177,self._ctx)

            self.state = 1842
            self.page_body()
            self.state = 1846
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 1843
                self.match(ZmeiLangParser.NL)
                self.state = 1848
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1849
            self.match(ZmeiLangParser.BRACE_CLOSE)
            self.state = 1853
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,179,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1850
                    self.match(ZmeiLangParser.NL) 
                self.state = 1855
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,179,self._ctx)

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
        self.enterRule(localctx, 390, self.RULE_an_crud_descriptor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1856
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
        self.enterRule(localctx, 392, self.RULE_an_crud_next_page)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1862
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1858
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1859
                self.an_crud_next_page_event_name()
                self.state = 1860
                self.match(ZmeiLangParser.BRACE_CLOSE)


            self.state = 1864
            self.match(ZmeiLangParser.EQUALS)
            self.state = 1865
            self.match(ZmeiLangParser.GT)
            self.state = 1866
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
        self.enterRule(localctx, 394, self.RULE_an_crud_next_page_event_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1868
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.KW_DELETE) | (1 << ZmeiLangParser.KW_EDIT) | (1 << ZmeiLangParser.KW_CREATE))) != 0)):
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
        self.enterRule(localctx, 396, self.RULE_an_crud_next_page_url)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1874
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1870
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1871
                self.an_crud_next_page_event_name()
                self.state = 1872
                self.match(ZmeiLangParser.BRACE_CLOSE)


            self.state = 1876
            self.match(ZmeiLangParser.EQUALS)
            self.state = 1877
            self.match(ZmeiLangParser.GT)
            self.state = 1878
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
        self.enterRule(localctx, 398, self.RULE_an_crud_next_page_url_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1880
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
        self.enterRule(localctx, 400, self.RULE_an_crud_target_model)
        try:
            self.state = 1884
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.HASH]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1882
                self.model_ref()
                pass
            elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1883
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
        self.enterRule(localctx, 402, self.RULE_an_crud_target_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1886
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
        self.enterRule(localctx, 404, self.RULE_an_crud_theme)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1888
            self.match(ZmeiLangParser.KW_THEME)
            self.state = 1889
            self.match(ZmeiLangParser.COLON)
            self.state = 1890
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
        self.enterRule(localctx, 406, self.RULE_an_crud_url_prefix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1892
            self.match(ZmeiLangParser.KW_URL_PREFIX)
            self.state = 1893
            self.match(ZmeiLangParser.COLON)
            self.state = 1894
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
        self.enterRule(localctx, 408, self.RULE_an_crud_url_prefix_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1896
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
        self.enterRule(localctx, 410, self.RULE_an_crud_link_suffix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1898
            self.match(ZmeiLangParser.KW_LINK_SUFFIX)
            self.state = 1899
            self.match(ZmeiLangParser.COLON)
            self.state = 1900
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
        self.enterRule(localctx, 412, self.RULE_an_crud_link_suffix_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1902
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
        self.enterRule(localctx, 414, self.RULE_an_crud_item_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1904
            self.match(ZmeiLangParser.KW_ITEM_NAME)
            self.state = 1905
            self.match(ZmeiLangParser.COLON)
            self.state = 1906
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
        self.enterRule(localctx, 416, self.RULE_an_crud_object_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1908
            self.match(ZmeiLangParser.KW_OBJECT_EXPR)
            self.state = 1912
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.ASSIGN]:
                self.state = 1909
                self.code_line()
                pass
            elif token in [ZmeiLangParser.COLON]:
                self.state = 1910
                self.match(ZmeiLangParser.COLON)
                self.state = 1911
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
        self.enterRule(localctx, 418, self.RULE_an_crud_can_edit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1914
            self.match(ZmeiLangParser.KW_CAN_EDIT)
            self.state = 1918
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.ASSIGN]:
                self.state = 1915
                self.code_line()
                pass
            elif token in [ZmeiLangParser.COLON]:
                self.state = 1916
                self.match(ZmeiLangParser.COLON)
                self.state = 1917
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
        self.enterRule(localctx, 420, self.RULE_an_crud_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1920
            self.match(ZmeiLangParser.KW_BLOCK)
            self.state = 1921
            self.match(ZmeiLangParser.COLON)
            self.state = 1922
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
        self.enterRule(localctx, 422, self.RULE_an_crud_pk_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1924
            self.match(ZmeiLangParser.KW_PK_PARAM)
            self.state = 1925
            self.match(ZmeiLangParser.COLON)
            self.state = 1926
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
        self.enterRule(localctx, 424, self.RULE_an_crud_skip)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1928
            self.match(ZmeiLangParser.KW_SKIP)
            self.state = 1929
            self.match(ZmeiLangParser.COLON)
            self.state = 1930
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
        self.enterRule(localctx, 426, self.RULE_an_crud_skip_values)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1932
            self.an_crud_view_name()
            self.state = 1937
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,185,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1933
                    self.match(ZmeiLangParser.COMA)
                    self.state = 1934
                    self.an_crud_view_name() 
                self.state = 1939
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,185,self._ctx)

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
        self.enterRule(localctx, 428, self.RULE_an_crud_view_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1940
            _la = self._input.LA(1)
            if not(((((_la - 53)) & ~0x3f) == 0 and ((1 << (_la - 53)) & ((1 << (ZmeiLangParser.KW_DELETE - 53)) | (1 << (ZmeiLangParser.KW_EDIT - 53)) | (1 << (ZmeiLangParser.KW_CREATE - 53)) | (1 << (ZmeiLangParser.KW_DETAIL - 53)) | (1 << (ZmeiLangParser.KW_LIST - 53)))) != 0)):
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
        self.enterRule(localctx, 430, self.RULE_an_crud_fields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1942
            self.match(ZmeiLangParser.KW_FIELDS)
            self.state = 1943
            self.match(ZmeiLangParser.COLON)
            self.state = 1944
            self.an_crud_fields_expr()
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
        self.enterRule(localctx, 432, self.RULE_an_crud_fields_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1946
            self.an_crud_field()
            self.state = 1951
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,186,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1947
                    self.match(ZmeiLangParser.COMA)
                    self.state = 1948
                    self.an_crud_field() 
                self.state = 1953
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,186,self._ctx)

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
        self.enterRule(localctx, 434, self.RULE_an_crud_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1954
            self.an_crud_field_spec()
            self.state = 1956
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 1955
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
        self.enterRule(localctx, 436, self.RULE_an_crud_field_spec)
        self._la = 0 # Token type
        try:
            self.state = 1963
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.STAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1958
                self.match(ZmeiLangParser.STAR)
                pass
            elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID, ZmeiLangParser.EXCLUDE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1960
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.EXCLUDE:
                    self.state = 1959
                    self.match(ZmeiLangParser.EXCLUDE)


                self.state = 1962
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
        self.enterRule(localctx, 438, self.RULE_an_crud_field_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1965
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
        self.enterRule(localctx, 440, self.RULE_an_crud_list_fields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1967
            self.match(ZmeiLangParser.KW_LIST_FIELDS)
            self.state = 1968
            self.match(ZmeiLangParser.COLON)
            self.state = 1969
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
        self.enterRule(localctx, 442, self.RULE_an_crud_list_fields_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1971
            self.an_crud_list_field()
            self.state = 1976
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,190,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1972
                    self.match(ZmeiLangParser.COMA)
                    self.state = 1973
                    self.an_crud_list_field() 
                self.state = 1978
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,190,self._ctx)

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
        self.enterRule(localctx, 444, self.RULE_an_crud_list_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1979
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
        self.enterRule(localctx, 446, self.RULE_an_crud_list_field_spec)
        self._la = 0 # Token type
        try:
            self.state = 1986
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.STAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1981
                self.match(ZmeiLangParser.STAR)
                pass
            elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID, ZmeiLangParser.EXCLUDE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1983
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.EXCLUDE:
                    self.state = 1982
                    self.match(ZmeiLangParser.EXCLUDE)


                self.state = 1985
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
        self.enterRule(localctx, 448, self.RULE_an_crud_edit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1988
            self.match(ZmeiLangParser.AN_CRUD_EDIT)
            self.state = 1989
            self.an_crud_params()
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
        self.enterRule(localctx, 450, self.RULE_an_crud_delete)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1991
            self.match(ZmeiLangParser.AN_CRUD_DELETE)
            self.state = 1992
            self.an_crud_params()
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
        self.enterRule(localctx, 452, self.RULE_an_crud_detail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1994
            self.match(ZmeiLangParser.AN_CRUD_DETAIL)
            self.state = 1995
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
        self.enterRule(localctx, 454, self.RULE_an_menu)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1997
            self.match(ZmeiLangParser.AN_MENU)
            self.state = 1998
            self.match(ZmeiLangParser.DOT)
            self.state = 1999
            self.an_menu_descriptor()
            self.state = 2000
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 2004
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,193,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2001
                    self.match(ZmeiLangParser.NL) 
                self.state = 2006
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,193,self._ctx)

            self.state = 2008 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 2007
                    self.an_menu_item()

                else:
                    raise NoViableAltException(self)
                self.state = 2010 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,194,self._ctx)

            self.state = 2015
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 2012
                self.match(ZmeiLangParser.NL)
                self.state = 2017
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2018
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
        self.enterRule(localctx, 456, self.RULE_an_menu_descriptor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2020
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
        self.enterRule(localctx, 458, self.RULE_an_menu_item)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2023
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COMA:
                self.state = 2022
                self.match(ZmeiLangParser.COMA)


            self.state = 2028
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 2025
                self.match(ZmeiLangParser.NL)
                self.state = 2030
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2032
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.SQ_BRACE_OPEN:
                self.state = 2031
                self.an_menu_item_args()


            self.state = 2034
            self.an_menu_label()
            self.state = 2037
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.ASSIGN]:
                self.state = 2035
                self.an_menu_item_code()
                pass
            elif token in [ZmeiLangParser.COLON]:
                self.state = 2036
                self.an_menu_target()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 2042
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,200,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2039
                    self.match(ZmeiLangParser.NL) 
                self.state = 2044
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,200,self._ctx)

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
        self.enterRule(localctx, 460, self.RULE_an_menu_target)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2045
            self.match(ZmeiLangParser.COLON)
            self.state = 2048
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.KW_PAGE]:
                self.state = 2046
                self.an_menu_item_page()
                pass
            elif token in [ZmeiLangParser.STRING_DQ, ZmeiLangParser.STRING_SQ]:
                self.state = 2047
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
        self.enterRule(localctx, 462, self.RULE_an_menu_item_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2050
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
        self.enterRule(localctx, 464, self.RULE_an_menu_item_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2052
            self.match(ZmeiLangParser.SQ_BRACE_OPEN)
            self.state = 2053
            self.an_menu_item_arg()
            self.state = 2058
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 2054
                self.match(ZmeiLangParser.COMA)
                self.state = 2055
                self.an_menu_item_arg()
                self.state = 2060
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2061
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
        self.enterRule(localctx, 466, self.RULE_an_menu_item_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2063
            self.an_menu_item_arg_key()
            self.state = 2064
            self.match(ZmeiLangParser.EQUALS)
            self.state = 2065
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
        self.enterRule(localctx, 468, self.RULE_an_menu_item_arg_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2067
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
        self.enterRule(localctx, 470, self.RULE_an_menu_item_arg_val)
        try:
            self.state = 2072
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.STRING_DQ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2069
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2070
                self.match(ZmeiLangParser.STRING_SQ)
                pass
            elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2071
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
        self.enterRule(localctx, 472, self.RULE_an_menu_item_url)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2074
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
        self.enterRule(localctx, 474, self.RULE_an_menu_item_page)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2076
            self.match(ZmeiLangParser.KW_PAGE)
            self.state = 2077
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 2078
            self.an_menu_item_page_ref()
            self.state = 2079
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
        self.enterRule(localctx, 476, self.RULE_an_menu_item_page_ref)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2084
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,204,self._ctx)
            if la_ == 1:
                self.state = 2081
                self.id_or_kw()
                self.state = 2082
                self.match(ZmeiLangParser.DOT)


            self.state = 2086
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
        self.enterRule(localctx, 478, self.RULE_an_menu_label)
        try:
            self.state = 2091
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.STRING_DQ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2088
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2089
                self.match(ZmeiLangParser.STRING_SQ)
                pass
            elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2090
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
        self.enterRule(localctx, 480, self.RULE_an_get)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2093
            self.match(ZmeiLangParser.AN_GET)
            self.state = 2095
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 2094
                self.code_block()


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
        self.enterRule(localctx, 482, self.RULE_an_stream)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2097
            self.match(ZmeiLangParser.AN_STREAM)

            self.state = 2098
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 2101 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 2101
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID, ZmeiLangParser.HASH]:
                    self.state = 2099
                    self.an_stream_model()
                    pass
                elif token in [ZmeiLangParser.NL]:
                    self.state = 2100
                    self.match(ZmeiLangParser.NL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 2103 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.WRITE_MODE) | (1 << ZmeiLangParser.BOOL) | (1 << ZmeiLangParser.KW_THEME) | (1 << ZmeiLangParser.KW_CHILD) | (1 << ZmeiLangParser.KW_FILTER_OUT) | (1 << ZmeiLangParser.KW_FILTER_IN) | (1 << ZmeiLangParser.KW_PAGE) | (1 << ZmeiLangParser.KW_LINK_SUFFIX) | (1 << ZmeiLangParser.KW_URL_PREFIX) | (1 << ZmeiLangParser.KW_CAN_EDIT) | (1 << ZmeiLangParser.KW_OBJECT_EXPR) | (1 << ZmeiLangParser.KW_BLOCK) | (1 << ZmeiLangParser.KW_ITEM_NAME) | (1 << ZmeiLangParser.KW_PK_PARAM) | (1 << ZmeiLangParser.KW_LIST_FIELDS) | (1 << ZmeiLangParser.KW_DELETE) | (1 << ZmeiLangParser.KW_EDIT) | (1 << ZmeiLangParser.KW_CREATE) | (1 << ZmeiLangParser.KW_DETAIL) | (1 << ZmeiLangParser.KW_SKIP) | (1 << ZmeiLangParser.KW_FROM) | (1 << ZmeiLangParser.KW_POLY_LIST) | (1 << ZmeiLangParser.KW_CSS) | (1 << ZmeiLangParser.KW_JS) | (1 << ZmeiLangParser.KW_INLINE_TYPE) | (1 << ZmeiLangParser.KW_AUTH_TYPE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ZmeiLangParser.KW_INLINE - 64)) | (1 << (ZmeiLangParser.KW_TYPE - 64)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 64)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 64)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 64)) | (1 << (ZmeiLangParser.KW_QUERY - 64)) | (1 << (ZmeiLangParser.KW_AUTH - 64)) | (1 << (ZmeiLangParser.KW_COUNT - 64)) | (1 << (ZmeiLangParser.KW_I18N - 64)) | (1 << (ZmeiLangParser.KW_EXTRA - 64)) | (1 << (ZmeiLangParser.KW_TABS - 64)) | (1 << (ZmeiLangParser.KW_LIST - 64)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 64)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 64)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 64)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 64)) | (1 << (ZmeiLangParser.KW_FIELDS - 64)) | (1 << (ZmeiLangParser.KW_IMPORT - 64)) | (1 << (ZmeiLangParser.KW_AS - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 64)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 64)) | (1 << (ZmeiLangParser.NL - 64)) | (1 << (ZmeiLangParser.ID - 64)) | (1 << (ZmeiLangParser.HASH - 64)))) != 0)):
                    break

            self.state = 2105
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
        self.enterRule(localctx, 484, self.RULE_an_stream_model)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2107
            self.an_stream_target_model()
            self.state = 2109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 2108
                self.an_stream_target_filter()


            self.state = 2112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.EQUALS:
                self.state = 2111
                self.an_stream_field_list()


            self.state = 2115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COMA:
                self.state = 2114
                self.match(ZmeiLangParser.COMA)


            self.state = 2118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,212,self._ctx)
            if la_ == 1:
                self.state = 2117
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
        self.enterRule(localctx, 486, self.RULE_an_stream_target_model)
        try:
            self.state = 2122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.HASH]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2120
                self.model_ref()
                pass
            elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2121
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
        self.enterRule(localctx, 488, self.RULE_an_stream_target_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2124
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
        self.enterRule(localctx, 490, self.RULE_an_stream_field_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2126
            self.match(ZmeiLangParser.EQUALS)
            self.state = 2127
            self.match(ZmeiLangParser.GT)
            self.state = 2137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.STAR]:
                self.state = 2128
                self.match(ZmeiLangParser.STAR)
                pass
            elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                self.state = 2129
                self.an_stream_field_name()
                self.state = 2134
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,214,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 2130
                        self.match(ZmeiLangParser.COMA)
                        self.state = 2131
                        self.an_stream_field_name() 
                    self.state = 2136
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,214,self._ctx)

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
        self.enterRule(localctx, 492, self.RULE_an_stream_field_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2139
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
        self.enterRule(localctx, 494, self.RULE_an_flutter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2141
            self.match(ZmeiLangParser.AN_FLUTTER)
            self.state = 2147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 2142
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 2144
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.KW_CHILD:
                    self.state = 2143
                    self.an_flutter_child()


                self.state = 2146
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
        self.enterRule(localctx, 496, self.RULE_an_flutter_child)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2149
            self.match(ZmeiLangParser.KW_CHILD)
            self.state = 2150
            self.match(ZmeiLangParser.COLON)
            self.state = 2151
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
        self.enterRule(localctx, 498, self.RULE_an_html)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2153
            self.match(ZmeiLangParser.AN_HTML)
            self.state = 2156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 2154
                self.match(ZmeiLangParser.DOT)
                self.state = 2155
                self.an_html_descriptor()


            self.state = 2158
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
        self.enterRule(localctx, 500, self.RULE_an_html_descriptor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2160
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






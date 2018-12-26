# Generated from /Users/aleksandrrudakov/dev/zmei/generator/grammar/ZmeiLangParser.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\u0094")
        buf.write("\u085c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("\4\u00f8\t\u00f8\4\u00f9\t\u00f9\4\u00fa\t\u00fa\3\2\7")
        buf.write("\2\u01f6\n\2\f\2\16\2\u01f9\13\2\3\2\7\2\u01fc\n\2\f\2")
        buf.write("\16\2\u01ff\13\2\3\2\7\2\u0202\n\2\f\2\16\2\u0205\13\2")
        buf.write("\3\2\5\2\u0208\n\2\3\2\6\2\u020b\n\2\r\2\16\2\u020c\5")
        buf.write("\2\u020f\n\2\3\2\7\2\u0212\n\2\f\2\16\2\u0215\13\2\3\2")
        buf.write("\5\2\u0218\n\2\3\2\6\2\u021b\n\2\r\2\16\2\u021c\5\2\u021f")
        buf.write("\n\2\3\2\7\2\u0222\n\2\f\2\16\2\u0225\13\2\3\2\3\2\3\3")
        buf.write("\6\3\u022a\n\3\r\3\16\3\u022b\3\4\6\4\u022f\n\4\r\4\16")
        buf.write("\4\u0230\3\5\3\5\3\6\3\6\3\7\3\7\5\7\u0239\n\7\3\7\3\7")
        buf.write("\3\7\6\7\u023e\n\7\r\7\16\7\u023f\3\b\5\b\u0243\n\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\7\t\u024a\n\t\f\t\16\t\u024d\13\t\3")
        buf.write("\n\3\n\3\n\5\n\u0252\n\n\3\n\5\n\u0255\n\n\3\13\3\13\3")
        buf.write("\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\7\17\u0262\n\17")
        buf.write("\f\17\16\17\u0265\13\17\3\20\5\20\u0268\n\20\3\20\3\20")
        buf.write("\3\20\3\20\7\20\u026e\n\20\f\20\16\20\u0271\13\20\3\20")
        buf.write("\3\20\3\20\5\20\u0276\n\20\3\20\7\20\u0279\n\20\f\20\16")
        buf.write("\20\u027c\13\20\5\20\u027e\n\20\3\21\5\21\u0281\n\21\3")
        buf.write("\21\3\21\5\21\u0285\n\21\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\5\23\u028d\n\23\3\24\3\24\3\24\3\24\3\25\3\25\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\5\26\u029b\n\26\3\27\3\27\3\27")
        buf.write("\5\27\u02a0\n\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3")
        buf.write("\31\7\31\u02aa\n\31\f\31\16\31\u02ad\13\31\3\32\3\32\3")
        buf.write("\32\5\32\u02b2\n\32\3\33\3\33\3\33\5\33\u02b7\n\33\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\36\3\36\5\36")
        buf.write("\u02c4\n\36\3\37\3\37\3 \3 \5 \u02ca\n \3 \7 \u02cd\n")
        buf.write(" \f \16 \u02d0\13 \3 \7 \u02d3\n \f \16 \u02d6\13 \3 ")
        buf.write("\7 \u02d9\n \f \16 \u02dc\13 \3 \7 \u02df\n \f \16 \u02e2")
        buf.write("\13 \3 \7 \u02e5\n \f \16 \u02e8\13 \3!\3!\3!\6!\u02ed")
        buf.write("\n!\r!\16!\u02ee\3!\5!\u02f2\n!\3\"\3\"\5\"\u02f6\n\"")
        buf.write("\3\"\3\"\5\"\u02fa\n\"\3\"\3\"\3\"\3#\3#\3#\3#\6#\u0303")
        buf.write("\n#\r#\16#\u0304\3$\3$\3$\3$\5$\u030b\n$\3%\3%\3%\5%\u0310")
        buf.write("\n%\3&\3&\3&\3&\3&\5&\u0317\n&\3\'\3\'\3(\7(\u031c\n(")
        buf.write("\f(\16(\u031f\13(\3(\3(\5(\u0323\n(\3(\5(\u0326\n(\3(")
        buf.write("\5(\u0329\n(\3(\6(\u032c\n(\r(\16(\u032d\3(\5(\u0331\n")
        buf.write("(\3)\3)\5)\u0335\n)\3)\3)\3)\5)\u033a\n)\3)\3)\3)\5)\u033f")
        buf.write("\n)\3*\3*\3+\5+\u0344\n+\3+\3+\3,\3,\3,\3-\3-\3.\3.\3")
        buf.write(".\3/\3/\3\60\3\60\3\61\6\61\u0355\n\61\r\61\16\61\u0356")
        buf.write("\3\61\3\61\5\61\u035b\n\61\3\62\3\62\3\62\3\63\3\63\3")
        buf.write("\63\3\64\3\64\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\5\66\u0379\n\66\3\67\3\67\38\38\39\39\3:\3:\3;\3")
        buf.write(";\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3C\3")
        buf.write("C\3C\5C\u0398\nC\3C\3C\5C\u039c\nC\3D\3D\3E\3E\3E\3E\3")
        buf.write("E\7E\u03a5\nE\fE\16E\u03a8\13E\3F\5F\u03ab\nF\3F\3F\3")
        buf.write("G\3G\3G\5G\u03b2\nG\3H\3H\3H\3I\3I\3I\3I\3I\5I\u03bc\n")
        buf.write("I\3J\3J\3J\3J\3J\7J\u03c3\nJ\fJ\16J\u03c6\13J\3K\5K\u03c9")
        buf.write("\nK\3K\3K\3L\3L\3L\5L\u03d0\nL\3M\3M\3M\3N\3N\3N\3N\3")
        buf.write("N\3O\3O\3O\7O\u03dd\nO\fO\16O\u03e0\13O\3P\3P\3Q\3Q\3")
        buf.write("Q\3Q\3Q\5Q\u03e9\nQ\3R\3R\3S\3S\3S\3S\3S\5S\u03f2\nS\3")
        buf.write("T\3T\3U\3U\3U\7U\u03f9\nU\fU\16U\u03fc\13U\3V\3V\3V\3")
        buf.write("V\3W\3W\3X\3X\3X\3Y\7Y\u0408\nY\fY\16Y\u040b\13Y\3Z\3")
        buf.write("Z\3Z\3[\3[\3[\3[\5[\u0414\n[\3[\5[\u0417\n[\3[\3[\3\\")
        buf.write("\3\\\3]\3]\3]\3^\3^\3_\3_\3_\3_\3`\3`\3`\3`\3`\3`\3`\3")
        buf.write("`\3`\3`\3`\3`\3`\3`\3`\5`\u0435\n`\3a\3a\3a\3a\3a\3b\3")
        buf.write("b\3c\3c\3c\3c\3c\3d\3d\3d\7d\u0446\nd\fd\16d\u0449\13")
        buf.write("d\3e\3e\3e\5e\u044e\ne\3e\3e\3e\3e\5e\u0454\ne\3f\3f\3")
        buf.write("f\3f\7f\u045a\nf\ff\16f\u045d\13f\3g\3g\3g\3g\3g\3g\3")
        buf.write("g\3g\3g\3g\3g\3g\7g\u046b\ng\fg\16g\u046e\13g\3h\3h\3")
        buf.write("i\3i\3i\3i\7i\u0476\ni\fi\16i\u0479\13i\3j\3j\3j\7j\u047e")
        buf.write("\nj\fj\16j\u0481\13j\3k\3k\5k\u0485\nk\3k\3k\7k\u0489")
        buf.write("\nk\fk\16k\u048c\13k\3l\3l\5l\u0490\nl\3l\3l\7l\u0494")
        buf.write("\nl\fl\16l\u0497\13l\3m\3m\5m\u049b\nm\3m\3m\7m\u049f")
        buf.write("\nm\fm\16m\u04a2\13m\3n\3n\3n\3n\7n\u04a8\nn\fn\16n\u04ab")
        buf.write("\13n\3o\3o\3o\3o\7o\u04b1\no\fo\16o\u04b4\13o\3p\3p\3")
        buf.write("p\3p\5p\u04ba\np\3p\7p\u04bd\np\fp\16p\u04c0\13p\3q\3")
        buf.write("q\3r\3r\3r\3r\3r\7r\u04c9\nr\fr\16r\u04cc\13r\3r\3r\3")
        buf.write("s\3s\3s\3s\5s\u04d4\ns\3t\3t\3t\3u\3u\3v\3v\3v\3v\7v\u04df")
        buf.write("\nv\fv\16v\u04e2\13v\3w\3w\3w\3w\5w\u04e8\nw\3x\3x\3y")
        buf.write("\3y\3z\3z\3z\3z\3z\6z\u04f3\nz\rz\16z\u04f4\3{\3{\3{\3")
        buf.write("{\3{\3|\3|\3}\3}\3}\3}\3}\3}\7}\u0504\n}\f}\16}\u0507")
        buf.write("\13}\5}\u0509\n}\3}\3}\5}\u050d\n}\3~\3~\3\177\3\177\3")
        buf.write("\u0080\3\u0080\3\u0080\3\u0081\3\u0081\3\u0081\3\u0082")
        buf.write("\3\u0082\3\u0082\3\u0083\3\u0083\3\u0083\3\u0084\3\u0084")
        buf.write("\3\u0084\3\u0085\3\u0085\3\u0085\3\u0086\3\u0086\3\u0086")
        buf.write("\3\u0086\3\u0086\3\u0087\3\u0087\3\u0087\3\u0087\3\u0087")
        buf.write("\3\u0088\3\u0088\3\u0089\3\u0089\3\u0089\3\u0089\3\u0089")
        buf.write("\5\u0089\u0536\n\u0089\3\u008a\3\u008a\3\u008b\3\u008b")
        buf.write("\3\u008b\3\u008b\3\u008b\3\u008b\3\u008b\3\u008b\3\u008b")
        buf.write("\3\u008b\3\u008b\3\u008b\3\u008b\3\u008b\7\u008b\u0548")
        buf.write("\n\u008b\f\u008b\16\u008b\u054b\13\u008b\3\u008b\7\u008b")
        buf.write("\u054e\n\u008b\f\u008b\16\u008b\u0551\13\u008b\3\u008b")
        buf.write("\5\u008b\u0554\n\u008b\3\u008b\7\u008b\u0557\n\u008b\f")
        buf.write("\u008b\16\u008b\u055a\13\u008b\3\u008c\3\u008c\3\u008c")
        buf.write("\7\u008c\u055f\n\u008c\f\u008c\16\u008c\u0562\13\u008c")
        buf.write("\3\u008c\3\u008c\3\u008c\7\u008c\u0567\n\u008c\f\u008c")
        buf.write("\16\u008c\u056a\13\u008c\3\u008c\7\u008c\u056d\n\u008c")
        buf.write("\f\u008c\16\u008c\u0570\13\u008c\3\u008d\3\u008d\3\u008d")
        buf.write("\3\u008d\3\u008d\7\u008d\u0577\n\u008d\f\u008d\16\u008d")
        buf.write("\u057a\13\u008d\3\u008e\3\u008e\3\u008f\3\u008f\3\u0090")
        buf.write("\3\u0090\3\u0090\3\u0090\3\u0090\7\u0090\u0585\n\u0090")
        buf.write("\f\u0090\16\u0090\u0588\13\u0090\3\u0091\3\u0091\3\u0091")
        buf.write("\3\u0091\3\u0091\3\u0091\3\u0091\7\u0091\u0591\n\u0091")
        buf.write("\f\u0091\16\u0091\u0594\13\u0091\3\u0091\5\u0091\u0597")
        buf.write("\n\u0091\3\u0092\3\u0092\3\u0093\3\u0093\3\u0093\3\u0093")
        buf.write("\3\u0094\3\u0094\3\u0094\3\u0094\3\u0095\3\u0095\3\u0095")
        buf.write("\3\u0095\3\u0096\3\u0096\3\u0096\3\u0096\3\u0096\7\u0096")
        buf.write("\u05ac\n\u0096\f\u0096\16\u0096\u05af\13\u0096\3\u0097")
        buf.write("\3\u0097\5\u0097\u05b3\n\u0097\3\u0097\3\u0097\3\u0097")
        buf.write("\3\u0097\3\u0098\3\u0098\3\u0099\3\u0099\3\u009a\3\u009a")
        buf.write("\3\u009a\3\u009a\7\u009a\u05c1\n\u009a\f\u009a\16\u009a")
        buf.write("\u05c4\13\u009a\3\u009b\3\u009b\3\u009b\3\u009b\7\u009b")
        buf.write("\u05ca\n\u009b\f\u009b\16\u009b\u05cd\13\u009b\3\u009c")
        buf.write("\3\u009c\3\u009c\3\u009c\7\u009c\u05d3\n\u009c\f\u009c")
        buf.write("\16\u009c\u05d6\13\u009c\3\u009d\3\u009d\3\u009d\3\u009d")
        buf.write("\7\u009d\u05dc\n\u009d\f\u009d\16\u009d\u05df\13\u009d")
        buf.write("\3\u009e\3\u009e\3\u009e\3\u009e\7\u009e\u05e5\n\u009e")
        buf.write("\f\u009e\16\u009e\u05e8\13\u009e\3\u009f\3\u009f\3\u009f")
        buf.write("\3\u009f\7\u009f\u05ee\n\u009f\f\u009f\16\u009f\u05f1")
        buf.write("\13\u009f\3\u00a0\3\u00a0\7\u00a0\u05f5\n\u00a0\f\u00a0")
        buf.write("\16\u00a0\u05f8\13\u00a0\3\u00a0\3\u00a0\7\u00a0\u05fc")
        buf.write("\n\u00a0\f\u00a0\16\u00a0\u05ff\13\u00a0\3\u00a1\3\u00a1")
        buf.write("\5\u00a1\u0603\n\u00a1\3\u00a1\3\u00a1\5\u00a1\u0607\n")
        buf.write("\u00a1\3\u00a1\3\u00a1\5\u00a1\u060b\n\u00a1\3\u00a1\3")
        buf.write("\u00a1\5\u00a1\u060f\n\u00a1\5\u00a1\u0611\n\u00a1\3\u00a1")
        buf.write("\3\u00a1\5\u00a1\u0615\n\u00a1\3\u00a2\3\u00a2\3\u00a2")
        buf.write("\3\u00a2\3\u00a3\3\u00a3\3\u00a3\3\u00a4\3\u00a4\3\u00a5")
        buf.write("\3\u00a5\5\u00a5\u0622\n\u00a5\3\u00a6\3\u00a6\3\u00a6")
        buf.write("\7\u00a6\u0627\n\u00a6\f\u00a6\16\u00a6\u062a\13\u00a6")
        buf.write("\3\u00a7\3\u00a7\3\u00a7\3\u00a7\3\u00a7\6\u00a7\u0631")
        buf.write("\n\u00a7\r\u00a7\16\u00a7\u0632\3\u00a8\5\u00a8\u0636")
        buf.write("\n\u00a8\3\u00a8\3\u00a8\3\u00a9\3\u00a9\3\u00a9\6\u00a9")
        buf.write("\u063d\n\u00a9\r\u00a9\16\u00a9\u063e\3\u00aa\3\u00aa")
        buf.write("\3\u00aa\3\u00aa\3\u00ab\3\u00ab\5\u00ab\u0647\n\u00ab")
        buf.write("\3\u00ac\3\u00ac\3\u00ac\6\u00ac\u064c\n\u00ac\r\u00ac")
        buf.write("\16\u00ac\u064d\3\u00ac\5\u00ac\u0651\n\u00ac\5\u00ac")
        buf.write("\u0653\n\u00ac\3\u00ad\3\u00ad\3\u00ae\7\u00ae\u0658\n")
        buf.write("\u00ae\f\u00ae\16\u00ae\u065b\13\u00ae\3\u00ae\7\u00ae")
        buf.write("\u065e\n\u00ae\f\u00ae\16\u00ae\u0661\13\u00ae\3\u00ae")
        buf.write("\5\u00ae\u0664\n\u00ae\3\u00ae\7\u00ae\u0667\n\u00ae\f")
        buf.write("\u00ae\16\u00ae\u066a\13\u00ae\3\u00ae\7\u00ae\u066d\n")
        buf.write("\u00ae\f\u00ae\16\u00ae\u0670\13\u00ae\3\u00af\3\u00af")
        buf.write("\3\u00b0\3\u00b0\3\u00b0\3\u00b0\6\u00b0\u0678\n\u00b0")
        buf.write("\r\u00b0\16\u00b0\u0679\3\u00b0\5\u00b0\u067d\n\u00b0")
        buf.write("\3\u00b1\3\u00b1\3\u00b2\3\u00b2\3\u00b3\3\u00b3\3\u00b3")
        buf.write("\5\u00b3\u0686\n\u00b3\3\u00b3\3\u00b3\5\u00b3\u068a\n")
        buf.write("\u00b3\3\u00b3\6\u00b3\u068d\n\u00b3\r\u00b3\16\u00b3")
        buf.write("\u068e\3\u00b3\5\u00b3\u0692\n\u00b3\3\u00b4\3\u00b4\3")
        buf.write("\u00b5\3\u00b5\3\u00b5\7\u00b5\u0699\n\u00b5\f\u00b5\16")
        buf.write("\u00b5\u069c\13\u00b5\3\u00b6\3\u00b6\3\u00b6\3\u00b6")
        buf.write("\3\u00b6\3\u00b6\3\u00b6\3\u00b6\3\u00b6\3\u00b6\3\u00b6")
        buf.write("\3\u00b6\3\u00b6\3\u00b6\3\u00b6\3\u00b6\5\u00b6\u06ae")
        buf.write("\n\u00b6\3\u00b7\3\u00b7\3\u00b7\5\u00b7\u06b3\n\u00b7")
        buf.write("\3\u00b7\3\u00b7\3\u00b8\3\u00b8\3\u00b9\3\u00b9\3\u00ba")
        buf.write("\3\u00ba\3\u00ba\5\u00ba\u06be\n\u00ba\3\u00ba\3\u00ba")
        buf.write("\3\u00bb\3\u00bb\3\u00bc\3\u00bc\5\u00bc\u06c6\n\u00bc")
        buf.write("\3\u00bd\3\u00bd\3\u00bd\3\u00bd\3\u00bd\3\u00be\3\u00be")
        buf.write("\3\u00bf\3\u00bf\5\u00bf\u06d1\n\u00bf\3\u00c0\3\u00c0")
        buf.write("\3\u00c0\3\u00c1\3\u00c1\3\u00c1\3\u00c2\3\u00c2\5\u00c2")
        buf.write("\u06db\n\u00c2\3\u00c2\3\u00c2\7\u00c2\u06df\n\u00c2\f")
        buf.write("\u00c2\16\u00c2\u06e2\13\u00c2\3\u00c2\3\u00c2\5\u00c2")
        buf.write("\u06e6\n\u00c2\3\u00c2\3\u00c2\3\u00c2\3\u00c2\3\u00c2")
        buf.write("\3\u00c2\3\u00c2\3\u00c2\3\u00c2\3\u00c2\3\u00c2\3\u00c2")
        buf.write("\3\u00c2\7\u00c2\u06f5\n\u00c2\f\u00c2\16\u00c2\u06f8")
        buf.write("\13\u00c2\3\u00c2\7\u00c2\u06fb\n\u00c2\f\u00c2\16\u00c2")
        buf.write("\u06fe\13\u00c2\3\u00c2\3\u00c2\5\u00c2\u0702\n\u00c2")
        buf.write("\3\u00c2\7\u00c2\u0705\n\u00c2\f\u00c2\16\u00c2\u0708")
        buf.write("\13\u00c2\3\u00c2\7\u00c2\u070b\n\u00c2\f\u00c2\16\u00c2")
        buf.write("\u070e\13\u00c2\3\u00c2\7\u00c2\u0711\n\u00c2\f\u00c2")
        buf.write("\16\u00c2\u0714\13\u00c2\3\u00c2\3\u00c2\3\u00c3\3\u00c3")
        buf.write("\7\u00c3\u071a\n\u00c3\f\u00c3\16\u00c3\u071d\13\u00c3")
        buf.write("\3\u00c3\3\u00c3\7\u00c3\u0721\n\u00c3\f\u00c3\16\u00c3")
        buf.write("\u0724\13\u00c3\3\u00c3\3\u00c3\7\u00c3\u0728\n\u00c3")
        buf.write("\f\u00c3\16\u00c3\u072b\13\u00c3\3\u00c3\3\u00c3\7\u00c3")
        buf.write("\u072f\n\u00c3\f\u00c3\16\u00c3\u0732\13\u00c3\3\u00c4")
        buf.write("\3\u00c4\3\u00c5\3\u00c5\3\u00c5\3\u00c5\5\u00c5\u073a")
        buf.write("\n\u00c5\3\u00c5\3\u00c5\3\u00c5\3\u00c5\3\u00c6\3\u00c6")
        buf.write("\3\u00c7\3\u00c7\3\u00c7\3\u00c7\5\u00c7\u0746\n\u00c7")
        buf.write("\3\u00c7\3\u00c7\3\u00c7\3\u00c7\3\u00c8\3\u00c8\3\u00c9")
        buf.write("\3\u00c9\3\u00c9\5\u00c9\u0751\n\u00c9\3\u00ca\3\u00ca")
        buf.write("\3\u00cb\3\u00cb\3\u00cb\3\u00cb\3\u00cc\3\u00cc\3\u00cc")
        buf.write("\3\u00cc\3\u00cd\3\u00cd\3\u00ce\3\u00ce\3\u00ce\3\u00ce")
        buf.write("\3\u00cf\3\u00cf\3\u00d0\3\u00d0\3\u00d0\3\u00d0\3\u00d1")
        buf.write("\3\u00d1\3\u00d1\3\u00d1\5\u00d1\u076d\n\u00d1\3\u00d2")
        buf.write("\3\u00d2\3\u00d2\3\u00d2\5\u00d2\u0773\n\u00d2\3\u00d3")
        buf.write("\3\u00d3\3\u00d3\3\u00d3\3\u00d4\3\u00d4\3\u00d4\3\u00d4")
        buf.write("\3\u00d5\3\u00d5\3\u00d5\3\u00d5\3\u00d6\3\u00d6\3\u00d6")
        buf.write("\7\u00d6\u0784\n\u00d6\f\u00d6\16\u00d6\u0787\13\u00d6")
        buf.write("\3\u00d7\3\u00d7\3\u00d8\3\u00d8\3\u00d8\3\u00d8\3\u00d9")
        buf.write("\3\u00d9\3\u00d9\7\u00d9\u0792\n\u00d9\f\u00d9\16\u00d9")
        buf.write("\u0795\13\u00d9\3\u00da\3\u00da\5\u00da\u0799\n\u00da")
        buf.write("\3\u00db\3\u00db\5\u00db\u079d\n\u00db\3\u00db\5\u00db")
        buf.write("\u07a0\n\u00db\3\u00dc\3\u00dc\3\u00dd\3\u00dd\3\u00dd")
        buf.write("\3\u00dd\3\u00de\3\u00de\3\u00de\7\u00de\u07ab\n\u00de")
        buf.write("\f\u00de\16\u00de\u07ae\13\u00de\3\u00df\3\u00df\3\u00e0")
        buf.write("\3\u00e0\5\u00e0\u07b4\n\u00e0\3\u00e0\5\u00e0\u07b7\n")
        buf.write("\u00e0\3\u00e1\3\u00e1\3\u00e1\3\u00e2\3\u00e2\3\u00e2")
        buf.write("\3\u00e3\3\u00e3\3\u00e3\3\u00e4\3\u00e4\3\u00e4\3\u00e4")
        buf.write("\3\u00e4\7\u00e4\u07c7\n\u00e4\f\u00e4\16\u00e4\u07ca")
        buf.write("\13\u00e4\3\u00e4\6\u00e4\u07cd\n\u00e4\r\u00e4\16\u00e4")
        buf.write("\u07ce\3\u00e4\7\u00e4\u07d2\n\u00e4\f\u00e4\16\u00e4")
        buf.write("\u07d5\13\u00e4\3\u00e4\3\u00e4\3\u00e5\3\u00e5\3\u00e6")
        buf.write("\5\u00e6\u07dc\n\u00e6\3\u00e6\7\u00e6\u07df\n\u00e6\f")
        buf.write("\u00e6\16\u00e6\u07e2\13\u00e6\3\u00e6\5\u00e6\u07e5\n")
        buf.write("\u00e6\3\u00e6\3\u00e6\3\u00e6\5\u00e6\u07ea\n\u00e6\3")
        buf.write("\u00e6\7\u00e6\u07ed\n\u00e6\f\u00e6\16\u00e6\u07f0\13")
        buf.write("\u00e6\3\u00e7\3\u00e7\3\u00e7\5\u00e7\u07f5\n\u00e7\3")
        buf.write("\u00e8\3\u00e8\3\u00e9\3\u00e9\3\u00e9\3\u00e9\7\u00e9")
        buf.write("\u07fd\n\u00e9\f\u00e9\16\u00e9\u0800\13\u00e9\3\u00e9")
        buf.write("\3\u00e9\3\u00ea\3\u00ea\3\u00ea\3\u00ea\3\u00eb\3\u00eb")
        buf.write("\3\u00ec\3\u00ec\3\u00ec\5\u00ec\u080d\n\u00ec\3\u00ed")
        buf.write("\3\u00ed\3\u00ee\3\u00ee\3\u00ee\3\u00ee\3\u00ee\3\u00ef")
        buf.write("\3\u00ef\3\u00f0\3\u00f0\3\u00f0\5\u00f0\u081b\n\u00f0")
        buf.write("\3\u00f1\3\u00f1\5\u00f1\u081f\n\u00f1\3\u00f2\3\u00f2")
        buf.write("\3\u00f2\3\u00f2\6\u00f2\u0825\n\u00f2\r\u00f2\16\u00f2")
        buf.write("\u0826\3\u00f2\3\u00f2\3\u00f3\3\u00f3\5\u00f3\u082d\n")
        buf.write("\u00f3\3\u00f3\5\u00f3\u0830\n\u00f3\3\u00f3\5\u00f3\u0833")
        buf.write("\n\u00f3\3\u00f3\5\u00f3\u0836\n\u00f3\3\u00f4\3\u00f4")
        buf.write("\3\u00f4\5\u00f4\u083b\n\u00f4\3\u00f5\3\u00f5\3\u00f6")
        buf.write("\3\u00f6\3\u00f6\3\u00f6\3\u00f6\3\u00f6\7\u00f6\u0845")
        buf.write("\n\u00f6\f\u00f6\16\u00f6\u0848\13\u00f6\5\u00f6\u084a")
        buf.write("\n\u00f6\3\u00f7\3\u00f7\3\u00f8\3\u00f8\3\u00f8\5\u00f8")
        buf.write("\u0851\n\u00f8\3\u00f9\3\u00f9\3\u00f9\5\u00f9\u0856\n")
        buf.write("\u00f9\3\u00f9\3\u00f9\3\u00fa\3\u00fa\3\u00fa\2\2\u00fb")
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
        buf.write("\u01ec\u01ee\u01f0\u01f2\2\17\4\2(jll\3\2\u0085\u0085")
        buf.write("\3\2\u0085\u0086\3\2\u008c\u008d\3\2~\u0083\4\2mmww\5")
        buf.write("\2]]__bb\3\2gi\4\2yy\u0083\u0083\4\2{{\177\177\3\2\23")
        buf.write("\25\3\2\668\4\2\669LL\2\u089a\2\u01f7\3\2\2\2\4\u0229")
        buf.write("\3\2\2\2\6\u022e\3\2\2\2\b\u0232\3\2\2\2\n\u0234\3\2\2")
        buf.write("\2\f\u0238\3\2\2\2\16\u0242\3\2\2\2\20\u0246\3\2\2\2\22")
        buf.write("\u0254\3\2\2\2\24\u0256\3\2\2\2\26\u0258\3\2\2\2\30\u025a")
        buf.write("\3\2\2\2\32\u025c\3\2\2\2\34\u025e\3\2\2\2\36\u027d\3")
        buf.write("\2\2\2 \u0280\3\2\2\2\"\u0286\3\2\2\2$\u028c\3\2\2\2&")
        buf.write("\u028e\3\2\2\2(\u0292\3\2\2\2*\u029a\3\2\2\2,\u029c\3")
        buf.write("\2\2\2.\u02a1\3\2\2\2\60\u02a6\3\2\2\2\62\u02ae\3\2\2")
        buf.write("\2\64\u02b3\3\2\2\2\66\u02b8\3\2\2\28\u02bc\3\2\2\2:\u02be")
        buf.write("\3\2\2\2<\u02c5\3\2\2\2>\u02c7\3\2\2\2@\u02e9\3\2\2\2")
        buf.write("B\u02f3\3\2\2\2D\u02fe\3\2\2\2F\u0306\3\2\2\2H\u030f\3")
        buf.write("\2\2\2J\u0311\3\2\2\2L\u0318\3\2\2\2N\u031d\3\2\2\2P\u033e")
        buf.write("\3\2\2\2R\u0340\3\2\2\2T\u0343\3\2\2\2V\u0347\3\2\2\2")
        buf.write("X\u034a\3\2\2\2Z\u034c\3\2\2\2\\\u034f\3\2\2\2^\u0351")
        buf.write("\3\2\2\2`\u035a\3\2\2\2b\u035c\3\2\2\2d\u035f\3\2\2\2")
        buf.write("f\u0362\3\2\2\2h\u0364\3\2\2\2j\u0378\3\2\2\2l\u037a\3")
        buf.write("\2\2\2n\u037c\3\2\2\2p\u037e\3\2\2\2r\u0380\3\2\2\2t\u0382")
        buf.write("\3\2\2\2v\u0384\3\2\2\2x\u0386\3\2\2\2z\u0388\3\2\2\2")
        buf.write("|\u038a\3\2\2\2~\u038c\3\2\2\2\u0080\u038e\3\2\2\2\u0082")
        buf.write("\u0390\3\2\2\2\u0084\u0392\3\2\2\2\u0086\u039d\3\2\2\2")
        buf.write("\u0088\u039f\3\2\2\2\u008a\u03aa\3\2\2\2\u008c\u03b1\3")
        buf.write("\2\2\2\u008e\u03b3\3\2\2\2\u0090\u03b6\3\2\2\2\u0092\u03bd")
        buf.write("\3\2\2\2\u0094\u03c8\3\2\2\2\u0096\u03cf\3\2\2\2\u0098")
        buf.write("\u03d1\3\2\2\2\u009a\u03d4\3\2\2\2\u009c\u03d9\3\2\2\2")
        buf.write("\u009e\u03e1\3\2\2\2\u00a0\u03e3\3\2\2\2\u00a2\u03ea\3")
        buf.write("\2\2\2\u00a4\u03ec\3\2\2\2\u00a6\u03f3\3\2\2\2\u00a8\u03f5")
        buf.write("\3\2\2\2\u00aa\u03fd\3\2\2\2\u00ac\u0401\3\2\2\2\u00ae")
        buf.write("\u0403\3\2\2\2\u00b0\u0409\3\2\2\2\u00b2\u040c\3\2\2\2")
        buf.write("\u00b4\u040f\3\2\2\2\u00b6\u041a\3\2\2\2\u00b8\u041c\3")
        buf.write("\2\2\2\u00ba\u041f\3\2\2\2\u00bc\u0421\3\2\2\2\u00be\u0434")
        buf.write("\3\2\2\2\u00c0\u0436\3\2\2\2\u00c2\u043b\3\2\2\2\u00c4")
        buf.write("\u043d\3\2\2\2\u00c6\u0442\3\2\2\2\u00c8\u044a\3\2\2\2")
        buf.write("\u00ca\u0455\3\2\2\2\u00cc\u046c\3\2\2\2\u00ce\u046f\3")
        buf.write("\2\2\2\u00d0\u0471\3\2\2\2\u00d2\u047a\3\2\2\2\u00d4\u0482")
        buf.write("\3\2\2\2\u00d6\u048d\3\2\2\2\u00d8\u0498\3\2\2\2\u00da")
        buf.write("\u04a3\3\2\2\2\u00dc\u04ac\3\2\2\2\u00de\u04b5\3\2\2\2")
        buf.write("\u00e0\u04c1\3\2\2\2\u00e2\u04c3\3\2\2\2\u00e4\u04cf\3")
        buf.write("\2\2\2\u00e6\u04d5\3\2\2\2\u00e8\u04d8\3\2\2\2\u00ea\u04da")
        buf.write("\3\2\2\2\u00ec\u04e3\3\2\2\2\u00ee\u04e9\3\2\2\2\u00f0")
        buf.write("\u04eb\3\2\2\2\u00f2\u04ed\3\2\2\2\u00f4\u04f6\3\2\2\2")
        buf.write("\u00f6\u04fb\3\2\2\2\u00f8\u04fd\3\2\2\2\u00fa\u050e\3")
        buf.write("\2\2\2\u00fc\u0510\3\2\2\2\u00fe\u0512\3\2\2\2\u0100\u0515")
        buf.write("\3\2\2\2\u0102\u0518\3\2\2\2\u0104\u051b\3\2\2\2\u0106")
        buf.write("\u051e\3\2\2\2\u0108\u0521\3\2\2\2\u010a\u0524\3\2\2\2")
        buf.write("\u010c\u0529\3\2\2\2\u010e\u052e\3\2\2\2\u0110\u0530\3")
        buf.write("\2\2\2\u0112\u0537\3\2\2\2\u0114\u0539\3\2\2\2\u0116\u055b")
        buf.write("\3\2\2\2\u0118\u0571\3\2\2\2\u011a\u057b\3\2\2\2\u011c")
        buf.write("\u057d\3\2\2\2\u011e\u057f\3\2\2\2\u0120\u0589\3\2\2\2")
        buf.write("\u0122\u0598\3\2\2\2\u0124\u059a\3\2\2\2\u0126\u059e\3")
        buf.write("\2\2\2\u0128\u05a2\3\2\2\2\u012a\u05a6\3\2\2\2\u012c\u05b0")
        buf.write("\3\2\2\2\u012e\u05b8\3\2\2\2\u0130\u05ba\3\2\2\2\u0132")
        buf.write("\u05bc\3\2\2\2\u0134\u05c5\3\2\2\2\u0136\u05ce\3\2\2\2")
        buf.write("\u0138\u05d7\3\2\2\2\u013a\u05e0\3\2\2\2\u013c\u05e9\3")
        buf.write("\2\2\2\u013e\u05f2\3\2\2\2\u0140\u0600\3\2\2\2\u0142\u0616")
        buf.write("\3\2\2\2\u0144\u061a\3\2\2\2\u0146\u061d\3\2\2\2\u0148")
        buf.write("\u0621\3\2\2\2\u014a\u0623\3\2\2\2\u014c\u0630\3\2\2\2")
        buf.write("\u014e\u0635\3\2\2\2\u0150\u063c\3\2\2\2\u0152\u0640\3")
        buf.write("\2\2\2\u0154\u0646\3\2\2\2\u0156\u0652\3\2\2\2\u0158\u0654")
        buf.write("\3\2\2\2\u015a\u0659\3\2\2\2\u015c\u0671\3\2\2\2\u015e")
        buf.write("\u0673\3\2\2\2\u0160\u067e\3\2\2\2\u0162\u0680\3\2\2\2")
        buf.write("\u0164\u0682\3\2\2\2\u0166\u0693\3\2\2\2\u0168\u0695\3")
        buf.write("\2\2\2\u016a\u06ad\3\2\2\2\u016c\u06af\3\2\2\2\u016e\u06b6")
        buf.write("\3\2\2\2\u0170\u06b8\3\2\2\2\u0172\u06ba\3\2\2\2\u0174")
        buf.write("\u06c1\3\2\2\2\u0176\u06c3\3\2\2\2\u0178\u06c7\3\2\2\2")
        buf.write("\u017a\u06cc\3\2\2\2\u017c\u06ce\3\2\2\2\u017e\u06d2\3")
        buf.write("\2\2\2\u0180\u06d5\3\2\2\2\u0182\u06da\3\2\2\2\u0184\u0717")
        buf.write("\3\2\2\2\u0186\u0733\3\2\2\2\u0188\u0739\3\2\2\2\u018a")
        buf.write("\u073f\3\2\2\2\u018c\u0745\3\2\2\2\u018e\u074b\3\2\2\2")
        buf.write("\u0190\u0750\3\2\2\2\u0192\u0752\3\2\2\2\u0194\u0754\3")
        buf.write("\2\2\2\u0196\u0758\3\2\2\2\u0198\u075c\3\2\2\2\u019a\u075e")
        buf.write("\3\2\2\2\u019c\u0762\3\2\2\2\u019e\u0764\3\2\2\2\u01a0")
        buf.write("\u0768\3\2\2\2\u01a2\u076e\3\2\2\2\u01a4\u0774\3\2\2\2")
        buf.write("\u01a6\u0778\3\2\2\2\u01a8\u077c\3\2\2\2\u01aa\u0780\3")
        buf.write("\2\2\2\u01ac\u0788\3\2\2\2\u01ae\u078a\3\2\2\2\u01b0\u078e")
        buf.write("\3\2\2\2\u01b2\u0796\3\2\2\2\u01b4\u079f\3\2\2\2\u01b6")
        buf.write("\u07a1\3\2\2\2\u01b8\u07a3\3\2\2\2\u01ba\u07a7\3\2\2\2")
        buf.write("\u01bc\u07af\3\2\2\2\u01be\u07b6\3\2\2\2\u01c0\u07b8\3")
        buf.write("\2\2\2\u01c2\u07bb\3\2\2\2\u01c4\u07be\3\2\2\2\u01c6\u07c1")
        buf.write("\3\2\2\2\u01c8\u07d8\3\2\2\2\u01ca\u07db\3\2\2\2\u01cc")
        buf.write("\u07f1\3\2\2\2\u01ce\u07f6\3\2\2\2\u01d0\u07f8\3\2\2\2")
        buf.write("\u01d2\u0803\3\2\2\2\u01d4\u0807\3\2\2\2\u01d6\u080c\3")
        buf.write("\2\2\2\u01d8\u080e\3\2\2\2\u01da\u0810\3\2\2\2\u01dc\u0815")
        buf.write("\3\2\2\2\u01de\u081a\3\2\2\2\u01e0\u081c\3\2\2\2\u01e2")
        buf.write("\u0820\3\2\2\2\u01e4\u082a\3\2\2\2\u01e6\u083a\3\2\2\2")
        buf.write("\u01e8\u083c\3\2\2\2\u01ea\u083e\3\2\2\2\u01ec\u084b\3")
        buf.write("\2\2\2\u01ee\u084d\3\2\2\2\u01f0\u0852\3\2\2\2\u01f2\u0859")
        buf.write("\3\2\2\2\u01f4\u01f6\7k\2\2\u01f5\u01f4\3\2\2\2\u01f6")
        buf.write("\u01f9\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f7\u01f8\3\2\2\2")
        buf.write("\u01f8\u01fd\3\2\2\2\u01f9\u01f7\3\2\2\2\u01fa\u01fc\5")
        buf.write("*\26\2\u01fb\u01fa\3\2\2\2\u01fc\u01ff\3\2\2\2\u01fd\u01fb")
        buf.write("\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe\u0203\3\2\2\2\u01ff")
        buf.write("\u01fd\3\2\2\2\u0200\u0202\7k\2\2\u0201\u0200\3\2\2\2")
        buf.write("\u0202\u0205\3\2\2\2\u0203\u0201\3\2\2\2\u0203\u0204\3")
        buf.write("\2\2\2\u0204\u020e\3\2\2\2\u0205\u0203\3\2\2\2\u0206\u0208")
        buf.write("\5\4\3\2\u0207\u0206\3\2\2\2\u0207\u0208\3\2\2\2\u0208")
        buf.write("\u020a\3\2\2\2\u0209\u020b\5\u013e\u00a0\2\u020a\u0209")
        buf.write("\3\2\2\2\u020b\u020c\3\2\2\2\u020c\u020a\3\2\2\2\u020c")
        buf.write("\u020d\3\2\2\2\u020d\u020f\3\2\2\2\u020e\u0207\3\2\2\2")
        buf.write("\u020e\u020f\3\2\2\2\u020f\u0213\3\2\2\2\u0210\u0212\7")
        buf.write("k\2\2\u0211\u0210\3\2\2\2\u0212\u0215\3\2\2\2\u0213\u0211")
        buf.write("\3\2\2\2\u0213\u0214\3\2\2\2\u0214\u021e\3\2\2\2\u0215")
        buf.write("\u0213\3\2\2\2\u0216\u0218\5\6\4\2\u0217\u0216\3\2\2\2")
        buf.write("\u0217\u0218\3\2\2\2\u0218\u021a\3\2\2\2\u0219\u021b\5")
        buf.write("> \2\u021a\u0219\3\2\2\2\u021b\u021c\3\2\2\2\u021c\u021a")
        buf.write("\3\2\2\2\u021c\u021d\3\2\2\2\u021d\u021f\3\2\2\2\u021e")
        buf.write("\u0217\3\2\2\2\u021e\u021f\3\2\2\2\u021f\u0223\3\2\2\2")
        buf.write("\u0220\u0222\7k\2\2\u0221\u0220\3\2\2\2\u0222\u0225\3")
        buf.write("\2\2\2\u0223\u0221\3\2\2\2\u0223\u0224\3\2\2\2\u0224\u0226")
        buf.write("\3\2\2\2\u0225\u0223\3\2\2\2\u0226\u0227\7\2\2\3\u0227")
        buf.write("\3\3\2\2\2\u0228\u022a\5\b\5\2\u0229\u0228\3\2\2\2\u022a")
        buf.write("\u022b\3\2\2\2\u022b\u0229\3\2\2\2\u022b\u022c\3\2\2\2")
        buf.write("\u022c\5\3\2\2\2\u022d\u022f\5\n\6\2\u022e\u022d\3\2\2")
        buf.write("\2\u022f\u0230\3\2\2\2\u0230\u022e\3\2\2\2\u0230\u0231")
        buf.write("\3\2\2\2\u0231\7\3\2\2\2\u0232\u0233\5\f\7\2\u0233\t\3")
        buf.write("\2\2\2\u0234\u0235\5\f\7\2\u0235\13\3\2\2\2\u0236\u0237")
        buf.write("\7;\2\2\u0237\u0239\5\16\b\2\u0238\u0236\3\2\2\2\u0238")
        buf.write("\u0239\3\2\2\2\u0239\u023a\3\2\2\2\u023a\u023b\7R\2\2")
        buf.write("\u023b\u023d\5\20\t\2\u023c\u023e\7k\2\2\u023d\u023c\3")
        buf.write("\2\2\2\u023e\u023f\3\2\2\2\u023f\u023d\3\2\2\2\u023f\u0240")
        buf.write("\3\2\2\2\u0240\r\3\2\2\2\u0241\u0243\7{\2\2\u0242\u0241")
        buf.write("\3\2\2\2\u0242\u0243\3\2\2\2\u0243\u0244\3\2\2\2\u0244")
        buf.write("\u0245\5\34\17\2\u0245\17\3\2\2\2\u0246\u024b\5\22\n\2")
        buf.write("\u0247\u0248\7z\2\2\u0248\u024a\5\22\n\2\u0249\u0247\3")
        buf.write("\2\2\2\u024a\u024d\3\2\2\2\u024b\u0249\3\2\2\2\u024b\u024c")
        buf.write("\3\2\2\2\u024c\21\3\2\2\2\u024d\u024b\3\2\2\2\u024e\u0251")
        buf.write("\5\24\13\2\u024f\u0250\7S\2\2\u0250\u0252\5\26\f\2\u0251")
        buf.write("\u024f\3\2\2\2\u0251\u0252\3\2\2\2\u0252\u0255\3\2\2\2")
        buf.write("\u0253\u0255\5\30\r\2\u0254\u024e\3\2\2\2\u0254\u0253")
        buf.write("\3\2\2\2\u0255\23\3\2\2\2\u0256\u0257\5\34\17\2\u0257")
        buf.write("\25\3\2\2\2\u0258\u0259\5\32\16\2\u0259\27\3\2\2\2\u025a")
        buf.write("\u025b\7\u0082\2\2\u025b\31\3\2\2\2\u025c\u025d\t\2\2")
        buf.write("\2\u025d\33\3\2\2\2\u025e\u0263\5\32\16\2\u025f\u0260")
        buf.write("\7{\2\2\u0260\u0262\5\32\16\2\u0261\u025f\3\2\2\2\u0262")
        buf.write("\u0265\3\2\2\2\u0263\u0261\3\2\2\2\u0263\u0264\3\2\2\2")
        buf.write("\u0264\35\3\2\2\2\u0265\u0263\3\2\2\2\u0266\u0268\7{\2")
        buf.write("\2\u0267\u0266\3\2\2\2\u0267\u0268\3\2\2\2\u0268\u0269")
        buf.write("\3\2\2\2\u0269\u026f\7\u0082\2\2\u026a\u026b\7z\2\2\u026b")
        buf.write("\u026c\7r\2\2\u026c\u026e\5 \21\2\u026d\u026a\3\2\2\2")
        buf.write("\u026e\u0271\3\2\2\2\u026f\u026d\3\2\2\2\u026f\u0270\3")
        buf.write("\2\2\2\u0270\u027e\3\2\2\2\u0271\u026f\3\2\2\2\u0272\u027a")
        buf.write("\5\32\16\2\u0273\u0275\7z\2\2\u0274\u0276\7r\2\2\u0275")
        buf.write("\u0274\3\2\2\2\u0275\u0276\3\2\2\2\u0276\u0277\3\2\2\2")
        buf.write("\u0277\u0279\5 \21\2\u0278\u0273\3\2\2\2\u0279\u027c\3")
        buf.write("\2\2\2\u027a\u0278\3\2\2\2\u027a\u027b\3\2\2\2\u027b\u027e")
        buf.write("\3\2\2\2\u027c\u027a\3\2\2\2\u027d\u0267\3\2\2\2\u027d")
        buf.write("\u0272\3\2\2\2\u027e\37\3\2\2\2\u027f\u0281\7\u0082\2")
        buf.write("\2\u0280\u027f\3\2\2\2\u0280\u0281\3\2\2\2\u0281\u0282")
        buf.write("\3\2\2\2\u0282\u0284\5\32\16\2\u0283\u0285\7\u0082\2\2")
        buf.write("\u0284\u0283\3\2\2\2\u0284\u0285\3\2\2\2\u0285!\3\2\2")
        buf.write("\2\u0286\u0287\7u\2\2\u0287\u0288\7(\2\2\u0288\u0289\7")
        buf.write("v\2\2\u0289#\3\2\2\2\u028a\u028d\5(\25\2\u028b\u028d\5")
        buf.write("&\24\2\u028c\u028a\3\2\2\2\u028c\u028b\3\2\2\2\u028d%")
        buf.write("\3\2\2\2\u028e\u028f\7\u008c\2\2\u028f\u0290\7\u0090\2")
        buf.write("\2\u0290\u0291\7k\2\2\u0291\'\3\2\2\2\u0292\u0293\7\u008e")
        buf.write("\2\2\u0293)\3\2\2\2\u0294\u029b\5:\36\2\u0295\u029b\5")
        buf.write("\66\34\2\u0296\u029b\5\64\33\2\u0297\u029b\5\62\32\2\u0298")
        buf.write("\u029b\5.\30\2\u0299\u029b\7k\2\2\u029a\u0294\3\2\2\2")
        buf.write("\u029a\u0295\3\2\2\2\u029a\u0296\3\2\2\2\u029a\u0297\3")
        buf.write("\2\2\2\u029a\u0298\3\2\2\2\u029a\u0299\3\2\2\2\u029b+")
        buf.write("\3\2\2\2\u029c\u029f\7%\2\2\u029d\u029e\7s\2\2\u029e\u02a0")
        buf.write("\7t\2\2\u029f\u029d\3\2\2\2\u029f\u02a0\3\2\2\2\u02a0")
        buf.write("-\3\2\2\2\u02a1\u02a2\7$\2\2\u02a2\u02a3\7s\2\2\u02a3")
        buf.write("\u02a4\5\60\31\2\u02a4\u02a5\7t\2\2\u02a5/\3\2\2\2\u02a6")
        buf.write("\u02ab\7l\2\2\u02a7\u02a8\7z\2\2\u02a8\u02aa\7l\2\2\u02a9")
        buf.write("\u02a7\3\2\2\2\u02aa\u02ad\3\2\2\2\u02ab\u02a9\3\2\2\2")
        buf.write("\u02ab\u02ac\3\2\2\2\u02ac\61\3\2\2\2\u02ad\u02ab\3\2")
        buf.write("\2\2\u02ae\u02b1\7\16\2\2\u02af\u02b0\7s\2\2\u02b0\u02b2")
        buf.write("\7t\2\2\u02b1\u02af\3\2\2\2\u02b1\u02b2\3\2\2\2\u02b2")
        buf.write("\63\3\2\2\2\u02b3\u02b6\7\6\2\2\u02b4\u02b5\7s\2\2\u02b5")
        buf.write("\u02b7\7t\2\2\u02b6\u02b4\3\2\2\2\u02b6\u02b7\3\2\2\2")
        buf.write("\u02b7\65\3\2\2\2\u02b8\u02b9\7\4\2\2\u02b9\u02ba\58\35")
        buf.write("\2\u02ba\u02bb\5$\23\2\u02bb\67\3\2\2\2\u02bc\u02bd\t")
        buf.write("\3\2\2\u02bd9\3\2\2\2\u02be\u02c3\7\'\2\2\u02bf\u02c0")
        buf.write("\7s\2\2\u02c0\u02c1\5<\37\2\u02c1\u02c2\7t\2\2\u02c2\u02c4")
        buf.write("\3\2\2\2\u02c3\u02bf\3\2\2\2\u02c3\u02c4\3\2\2\2\u02c4")
        buf.write(";\3\2\2\2\u02c5\u02c6\t\4\2\2\u02c6=\3\2\2\2\u02c7\u02c9")
        buf.write("\5B\"\2\u02c8\u02ca\5@!\2\u02c9\u02c8\3\2\2\2\u02c9\u02ca")
        buf.write("\3\2\2\2\u02ca\u02ce\3\2\2\2\u02cb\u02cd\7k\2\2\u02cc")
        buf.write("\u02cb\3\2\2\2\u02cd\u02d0\3\2\2\2\u02ce\u02cc\3\2\2\2")
        buf.write("\u02ce\u02cf\3\2\2\2\u02cf\u02d4\3\2\2\2\u02d0\u02ce\3")
        buf.write("\2\2\2\u02d1\u02d3\5N(\2\u02d2\u02d1\3\2\2\2\u02d3\u02d6")
        buf.write("\3\2\2\2\u02d4\u02d2\3\2\2\2\u02d4\u02d5\3\2\2\2\u02d5")
        buf.write("\u02da\3\2\2\2\u02d6\u02d4\3\2\2\2\u02d7\u02d9\7k\2\2")
        buf.write("\u02d8\u02d7\3\2\2\2\u02d9\u02dc\3\2\2\2\u02da\u02d8\3")
        buf.write("\2\2\2\u02da\u02db\3\2\2\2\u02db\u02e0\3\2\2\2\u02dc\u02da")
        buf.write("\3\2\2\2\u02dd\u02df\5\u00be`\2\u02de\u02dd\3\2\2\2\u02df")
        buf.write("\u02e2\3\2\2\2\u02e0\u02de\3\2\2\2\u02e0\u02e1\3\2\2\2")
        buf.write("\u02e1\u02e6\3\2\2\2\u02e2\u02e0\3\2\2\2\u02e3\u02e5\7")
        buf.write("k\2\2\u02e4\u02e3\3\2\2\2\u02e5\u02e8\3\2\2\2\u02e6\u02e4")
        buf.write("\3\2\2\2\u02e6\u02e7\3\2\2\2\u02e7?\3\2\2\2\u02e8\u02e6")
        buf.write("\3\2\2\2\u02e9\u02ea\7~\2\2\u02ea\u02f1\t\4\2\2\u02eb")
        buf.write("\u02ed\7k\2\2\u02ec\u02eb\3\2\2\2\u02ed\u02ee\3\2\2\2")
        buf.write("\u02ee\u02ec\3\2\2\2\u02ee\u02ef\3\2\2\2\u02ef\u02f2\3")
        buf.write("\2\2\2\u02f0\u02f2\7\2\2\3\u02f1\u02ec\3\2\2\2\u02f1\u02f0")
        buf.write("\3\2\2\2\u02f2A\3\2\2\2\u02f3\u02f5\7|\2\2\u02f4\u02f6")
        buf.write("\5J&\2\u02f5\u02f4\3\2\2\2\u02f5\u02f6\3\2\2\2\u02f6\u02f7")
        buf.write("\3\2\2\2\u02f7\u02f9\5L\'\2\u02f8\u02fa\5F$\2\u02f9\u02f8")
        buf.write("\3\2\2\2\u02f9\u02fa\3\2\2\2\u02fa\u02fb\3\2\2\2\u02fb")
        buf.write("\u02fc\5D#\2\u02fc\u02fd\7k\2\2\u02fdC\3\2\2\2\u02fe\u02ff")
        buf.write("\7k\2\2\u02ff\u0300\7y\2\2\u0300\u0302\7y\2\2\u0301\u0303")
        buf.write("\7y\2\2\u0302\u0301\3\2\2\2\u0303\u0304\3\2\2\2\u0304")
        buf.write("\u0302\3\2\2\2\u0304\u0305\3\2\2\2\u0305E\3\2\2\2\u0306")
        buf.write("\u0307\7q\2\2\u0307\u030a\5H%\2\u0308\u0309\7}\2\2\u0309")
        buf.write("\u030b\5H%\2\u030a\u0308\3\2\2\2\u030a\u030b\3\2\2\2\u030b")
        buf.write("G\3\2\2\2\u030c\u0310\5\32\16\2\u030d\u0310\7\u0085\2")
        buf.write("\2\u030e\u0310\7\u0086\2\2\u030f\u030c\3\2\2\2\u030f\u030d")
        buf.write("\3\2\2\2\u030f\u030e\3\2\2\2\u0310I\3\2\2\2\u0311\u0316")
        buf.write("\5\32\16\2\u0312\u0313\7y\2\2\u0313\u0317\7p\2\2\u0314")
        buf.write("\u0315\7\u0083\2\2\u0315\u0317\7p\2\2\u0316\u0312\3\2")
        buf.write("\2\2\u0316\u0314\3\2\2\2\u0317K\3\2\2\2\u0318\u0319\5")
        buf.write("\32\16\2\u0319M\3\2\2\2\u031a\u031c\5h\65\2\u031b\u031a")
        buf.write("\3\2\2\2\u031c\u031f\3\2\2\2\u031d\u031b\3\2\2\2\u031d")
        buf.write("\u031e\3\2\2\2\u031e\u0320\3\2\2\2\u031f\u031d\3\2\2\2")
        buf.write("\u0320\u0322\5f\64\2\u0321\u0323\5P)\2\u0322\u0321\3\2")
        buf.write("\2\2\u0322\u0323\3\2\2\2\u0323\u0325\3\2\2\2\u0324\u0326")
        buf.write("\5d\63\2\u0325\u0324\3\2\2\2\u0325\u0326\3\2\2\2\u0326")
        buf.write("\u0328\3\2\2\2\u0327\u0329\5b\62\2\u0328\u0327\3\2\2\2")
        buf.write("\u0328\u0329\3\2\2\2\u0329\u0330\3\2\2\2\u032a\u032c\7")
        buf.write("k\2\2\u032b\u032a\3\2\2\2\u032c\u032d\3\2\2\2\u032d\u032b")
        buf.write("\3\2\2\2\u032d\u032e\3\2\2\2\u032e\u0331\3\2\2\2\u032f")
        buf.write("\u0331\7\2\2\3\u0330\u032b\3\2\2\2\u0330\u032f\3\2\2\2")
        buf.write("\u0331O\3\2\2\2\u0332\u0334\7q\2\2\u0333\u0335\5R*\2\u0334")
        buf.write("\u0333\3\2\2\2\u0334\u0335\3\2\2\2\u0335\u033f\3\2\2\2")
        buf.write("\u0336\u0337\7q\2\2\u0337\u0339\5j\66\2\u0338\u033a\5")
        buf.write("T+\2\u0339\u0338\3\2\2\2\u0339\u033a\3\2\2\2\u033a\u033f")
        buf.write("\3\2\2\2\u033b\u033c\7q\2\2\u033c\u033f\5X-\2\u033d\u033f")
        buf.write("\5Z.\2\u033e\u0332\3\2\2\2\u033e\u0336\3\2\2\2\u033e\u033b")
        buf.write("\3\2\2\2\u033e\u033d\3\2\2\2\u033fQ\3\2\2\2\u0340\u0341")
        buf.write("\5(\25\2\u0341S\3\2\2\2\u0342\u0344\5V,\2\u0343\u0342")
        buf.write("\3\2\2\2\u0343\u0344\3\2\2\2\u0344\u0345\3\2\2\2\u0345")
        buf.write("\u0346\5(\25\2\u0346U\3\2\2\2\u0347\u0348\7{\2\2\u0348")
        buf.write("\u0349\7{\2\2\u0349W\3\2\2\2\u034a\u034b\5\32\16\2\u034b")
        buf.write("Y\3\2\2\2\u034c\u034d\5\\/\2\u034d\u034e\5^\60\2\u034e")
        buf.write("[\3\2\2\2\u034f\u0350\t\5\2\2\u0350]\3\2\2\2\u0351\u0352")
        buf.write("\7\u0090\2\2\u0352_\3\2\2\2\u0353\u0355\5\32\16\2\u0354")
        buf.write("\u0353\3\2\2\2\u0355\u0356\3\2\2\2\u0356\u0354\3\2\2\2")
        buf.write("\u0356\u0357\3\2\2\2\u0357\u035b\3\2\2\2\u0358\u035b\7")
        buf.write("\u0085\2\2\u0359\u035b\7\u0086\2\2\u035a\u0354\3\2\2\2")
        buf.write("\u035a\u0358\3\2\2\2\u035a\u0359\3\2\2\2\u035ba\3\2\2")
        buf.write("\2\u035c\u035d\7w\2\2\u035d\u035e\5`\61\2\u035ec\3\2\2")
        buf.write("\2\u035f\u0360\7}\2\2\u0360\u0361\5`\61\2\u0361e\3\2\2")
        buf.write("\2\u0362\u0363\5\32\16\2\u0363g\3\2\2\2\u0364\u0365\t")
        buf.write("\6\2\2\u0365i\3\2\2\2\u0366\u0379\5l\67\2\u0367\u0379")
        buf.write("\5p9\2\u0368\u0379\5n8\2\u0369\u0379\5r:\2\u036a\u0379")
        buf.write("\5t;\2\u036b\u0379\5v<\2\u036c\u0379\5x=\2\u036d\u0379")
        buf.write("\5z>\2\u036e\u0379\5|?\2\u036f\u0379\5\u0084C\2\u0370")
        buf.write("\u0379\5\u0090I\2\u0371\u0379\5\u009aN\2\u0372\u0379\5")
        buf.write("\u00a0Q\2\u0373\u0379\5\u00b4[\2\u0374\u0379\5\u00a4S")
        buf.write("\2\u0375\u0379\5~@\2\u0376\u0379\5\u0080A\2\u0377\u0379")
        buf.write("\5\u0082B\2\u0378\u0366\3\2\2\2\u0378\u0367\3\2\2\2\u0378")
        buf.write("\u0368\3\2\2\2\u0378\u0369\3\2\2\2\u0378\u036a\3\2\2\2")
        buf.write("\u0378\u036b\3\2\2\2\u0378\u036c\3\2\2\2\u0378\u036d\3")
        buf.write("\2\2\2\u0378\u036e\3\2\2\2\u0378\u036f\3\2\2\2\u0378\u0370")
        buf.write("\3\2\2\2\u0378\u0371\3\2\2\2\u0378\u0372\3\2\2\2\u0378")
        buf.write("\u0373\3\2\2\2\u0378\u0374\3\2\2\2\u0378\u0375\3\2\2\2")
        buf.write("\u0378\u0376\3\2\2\2\u0378\u0377\3\2\2\2\u0379k\3\2\2")
        buf.write("\2\u037a\u037b\7T\2\2\u037bm\3\2\2\2\u037c\u037d\7U\2")
        buf.write("\2\u037do\3\2\2\2\u037e\u037f\7V\2\2\u037fq\3\2\2\2\u0380")
        buf.write("\u0381\7W\2\2\u0381s\3\2\2\2\u0382\u0383\7X\2\2\u0383")
        buf.write("u\3\2\2\2\u0384\u0385\7Y\2\2\u0385w\3\2\2\2\u0386\u0387")
        buf.write("\7Z\2\2\u0387y\3\2\2\2\u0388\u0389\7[\2\2\u0389{\3\2\2")
        buf.write("\2\u038a\u038b\7\\\2\2\u038b}\3\2\2\2\u038c\u038d\7^\2")
        buf.write("\2\u038d\177\3\2\2\2\u038e\u038f\7`\2\2\u038f\u0081\3")
        buf.write("\2\2\2\u0390\u0391\7a\2\2\u0391\u0083\3\2\2\2\u0392\u039b")
        buf.write("\7c\2\2\u0393\u0394\7s\2\2\u0394\u0397\5\u0086D\2\u0395")
        buf.write("\u0396\7z\2\2\u0396\u0398\5\u0088E\2\u0397\u0395\3\2\2")
        buf.write("\2\u0397\u0398\3\2\2\2\u0398\u0399\3\2\2\2\u0399\u039a")
        buf.write("\7t\2\2\u039a\u039c\3\2\2\2\u039b\u0393\3\2\2\2\u039b")
        buf.write("\u039c\3\2\2\2\u039c\u0085\3\2\2\2\u039d\u039e\t\7\2\2")
        buf.write("\u039e\u0087\3\2\2\2\u039f\u03a0\7j\2\2\u03a0\u03a1\7")
        buf.write("~\2\2\u03a1\u03a6\5\u008aF\2\u03a2\u03a3\7z\2\2\u03a3")
        buf.write("\u03a5\5\u008aF\2\u03a4\u03a2\3\2\2\2\u03a5\u03a8\3\2")
        buf.write("\2\2\u03a6\u03a4\3\2\2\2\u03a6\u03a7\3\2\2\2\u03a7\u0089")
        buf.write("\3\2\2\2\u03a8\u03a6\3\2\2\2\u03a9\u03ab\5\u008eH\2\u03aa")
        buf.write("\u03a9\3\2\2\2\u03aa\u03ab\3\2\2\2\u03ab\u03ac\3\2\2\2")
        buf.write("\u03ac\u03ad\5\u008cG\2\u03ad\u008b\3\2\2\2\u03ae\u03b2")
        buf.write("\5\32\16\2\u03af\u03b2\7\u0085\2\2\u03b0\u03b2\7\u0086")
        buf.write("\2\2\u03b1\u03ae\3\2\2\2\u03b1\u03af\3\2\2\2\u03b1\u03b0")
        buf.write("\3\2\2\2\u03b2\u008d\3\2\2\2\u03b3\u03b4\5\32\16\2\u03b4")
        buf.write("\u03b5\7q\2\2\u03b5\u008f\3\2\2\2\u03b6\u03bb\7d\2\2\u03b7")
        buf.write("\u03b8\7s\2\2\u03b8\u03b9\5\u0092J\2\u03b9\u03ba\7t\2")
        buf.write("\2\u03ba\u03bc\3\2\2\2\u03bb\u03b7\3\2\2\2\u03bb\u03bc")
        buf.write("\3\2\2\2\u03bc\u0091\3\2\2\2\u03bd\u03be\7j\2\2\u03be")
        buf.write("\u03bf\7~\2\2\u03bf\u03c4\5\u0094K\2\u03c0\u03c1\7z\2")
        buf.write("\2\u03c1\u03c3\5\u0094K\2\u03c2\u03c0\3\2\2\2\u03c3\u03c6")
        buf.write("\3\2\2\2\u03c4\u03c2\3\2\2\2\u03c4\u03c5\3\2\2\2\u03c5")
        buf.write("\u0093\3\2\2\2\u03c6\u03c4\3\2\2\2\u03c7\u03c9\5\u0098")
        buf.write("M\2\u03c8\u03c7\3\2\2\2\u03c8\u03c9\3\2\2\2\u03c9\u03ca")
        buf.write("\3\2\2\2\u03ca\u03cb\5\u0096L\2\u03cb\u0095\3\2\2\2\u03cc")
        buf.write("\u03d0\5\32\16\2\u03cd\u03d0\7\u0085\2\2\u03ce\u03d0\7")
        buf.write("\u0086\2\2\u03cf\u03cc\3\2\2\2\u03cf\u03cd\3\2\2\2\u03cf")
        buf.write("\u03ce\3\2\2\2\u03d0\u0097\3\2\2\2\u03d1\u03d2\7m\2\2")
        buf.write("\u03d2\u03d3\7q\2\2\u03d3\u0099\3\2\2\2\u03d4\u03d5\7")
        buf.write("e\2\2\u03d5\u03d6\7s\2\2\u03d6\u03d7\5\u009cO\2\u03d7")
        buf.write("\u03d8\7t\2\2\u03d8\u009b\3\2\2\2\u03d9\u03de\5\u009e")
        buf.write("P\2\u03da\u03db\7z\2\2\u03db\u03dd\5\u009eP\2\u03dc\u03da")
        buf.write("\3\2\2\2\u03dd\u03e0\3\2\2\2\u03de\u03dc\3\2\2\2\u03de")
        buf.write("\u03df\3\2\2\2\u03df\u009d\3\2\2\2\u03e0\u03de\3\2\2\2")
        buf.write("\u03e1\u03e2\5\32\16\2\u03e2\u009f\3\2\2\2\u03e3\u03e8")
        buf.write("\7f\2\2\u03e4\u03e5\7s\2\2\u03e5\u03e6\5\u00a2R\2\u03e6")
        buf.write("\u03e7\7t\2\2\u03e7\u03e9\3\2\2\2\u03e8\u03e4\3\2\2\2")
        buf.write("\u03e8\u03e9\3\2\2\2\u03e9\u00a1\3\2\2\2\u03ea\u03eb\7")
        buf.write(")\2\2\u03eb\u00a3\3\2\2\2\u03ec\u03f1\5\u00a6T\2\u03ed")
        buf.write("\u03ee\7s\2\2\u03ee\u03ef\5\u00a8U\2\u03ef\u03f0\7t\2")
        buf.write("\2\u03f0\u03f2\3\2\2\2\u03f1\u03ed\3\2\2\2\u03f1\u03f2")
        buf.write("\3\2\2\2\u03f2\u00a5\3\2\2\2\u03f3\u03f4\t\b\2\2\u03f4")
        buf.write("\u00a7\3\2\2\2\u03f5\u03fa\5\u00aaV\2\u03f6\u03f7\7z\2")
        buf.write("\2\u03f7\u03f9\5\u00aaV\2\u03f8\u03f6\3\2\2\2\u03f9\u03fc")
        buf.write("\3\2\2\2\u03fa\u03f8\3\2\2\2\u03fa\u03fb\3\2\2\2\u03fb")
        buf.write("\u00a9\3\2\2\2\u03fc\u03fa\3\2\2\2\u03fd\u03fe\5\u00ae")
        buf.write("X\2\u03fe\u03ff\5\u00acW\2\u03ff\u0400\5\u00b0Y\2\u0400")
        buf.write("\u00ab\3\2\2\2\u0401\u0402\7n\2\2\u0402\u00ad\3\2\2\2")
        buf.write("\u0403\u0404\5\32\16\2\u0404\u0405\7~\2\2\u0405\u00af")
        buf.write("\3\2\2\2\u0406\u0408\5\u00b2Z\2\u0407\u0406\3\2\2\2\u0408")
        buf.write("\u040b\3\2\2\2\u0409\u0407\3\2\2\2\u0409\u040a\3\2\2\2")
        buf.write("\u040a\u00b1\3\2\2\2\u040b\u0409\3\2\2\2\u040c\u040d\7")
        buf.write("\u0084\2\2\u040d\u040e\5\32\16\2\u040e\u00b3\3\2\2\2\u040f")
        buf.write("\u0410\5\u00b6\\\2\u0410\u0413\7s\2\2\u0411\u0414\5\u00b8")
        buf.write("]\2\u0412\u0414\5\u00ba^\2\u0413\u0411\3\2\2\2\u0413\u0412")
        buf.write("\3\2\2\2\u0414\u0416\3\2\2\2\u0415\u0417\5\u00bc_\2\u0416")
        buf.write("\u0415\3\2\2\2\u0416\u0417\3\2\2\2\u0417\u0418\3\2\2\2")
        buf.write("\u0418\u0419\7t\2\2\u0419\u00b5\3\2\2\2\u041a\u041b\t")
        buf.write("\t\2\2\u041b\u00b7\3\2\2\2\u041c\u041d\7|\2\2\u041d\u041e")
        buf.write("\5\32\16\2\u041e\u00b9\3\2\2\2\u041f\u0420\5\34\17\2\u0420")
        buf.write("\u00bb\3\2\2\2\u0421\u0422\7y\2\2\u0422\u0423\7p\2\2\u0423")
        buf.write("\u0424\5\32\16\2\u0424\u00bd\3\2\2\2\u0425\u0435\5\u0114")
        buf.write("\u008b\2\u0426\u0435\5\u0110\u0089\2\u0427\u0435\5\u010c")
        buf.write("\u0087\2\u0428\u0435\5\u010a\u0086\2\u0429\u0435\5\u0108")
        buf.write("\u0085\2\u042a\u0435\5\u0106\u0084\2\u042b\u0435\5\u0104")
        buf.write("\u0083\2\u042c\u0435\5\u0102\u0082\2\u042d\u0435\5\u0100")
        buf.write("\u0081\2\u042e\u0435\5\u00fe\u0080\2\u042f\u0435\5\u00f8")
        buf.write("}\2\u0430\u0435\5\u00c8e\2\u0431\u0435\5\u00c4c\2\u0432")
        buf.write("\u0435\5\u00c0a\2\u0433\u0435\7k\2\2\u0434\u0425\3\2\2")
        buf.write("\2\u0434\u0426\3\2\2\2\u0434\u0427\3\2\2\2\u0434\u0428")
        buf.write("\3\2\2\2\u0434\u0429\3\2\2\2\u0434\u042a\3\2\2\2\u0434")
        buf.write("\u042b\3\2\2\2\u0434\u042c\3\2\2\2\u0434\u042d\3\2\2\2")
        buf.write("\u0434\u042e\3\2\2\2\u0434\u042f\3\2\2\2\u0434\u0430\3")
        buf.write("\2\2\2\u0434\u0431\3\2\2\2\u0434\u0432\3\2\2\2\u0434\u0433")
        buf.write("\3\2\2\2\u0435\u00bf\3\2\2\2\u0436\u0437\7#\2\2\u0437")
        buf.write("\u0438\7s\2\2\u0438\u0439\5\u00c2b\2\u0439\u043a\7t\2")
        buf.write("\2\u043a\u00c1\3\2\2\2\u043b\u043c\5\32\16\2\u043c\u00c3")
        buf.write("\3\2\2\2\u043d\u043e\7\"\2\2\u043e\u043f\7s\2\2\u043f")
        buf.write("\u0440\5\u00c6d\2\u0440\u0441\7t\2\2\u0441\u00c5\3\2\2")
        buf.write("\2\u0442\u0447\5\32\16\2\u0443\u0444\7z\2\2\u0444\u0446")
        buf.write("\5\32\16\2\u0445\u0443\3\2\2\2\u0446\u0449\3\2\2\2\u0447")
        buf.write("\u0445\3\2\2\2\u0447\u0448\3\2\2\2\u0448\u00c7\3\2\2\2")
        buf.write("\u0449\u0447\3\2\2\2\u044a\u044d\7!\2\2\u044b\u044c\7")
        buf.write("{\2\2\u044c\u044e\5\u00ceh\2\u044d\u044b\3\2\2\2\u044d")
        buf.write("\u044e\3\2\2\2\u044e\u0453\3\2\2\2\u044f\u0450\7s\2\2")
        buf.write("\u0450\u0451\5\u00caf\2\u0451\u0452\7t\2\2\u0452\u0454")
        buf.write("\3\2\2\2\u0453\u044f\3\2\2\2\u0453\u0454\3\2\2\2\u0454")
        buf.write("\u00c9\3\2\2\2\u0455\u045b\5\u00ccg\2\u0456\u045a\5\u00f2")
        buf.write("z\2\u0457\u045a\7k\2\2\u0458\u045a\7z\2\2\u0459\u0456")
        buf.write("\3\2\2\2\u0459\u0457\3\2\2\2\u0459\u0458\3\2\2\2\u045a")
        buf.write("\u045d\3\2\2\2\u045b\u0459\3\2\2\2\u045b\u045c\3\2\2\2")
        buf.write("\u045c\u00cb\3\2\2\2\u045d\u045b\3\2\2\2\u045e\u046b\5")
        buf.write("\u00dep\2\u045f\u046b\5\u00d0i\2\u0460\u046b\5\u00e2r")
        buf.write("\2\u0461\u046b\5\u00d2j\2\u0462\u046b\5\u00d4k\2\u0463")
        buf.write("\u046b\5\u00d6l\2\u0464\u046b\5\u00d8m\2\u0465\u046b\5")
        buf.write("\u00dan\2\u0466\u046b\5\u00dco\2\u0467\u046b\5\u00eav")
        buf.write("\2\u0468\u046b\7k\2\2\u0469\u046b\7z\2\2\u046a\u045e\3")
        buf.write("\2\2\2\u046a\u045f\3\2\2\2\u046a\u0460\3\2\2\2\u046a\u0461")
        buf.write("\3\2\2\2\u046a\u0462\3\2\2\2\u046a\u0463\3\2\2\2\u046a")
        buf.write("\u0464\3\2\2\2\u046a\u0465\3\2\2\2\u046a\u0466\3\2\2\2")
        buf.write("\u046a\u0467\3\2\2\2\u046a\u0468\3\2\2\2\u046a\u0469\3")
        buf.write("\2\2\2\u046b\u046e\3\2\2\2\u046c\u046a\3\2\2\2\u046c\u046d")
        buf.write("\3\2\2\2\u046d\u00cd\3\2\2\2\u046e\u046c\3\2\2\2\u046f")
        buf.write("\u0470\5\32\16\2\u0470\u00cf\3\2\2\2\u0471\u0472\7I\2")
        buf.write("\2\u0472\u0473\7q\2\2\u0473\u0477\7)\2\2\u0474\u0476\7")
        buf.write("k\2\2\u0475\u0474\3\2\2\2\u0476\u0479\3\2\2\2\u0477\u0475")
        buf.write("\3\2\2\2\u0477\u0478\3\2\2\2\u0478\u00d1\3\2\2\2\u0479")
        buf.write("\u0477\3\2\2\2\u047a\u047b\7F\2\2\u047b\u047f\5$\23\2")
        buf.write("\u047c\u047e\7k\2\2\u047d\u047c\3\2\2\2\u047e\u0481\3")
        buf.write("\2\2\2\u047f\u047d\3\2\2\2\u047f\u0480\3\2\2\2\u0480\u00d3")
        buf.write("\3\2\2\2\u0481\u047f\3\2\2\2\u0482\u0484\7E\2\2\u0483")
        buf.write("\u0485\7q\2\2\u0484\u0483\3\2\2\2\u0484\u0485\3\2\2\2")
        buf.write("\u0485\u0486\3\2\2\2\u0486\u048a\5$\23\2\u0487\u0489\7")
        buf.write("k\2\2\u0488\u0487\3\2\2\2\u0489\u048c\3\2\2\2\u048a\u0488")
        buf.write("\3\2\2\2\u048a\u048b\3\2\2\2\u048b\u00d5\3\2\2\2\u048c")
        buf.write("\u048a\3\2\2\2\u048d\u048f\7,\2\2\u048e\u0490\7q\2\2\u048f")
        buf.write("\u048e\3\2\2\2\u048f\u0490\3\2\2\2\u0490\u0491\3\2\2\2")
        buf.write("\u0491\u0495\5$\23\2\u0492\u0494\7k\2\2\u0493\u0492\3")
        buf.write("\2\2\2\u0494\u0497\3\2\2\2\u0495\u0493\3\2\2\2\u0495\u0496")
        buf.write("\3\2\2\2\u0496\u00d7\3\2\2\2\u0497\u0495\3\2\2\2\u0498")
        buf.write("\u049a\7+\2\2\u0499\u049b\7q\2\2\u049a\u0499\3\2\2\2\u049a")
        buf.write("\u049b\3\2\2\2\u049b\u049c\3\2\2\2\u049c\u04a0\5$\23\2")
        buf.write("\u049d\u049f\7k\2\2\u049e\u049d\3\2\2\2\u049f\u04a2\3")
        buf.write("\2\2\2\u04a0\u049e\3\2\2\2\u04a0\u04a1\3\2\2\2\u04a1\u00d9")
        buf.write("\3\2\2\2\u04a2\u04a0\3\2\2\2\u04a3\u04a4\7M\2\2\u04a4")
        buf.write("\u04a5\7q\2\2\u04a5\u04a9\5\36\20\2\u04a6\u04a8\7k\2\2")
        buf.write("\u04a7\u04a6\3\2\2\2\u04a8\u04ab\3\2\2\2\u04a9\u04a7\3")
        buf.write("\2\2\2\u04a9\u04aa\3\2\2\2\u04aa\u00db\3\2\2\2\u04ab\u04a9")
        buf.write("\3\2\2\2\u04ac\u04ad\7C\2\2\u04ad\u04ae\7q\2\2\u04ae\u04b2")
        buf.write("\5\32\16\2\u04af\u04b1\7k\2\2\u04b0\u04af\3\2\2\2\u04b1")
        buf.write("\u04b4\3\2\2\2\u04b2\u04b0\3\2\2\2\u04b2\u04b3\3\2\2\2")
        buf.write("\u04b3\u00dd\3\2\2\2\u04b4\u04b2\3\2\2\2\u04b5\u04b6\7")
        buf.write("Q\2\2\u04b6\u04b7\7q\2\2\u04b7\u04b9\5\36\20\2\u04b8\u04ba")
        buf.write("\5\u00e0q\2\u04b9\u04b8\3\2\2\2\u04b9\u04ba\3\2\2\2\u04ba")
        buf.write("\u04be\3\2\2\2\u04bb\u04bd\7k\2\2\u04bc\u04bb\3\2\2\2")
        buf.write("\u04bd\u04c0\3\2\2\2\u04be\u04bc\3\2\2\2\u04be\u04bf\3")
        buf.write("\2\2\2\u04bf\u00df\3\2\2\2\u04c0\u04be\3\2\2\2\u04c1\u04c2")
        buf.write("\5\"\22\2\u04c2\u00e1\3\2\2\2\u04c3\u04c4\7G\2\2\u04c4")
        buf.write("\u04c5\7s\2\2\u04c5\u04ca\5\u00e4s\2\u04c6\u04c7\7z\2")
        buf.write("\2\u04c7\u04c9\5\u00e4s\2\u04c8\u04c6\3\2\2\2\u04c9\u04cc")
        buf.write("\3\2\2\2\u04ca\u04c8\3\2\2\2\u04ca\u04cb\3\2\2\2\u04cb")
        buf.write("\u04cd\3\2\2\2\u04cc\u04ca\3\2\2\2\u04cd\u04ce\7t\2\2")
        buf.write("\u04ce\u00e3\3\2\2\2\u04cf\u04d3\7@\2\2\u04d0\u04d1\7")
        buf.write("q\2\2\u04d1\u04d4\5\u00e6t\2\u04d2\u04d4\5\u00e8u\2\u04d3")
        buf.write("\u04d0\3\2\2\2\u04d3\u04d2\3\2\2\2\u04d3\u04d4\3\2\2\2")
        buf.write("\u04d4\u00e5\3\2\2\2\u04d5\u04d6\7|\2\2\u04d6\u04d7\5")
        buf.write("\32\16\2\u04d7\u00e7\3\2\2\2\u04d8\u04d9\5\34\17\2\u04d9")
        buf.write("\u00e9\3\2\2\2\u04da\u04db\7D\2\2\u04db\u04dc\7q\2\2\u04dc")
        buf.write("\u04e0\5\u00ecw\2\u04dd\u04df\7k\2\2\u04de\u04dd\3\2\2")
        buf.write("\2\u04df\u04e2\3\2\2\2\u04e0\u04de\3\2\2\2\u04e0\u04e1")
        buf.write("\3\2\2\2\u04e1\u00eb\3\2\2\2\u04e2\u04e0\3\2\2\2\u04e3")
        buf.write("\u04e4\7H\2\2\u04e4\u04e7\5\u00eex\2\u04e5\u04e6\7S\2")
        buf.write("\2\u04e6\u04e8\5\u00f0y\2\u04e7\u04e5\3\2\2\2\u04e7\u04e8")
        buf.write("\3\2\2\2\u04e8\u00ed\3\2\2\2\u04e9\u04ea\5\32\16\2\u04ea")
        buf.write("\u00ef\3\2\2\2\u04eb\u04ec\5\32\16\2\u04ec\u00f1\3\2\2")
        buf.write("\2\u04ed\u04ee\7A\2\2\u04ee\u04f2\7q\2\2\u04ef\u04f3\5")
        buf.write("\u00f4{\2\u04f0\u04f3\7z\2\2\u04f1\u04f3\7k\2\2\u04f2")
        buf.write("\u04ef\3\2\2\2\u04f2\u04f0\3\2\2\2\u04f2\u04f1\3\2\2\2")
        buf.write("\u04f3\u04f4\3\2\2\2\u04f4\u04f2\3\2\2\2\u04f4\u04f5\3")
        buf.write("\2\2\2\u04f5\u00f3\3\2\2\2\u04f6\u04f7\5\u00f6|\2\u04f7")
        buf.write("\u04f8\7s\2\2\u04f8\u04f9\5\u00caf\2\u04f9\u04fa\7t\2")
        buf.write("\2\u04fa\u00f5\3\2\2\2\u04fb\u04fc\5\32\16\2\u04fc\u00f7")
        buf.write("\3\2\2\2\u04fd\u050c\7 \2\2\u04fe\u0508\7s\2\2\u04ff\u0509")
        buf.write("\5\u00fa~\2\u0500\u0505\5\u00fc\177\2\u0501\u0502\7z\2")
        buf.write("\2\u0502\u0504\5\u00fc\177\2\u0503\u0501\3\2\2\2\u0504")
        buf.write("\u0507\3\2\2\2\u0505\u0503\3\2\2\2\u0505\u0506\3\2\2\2")
        buf.write("\u0506\u0509\3\2\2\2\u0507\u0505\3\2\2\2\u0508\u04ff\3")
        buf.write("\2\2\2\u0508\u0500\3\2\2\2\u0509\u050a\3\2\2\2\u050a\u050b")
        buf.write("\7t\2\2\u050b\u050d\3\2\2\2\u050c\u04fe\3\2\2\2\u050c")
        buf.write("\u050d\3\2\2\2\u050d\u00f9\3\2\2\2\u050e\u050f\7\u0082")
        buf.write("\2\2\u050f\u00fb\3\2\2\2\u0510\u0511\5\32\16\2\u0511\u00fd")
        buf.write("\3\2\2\2\u0512\u0513\7\37\2\2\u0513\u0514\5$\23\2\u0514")
        buf.write("\u00ff\3\2\2\2\u0515\u0516\7\36\2\2\u0516\u0517\5$\23")
        buf.write("\2\u0517\u0101\3\2\2\2\u0518\u0519\7\35\2\2\u0519\u051a")
        buf.write("\5$\23\2\u051a\u0103\3\2\2\2\u051b\u051c\7\34\2\2\u051c")
        buf.write("\u051d\5$\23\2\u051d\u0105\3\2\2\2\u051e\u051f\7\33\2")
        buf.write("\2\u051f\u0520\5$\23\2\u0520\u0107\3\2\2\2\u0521\u0522")
        buf.write("\7\32\2\2\u0522\u0523\5$\23\2\u0523\u0109\3\2\2\2\u0524")
        buf.write("\u0525\7\31\2\2\u0525\u0526\7s\2\2\u0526\u0527\5\34\17")
        buf.write("\2\u0527\u0528\7t\2\2\u0528\u010b\3\2\2\2\u0529\u052a")
        buf.write("\7\30\2\2\u052a\u052b\7s\2\2\u052b\u052c\5\u010e\u0088")
        buf.write("\2\u052c\u052d\7t\2\2\u052d\u010d\3\2\2\2\u052e\u052f")
        buf.write("\5\32\16\2\u052f\u010f\3\2\2\2\u0530\u0535\7\27\2\2\u0531")
        buf.write("\u0532\7s\2\2\u0532\u0533\5\u0112\u008a\2\u0533\u0534")
        buf.write("\7t\2\2\u0534\u0536\3\2\2\2\u0535\u0531\3\2\2\2\u0535")
        buf.write("\u0536\3\2\2\2\u0536\u0111\3\2\2\2\u0537\u0538\7<\2\2")
        buf.write("\u0538\u0113\3\2\2\2\u0539\u0553\7&\2\2\u053a\u0549\7")
        buf.write("s\2\2\u053b\u0548\5\u0132\u009a\2\u053c\u0548\5\u0134")
        buf.write("\u009b\2\u053d\u0548\5\u0136\u009c\2\u053e\u0548\5\u0138")
        buf.write("\u009d\2\u053f\u0548\5\u013a\u009e\2\u0540\u0548\5\u013c")
        buf.write("\u009f\2\u0541\u0548\5\u012a\u0096\2\u0542\u0548\5\u011e")
        buf.write("\u0090\2\u0543\u0548\5\u0118\u008d\2\u0544\u0548\5\u0116")
        buf.write("\u008c\2\u0545\u0548\7k\2\2\u0546\u0548\7z\2\2\u0547\u053b")
        buf.write("\3\2\2\2\u0547\u053c\3\2\2\2\u0547\u053d\3\2\2\2\u0547")
        buf.write("\u053e\3\2\2\2\u0547\u053f\3\2\2\2\u0547\u0540\3\2\2\2")
        buf.write("\u0547\u0541\3\2\2\2\u0547\u0542\3\2\2\2\u0547\u0543\3")
        buf.write("\2\2\2\u0547\u0544\3\2\2\2\u0547\u0545\3\2\2\2\u0547\u0546")
        buf.write("\3\2\2\2\u0548\u054b\3\2\2\2\u0549\u0547\3\2\2\2\u0549")
        buf.write("\u054a\3\2\2\2\u054a\u054f\3\2\2\2\u054b\u0549\3\2\2\2")
        buf.write("\u054c\u054e\7k\2\2\u054d\u054c\3\2\2\2\u054e\u0551\3")
        buf.write("\2\2\2\u054f\u054d\3\2\2\2\u054f\u0550\3\2\2\2\u0550\u0552")
        buf.write("\3\2\2\2\u0551\u054f\3\2\2\2\u0552\u0554\7t\2\2\u0553")
        buf.write("\u053a\3\2\2\2\u0553\u0554\3\2\2\2\u0554\u0558\3\2\2\2")
        buf.write("\u0555\u0557\7k\2\2\u0556\u0555\3\2\2\2\u0557\u055a\3")
        buf.write("\2\2\2\u0558\u0556\3\2\2\2\u0558\u0559\3\2\2\2\u0559\u0115")
        buf.write("\3\2\2\2\u055a\u0558\3\2\2\2\u055b\u055c\7>\2\2\u055c")
        buf.write("\u0560\7q\2\2\u055d\u055f\7k\2\2\u055e\u055d\3\2\2\2\u055f")
        buf.write("\u0562\3\2\2\2\u0560\u055e\3\2\2\2\u0560\u0561\3\2\2\2")
        buf.write("\u0561\u0563\3\2\2\2\u0562\u0560\3\2\2\2\u0563\u056e\5")
        buf.write("\u011c\u008f\2\u0564\u0568\7z\2\2\u0565\u0567\7k\2\2\u0566")
        buf.write("\u0565\3\2\2\2\u0567\u056a\3\2\2\2\u0568\u0566\3\2\2\2")
        buf.write("\u0568\u0569\3\2\2\2\u0569\u056b\3\2\2\2\u056a\u0568\3")
        buf.write("\2\2\2\u056b\u056d\5\u011c\u008f\2\u056c\u0564\3\2\2\2")
        buf.write("\u056d\u0570\3\2\2\2\u056e\u056c\3\2\2\2\u056e\u056f\3")
        buf.write("\2\2\2\u056f\u0117\3\2\2\2\u0570\u056e\3\2\2\2\u0571\u0572")
        buf.write("\7=\2\2\u0572\u0573\7q\2\2\u0573\u0578\5\u011a\u008e\2")
        buf.write("\u0574\u0575\7z\2\2\u0575\u0577\5\u011a\u008e\2\u0576")
        buf.write("\u0574\3\2\2\2\u0577\u057a\3\2\2\2\u0578\u0576\3\2\2\2")
        buf.write("\u0578\u0579\3\2\2\2\u0579\u0119\3\2\2\2\u057a\u0578\3")
        buf.write("\2\2\2\u057b\u057c\t\4\2\2\u057c\u011b\3\2\2\2\u057d\u057e")
        buf.write("\t\4\2\2\u057e\u011d\3\2\2\2\u057f\u0580\7A\2\2\u0580")
        buf.write("\u0581\7q\2\2\u0581\u0586\5\u0120\u0091\2\u0582\u0583")
        buf.write("\7z\2\2\u0583\u0585\5\u0120\u0091\2\u0584\u0582\3\2\2")
        buf.write("\2\u0585\u0588\3\2\2\2\u0586\u0584\3\2\2\2\u0586\u0587")
        buf.write("\3\2\2\2\u0587\u011f\3\2\2\2\u0588\u0586\3\2\2\2\u0589")
        buf.write("\u0596\5\u0122\u0092\2\u058a\u0592\7s\2\2\u058b\u0591")
        buf.write("\5\u0124\u0093\2\u058c\u0591\5\u0126\u0094\2\u058d\u0591")
        buf.write("\5\u0128\u0095\2\u058e\u0591\7k\2\2\u058f\u0591\7z\2\2")
        buf.write("\u0590\u058b\3\2\2\2\u0590\u058c\3\2\2\2\u0590\u058d\3")
        buf.write("\2\2\2\u0590\u058e\3\2\2\2\u0590\u058f\3\2\2\2\u0591\u0594")
        buf.write("\3\2\2\2\u0592\u0590\3\2\2\2\u0592\u0593\3\2\2\2\u0593")
        buf.write("\u0595\3\2\2\2\u0594\u0592\3\2\2\2\u0595\u0597\7t\2\2")
        buf.write("\u0596\u058a\3\2\2\2\u0596\u0597\3\2\2\2\u0597\u0121\3")
        buf.write("\2\2\2\u0598\u0599\5\32\16\2\u0599\u0123\3\2\2\2\u059a")
        buf.write("\u059b\7B\2\2\u059b\u059c\7q\2\2\u059c\u059d\7?\2\2\u059d")
        buf.write("\u0125\3\2\2\2\u059e\u059f\7J\2\2\u059f\u05a0\7q\2\2\u05a0")
        buf.write("\u05a1\7m\2\2\u05a1\u0127\3\2\2\2\u05a2\u05a3\7Q\2\2\u05a3")
        buf.write("\u05a4\7q\2\2\u05a4\u05a5\5\36\20\2\u05a5\u0129\3\2\2")
        buf.write("\2\u05a6\u05a7\7K\2\2\u05a7\u05a8\7q\2\2\u05a8\u05ad\5")
        buf.write("\u012c\u0097\2\u05a9\u05aa\7z\2\2\u05aa\u05ac\5\u012c")
        buf.write("\u0097\2\u05ab\u05a9\3\2\2\2\u05ac\u05af\3\2\2\2\u05ad")
        buf.write("\u05ab\3\2\2\2\u05ad\u05ae\3\2\2\2\u05ae\u012b\3\2\2\2")
        buf.write("\u05af\u05ad\3\2\2\2\u05b0\u05b2\5\u012e\u0098\2\u05b1")
        buf.write("\u05b3\5\u0130\u0099\2\u05b2\u05b1\3\2\2\2\u05b2\u05b3")
        buf.write("\3\2\2\2\u05b3\u05b4\3\2\2\2\u05b4\u05b5\7s\2\2\u05b5")
        buf.write("\u05b6\5\36\20\2\u05b6\u05b7\7t\2\2\u05b7\u012d\3\2\2")
        buf.write("\2\u05b8\u05b9\5\32\16\2\u05b9\u012f\3\2\2\2\u05ba\u05bb")
        buf.write("\t\4\2\2\u05bb\u0131\3\2\2\2\u05bc\u05bd\7L\2\2\u05bd")
        buf.write("\u05be\7q\2\2\u05be\u05c2\5\36\20\2\u05bf\u05c1\7k\2\2")
        buf.write("\u05c0\u05bf\3\2\2\2\u05c1\u05c4\3\2\2\2\u05c2\u05c0\3")
        buf.write("\2\2\2\u05c2\u05c3\3\2\2\2\u05c3\u0133\3\2\2\2\u05c4\u05c2")
        buf.write("\3\2\2\2\u05c5\u05c6\7M\2\2\u05c6\u05c7\7q\2\2\u05c7\u05cb")
        buf.write("\5\36\20\2\u05c8\u05ca\7k\2\2\u05c9\u05c8\3\2\2\2\u05ca")
        buf.write("\u05cd\3\2\2\2\u05cb\u05c9\3\2\2\2\u05cb\u05cc\3\2\2\2")
        buf.write("\u05cc\u0135\3\2\2\2\u05cd\u05cb\3\2\2\2\u05ce\u05cf\7")
        buf.write("N\2\2\u05cf\u05d0\7q\2\2\u05d0\u05d4\5\36\20\2\u05d1\u05d3")
        buf.write("\7k\2\2\u05d2\u05d1\3\2\2\2\u05d3\u05d6\3\2\2\2\u05d4")
        buf.write("\u05d2\3\2\2\2\u05d4\u05d5\3\2\2\2\u05d5\u0137\3\2\2\2")
        buf.write("\u05d6\u05d4\3\2\2\2\u05d7\u05d8\7O\2\2\u05d8\u05d9\7")
        buf.write("q\2\2\u05d9\u05dd\5\36\20\2\u05da\u05dc\7k\2\2\u05db\u05da")
        buf.write("\3\2\2\2\u05dc\u05df\3\2\2\2\u05dd\u05db\3\2\2\2\u05dd")
        buf.write("\u05de\3\2\2\2\u05de\u0139\3\2\2\2\u05df\u05dd\3\2\2\2")
        buf.write("\u05e0\u05e1\7P\2\2\u05e1\u05e2\7q\2\2\u05e2\u05e6\5\36")
        buf.write("\20\2\u05e3\u05e5\7k\2\2\u05e4\u05e3\3\2\2\2\u05e5\u05e8")
        buf.write("\3\2\2\2\u05e6\u05e4\3\2\2\2\u05e6\u05e7\3\2\2\2\u05e7")
        buf.write("\u013b\3\2\2\2\u05e8\u05e6\3\2\2\2\u05e9\u05ea\7Q\2\2")
        buf.write("\u05ea\u05eb\7q\2\2\u05eb\u05ef\5\36\20\2\u05ec\u05ee")
        buf.write("\7k\2\2\u05ed\u05ec\3\2\2\2\u05ee\u05f1\3\2\2\2\u05ef")
        buf.write("\u05ed\3\2\2\2\u05ef\u05f0\3\2\2\2\u05f0\u013d\3\2\2\2")
        buf.write("\u05f1\u05ef\3\2\2\2\u05f2\u05f6\5\u0140\u00a1\2\u05f3")
        buf.write("\u05f5\7k\2\2\u05f4\u05f3\3\2\2\2\u05f5\u05f8\3\2\2\2")
        buf.write("\u05f6\u05f4\3\2\2\2\u05f6\u05f7\3\2\2\2\u05f7\u05f9\3")
        buf.write("\2\2\2\u05f8\u05f6\3\2\2\2\u05f9\u05fd\5\u015a\u00ae\2")
        buf.write("\u05fa\u05fc\7k\2\2\u05fb\u05fa\3\2\2\2\u05fc\u05ff\3")
        buf.write("\2\2\2\u05fd\u05fb\3\2\2\2\u05fd\u05fe\3\2\2\2\u05fe\u013f")
        buf.write("\3\2\2\2\u05ff\u05fd\3\2\2\2\u0600\u0602\7u\2\2\u0601")
        buf.write("\u0603\5\u0142\u00a2\2\u0602\u0601\3\2\2\2\u0602\u0603")
        buf.write("\3\2\2\2\u0603\u0604\3\2\2\2\u0604\u0606\5\u0158\u00ad")
        buf.write("\2\u0605\u0607\5\u0144\u00a3\2\u0606\u0605\3\2\2\2\u0606")
        buf.write("\u0607\3\2\2\2\u0607\u0610\3\2\2\2\u0608\u060a\7q\2\2")
        buf.write("\u0609\u060b\5\u014e\u00a8\2\u060a\u0609\3\2\2\2\u060a")
        buf.write("\u060b\3\2\2\2\u060b\u060e\3\2\2\2\u060c\u060d\7q\2\2")
        buf.write("\u060d\u060f\5\u0148\u00a5\2\u060e\u060c\3\2\2\2\u060e")
        buf.write("\u060f\3\2\2\2\u060f\u0611\3\2\2\2\u0610\u0608\3\2\2\2")
        buf.write("\u0610\u0611\3\2\2\2\u0611\u0612\3\2\2\2\u0612\u0614\7")
        buf.write("v\2\2\u0613\u0615\7k\2\2\u0614\u0613\3\2\2\2\u0614\u0615")
        buf.write("\3\2\2\2\u0615\u0141\3\2\2\2\u0616\u0617\5\32\16\2\u0617")
        buf.write("\u0618\t\n\2\2\u0618\u0619\7p\2\2\u0619\u0143\3\2\2\2")
        buf.write("\u061a\u061b\7S\2\2\u061b\u061c\5\u0146\u00a4\2\u061c")
        buf.write("\u0145\3\2\2\2\u061d\u061e\5\32\16\2\u061e\u0147\3\2\2")
        buf.write("\2\u061f\u0622\5\u014a\u00a6\2\u0620\u0622\5$\23\2\u0621")
        buf.write("\u061f\3\2\2\2\u0621\u0620\3\2\2\2\u0622\u0149\3\2\2\2")
        buf.write("\u0623\u0628\5\u014c\u00a7\2\u0624\u0625\7}\2\2\u0625")
        buf.write("\u0627\5\u014c\u00a7\2\u0626\u0624\3\2\2\2\u0627\u062a")
        buf.write("\3\2\2\2\u0628\u0626\3\2\2\2\u0628\u0629\3\2\2\2\u0629")
        buf.write("\u014b\3\2\2\2\u062a\u0628\3\2\2\2\u062b\u0631\5\32\16")
        buf.write("\2\u062c\u0631\7m\2\2\u062d\u0631\7y\2\2\u062e\u0631\7")
        buf.write("x\2\2\u062f\u0631\7{\2\2\u0630\u062b\3\2\2\2\u0630\u062c")
        buf.write("\3\2\2\2\u0630\u062d\3\2\2\2\u0630\u062e\3\2\2\2\u0630")
        buf.write("\u062f\3\2\2\2\u0631\u0632\3\2\2\2\u0632\u0630\3\2\2\2")
        buf.write("\u0632\u0633\3\2\2\2\u0633\u014d\3\2\2\2\u0634\u0636\t")
        buf.write("\13\2\2\u0635\u0634\3\2\2\2\u0635\u0636\3\2\2\2\u0636")
        buf.write("\u0637\3\2\2\2\u0637\u0638\5\u0156\u00ac\2\u0638\u014f")
        buf.write("\3\2\2\2\u0639\u063d\5\32\16\2\u063a\u063d\7y\2\2\u063b")
        buf.write("\u063d\7m\2\2\u063c\u0639\3\2\2\2\u063c\u063a\3\2\2\2")
        buf.write("\u063c\u063b\3\2\2\2\u063d\u063e\3\2\2\2\u063e\u063c\3")
        buf.write("\2\2\2\u063e\u063f\3\2\2\2\u063f\u0151\3\2\2\2\u0640\u0641")
        buf.write("\7o\2\2\u0641\u0642\5\32\16\2\u0642\u0643\7p\2\2\u0643")
        buf.write("\u0153\3\2\2\2\u0644\u0647\5\u0150\u00a9\2\u0645\u0647")
        buf.write("\5\u0152\u00aa\2\u0646\u0644\3\2\2\2\u0646\u0645\3\2\2")
        buf.write("\2\u0647\u0155\3\2\2\2\u0648\u0653\7}\2\2\u0649\u064a")
        buf.write("\7}\2\2\u064a\u064c\5\u0154\u00ab\2\u064b\u0649\3\2\2")
        buf.write("\2\u064c\u064d\3\2\2\2\u064d\u064b\3\2\2\2\u064d\u064e")
        buf.write("\3\2\2\2\u064e\u0650\3\2\2\2\u064f\u0651\7}\2\2\u0650")
        buf.write("\u064f\3\2\2\2\u0650\u0651\3\2\2\2\u0651\u0653\3\2\2\2")
        buf.write("\u0652\u0648\3\2\2\2\u0652\u064b\3\2\2\2\u0653\u0157\3")
        buf.write("\2\2\2\u0654\u0655\5\32\16\2\u0655\u0159\3\2\2\2\u0656")
        buf.write("\u0658\5\u015e\u00b0\2\u0657\u0656\3\2\2\2\u0658\u065b")
        buf.write("\3\2\2\2\u0659\u0657\3\2\2\2\u0659\u065a\3\2\2\2\u065a")
        buf.write("\u065f\3\2\2\2\u065b\u0659\3\2\2\2\u065c\u065e\5\u0164")
        buf.write("\u00b3\2\u065d\u065c\3\2\2\2\u065e\u0661\3\2\2\2\u065f")
        buf.write("\u065d\3\2\2\2\u065f\u0660\3\2\2\2\u0660\u0663\3\2\2\2")
        buf.write("\u0661\u065f\3\2\2\2\u0662\u0664\5\u015c\u00af\2\u0663")
        buf.write("\u0662\3\2\2\2\u0663\u0664\3\2\2\2\u0664\u0668\3\2\2\2")
        buf.write("\u0665\u0667\7k\2\2\u0666\u0665\3\2\2\2\u0667\u066a\3")
        buf.write("\2\2\2\u0668\u0666\3\2\2\2\u0668\u0669\3\2\2\2\u0669\u066e")
        buf.write("\3\2\2\2\u066a\u0668\3\2\2\2\u066b\u066d\5\u016a\u00b6")
        buf.write("\2\u066c\u066b\3\2\2\2\u066d\u0670\3\2\2\2\u066e\u066c")
        buf.write("\3\2\2\2\u066e\u066f\3\2\2\2\u066f\u015b\3\2\2\2\u0670")
        buf.write("\u066e\3\2\2\2\u0671\u0672\5$\23\2\u0672\u015d\3\2\2\2")
        buf.write("\u0673\u0674\5\u0160\u00b1\2\u0674\u0675\7\u008c\2\2\u0675")
        buf.write("\u067c\5\u0162\u00b2\2\u0676\u0678\7k\2\2\u0677\u0676")
        buf.write("\3\2\2\2\u0678\u0679\3\2\2\2\u0679\u0677\3\2\2\2\u0679")
        buf.write("\u067a\3\2\2\2\u067a\u067d\3\2\2\2\u067b\u067d\7\2\2\3")
        buf.write("\u067c\u0677\3\2\2\2\u067c\u067b\3\2\2\2\u067d\u015f\3")
        buf.write("\2\2\2\u067e\u067f\5\32\16\2\u067f\u0161\3\2\2\2\u0680")
        buf.write("\u0681\7\u0090\2\2\u0681\u0163\3\2\2\2\u0682\u0683\5\u0166")
        buf.write("\u00b4\2\u0683\u0685\7s\2\2\u0684\u0686\5\u0168\u00b5")
        buf.write("\2\u0685\u0684\3\2\2\2\u0685\u0686\3\2\2\2\u0686\u0687")
        buf.write("\3\2\2\2\u0687\u0689\7t\2\2\u0688\u068a\5(\25\2\u0689")
        buf.write("\u0688\3\2\2\2\u0689\u068a\3\2\2\2\u068a\u0691\3\2\2\2")
        buf.write("\u068b\u068d\7k\2\2\u068c\u068b\3\2\2\2\u068d\u068e\3")
        buf.write("\2\2\2\u068e\u068c\3\2\2\2\u068e\u068f\3\2\2\2\u068f\u0692")
        buf.write("\3\2\2\2\u0690\u0692\7\2\2\3\u0691\u068c\3\2\2\2\u0691")
        buf.write("\u0690\3\2\2\2\u0692\u0165\3\2\2\2\u0693\u0694\5\32\16")
        buf.write("\2\u0694\u0167\3\2\2\2\u0695\u069a\5\32\16\2\u0696\u0697")
        buf.write("\7z\2\2\u0697\u0699\5\32\16\2\u0698\u0696\3\2\2\2\u0699")
        buf.write("\u069c\3\2\2\2\u069a\u0698\3\2\2\2\u069a\u069b\3\2\2\2")
        buf.write("\u069b\u0169\3\2\2\2\u069c\u069a\3\2\2\2\u069d\u06ae\5")
        buf.write("\u01f0\u00f9\2\u069e\u06ae\5\u016c\u00b7\2\u069f\u06ae")
        buf.write("\5\u01ee\u00f8\2\u06a0\u06ae\5\u01e2\u00f2\2\u06a1\u06ae")
        buf.write("\5\u01e0\u00f1\2\u06a2\u06ae\5\u01c6\u00e4\2\u06a3\u06ae")
        buf.write("\5\u0180\u00c1\2\u06a4\u06ae\5\u01c4\u00e3\2\u06a5\u06ae")
        buf.write("\5\u01c2\u00e2\2\u06a6\u06ae\5\u01c0\u00e1\2\u06a7\u06ae")
        buf.write("\5\u017e\u00c0\2\u06a8\u06ae\5\u017c\u00bf\2\u06a9\u06ae")
        buf.write("\5\u0178\u00bd\2\u06aa\u06ae\5\u0176\u00bc\2\u06ab\u06ae")
        buf.write("\5\u0172\u00ba\2\u06ac\u06ae\7k\2\2\u06ad\u069d\3\2\2")
        buf.write("\2\u06ad\u069e\3\2\2\2\u06ad\u069f\3\2\2\2\u06ad\u06a0")
        buf.write("\3\2\2\2\u06ad\u06a1\3\2\2\2\u06ad\u06a2\3\2\2\2\u06ad")
        buf.write("\u06a3\3\2\2\2\u06ad\u06a4\3\2\2\2\u06ad\u06a5\3\2\2\2")
        buf.write("\u06ad\u06a6\3\2\2\2\u06ad\u06a7\3\2\2\2\u06ad\u06a8\3")
        buf.write("\2\2\2\u06ad\u06a9\3\2\2\2\u06ad\u06aa\3\2\2\2\u06ad\u06ab")
        buf.write("\3\2\2\2\u06ad\u06ac\3\2\2\2\u06ae\u016b\3\2\2\2\u06af")
        buf.write("\u06b2\5\u016e\u00b8\2\u06b0\u06b1\7{\2\2\u06b1\u06b3")
        buf.write("\5\u0170\u00b9\2\u06b2\u06b0\3\2\2\2\u06b2\u06b3\3\2\2")
        buf.write("\2\u06b3\u06b4\3\2\2\2\u06b4\u06b5\5(\25\2\u06b5\u016d")
        buf.write("\3\2\2\2\u06b6\u06b7\t\f\2\2\u06b7\u016f\3\2\2\2\u06b8")
        buf.write("\u06b9\5\32\16\2\u06b9\u0171\3\2\2\2\u06ba\u06bd\7\22")
        buf.write("\2\2\u06bb\u06bc\7{\2\2\u06bc\u06be\5\u0174\u00bb\2\u06bd")
        buf.write("\u06bb\3\2\2\2\u06bd\u06be\3\2\2\2\u06be\u06bf\3\2\2\2")
        buf.write("\u06bf\u06c0\5(\25\2\u06c0\u0173\3\2\2\2\u06c1\u06c2\5")
        buf.write("\32\16\2\u06c2\u0175\3\2\2\2\u06c3\u06c5\7\21\2\2\u06c4")
        buf.write("\u06c6\5(\25\2\u06c5\u06c4\3\2\2\2\u06c5\u06c6\3\2\2\2")
        buf.write("\u06c6\u0177\3\2\2\2\u06c7\u06c8\7\20\2\2\u06c8\u06c9")
        buf.write("\7s\2\2\u06c9\u06ca\5\u017a\u00be\2\u06ca\u06cb\7t\2\2")
        buf.write("\u06cb\u0179\3\2\2\2\u06cc\u06cd\7m\2\2\u06cd\u017b\3")
        buf.write("\2\2\2\u06ce\u06d0\7\17\2\2\u06cf\u06d1\5(\25\2\u06d0")
        buf.write("\u06cf\3\2\2\2\u06d0\u06d1\3\2\2\2\u06d1\u017d\3\2\2\2")
        buf.write("\u06d2\u06d3\7\r\2\2\u06d3\u06d4\5\u0182\u00c2\2\u06d4")
        buf.write("\u017f\3\2\2\2\u06d5\u06d6\7\t\2\2\u06d6\u06d7\5\u0182")
        buf.write("\u00c2\2\u06d7\u0181\3\2\2\2\u06d8\u06d9\7{\2\2\u06d9")
        buf.write("\u06db\5\u0186\u00c4\2\u06da\u06d8\3\2\2\2\u06da\u06db")
        buf.write("\3\2\2\2\u06db\u06dc\3\2\2\2\u06dc\u06e0\7s\2\2\u06dd")
        buf.write("\u06df\7k\2\2\u06de\u06dd\3\2\2\2\u06df\u06e2\3\2\2\2")
        buf.write("\u06e0\u06de\3\2\2\2\u06e0\u06e1\3\2\2\2\u06e1\u06e3\3")
        buf.write("\2\2\2\u06e2\u06e0\3\2\2\2\u06e3\u06e5\5\u0190\u00c9\2")
        buf.write("\u06e4\u06e6\5\u0192\u00ca\2\u06e5\u06e4\3\2\2\2\u06e5")
        buf.write("\u06e6\3\2\2\2\u06e6\u06f6\3\2\2\2\u06e7\u06f5\5\u0194")
        buf.write("\u00cb\2\u06e8\u06f5\5\u01a8\u00d5\2\u06e9\u06f5\5\u01ae")
        buf.write("\u00d8\2\u06ea\u06f5\5\u01b8\u00dd\2\u06eb\u06f5\5\u01a6")
        buf.write("\u00d4\2\u06ec\u06f5\5\u019e\u00d0\2\u06ed\u06f5\5\u01a4")
        buf.write("\u00d3\2\u06ee\u06f5\5\u01a0\u00d1\2\u06ef\u06f5\5\u01a2")
        buf.write("\u00d2\2\u06f0\u06f5\5\u0196\u00cc\2\u06f1\u06f5\5\u019a")
        buf.write("\u00ce\2\u06f2\u06f5\7k\2\2\u06f3\u06f5\7z\2\2\u06f4\u06e7")
        buf.write("\3\2\2\2\u06f4\u06e8\3\2\2\2\u06f4\u06e9\3\2\2\2\u06f4")
        buf.write("\u06ea\3\2\2\2\u06f4\u06eb\3\2\2\2\u06f4\u06ec\3\2\2\2")
        buf.write("\u06f4\u06ed\3\2\2\2\u06f4\u06ee\3\2\2\2\u06f4\u06ef\3")
        buf.write("\2\2\2\u06f4\u06f0\3\2\2\2\u06f4\u06f1\3\2\2\2\u06f4\u06f2")
        buf.write("\3\2\2\2\u06f4\u06f3\3\2\2\2\u06f5\u06f8\3\2\2\2\u06f6")
        buf.write("\u06f4\3\2\2\2\u06f6\u06f7\3\2\2\2\u06f7\u06fc\3\2\2\2")
        buf.write("\u06f8\u06f6\3\2\2\2\u06f9\u06fb\7k\2\2\u06fa\u06f9\3")
        buf.write("\2\2\2\u06fb\u06fe\3\2\2\2\u06fc\u06fa\3\2\2\2\u06fc\u06fd")
        buf.write("\3\2\2\2\u06fd\u0701\3\2\2\2\u06fe\u06fc\3\2\2\2\u06ff")
        buf.write("\u0702\5\u0188\u00c5\2\u0700\u0702\5\u018c\u00c7\2\u0701")
        buf.write("\u06ff\3\2\2\2\u0701\u0700\3\2\2\2\u0701\u0702\3\2\2\2")
        buf.write("\u0702\u0706\3\2\2\2\u0703\u0705\7k\2\2\u0704\u0703\3")
        buf.write("\2\2\2\u0705\u0708\3\2\2\2\u0706\u0704\3\2\2\2\u0706\u0707")
        buf.write("\3\2\2\2\u0707\u070c\3\2\2\2\u0708\u0706\3\2\2\2\u0709")
        buf.write("\u070b\5\u0184\u00c3\2\u070a\u0709\3\2\2\2\u070b\u070e")
        buf.write("\3\2\2\2\u070c\u070a\3\2\2\2\u070c\u070d\3\2\2\2\u070d")
        buf.write("\u0712\3\2\2\2\u070e\u070c\3\2\2\2\u070f\u0711\7k\2\2")
        buf.write("\u0710\u070f\3\2\2\2\u0711\u0714\3\2\2\2\u0712\u0710\3")
        buf.write("\2\2\2\u0712\u0713\3\2\2\2\u0713\u0715\3\2\2\2\u0714\u0712")
        buf.write("\3\2\2\2\u0715\u0716\7t\2\2\u0716\u0183\3\2\2\2\u0717")
        buf.write("\u071b\5\u01ac\u00d7\2\u0718\u071a\7k\2\2\u0719\u0718")
        buf.write("\3\2\2\2\u071a\u071d\3\2\2\2\u071b\u0719\3\2\2\2\u071b")
        buf.write("\u071c\3\2\2\2\u071c\u071e\3\2\2\2\u071d\u071b\3\2\2\2")
        buf.write("\u071e\u0722\7s\2\2\u071f\u0721\7k\2\2\u0720\u071f\3\2")
        buf.write("\2\2\u0721\u0724\3\2\2\2\u0722\u0720\3\2\2\2\u0722\u0723")
        buf.write("\3\2\2\2\u0723\u0725\3\2\2\2\u0724\u0722\3\2\2\2\u0725")
        buf.write("\u0729\5\u015a\u00ae\2\u0726\u0728\7k\2\2\u0727\u0726")
        buf.write("\3\2\2\2\u0728\u072b\3\2\2\2\u0729\u0727\3\2\2\2\u0729")
        buf.write("\u072a\3\2\2\2\u072a\u072c\3\2\2\2\u072b\u0729\3\2\2\2")
        buf.write("\u072c\u0730\7t\2\2\u072d\u072f\7k\2\2\u072e\u072d\3\2")
        buf.write("\2\2\u072f\u0732\3\2\2\2\u0730\u072e\3\2\2\2\u0730\u0731")
        buf.write("\3\2\2\2\u0731\u0185\3\2\2\2\u0732\u0730\3\2\2\2\u0733")
        buf.write("\u0734\5\32\16\2\u0734\u0187\3\2\2\2\u0735\u0736\7s\2")
        buf.write("\2\u0736\u0737\5\u018a\u00c6\2\u0737\u0738\7t\2\2\u0738")
        buf.write("\u073a\3\2\2\2\u0739\u0735\3\2\2\2\u0739\u073a\3\2\2\2")
        buf.write("\u073a\u073b\3\2\2\2\u073b\u073c\7~\2\2\u073c\u073d\7")
        buf.write("p\2\2\u073d\u073e\5(\25\2\u073e\u0189\3\2\2\2\u073f\u0740")
        buf.write("\t\r\2\2\u0740\u018b\3\2\2\2\u0741\u0742\7s\2\2\u0742")
        buf.write("\u0743\5\u018a\u00c6\2\u0743\u0744\7t\2\2\u0744\u0746")
        buf.write("\3\2\2\2\u0745\u0741\3\2\2\2\u0745\u0746\3\2\2\2\u0746")
        buf.write("\u0747\3\2\2\2\u0747\u0748\7~\2\2\u0748\u0749\7p\2\2\u0749")
        buf.write("\u074a\5\u018e\u00c8\2\u074a\u018d\3\2\2\2\u074b\u074c")
        buf.write("\t\4\2\2\u074c\u018f\3\2\2\2\u074d\u074e\7|\2\2\u074e")
        buf.write("\u0751\5\32\16\2\u074f\u0751\5\34\17\2\u0750\u074d\3\2")
        buf.write("\2\2\u0750\u074f\3\2\2\2\u0751\u0191\3\2\2\2\u0752\u0753")
        buf.write("\5(\25\2\u0753\u0193\3\2\2\2\u0754\u0755\7*\2\2\u0755")
        buf.write("\u0756\7q\2\2\u0756\u0757\5\32\16\2\u0757\u0195\3\2\2")
        buf.write("\2\u0758\u0759\7/\2\2\u0759\u075a\7q\2\2\u075a\u075b\5")
        buf.write("\u0198\u00cd\2\u075b\u0197\3\2\2\2\u075c\u075d\t\4\2\2")
        buf.write("\u075d\u0199\3\2\2\2\u075e\u075f\7.\2\2\u075f\u0760\7")
        buf.write("q\2\2\u0760\u0761\5\u019c\u00cf\2\u0761\u019b\3\2\2\2")
        buf.write("\u0762\u0763\t\4\2\2\u0763\u019d\3\2\2\2\u0764\u0765\7")
        buf.write("\63\2\2\u0765\u0766\7q\2\2\u0766\u0767\5\32\16\2\u0767")
        buf.write("\u019f\3\2\2\2\u0768\u076c\7\61\2\2\u0769\u076d\5&\24")
        buf.write("\2\u076a\u076b\7q\2\2\u076b\u076d\5(\25\2\u076c\u0769")
        buf.write("\3\2\2\2\u076c\u076a\3\2\2\2\u076d\u01a1\3\2\2\2\u076e")
        buf.write("\u0772\7\60\2\2\u076f\u0773\5&\24\2\u0770\u0771\7q\2\2")
        buf.write("\u0771\u0773\5(\25\2\u0772\u076f\3\2\2\2\u0772\u0770\3")
        buf.write("\2\2\2\u0773\u01a3\3\2\2\2\u0774\u0775\7\62\2\2\u0775")
        buf.write("\u0776\7q\2\2\u0776\u0777\5\32\16\2\u0777\u01a5\3\2\2")
        buf.write("\2\u0778\u0779\7\64\2\2\u0779\u077a\7q\2\2\u077a\u077b")
        buf.write("\5\32\16\2\u077b\u01a7\3\2\2\2\u077c\u077d\7:\2\2\u077d")
        buf.write("\u077e\7q\2\2\u077e\u077f\5\u01aa\u00d6\2\u077f\u01a9")
        buf.write("\3\2\2\2\u0780\u0785\5\u01ac\u00d7\2\u0781\u0782\7z\2")
        buf.write("\2\u0782\u0784\5\u01ac\u00d7\2\u0783\u0781\3\2\2\2\u0784")
        buf.write("\u0787\3\2\2\2\u0785\u0783\3\2\2\2\u0785\u0786\3\2\2\2")
        buf.write("\u0786\u01ab\3\2\2\2\u0787\u0785\3\2\2\2\u0788\u0789\t")
        buf.write("\16\2\2\u0789\u01ad\3\2\2\2\u078a\u078b\7Q\2\2\u078b\u078c")
        buf.write("\7q\2\2\u078c\u078d\5\u01b0\u00d9\2\u078d\u01af\3\2\2")
        buf.write("\2\u078e\u0793\5\u01b2\u00da\2\u078f\u0790\7z\2\2\u0790")
        buf.write("\u0792\5\u01b2\u00da\2\u0791\u078f\3\2\2\2\u0792\u0795")
        buf.write("\3\2\2\2\u0793\u0791\3\2\2\2\u0793\u0794\3\2\2\2\u0794")
        buf.write("\u01b1\3\2\2\2\u0795\u0793\3\2\2\2\u0796\u0798\5\u01b4")
        buf.write("\u00db\2\u0797\u0799\5\u01b6\u00dc\2\u0798\u0797\3\2\2")
        buf.write("\2\u0798\u0799\3\2\2\2\u0799\u01b3\3\2\2\2\u079a\u07a0")
        buf.write("\7\u0082\2\2\u079b\u079d\7r\2\2\u079c\u079b\3\2\2\2\u079c")
        buf.write("\u079d\3\2\2\2\u079d\u079e\3\2\2\2\u079e\u07a0\5\32\16")
        buf.write("\2\u079f\u079a\3\2\2\2\u079f\u079c\3\2\2\2\u07a0\u01b5")
        buf.write("\3\2\2\2\u07a1\u07a2\5(\25\2\u07a2\u01b7\3\2\2\2\u07a3")
        buf.write("\u07a4\7\65\2\2\u07a4\u07a5\7q\2\2\u07a5\u07a6\5\u01ba")
        buf.write("\u00de\2\u07a6\u01b9\3\2\2\2\u07a7\u07ac\5\u01bc\u00df")
        buf.write("\2\u07a8\u07a9\7z\2\2\u07a9\u07ab\5\u01bc\u00df\2\u07aa")
        buf.write("\u07a8\3\2\2\2\u07ab\u07ae\3\2\2\2\u07ac\u07aa\3\2\2\2")
        buf.write("\u07ac\u07ad\3\2\2\2\u07ad\u01bb\3\2\2\2\u07ae\u07ac\3")
        buf.write("\2\2\2\u07af\u07b0\5\u01be\u00e0\2\u07b0\u01bd\3\2\2\2")
        buf.write("\u07b1\u07b7\7\u0082\2\2\u07b2\u07b4\7r\2\2\u07b3\u07b2")
        buf.write("\3\2\2\2\u07b3\u07b4\3\2\2\2\u07b4\u07b5\3\2\2\2\u07b5")
        buf.write("\u07b7\5\32\16\2\u07b6\u07b1\3\2\2\2\u07b6\u07b3\3\2\2")
        buf.write("\2\u07b7\u01bf\3\2\2\2\u07b8\u07b9\7\f\2\2\u07b9\u07ba")
        buf.write("\5\u0182\u00c2\2\u07ba\u01c1\3\2\2\2\u07bb\u07bc\7\13")
        buf.write("\2\2\u07bc\u07bd\5\u0182\u00c2\2\u07bd\u01c3\3\2\2\2\u07be")
        buf.write("\u07bf\7\n\2\2\u07bf\u07c0\5\u0182\u00c2\2\u07c0\u01c5")
        buf.write("\3\2\2\2\u07c1\u07c2\7\b\2\2\u07c2\u07c3\7{\2\2\u07c3")
        buf.write("\u07c4\5\u01c8\u00e5\2\u07c4\u07c8\7s\2\2\u07c5\u07c7")
        buf.write("\7k\2\2\u07c6\u07c5\3\2\2\2\u07c7\u07ca\3\2\2\2\u07c8")
        buf.write("\u07c6\3\2\2\2\u07c8\u07c9\3\2\2\2\u07c9\u07cc\3\2\2\2")
        buf.write("\u07ca\u07c8\3\2\2\2\u07cb\u07cd\5\u01ca\u00e6\2\u07cc")
        buf.write("\u07cb\3\2\2\2\u07cd\u07ce\3\2\2\2\u07ce\u07cc\3\2\2\2")
        buf.write("\u07ce\u07cf\3\2\2\2\u07cf\u07d3\3\2\2\2\u07d0\u07d2\7")
        buf.write("k\2\2\u07d1\u07d0\3\2\2\2\u07d2\u07d5\3\2\2\2\u07d3\u07d1")
        buf.write("\3\2\2\2\u07d3\u07d4\3\2\2\2\u07d4\u07d6\3\2\2\2\u07d5")
        buf.write("\u07d3\3\2\2\2\u07d6\u07d7\7t\2\2\u07d7\u01c7\3\2\2\2")
        buf.write("\u07d8\u07d9\5\32\16\2\u07d9\u01c9\3\2\2\2\u07da\u07dc")
        buf.write("\7z\2\2\u07db\u07da\3\2\2\2\u07db\u07dc\3\2\2\2\u07dc")
        buf.write("\u07e0\3\2\2\2\u07dd\u07df\7k\2\2\u07de\u07dd\3\2\2\2")
        buf.write("\u07df\u07e2\3\2\2\2\u07e0\u07de\3\2\2\2\u07e0\u07e1\3")
        buf.write("\2\2\2\u07e1\u07e4\3\2\2\2\u07e2\u07e0\3\2\2\2\u07e3\u07e5")
        buf.write("\5\u01d0\u00e9\2\u07e4\u07e3\3\2\2\2\u07e4\u07e5\3\2\2")
        buf.write("\2\u07e5\u07e6\3\2\2\2\u07e6\u07e9\5\u01de\u00f0\2\u07e7")
        buf.write("\u07ea\5\u01ce\u00e8\2\u07e8\u07ea\5\u01cc\u00e7\2\u07e9")
        buf.write("\u07e7\3\2\2\2\u07e9\u07e8\3\2\2\2\u07ea\u07ee\3\2\2\2")
        buf.write("\u07eb\u07ed\7k\2\2\u07ec\u07eb\3\2\2\2\u07ed\u07f0\3")
        buf.write("\2\2\2\u07ee\u07ec\3\2\2\2\u07ee\u07ef\3\2\2\2\u07ef\u01cb")
        buf.write("\3\2\2\2\u07f0\u07ee\3\2\2\2\u07f1\u07f4\7q\2\2\u07f2")
        buf.write("\u07f5\5\u01da\u00ee\2\u07f3\u07f5\5\u01d8\u00ed\2\u07f4")
        buf.write("\u07f2\3\2\2\2\u07f4\u07f3\3\2\2\2\u07f5\u01cd\3\2\2\2")
        buf.write("\u07f6\u07f7\5&\24\2\u07f7\u01cf\3\2\2\2\u07f8\u07f9\7")
        buf.write("u\2\2\u07f9\u07fe\5\u01d2\u00ea\2\u07fa\u07fb\7z\2\2\u07fb")
        buf.write("\u07fd\5\u01d2\u00ea\2\u07fc\u07fa\3\2\2\2\u07fd\u0800")
        buf.write("\3\2\2\2\u07fe\u07fc\3\2\2\2\u07fe\u07ff\3\2\2\2\u07ff")
        buf.write("\u0801\3\2\2\2\u0800\u07fe\3\2\2\2\u0801\u0802\7v\2\2")
        buf.write("\u0802\u01d1\3\2\2\2\u0803\u0804\5\u01d4\u00eb\2\u0804")
        buf.write("\u0805\7~\2\2\u0805\u0806\5\u01d6\u00ec\2\u0806\u01d3")
        buf.write("\3\2\2\2\u0807\u0808\5\32\16\2\u0808\u01d5\3\2\2\2\u0809")
        buf.write("\u080d\7\u0085\2\2\u080a\u080d\7\u0086\2\2\u080b\u080d")
        buf.write("\5\32\16\2\u080c\u0809\3\2\2\2\u080c\u080a\3\2\2\2\u080c")
        buf.write("\u080b\3\2\2\2\u080d\u01d7\3\2\2\2\u080e\u080f\t\4\2\2")
        buf.write("\u080f\u01d9\3\2\2\2\u0810\u0811\7-\2\2\u0811\u0812\7")
        buf.write("s\2\2\u0812\u0813\5\u01dc\u00ef\2\u0813\u0814\7t\2\2\u0814")
        buf.write("\u01db\3\2\2\2\u0815\u0816\5\32\16\2\u0816\u01dd\3\2\2")
        buf.write("\2\u0817\u081b\7\u0085\2\2\u0818\u081b\7\u0086\2\2\u0819")
        buf.write("\u081b\5\32\16\2\u081a\u0817\3\2\2\2\u081a\u0818\3\2\2")
        buf.write("\2\u081a\u0819\3\2\2\2\u081b\u01df\3\2\2\2\u081c\u081e")
        buf.write("\7\7\2\2\u081d\u081f\5(\25\2\u081e\u081d\3\2\2\2\u081e")
        buf.write("\u081f\3\2\2\2\u081f\u01e1\3\2\2\2\u0820\u0821\7\5\2\2")
        buf.write("\u0821\u0824\7s\2\2\u0822\u0825\5\u01e4\u00f3\2\u0823")
        buf.write("\u0825\7k\2\2\u0824\u0822\3\2\2\2\u0824\u0823\3\2\2\2")
        buf.write("\u0825\u0826\3\2\2\2\u0826\u0824\3\2\2\2\u0826\u0827\3")
        buf.write("\2\2\2\u0827\u0828\3\2\2\2\u0828\u0829\7t\2\2\u0829\u01e3")
        buf.write("\3\2\2\2\u082a\u082c\5\u01e6\u00f4\2\u082b\u082d\5\u01e8")
        buf.write("\u00f5\2\u082c\u082b\3\2\2\2\u082c\u082d\3\2\2\2\u082d")
        buf.write("\u082f\3\2\2\2\u082e\u0830\5\u01ea\u00f6\2\u082f\u082e")
        buf.write("\3\2\2\2\u082f\u0830\3\2\2\2\u0830\u0832\3\2\2\2\u0831")
        buf.write("\u0833\7z\2\2\u0832\u0831\3\2\2\2\u0832\u0833\3\2\2\2")
        buf.write("\u0833\u0835\3\2\2\2\u0834\u0836\7k\2\2\u0835\u0834\3")
        buf.write("\2\2\2\u0835\u0836\3\2\2\2\u0836\u01e5\3\2\2\2\u0837\u0838")
        buf.write("\7|\2\2\u0838\u083b\5\32\16\2\u0839\u083b\5\34\17\2\u083a")
        buf.write("\u0837\3\2\2\2\u083a\u0839\3\2\2\2\u083b\u01e7\3\2\2\2")
        buf.write("\u083c\u083d\5(\25\2\u083d\u01e9\3\2\2\2\u083e\u083f\7")
        buf.write("~\2\2\u083f\u0849\7p\2\2\u0840\u084a\7\u0082\2\2\u0841")
        buf.write("\u0846\5\u01ec\u00f7\2\u0842\u0843\7z\2\2\u0843\u0845")
        buf.write("\5\u01ec\u00f7\2\u0844\u0842\3\2\2\2\u0845\u0848\3\2\2")
        buf.write("\2\u0846\u0844\3\2\2\2\u0846\u0847\3\2\2\2\u0847\u084a")
        buf.write("\3\2\2\2\u0848\u0846\3\2\2\2\u0849\u0840\3\2\2\2\u0849")
        buf.write("\u0841\3\2\2\2\u084a\u01eb\3\2\2\2\u084b\u084c\5\32\16")
        buf.write("\2\u084c\u01ed\3\2\2\2\u084d\u0850\7\3\2\2\u084e\u084f")
        buf.write("\7s\2\2\u084f\u0851\7t\2\2\u0850\u084e\3\2\2\2\u0850\u0851")
        buf.write("\3\2\2\2\u0851\u01ef\3\2\2\2\u0852\u0855\7\26\2\2\u0853")
        buf.write("\u0854\7{\2\2\u0854\u0856\5\u01f2\u00fa\2\u0855\u0853")
        buf.write("\3\2\2\2\u0855\u0856\3\2\2\2\u0856\u0857\3\2\2\2\u0857")
        buf.write("\u0858\5(\25\2\u0858\u01f1\3\2\2\2\u0859\u085a\5\32\16")
        buf.write("\2\u085a\u01f3\3\2\2\2\u00d9\u01f7\u01fd\u0203\u0207\u020c")
        buf.write("\u020e\u0213\u0217\u021c\u021e\u0223\u022b\u0230\u0238")
        buf.write("\u023f\u0242\u024b\u0251\u0254\u0263\u0267\u026f\u0275")
        buf.write("\u027a\u027d\u0280\u0284\u028c\u029a\u029f\u02ab\u02b1")
        buf.write("\u02b6\u02c3\u02c9\u02ce\u02d4\u02da\u02e0\u02e6\u02ee")
        buf.write("\u02f1\u02f5\u02f9\u0304\u030a\u030f\u0316\u031d\u0322")
        buf.write("\u0325\u0328\u032d\u0330\u0334\u0339\u033e\u0343\u0356")
        buf.write("\u035a\u0378\u0397\u039b\u03a6\u03aa\u03b1\u03bb\u03c4")
        buf.write("\u03c8\u03cf\u03de\u03e8\u03f1\u03fa\u0409\u0413\u0416")
        buf.write("\u0434\u0447\u044d\u0453\u0459\u045b\u046a\u046c\u0477")
        buf.write("\u047f\u0484\u048a\u048f\u0495\u049a\u04a0\u04a9\u04b2")
        buf.write("\u04b9\u04be\u04ca\u04d3\u04e0\u04e7\u04f2\u04f4\u0505")
        buf.write("\u0508\u050c\u0535\u0547\u0549\u054f\u0553\u0558\u0560")
        buf.write("\u0568\u056e\u0578\u0586\u0590\u0592\u0596\u05ad\u05b2")
        buf.write("\u05c2\u05cb\u05d4\u05dd\u05e6\u05ef\u05f6\u05fd\u0602")
        buf.write("\u0606\u060a\u060e\u0610\u0614\u0621\u0628\u0630\u0632")
        buf.write("\u0635\u063c\u063e\u0646\u064d\u0650\u0652\u0659\u065f")
        buf.write("\u0663\u0668\u066e\u0679\u067c\u0685\u0689\u068e\u0691")
        buf.write("\u069a\u06ad\u06b2\u06bd\u06c5\u06d0\u06da\u06e0\u06e5")
        buf.write("\u06f4\u06f6\u06fc\u0701\u0706\u070c\u0712\u071b\u0722")
        buf.write("\u0729\u0730\u0739\u0745\u0750\u076c\u0772\u0785\u0793")
        buf.write("\u0798\u079c\u079f\u07ac\u07b3\u07b6\u07c8\u07ce\u07d3")
        buf.write("\u07db\u07e0\u07e4\u07e9\u07ee\u07f4\u07fe\u080c\u081a")
        buf.write("\u081e\u0824\u0826\u082c\u082f\u0832\u0835\u083a\u0846")
        buf.write("\u0849\u0850\u0855")
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
                     "'@suit'", "<INVALID>", "<INVALID>", "'theme'", "'filter_out'", 
                     "'filter_in'", "'page'", "'link_suffix'", "'url_prefix'", 
                     "'can_edit'", "'object_expr'", "'block'", "'item_name'", 
                     "'pk_param'", "'list_fields'", "'delete'", "'edit'", 
                     "'create'", "'detail'", "'skip'", "'from'", "'+polymorphic_list'", 
                     "'css'", "'js'", "<INVALID>", "<INVALID>", "'inline'", 
                     "'type'", "'user_field'", "'annotate'", "'on_create'", 
                     "'query'", "'auth'", "'count'", "'i18n'", "'extra'", 
                     "'tabs'", "'list'", "'read_only'", "'list_editable'", 
                     "'list_filter'", "'list_search'", "'fields'", "'import'", 
                     "'as'", "'text'", "'html'", "'html_media'", "'float'", 
                     "'decimal'", "'date'", "'datetime'", "'create_time'", 
                     "'update_time'", "'image'", "'file'", "'filer_image'", 
                     "'filer_file'", "'filer_folder'", "'filer_image_folder'", 
                     "'str'", "'int'", "'slug'", "'bool'", "'one'", "'one2one'", 
                     "'many'", "'choices'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'<'", "'>'", "':'", "'^'", "'('", "')'", 
                     "'['", "']'", "'?'", "'_'", "'-'", "','", "'.'", "'#'", 
                     "'/'", "'='", "'$'", "'&'", "'!'", "'*'", "'~'", "'|'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "' '", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "';'", "<INVALID>", "'\n'" ]

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
                      "KW_THEME", "KW_FILTER_OUT", "KW_FILTER_IN", "KW_PAGE", 
                      "KW_LINK_SUFFIX", "KW_URL_PREFIX", "KW_CAN_EDIT", 
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
    RULE_field_list_expr = 14
    RULE_field_list_expr_field = 15
    RULE_write_mode_expr = 16
    RULE_python_code = 17
    RULE_code_line = 18
    RULE_code_block = 19
    RULE_cs_annotation = 20
    RULE_an_filer = 21
    RULE_an_langs = 22
    RULE_an_langs_list = 23
    RULE_an_celery = 24
    RULE_an_channels = 25
    RULE_an_file = 26
    RULE_an_file_name = 27
    RULE_an_suit = 28
    RULE_an_suit_app_name = 29
    RULE_col = 30
    RULE_col_str_expr = 31
    RULE_col_header = 32
    RULE_col_header_line_separator = 33
    RULE_col_verbose_name = 34
    RULE_verbose_name_part = 35
    RULE_col_base_name = 36
    RULE_col_name = 37
    RULE_col_field = 38
    RULE_col_field_expr_or_def = 39
    RULE_col_field_custom = 40
    RULE_col_field_extend = 41
    RULE_col_field_extend_append = 42
    RULE_wrong_field_type = 43
    RULE_col_field_expr = 44
    RULE_col_field_expr_marker = 45
    RULE_col_feild_expr_code = 46
    RULE_string_or_quoted = 47
    RULE_col_field_help_text = 48
    RULE_col_field_verbose_name = 49
    RULE_col_field_name = 50
    RULE_col_modifier = 51
    RULE_col_field_def = 52
    RULE_field_longtext = 53
    RULE_field_html = 54
    RULE_field_html_media = 55
    RULE_field_float = 56
    RULE_field_decimal = 57
    RULE_field_date = 58
    RULE_field_datetime = 59
    RULE_field_create_time = 60
    RULE_field_update_time = 61
    RULE_field_file = 62
    RULE_field_filer_file = 63
    RULE_field_filer_folder = 64
    RULE_field_text = 65
    RULE_field_text_size = 66
    RULE_field_text_choices = 67
    RULE_field_text_choice = 68
    RULE_field_text_choice_val = 69
    RULE_field_text_choice_key = 70
    RULE_field_int = 71
    RULE_field_int_choices = 72
    RULE_field_int_choice = 73
    RULE_field_int_choice_val = 74
    RULE_field_int_choice_key = 75
    RULE_field_slug = 76
    RULE_field_slug_ref_field = 77
    RULE_field_slug_ref_field_id = 78
    RULE_field_bool = 79
    RULE_field_bool_default = 80
    RULE_field_image = 81
    RULE_filer_image_type = 82
    RULE_field_image_sizes = 83
    RULE_field_image_size = 84
    RULE_field_image_size_dimensions = 85
    RULE_field_image_size_name = 86
    RULE_field_image_filters = 87
    RULE_field_image_filter = 88
    RULE_field_relation = 89
    RULE_field_relation_type = 90
    RULE_field_relation_target_ref = 91
    RULE_field_relation_target_class = 92
    RULE_field_relation_related_name = 93
    RULE_model_annotation = 94
    RULE_an_sortable = 95
    RULE_an_sortable_field_name = 96
    RULE_an_order = 97
    RULE_an_order_fields = 98
    RULE_an_rest = 99
    RULE_an_rest_config = 100
    RULE_an_rest_main_part = 101
    RULE_an_rest_descriptor = 102
    RULE_an_rest_i18n = 103
    RULE_an_rest_query = 104
    RULE_an_rest_on_create = 105
    RULE_an_rest_filter_in = 106
    RULE_an_rest_filter_out = 107
    RULE_an_rest_read_only = 108
    RULE_an_rest_user_field = 109
    RULE_an_rest_fields = 110
    RULE_an_rest_fields_write_mode = 111
    RULE_an_rest_auth = 112
    RULE_an_rest_auth_type = 113
    RULE_an_rest_auth_token_model = 114
    RULE_an_rest_auth_token_class = 115
    RULE_an_rest_annotate = 116
    RULE_an_rest_annotate_count = 117
    RULE_an_rest_annotate_count_field = 118
    RULE_an_rest_annotate_count_alias = 119
    RULE_an_rest_inline = 120
    RULE_an_rest_inline_decl = 121
    RULE_an_rest_inline_name = 122
    RULE_an_api = 123
    RULE_an_api_all = 124
    RULE_an_api_name = 125
    RULE_an_clean = 126
    RULE_an_pre_save = 127
    RULE_an_post_save = 128
    RULE_an_pre_delete = 129
    RULE_an_post_delete = 130
    RULE_an_m2m_changed = 131
    RULE_an_mixin = 132
    RULE_an_date_tree = 133
    RULE_an_date_tree_field = 134
    RULE_an_tree = 135
    RULE_an_tree_poly = 136
    RULE_an_admin = 137
    RULE_an_admin_js = 138
    RULE_an_admin_css = 139
    RULE_an_admin_css_file_name = 140
    RULE_an_admin_js_file_name = 141
    RULE_an_admin_inlines = 142
    RULE_an_admin_inline = 143
    RULE_inline_name = 144
    RULE_inline_type = 145
    RULE_inline_extra = 146
    RULE_inline_fields = 147
    RULE_an_admin_tabs = 148
    RULE_an_admin_tab = 149
    RULE_tab_name = 150
    RULE_tab_verbose_name = 151
    RULE_an_admin_list = 152
    RULE_an_admin_read_only = 153
    RULE_an_admin_list_editable = 154
    RULE_an_admin_list_filter = 155
    RULE_an_admin_list_search = 156
    RULE_an_admin_fields = 157
    RULE_page = 158
    RULE_page_header = 159
    RULE_page_base = 160
    RULE_page_alias = 161
    RULE_page_alias_name = 162
    RULE_page_template = 163
    RULE_template_name = 164
    RULE_file_name_part = 165
    RULE_page_url = 166
    RULE_url_part = 167
    RULE_url_param = 168
    RULE_url_segment = 169
    RULE_url_segments = 170
    RULE_page_name = 171
    RULE_page_body = 172
    RULE_page_code = 173
    RULE_page_field = 174
    RULE_page_field_name = 175
    RULE_page_field_code = 176
    RULE_page_function = 177
    RULE_page_function_name = 178
    RULE_page_function_args = 179
    RULE_page_annotation = 180
    RULE_an_react = 181
    RULE_an_react_type = 182
    RULE_an_react_descriptor = 183
    RULE_an_markdown = 184
    RULE_an_markdown_descriptor = 185
    RULE_an_auth = 186
    RULE_an_error = 187
    RULE_an_error_code = 188
    RULE_an_post = 189
    RULE_an_crud_create = 190
    RULE_an_crud = 191
    RULE_an_crud_params = 192
    RULE_an_crud_page_override = 193
    RULE_an_crud_descriptor = 194
    RULE_an_crud_next_page = 195
    RULE_an_crud_next_page_event_name = 196
    RULE_an_crud_next_page_url = 197
    RULE_an_crud_next_page_url_val = 198
    RULE_an_crud_target_model = 199
    RULE_an_crud_target_filter = 200
    RULE_an_crud_theme = 201
    RULE_an_crud_url_prefix = 202
    RULE_an_crud_url_prefix_val = 203
    RULE_an_crud_link_suffix = 204
    RULE_an_crud_link_suffix_val = 205
    RULE_an_crud_item_name = 206
    RULE_an_crud_object_expr = 207
    RULE_an_crud_can_edit = 208
    RULE_an_crud_block = 209
    RULE_an_crud_pk_param = 210
    RULE_an_crud_skip = 211
    RULE_an_crud_skip_values = 212
    RULE_an_crud_view_name = 213
    RULE_an_crud_fields = 214
    RULE_an_crud_fields_expr = 215
    RULE_an_crud_field = 216
    RULE_an_crud_field_spec = 217
    RULE_an_crud_field_filter = 218
    RULE_an_crud_list_fields = 219
    RULE_an_crud_list_fields_expr = 220
    RULE_an_crud_list_field = 221
    RULE_an_crud_list_field_spec = 222
    RULE_an_crud_edit = 223
    RULE_an_crud_delete = 224
    RULE_an_crud_detail = 225
    RULE_an_menu = 226
    RULE_an_menu_descriptor = 227
    RULE_an_menu_item = 228
    RULE_an_menu_target = 229
    RULE_an_menu_item_code = 230
    RULE_an_menu_item_args = 231
    RULE_an_menu_item_arg = 232
    RULE_an_menu_item_arg_key = 233
    RULE_an_menu_item_arg_val = 234
    RULE_an_menu_item_url = 235
    RULE_an_menu_item_page = 236
    RULE_an_menu_item_page_ref = 237
    RULE_an_menu_label = 238
    RULE_an_get = 239
    RULE_an_stream = 240
    RULE_an_stream_model = 241
    RULE_an_stream_target_model = 242
    RULE_an_stream_target_filter = 243
    RULE_an_stream_field_list = 244
    RULE_an_stream_field_name = 245
    RULE_an_flutter = 246
    RULE_an_html = 247
    RULE_an_html_descriptor = 248

    ruleNames =  [ "col_file", "page_imports", "model_imports", "page_import_statement", 
                   "model_import_statement", "import_statement", "import_source", 
                   "import_list", "import_item", "import_item_name", "import_item_alias", 
                   "import_item_all", "id_or_kw", "classname", "field_list_expr", 
                   "field_list_expr_field", "write_mode_expr", "python_code", 
                   "code_line", "code_block", "cs_annotation", "an_filer", 
                   "an_langs", "an_langs_list", "an_celery", "an_channels", 
                   "an_file", "an_file_name", "an_suit", "an_suit_app_name", 
                   "col", "col_str_expr", "col_header", "col_header_line_separator", 
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
                   "field_relation", "field_relation_type", "field_relation_target_ref", 
                   "field_relation_target_class", "field_relation_related_name", 
                   "model_annotation", "an_sortable", "an_sortable_field_name", 
                   "an_order", "an_order_fields", "an_rest", "an_rest_config", 
                   "an_rest_main_part", "an_rest_descriptor", "an_rest_i18n", 
                   "an_rest_query", "an_rest_on_create", "an_rest_filter_in", 
                   "an_rest_filter_out", "an_rest_read_only", "an_rest_user_field", 
                   "an_rest_fields", "an_rest_fields_write_mode", "an_rest_auth", 
                   "an_rest_auth_type", "an_rest_auth_token_model", "an_rest_auth_token_class", 
                   "an_rest_annotate", "an_rest_annotate_count", "an_rest_annotate_count_field", 
                   "an_rest_annotate_count_alias", "an_rest_inline", "an_rest_inline_decl", 
                   "an_rest_inline_name", "an_api", "an_api_all", "an_api_name", 
                   "an_clean", "an_pre_save", "an_post_save", "an_pre_delete", 
                   "an_post_delete", "an_m2m_changed", "an_mixin", "an_date_tree", 
                   "an_date_tree_field", "an_tree", "an_tree_poly", "an_admin", 
                   "an_admin_js", "an_admin_css", "an_admin_css_file_name", 
                   "an_admin_js_file_name", "an_admin_inlines", "an_admin_inline", 
                   "inline_name", "inline_type", "inline_extra", "inline_fields", 
                   "an_admin_tabs", "an_admin_tab", "tab_name", "tab_verbose_name", 
                   "an_admin_list", "an_admin_read_only", "an_admin_list_editable", 
                   "an_admin_list_filter", "an_admin_list_search", "an_admin_fields", 
                   "page", "page_header", "page_base", "page_alias", "page_alias_name", 
                   "page_template", "template_name", "file_name_part", "page_url", 
                   "url_part", "url_param", "url_segment", "url_segments", 
                   "page_name", "page_body", "page_code", "page_field", 
                   "page_field_name", "page_field_code", "page_function", 
                   "page_function_name", "page_function_args", "page_annotation", 
                   "an_react", "an_react_type", "an_react_descriptor", "an_markdown", 
                   "an_markdown_descriptor", "an_auth", "an_error", "an_error_code", 
                   "an_post", "an_crud_create", "an_crud", "an_crud_params", 
                   "an_crud_page_override", "an_crud_descriptor", "an_crud_next_page", 
                   "an_crud_next_page_event_name", "an_crud_next_page_url", 
                   "an_crud_next_page_url_val", "an_crud_target_model", 
                   "an_crud_target_filter", "an_crud_theme", "an_crud_url_prefix", 
                   "an_crud_url_prefix_val", "an_crud_link_suffix", "an_crud_link_suffix_val", 
                   "an_crud_item_name", "an_crud_object_expr", "an_crud_can_edit", 
                   "an_crud_block", "an_crud_pk_param", "an_crud_skip", 
                   "an_crud_skip_values", "an_crud_view_name", "an_crud_fields", 
                   "an_crud_fields_expr", "an_crud_field", "an_crud_field_spec", 
                   "an_crud_field_filter", "an_crud_list_fields", "an_crud_list_fields_expr", 
                   "an_crud_list_field", "an_crud_list_field_spec", "an_crud_edit", 
                   "an_crud_delete", "an_crud_detail", "an_menu", "an_menu_descriptor", 
                   "an_menu_item", "an_menu_target", "an_menu_item_code", 
                   "an_menu_item_args", "an_menu_item_arg", "an_menu_item_arg_key", 
                   "an_menu_item_arg_val", "an_menu_item_url", "an_menu_item_page", 
                   "an_menu_item_page_ref", "an_menu_label", "an_get", "an_stream", 
                   "an_stream_model", "an_stream_target_model", "an_stream_target_filter", 
                   "an_stream_field_list", "an_stream_field_name", "an_flutter", 
                   "an_html", "an_html_descriptor" ]

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
    KW_FILTER_OUT=41
    KW_FILTER_IN=42
    KW_PAGE=43
    KW_LINK_SUFFIX=44
    KW_URL_PREFIX=45
    KW_CAN_EDIT=46
    KW_OBJECT_EXPR=47
    KW_BLOCK=48
    KW_ITEM_NAME=49
    KW_PK_PARAM=50
    KW_LIST_FIELDS=51
    KW_DELETE=52
    KW_EDIT=53
    KW_CREATE=54
    KW_DETAIL=55
    KW_SKIP=56
    KW_FROM=57
    KW_POLY_LIST=58
    KW_CSS=59
    KW_JS=60
    KW_INLINE_TYPE=61
    KW_AUTH_TYPE=62
    KW_INLINE=63
    KW_TYPE=64
    KW_USER_FIELD=65
    KW_ANNOTATE=66
    KW_ON_CREATE=67
    KW_QUERY=68
    KW_AUTH=69
    KW_COUNT=70
    KW_I18N=71
    KW_EXTRA=72
    KW_TABS=73
    KW_LIST=74
    KW_READ_ONLY=75
    KW_LIST_EDITABLE=76
    KW_LIST_FILTER=77
    KW_LIST_SEARCH=78
    KW_FIELDS=79
    KW_IMPORT=80
    KW_AS=81
    COL_FIELD_TYPE_LONGTEXT=82
    COL_FIELD_TYPE_HTML=83
    COL_FIELD_TYPE_HTML_MEDIA=84
    COL_FIELD_TYPE_FLOAT=85
    COL_FIELD_TYPE_DECIMAL=86
    COL_FIELD_TYPE_DATE=87
    COL_FIELD_TYPE_DATETIME=88
    COL_FIELD_TYPE_CREATE_TIME=89
    COL_FIELD_TYPE_UPDATE_TIME=90
    COL_FIELD_TYPE_IMAGE=91
    COL_FIELD_TYPE_FILE=92
    COL_FIELD_TYPE_FILER_IMAGE=93
    COL_FIELD_TYPE_FILER_FILE=94
    COL_FIELD_TYPE_FILER_FOLDER=95
    COL_FIELD_TYPE_FILER_IMAGE_FOLDER=96
    COL_FIELD_TYPE_TEXT=97
    COL_FIELD_TYPE_INT=98
    COL_FIELD_TYPE_SLUG=99
    COL_FIELD_TYPE_BOOL=100
    COL_FIELD_TYPE_ONE=101
    COL_FIELD_TYPE_ONE2ONE=102
    COL_FIELD_TYPE_MANY=103
    COL_FIELD_CHOICES=104
    NL=105
    ID=106
    DIGIT=107
    SIZE2D=108
    LT=109
    GT=110
    COLON=111
    EXCLUDE=112
    BRACE_OPEN=113
    BRACE_CLOSE=114
    SQ_BRACE_OPEN=115
    SQ_BRACE_CLOSE=116
    QUESTION_MARK=117
    UNDERSCORE=118
    DASH=119
    COMA=120
    DOT=121
    HASH=122
    SLASH=123
    EQUALS=124
    DOLLAR=125
    AMP=126
    EXCLAM=127
    STAR=128
    APPROX=129
    PIPE=130
    STRING_DQ=131
    STRING_SQ=132
    COMMENT_LINE=133
    COMMENT_BLOCK=134
    UNICODE=135
    WS=136
    COL_FIELD_CALCULATED=137
    ASSIGN=138
    ASSIGN_STATIC=139
    CODE_BLOCK=140
    ERRCHAR=141
    PYTHON_CODE=142
    PYTHON_LINE_ERRCHAR=143
    PYTHON_LINE_END=144
    PYTHON_EXPR_ERRCHAR=145
    PYTHON_LINE_NL=146

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
            self.state = 501
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 498
                    self.match(ZmeiLangParser.NL) 
                self.state = 503
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 507
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 504
                    self.cs_annotation() 
                self.state = 509
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 513
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 510
                    self.match(ZmeiLangParser.NL) 
                self.state = 515
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 524
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 517
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.KW_FROM or _la==ZmeiLangParser.KW_IMPORT:
                    self.state = 516
                    self.page_imports()


                self.state = 520 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 519
                    self.page()
                    self.state = 522 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZmeiLangParser.SQ_BRACE_OPEN):
                        break



            self.state = 529
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 526
                    self.match(ZmeiLangParser.NL) 
                self.state = 531
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 540
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.KW_FROM or _la==ZmeiLangParser.KW_IMPORT or _la==ZmeiLangParser.HASH:
                self.state = 533
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.KW_FROM or _la==ZmeiLangParser.KW_IMPORT:
                    self.state = 532
                    self.model_imports()


                self.state = 536 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 535
                    self.col()
                    self.state = 538 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZmeiLangParser.HASH):
                        break



            self.state = 545
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 542
                self.match(ZmeiLangParser.NL)
                self.state = 547
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 548
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
            self.state = 551 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 550
                self.page_import_statement()
                self.state = 553 
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
            self.state = 556 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 555
                self.model_import_statement()
                self.state = 558 
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
            self.state = 560
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
            self.state = 562
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
            self.state = 566
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.KW_FROM:
                self.state = 564
                self.match(ZmeiLangParser.KW_FROM)
                self.state = 565
                self.import_source()


            self.state = 568
            self.match(ZmeiLangParser.KW_IMPORT)
            self.state = 569
            self.import_list()
            self.state = 571 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 570
                self.match(ZmeiLangParser.NL)
                self.state = 573 
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
            self.state = 576
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 575
                self.match(ZmeiLangParser.DOT)


            self.state = 578
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
            self.state = 580
            self.import_item()
            self.state = 585
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 581
                self.match(ZmeiLangParser.COMA)
                self.state = 582
                self.import_item()
                self.state = 587
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
            self.state = 594
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 588
                self.import_item_name()
                self.state = 591
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.KW_AS:
                    self.state = 589
                    self.match(ZmeiLangParser.KW_AS)
                    self.state = 590
                    self.import_item_alias()


                pass
            elif token in [ZmeiLangParser.STAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 593
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
            self.state = 596
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
            self.state = 598
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
            self.state = 600
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
            self.state = 602
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.WRITE_MODE) | (1 << ZmeiLangParser.BOOL) | (1 << ZmeiLangParser.KW_THEME) | (1 << ZmeiLangParser.KW_FILTER_OUT) | (1 << ZmeiLangParser.KW_FILTER_IN) | (1 << ZmeiLangParser.KW_PAGE) | (1 << ZmeiLangParser.KW_LINK_SUFFIX) | (1 << ZmeiLangParser.KW_URL_PREFIX) | (1 << ZmeiLangParser.KW_CAN_EDIT) | (1 << ZmeiLangParser.KW_OBJECT_EXPR) | (1 << ZmeiLangParser.KW_BLOCK) | (1 << ZmeiLangParser.KW_ITEM_NAME) | (1 << ZmeiLangParser.KW_PK_PARAM) | (1 << ZmeiLangParser.KW_LIST_FIELDS) | (1 << ZmeiLangParser.KW_DELETE) | (1 << ZmeiLangParser.KW_EDIT) | (1 << ZmeiLangParser.KW_CREATE) | (1 << ZmeiLangParser.KW_DETAIL) | (1 << ZmeiLangParser.KW_SKIP) | (1 << ZmeiLangParser.KW_FROM) | (1 << ZmeiLangParser.KW_POLY_LIST) | (1 << ZmeiLangParser.KW_CSS) | (1 << ZmeiLangParser.KW_JS) | (1 << ZmeiLangParser.KW_INLINE_TYPE) | (1 << ZmeiLangParser.KW_AUTH_TYPE) | (1 << ZmeiLangParser.KW_INLINE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ZmeiLangParser.KW_TYPE - 64)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 64)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 64)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 64)) | (1 << (ZmeiLangParser.KW_QUERY - 64)) | (1 << (ZmeiLangParser.KW_AUTH - 64)) | (1 << (ZmeiLangParser.KW_COUNT - 64)) | (1 << (ZmeiLangParser.KW_I18N - 64)) | (1 << (ZmeiLangParser.KW_EXTRA - 64)) | (1 << (ZmeiLangParser.KW_TABS - 64)) | (1 << (ZmeiLangParser.KW_LIST - 64)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 64)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 64)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 64)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 64)) | (1 << (ZmeiLangParser.KW_FIELDS - 64)) | (1 << (ZmeiLangParser.KW_IMPORT - 64)) | (1 << (ZmeiLangParser.KW_AS - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 64)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 64)) | (1 << (ZmeiLangParser.ID - 64)))) != 0)):
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
            self.state = 604
            self.id_or_kw()
            self.state = 609
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.DOT:
                self.state = 605
                self.match(ZmeiLangParser.DOT)
                self.state = 606
                self.id_or_kw()
                self.state = 611
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 28, self.RULE_field_list_expr)
        self._la = 0 # Token type
        try:
            self.state = 635
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.DOT, ZmeiLangParser.STAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 613
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.DOT:
                    self.state = 612
                    self.match(ZmeiLangParser.DOT)


                self.state = 615
                self.match(ZmeiLangParser.STAR)
                self.state = 621
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 616
                        self.match(ZmeiLangParser.COMA)
                        self.state = 617
                        self.match(ZmeiLangParser.EXCLUDE)
                        self.state = 618
                        self.field_list_expr_field() 
                    self.state = 623
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

                pass
            elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 624
                self.id_or_kw()
                self.state = 632
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 625
                        self.match(ZmeiLangParser.COMA)
                        self.state = 627
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==ZmeiLangParser.EXCLUDE:
                            self.state = 626
                            self.match(ZmeiLangParser.EXCLUDE)


                        self.state = 629
                        self.field_list_expr_field() 
                    self.state = 634
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
        self.enterRule(localctx, 30, self.RULE_field_list_expr_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 638
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.STAR:
                self.state = 637
                self.match(ZmeiLangParser.STAR)


            self.state = 640
            self.id_or_kw()
            self.state = 642
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.STAR:
                self.state = 641
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
        self.enterRule(localctx, 32, self.RULE_write_mode_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 644
            self.match(ZmeiLangParser.SQ_BRACE_OPEN)
            self.state = 645
            self.match(ZmeiLangParser.WRITE_MODE)
            self.state = 646
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
        self.enterRule(localctx, 34, self.RULE_python_code)
        try:
            self.state = 650
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.CODE_BLOCK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 648
                self.code_block()
                pass
            elif token in [ZmeiLangParser.ASSIGN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 649
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
        self.enterRule(localctx, 36, self.RULE_code_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 652
            self.match(ZmeiLangParser.ASSIGN)
            self.state = 653
            self.match(ZmeiLangParser.PYTHON_CODE)
            self.state = 654
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
        self.enterRule(localctx, 38, self.RULE_code_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 656
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
        self.enterRule(localctx, 40, self.RULE_cs_annotation)
        try:
            self.state = 664
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.AN_SUIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 658
                self.an_suit()
                pass
            elif token in [ZmeiLangParser.AN_FILE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 659
                self.an_file()
                pass
            elif token in [ZmeiLangParser.AN_CHANNELS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 660
                self.an_channels()
                pass
            elif token in [ZmeiLangParser.AN_CELERY]:
                self.enterOuterAlt(localctx, 4)
                self.state = 661
                self.an_celery()
                pass
            elif token in [ZmeiLangParser.AN_LANGS]:
                self.enterOuterAlt(localctx, 5)
                self.state = 662
                self.an_langs()
                pass
            elif token in [ZmeiLangParser.NL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 663
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
        self.enterRule(localctx, 42, self.RULE_an_filer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 666
            self.match(ZmeiLangParser.AN_FILER)
            self.state = 669
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 667
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 668
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
        self.enterRule(localctx, 44, self.RULE_an_langs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 671
            self.match(ZmeiLangParser.AN_LANGS)
            self.state = 672
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 673
            self.an_langs_list()
            self.state = 674
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
        self.enterRule(localctx, 46, self.RULE_an_langs_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 676
            self.match(ZmeiLangParser.ID)
            self.state = 681
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 677
                self.match(ZmeiLangParser.COMA)
                self.state = 678
                self.match(ZmeiLangParser.ID)
                self.state = 683
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
        self.enterRule(localctx, 48, self.RULE_an_celery)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 684
            self.match(ZmeiLangParser.AN_CELERY)
            self.state = 687
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 685
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 686
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
            self.state = 689
            self.match(ZmeiLangParser.AN_CHANNELS)
            self.state = 692
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 690
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 691
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
        self.enterRule(localctx, 52, self.RULE_an_file)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 694
            self.match(ZmeiLangParser.AN_FILE)
            self.state = 695
            self.an_file_name()
            self.state = 696
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
        self.enterRule(localctx, 54, self.RULE_an_file_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 698
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
        self.enterRule(localctx, 56, self.RULE_an_suit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 700
            self.match(ZmeiLangParser.AN_SUIT)
            self.state = 705
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 701
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 702
                self.an_suit_app_name()
                self.state = 703
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
        self.enterRule(localctx, 58, self.RULE_an_suit_app_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 707
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
        self.enterRule(localctx, 60, self.RULE_col)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 709
            self.col_header()
            self.state = 711
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 710
                self.col_str_expr()


            self.state = 716
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 713
                    self.match(ZmeiLangParser.NL) 
                self.state = 718
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

            self.state = 722
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 38)) & ~0x3f) == 0 and ((1 << (_la - 38)) & ((1 << (ZmeiLangParser.WRITE_MODE - 38)) | (1 << (ZmeiLangParser.BOOL - 38)) | (1 << (ZmeiLangParser.KW_THEME - 38)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 38)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 38)) | (1 << (ZmeiLangParser.KW_PAGE - 38)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 38)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 38)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 38)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 38)) | (1 << (ZmeiLangParser.KW_BLOCK - 38)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 38)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 38)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 38)) | (1 << (ZmeiLangParser.KW_DELETE - 38)) | (1 << (ZmeiLangParser.KW_EDIT - 38)) | (1 << (ZmeiLangParser.KW_CREATE - 38)) | (1 << (ZmeiLangParser.KW_DETAIL - 38)) | (1 << (ZmeiLangParser.KW_SKIP - 38)) | (1 << (ZmeiLangParser.KW_FROM - 38)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 38)) | (1 << (ZmeiLangParser.KW_CSS - 38)) | (1 << (ZmeiLangParser.KW_JS - 38)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE - 38)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE - 38)) | (1 << (ZmeiLangParser.KW_INLINE - 38)) | (1 << (ZmeiLangParser.KW_TYPE - 38)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 38)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 38)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 38)) | (1 << (ZmeiLangParser.KW_QUERY - 38)) | (1 << (ZmeiLangParser.KW_AUTH - 38)) | (1 << (ZmeiLangParser.KW_COUNT - 38)) | (1 << (ZmeiLangParser.KW_I18N - 38)) | (1 << (ZmeiLangParser.KW_EXTRA - 38)) | (1 << (ZmeiLangParser.KW_TABS - 38)) | (1 << (ZmeiLangParser.KW_LIST - 38)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 38)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 38)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 38)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 38)) | (1 << (ZmeiLangParser.KW_FIELDS - 38)) | (1 << (ZmeiLangParser.KW_IMPORT - 38)) | (1 << (ZmeiLangParser.KW_AS - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 38)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 38)))) != 0) or ((((_la - 102)) & ~0x3f) == 0 and ((1 << (_la - 102)) & ((1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 102)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 102)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 102)) | (1 << (ZmeiLangParser.ID - 102)) | (1 << (ZmeiLangParser.EQUALS - 102)) | (1 << (ZmeiLangParser.DOLLAR - 102)) | (1 << (ZmeiLangParser.AMP - 102)) | (1 << (ZmeiLangParser.EXCLAM - 102)) | (1 << (ZmeiLangParser.STAR - 102)) | (1 << (ZmeiLangParser.APPROX - 102)))) != 0):
                self.state = 719
                self.col_field()
                self.state = 724
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 728
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 725
                    self.match(ZmeiLangParser.NL) 
                self.state = 730
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

            self.state = 734
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 731
                    self.model_annotation() 
                self.state = 736
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

            self.state = 740
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 737
                    self.match(ZmeiLangParser.NL) 
                self.state = 742
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

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
        self.enterRule(localctx, 62, self.RULE_col_str_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 743
            self.match(ZmeiLangParser.EQUALS)
            self.state = 744
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.STRING_DQ or _la==ZmeiLangParser.STRING_SQ):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 751
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.NL]:
                self.state = 746 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 745
                        self.match(ZmeiLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 748 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

                pass
            elif token in [ZmeiLangParser.EOF]:
                self.state = 750
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
        self.enterRule(localctx, 64, self.RULE_col_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 753
            self.match(ZmeiLangParser.HASH)
            self.state = 755
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 754
                self.col_base_name()


            self.state = 757
            self.col_name()
            self.state = 759
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COLON:
                self.state = 758
                self.col_verbose_name()


            self.state = 761
            self.col_header_line_separator()
            self.state = 762
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
        self.enterRule(localctx, 66, self.RULE_col_header_line_separator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 764
            self.match(ZmeiLangParser.NL)
            self.state = 765
            self.match(ZmeiLangParser.DASH)
            self.state = 766
            self.match(ZmeiLangParser.DASH)
            self.state = 768 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 767
                self.match(ZmeiLangParser.DASH)
                self.state = 770 
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
        self.enterRule(localctx, 68, self.RULE_col_verbose_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 772
            self.match(ZmeiLangParser.COLON)
            self.state = 773
            self.verbose_name_part()
            self.state = 776
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.SLASH:
                self.state = 774
                self.match(ZmeiLangParser.SLASH)
                self.state = 775
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
        self.enterRule(localctx, 70, self.RULE_verbose_name_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 781
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                self.state = 778
                self.id_or_kw()
                pass
            elif token in [ZmeiLangParser.STRING_DQ]:
                self.state = 779
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.state = 780
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
        self.enterRule(localctx, 72, self.RULE_col_base_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 783
            self.id_or_kw()
            self.state = 788
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.DASH]:
                self.state = 784
                self.match(ZmeiLangParser.DASH)
                self.state = 785
                self.match(ZmeiLangParser.GT)
                pass
            elif token in [ZmeiLangParser.APPROX]:
                self.state = 786
                self.match(ZmeiLangParser.APPROX)
                self.state = 787
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
        self.enterRule(localctx, 74, self.RULE_col_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 790
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
        self.enterRule(localctx, 76, self.RULE_col_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 795
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 124)) & ~0x3f) == 0 and ((1 << (_la - 124)) & ((1 << (ZmeiLangParser.EQUALS - 124)) | (1 << (ZmeiLangParser.DOLLAR - 124)) | (1 << (ZmeiLangParser.AMP - 124)) | (1 << (ZmeiLangParser.EXCLAM - 124)) | (1 << (ZmeiLangParser.STAR - 124)) | (1 << (ZmeiLangParser.APPROX - 124)))) != 0):
                self.state = 792
                self.col_modifier()
                self.state = 797
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 798
            self.col_field_name()
            self.state = 800
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 111)) & ~0x3f) == 0 and ((1 << (_la - 111)) & ((1 << (ZmeiLangParser.COLON - 111)) | (1 << (ZmeiLangParser.ASSIGN - 111)) | (1 << (ZmeiLangParser.ASSIGN_STATIC - 111)))) != 0):
                self.state = 799
                self.col_field_expr_or_def()


            self.state = 803
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.SLASH:
                self.state = 802
                self.col_field_verbose_name()


            self.state = 806
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.QUESTION_MARK:
                self.state = 805
                self.col_field_help_text()


            self.state = 814
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.NL]:
                self.state = 809 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 808
                        self.match(ZmeiLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 811 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

                pass
            elif token in [ZmeiLangParser.EOF]:
                self.state = 813
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
        self.enterRule(localctx, 78, self.RULE_col_field_expr_or_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 828
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                self.state = 816
                self.match(ZmeiLangParser.COLON)
                self.state = 818
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.CODE_BLOCK:
                    self.state = 817
                    self.col_field_custom()


                pass

            elif la_ == 2:
                self.state = 820
                self.match(ZmeiLangParser.COLON)
                self.state = 821
                self.col_field_def()
                self.state = 823
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.DOT or _la==ZmeiLangParser.CODE_BLOCK:
                    self.state = 822
                    self.col_field_extend()


                pass

            elif la_ == 3:
                self.state = 825
                self.match(ZmeiLangParser.COLON)
                self.state = 826
                self.wrong_field_type()
                pass

            elif la_ == 4:
                self.state = 827
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
        self.enterRule(localctx, 80, self.RULE_col_field_custom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 830
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
        self.enterRule(localctx, 82, self.RULE_col_field_extend)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 833
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 832
                self.col_field_extend_append()


            self.state = 835
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
        self.enterRule(localctx, 84, self.RULE_col_field_extend_append)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 837
            self.match(ZmeiLangParser.DOT)
            self.state = 838
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
        self.enterRule(localctx, 86, self.RULE_wrong_field_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 840
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
        self.enterRule(localctx, 88, self.RULE_col_field_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 842
            self.col_field_expr_marker()
            self.state = 843
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
        self.enterRule(localctx, 90, self.RULE_col_field_expr_marker)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 845
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
        self.enterRule(localctx, 92, self.RULE_col_feild_expr_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 847
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
        self.enterRule(localctx, 94, self.RULE_string_or_quoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 856
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                self.state = 850 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 849
                    self.id_or_kw()
                    self.state = 852 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.WRITE_MODE) | (1 << ZmeiLangParser.BOOL) | (1 << ZmeiLangParser.KW_THEME) | (1 << ZmeiLangParser.KW_FILTER_OUT) | (1 << ZmeiLangParser.KW_FILTER_IN) | (1 << ZmeiLangParser.KW_PAGE) | (1 << ZmeiLangParser.KW_LINK_SUFFIX) | (1 << ZmeiLangParser.KW_URL_PREFIX) | (1 << ZmeiLangParser.KW_CAN_EDIT) | (1 << ZmeiLangParser.KW_OBJECT_EXPR) | (1 << ZmeiLangParser.KW_BLOCK) | (1 << ZmeiLangParser.KW_ITEM_NAME) | (1 << ZmeiLangParser.KW_PK_PARAM) | (1 << ZmeiLangParser.KW_LIST_FIELDS) | (1 << ZmeiLangParser.KW_DELETE) | (1 << ZmeiLangParser.KW_EDIT) | (1 << ZmeiLangParser.KW_CREATE) | (1 << ZmeiLangParser.KW_DETAIL) | (1 << ZmeiLangParser.KW_SKIP) | (1 << ZmeiLangParser.KW_FROM) | (1 << ZmeiLangParser.KW_POLY_LIST) | (1 << ZmeiLangParser.KW_CSS) | (1 << ZmeiLangParser.KW_JS) | (1 << ZmeiLangParser.KW_INLINE_TYPE) | (1 << ZmeiLangParser.KW_AUTH_TYPE) | (1 << ZmeiLangParser.KW_INLINE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ZmeiLangParser.KW_TYPE - 64)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 64)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 64)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 64)) | (1 << (ZmeiLangParser.KW_QUERY - 64)) | (1 << (ZmeiLangParser.KW_AUTH - 64)) | (1 << (ZmeiLangParser.KW_COUNT - 64)) | (1 << (ZmeiLangParser.KW_I18N - 64)) | (1 << (ZmeiLangParser.KW_EXTRA - 64)) | (1 << (ZmeiLangParser.KW_TABS - 64)) | (1 << (ZmeiLangParser.KW_LIST - 64)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 64)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 64)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 64)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 64)) | (1 << (ZmeiLangParser.KW_FIELDS - 64)) | (1 << (ZmeiLangParser.KW_IMPORT - 64)) | (1 << (ZmeiLangParser.KW_AS - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 64)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 64)) | (1 << (ZmeiLangParser.ID - 64)))) != 0)):
                        break

                pass
            elif token in [ZmeiLangParser.STRING_DQ]:
                self.state = 854
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.state = 855
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
        self.enterRule(localctx, 96, self.RULE_col_field_help_text)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 858
            self.match(ZmeiLangParser.QUESTION_MARK)
            self.state = 859
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
        self.enterRule(localctx, 98, self.RULE_col_field_verbose_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 861
            self.match(ZmeiLangParser.SLASH)
            self.state = 862
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
        self.enterRule(localctx, 100, self.RULE_col_field_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 864
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
        self.enterRule(localctx, 102, self.RULE_col_modifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 866
            _la = self._input.LA(1)
            if not(((((_la - 124)) & ~0x3f) == 0 and ((1 << (_la - 124)) & ((1 << (ZmeiLangParser.EQUALS - 124)) | (1 << (ZmeiLangParser.DOLLAR - 124)) | (1 << (ZmeiLangParser.AMP - 124)) | (1 << (ZmeiLangParser.EXCLAM - 124)) | (1 << (ZmeiLangParser.STAR - 124)) | (1 << (ZmeiLangParser.APPROX - 124)))) != 0)):
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
        self.enterRule(localctx, 104, self.RULE_col_field_def)
        try:
            self.state = 886
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 868
                self.field_longtext()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 869
                self.field_html_media()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_HTML]:
                self.enterOuterAlt(localctx, 3)
                self.state = 870
                self.field_html()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_FLOAT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 871
                self.field_float()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_DECIMAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 872
                self.field_decimal()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_DATE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 873
                self.field_date()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_DATETIME]:
                self.enterOuterAlt(localctx, 7)
                self.state = 874
                self.field_datetime()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME]:
                self.enterOuterAlt(localctx, 8)
                self.state = 875
                self.field_create_time()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME]:
                self.enterOuterAlt(localctx, 9)
                self.state = 876
                self.field_update_time()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_TEXT]:
                self.enterOuterAlt(localctx, 10)
                self.state = 877
                self.field_text()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_INT]:
                self.enterOuterAlt(localctx, 11)
                self.state = 878
                self.field_int()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_SLUG]:
                self.enterOuterAlt(localctx, 12)
                self.state = 879
                self.field_slug()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_BOOL]:
                self.enterOuterAlt(localctx, 13)
                self.state = 880
                self.field_bool()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY]:
                self.enterOuterAlt(localctx, 14)
                self.state = 881
                self.field_relation()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER]:
                self.enterOuterAlt(localctx, 15)
                self.state = 882
                self.field_image()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_FILE]:
                self.enterOuterAlt(localctx, 16)
                self.state = 883
                self.field_file()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE]:
                self.enterOuterAlt(localctx, 17)
                self.state = 884
                self.field_filer_file()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER]:
                self.enterOuterAlt(localctx, 18)
                self.state = 885
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
        self.enterRule(localctx, 106, self.RULE_field_longtext)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 888
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
        self.enterRule(localctx, 108, self.RULE_field_html)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 890
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
        self.enterRule(localctx, 110, self.RULE_field_html_media)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 892
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
        self.enterRule(localctx, 112, self.RULE_field_float)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 894
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
        self.enterRule(localctx, 114, self.RULE_field_decimal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 896
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
        self.enterRule(localctx, 116, self.RULE_field_date)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 898
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
        self.enterRule(localctx, 118, self.RULE_field_datetime)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 900
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
        self.enterRule(localctx, 120, self.RULE_field_create_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 902
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
        self.enterRule(localctx, 122, self.RULE_field_update_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 904
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
        self.enterRule(localctx, 124, self.RULE_field_file)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 906
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
        self.enterRule(localctx, 126, self.RULE_field_filer_file)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 908
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
        self.enterRule(localctx, 128, self.RULE_field_filer_folder)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 910
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
        self.enterRule(localctx, 130, self.RULE_field_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 912
            self.match(ZmeiLangParser.COL_FIELD_TYPE_TEXT)
            self.state = 921
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 913
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 914
                self.field_text_size()
                self.state = 917
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.COMA:
                    self.state = 915
                    self.match(ZmeiLangParser.COMA)
                    self.state = 916
                    self.field_text_choices()


                self.state = 919
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
        self.enterRule(localctx, 132, self.RULE_field_text_size)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 923
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
        self.enterRule(localctx, 134, self.RULE_field_text_choices)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 925
            self.match(ZmeiLangParser.COL_FIELD_CHOICES)
            self.state = 926
            self.match(ZmeiLangParser.EQUALS)
            self.state = 927
            self.field_text_choice()
            self.state = 932
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 928
                self.match(ZmeiLangParser.COMA)
                self.state = 929
                self.field_text_choice()
                self.state = 934
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
        self.enterRule(localctx, 136, self.RULE_field_text_choice)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 936
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.state = 935
                self.field_text_choice_key()


            self.state = 938
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
        self.enterRule(localctx, 138, self.RULE_field_text_choice_val)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 943
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                self.state = 940
                self.id_or_kw()
                pass
            elif token in [ZmeiLangParser.STRING_DQ]:
                self.state = 941
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.state = 942
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
        self.enterRule(localctx, 140, self.RULE_field_text_choice_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 945
            self.id_or_kw()
            self.state = 946
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
        self.enterRule(localctx, 142, self.RULE_field_int)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 948
            self.match(ZmeiLangParser.COL_FIELD_TYPE_INT)
            self.state = 953
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 949
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 950
                self.field_int_choices()
                self.state = 951
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
        self.enterRule(localctx, 144, self.RULE_field_int_choices)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 955
            self.match(ZmeiLangParser.COL_FIELD_CHOICES)
            self.state = 956
            self.match(ZmeiLangParser.EQUALS)
            self.state = 957
            self.field_int_choice()
            self.state = 962
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 958
                self.match(ZmeiLangParser.COMA)
                self.state = 959
                self.field_int_choice()
                self.state = 964
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
        self.enterRule(localctx, 146, self.RULE_field_int_choice)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 966
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DIGIT:
                self.state = 965
                self.field_int_choice_key()


            self.state = 968
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
        self.enterRule(localctx, 148, self.RULE_field_int_choice_val)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 973
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                self.state = 970
                self.id_or_kw()
                pass
            elif token in [ZmeiLangParser.STRING_DQ]:
                self.state = 971
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.state = 972
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
        self.enterRule(localctx, 150, self.RULE_field_int_choice_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 975
            self.match(ZmeiLangParser.DIGIT)
            self.state = 976
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
        self.enterRule(localctx, 152, self.RULE_field_slug)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 978
            self.match(ZmeiLangParser.COL_FIELD_TYPE_SLUG)
            self.state = 979
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 980
            self.field_slug_ref_field()
            self.state = 981
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
        self.enterRule(localctx, 154, self.RULE_field_slug_ref_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 983
            self.field_slug_ref_field_id()
            self.state = 988
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 984
                self.match(ZmeiLangParser.COMA)
                self.state = 985
                self.field_slug_ref_field_id()
                self.state = 990
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
        self.enterRule(localctx, 156, self.RULE_field_slug_ref_field_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 991
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
        self.enterRule(localctx, 158, self.RULE_field_bool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 993
            self.match(ZmeiLangParser.COL_FIELD_TYPE_BOOL)
            self.state = 998
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 994
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 995
                self.field_bool_default()
                self.state = 996
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
        self.enterRule(localctx, 160, self.RULE_field_bool_default)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1000
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
        self.enterRule(localctx, 162, self.RULE_field_image)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1002
            self.filer_image_type()
            self.state = 1007
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1003
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1004
                self.field_image_sizes()
                self.state = 1005
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
        self.enterRule(localctx, 164, self.RULE_filer_image_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1009
            _la = self._input.LA(1)
            if not(((((_la - 91)) & ~0x3f) == 0 and ((1 << (_la - 91)) & ((1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 91)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 91)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 91)))) != 0)):
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
        self.enterRule(localctx, 166, self.RULE_field_image_sizes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1011
            self.field_image_size()
            self.state = 1016
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 1012
                self.match(ZmeiLangParser.COMA)
                self.state = 1013
                self.field_image_size()
                self.state = 1018
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
        self.enterRule(localctx, 168, self.RULE_field_image_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1019
            self.field_image_size_name()
            self.state = 1020
            self.field_image_size_dimensions()
            self.state = 1021
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
        self.enterRule(localctx, 170, self.RULE_field_image_size_dimensions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1023
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
        self.enterRule(localctx, 172, self.RULE_field_image_size_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1025
            self.id_or_kw()
            self.state = 1026
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
        self.enterRule(localctx, 174, self.RULE_field_image_filters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1031
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.PIPE:
                self.state = 1028
                self.field_image_filter()
                self.state = 1033
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
        self.enterRule(localctx, 176, self.RULE_field_image_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1034
            self.match(ZmeiLangParser.PIPE)
            self.state = 1035
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
        self.enterRule(localctx, 178, self.RULE_field_relation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1037
            self.field_relation_type()
            self.state = 1038
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1041
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.HASH]:
                self.state = 1039
                self.field_relation_target_ref()
                pass
            elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                self.state = 1040
                self.field_relation_target_class()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 1044
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DASH:
                self.state = 1043
                self.field_relation_related_name()


            self.state = 1046
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
        self.enterRule(localctx, 180, self.RULE_field_relation_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1048
            _la = self._input.LA(1)
            if not(((((_la - 101)) & ~0x3f) == 0 and ((1 << (_la - 101)) & ((1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 101)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 101)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 101)))) != 0)):
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

        def HASH(self):
            return self.getToken(ZmeiLangParser.HASH, 0)

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


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
        self.enterRule(localctx, 182, self.RULE_field_relation_target_ref)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1050
            self.match(ZmeiLangParser.HASH)
            self.state = 1051
            self.id_or_kw()
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
        self.enterRule(localctx, 184, self.RULE_field_relation_target_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1053
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
        self.enterRule(localctx, 186, self.RULE_field_relation_related_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1055
            self.match(ZmeiLangParser.DASH)
            self.state = 1056
            self.match(ZmeiLangParser.GT)
            self.state = 1057
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
        self.enterRule(localctx, 188, self.RULE_model_annotation)
        try:
            self.state = 1074
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.AN_ADMIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1059
                self.an_admin()
                pass
            elif token in [ZmeiLangParser.AN_TREE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1060
                self.an_tree()
                pass
            elif token in [ZmeiLangParser.AN_DATE_TREE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1061
                self.an_date_tree()
                pass
            elif token in [ZmeiLangParser.AN_MIXIN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1062
                self.an_mixin()
                pass
            elif token in [ZmeiLangParser.AN_M2M_CHANGED]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1063
                self.an_m2m_changed()
                pass
            elif token in [ZmeiLangParser.AN_POST_DELETE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 1064
                self.an_post_delete()
                pass
            elif token in [ZmeiLangParser.AN_PRE_DELETE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 1065
                self.an_pre_delete()
                pass
            elif token in [ZmeiLangParser.AN_POST_SAVE]:
                self.enterOuterAlt(localctx, 8)
                self.state = 1066
                self.an_post_save()
                pass
            elif token in [ZmeiLangParser.AN_PRE_SAVE]:
                self.enterOuterAlt(localctx, 9)
                self.state = 1067
                self.an_pre_save()
                pass
            elif token in [ZmeiLangParser.AN_CLEAN]:
                self.enterOuterAlt(localctx, 10)
                self.state = 1068
                self.an_clean()
                pass
            elif token in [ZmeiLangParser.AN_API]:
                self.enterOuterAlt(localctx, 11)
                self.state = 1069
                self.an_api()
                pass
            elif token in [ZmeiLangParser.AN_REST]:
                self.enterOuterAlt(localctx, 12)
                self.state = 1070
                self.an_rest()
                pass
            elif token in [ZmeiLangParser.AN_ORDER]:
                self.enterOuterAlt(localctx, 13)
                self.state = 1071
                self.an_order()
                pass
            elif token in [ZmeiLangParser.AN_SORTABLE]:
                self.enterOuterAlt(localctx, 14)
                self.state = 1072
                self.an_sortable()
                pass
            elif token in [ZmeiLangParser.NL]:
                self.enterOuterAlt(localctx, 15)
                self.state = 1073
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
        self.enterRule(localctx, 190, self.RULE_an_sortable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1076
            self.match(ZmeiLangParser.AN_SORTABLE)
            self.state = 1077
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1078
            self.an_sortable_field_name()
            self.state = 1079
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
        self.enterRule(localctx, 192, self.RULE_an_sortable_field_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1081
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
        self.enterRule(localctx, 194, self.RULE_an_order)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1083
            self.match(ZmeiLangParser.AN_ORDER)
            self.state = 1084
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1085
            self.an_order_fields()
            self.state = 1086
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
        self.enterRule(localctx, 196, self.RULE_an_order_fields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1088
            self.id_or_kw()
            self.state = 1093
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 1089
                self.match(ZmeiLangParser.COMA)
                self.state = 1090
                self.id_or_kw()
                self.state = 1095
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
        self.enterRule(localctx, 198, self.RULE_an_rest)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1096
            self.match(ZmeiLangParser.AN_REST)
            self.state = 1099
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 1097
                self.match(ZmeiLangParser.DOT)
                self.state = 1098
                self.an_rest_descriptor()


            self.state = 1105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1101
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1102
                self.an_rest_config()
                self.state = 1103
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
        self.enterRule(localctx, 200, self.RULE_an_rest_config)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1107
            self.an_rest_main_part()
            self.state = 1113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 63)) & ~0x3f) == 0 and ((1 << (_la - 63)) & ((1 << (ZmeiLangParser.KW_INLINE - 63)) | (1 << (ZmeiLangParser.NL - 63)) | (1 << (ZmeiLangParser.COMA - 63)))) != 0):
                self.state = 1111
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.KW_INLINE]:
                    self.state = 1108
                    self.an_rest_inline()
                    pass
                elif token in [ZmeiLangParser.NL]:
                    self.state = 1109
                    self.match(ZmeiLangParser.NL)
                    pass
                elif token in [ZmeiLangParser.COMA]:
                    self.state = 1110
                    self.match(ZmeiLangParser.COMA)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1115
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
        self.enterRule(localctx, 202, self.RULE_an_rest_main_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1130
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,84,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1128
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [ZmeiLangParser.KW_FIELDS]:
                        self.state = 1116
                        self.an_rest_fields()
                        pass
                    elif token in [ZmeiLangParser.KW_I18N]:
                        self.state = 1117
                        self.an_rest_i18n()
                        pass
                    elif token in [ZmeiLangParser.KW_AUTH]:
                        self.state = 1118
                        self.an_rest_auth()
                        pass
                    elif token in [ZmeiLangParser.KW_QUERY]:
                        self.state = 1119
                        self.an_rest_query()
                        pass
                    elif token in [ZmeiLangParser.KW_ON_CREATE]:
                        self.state = 1120
                        self.an_rest_on_create()
                        pass
                    elif token in [ZmeiLangParser.KW_FILTER_IN]:
                        self.state = 1121
                        self.an_rest_filter_in()
                        pass
                    elif token in [ZmeiLangParser.KW_FILTER_OUT]:
                        self.state = 1122
                        self.an_rest_filter_out()
                        pass
                    elif token in [ZmeiLangParser.KW_READ_ONLY]:
                        self.state = 1123
                        self.an_rest_read_only()
                        pass
                    elif token in [ZmeiLangParser.KW_USER_FIELD]:
                        self.state = 1124
                        self.an_rest_user_field()
                        pass
                    elif token in [ZmeiLangParser.KW_ANNOTATE]:
                        self.state = 1125
                        self.an_rest_annotate()
                        pass
                    elif token in [ZmeiLangParser.NL]:
                        self.state = 1126
                        self.match(ZmeiLangParser.NL)
                        pass
                    elif token in [ZmeiLangParser.COMA]:
                        self.state = 1127
                        self.match(ZmeiLangParser.COMA)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 1132
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,84,self._ctx)

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
        self.enterRule(localctx, 204, self.RULE_an_rest_descriptor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1133
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
        self.enterRule(localctx, 206, self.RULE_an_rest_i18n)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1135
            self.match(ZmeiLangParser.KW_I18N)
            self.state = 1136
            self.match(ZmeiLangParser.COLON)
            self.state = 1137
            self.match(ZmeiLangParser.BOOL)
            self.state = 1141
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,85,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1138
                    self.match(ZmeiLangParser.NL) 
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
        self.enterRule(localctx, 208, self.RULE_an_rest_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1144
            self.match(ZmeiLangParser.KW_QUERY)
            self.state = 1145
            self.python_code()
            self.state = 1149
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,86,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1146
                    self.match(ZmeiLangParser.NL) 
                self.state = 1151
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,86,self._ctx)

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
        self.enterRule(localctx, 210, self.RULE_an_rest_on_create)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1152
            self.match(ZmeiLangParser.KW_ON_CREATE)
            self.state = 1154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COLON:
                self.state = 1153
                self.match(ZmeiLangParser.COLON)


            self.state = 1156
            self.python_code()
            self.state = 1160
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,88,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1157
                    self.match(ZmeiLangParser.NL) 
                self.state = 1162
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,88,self._ctx)

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
        self.enterRule(localctx, 212, self.RULE_an_rest_filter_in)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1163
            self.match(ZmeiLangParser.KW_FILTER_IN)
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
            _alt = self._interp.adaptivePredict(self._input,90,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1168
                    self.match(ZmeiLangParser.NL) 
                self.state = 1173
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,90,self._ctx)

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
        self.enterRule(localctx, 214, self.RULE_an_rest_filter_out)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1174
            self.match(ZmeiLangParser.KW_FILTER_OUT)
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
            _alt = self._interp.adaptivePredict(self._input,92,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1179
                    self.match(ZmeiLangParser.NL) 
                self.state = 1184
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,92,self._ctx)

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
        self.enterRule(localctx, 216, self.RULE_an_rest_read_only)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1185
            self.match(ZmeiLangParser.KW_READ_ONLY)
            self.state = 1186
            self.match(ZmeiLangParser.COLON)
            self.state = 1187
            self.field_list_expr()
            self.state = 1191
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,93,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1188
                    self.match(ZmeiLangParser.NL) 
                self.state = 1193
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,93,self._ctx)

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
        self.enterRule(localctx, 218, self.RULE_an_rest_user_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1194
            self.match(ZmeiLangParser.KW_USER_FIELD)
            self.state = 1195
            self.match(ZmeiLangParser.COLON)
            self.state = 1196
            self.id_or_kw()
            self.state = 1200
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,94,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1197
                    self.match(ZmeiLangParser.NL) 
                self.state = 1202
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,94,self._ctx)

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
        self.enterRule(localctx, 220, self.RULE_an_rest_fields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1203
            self.match(ZmeiLangParser.KW_FIELDS)
            self.state = 1204
            self.match(ZmeiLangParser.COLON)
            self.state = 1205
            self.field_list_expr()
            self.state = 1207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.SQ_BRACE_OPEN:
                self.state = 1206
                self.an_rest_fields_write_mode()


            self.state = 1212
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,96,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1209
                    self.match(ZmeiLangParser.NL) 
                self.state = 1214
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,96,self._ctx)

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
        self.enterRule(localctx, 222, self.RULE_an_rest_fields_write_mode)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1215
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
        self.enterRule(localctx, 224, self.RULE_an_rest_auth)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1217
            self.match(ZmeiLangParser.KW_AUTH)
            self.state = 1218
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1219
            self.an_rest_auth_type()
            self.state = 1224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 1220
                self.match(ZmeiLangParser.COMA)
                self.state = 1221
                self.an_rest_auth_type()
                self.state = 1226
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1227
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
        self.enterRule(localctx, 226, self.RULE_an_rest_auth_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1229
            self.match(ZmeiLangParser.KW_AUTH_TYPE)
            self.state = 1233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.COLON]:
                self.state = 1230
                self.match(ZmeiLangParser.COLON)
                self.state = 1231
                self.an_rest_auth_token_model()
                pass
            elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                self.state = 1232
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

        def HASH(self):
            return self.getToken(ZmeiLangParser.HASH, 0)

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


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
        self.enterRule(localctx, 228, self.RULE_an_rest_auth_token_model)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1235
            self.match(ZmeiLangParser.HASH)
            self.state = 1236
            self.id_or_kw()
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
        self.enterRule(localctx, 230, self.RULE_an_rest_auth_token_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1238
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
        self.enterRule(localctx, 232, self.RULE_an_rest_annotate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1240
            self.match(ZmeiLangParser.KW_ANNOTATE)
            self.state = 1241
            self.match(ZmeiLangParser.COLON)
            self.state = 1242
            self.an_rest_annotate_count()
            self.state = 1246
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,99,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1243
                    self.match(ZmeiLangParser.NL) 
                self.state = 1248
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,99,self._ctx)

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
        self.enterRule(localctx, 234, self.RULE_an_rest_annotate_count)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1249
            self.match(ZmeiLangParser.KW_COUNT)
            self.state = 1250
            self.an_rest_annotate_count_field()
            self.state = 1253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.KW_AS:
                self.state = 1251
                self.match(ZmeiLangParser.KW_AS)
                self.state = 1252
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
        self.enterRule(localctx, 236, self.RULE_an_rest_annotate_count_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1255
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
        self.enterRule(localctx, 238, self.RULE_an_rest_annotate_count_alias)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1257
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
        self.enterRule(localctx, 240, self.RULE_an_rest_inline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1259
            self.match(ZmeiLangParser.KW_INLINE)
            self.state = 1260
            self.match(ZmeiLangParser.COLON)
            self.state = 1264 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 1264
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                        self.state = 1261
                        self.an_rest_inline_decl()
                        pass
                    elif token in [ZmeiLangParser.COMA]:
                        self.state = 1262
                        self.match(ZmeiLangParser.COMA)
                        pass
                    elif token in [ZmeiLangParser.NL]:
                        self.state = 1263
                        self.match(ZmeiLangParser.NL)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 1266 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,102,self._ctx)

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
        self.enterRule(localctx, 242, self.RULE_an_rest_inline_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1268
            self.an_rest_inline_name()
            self.state = 1269
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1270
            self.an_rest_config()
            self.state = 1271
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
        self.enterRule(localctx, 244, self.RULE_an_rest_inline_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1273
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
        self.enterRule(localctx, 246, self.RULE_an_api)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1275
            self.match(ZmeiLangParser.AN_API)
            self.state = 1290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1276
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1286
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.STAR]:
                    self.state = 1277
                    self.an_api_all()
                    pass
                elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                    self.state = 1278
                    self.an_api_name()
                    self.state = 1283
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==ZmeiLangParser.COMA:
                        self.state = 1279
                        self.match(ZmeiLangParser.COMA)
                        self.state = 1280
                        self.an_api_name()
                        self.state = 1285
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1288
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
        self.enterRule(localctx, 248, self.RULE_an_api_all)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1292
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
        self.enterRule(localctx, 250, self.RULE_an_api_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1294
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
        self.enterRule(localctx, 252, self.RULE_an_clean)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1296
            self.match(ZmeiLangParser.AN_CLEAN)
            self.state = 1297
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
        self.enterRule(localctx, 254, self.RULE_an_pre_save)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1299
            self.match(ZmeiLangParser.AN_PRE_SAVE)
            self.state = 1300
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
        self.enterRule(localctx, 256, self.RULE_an_post_save)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1302
            self.match(ZmeiLangParser.AN_POST_SAVE)
            self.state = 1303
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
        self.enterRule(localctx, 258, self.RULE_an_pre_delete)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1305
            self.match(ZmeiLangParser.AN_PRE_DELETE)
            self.state = 1306
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
        self.enterRule(localctx, 260, self.RULE_an_post_delete)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1308
            self.match(ZmeiLangParser.AN_POST_DELETE)
            self.state = 1309
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
        self.enterRule(localctx, 262, self.RULE_an_m2m_changed)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1311
            self.match(ZmeiLangParser.AN_M2M_CHANGED)
            self.state = 1312
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
        self.enterRule(localctx, 264, self.RULE_an_mixin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1314
            self.match(ZmeiLangParser.AN_MIXIN)

            self.state = 1315
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1316
            self.classname()
            self.state = 1317
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
        self.enterRule(localctx, 266, self.RULE_an_date_tree)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1319
            self.match(ZmeiLangParser.AN_DATE_TREE)

            self.state = 1320
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1321
            self.an_date_tree_field()
            self.state = 1322
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
        self.enterRule(localctx, 268, self.RULE_an_date_tree_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1324
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
        self.enterRule(localctx, 270, self.RULE_an_tree)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1326
            self.match(ZmeiLangParser.AN_TREE)
            self.state = 1331
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1327
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1328
                self.an_tree_poly()
                self.state = 1329
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
        self.enterRule(localctx, 272, self.RULE_an_tree_poly)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1333
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
        self.enterRule(localctx, 274, self.RULE_an_admin)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1335
            self.match(ZmeiLangParser.AN_ADMIN)
            self.state = 1361
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1336
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1351
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,108,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 1349
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [ZmeiLangParser.KW_LIST]:
                            self.state = 1337
                            self.an_admin_list()
                            pass
                        elif token in [ZmeiLangParser.KW_READ_ONLY]:
                            self.state = 1338
                            self.an_admin_read_only()
                            pass
                        elif token in [ZmeiLangParser.KW_LIST_EDITABLE]:
                            self.state = 1339
                            self.an_admin_list_editable()
                            pass
                        elif token in [ZmeiLangParser.KW_LIST_FILTER]:
                            self.state = 1340
                            self.an_admin_list_filter()
                            pass
                        elif token in [ZmeiLangParser.KW_LIST_SEARCH]:
                            self.state = 1341
                            self.an_admin_list_search()
                            pass
                        elif token in [ZmeiLangParser.KW_FIELDS]:
                            self.state = 1342
                            self.an_admin_fields()
                            pass
                        elif token in [ZmeiLangParser.KW_TABS]:
                            self.state = 1343
                            self.an_admin_tabs()
                            pass
                        elif token in [ZmeiLangParser.KW_INLINE]:
                            self.state = 1344
                            self.an_admin_inlines()
                            pass
                        elif token in [ZmeiLangParser.KW_CSS]:
                            self.state = 1345
                            self.an_admin_css()
                            pass
                        elif token in [ZmeiLangParser.KW_JS]:
                            self.state = 1346
                            self.an_admin_js()
                            pass
                        elif token in [ZmeiLangParser.NL]:
                            self.state = 1347
                            self.match(ZmeiLangParser.NL)
                            pass
                        elif token in [ZmeiLangParser.COMA]:
                            self.state = 1348
                            self.match(ZmeiLangParser.COMA)
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 1353
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,108,self._ctx)

                self.state = 1357
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZmeiLangParser.NL:
                    self.state = 1354
                    self.match(ZmeiLangParser.NL)
                    self.state = 1359
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 1360
                self.match(ZmeiLangParser.BRACE_CLOSE)


            self.state = 1366
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,111,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1363
                    self.match(ZmeiLangParser.NL) 
                self.state = 1368
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,111,self._ctx)

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
        self.enterRule(localctx, 276, self.RULE_an_admin_js)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1369
            self.match(ZmeiLangParser.KW_JS)
            self.state = 1370
            self.match(ZmeiLangParser.COLON)
            self.state = 1374
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 1371
                self.match(ZmeiLangParser.NL)
                self.state = 1376
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1377
            self.an_admin_js_file_name()
            self.state = 1388
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,114,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1378
                    self.match(ZmeiLangParser.COMA)
                    self.state = 1382
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==ZmeiLangParser.NL:
                        self.state = 1379
                        self.match(ZmeiLangParser.NL)
                        self.state = 1384
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 1385
                    self.an_admin_js_file_name() 
                self.state = 1390
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,114,self._ctx)

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
        self.enterRule(localctx, 278, self.RULE_an_admin_css)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1391
            self.match(ZmeiLangParser.KW_CSS)
            self.state = 1392
            self.match(ZmeiLangParser.COLON)
            self.state = 1393
            self.an_admin_css_file_name()
            self.state = 1398
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,115,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1394
                    self.match(ZmeiLangParser.COMA)
                    self.state = 1395
                    self.an_admin_css_file_name() 
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
        self.enterRule(localctx, 280, self.RULE_an_admin_css_file_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1401
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
        self.enterRule(localctx, 282, self.RULE_an_admin_js_file_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1403
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
        self.enterRule(localctx, 284, self.RULE_an_admin_inlines)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1405
            self.match(ZmeiLangParser.KW_INLINE)
            self.state = 1406
            self.match(ZmeiLangParser.COLON)
            self.state = 1407
            self.an_admin_inline()
            self.state = 1412
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,116,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1408
                    self.match(ZmeiLangParser.COMA)
                    self.state = 1409
                    self.an_admin_inline() 
                self.state = 1414
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,116,self._ctx)

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
        self.enterRule(localctx, 286, self.RULE_an_admin_inline)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1415
            self.inline_name()
            self.state = 1428
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1416
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1424
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ZmeiLangParser.KW_TYPE - 64)) | (1 << (ZmeiLangParser.KW_EXTRA - 64)) | (1 << (ZmeiLangParser.KW_FIELDS - 64)) | (1 << (ZmeiLangParser.NL - 64)) | (1 << (ZmeiLangParser.COMA - 64)))) != 0):
                    self.state = 1422
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [ZmeiLangParser.KW_TYPE]:
                        self.state = 1417
                        self.inline_type()
                        pass
                    elif token in [ZmeiLangParser.KW_EXTRA]:
                        self.state = 1418
                        self.inline_extra()
                        pass
                    elif token in [ZmeiLangParser.KW_FIELDS]:
                        self.state = 1419
                        self.inline_fields()
                        pass
                    elif token in [ZmeiLangParser.NL]:
                        self.state = 1420
                        self.match(ZmeiLangParser.NL)
                        pass
                    elif token in [ZmeiLangParser.COMA]:
                        self.state = 1421
                        self.match(ZmeiLangParser.COMA)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 1426
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 1427
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
        self.enterRule(localctx, 288, self.RULE_inline_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1430
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
        self.enterRule(localctx, 290, self.RULE_inline_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1432
            self.match(ZmeiLangParser.KW_TYPE)
            self.state = 1433
            self.match(ZmeiLangParser.COLON)
            self.state = 1434
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
        self.enterRule(localctx, 292, self.RULE_inline_extra)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1436
            self.match(ZmeiLangParser.KW_EXTRA)
            self.state = 1437
            self.match(ZmeiLangParser.COLON)
            self.state = 1438
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
        self.enterRule(localctx, 294, self.RULE_inline_fields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1440
            self.match(ZmeiLangParser.KW_FIELDS)
            self.state = 1441
            self.match(ZmeiLangParser.COLON)
            self.state = 1442
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
        self.enterRule(localctx, 296, self.RULE_an_admin_tabs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1444
            self.match(ZmeiLangParser.KW_TABS)
            self.state = 1445
            self.match(ZmeiLangParser.COLON)
            self.state = 1446
            self.an_admin_tab()
            self.state = 1451
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,120,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1447
                    self.match(ZmeiLangParser.COMA)
                    self.state = 1448
                    self.an_admin_tab() 
                self.state = 1453
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,120,self._ctx)

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
        self.enterRule(localctx, 298, self.RULE_an_admin_tab)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1454
            self.tab_name()
            self.state = 1456
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.STRING_DQ or _la==ZmeiLangParser.STRING_SQ:
                self.state = 1455
                self.tab_verbose_name()


            self.state = 1458
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1459
            self.field_list_expr()
            self.state = 1460
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
        self.enterRule(localctx, 300, self.RULE_tab_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1462
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
        self.enterRule(localctx, 302, self.RULE_tab_verbose_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1464
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
        self.enterRule(localctx, 304, self.RULE_an_admin_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1466
            self.match(ZmeiLangParser.KW_LIST)
            self.state = 1467
            self.match(ZmeiLangParser.COLON)
            self.state = 1468
            self.field_list_expr()
            self.state = 1472
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,122,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1469
                    self.match(ZmeiLangParser.NL) 
                self.state = 1474
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,122,self._ctx)

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
        self.enterRule(localctx, 306, self.RULE_an_admin_read_only)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1475
            self.match(ZmeiLangParser.KW_READ_ONLY)
            self.state = 1476
            self.match(ZmeiLangParser.COLON)
            self.state = 1477
            self.field_list_expr()
            self.state = 1481
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,123,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1478
                    self.match(ZmeiLangParser.NL) 
                self.state = 1483
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,123,self._ctx)

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
        self.enterRule(localctx, 308, self.RULE_an_admin_list_editable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1484
            self.match(ZmeiLangParser.KW_LIST_EDITABLE)
            self.state = 1485
            self.match(ZmeiLangParser.COLON)
            self.state = 1486
            self.field_list_expr()
            self.state = 1490
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,124,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1487
                    self.match(ZmeiLangParser.NL) 
                self.state = 1492
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,124,self._ctx)

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
        self.enterRule(localctx, 310, self.RULE_an_admin_list_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1493
            self.match(ZmeiLangParser.KW_LIST_FILTER)
            self.state = 1494
            self.match(ZmeiLangParser.COLON)
            self.state = 1495
            self.field_list_expr()
            self.state = 1499
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,125,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1496
                    self.match(ZmeiLangParser.NL) 
                self.state = 1501
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,125,self._ctx)

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
        self.enterRule(localctx, 312, self.RULE_an_admin_list_search)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1502
            self.match(ZmeiLangParser.KW_LIST_SEARCH)
            self.state = 1503
            self.match(ZmeiLangParser.COLON)
            self.state = 1504
            self.field_list_expr()
            self.state = 1508
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,126,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1505
                    self.match(ZmeiLangParser.NL) 
                self.state = 1510
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,126,self._ctx)

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
        self.enterRule(localctx, 314, self.RULE_an_admin_fields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1511
            self.match(ZmeiLangParser.KW_FIELDS)
            self.state = 1512
            self.match(ZmeiLangParser.COLON)
            self.state = 1513
            self.field_list_expr()
            self.state = 1517
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,127,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1514
                    self.match(ZmeiLangParser.NL) 
                self.state = 1519
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,127,self._ctx)

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
        self.enterRule(localctx, 316, self.RULE_page)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1520
            self.page_header()
            self.state = 1524
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,128,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1521
                    self.match(ZmeiLangParser.NL) 
                self.state = 1526
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,128,self._ctx)

            self.state = 1527
            self.page_body()
            self.state = 1531
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,129,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1528
                    self.match(ZmeiLangParser.NL) 
                self.state = 1533
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,129,self._ctx)

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
        self.enterRule(localctx, 318, self.RULE_page_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1534
            self.match(ZmeiLangParser.SQ_BRACE_OPEN)
            self.state = 1536
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,130,self._ctx)
            if la_ == 1:
                self.state = 1535
                self.page_base()


            self.state = 1538
            self.page_name()
            self.state = 1540
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.KW_AS:
                self.state = 1539
                self.page_alias()


            self.state = 1550
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COLON:
                self.state = 1542
                self.match(ZmeiLangParser.COLON)
                self.state = 1544
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 121)) & ~0x3f) == 0 and ((1 << (_la - 121)) & ((1 << (ZmeiLangParser.DOT - 121)) | (1 << (ZmeiLangParser.SLASH - 121)) | (1 << (ZmeiLangParser.DOLLAR - 121)))) != 0):
                    self.state = 1543
                    self.page_url()


                self.state = 1548
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.COLON:
                    self.state = 1546
                    self.match(ZmeiLangParser.COLON)
                    self.state = 1547
                    self.page_template()




            self.state = 1552
            self.match(ZmeiLangParser.SQ_BRACE_CLOSE)
            self.state = 1554
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,135,self._ctx)
            if la_ == 1:
                self.state = 1553
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

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def GT(self):
            return self.getToken(ZmeiLangParser.GT, 0)

        def DASH(self):
            return self.getToken(ZmeiLangParser.DASH, 0)

        def APPROX(self):
            return self.getToken(ZmeiLangParser.APPROX, 0)

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
        self.enterRule(localctx, 320, self.RULE_page_base)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1556
            self.id_or_kw()
            self.state = 1557
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.DASH or _la==ZmeiLangParser.APPROX):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 1558
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
        self.enterRule(localctx, 322, self.RULE_page_alias)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1560
            self.match(ZmeiLangParser.KW_AS)
            self.state = 1561
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
        self.enterRule(localctx, 324, self.RULE_page_alias_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1563
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
        self.enterRule(localctx, 326, self.RULE_page_template)
        try:
            self.state = 1567
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID, ZmeiLangParser.DIGIT, ZmeiLangParser.UNDERSCORE, ZmeiLangParser.DASH, ZmeiLangParser.DOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1565
                self.template_name()
                pass
            elif token in [ZmeiLangParser.ASSIGN, ZmeiLangParser.CODE_BLOCK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1566
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
        self.enterRule(localctx, 328, self.RULE_template_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1569
            self.file_name_part()
            self.state = 1574
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.SLASH:
                self.state = 1570
                self.match(ZmeiLangParser.SLASH)
                self.state = 1571
                self.file_name_part()
                self.state = 1576
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
        self.enterRule(localctx, 330, self.RULE_file_name_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1582 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1582
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                    self.state = 1577
                    self.id_or_kw()
                    pass
                elif token in [ZmeiLangParser.DIGIT]:
                    self.state = 1578
                    self.match(ZmeiLangParser.DIGIT)
                    pass
                elif token in [ZmeiLangParser.DASH]:
                    self.state = 1579
                    self.match(ZmeiLangParser.DASH)
                    pass
                elif token in [ZmeiLangParser.UNDERSCORE]:
                    self.state = 1580
                    self.match(ZmeiLangParser.UNDERSCORE)
                    pass
                elif token in [ZmeiLangParser.DOT]:
                    self.state = 1581
                    self.match(ZmeiLangParser.DOT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1584 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.WRITE_MODE) | (1 << ZmeiLangParser.BOOL) | (1 << ZmeiLangParser.KW_THEME) | (1 << ZmeiLangParser.KW_FILTER_OUT) | (1 << ZmeiLangParser.KW_FILTER_IN) | (1 << ZmeiLangParser.KW_PAGE) | (1 << ZmeiLangParser.KW_LINK_SUFFIX) | (1 << ZmeiLangParser.KW_URL_PREFIX) | (1 << ZmeiLangParser.KW_CAN_EDIT) | (1 << ZmeiLangParser.KW_OBJECT_EXPR) | (1 << ZmeiLangParser.KW_BLOCK) | (1 << ZmeiLangParser.KW_ITEM_NAME) | (1 << ZmeiLangParser.KW_PK_PARAM) | (1 << ZmeiLangParser.KW_LIST_FIELDS) | (1 << ZmeiLangParser.KW_DELETE) | (1 << ZmeiLangParser.KW_EDIT) | (1 << ZmeiLangParser.KW_CREATE) | (1 << ZmeiLangParser.KW_DETAIL) | (1 << ZmeiLangParser.KW_SKIP) | (1 << ZmeiLangParser.KW_FROM) | (1 << ZmeiLangParser.KW_POLY_LIST) | (1 << ZmeiLangParser.KW_CSS) | (1 << ZmeiLangParser.KW_JS) | (1 << ZmeiLangParser.KW_INLINE_TYPE) | (1 << ZmeiLangParser.KW_AUTH_TYPE) | (1 << ZmeiLangParser.KW_INLINE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ZmeiLangParser.KW_TYPE - 64)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 64)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 64)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 64)) | (1 << (ZmeiLangParser.KW_QUERY - 64)) | (1 << (ZmeiLangParser.KW_AUTH - 64)) | (1 << (ZmeiLangParser.KW_COUNT - 64)) | (1 << (ZmeiLangParser.KW_I18N - 64)) | (1 << (ZmeiLangParser.KW_EXTRA - 64)) | (1 << (ZmeiLangParser.KW_TABS - 64)) | (1 << (ZmeiLangParser.KW_LIST - 64)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 64)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 64)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 64)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 64)) | (1 << (ZmeiLangParser.KW_FIELDS - 64)) | (1 << (ZmeiLangParser.KW_IMPORT - 64)) | (1 << (ZmeiLangParser.KW_AS - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 64)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 64)) | (1 << (ZmeiLangParser.ID - 64)) | (1 << (ZmeiLangParser.DIGIT - 64)) | (1 << (ZmeiLangParser.UNDERSCORE - 64)) | (1 << (ZmeiLangParser.DASH - 64)) | (1 << (ZmeiLangParser.DOT - 64)))) != 0)):
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
        self.enterRule(localctx, 332, self.RULE_page_url)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1587
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT or _la==ZmeiLangParser.DOLLAR:
                self.state = 1586
                _la = self._input.LA(1)
                if not(_la==ZmeiLangParser.DOT or _la==ZmeiLangParser.DOLLAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 1589
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
        self.enterRule(localctx, 334, self.RULE_url_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1594 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1594
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                    self.state = 1591
                    self.id_or_kw()
                    pass
                elif token in [ZmeiLangParser.DASH]:
                    self.state = 1592
                    self.match(ZmeiLangParser.DASH)
                    pass
                elif token in [ZmeiLangParser.DIGIT]:
                    self.state = 1593
                    self.match(ZmeiLangParser.DIGIT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1596 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.WRITE_MODE) | (1 << ZmeiLangParser.BOOL) | (1 << ZmeiLangParser.KW_THEME) | (1 << ZmeiLangParser.KW_FILTER_OUT) | (1 << ZmeiLangParser.KW_FILTER_IN) | (1 << ZmeiLangParser.KW_PAGE) | (1 << ZmeiLangParser.KW_LINK_SUFFIX) | (1 << ZmeiLangParser.KW_URL_PREFIX) | (1 << ZmeiLangParser.KW_CAN_EDIT) | (1 << ZmeiLangParser.KW_OBJECT_EXPR) | (1 << ZmeiLangParser.KW_BLOCK) | (1 << ZmeiLangParser.KW_ITEM_NAME) | (1 << ZmeiLangParser.KW_PK_PARAM) | (1 << ZmeiLangParser.KW_LIST_FIELDS) | (1 << ZmeiLangParser.KW_DELETE) | (1 << ZmeiLangParser.KW_EDIT) | (1 << ZmeiLangParser.KW_CREATE) | (1 << ZmeiLangParser.KW_DETAIL) | (1 << ZmeiLangParser.KW_SKIP) | (1 << ZmeiLangParser.KW_FROM) | (1 << ZmeiLangParser.KW_POLY_LIST) | (1 << ZmeiLangParser.KW_CSS) | (1 << ZmeiLangParser.KW_JS) | (1 << ZmeiLangParser.KW_INLINE_TYPE) | (1 << ZmeiLangParser.KW_AUTH_TYPE) | (1 << ZmeiLangParser.KW_INLINE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ZmeiLangParser.KW_TYPE - 64)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 64)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 64)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 64)) | (1 << (ZmeiLangParser.KW_QUERY - 64)) | (1 << (ZmeiLangParser.KW_AUTH - 64)) | (1 << (ZmeiLangParser.KW_COUNT - 64)) | (1 << (ZmeiLangParser.KW_I18N - 64)) | (1 << (ZmeiLangParser.KW_EXTRA - 64)) | (1 << (ZmeiLangParser.KW_TABS - 64)) | (1 << (ZmeiLangParser.KW_LIST - 64)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 64)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 64)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 64)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 64)) | (1 << (ZmeiLangParser.KW_FIELDS - 64)) | (1 << (ZmeiLangParser.KW_IMPORT - 64)) | (1 << (ZmeiLangParser.KW_AS - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 64)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 64)) | (1 << (ZmeiLangParser.ID - 64)) | (1 << (ZmeiLangParser.DIGIT - 64)) | (1 << (ZmeiLangParser.DASH - 64)))) != 0)):
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
        self.enterRule(localctx, 336, self.RULE_url_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1598
            self.match(ZmeiLangParser.LT)
            self.state = 1599
            self.id_or_kw()
            self.state = 1600
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
        self.enterRule(localctx, 338, self.RULE_url_segment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1604
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID, ZmeiLangParser.DIGIT, ZmeiLangParser.DASH]:
                self.state = 1602
                self.url_part()
                pass
            elif token in [ZmeiLangParser.LT]:
                self.state = 1603
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
        self.enterRule(localctx, 340, self.RULE_url_segments)
        self._la = 0 # Token type
        try:
            self.state = 1616
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,146,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1606
                self.match(ZmeiLangParser.SLASH)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1609 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 1607
                        self.match(ZmeiLangParser.SLASH)
                        self.state = 1608
                        self.url_segment()

                    else:
                        raise NoViableAltException(self)
                    self.state = 1611 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,144,self._ctx)

                self.state = 1614
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.SLASH:
                    self.state = 1613
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
        self.enterRule(localctx, 342, self.RULE_page_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1618
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
        self.enterRule(localctx, 344, self.RULE_page_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1623
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,147,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1620
                    self.page_field() 
                self.state = 1625
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,147,self._ctx)

            self.state = 1629
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,148,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1626
                    self.page_function() 
                self.state = 1631
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,148,self._ctx)

            self.state = 1633
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.ASSIGN or _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 1632
                self.page_code()


            self.state = 1638
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,150,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1635
                    self.match(ZmeiLangParser.NL) 
                self.state = 1640
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,150,self._ctx)

            self.state = 1644
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,151,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1641
                    self.page_annotation() 
                self.state = 1646
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,151,self._ctx)

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
        self.enterRule(localctx, 346, self.RULE_page_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1647
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
        self.enterRule(localctx, 348, self.RULE_page_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1649
            self.page_field_name()
            self.state = 1650
            self.match(ZmeiLangParser.ASSIGN)
            self.state = 1651
            self.page_field_code()
            self.state = 1658
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.NL]:
                self.state = 1653 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 1652
                        self.match(ZmeiLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 1655 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,152,self._ctx)

                pass
            elif token in [ZmeiLangParser.EOF]:
                self.state = 1657
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
        self.enterRule(localctx, 350, self.RULE_page_field_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1660
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
        self.enterRule(localctx, 352, self.RULE_page_field_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1662
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
        self.enterRule(localctx, 354, self.RULE_page_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1664
            self.page_function_name()
            self.state = 1665
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1667
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.WRITE_MODE) | (1 << ZmeiLangParser.BOOL) | (1 << ZmeiLangParser.KW_THEME) | (1 << ZmeiLangParser.KW_FILTER_OUT) | (1 << ZmeiLangParser.KW_FILTER_IN) | (1 << ZmeiLangParser.KW_PAGE) | (1 << ZmeiLangParser.KW_LINK_SUFFIX) | (1 << ZmeiLangParser.KW_URL_PREFIX) | (1 << ZmeiLangParser.KW_CAN_EDIT) | (1 << ZmeiLangParser.KW_OBJECT_EXPR) | (1 << ZmeiLangParser.KW_BLOCK) | (1 << ZmeiLangParser.KW_ITEM_NAME) | (1 << ZmeiLangParser.KW_PK_PARAM) | (1 << ZmeiLangParser.KW_LIST_FIELDS) | (1 << ZmeiLangParser.KW_DELETE) | (1 << ZmeiLangParser.KW_EDIT) | (1 << ZmeiLangParser.KW_CREATE) | (1 << ZmeiLangParser.KW_DETAIL) | (1 << ZmeiLangParser.KW_SKIP) | (1 << ZmeiLangParser.KW_FROM) | (1 << ZmeiLangParser.KW_POLY_LIST) | (1 << ZmeiLangParser.KW_CSS) | (1 << ZmeiLangParser.KW_JS) | (1 << ZmeiLangParser.KW_INLINE_TYPE) | (1 << ZmeiLangParser.KW_AUTH_TYPE) | (1 << ZmeiLangParser.KW_INLINE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ZmeiLangParser.KW_TYPE - 64)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 64)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 64)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 64)) | (1 << (ZmeiLangParser.KW_QUERY - 64)) | (1 << (ZmeiLangParser.KW_AUTH - 64)) | (1 << (ZmeiLangParser.KW_COUNT - 64)) | (1 << (ZmeiLangParser.KW_I18N - 64)) | (1 << (ZmeiLangParser.KW_EXTRA - 64)) | (1 << (ZmeiLangParser.KW_TABS - 64)) | (1 << (ZmeiLangParser.KW_LIST - 64)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 64)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 64)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 64)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 64)) | (1 << (ZmeiLangParser.KW_FIELDS - 64)) | (1 << (ZmeiLangParser.KW_IMPORT - 64)) | (1 << (ZmeiLangParser.KW_AS - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 64)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 64)) | (1 << (ZmeiLangParser.ID - 64)))) != 0):
                self.state = 1666
                self.page_function_args()


            self.state = 1669
            self.match(ZmeiLangParser.BRACE_CLOSE)
            self.state = 1671
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 1670
                self.code_block()


            self.state = 1679
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.NL]:
                self.state = 1674 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 1673
                        self.match(ZmeiLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 1676 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,156,self._ctx)

                pass
            elif token in [ZmeiLangParser.EOF]:
                self.state = 1678
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
        self.enterRule(localctx, 356, self.RULE_page_function_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1681
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
        self.enterRule(localctx, 358, self.RULE_page_function_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1683
            self.id_or_kw()
            self.state = 1688
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 1684
                self.match(ZmeiLangParser.COMA)
                self.state = 1685
                self.id_or_kw()
                self.state = 1690
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
        self.enterRule(localctx, 360, self.RULE_page_annotation)
        try:
            self.state = 1707
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.AN_HTML]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1691
                self.an_html()
                pass
            elif token in [ZmeiLangParser.AN_REACT, ZmeiLangParser.AN_REACT_CLIENT, ZmeiLangParser.AN_REACT_SERVER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1692
                self.an_react()
                pass
            elif token in [ZmeiLangParser.AN_FLUTTER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1693
                self.an_flutter()
                pass
            elif token in [ZmeiLangParser.AN_STREAM]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1694
                self.an_stream()
                pass
            elif token in [ZmeiLangParser.AN_GET]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1695
                self.an_get()
                pass
            elif token in [ZmeiLangParser.AN_MENU]:
                self.enterOuterAlt(localctx, 6)
                self.state = 1696
                self.an_menu()
                pass
            elif token in [ZmeiLangParser.AN_CRUD]:
                self.enterOuterAlt(localctx, 7)
                self.state = 1697
                self.an_crud()
                pass
            elif token in [ZmeiLangParser.AN_CRUD_DETAIL]:
                self.enterOuterAlt(localctx, 8)
                self.state = 1698
                self.an_crud_detail()
                pass
            elif token in [ZmeiLangParser.AN_CRUD_DELETE]:
                self.enterOuterAlt(localctx, 9)
                self.state = 1699
                self.an_crud_delete()
                pass
            elif token in [ZmeiLangParser.AN_CRUD_EDIT]:
                self.enterOuterAlt(localctx, 10)
                self.state = 1700
                self.an_crud_edit()
                pass
            elif token in [ZmeiLangParser.AN_CRUD_CREATE]:
                self.enterOuterAlt(localctx, 11)
                self.state = 1701
                self.an_crud_create()
                pass
            elif token in [ZmeiLangParser.AN_POST]:
                self.enterOuterAlt(localctx, 12)
                self.state = 1702
                self.an_post()
                pass
            elif token in [ZmeiLangParser.AN_ERROR]:
                self.enterOuterAlt(localctx, 13)
                self.state = 1703
                self.an_error()
                pass
            elif token in [ZmeiLangParser.AN_AUTH]:
                self.enterOuterAlt(localctx, 14)
                self.state = 1704
                self.an_auth()
                pass
            elif token in [ZmeiLangParser.AN_MARKDOWN]:
                self.enterOuterAlt(localctx, 15)
                self.state = 1705
                self.an_markdown()
                pass
            elif token in [ZmeiLangParser.NL]:
                self.enterOuterAlt(localctx, 16)
                self.state = 1706
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
        self.enterRule(localctx, 362, self.RULE_an_react)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1709
            self.an_react_type()
            self.state = 1712
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 1710
                self.match(ZmeiLangParser.DOT)
                self.state = 1711
                self.an_react_descriptor()


            self.state = 1714
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
        self.enterRule(localctx, 364, self.RULE_an_react_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1716
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
        self.enterRule(localctx, 366, self.RULE_an_react_descriptor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1718
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
        self.enterRule(localctx, 368, self.RULE_an_markdown)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1720
            self.match(ZmeiLangParser.AN_MARKDOWN)
            self.state = 1723
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 1721
                self.match(ZmeiLangParser.DOT)
                self.state = 1722
                self.an_markdown_descriptor()


            self.state = 1725
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
        self.enterRule(localctx, 370, self.RULE_an_markdown_descriptor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1727
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
        self.enterRule(localctx, 372, self.RULE_an_auth)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1729
            self.match(ZmeiLangParser.AN_AUTH)
            self.state = 1731
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 1730
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
        self.enterRule(localctx, 374, self.RULE_an_error)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1733
            self.match(ZmeiLangParser.AN_ERROR)
            self.state = 1734
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1735
            self.an_error_code()
            self.state = 1736
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
        self.enterRule(localctx, 376, self.RULE_an_error_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1738
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
        self.enterRule(localctx, 378, self.RULE_an_post)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1740
            self.match(ZmeiLangParser.AN_POST)
            self.state = 1742
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 1741
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
        self.enterRule(localctx, 380, self.RULE_an_crud_create)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1744
            self.match(ZmeiLangParser.AN_CRUD_CREATE)
            self.state = 1745
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
        self.enterRule(localctx, 382, self.RULE_an_crud)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1747
            self.match(ZmeiLangParser.AN_CRUD)
            self.state = 1748
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
        self.enterRule(localctx, 384, self.RULE_an_crud_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1752
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 1750
                self.match(ZmeiLangParser.DOT)
                self.state = 1751
                self.an_crud_descriptor()


            self.state = 1754
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1758
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 1755
                self.match(ZmeiLangParser.NL)
                self.state = 1760
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1761
            self.an_crud_target_model()
            self.state = 1763
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 1762
                self.an_crud_target_filter()


            self.state = 1780
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,168,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1778
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [ZmeiLangParser.KW_THEME]:
                        self.state = 1765
                        self.an_crud_theme()
                        pass
                    elif token in [ZmeiLangParser.KW_SKIP]:
                        self.state = 1766
                        self.an_crud_skip()
                        pass
                    elif token in [ZmeiLangParser.KW_FIELDS]:
                        self.state = 1767
                        self.an_crud_fields()
                        pass
                    elif token in [ZmeiLangParser.KW_LIST_FIELDS]:
                        self.state = 1768
                        self.an_crud_list_fields()
                        pass
                    elif token in [ZmeiLangParser.KW_PK_PARAM]:
                        self.state = 1769
                        self.an_crud_pk_param()
                        pass
                    elif token in [ZmeiLangParser.KW_ITEM_NAME]:
                        self.state = 1770
                        self.an_crud_item_name()
                        pass
                    elif token in [ZmeiLangParser.KW_BLOCK]:
                        self.state = 1771
                        self.an_crud_block()
                        pass
                    elif token in [ZmeiLangParser.KW_OBJECT_EXPR]:
                        self.state = 1772
                        self.an_crud_object_expr()
                        pass
                    elif token in [ZmeiLangParser.KW_CAN_EDIT]:
                        self.state = 1773
                        self.an_crud_can_edit()
                        pass
                    elif token in [ZmeiLangParser.KW_URL_PREFIX]:
                        self.state = 1774
                        self.an_crud_url_prefix()
                        pass
                    elif token in [ZmeiLangParser.KW_LINK_SUFFIX]:
                        self.state = 1775
                        self.an_crud_link_suffix()
                        pass
                    elif token in [ZmeiLangParser.NL]:
                        self.state = 1776
                        self.match(ZmeiLangParser.NL)
                        pass
                    elif token in [ZmeiLangParser.COMA]:
                        self.state = 1777
                        self.match(ZmeiLangParser.COMA)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 1782
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,168,self._ctx)

            self.state = 1786
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,169,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1783
                    self.match(ZmeiLangParser.NL) 
                self.state = 1788
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,169,self._ctx)

            self.state = 1791
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,170,self._ctx)
            if la_ == 1:
                self.state = 1789
                self.an_crud_next_page()

            elif la_ == 2:
                self.state = 1790
                self.an_crud_next_page_url()


            self.state = 1796
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,171,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1793
                    self.match(ZmeiLangParser.NL) 
                self.state = 1798
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,171,self._ctx)

            self.state = 1802
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 52)) & ~0x3f) == 0 and ((1 << (_la - 52)) & ((1 << (ZmeiLangParser.KW_DELETE - 52)) | (1 << (ZmeiLangParser.KW_EDIT - 52)) | (1 << (ZmeiLangParser.KW_CREATE - 52)) | (1 << (ZmeiLangParser.KW_DETAIL - 52)) | (1 << (ZmeiLangParser.KW_LIST - 52)))) != 0):
                self.state = 1799
                self.an_crud_page_override()
                self.state = 1804
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1808
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 1805
                self.match(ZmeiLangParser.NL)
                self.state = 1810
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1811
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
        self.enterRule(localctx, 386, self.RULE_an_crud_page_override)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1813
            self.an_crud_view_name()
            self.state = 1817
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 1814
                self.match(ZmeiLangParser.NL)
                self.state = 1819
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1820
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1824
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,175,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1821
                    self.match(ZmeiLangParser.NL) 
                self.state = 1826
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,175,self._ctx)

            self.state = 1827
            self.page_body()
            self.state = 1831
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 1828
                self.match(ZmeiLangParser.NL)
                self.state = 1833
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1834
            self.match(ZmeiLangParser.BRACE_CLOSE)
            self.state = 1838
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,177,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1835
                    self.match(ZmeiLangParser.NL) 
                self.state = 1840
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,177,self._ctx)

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
        self.enterRule(localctx, 388, self.RULE_an_crud_descriptor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1841
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
        self.enterRule(localctx, 390, self.RULE_an_crud_next_page)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1847
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1843
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1844
                self.an_crud_next_page_event_name()
                self.state = 1845
                self.match(ZmeiLangParser.BRACE_CLOSE)


            self.state = 1849
            self.match(ZmeiLangParser.EQUALS)
            self.state = 1850
            self.match(ZmeiLangParser.GT)
            self.state = 1851
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
        self.enterRule(localctx, 392, self.RULE_an_crud_next_page_event_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1853
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
        self.enterRule(localctx, 394, self.RULE_an_crud_next_page_url)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1859
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1855
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1856
                self.an_crud_next_page_event_name()
                self.state = 1857
                self.match(ZmeiLangParser.BRACE_CLOSE)


            self.state = 1861
            self.match(ZmeiLangParser.EQUALS)
            self.state = 1862
            self.match(ZmeiLangParser.GT)
            self.state = 1863
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
        self.enterRule(localctx, 396, self.RULE_an_crud_next_page_url_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1865
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

        def HASH(self):
            return self.getToken(ZmeiLangParser.HASH, 0)

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


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
        self.enterRule(localctx, 398, self.RULE_an_crud_target_model)
        try:
            self.state = 1870
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.HASH]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1867
                self.match(ZmeiLangParser.HASH)
                self.state = 1868
                self.id_or_kw()
                pass
            elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1869
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
        self.enterRule(localctx, 400, self.RULE_an_crud_target_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1872
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
        self.enterRule(localctx, 402, self.RULE_an_crud_theme)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1874
            self.match(ZmeiLangParser.KW_THEME)
            self.state = 1875
            self.match(ZmeiLangParser.COLON)
            self.state = 1876
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
        self.enterRule(localctx, 404, self.RULE_an_crud_url_prefix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1878
            self.match(ZmeiLangParser.KW_URL_PREFIX)
            self.state = 1879
            self.match(ZmeiLangParser.COLON)
            self.state = 1880
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
        self.enterRule(localctx, 406, self.RULE_an_crud_url_prefix_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1882
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
        self.enterRule(localctx, 408, self.RULE_an_crud_link_suffix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1884
            self.match(ZmeiLangParser.KW_LINK_SUFFIX)
            self.state = 1885
            self.match(ZmeiLangParser.COLON)
            self.state = 1886
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
        self.enterRule(localctx, 410, self.RULE_an_crud_link_suffix_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1888
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
        self.enterRule(localctx, 412, self.RULE_an_crud_item_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1890
            self.match(ZmeiLangParser.KW_ITEM_NAME)
            self.state = 1891
            self.match(ZmeiLangParser.COLON)
            self.state = 1892
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
        self.enterRule(localctx, 414, self.RULE_an_crud_object_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1894
            self.match(ZmeiLangParser.KW_OBJECT_EXPR)
            self.state = 1898
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.ASSIGN]:
                self.state = 1895
                self.code_line()
                pass
            elif token in [ZmeiLangParser.COLON]:
                self.state = 1896
                self.match(ZmeiLangParser.COLON)
                self.state = 1897
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
        self.enterRule(localctx, 416, self.RULE_an_crud_can_edit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1900
            self.match(ZmeiLangParser.KW_CAN_EDIT)
            self.state = 1904
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.ASSIGN]:
                self.state = 1901
                self.code_line()
                pass
            elif token in [ZmeiLangParser.COLON]:
                self.state = 1902
                self.match(ZmeiLangParser.COLON)
                self.state = 1903
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
        self.enterRule(localctx, 418, self.RULE_an_crud_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1906
            self.match(ZmeiLangParser.KW_BLOCK)
            self.state = 1907
            self.match(ZmeiLangParser.COLON)
            self.state = 1908
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
        self.enterRule(localctx, 420, self.RULE_an_crud_pk_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1910
            self.match(ZmeiLangParser.KW_PK_PARAM)
            self.state = 1911
            self.match(ZmeiLangParser.COLON)
            self.state = 1912
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
        self.enterRule(localctx, 422, self.RULE_an_crud_skip)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1914
            self.match(ZmeiLangParser.KW_SKIP)
            self.state = 1915
            self.match(ZmeiLangParser.COLON)
            self.state = 1916
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
        self.enterRule(localctx, 424, self.RULE_an_crud_skip_values)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1918
            self.an_crud_view_name()
            self.state = 1923
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,183,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1919
                    self.match(ZmeiLangParser.COMA)
                    self.state = 1920
                    self.an_crud_view_name() 
                self.state = 1925
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,183,self._ctx)

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
        self.enterRule(localctx, 426, self.RULE_an_crud_view_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1926
            _la = self._input.LA(1)
            if not(((((_la - 52)) & ~0x3f) == 0 and ((1 << (_la - 52)) & ((1 << (ZmeiLangParser.KW_DELETE - 52)) | (1 << (ZmeiLangParser.KW_EDIT - 52)) | (1 << (ZmeiLangParser.KW_CREATE - 52)) | (1 << (ZmeiLangParser.KW_DETAIL - 52)) | (1 << (ZmeiLangParser.KW_LIST - 52)))) != 0)):
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
        self.enterRule(localctx, 428, self.RULE_an_crud_fields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1928
            self.match(ZmeiLangParser.KW_FIELDS)
            self.state = 1929
            self.match(ZmeiLangParser.COLON)
            self.state = 1930
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
        self.enterRule(localctx, 430, self.RULE_an_crud_fields_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1932
            self.an_crud_field()
            self.state = 1937
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,184,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1933
                    self.match(ZmeiLangParser.COMA)
                    self.state = 1934
                    self.an_crud_field() 
                self.state = 1939
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,184,self._ctx)

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
        self.enterRule(localctx, 432, self.RULE_an_crud_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1940
            self.an_crud_field_spec()
            self.state = 1942
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 1941
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
        self.enterRule(localctx, 434, self.RULE_an_crud_field_spec)
        self._la = 0 # Token type
        try:
            self.state = 1949
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.STAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1944
                self.match(ZmeiLangParser.STAR)
                pass
            elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID, ZmeiLangParser.EXCLUDE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1946
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.EXCLUDE:
                    self.state = 1945
                    self.match(ZmeiLangParser.EXCLUDE)


                self.state = 1948
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
        self.enterRule(localctx, 436, self.RULE_an_crud_field_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1951
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
        self.enterRule(localctx, 438, self.RULE_an_crud_list_fields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1953
            self.match(ZmeiLangParser.KW_LIST_FIELDS)
            self.state = 1954
            self.match(ZmeiLangParser.COLON)
            self.state = 1955
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
        self.enterRule(localctx, 440, self.RULE_an_crud_list_fields_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1957
            self.an_crud_list_field()
            self.state = 1962
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,188,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1958
                    self.match(ZmeiLangParser.COMA)
                    self.state = 1959
                    self.an_crud_list_field() 
                self.state = 1964
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,188,self._ctx)

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
        self.enterRule(localctx, 442, self.RULE_an_crud_list_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1965
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
        self.enterRule(localctx, 444, self.RULE_an_crud_list_field_spec)
        self._la = 0 # Token type
        try:
            self.state = 1972
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.STAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1967
                self.match(ZmeiLangParser.STAR)
                pass
            elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID, ZmeiLangParser.EXCLUDE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1969
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.EXCLUDE:
                    self.state = 1968
                    self.match(ZmeiLangParser.EXCLUDE)


                self.state = 1971
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
        self.enterRule(localctx, 446, self.RULE_an_crud_edit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1974
            self.match(ZmeiLangParser.AN_CRUD_EDIT)
            self.state = 1975
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
        self.enterRule(localctx, 448, self.RULE_an_crud_delete)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1977
            self.match(ZmeiLangParser.AN_CRUD_DELETE)
            self.state = 1978
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
        self.enterRule(localctx, 450, self.RULE_an_crud_detail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1980
            self.match(ZmeiLangParser.AN_CRUD_DETAIL)
            self.state = 1981
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
        self.enterRule(localctx, 452, self.RULE_an_menu)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1983
            self.match(ZmeiLangParser.AN_MENU)
            self.state = 1984
            self.match(ZmeiLangParser.DOT)
            self.state = 1985
            self.an_menu_descriptor()
            self.state = 1986
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1990
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,191,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1987
                    self.match(ZmeiLangParser.NL) 
                self.state = 1992
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,191,self._ctx)

            self.state = 1994 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 1993
                    self.an_menu_item()

                else:
                    raise NoViableAltException(self)
                self.state = 1996 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,192,self._ctx)

            self.state = 2001
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 1998
                self.match(ZmeiLangParser.NL)
                self.state = 2003
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2004
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
        self.enterRule(localctx, 454, self.RULE_an_menu_descriptor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2006
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
        self.enterRule(localctx, 456, self.RULE_an_menu_item)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2009
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COMA:
                self.state = 2008
                self.match(ZmeiLangParser.COMA)


            self.state = 2014
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 2011
                self.match(ZmeiLangParser.NL)
                self.state = 2016
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2018
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.SQ_BRACE_OPEN:
                self.state = 2017
                self.an_menu_item_args()


            self.state = 2020
            self.an_menu_label()
            self.state = 2023
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.ASSIGN]:
                self.state = 2021
                self.an_menu_item_code()
                pass
            elif token in [ZmeiLangParser.COLON]:
                self.state = 2022
                self.an_menu_target()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 2028
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,198,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2025
                    self.match(ZmeiLangParser.NL) 
                self.state = 2030
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,198,self._ctx)

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
        self.enterRule(localctx, 458, self.RULE_an_menu_target)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2031
            self.match(ZmeiLangParser.COLON)
            self.state = 2034
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.KW_PAGE]:
                self.state = 2032
                self.an_menu_item_page()
                pass
            elif token in [ZmeiLangParser.STRING_DQ, ZmeiLangParser.STRING_SQ]:
                self.state = 2033
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
        self.enterRule(localctx, 460, self.RULE_an_menu_item_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2036
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
        self.enterRule(localctx, 462, self.RULE_an_menu_item_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2038
            self.match(ZmeiLangParser.SQ_BRACE_OPEN)
            self.state = 2039
            self.an_menu_item_arg()
            self.state = 2044
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 2040
                self.match(ZmeiLangParser.COMA)
                self.state = 2041
                self.an_menu_item_arg()
                self.state = 2046
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2047
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
        self.enterRule(localctx, 464, self.RULE_an_menu_item_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2049
            self.an_menu_item_arg_key()
            self.state = 2050
            self.match(ZmeiLangParser.EQUALS)
            self.state = 2051
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
        self.enterRule(localctx, 466, self.RULE_an_menu_item_arg_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2053
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
        self.enterRule(localctx, 468, self.RULE_an_menu_item_arg_val)
        try:
            self.state = 2058
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.STRING_DQ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2055
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2056
                self.match(ZmeiLangParser.STRING_SQ)
                pass
            elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2057
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
        self.enterRule(localctx, 470, self.RULE_an_menu_item_url)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2060
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
        self.enterRule(localctx, 472, self.RULE_an_menu_item_page)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2062
            self.match(ZmeiLangParser.KW_PAGE)
            self.state = 2063
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 2064
            self.an_menu_item_page_ref()
            self.state = 2065
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

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


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
        self.enterRule(localctx, 474, self.RULE_an_menu_item_page_ref)
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
        self.enterRule(localctx, 476, self.RULE_an_menu_label)
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
            elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
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
        self.enterRule(localctx, 478, self.RULE_an_get)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2074
            self.match(ZmeiLangParser.AN_GET)
            self.state = 2076
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 2075
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
        self.enterRule(localctx, 480, self.RULE_an_stream)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2078
            self.match(ZmeiLangParser.AN_STREAM)

            self.state = 2079
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 2082 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 2082
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID, ZmeiLangParser.HASH]:
                    self.state = 2080
                    self.an_stream_model()
                    pass
                elif token in [ZmeiLangParser.NL]:
                    self.state = 2081
                    self.match(ZmeiLangParser.NL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 2084 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.WRITE_MODE) | (1 << ZmeiLangParser.BOOL) | (1 << ZmeiLangParser.KW_THEME) | (1 << ZmeiLangParser.KW_FILTER_OUT) | (1 << ZmeiLangParser.KW_FILTER_IN) | (1 << ZmeiLangParser.KW_PAGE) | (1 << ZmeiLangParser.KW_LINK_SUFFIX) | (1 << ZmeiLangParser.KW_URL_PREFIX) | (1 << ZmeiLangParser.KW_CAN_EDIT) | (1 << ZmeiLangParser.KW_OBJECT_EXPR) | (1 << ZmeiLangParser.KW_BLOCK) | (1 << ZmeiLangParser.KW_ITEM_NAME) | (1 << ZmeiLangParser.KW_PK_PARAM) | (1 << ZmeiLangParser.KW_LIST_FIELDS) | (1 << ZmeiLangParser.KW_DELETE) | (1 << ZmeiLangParser.KW_EDIT) | (1 << ZmeiLangParser.KW_CREATE) | (1 << ZmeiLangParser.KW_DETAIL) | (1 << ZmeiLangParser.KW_SKIP) | (1 << ZmeiLangParser.KW_FROM) | (1 << ZmeiLangParser.KW_POLY_LIST) | (1 << ZmeiLangParser.KW_CSS) | (1 << ZmeiLangParser.KW_JS) | (1 << ZmeiLangParser.KW_INLINE_TYPE) | (1 << ZmeiLangParser.KW_AUTH_TYPE) | (1 << ZmeiLangParser.KW_INLINE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ZmeiLangParser.KW_TYPE - 64)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 64)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 64)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 64)) | (1 << (ZmeiLangParser.KW_QUERY - 64)) | (1 << (ZmeiLangParser.KW_AUTH - 64)) | (1 << (ZmeiLangParser.KW_COUNT - 64)) | (1 << (ZmeiLangParser.KW_I18N - 64)) | (1 << (ZmeiLangParser.KW_EXTRA - 64)) | (1 << (ZmeiLangParser.KW_TABS - 64)) | (1 << (ZmeiLangParser.KW_LIST - 64)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 64)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 64)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 64)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 64)) | (1 << (ZmeiLangParser.KW_FIELDS - 64)) | (1 << (ZmeiLangParser.KW_IMPORT - 64)) | (1 << (ZmeiLangParser.KW_AS - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 64)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 64)) | (1 << (ZmeiLangParser.NL - 64)) | (1 << (ZmeiLangParser.ID - 64)) | (1 << (ZmeiLangParser.HASH - 64)))) != 0)):
                    break

            self.state = 2086
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
        self.enterRule(localctx, 482, self.RULE_an_stream_model)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2088
            self.an_stream_target_model()
            self.state = 2090
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 2089
                self.an_stream_target_filter()


            self.state = 2093
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.EQUALS:
                self.state = 2092
                self.an_stream_field_list()


            self.state = 2096
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COMA:
                self.state = 2095
                self.match(ZmeiLangParser.COMA)


            self.state = 2099
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,209,self._ctx)
            if la_ == 1:
                self.state = 2098
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

        def HASH(self):
            return self.getToken(ZmeiLangParser.HASH, 0)

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


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
        self.enterRule(localctx, 484, self.RULE_an_stream_target_model)
        try:
            self.state = 2104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.HASH]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2101
                self.match(ZmeiLangParser.HASH)
                self.state = 2102
                self.id_or_kw()
                pass
            elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2103
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
        self.enterRule(localctx, 486, self.RULE_an_stream_target_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2106
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
        self.enterRule(localctx, 488, self.RULE_an_stream_field_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2108
            self.match(ZmeiLangParser.EQUALS)
            self.state = 2109
            self.match(ZmeiLangParser.GT)
            self.state = 2119
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.STAR]:
                self.state = 2110
                self.match(ZmeiLangParser.STAR)
                pass
            elif token in [ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE, ZmeiLangParser.KW_AUTH_TYPE, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTRA, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.ID]:
                self.state = 2111
                self.an_stream_field_name()
                self.state = 2116
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,211,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 2112
                        self.match(ZmeiLangParser.COMA)
                        self.state = 2113
                        self.an_stream_field_name() 
                    self.state = 2118
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
        self.enterRule(localctx, 490, self.RULE_an_stream_field_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2121
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
        self.enterRule(localctx, 492, self.RULE_an_flutter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2123
            self.match(ZmeiLangParser.AN_FLUTTER)
            self.state = 2126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 2124
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 2125
                self.match(ZmeiLangParser.BRACE_CLOSE)


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
        self.enterRule(localctx, 494, self.RULE_an_html)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2128
            self.match(ZmeiLangParser.AN_HTML)
            self.state = 2131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 2129
                self.match(ZmeiLangParser.DOT)
                self.state = 2130
                self.an_html_descriptor()


            self.state = 2133
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
        self.enterRule(localctx, 496, self.RULE_an_html_descriptor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2135
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






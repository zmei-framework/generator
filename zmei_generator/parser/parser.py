from antlr4 import *

from .gen.ZmeiLangSimpleLexer import ZmeiLangSimpleLexer
from .gen.ZmeiLangParser import ZmeiLangParser


def parse_file(filename):
    return parse(FileStream(filename))


def parse_string(string):
    return parse(InputStream(string))


def parse(stream):
    lexer = ZmeiLangSimpleLexer(stream)
    stream = CommonTokenStream(lexer)
    parser = ZmeiLangParser(stream)
    return parser.col_file()


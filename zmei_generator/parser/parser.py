from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

from zmei_generator.parser.errors import ValidationError
from .gen.ZmeiLangSimpleLexer import ZmeiLangSimpleLexer
from .gen.ZmeiLangParser import ZmeiLangParser


def parse_file(filename, fail_on_error=True):
    return parse(FileStream(filename), fail_on_error=fail_on_error)


def parse_string(string, fail_on_error=True):
    return parse(InputStream(string), fail_on_error=fail_on_error)


class ExceptionErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ValidationError(line, column, msg)


def parse(stream, fail_on_error=True):
    lexer = ZmeiLangSimpleLexer(stream)
    stream = CommonTokenStream(lexer)
    parser = ZmeiLangParser(stream)
    if fail_on_error:
        parser.addErrorListener(ExceptionErrorListener())

    return parser.col_file()


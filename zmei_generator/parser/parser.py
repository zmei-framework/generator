from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

from zmei_generator.config.domain.collection_set_def import CollectionSetDef
from zmei_generator.generator.utils import handle_parse_exception
from zmei_generator.parser.errors import ValidationError
from zmei_generator.parser.populate import PartsCollectorListener
from zmei_generator.parser.populate_model_extras import ModelExtraListener
from zmei_generator.parser.populate_page_extras import PageExtraListener
from zmei_generator.parser.stats import StatsCollector
from .gen.ZmeiLangSimpleLexer import ZmeiLangSimpleLexer
from .gen.ZmeiLangParser import ZmeiLangParser


class ExceptionErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ValidationError(line, column, msg)


class ZmeiParser(object):
    def __init__(self) -> None:
        super().__init__()

        self.tree = None
        self.walker = ParseTreeWalker()
        self.filename = None
        self.string = None

    def parse_file(self, filename, fail_on_error=True):
        self.filename = filename
        try:
            return self.parse(FileStream(filename), fail_on_error=fail_on_error)

        except ValidationError as e:
            with open(filename, 'r', encoding='utf8') as f:
                config = f.read()
            handle_parse_exception(e, config, 'Error parsing col file ' + filename)

    def parse_string(self, string, fail_on_error=True):
        self.string = string
        try:
            return self.parse(InputStream(string), fail_on_error=fail_on_error)

        except ValidationError as e:
            handle_parse_exception(e, string, 'Error parsing col file')

    def parse(self, stream, fail_on_error=True):
        lexer = ZmeiLangSimpleLexer(stream)
        stream = CommonTokenStream(lexer)
        parser = ZmeiLangParser(stream)
        if fail_on_error:
            parser.addErrorListener(ExceptionErrorListener())

        self.tree = parser.col_file()

        return self.tree

    def populate_collection_set(self, app_name='noname'):
        cs = CollectionSetDef(app_name)

        listener = PartsCollectorListener(cs)
        model_extra_listener = ModelExtraListener(cs)
        page_extra_listener = PageExtraListener(cs)

        self.walker.walk(listener, self.tree)
        cs.post_process()

        self.walker.walk(model_extra_listener, self.tree)

        self.walker.walk(page_extra_listener, self.tree)
        cs.post_process_extras()

        return cs

    def populate_collection_set_and_errors(self, *args, **kwargs):
        try:
            return self.populate_collection_set(*args, **kwargs)

        except ValidationError as e:
            if self.filename:
                with open(self.filename, 'r', encoding='utf8') as f:
                    config = f.read()
                handle_parse_exception(e, config, 'Error processing col file ' + self.filename)
            else:
                config = self.string
                handle_parse_exception(e, config, 'Error processing col file')

    def collect_stats(self, stats_listener):
        self.walker.walk(stats_listener, self.tree)

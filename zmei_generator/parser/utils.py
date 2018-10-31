from textwrap import dedent

from zmei_generator.config.domain.collection_set_def import CollectionSetDef
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.gen.ZmeiLangParserListener import ZmeiLangParserListener


class BaseListener(ZmeiLangParserListener):

    def __init__(self, collection_set: CollectionSetDef) -> None:
        super().__init__()

        self.collection_set = collection_set

    def _get_code(self, ctx):
        if ctx.code_block():
            code = ctx.code_block().getText().strip()[1:-1]
            return dedent(code).strip()
        elif ctx.code_line():
            return dedent(ctx.code_line().PYTHON_CODE().getText()).strip()

    def _get_fields(self, ctx):
        return [x.strip() for x in ctx.field_list_expr().getText().split(',')]

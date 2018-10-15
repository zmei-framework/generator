from zmei_generator.config.domain.collection_set_def import CollectionSetDef
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.gen.ZmeiLangParserListener import ZmeiLangParserListener


class BaseListener(ZmeiLangParserListener):

    def __init__(self, collection_set: CollectionSetDef) -> None:
        super().__init__()

        self.collection_set = collection_set

    def _get_code(self, ctx: ZmeiLangParser.Python_codeContext):
        if ctx.code_block():
            return ctx.code_block().PYTHON_CODE().getText().strip()
        elif ctx.code_line():
            return ctx.code_line().PYTHON_CODE().getText().strip()

    def _get_fields(self, ctx):
        return [x.strip() for x in ctx.field_list_expr().getText().split(',')]

from textwrap import dedent

from zmei_generator.domain.application_def import ApplicationDef
from zmei_generator.parser.gen.ZmeiLangParserListener import ZmeiLangParserListener


class BaseListener(ZmeiLangParserListener):

    def __init__(self, application: ApplicationDef) -> None:
        super().__init__()

        self.application = application

    def _get_code(self, ctx):
        if ctx.code_block():
            code = ctx.code_block().getText().strip()[1:-1]
            return dedent(code).strip()
        elif ctx.code_line():
            return dedent(ctx.code_line().PYTHON_CODE().getText()).strip()

    def _get_fields(self, ctx):
        return [x.strip() for x in ctx.field_list_expr().getText().split(',')]

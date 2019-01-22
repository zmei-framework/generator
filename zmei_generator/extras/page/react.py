from textwrap import dedent

from zmei_generator.config.extras import PageExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class ReactPageExtra(PageExtra):
    def __init__(self, page) -> None:
        super().__init__(page)

        self.react_type = None
        self.area = None
        self.code = None

    def get_required_deps(self):
        return ['py_mini_racer']

    def post_process(self):
        super().post_process()

        self.page.set_html(self.code, react=self.react_type, area=self.area)


class ReactPageExtraParserListener(BaseListener):

    def enterAn_react(self, ctx: ZmeiLangParser.An_reactContext):
        extra = ReactPageExtra(self.page)

        self.collection_set.extras.append(extra)

        extra.react_type = ctx.an_react_type().getText()
        extra.code = self._get_code(ctx)

        extra.area = 'content'
        if ctx.an_react_descriptor():
            extra.area = ctx.an_react_descriptor().id_or_kw().getText()



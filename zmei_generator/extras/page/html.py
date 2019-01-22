from textwrap import dedent

from zmei_generator.config.extras import PageExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class HtmlPageExtra(PageExtra):
    def __init__(self, page) -> None:
        super().__init__(page)

        self.react_type = None
        self.area = None
        self.code = None

    def post_process(self):
        super().post_process()

        self.page.set_html(self.code, area=self.area)


class HtmlPageExtraParserListener(BaseListener):

    def enterAn_html(self, ctx: ZmeiLangParser.An_htmlContext):
        extra = HtmlPageExtra(self.page)
        self.collection_set.extras.append(
            extra
        )
        extra.area = 'content'
        if ctx.an_html_descriptor():
            extra.area = ctx.an_html_descriptor().id_or_kw().getText()

        extra.code = self._get_code(ctx)

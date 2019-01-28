from zmei_generator.domain.extensions import PageExtension
from zmei_generator.contrib.web.extensions.page.block import InlineTemplatePageBlock
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class HtmlPageExtension(PageExtension):
    def __init__(self, page) -> None:
        super().__init__(page)

        self.react_type = None
        self.area = None
        self.code = None

    def post_process(self):
        super().post_process()

        self.page.add_block(
            self.area,
            InlineTemplatePageBlock(f"theme/content.html", {
                'content': self.code
            })
        )



class HtmlPageExtensionParserListener(BaseListener):

    def enterAn_html(self, ctx: ZmeiLangParser.An_htmlContext):
        extension = HtmlPageExtension(self.page)
        self.application.extensions.append(
            extension
        )
        extension.area = 'content'
        if ctx.an_html_descriptor():
            extension.area = ctx.an_html_descriptor().id_or_kw().getText()

        extension.code = self._get_code(ctx)

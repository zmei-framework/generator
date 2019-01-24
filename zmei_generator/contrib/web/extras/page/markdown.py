import markdown

from zmei_generator.domain.extras import PageExtra
from zmei_generator.contrib.web.extras.page.block import InlineTemplatePageBlock
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class MarkdownPageExtra(PageExtra):
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


class MarkdownPageExtraParserListener(BaseListener):

    def enterAn_markdown(self, ctx: ZmeiLangParser.An_markdownContext):
        extra = MarkdownPageExtra(self.page)
        self.collection_set.extras.append(
            extra
        )

        extra.area = 'content'
        if ctx.an_markdown_descriptor():
            extra.area = ctx.an_markdown_descriptor().id_or_kw().getText()

        md = self._get_code(ctx)
        html = markdown.markdown(md)

        extra.code = html



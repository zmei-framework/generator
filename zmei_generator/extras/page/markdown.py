import markdown

from zmei_generator.config.extras import PageExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class MarkdownPageExtra(PageExtra):
    # markdown
    pass


class MarkdownPageExtraParserListener(BaseListener):

    def enterAn_markdown(self, ctx: ZmeiLangParser.An_markdownContext):
        self.collection_set.extras.append(
            MarkdownPageExtra(self.page)
        )

        area = 'content'
        if ctx.an_markdown_descriptor():
            area = ctx.an_markdown_descriptor().id_or_kw().getText()

        md = self._get_code(ctx)
        html = markdown.markdown(md)

        self.page.set_html(html, area=area)

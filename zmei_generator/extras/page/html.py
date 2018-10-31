from textwrap import dedent

from zmei_generator.config.extras import PageExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

class HtmlPageExtra(PageExtra):
    # html
    pass
    
class HtmlPageExtraParserListener(BaseListener):

    def enterAn_html(self, ctx: ZmeiLangParser.An_htmlContext):
        self.collection_set.extras.append(
            HtmlPageExtra(self.page)
        )

        area = 'content'
        if ctx.an_html_descriptor():
            area = ctx.an_html_descriptor().id_or_kw().getText()

        self.page.set_html(self._get_code(ctx), area=area)

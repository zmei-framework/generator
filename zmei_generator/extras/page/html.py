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
        if ctx.an_html_discriminator():
            area = ctx.an_html_discriminator().id_or_kw().getText()

        html = dedent(ctx.code_block().PYTHON_CODE().getText().strip('\n'))
        self.page.set_html(html, area=area)

from textwrap import dedent

from zmei_generator.config.extras import PageExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class ReactPageExtra(PageExtra):
    # react
    pass


class ReactPageExtraParserListener(BaseListener):

    def enterAn_react(self, ctx: ZmeiLangParser.An_reactContext):
        self.collection_set.extras.append(
            ReactPageExtra(self.page)
        )

        area = 'content'
        if ctx.an_react_descriptor():
            area = ctx.an_react_descriptor().id_or_kw().getText()

        self.page.set_html(self._get_code(ctx), react=True, area=area)

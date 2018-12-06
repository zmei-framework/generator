from textwrap import dedent

from zmei_generator.config.extras import PageExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class ReactPageExtra(PageExtra):
    def get_required_deps(self):
        return ['py_mini_racer']


class ReactPageExtraParserListener(BaseListener):

    def enterAn_react(self, ctx: ZmeiLangParser.An_reactContext):
        self.collection_set.extras.append(
            ReactPageExtra(self.page)
        )

        react_type = ctx.an_react_type().getText()

        area = 'content'
        if ctx.an_react_descriptor():
            area = ctx.an_react_descriptor().id_or_kw().getText()

        self.page.set_html(self._get_code(ctx), react=react_type, area=area)

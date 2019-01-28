from zmei_generator.domain.extras import PageExtra
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


class ReactPageExtraParserListener(BaseListener):

    def enterAn_react(self, ctx: ZmeiLangParser.An_reactContext):
        extra = ReactPageExtra(self.page)
        self.application.extras.append(extra)
        extra.react_type = ctx.an_react_type().getText()
        #
        # if self.react:
        #     if 'ZmeiDataViewMixin' in self.extra_bases:
        #         self.extra_bases.remove('ZmeiDataViewMixin')
        #
        #     self.extra_bases.append('ZmeiReactViewMixin')




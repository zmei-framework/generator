from zmei_generator.domain.extensions import PageExtension
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class ReactPageExtension(PageExtension):
    def __init__(self, page) -> None:
        super().__init__(page)

        self.react_type = None
        self.area = None
        self.code = None

    def get_required_deps(self):
        return ['py_mini_racer']


class ReactPageExtensionParserListener(BaseListener):

    def enterAn_react(self, ctx: ZmeiLangParser.An_reactContext):
        extension = ReactPageExtension(self.page)
        self.application.extensions.append(extension)
        extension.react_type = ctx.an_react_type().getText()
        #
        # if self.react:
        #     if 'ZmeiDataViewMixin' in self.extension_bases:
        #         self.extension_bases.remove('ZmeiDataViewMixin')
        #
        #     self.extension_bases.append('ZmeiReactViewMixin')




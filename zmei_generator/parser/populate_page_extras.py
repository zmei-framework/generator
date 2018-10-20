from zmei_generator.config.domain.collection_set_def import CollectionSetDef
from zmei_generator.config.domain.page_def import PageDef
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener
from zmei_generator.extras.page.auth import AuthPageExtraParserListener
from zmei_generator.extras.page.markdown import MarkdownPageExtraParserListener
from zmei_generator.extras.page.react import ReactPageExtraParserListener
from zmei_generator.extras.page.html import HtmlPageExtraParserListener


class PageExtraListener(
    AuthPageExtraParserListener,
    MarkdownPageExtraParserListener,
    ReactPageExtraParserListener,
    HtmlPageExtraParserListener,
    BaseListener
):

    def __init__(self, collection_set: CollectionSetDef) -> None:
        super().__init__(collection_set)

        self.page = None  # type: PageDef

    def enterPage(self, ctx: ZmeiLangParser.PageContext):
        self.page = PageDef(self.collection_set)

    def enterPage_name(self, ctx: ZmeiLangParser.Page_nameContext):
        self.page = self.collection_set.pages[ctx.getText()]

    def exitPage(self, ctx: ZmeiLangParser.PageContext):
        self.page = None




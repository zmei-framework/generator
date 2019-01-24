from zmei_generator.domain.extras import PageExtra
from zmei_generator.contrib.web.extras.page.block import BlockPlaceholder
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class PlaceholderPageExtra(PageExtra):
    def post_process(self):
        super().post_process()

        self.page.add_block('content', BlockPlaceholder())


class PlaceholderPageExtraParserListener(BaseListener):

    def enterPage_priority_marker(self, ctx: ZmeiLangParser.Page_priority_markerContext):
        extra = PlaceholderPageExtra(self.page)
        self.collection_set.extras.append(
            extra
        )

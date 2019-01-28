from zmei_generator.domain.extensions import PageExtension
from zmei_generator.contrib.web.extensions.page.block import BlockPlaceholder
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class PlaceholderPageExtension(PageExtension):
    def post_process(self):
        super().post_process()

        self.page.add_block('content', BlockPlaceholder())


class PlaceholderPageExtensionParserListener(BaseListener):

    def enterAn_priority_marker(self, ctx: ZmeiLangParser.An_priority_markerContext):
        extension = PlaceholderPageExtension(self.page)
        self.application.extensions.append(
            extension
        )

from zmei_generator.config.extras import PageExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class FlutterPageExtra(PageExtra):

    def __init__(self, page) -> None:
        super().__init__(page)

        self.include_child = False


class FlutterPageExtraParserListener(BaseListener):

    def enterAn_flutter(self, ctx: ZmeiLangParser.An_flutterContext):
        extra = FlutterPageExtra(self.page)
        self.collection_set.extras.append(
            extra
        )

        self.set_flutter(self.page, extra)
        self.collection_set.flutter = True

    def enterAn_flutter_child(self, ctx: ZmeiLangParser.An_flutter_childContext):
        if str(ctx.BOOL()) == 'true':
            self.page.flutter.include_child = True

    def set_flutter(self, page, extra):
        page._flutter = extra

        if page.get_parent():
            parent = page.get_parent()
            if not parent._flutter:
                self.set_flutter(parent, extra)

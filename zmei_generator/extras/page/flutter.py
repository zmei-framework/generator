from zmei_generator.config.extras import PageExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class FlutterPageExtra(PageExtra):
    # flutter
    pass


class FlutterPageExtraParserListener(BaseListener):

    def enterAn_flutter(self, ctx: ZmeiLangParser.An_flutterContext):
        extra = FlutterPageExtra(self.page)
        self.collection_set.extras.append(
            extra
        )

        self.set_flutter(self.page, extra)
        self.collection_set.flutter = True

    def enterAn_flutter_child(self, ctx: ZmeiLangParser.An_flutter_childContext):
        if ctx.BOOL().get_text() == 'true':
            pass



    def set_flutter(self, page, extra):
        page.flutter = extra

        if page.get_parent():
            parent = page.get_parent()
            if not parent.flutter:
                self.set_flutter(parent, extra)



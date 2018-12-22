
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

        self.page.flutter = extra
        self.collection_set.flutter = True


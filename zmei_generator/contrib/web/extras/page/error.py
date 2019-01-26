
from zmei_generator.domain.extras import PageExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

class ErrorPageExtra(PageExtra):
    # error
    pass
    
class ErrorPageExtraParserListener(BaseListener):

    def enterAn_error(self, ctx: ZmeiLangParser.An_errorContext):
        self.application.extras.append(
            ErrorPageExtra(self.page)
        )

    def enterAn_error_code(self, ctx: ZmeiLangParser.An_error_codeContext):
        self.page.handlers.append(int(ctx.getText()))


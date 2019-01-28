
from zmei_generator.domain.extensions import PageExtension
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

class ErrorPageExtension(PageExtension):
    # error
    pass
    
class ErrorPageExtensionParserListener(BaseListener):

    def enterAn_error(self, ctx: ZmeiLangParser.An_errorContext):
        self.application.extensions.append(
            ErrorPageExtension(self.page)
        )

    def enterAn_error_code(self, ctx: ZmeiLangParser.An_error_codeContext):
        self.page.handlers.append(int(ctx.getText()))


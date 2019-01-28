
from zmei_generator.domain.extensions import ModelExtension
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

class CleanModelExtension(ModelExtension):
    def get_name(cls):
        return 'clean'
    

class CleanModelExtensionParserListener(BaseListener):

    def enterAn_clean(self, ctx: ZmeiLangParser.An_cleanContext):
        self.application.extensions.append(
            CleanModelExtension(self.model)
        )

        self.model.validators.append(self._get_code(ctx.python_code()))



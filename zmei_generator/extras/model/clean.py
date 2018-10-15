
from zmei_generator.config.extras import ModelExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

class CleanModelExtra(ModelExtra):
    def get_name(cls):
        return 'clean'
    

class CleanModelExtraParserListener(BaseListener):

    def enterAn_clean(self, ctx: ZmeiLangParser.An_cleanContext):
        self.collection_set.extras.append(
            CleanModelExtra(self.model)
        )

        self.model.validators.append(self._get_code(ctx.python_code()))



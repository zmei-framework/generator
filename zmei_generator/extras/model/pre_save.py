
from zmei_generator.config.extras import ModelExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

class PreSaveModelExtra(ModelExtra):
    def get_name(cls):
        return 'pre_save'
    

class PreSaveModelExtraParserListener(BaseListener):

    def enterAn_pre_save(self, ctx: ZmeiLangParser.An_pre_saveContext):
        self.collection_set.extras.append(
            PreSaveModelExtra(self.model)
        )

        self.model.signal_handlers.append(
            (['django.db.models.signals', 'pre_save'], self._get_code(ctx.python_code())))


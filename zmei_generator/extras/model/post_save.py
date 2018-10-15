
from zmei_generator.config.extras import ModelExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

class PostSaveModelExtra(ModelExtra):
    def get_name(cls):
        return 'post_save'
    

class PostSaveModelExtraParserListener(BaseListener):

    def enterAn_post_save(self, ctx: ZmeiLangParser.An_post_saveContext):
        self.collection_set.extras.append(
            PostSaveModelExtra(self.model)
        )

        self.model.signal_handlers.append(
            (['django.db.models.signals', 'post_save'], self._get_code(ctx.python_code())))


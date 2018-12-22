
from zmei_generator.config.extras import ModelExtra
from zmei_generator.extras.model._signals import SignalBaseModelExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

class PreSaveModelExtra(SignalBaseModelExtra):
    def get_name(cls):
        return 'pre_save'
    

class PreSaveModelExtraParserListener(BaseListener):

    def enterAn_pre_save(self, ctx: ZmeiLangParser.An_pre_saveContext):
        self.collection_set.extras.append(
            PreSaveModelExtra(self.model)
        )

        self.model.signal_handlers.append(
            ([
                # ('django_query_signals', 'pre_bulk_create'),
                ('django.db.models.signals', 'pre_save'),
                # ('django_query_signals', 'pre_get_or_create'),
                # ('django_query_signals', 'pre_update_or_create'),
                # ('django_query_signals', 'pre_update'),
            ], self._get_code(ctx.python_code())))


from zmei_generator.contrib.web.extensions.model._signals import SignalBaseModelExtension
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

class PreSaveModelExtension(SignalBaseModelExtension):
    def get_name(cls):
        return 'pre_save'
    

class PreSaveModelExtensionParserListener(BaseListener):

    def enterAn_pre_save(self, ctx: ZmeiLangParser.An_pre_saveContext):
        self.application.extensions.append(
            PreSaveModelExtension(self.model)
        )

        self.model.signal_handlers.append(
            ([
                # ('django_query_signals', 'pre_bulk_create'),
                ('django.db.models.signals', 'pre_save'),
                # ('django_query_signals', 'pre_get_or_create'),
                # ('django_query_signals', 'pre_update_or_create'),
                # ('django_query_signals', 'pre_update'),
            ], self._get_code(ctx.python_code())))


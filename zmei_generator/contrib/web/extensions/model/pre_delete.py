from zmei_generator.contrib.web.extensions.model._signals import SignalBaseModelExtension
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

class PreDeleteModelExtension(SignalBaseModelExtension):
    def get_name(cls):
        return 'pre_delete'
    

class PreDeleteModelExtensionParserListener(BaseListener):

    def enterAn_pre_delete(self, ctx: ZmeiLangParser.An_pre_deleteContext):
        self.application.extensions.append(
            PreDeleteModelExtension(self.model)
        )

        self.model.signal_handlers.append(
            ([
                # ('django_query_signals', 'pre_delete'),
                ('django.db.models.signals', 'pre_delete'),
            ], self._get_code(ctx.python_code())))


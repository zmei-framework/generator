from zmei_generator.contrib.web.extensions.model._signals import SignalBaseModelExtension
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

class PostDeleteModelExtension(SignalBaseModelExtension):

    def get_name(cls):
        return 'post_delete'
    

class PostDeleteModelExtensionParserListener(BaseListener):

    def enterAn_post_delete(self, ctx: ZmeiLangParser.An_post_deleteContext):
        self.application.extensions.append(
            PostDeleteModelExtension(self.model)
        )

        self.model.signal_handlers.append(
            ([
                # ('django_query_signals', 'post_delete'),
                ('django.db.models.signals', 'post_delete'),
            ], self._get_code(ctx.python_code())))


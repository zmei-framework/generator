from zmei_generator.contrib.web.extras.model._signals import SignalBaseModelExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

class PostDeleteModelExtra(SignalBaseModelExtra):

    def get_name(cls):
        return 'post_delete'
    

class PostDeleteModelExtraParserListener(BaseListener):

    def enterAn_post_delete(self, ctx: ZmeiLangParser.An_post_deleteContext):
        self.application.extras.append(
            PostDeleteModelExtra(self.model)
        )

        self.model.signal_handlers.append(
            ([
                # ('django_query_signals', 'post_delete'),
                ('django.db.models.signals', 'post_delete'),
            ], self._get_code(ctx.python_code())))


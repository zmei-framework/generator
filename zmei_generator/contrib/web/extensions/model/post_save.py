from zmei_generator.contrib.web.extensions.model._signals import SignalBaseModelExtension
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

class PostSaveModelExtension(SignalBaseModelExtension):
    def get_name(cls):
        return 'post_save'
    

class PostSaveModelExtensionParserListener(BaseListener):

    def enterAn_post_save(self, ctx: ZmeiLangParser.An_post_saveContext):
        self.application.extensions.append(
            PostSaveModelExtension(self.model)
        )

        self.model.signal_handlers.append(
            ([
                # ('django_query_signals', 'post_bulk_create'),
                ('django.db.models.signals', 'post_save'),
                # ('django_query_signals', 'post_get_or_create'),
                # ('django_query_signals', 'post_update_or_create'),
                # ('django_query_signals', 'post_update'),
            ], self._get_code(ctx.python_code())))


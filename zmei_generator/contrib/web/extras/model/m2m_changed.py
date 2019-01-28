from zmei_generator.contrib.web.extensions.model._signals import SignalBaseModelExtension
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

class M2mChangedModelExtension(SignalBaseModelExtension):
    def get_name(cls):
        return 'm2m_changed'
    

class M2mChangedModelExtensionParserListener(BaseListener):

    def enterAn_m2m_changed(self, ctx: ZmeiLangParser.An_m2m_changedContext):
        self.application.extensions.append(
            M2mChangedModelExtension(self.model)
        )

        self.model.signal_handlers.append(
            (['django.db.models.signals', 'm2m_changed'], self._get_code(ctx.python_code())))


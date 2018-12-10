
from zmei_generator.config.extras import ModelExtra
from zmei_generator.extras.model._signals import SignalBaseModelExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

class M2mChangedModelExtra(SignalBaseModelExtra):
    def get_name(cls):
        return 'm2m_changed'
    

class M2mChangedModelExtraParserListener(BaseListener):

    def enterAn_m2m_changed(self, ctx: ZmeiLangParser.An_m2m_changedContext):
        self.collection_set.extras.append(
            M2mChangedModelExtra(self.model)
        )

        self.model.signal_handlers.append(
            (['django.db.models.signals', 'm2m_changed'], self._get_code(ctx.python_code())))


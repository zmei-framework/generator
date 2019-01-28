import pkg_resources

from zmei_generator.domain.model_def import ModelDef
from zmei_generator.domain.application_def import ApplicationDef
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

parsers = []
for entry_point in pkg_resources.iter_entry_points('zmei.parser.stage2'):
    parsers += entry_point.load()

parsers.append(BaseListener)


class ModelExtensionListener(*parsers):

    def __init__(self, application: ApplicationDef) -> None:
        super().__init__(application)

        self.model = None  # type: ModelDef
        self.model_extend_name = None  # type: ModelDef
        self.model_base_name = None  # type: ModelDef

    def enterCol_name(self, ctx: ZmeiLangParser.Col_nameContext):
        ref = ctx.getText().strip()

        if self.model_extend_name:
            ref = '{}_{}'.format(self.model_base_name, ref)

        self.model = self.application.models[ref]

    def enterCol_base_name(self, ctx: ZmeiLangParser.Col_base_nameContext):
        base = ctx.getText()

        self.model_extend_name = base[-2:] == '~>'
        if self.model_extend_name:
            self.model_base_name = base[:-2].strip()

    def exitCol_name(self, ctx: ZmeiLangParser.Col_nameContext):
        self.model_extend_name = None  # type: ModelDef
        self.model_base_name = None  # type: ModelDef

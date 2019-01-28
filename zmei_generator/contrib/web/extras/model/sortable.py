from zmei_generator.domain.extensions import ModelExtension
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class SortableModelExtension(ModelExtension):
    def get_name(cls):
        return 'sortable'


class SortableModelExtensionParserListener(BaseListener):

    def enterAn_sortable(self, ctx: ZmeiLangParser.An_sortableContext):
        self.application.extensions.append(
            SortableModelExtension(self.model)
        )

        self.model.sortable = True

    def enterAn_sortable_field_name(self, ctx: ZmeiLangParser.An_sortable_field_nameContext):
        self.model.sortable_field = [ctx.getText().strip()]

from zmei_generator.config.extras import ModelExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class SortableModelExtra(ModelExtra):
    def get_name(cls):
        return 'sortable'


class SortableModelExtraParserListener(BaseListener):

    def enterAn_sortable(self, ctx: ZmeiLangParser.An_sortableContext):
        self.collection_set.extras.append(
            SortableModelExtra(self.model)
        )

        self.model.sortable = True

    def enterAn_sortable_field_name(self, ctx: ZmeiLangParser.An_sortable_field_nameContext):
        self.model.sortable_field = [ctx.getText().strip()]

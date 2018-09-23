from zmei_generator.config.domain.collection_def import CollectionDef
from zmei_generator.config.domain.field_def import FieldDef


class ExpressionFieldDef(FieldDef):
    def __init__(self, collection: CollectionDef, field) -> None:
        super().__init__(collection, field)

        self.type_name = 'expr'
        self.read_only = True

        self.expression = None
        self.static = False

        self.boolean = False

    def get_model_field(self):
        return None

    @property
    def admin_list_renderer(self):
        return """
        return obj.%s
        """ % self.name



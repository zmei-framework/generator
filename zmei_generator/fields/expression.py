from zmei_generator.config.domain.collection_def import CollectionDef
from zmei_generator.config.domain.field_def import FieldDef


class ExpressionFieldDef(FieldDef):
    def __init__(self, collection: CollectionDef, field) -> None:
        super().__init__(collection, field)

        self.type_name = 'expr'
        self.read_only = True
        if field.calculated_static_expression:
            self.expression = field.calculated_static_expression
            self.static = True
        else:
            self.expression = field.calculated_expression
            self.static = False

        self.boolean = False

        if self.expression[0] == '!':
            self.expression = self.expression[1:]
            self.boolean = True

    def get_model_field(self, collection: CollectionDef):
        return None

    @property
    def admin_list_renderer(self):
        return """
        return obj.%s
        """ % self.name



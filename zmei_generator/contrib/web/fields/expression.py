from zmei_generator.domain.model_def import ModelDef
from zmei_generator.domain.field_def import FieldDef


class ExpressionFieldDef(FieldDef):
    def __init__(self, model: ModelDef, field) -> None:
        super().__init__(model, field)

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



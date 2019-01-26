from zmei_generator.domain.model_def import ModelDef
from zmei_generator.domain.application_def import FieldDeclaration
from zmei_generator.domain.field_def import FieldDef, FieldConfig


class CustomFieldDef(FieldDef):
    def __init__(self, model: ModelDef, field: FieldConfig) -> None:
        super().__init__(model, field)

        self.custom_declaration = None

    def get_model_field(self):
        return FieldDeclaration(
            [], self.custom_declaration
        )

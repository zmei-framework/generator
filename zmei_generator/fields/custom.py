from zmei_generator.config.domain.collection_def import CollectionDef
from zmei_generator.config.domain.collection_set_def import FieldDeclaration
from zmei_generator.config.domain.field_def import FieldDef, FieldConfig


class CustomFieldDef(FieldDef):
    def __init__(self, collection: CollectionDef, field: FieldConfig) -> None:
        super().__init__(collection, field)

        self.custom_declaration = None

    def get_model_field(self):
        return FieldDeclaration(
            [], self.custom_declaration
        )

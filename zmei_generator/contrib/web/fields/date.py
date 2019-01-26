from zmei_generator.domain.model_def import ModelDef
from zmei_generator.domain.application_def import FieldDeclaration
from zmei_generator.domain.field_def import FieldDef, FieldConfig
from zmei_generator.generator.utils import gen_args


class DateFieldDef(FieldDef):
    def get_model_field(self):
        args = self.prepare_field_arguemnts()

        return FieldDeclaration(
            [('django.db', 'models')],
            'models.DateField({})'.format(gen_args(args))
        )


class DateTimeFieldDef(FieldDef):

    def get_flutter_field(self):
        return 'DateTime'

    def get_flutter_from_json(self, name):
        return f'DateTime.parse(data[\'{name}\'])'

    def get_model_field(self):
        args = self.prepare_field_arguemnts()

        return FieldDeclaration(
            [('django.db', 'models')],
            'models.DateTimeField({})'.format(gen_args(args))
        )


class AutoNowDateTimeFieldDef(DateTimeFieldDef):

    def __init__(self, model: ModelDef, field: FieldConfig) -> None:
        super().__init__(model, field)

        self.read_only = True

    def prepare_field_arguemnts(self, own_args=None):
        args = super().prepare_field_arguemnts(own_args)
        args['auto_now'] = True
        return args


class AutoNowAddDateTimeFieldDef(DateTimeFieldDef):

    def __init__(self, model: ModelDef, field: FieldConfig) -> None:
        super().__init__(model, field)

        self.read_only = True

    def prepare_field_arguemnts(self, own_args=None):
        args = super().prepare_field_arguemnts(own_args)
        args['auto_now_add'] = True
        return args

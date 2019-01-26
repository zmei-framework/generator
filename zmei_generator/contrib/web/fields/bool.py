from zmei_generator.domain.application_def import FieldDeclaration
from zmei_generator.domain.field_def import FieldDef
from zmei_generator.generator.utils import gen_args


class BooleanFieldDef(FieldDef):
    """
    Boolean field

    bool([default value])
    """

    default = False

    def get_flutter_field(self):
        return 'bool'

    def get_model_field(self):
        args = self.prepare_field_arguemnts({'default': self.default})

        if 'null' in args:
            del args['null']

        return FieldDeclaration(
            [('django.db', 'models')],
            'models.BooleanField({})'.format(gen_args(args))
        )
from zmei_generator.config.domain.collection_set_def import FieldDeclaration
from zmei_generator.config.domain.field_def import FieldDef
from zmei_generator.generator.utils import gen_args
from cPyparsing import *

class BooleanFieldDef(FieldDef):
    """
    Boolean field

    bool([default value])
    """

    default = False

    def get_model_field(self, collection):
        args = self.prepare_field_arguemnts({'default': self.default == 'true'})

        if 'null' in args:
            del args['null']

        return FieldDeclaration(
            [('django.db', 'models')],
            'models.BooleanField({})'.format(gen_args(args))
        )
from cratis_generator.config.domain.collection_set_def import FieldDeclaration
from cratis_generator.config.domain.field_def import FieldDef
from cratis_generator.generator.utils import gen_args
from cPyparsing import *

class BooleanFieldDef(FieldDef):
    """
    Boolean field

    bool([default value])
    """

    default = False

    def parse_options(self):
        if self.options:
            options_grammar = oneOf('true false').setResultsName('default') + stringEnd

            result = options_grammar.parseString(self.options)

            if result.default:
                self.default = result.default


    def get_model_field(self, collection):
        args = self.prepare_field_arguemnts({'default': self.default == 'true'})

        if 'null' in args:
            del args['null']

        return FieldDeclaration(
            [('django.db', 'models')],
            'models.BooleanField({})'.format(gen_args(args))
        )
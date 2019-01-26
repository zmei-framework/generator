from zmei_generator.domain.application_def import FieldDeclaration
from zmei_generator.domain.field_def import FieldDef
from zmei_generator.generator.utils import gen_args


class IntegerFieldDef(FieldDef):

    choices = None

    def get_flutter_field(self):
        return 'int'

    def get_model_field(self):
        args = self.prepare_field_arguemnts()

        if self.choices:
            args['choices'] = self.choices

        return FieldDeclaration(
            [('django.db', 'models')],
            'models.IntegerField({})'.format(gen_args(args))
        )


class FloatFieldDef(FieldDef):

    def get_flutter_field(self):
        return 'double'

    def get_model_field(self):
        args = self.prepare_field_arguemnts()

        return FieldDeclaration(
            [('django.db', 'models')],
            'models.FloatField({})'.format(gen_args(args))
        )


class DecimalFieldDef(FieldDef):

    positive = False

    def get_flutter_field(self):
        return 'double'

    def parse_options(self):
        if isinstance(self.options, str) and self.options.strip() != '':
            self.positive = self.options.strip() == '+'

    def get_model_field(self):
        imports = [('django.db', 'models')]

        own_args = {'max_digits': 15, 'decimal_places': 2, }

        if self.positive:
            imports.append(
                ('django.core.validators', 'MinValueValidator')
            )
            imports.append(
                ('decimal', 'Decimal')
            )
            own_args['validators'] = '[MinValueValidator(Decimal("0.00"))]'

        args = self.prepare_field_arguemnts(own_args)

        return FieldDeclaration(
            imports,
            'models.DecimalField({})'.format(gen_args(args, raw_args=['validators']))
        )

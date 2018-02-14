import re

from cratis_generator.config.domain import FieldDef, FieldDeclaration
from cratis_generator.config.grammar import choices
from cratis_generator.generator.utils import gen_args, handle_parse_exception
from pyparsing import *


class IntegerFieldDef(FieldDef):

    choices = None

    def parse_options(self):

        field_opts = Optional(Suppress('choices') + Suppress(':') + choices) + stringEnd

        if isinstance(self.options, str) and self.options.strip() != '':
            try:
                opts = field_opts.parseString(self.options)

                if opts.choices:
                    choice_list = []
                    for x in opts.choices:
                        value = int(x.value)
                        label = x.label or x.value
                        choice_list.append((value, label))
                    self.choices = tuple(choice_list)

            except ParseException as e:
                handle_parse_exception(e, self.options,
                                       'Can not parse options for field "{}" for collection "{}"'.format(self.name, self.collection.ref))

    def get_model_field(self, collection):
        args = self.prepare_field_arguemnts()

        if self.choices:
            args['choices'] = self.choices

        return FieldDeclaration(
            [('django.db', 'models')],
            'models.IntegerField({})'.format(gen_args(args))
        )


class FloatFieldDef(FieldDef):
    def get_model_field(self, collection):
        args = self.prepare_field_arguemnts()

        return FieldDeclaration(
            [('django.db', 'models')],
            'models.FloatField({})'.format(gen_args(args))
        )


class DecimalFieldDef(FieldDef):
    def get_model_field(self, collection):
        args = self.prepare_field_arguemnts({
            'max_digits': 15,
            'decimal_places': 2,
        })

        return FieldDeclaration(
            [('django.db', 'models')],
            'models.DecimalField({})'.format(gen_args(args))
        )

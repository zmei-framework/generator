import glob
import re

from cratis_generator.config.domain.collection_set_def import FieldDeclaration
from cratis_generator.config.domain.exceptions import ValidationException
from cratis_generator.config.domain.field_def import FieldDef
from cratis_generator.generator.utils import gen_args, handle_parse_exception
from cratis_generator.config.grammar import choices, choices_or_glob

from cPyparsing import *


class DefaultTextMixin(FieldDef):
    def prepare_field_arguemnts(self, own_args=None):

        args = super().prepare_field_arguemnts(own_args)
        if not self.required and 'required' not in args:
            args['default'] = ''

        return args


class TextFieldDef(DefaultTextMixin, FieldDef):
    max_length = 100
    choices = None

    def parse_options(self):

        field_opts = (Word(nums)|Literal('?')).setResultsName('length') + Optional(Suppress(',') + Suppress('choices') + Suppress(':') + choices_or_glob) + stringEnd

        if isinstance(self.options, str) and self.options.strip() != '':
            try:
                opts = field_opts.parseString(self.options)

                if opts.choices:
                    choice_list = []
                    for x in opts.choices:
                        value = x.value
                        label = x.label or x.value
                        choice_list.append((value, label))
                    self.choices = tuple(choice_list)

                if opts.glob_expr:
                    self.choices = self.choices_by_glob(opts.glob_expr)

                if opts.length != '?':
                    self.max_length = int(opts.length)
                else:
                    if len(self.choices):
                        self.max_length = max([len(value) for value, label in self.choices])
                    else:
                        raise ParseException('Auto-length "?" may be used only with "choices:"')

            except ParseException as e:
                handle_parse_exception(e, self.options,
                                       'Can not parse options for field "{}" for collection "{}"'.format(self.name, self.collection.ref))

    def choices_by_glob(self, glob_expr):
        match = re.match('^([^\{]+)\{([^\}]+)\}$', glob_expr)

        if not match:
            raise ParseException('Can not parse glob expression: {}'.format(glob_expr))

        prefix = match.group(1)
        expr = match.group(2)
        prefix_len = len(prefix)

        choices = []
        glob_expr = prefix + expr

        for filename in glob.iglob(glob_expr, recursive=True):
            if filename.startswith(prefix):
                val = filename[prefix_len:]
                choices.append((val, val))

        if not len(choices):
            raise ParseException('glob expression did not match any files: {}'.format(glob_expr))

        return choices



    def get_model_field(self, collection):
        args = self.prepare_field_arguemnts({'max_length': self.max_length})

        if self.choices:
            args['choices'] = self.choices

        return FieldDeclaration(
            [('django.db', 'models')],
            'models.CharField({})'.format(gen_args(args))
        )


class SlugFieldDef(DefaultTextMixin, FieldDef):
    field_names = []

    def parse_options(self):
        if isinstance(self.options, str) and self.options.strip() != '':
            self.field_names = tuple([x.strip() for x in self.options.split(',')])
        else:
            raise ValidationException('Slug field "{}" argument should be names of another fields in same collection separated by ","'.format(self.name))

    def get_model_field(self, collection):
        max_len = 0

        for field_name in self.field_names:
            if field_name not in collection.all_and_inherited_fields_map:
                raise ValidationException(
                    'Slug field "{}" can not find field "{}" in the collection'.format(self.name, field_name))

            target_field = collection.all_and_inherited_fields_map[field_name]

            if not isinstance(target_field, TextFieldDef):
                raise ValidationException(
                    'Slug field "{}" target field is not of type text()'.format(self.name))

            max_len += target_field.max_length

        args = self.prepare_field_arguemnts({'max_length': max_len})

        return FieldDeclaration(
            [('django.db', 'models')],
            'models.SlugField({})'.format(gen_args(args))
        )

    def get_prepopulated_from(self):
        return self.field_names


class LongTextFieldDef(DefaultTextMixin, FieldDef):
    def get_model_field(self, collection):
        args = self.prepare_field_arguemnts()

        return FieldDeclaration(
            [('django.db', 'models')],
            'models.TextField({})'.format(gen_args(args))
        )


class RichTextFieldDef(DefaultTextMixin, FieldDef):
    def get_model_field(self, collection):
        args = self.prepare_field_arguemnts()

        return FieldDeclaration(
            [('ckeditor_uploader.fields', 'RichTextUploadingField')],
            'RichTextUploadingField({})'.format(gen_args(args))
        )


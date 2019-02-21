from zmei_generator.domain.application_def import FieldDeclaration
from zmei_generator.domain.model_def import ModelDef
from zmei_generator.parser.errors import GlobalScopeValidationError as ValidationException
from zmei_generator.domain.field_def import FieldDef, FieldConfig
from zmei_generator.generator.utils import gen_args


class DefaultTextMixin(FieldDef):

    def get_flutter_field(self):
        return 'String'

    def prepare_field_arguemnts(self, own_args=None):
        args = super().prepare_field_arguemnts(own_args)

        if not self.extension_args_append and self.extension_args:
            return args

        # if not self.required and 'required' not in args:
        #     args['default'] = ''

        return args


class TextFieldDef(DefaultTextMixin, FieldDef):
    max_length = 100
    choices = None

    def get_model_field(self):
        args = self.prepare_field_arguemnts({'max_length': self.max_length})

        if self.choices:
            args['choices'] = self.choices

        return FieldDeclaration(
            [('django.db', 'models')],
            'models.CharField({})'.format(gen_args(args))
        )


class SlugFieldDef(DefaultTextMixin, FieldDef):

    def __init__(self, model: ModelDef, field: FieldConfig) -> None:
        super().__init__(model, field)

        self.field_names = []

    def parse_options(self):
        if isinstance(self.options, str) and self.options.strip() != '':
            self.field_names = tuple([x.strip() for x in self.options.split(',')])
        else:
            raise ValidationException(
                'Slug field "{}" argument should be names of another fields in same model separated by ","'.format(
                    self.name))

    def get_model_field(self):
        max_len = 0

        # TODO: get validation back
        # for field_name in self.field_names:
        #
        #     if field_name not in self.model.all_and_inherited_fields_map:
        #         raise ValidationException(
        #             'Slug field "{}" can not find field "{}" in the model'.format(self.name, field_name))
        #
        #     target_field = self.model.all_and_inherited_fields_map[field_name]
        #
        #     if not isinstance(target_field, TextFieldDef):
        #         raise ValidationException(
        #             'Slug field "{}" target field is not of type text()'.format(self.name))
        #
        #     max_len += target_field.max_length

        args = self.prepare_field_arguemnts({'max_length': 100})

        return FieldDeclaration(
            [('django.db', 'models')],
            'models.SlugField({})'.format(gen_args(args))
        )

    def get_prepopulated_from(self):
        return self.field_names


class LongTextFieldDef(DefaultTextMixin, FieldDef):
    def get_model_field(self):
        args = self.prepare_field_arguemnts()

        return FieldDeclaration(
            [('django.db', 'models')],
            'models.TextField({})'.format(gen_args(args))
        )


class RichTextFieldDef(DefaultTextMixin, FieldDef):
    def get_model_field(self):
        args = self.prepare_field_arguemnts()

        return FieldDeclaration(
            [('ckeditor.fields', 'RichTextField')],
            'RichTextField({})'.format(gen_args(args))
        )

    def get_required_deps(self):
        return ['django-ckeditor']

    def get_required_apps(self):
        return ['ckeditor']

    def get_required_settings(self):
        return {
            'CKEDITOR_UPLOAD_PATH': 'uploads/'
        }


class RichTextFieldWithUploadDef(DefaultTextMixin, FieldDef):
    def get_model_field(self):
        args = self.prepare_field_arguemnts()

        return FieldDeclaration(
            [('ckeditor_uploader.fields', 'RichTextUploadingField')],
            'RichTextUploadingField({})'.format(gen_args(args))
        )

    def get_required_deps(self):
        return ['django-ckeditor', 'Pillow']

    def get_required_apps(self):
        return ['ckeditor', 'ckeditor_uploader']

    def get_required_settings(self):
        return {
            'CKEDITOR_UPLOAD_PATH': 'uploads/'
        }

    def get_required_urls(self):
        return [
            (None, "url(r'^ckeditor/', include('ckeditor_uploader.urls')),")
        ]

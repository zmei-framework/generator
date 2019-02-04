from zmei_generator.domain.extensions import Extendable
from zmei_generator.domain.model_def import ModelDef


class FieldConfig(object):
    type_name = None
    name = None
    verbose_name = None
    field_help = None
    required = None
    not_null = None
    unique = None
    index = None
    display_field = None
    translatable = None
    comment = None
    type_opts = {}


class FieldDef(Extendable):
    def __init__(self, model: ModelDef, field: FieldConfig) -> None:
        super().__init__()

        self.field_config = field

        self.model = model

        self.type_name = field.type_name
        self.name = None
        self.verbose_name = None
        self.help = None
        self.required = None
        self.not_null = None
        self.unique = None
        self.index = None
        self.display_field = None
        self.translatable = None
        self.comment = None

        self.read_only = False
        self.inline = False
        self.extension_args = None
        self.extension_args_append = False

        self.options = None

    def load_field_config(self):

        field = self.field_config

        self.name = field.name
        self.verbose_name = field.verbose_name
        self.help = field.field_help
        self.required = field.required
        self.not_null = field.not_null
        self.unique = field.unique
        self.index = field.index
        self.display_field = field.display_field
        self.translatable = field.translatable
        self.comment = field.comment.strip() if field.comment else None

        if self.translatable:
            self.model.translatable = True
            self.model.application.translatable = True

        self.options = field.type_opts

    def post_process(self):
        pass

    def prepare_field_arguemnts(self, own_args=None):
        if not self.extension_args_append and self.extension_args:
            return {'_': self.extension_args}

        args = {}

        if self.verbose_name:
            args['verbose_name'] = self.verbose_name
        else:
            args['verbose_name'] = self.name.replace('_', ' ').capitalize()

        if self.help:
            args['help_text'] = self.help

        if not self.not_null:
            args['null'] = True

        args['blank'] = not self.required

        if self.unique:
            args['unique'] = True

        if self.index:
            args['db_index'] = True

        if own_args:
            args.update(own_args)

        if self.extension_args:
            args['_'] = self.extension_args

        return args

    def parse_options(self):
        self.options = {}

    def get_model_field(self):
        raise NotImplementedError('Field "{}" ({}) is not yet implemented.'.format(self.type_name, type(self)))

    def get_flutter_field(self):
        return 'dynamic'

    def get_flutter_from_json(self, name):
        return f"data['{name}']"

    def get_admin_widget(self):
        return None

    def get_prepopulated_from(self):
        return None

    def get_rest_field(self):
        return None

    def get_rest_inline_model(self):
        return None

    def get_required_apps(self):
        return []

    def get_required_deps(self):
        return []

    def get_required_settings(self):
        return {}

    def get_required_urls(self):
        return []

    @property
    def admin_list_renderer(self):
        return None

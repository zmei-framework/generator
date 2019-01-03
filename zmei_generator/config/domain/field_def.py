from zmei_generator.config.domain.collection_def import CollectionDef


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


class FieldDef(object):
    def __init__(self, collection: CollectionDef, field: FieldConfig) -> None:
        super().__init__()

        self.type_name = field.type_name
        self.name = field.name
        self.verbose_name = field.verbose_name
        self.help = field.field_help

        self.collection = collection
        self.required = field.required
        self.not_null = field.not_null
        self.unique = field.unique
        self.index = field.index
        self.display_field = field.display_field
        self.translatable = field.translatable
        self.comment = field.comment.strip() if field.comment else None

        self.read_only = False

        self.inline = False

        self.extra_args = None
        self.extra_args_append = False

        if self.translatable:
            collection.translatable = True
            collection.collection_set.translatable = True

        self.options = field.type_opts

    def post_process(self):
        pass

    def prepare_field_arguemnts(self, own_args=None):
        if not self.extra_args_append and self.extra_args:
            return {'_': self.extra_args}

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

        if self.extra_args:
            args['_'] = self.extra_args

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

    def get_rest_inline_collection(self):
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

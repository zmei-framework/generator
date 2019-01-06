from zmei_generator.config.domain.no_model_field import NoModelField


class ReferenceField(object):
    def __init__(self, collection, target_collection, name: str, source_field) -> None:
        super().__init__()

        self.target_collection = target_collection

        self.type_name = 'ref'
        self.name = name
        self.source_field = source_field
        self.source_field_name = source_field.name

        self.collection = collection
        self.display_field = False
        self.translatable = False

        self.options = {}

        self.inline = False

    def get_flutter_field(self):
        if self.target_collection:
            return f'List<{self.target_collection.class_name}>'
        else:
            return 'dynamic'

    def get_flutter_from_json(self, name):
        if self.target_collection:
            return f'data[\'{name}\'].map<{self.target_collection.class_name}>((item) => {self.target_collection.class_name}.fromJson(item)).toList()'
        else:
            return f'data[\'{name}\']'

    def post_process(self):
        pass

    def parse_options(self):
        pass

    def get_model_field(self, collection):
        raise NoModelField()

    def get_admin_widget(self):
        return None

    def get_prepopulated_from(self):
        return None

    def get_rest_field(self):
        return None

    def get_rest_inline_collection(self):
        return self.target_collection

    def get_required_apps(self):
        return []

    def get_required_deps(self):
        return []

    def get_required_settings(self):
        return {}

    def get_required_urls(self):
        return []

    @property
    def is_many(self):
        return self.source_field.is_many_reverse

    @property
    def admin_list_renderer(self):
        return None



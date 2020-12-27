import hcl2
from zmei_generator.generator.utils import handle_parse_exception
from zmei_generator.parser.errors import ValidationError
from .parser import ZmeiParser
from ..contrib.web.fields.text import TextFieldDef
from ..domain.field_def import FieldConfig
from ..domain.model_def import ModelDef


class HclParser(ZmeiParser):
    def __init__(self) -> None:
        super().__init__()

        self.tree = None
        self.filename = None
        self.string = None

    def parse_file(self, filename, fail_on_error=True):
        self.filename = filename
        try:
            with open(filename, "r") as f:
                return self.parse(hcl2.load(f), fail_on_error=fail_on_error)

        except ValidationError as e:
            with open(filename, 'r', encoding='utf8') as f:
                config = f.read()
            handle_parse_exception(e, config, 'Error parsing hcl file ' + filename)

    def parse_string(self, string, fail_on_error=True):
        self.string = string
        try:
            return self.parse(hcl2.loads(string), fail_on_error=fail_on_error)

        except ValidationError as e:
            handle_parse_exception(e, string, 'Error parsing hcl file')

    def parse(self, stream, fail_on_error=True):
        self.tree = stream
        print(self.tree)

    def process_page_extensions(self, app):
        # page_extension_listener = PageExtensionListener(app)
        # self.walker.walk(page_extension_listener, self.tree)
        pass

    def process_model_extensions(self, app):
        # model_extension_listener = ModelExtensionListener(app)
        # self.walker.walk(model_extension_listener, self.tree)
        pass

    def process_application(self, app):

        models = [(list(x.keys())[0], list(x.values())[0]) for x in self.tree.get('model', [])]

        for name, config in models:
            model = ModelDef(app)
            model.ref = name
            model.short_ref = name
            model.name = ' '.join(name.split('_')).capitalize()

            for field_name, field_config in config.items():
                cfg = FieldConfig()
                cfg.name = field_name
                field = TextFieldDef(model, cfg)
                field.load_field_config()

                model.fields[field.name] = field

            app.models[model.ref] = model

import hcl2
from attr import dataclass

from zmei_generator.generator.utils import handle_parse_exception
from zmei_generator.parser.errors import ValidationError
from .parser import ZmeiParser
from ..contrib.web.fields.bool import BooleanFieldDef
from ..contrib.web.fields.expression import ExpressionFieldDef
from ..contrib.web.fields.text import TextFieldDef, LongTextFieldDef, \
    RichTextFieldDef, RichTextFieldWithUploadDef
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

        def normalize_argument(data):
            if isinstance(data, dict):
                return {key: normalize_argument(val) for key, val in data.items()}

            if isinstance(data, (list, tuple)):
                return [normalize_argument(val) for val in data]

            if isinstance(data, str):
                if data.startswith("${") and data.endswith("}"):
                    return data[2:-1]

            return data

        class FieldParser(object):
            pass

        class StrFieldParser(FieldParser):
            def __init__(self, *args):
                self.len = None
                self.options = {}

                for arg in args:
                    if isinstance(arg, int):
                        self.len = arg
                    elif isinstance(arg, dict):
                        self.options = normalize_argument(arg)
                    else:
                        raise TypeError("Argument of unknown type")

            def parse(self, model, config):
                field = TextFieldDef(model, config)

                choices = self.options.get("choices")

                if self.len:
                    field.max_length = self.len
                else:
                    if choices:
                        field.max_length = max([len(x) for x in choices])
                    else:
                        field.max_length = 100

                if choices:
                    if isinstance(choices, dict):
                        field.choices = tuple([(key, val) for key, val in choices.items()])
                    else:
                        field.choices = tuple([(val, val) for val in choices])

                print(choices)

                field.load_field_config()

                return field

        @dataclass
        class BoolFieldParser(FieldParser):
            default: bool = False

            def parse(self, model, config):
                field = BooleanFieldDef(model, config)
                field.default = self.default
                field.load_field_config()

                return field

        def simple_field(cls):
            class SimpleFieldParser(FieldParser):
                def parse(self, model, config):
                    field = cls(model, config)
                    field.load_field_config()

                    return field

            return SimpleFieldParser

        def expr(source):
            return eval(source, {}, {
                "str": StrFieldParser,
                "bool": BoolFieldParser,
                "text": simple_field(LongTextFieldDef),
                "html": simple_field(RichTextFieldDef),
                "html_media": simple_field(RichTextFieldWithUploadDef),
            })

        models = [(list(x.keys())[0], list(x.values())[0]) for x in self.tree.get('model', [])]

        for name, config in models:
            model = ModelDef(app)
            model.ref = name
            model.short_ref = name
            model.name = ' '.join(name.split('_')).capitalize()

            for field_name, field_config in config.items():
                cfg = FieldConfig()
                cfg.name = field_name

                source = field_config[0]
                if source.startswith("${") and source.endswith("}"):
                    source = expr(source[2:-1])

                if isinstance(source, (str, int, bool)):
                    field = ExpressionFieldDef(model, cfg)
                    field.expression = repr(source)
                    field.load_field_config()

                # field parser type is
                else:
                    field_parser = source
                    if isinstance(field_parser, type):
                        field_parser = field_parser()

                    if not isinstance(field_parser, FieldParser):
                        raise GeneratorExit(
                            f"Unknown field type: {name} -> {field_name}")

                    field = field_parser.parse(model=model, config=cfg)
                    field.load_field_config()

                model.fields[field.name] = field

            app.models[model.ref] = model

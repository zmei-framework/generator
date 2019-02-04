from zmei_generator.contrib.web.extensions.application.langs import LangsAppExtension
from zmei_generator.contrib.web.fields.custom import CustomFieldDef
from zmei_generator.contrib.web.fields.expression import ExpressionFieldDef
from zmei_generator.contrib.web.fields.text import TextFieldDef
from zmei_generator.domain.model_def import ModelDef
from zmei_generator.domain.application_def import ApplicationDef
from zmei_generator.domain.field_def import FieldConfig
from zmei_generator.parser.errors import LangsRequiredValidationError
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class ModelParserListener(BaseListener):
    def __init__(self, application: ApplicationDef) -> None:
        super().__init__(application)

        self.model = None  # type: ModelDef
        self.field = None  # type
        self.field_config = None  # type: FieldConfig

    ############################################
    # Model
    ############################################

    def enterCol(self, ctx: ZmeiLangParser.ColContext):
        self.model = ModelDef(self.application)

    def enterCol_name(self, ctx: ZmeiLangParser.Col_nameContext):
        ref = ctx.getText().strip()
        if self.model.extend_name:
            self.model.ref = '{}_{}'.format(self.model.parent.ref, ref)
        else:
            self.model.ref = ref

        self.model.short_ref = ref
        self.model.name = ' '.join(ref.split('_')).capitalize()

    def enterCol_base_name(self, ctx: ZmeiLangParser.Col_base_nameContext):
        base = ctx.getText()
        separator = base[-2:]
        base = base[:-2].strip()

        self.model.extend_name = separator == '~>'

        self.model.set_parent(base)

    def enterCol_verbose_name(self, ctx: ZmeiLangParser.Col_verbose_nameContext):
        name = ctx.getText()[1:].strip()
        if '/' in name:
            name, plural = name.split('/')
            name = name.strip(' "\'')
            plural = plural.strip(' "\'')

            self.model.name_plural = plural

        self.model.name = name.strip(' "\'')

    def enterCol_str_expr(self, ctx: ZmeiLangParser.Col_str_exprContext):
        self.model.to_string = ctx.getText().strip()[2:-1].strip()

    def exitCol(self, ctx: ZmeiLangParser.ColContext):
        self.application.models[self.model.ref] = self.model
        self.model = None

    ############################################
    # Model field
    ############################################

    def enterCol_field(self, ctx: ZmeiLangParser.Col_fieldContext):
        self.field_config = FieldConfig()

    def enterCol_field_verbose_name(self, ctx: ZmeiLangParser.Col_field_verbose_nameContext):
        self.field_config.verbose_name = ' '.join([x.getText() for x in ctx.string_or_quoted().children]).strip('"\' ')

    def enterCol_field_help_text(self, ctx: ZmeiLangParser.Col_field_help_textContext):
        self.field_config.field_help = ' '.join([x.getText() for x in ctx.string_or_quoted().children]).strip('"\' ')

    def enterCol_modifier(self, ctx: ZmeiLangParser.Col_modifierContext):
        m = ctx.getText()
        if m == "$":
            if not self.application.supports(LangsAppExtension):
                raise LangsRequiredValidationError(ctx.start)

            self.field_config.translatable = True
        elif m == "!":
            self.field_config.index = True
        elif m == "=":
            self.field_config.display_field = True
        elif m == "*":
            self.field_config.required = True
        elif m == "~":
            self.field_config.not_null = True
        elif m == "&":
            self.field_config.unique = True

    def enterCol_field_name(self, ctx: ZmeiLangParser.Col_field_nameContext):
        self.field_config.name = ctx.getText().strip()

    def exitCol_field(self, ctx: ZmeiLangParser.Col_fieldContext):
        if not self.field:
            self.field = TextFieldDef(self.model, self.field_config)

        self.field.load_field_config()

        self.model.fields[self.field.name] = self.field
        self.field = None
        self.field_config = None

    # Calculated field

    def enterCol_field_expr(self, ctx: ZmeiLangParser.Col_field_exprContext):
        self.field = ExpressionFieldDef(self.model, self.field_config)

    def enterCol_field_expr_marker(self, ctx: ZmeiLangParser.Col_field_expr_markerContext):
        marker = ctx.getText().strip()
        if marker == '@=':
            self.field.static = True

    def enterCol_feild_expr_code(self, ctx: ZmeiLangParser.Col_feild_expr_codeContext):
        expr = ctx.getText().strip()

        if expr[0] == '!':
            expr = expr[1:].strip()
            self.field.boolean = True

        self.field.expression = expr

    def enterCol_field_extend_append(self, ctx: ZmeiLangParser.Col_field_extend_appendContext):
        self.field.extension_args_append = True

    def enterCol_field_extend(self, ctx: ZmeiLangParser.Col_field_extendContext):
        self.field.extension_args = self._get_code(ctx)

    # Custom

    def enterCol_field_custom(self, ctx: ZmeiLangParser.Col_field_customContext):
        self.field = CustomFieldDef(self.model, self.field_config)
        self.field.custom_declaration = self._get_code(ctx)

from zmei_generator.config.domain.collection_def import CollectionDef
from zmei_generator.config.domain.collection_set_def import CollectionSetDef
from zmei_generator.config.domain.field_def import FieldConfig
from zmei_generator.config.domain.page_def import PageDef, PageFunction
from zmei_generator.config.domain.page_expression import PageExpression
from zmei_generator.extras.collection_set.celery import CeleryCsExtraParserListener
from zmei_generator.extras.collection_set.channels import ChannelsCsExtraParserListener
from zmei_generator.extras.collection_set.docker import DockerCsExtraParserListener
from zmei_generator.extras.collection_set.file import FileCsExtraParserListener
from zmei_generator.extras.collection_set.filer import FilerCsExtraParserListener
from zmei_generator.extras.collection_set.gitlab import GitlabCsExtraParserListener
from zmei_generator.extras.collection_set.langs import LangsCsExtraParserListener
from zmei_generator.extras.collection_set.suit import SuitCsExtra
from zmei_generator.extras.model.admin import AdminExtra, AdminInlineConfig
from zmei_generator.fields.bool import BooleanFieldDef
from zmei_generator.fields.custom import CustomFieldDef
from zmei_generator.fields.date import DateFieldDef, DateTimeFieldDef, AutoNowDateTimeFieldDef, \
    AutoNowAddDateTimeFieldDef
from zmei_generator.fields.expression import ExpressionFieldDef
from zmei_generator.fields.filer import FilerImageFieldDef, FilerFileFieldDef, FilerFileFolderDef, \
    FilerImageFolderFieldDef, ImageSize
from zmei_generator.fields.image import ImageFieldDef, SimpleFieldDef
from zmei_generator.fields.number import IntegerFieldDef, FloatFieldDef, DecimalFieldDef
from zmei_generator.fields.relation import RelationOneDef, RelationOne2OneDef, RelationManyDef
from zmei_generator.fields.text import TextFieldDef, SlugFieldDef, LongTextFieldDef, RichTextFieldDef, \
    RichTextFieldWithUploadDef
from zmei_generator.parser.errors import TabsSuitRequiredValidationError, LangsRequiredValidationError
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.populate_page_crud_overrides import PageCrudOverrideExtraListener
from zmei_generator.parser.utils import BaseListener


class PartsCollectorListener(
    GitlabCsExtraParserListener,
    DockerCsExtraParserListener,
    FileCsExtraParserListener,
    ChannelsCsExtraParserListener,
    CeleryCsExtraParserListener,
    LangsCsExtraParserListener,
    FilerCsExtraParserListener,
    PageCrudOverrideExtraListener,
    BaseListener
):

    def __init__(self, collection_set: CollectionSetDef) -> None:
        super().__init__(collection_set)

        self.page = None  # type: PageDef
        self.model = None  # type: CollectionDef

        self.inline = None  # type

        self.field = None  # type
        self.field_config = None  # type: FieldConfig
        self.image_size = None  # type: ImageSize

        self.import_from = None
        self.import_list = []

    def enterImport_statement(self, ctx: ZmeiLangParser.Import_statementContext):
        self.import_from = None
        self.import_list = []

    def enterImport_source(self, ctx: ZmeiLangParser.Import_sourceContext):
        self.import_from = ctx.getText()

    def enterImport_item(self, ctx: ZmeiLangParser.Import_itemContext):
        if ctx.import_item_all():
            name = '*'
        else:
            name = ctx.import_item_name().getText()
            if ctx.import_item_alias():
                name += ' as ' + ctx.import_item_alias().getText()
        self.import_list.append(name)

    def exitPage_import_statement(self, ctx: ZmeiLangParser.Page_import_statementContext):
        self.collection_set.page_imports.add(self.import_from, *self.import_list)

    def exitModel_import_statement(self, ctx: ZmeiLangParser.Model_import_statementContext):
        self.collection_set.model_imports.add(self.import_from, *self.import_list)

    ############################################
    # Page
    ############################################

    def enterPage(self, ctx: ZmeiLangParser.PageContext):
        self.page = PageDef(self.collection_set)
        self.page.page_items = {}

    def enterPage_name(self, ctx: ZmeiLangParser.Page_nameContext):
        self.page.name = ctx.getText()

    def enterPage_alias_name(self, ctx: ZmeiLangParser.Page_alias_nameContext):
        self.page.defined_url_alias = ctx.getText()

    def enterPage_base(self, ctx: ZmeiLangParser.Page_baseContext):
        self.page.extend_name = ctx.getText()[-2] == '~'
        self.page.parent_name = ctx.getText()[:-2]

    def enterPage_url(self, ctx: ZmeiLangParser.Page_urlContext):
        url = ctx.getText().strip()
        if url[0] == '$':
            if not self.collection_set.langs:
                raise LangsRequiredValidationError(ctx.start)
        self.page.set_uri(url)

    def enterPage_template(self, ctx: ZmeiLangParser.Page_templateContext):
        tpl = ctx.getText().strip()

        if '{' in tpl:
            self.page.parsed_template_expr = tpl.strip('{}')
        else:
            self.page.parsed_template_name = tpl

    def enterPage_field(self, ctx: ZmeiLangParser.Page_fieldContext):
        field = ctx.page_field_name().getText()
        val = ctx.page_field_code().getText()

        expr = PageExpression(field, val, self.page)

        if field == 'sitemap':
            self.page.sitemap_expr = expr
        else:
            self.page.page_items[field] = expr

    def enterPage_function(self, ctx: ZmeiLangParser.Page_functionContext):
        super().enterPage_function(ctx)

        func = PageFunction()
        func.name = ctx.page_function_name().getText()
        if ctx.page_function_args():
            func.out_args = [x.strip() for x in ctx.page_function_args().getText().split(',')]
            func.args = [x for x in func.out_args if x not in ('url', 'request')]
        else:
            func.args = []

        if ctx.code_block():
            func.body = self._get_code(ctx)

        self.page.functions[func.name] = func

    def enterPage_code(self, ctx: ZmeiLangParser.Page_codeContext):
        self.page.page_code = self._get_code(ctx.python_code()) + '\n'

    def exitPage(self, ctx: ZmeiLangParser.PageContext):
        if self.page.parent_name and self.page.extend_name:
            self.page.name = f'{self.page.parent_name}_{self.page.name}'

        self.collection_set.pages[self.page.name] = self.page
        self.page = None


    ############################################
    # Model
    ############################################

    def enterCol(self, ctx: ZmeiLangParser.ColContext):
        self.model = CollectionDef(self.collection_set)

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
        self.collection_set.collections[self.model.ref] = self.model
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
            if not self.collection_set.langs:
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
        self.field.extra_args_append = True

    def enterCol_field_extend(self, ctx: ZmeiLangParser.Col_field_extendContext):
        self.field.extra_args = self._get_code(ctx)

    # Custom

    def enterCol_field_custom(self, ctx: ZmeiLangParser.Col_field_customContext):
        self.field = CustomFieldDef(self.model, self.field_config)
        self.field.custom_declaration = self._get_code(ctx)

    # Text

    def enterField_text(self, ctx: ZmeiLangParser.Field_textContext):
        self.field = TextFieldDef(self.model, self.field_config)

    def enterField_text_size(self, ctx: ZmeiLangParser.Field_text_sizeContext):
        mlen = ctx.getText()
        if mlen == '?':
            self.field.max_length = 0
        else:
            self.field.max_length = int(mlen)

    def enterField_text_choices(self, ctx: ZmeiLangParser.Field_text_choicesContext):
        self.field.choices = {}

    def enterField_text_choice(self, ctx: ZmeiLangParser.Field_text_choiceContext):
        choice_key = ctx.field_text_choice_key()

        val = ctx.field_text_choice_val().getText().strip('"\' ')
        if choice_key:
            key = choice_key.getText().strip(': ')
        else:
            key = val

        self.field.choices[key] = val

    def exitField_text_choices(self, ctx: ZmeiLangParser.Field_text_choicesContext):
        if not self.field.max_length:
            for key in self.field.choices.keys():
                self.field.max_length = max(self.field.max_length, len(key))

        self.field.choices = tuple(self.field.choices.items())

    # Integer

    def enterField_int(self, ctx: ZmeiLangParser.Field_intContext):
        self.field = IntegerFieldDef(self.model, self.field_config)

    def enterField_int_choices(self, ctx: ZmeiLangParser.Field_int_choicesContext):
        self.field.choices = {}

    def enterField_int_choice(self, ctx: ZmeiLangParser.Field_int_choiceContext):
        choice_key = ctx.field_int_choice_key()
        if choice_key:
            key = int(choice_key.getText().strip(': '))
        else:
            key = len(self.field.choices)

        val = ctx.field_int_choice_val().getText().strip('"\' ')

        self.field.choices[key] = val

    def exitField_int_choices(self, ctx: ZmeiLangParser.Field_int_choicesContext):
        self.field.choices = tuple(self.field.choices.items())

    # Float field

    def enterField_float(self, ctx: ZmeiLangParser.Field_floatContext):
        self.field = FloatFieldDef(self.model, self.field_config)

    # Decimal field

    def enterField_decimal(self, ctx: ZmeiLangParser.Field_decimalContext):
        self.field = DecimalFieldDef(self.model, self.field_config)

    # Slug field

    def enterField_slug(self, ctx: ZmeiLangParser.Field_slugContext):
        self.field = SlugFieldDef(self.model, self.field_config)

    def enterField_slug_ref_field_id(self, ctx: ZmeiLangParser.Field_slug_ref_field_idContext):
        self.field.field_names.append(ctx.getText())

    # LongText field

    def enterField_longtext(self, ctx: ZmeiLangParser.Field_longtextContext):
        self.field = LongTextFieldDef(self.model, self.field_config)

    # Html field

    def enterField_html(self, ctx: ZmeiLangParser.Field_htmlContext):
        self.field = RichTextFieldDef(self.model, self.field_config)

    # Html media field

    def enterField_html_media(self, ctx: ZmeiLangParser.Field_html_mediaContext):
        self.field = RichTextFieldWithUploadDef(self.model, self.field_config)

    # Bool field

    def enterField_bool(self, ctx: ZmeiLangParser.Field_boolContext):
        self.field = BooleanFieldDef(self.model, self.field_config)

    def enterField_bool_default(self, ctx: ZmeiLangParser.Field_bool_defaultContext):
        self.field.default = ctx.getText().strip() == 'true'

    # Date field

    def enterField_date(self, ctx: ZmeiLangParser.Field_dateContext):
        self.field = DateFieldDef(self.model, self.field_config)

    # Datetime field

    def enterField_datetime(self, ctx: ZmeiLangParser.Field_datetimeContext):
        self.field = DateTimeFieldDef(self.model, self.field_config)

    # update_time field

    def enterField_update_time(self, ctx: ZmeiLangParser.Field_update_timeContext):
        self.field = AutoNowDateTimeFieldDef(self.model, self.field_config)

    # create_time field

    def enterField_create_time(self, ctx: ZmeiLangParser.Field_create_timeContext):
        self.field = AutoNowAddDateTimeFieldDef(self.model, self.field_config)

    # image and image_folder field

    def enterField_image(self, ctx: ZmeiLangParser.Field_imageContext):
        type_name = ctx.filer_image_type().getText()
        if type_name == 'image':
            self.field = ImageFieldDef(self.model, self.field_config)
        elif type_name == 'filer_image_folder':
            self.field = FilerImageFolderFieldDef(self.model, self.field_config)
        else:
            self.field = FilerImageFieldDef(self.model, self.field_config)

        self.field.sizes = []

    def enterField_image_size(self, ctx: ZmeiLangParser.Field_image_sizeContext):
        self.image_size = ImageSize()
        self.image_size.filters = []

    def enterField_image_size_name(self, ctx: ZmeiLangParser.Field_image_size_nameContext):
        self.image_size.name = ctx.getText().strip()

    def enterField_image_size_dimensions(self, ctx: ZmeiLangParser.Field_image_size_dimensionsContext):
        width, height = ctx.getText().strip().split('x')
        self.image_size.width = int(width)
        self.image_size.height = int(height)

    def enterField_image_filter(self, ctx: ZmeiLangParser.Field_image_filterContext):
        self.image_size.filters.append(ctx.getText()[1:])

    def exitField_image_size(self, ctx: ZmeiLangParser.Field_image_sizeContext):
        self.field.sizes.append(self.image_size)
        self.image_size = None

    # filer_file  field

    def enterField_filer_file(self, ctx: ZmeiLangParser.Field_filer_fileContext):
        self.field = FilerFileFieldDef(self.model, self.field_config)

    # file  field

    def enterField_file(self, ctx: ZmeiLangParser.Field_fileContext):
        self.field = SimpleFieldDef(self.model, self.field_config)

    # folder  field

    def enterField_filer_folder(self, ctx: ZmeiLangParser.Field_filer_folderContext):
        self.field = FilerFileFolderDef(self.model, self.field_config)

    # Relation field

    def enterField_relation_type(self, ctx: ZmeiLangParser.Field_relation_typeContext):
        type_name = ctx.getText()
        if type_name == 'one':
            self.field = RelationOneDef(self.model, self.field_config)
        if type_name == 'one2one':
            self.field = RelationOne2OneDef(self.model, self.field_config)
        if type_name == 'many':
            self.field = RelationManyDef(self.model, self.field_config)

    def enterField_relation_target_class(self, ctx: ZmeiLangParser.Field_relation_target_classContext):
        self.field.related_class = ctx.getText()

    def enterField_relation_target_ref(self, ctx: ZmeiLangParser.Field_relation_target_refContext):
        self.field.ref_collection_def = ctx.getText()[1:]

    def enterField_relation_related_name(self, ctx: ZmeiLangParser.Field_relation_related_nameContext):
        related_name = ctx.getText()[2:].strip()

        self.field.related_name = related_name

    ############################################
    # Admin
    ############################################

    def enterAn_admin(self, ctx: ZmeiLangParser.An_adminContext):
        self.model.admin = AdminExtra(self.model)
        self.collection_set.admin = True
        self.collection_set.extras.append(self.model.admin)

    def enterAn_admin_list(self, ctx: ZmeiLangParser.An_admin_listContext):
        self.model.admin.admin_list = self.model.filter_fields(self._get_fields(ctx))

    def enterAn_admin_read_only(self, ctx: ZmeiLangParser.An_admin_read_onlyContext):
        self.model.admin.read_only = self.model.filter_fields(self._get_fields(ctx))

    def enterAn_admin_list_editable(self, ctx: ZmeiLangParser.An_admin_list_editableContext):
        self.model.admin.list_editable = self.model.filter_fields(self._get_fields(ctx))

    def enterAn_admin_list_filter(self, ctx: ZmeiLangParser.An_admin_list_filterContext):
        self.model.admin.list_filter = self.model.filter_fields(self._get_fields(ctx))

    def enterAn_admin_list_search(self, ctx: ZmeiLangParser.An_admin_list_searchContext):
        self.model.admin.list_search = self.model.filter_fields(self._get_fields(ctx))

    def enterAn_admin_fields(self, ctx: ZmeiLangParser.An_admin_fieldsContext):
        self.model.admin.fields = self.model.filter_fields(self._get_fields(ctx))

    def enterAn_admin_tabs(self, ctx: ZmeiLangParser.An_admin_tabsContext):
        if not self.collection_set.suit:
            raise TabsSuitRequiredValidationError(ctx.start)

    def enterAn_admin_tab(self, ctx: ZmeiLangParser.An_admin_tabContext):
        fields = self._get_fields(ctx)
        name = ctx.tab_name().getText()
        vname = ctx.tab_verbose_name()
        if vname:
            vname = vname.getText().strip('"\' ')
        else:
            vname = None
        self.model.admin.register_tab(name, vname, fields)

    def enterAn_admin_inline(self, ctx: ZmeiLangParser.An_admin_inlineContext):
        self.inline = AdminInlineConfig(self.model.admin, ctx.inline_name().getText())

    def enterInline_type(self, ctx: ZmeiLangParser.Inline_typeContext):
        type_name = ctx.KW_INLINE_TYPE().getText()

        if type_name == 'polymorphic':
            self.model.admin.has_polymorphic_inlines = True

        self.inline.inline_type = type_name

    def enterInline_fields(self, ctx: ZmeiLangParser.Inline_fieldsContext):
        self.inline.fields_expr = self._get_fields(ctx)

    def enterInline_extra(self, ctx: ZmeiLangParser.Inline_extraContext):
        self.inline.extra_count = int(ctx.DIGIT().getText())

    def enterAn_admin_css_file_name(self, ctx: ZmeiLangParser.An_admin_css_file_nameContext):
        self.model.admin.css.append(ctx.getText().strip('"\''))

    def enterAn_admin_js_file_name(self, ctx: ZmeiLangParser.An_admin_js_file_nameContext):
        self.model.admin.js.append(ctx.getText().strip('"\''))

    def exitAn_admin_inline(self, ctx: ZmeiLangParser.An_admin_inlineContext):
        self.model.admin.inlines.append(
            self.inline
        )
        self.inline = None

    # Suit

    def enterAn_suit(self, ctx: ZmeiLangParser.An_suitContext):
        suit = SuitCsExtra(self.collection_set)
        self.collection_set.extras.append(suit)
        self.collection_set.suit = suit

    def enterAn_suit_app_name(self, ctx: ZmeiLangParser.An_suit_app_nameContext):
        self.collection_set.suit.app_name = ctx.getText().strip('"\'')



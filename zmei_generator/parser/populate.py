from zmei_generator.config.domain.collection_def import CollectionDef
from zmei_generator.config.domain.collection_set_def import CollectionSetDef
from zmei_generator.config.domain.exceptions import ValidationException
from zmei_generator.config.domain.field_def import FieldConfig, FieldDef
from zmei_generator.config.domain.page_def import PageDef
from zmei_generator.config.domain.page_expression import PageExpression
from zmei_generator.config.domain.reference_field import ReferenceField
from zmei_generator.extras.admin import AdminExtra
from zmei_generator.fields.bool import BooleanFieldDef
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
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser, ParseTreeWalker
from zmei_generator.parser.gen.ZmeiLangParserListener import ZmeiLangParserListener


class PartsCollectorListener(ZmeiLangParserListener):

    def __init__(self, collection_set: CollectionSetDef) -> None:
        super().__init__()

        self.collection_set = collection_set

        self.page = None  # type: PageDef
        self.model = None  # type: CollectionDef

        self.field = None  # type
        self.field_config = None  # type: FieldConfig
        self.image_size = None  # type: ImageSize

    ############################################
    # Page
    ############################################

    def enterPage(self, ctx: ZmeiLangParser.PageContext):
        self.page = PageDef(self.collection_set)
        self.page.page_items = {}

    def enterPage_name(self, ctx: ZmeiLangParser.Page_nameContext):
        self.page.name = ctx.getText()
        self.page.url_alias = ctx.getText()

    def enterPage_alias_name(self, ctx: ZmeiLangParser.Page_alias_nameContext):
        self.page.url_alias = ctx.getText()

    def enterPage_base(self, ctx: ZmeiLangParser.Page_baseContext):
        self.page.parent_name = ctx.getText()[:-2]

    def enterPage_url(self, ctx: ZmeiLangParser.Page_urlContext):
        self.page.set_uri(ctx.getText().strip())

    def enterPage_template(self, ctx: ZmeiLangParser.Page_templateContext):
        tpl = ctx.getText().strip()

        if '{' in tpl:
            self.page.parsed_template_expr = tpl.strip('{}')
        else:
            self.page.parsed_template_name = tpl

    def enterPage_code(self, ctx: ZmeiLangParser.Page_codeContext):
        self.page.page_code = ctx.getText().strip('{} \n')

    def enterPage_field(self, ctx: ZmeiLangParser.Page_fieldContext):
        field = ctx.page_field_name().getText()
        val = ctx.page_field_code().getText()

        expr = PageExpression(field, val, self.page)

        if field == 'sitemap':
            self.page.sitemap_expr = expr
        else:
            self.page.page_items[field] = expr

    def enterPage_element(self, ctx: ZmeiLangParser.Page_elementContext):
        self.page.set_html(ctx.getText().strip())

    def exitPage(self, ctx: ZmeiLangParser.PageContext):
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

    # image_file  field

    def enterField_image_file(self, ctx: ZmeiLangParser.Field_image_fileContext):
        self.field = ImageFieldDef(self.model, self.field_config)

    # image and image_folder field

    def enterField_image(self, ctx: ZmeiLangParser.Field_imageContext):
        type_name = ctx.filer_image_type().getText()
        if type_name == 'image_folder':
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

    # filer_image  field

    def enterField_filer_image(self, ctx: ZmeiLangParser.Field_filer_imageContext):
        self.field = FilerImageFieldDef(self.model, self.field_config)

    # filer_file  field

    def enterField_filer_file(self, ctx: ZmeiLangParser.Field_filer_fileContext):
        self.field = FilerFileFieldDef(self.model, self.field_config)

    # file  field

    def enterField_file(self, ctx: ZmeiLangParser.Field_fileContext):
        self.field = FilerFileFieldDef(self.model, self.field_config)

    # simple_file  field

    def enterField_simple_file(self, ctx: ZmeiLangParser.Field_simple_fileContext):
        self.field = SimpleFieldDef(self.model, self.field_config)

    # folder  field

    def enterField_folder(self, ctx: ZmeiLangParser.Field_folderContext):
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
        ref = ctx.getText()[1:]

        try:
            ref_collection = self.collection_set.collections[ref]
        except KeyError:
            raise ValidationException('Reference to unknown collection: #{}'.format(ref))

        self.field.ref_collection = ref_collection
        self.field.related_class = ref_collection.class_name

    def enterField_relation_related_name(self, ctx: ZmeiLangParser.Field_relation_related_nameContext):
        related_name = ctx.getText()[2:].strip()

        self.field.related_name = related_name

        if self.field.ref_collection and related_name in self.field.ref_collection.fields:
            raise ValidationException('Can not override field with related field: {}'.format(related_name))

        if self.field.ref_collection:
            self.field.ref_collection.fields[related_name] = \
                ReferenceField(self.field.ref_collection, self.model, related_name, self.field)

    ############################################
    # Admin
    ############################################

    def enterAn_admin(self, ctx: ZmeiLangParser.An_adminContext):
        self.model.admin = AdminExtra()
        self.collection_set.admin = True

    def enterAn_admin_list(self, ctx: ZmeiLangParser.An_admin_listContext):
        self.model.admin.admin_list = self.model.filter_fields(self._get_admin_fields(ctx))

    def enterAn_admin_read_only(self, ctx: ZmeiLangParser.An_admin_read_onlyContext):
        self.model.admin.read_only = self.model.filter_fields(self._get_admin_fields(ctx))

    def enterAn_admin_list_editable(self, ctx: ZmeiLangParser.An_admin_list_editableContext):
        self.model.admin.list_editable  = self.model.filter_fields(self._get_admin_fields(ctx))

    def enterAn_admin_list_filter(self, ctx: ZmeiLangParser.An_admin_list_filterContext):
        self.model.admin.list_filter  = self.model.filter_fields(self._get_admin_fields(ctx))

    def enterAn_admin_list_search(self, ctx: ZmeiLangParser.An_admin_list_searchContext):
        self.model.admin.list_search  = self.model.filter_fields(self._get_admin_fields(ctx))

    def enterAn_admin_fields(self, ctx: ZmeiLangParser.An_admin_fieldsContext):
        self.model.admin.fields  = self.model.filter_fields(self._get_admin_fields(ctx))

    def _get_admin_fields(self, ctx):
        return [x.strip() for x in ctx.field_list_expr().getText().split(',')]


def populate_collection_set(tree, app_name='noname'):
    cs = CollectionSetDef(app_name)

    validator = PartsCollectorListener(cs)

    walker = ParseTreeWalker()
    walker.walk(validator, tree)

    return cs

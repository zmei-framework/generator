from zmei_generator.contrib.filer.fields.filer import FilerImageFolderFieldDef, FilerImageFieldDef, ImageSize, \
    FilerFileFieldDef, FilerFileFolderDef
from zmei_generator.contrib.web.fields.bool import BooleanFieldDef
from zmei_generator.contrib.web.fields.date import DateFieldDef, DateTimeFieldDef, AutoNowDateTimeFieldDef, \
    AutoNowAddDateTimeFieldDef
from zmei_generator.contrib.web.fields.image import ImageFieldDef, SimpleFieldDef
from zmei_generator.contrib.web.fields.number import IntegerFieldDef, FloatFieldDef, DecimalFieldDef
from zmei_generator.contrib.web.fields.relation import RelationOneDef, RelationOne2OneDef, RelationManyDef
from zmei_generator.contrib.web.fields.text import TextFieldDef, SlugFieldDef, LongTextFieldDef, RichTextFieldDef, \
    RichTextFieldWithUploadDef
from zmei_generator.domain.application_def import ApplicationDef
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class FieldsParserListener(BaseListener):
    def __init__(self, application: ApplicationDef) -> None:
        super().__init__(application)

        self.image_size = None  # type: ImageSize

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

    def enterField_relation_cascade_marker(self, ctx: ZmeiLangParser.Field_relation_cascade_markerContext):
        if ctx.getText() == '!':
            self.field.on_delete = 'CASCADE'
        elif ctx.getText() == '~':
            self.field.on_delete = 'SET_NULL'

    def enterField_relation_target_class(self, ctx: ZmeiLangParser.Field_relation_target_classContext):
        self.field.related_class = ctx.getText()

    def enterField_relation_target_ref(self, ctx: ZmeiLangParser.Field_relation_target_refContext):
        self.field.ref_model_def = ctx.getText()[1:]

    def enterField_relation_related_name(self, ctx: ZmeiLangParser.Field_relation_related_nameContext):
        related_name = ctx.getText()[2:].strip()

        self.field.related_name = related_name

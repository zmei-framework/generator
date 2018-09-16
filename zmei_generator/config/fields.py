from zmei_generator.fields.bool import BooleanFieldDef
from zmei_generator.fields.date import DateFieldDef, DateTimeFieldDef, AutoNowDateTimeFieldDef, \
    AutoNowAddDateTimeFieldDef
from zmei_generator.fields.filer import FilerFileFolderDef, FilerImageFolderFieldDef, FilerImageFieldDef, \
    FilerFileFieldDef
from zmei_generator.fields.image import ImageFieldDef, SimpleFieldDef
from zmei_generator.fields.number import IntegerFieldDef, FloatFieldDef, DecimalFieldDef
from zmei_generator.fields.relation import RelationOneDef, RelationManyDef, RelationOne2OneDef
from zmei_generator.fields.text import TextFieldDef, LongTextFieldDef, RichTextFieldDef, SlugFieldDef, \
    RichTextFieldWithUploadDef

field_type_map = {
    'text': TextFieldDef,
    'slug': SlugFieldDef,
    'longtext': LongTextFieldDef,
    'html': RichTextFieldDef,
    'html_media': RichTextFieldWithUploadDef,

    'date': DateFieldDef,
    'datetime': DateTimeFieldDef,
    'update_time': AutoNowDateTimeFieldDef,
    'create_time': AutoNowAddDateTimeFieldDef,

    'bool': BooleanFieldDef,

    'int': IntegerFieldDef,
    'float': FloatFieldDef,
    'decimal': DecimalFieldDef,

    'one': RelationOneDef,
    'many': RelationManyDef,
    'one2one': RelationOne2OneDef,

    'image_file': ImageFieldDef,
    'image': FilerImageFieldDef,
    'filer_image': FilerImageFieldDef,
    'filer_file': FilerFileFieldDef,
    'file': FilerFileFieldDef,
    'simple_file': SimpleFieldDef,
    'folder': FilerFileFolderDef,
    'image_folder': FilerImageFolderFieldDef,
}
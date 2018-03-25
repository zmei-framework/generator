from cratis_generator.config.domain import FieldDef
from cratis_generator.fields.bool import BooleanFieldDef
from cratis_generator.fields.date import DateFieldDef, DateTimeFieldDef, AutoNowDateTimeFieldDef, \
    AutoNowAddDateTimeFieldDef
from cratis_generator.fields.filer import FilerFileFolderDef, FilerImageFolderFieldDef, FilerImageFieldDef, \
    FilerFileFieldDef
from cratis_generator.fields.image import ImageFieldDef
from cratis_generator.fields.number import IntegerFieldDef, FloatFieldDef, DecimalFieldDef
from cratis_generator.fields.relation import RelationOneDef, RelationManyDef, RelationOne2OneDef
from cratis_generator.fields.text import TextFieldDef, LongTextFieldDef, RichTextFieldDef, SlugFieldDef


field_type_map = {
    'text': TextFieldDef,
    'slug': SlugFieldDef,
    'longtext': LongTextFieldDef,
    'html': RichTextFieldDef,
    'one': RelationOneDef,
    'many': RelationManyDef,
    'one2one': RelationOne2OneDef,
    'image_file': ImageFieldDef,
    'filer_image': FilerImageFieldDef,
    'filer_file': FilerFileFieldDef,
    'folder': FilerFileFolderDef,
    'image_folder': FilerImageFolderFieldDef,

    'date': DateFieldDef,
    'datetime': DateTimeFieldDef,
    'update_time': AutoNowDateTimeFieldDef,
    'create_time': AutoNowAddDateTimeFieldDef,

    'bool': BooleanFieldDef,

    'int': IntegerFieldDef,
    'float': FloatFieldDef,
    'decimal': DecimalFieldDef,
}
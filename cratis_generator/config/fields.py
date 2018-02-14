from cratis_generator.config.domain import FieldDef
from cratis_generator.fields.bool import BooleanFieldDef
from cratis_generator.fields.date import DateFieldDef, DateTimeFieldDef, AutoNowDateTimeFieldDef, \
    AutoNowAddDateTimeFieldDef
from cratis_generator.fields.number import IntegerFieldDef, FloatFieldDef, DecimalFieldDef
from cratis_generator.fields.relation import RelationOneDef, RelationManyDef
from cratis_generator.fields.text import TextFieldDef, LongTextFieldDef, RichTextFieldDef, SlugFieldDef
from cratis_generator.fields.filer import ImageFieldDef, FileFieldDef, ImageFolderFieldDef, FileFolderDef

field_type_map = {
    'text': TextFieldDef,
    'slug': SlugFieldDef,
    'longtext': LongTextFieldDef,
    'html': RichTextFieldDef,
    'one': RelationOneDef,
    'many': RelationManyDef,
    'image': ImageFieldDef,
    'file': FileFieldDef,
    'folder': FileFolderDef,
    'image_folder': ImageFolderFieldDef,

    'date': DateFieldDef,
    'datetime': DateTimeFieldDef,
    'update_time': AutoNowDateTimeFieldDef,
    'create_time': AutoNowAddDateTimeFieldDef,

    'bool': BooleanFieldDef,

    'int': IntegerFieldDef,
    'float': FloatFieldDef,
    'decimal': DecimalFieldDef,
}
from textwrap import dedent

from zmei_generator.fields.bool import BooleanFieldDef
from zmei_generator.fields.text import TextFieldDef, LongTextFieldDef, RichTextFieldDef, RichTextFieldWithUploadDef
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_bool_field():
    cs = _("""
    
        #boo
        ----------
        a: bool
        b: bool(true)
        ~c: bool(false)
    """)

    a = cs.collections['boo'].fields['a']
    b = cs.collections['boo'].fields['b']
    c = cs.collections['boo'].fields['c']

    assert isinstance(a, BooleanFieldDef)
    assert isinstance(b, BooleanFieldDef)
    assert isinstance(c, BooleanFieldDef)

    assert a.default is False
    assert b.default is True
    assert c.default is False

    assert "default=False" in a.get_model_field()[1]
    assert "default=True" in b.get_model_field()[1]
    assert "default=False" in c.get_model_field()[1]

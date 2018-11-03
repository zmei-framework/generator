from textwrap import dedent

from zmei_generator.fields.text import SlugFieldDef
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_slug_field():
    cs = _("""
    
        #boo
        ----------
        a: str(15)
        b: str(10)
        c: slug(a,b)
    """)

    c = cs.collections['boo'].fields['c']

    assert isinstance(c, SlugFieldDef)
    assert c.field_names == ['a', 'b']

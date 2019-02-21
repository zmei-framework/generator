from textwrap import dedent

from zmei_generator.contrib.web.fields.text import SlugFieldDef
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_slug_field():
    app = _("""
    
        #boo
        ----------
        a: str(15)
        b: str(10)
        c: slug(a,b)
    """)

    c = app.models['boo'].fields['c']

    assert isinstance(c, SlugFieldDef)
    assert c.field_names == ['a', 'b']


def test_slug_field_2models():
    app = _("""
    
        #boo
        ----------
        a: str(15)
        b: str(10)
        c: slug(a)
    
        #foo
        ----------
        a: str(15)
        b: str(10)
        c: slug(b)
    """)

    boo = app.models['boo'].fields['c']

    assert isinstance(boo, SlugFieldDef)
    assert boo.field_names == ['a']

    foo = app.models['foo'].fields['c']

    assert isinstance(foo, SlugFieldDef)
    assert foo.field_names == ['b']

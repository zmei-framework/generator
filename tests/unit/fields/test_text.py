from textwrap import dedent

from zmei_generator.contrib.web.fields.text import TextFieldDef, LongTextFieldDef, RichTextFieldDef, \
    RichTextFieldWithUploadDef
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_text_field():
    app = _("""
    
        #boo
        ----------
        a
        b: str(255)
        c: str(?, choices=ab:Cda,abcd:Cda1,abcdef:"Яба яба")
        d: str(?, choices=foo,bar,baz)
    """)

    a = app.models['boo'].fields['a']

    assert isinstance(a, TextFieldDef)
    assert a.max_length == 100

    b = app.models['boo'].fields['b']

    assert isinstance(b, TextFieldDef)
    assert b.max_length == 255

    c = app.models['boo'].fields['c']

    assert isinstance(c, TextFieldDef)
    assert c.max_length == 6
    assert c.choices == (
        ('ab', 'Cda'),
        ('abcd', 'Cda1'),
        ('abcdef', 'Яба яба'),
    )

    d = app.models['boo'].fields['d']

    assert isinstance(d, TextFieldDef)
    assert d.choices == (
        ('foo', 'foo'),
        ('bar', 'bar'),
        ('baz', 'baz'),
    )

def test_longtext_field():
    app = _("""
    
        #boo
        ----------
        a: text
    """)

    a = app.models['boo'].fields['a']

    assert isinstance(a, LongTextFieldDef)


def test_html_field():
    app = _("""
    
        #boo
        ----------
        a: html
    """)

    a = app.models['boo'].fields['a']

    assert isinstance(a, RichTextFieldDef)


def test_html_media_field():
    app = _("""
    
        #boo
        ----------
        a: html_media
    """)

    a = app.models['boo'].fields['a']

    assert isinstance(a, RichTextFieldWithUploadDef)

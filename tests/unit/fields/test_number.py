from textwrap import dedent

from zmei_generator.contrib.web.fields.number import IntegerFieldDef, FloatFieldDef, DecimalFieldDef
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_int_field():
    app = _("""
    
        #boo
        ----------
        b: int
        c: int(choices=2:Cda, 4:Cda1, 5:"Яба яба")
        d: int(choices=foo,bar,baz)
    """)

    b = app.models['boo'].fields['b']

    assert isinstance(b, IntegerFieldDef)

    c = app.models['boo'].fields['c']

    assert isinstance(c, IntegerFieldDef)
    assert c.choices == (
        (2, 'Cda'),
        (4, 'Cda1'),
        (5, 'Яба яба'),
    )

    d = app.models['boo'].fields['d']

    assert isinstance(d, IntegerFieldDef)
    assert d.choices == (
        (0, 'foo'),
        (1, 'bar'),
        (2, 'baz'),
    )


def test_float_field():
    app = _("""

        #boo
        ----------
        a: float
    """)

    a = app.models['boo'].fields['a']

    assert isinstance(a, FloatFieldDef)


def test_decimal_field():
    app = _("""

        #boo
        ----------
        a: decimal
    """)

    a = app.models['boo'].fields['a']

    assert isinstance(a, DecimalFieldDef)

from textwrap import dedent

from zmei_generator.fields.number import IntegerFieldDef, FloatFieldDef, DecimalFieldDef
from zmei_generator.parser.parser import parse_string
from zmei_generator.parser.populate import populate_collection_set


def _(code):
    tree = parse_string(dedent(code))

    return populate_collection_set(tree, 'example')


def test_int_field():
    cs = _("""
    
        #boo
        ----------
        b: int
        c: int(choices=2/Cda, 4/Cda1, 5/"Яба яба")
    """)

    b = cs.collections['boo'].fields['b']

    assert isinstance(b, IntegerFieldDef)

    c = cs.collections['boo'].fields['c']

    assert isinstance(c, IntegerFieldDef)
    assert c.choices == (
        (2, 'Cda'),
        (4, 'Cda1'),
        (5, 'Яба яба'),
    )


def test_float_field():
    cs = _("""

        #boo
        ----------
        a: float
    """)

    a = cs.collections['boo'].fields['a']

    assert isinstance(a, FloatFieldDef)


def test_decimal_field():
    cs = _("""

        #boo
        ----------
        a: decimal
    """)

    a = cs.collections['boo'].fields['a']

    assert isinstance(a, DecimalFieldDef)

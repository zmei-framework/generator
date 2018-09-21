from textwrap import dedent

from zmei_generator.fields.expression import ExpressionFieldDef
from zmei_generator.fields.text import SlugFieldDef
from zmei_generator.parser.parser import parse_string
from zmei_generator.parser.populate import populate_collection_set


def _(code):
    tree = parse_string(dedent(code))

    return populate_collection_set(tree, 'example')


def test_calculated_field():
    cs = _("""
    
        #boo
        ----------
        a:= 3 + 2
        b@= 3 + 2
        c:= !3 + 2
    """)

    a = cs.collections['boo'].fields['a']
    b = cs.collections['boo'].fields['b']
    c = cs.collections['boo'].fields['c']

    assert isinstance(a, ExpressionFieldDef)
    assert a.expression == '3 + 2'
    assert a.static is False
    assert a.boolean is False

    assert isinstance(b, ExpressionFieldDef)
    assert b.expression == '3 + 2'
    assert b.static is True
    assert b.boolean is False

    assert isinstance(b, ExpressionFieldDef)
    assert c.expression == '3 + 2'
    assert c.static is False
    assert c.boolean is True

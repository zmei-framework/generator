from textwrap import dedent

from zmei_generator.contrib.web.fields.expression import ExpressionFieldDef
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_calculated_field():
    app = _("""
    
        #boo
        ----------
        a:= 3 + 2
        b@= 3 + 2
        c:= !3 + 2
    """)

    a = app.models['boo'].fields['a']
    b = app.models['boo'].fields['b']
    c = app.models['boo'].fields['c']

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

    assert a.get_model_field() is None
    assert a.admin_list_renderer.strip() == "return obj.a"


def test_calculated_field2():
    app = _("""    
        
        #dog
        -------
        sound:= 'Bark!'
    """)

    dog = app.models['dog']
    a = dog.fields['sound']

    assert isinstance(a, ExpressionFieldDef)
    print('Type is', a.type_name)
    assert a.expression == "'Bark!'"
    assert a.static is False
    assert a.boolean is False
    assert a in dog.expression_fields
    assert a not in dog.own_fields_non_expr

from textwrap import dedent

from zmei_generator.contrib.web.fields.relation import RelationOneDef, RelationManyDef, RelationOne2OneDef
from zmei_generator.domain.reference_field import ReferenceField
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_one_relation():
    app = _("""
        #zoo
        ---------
        lala
    
        #boo
        ----------
        a: one(#zoo)
        b: many(#zoo -> rel_name)
        c: one2one(me.Foo)
        d: one(me.Foo -> rel_name)
    """)

    zoo = app.models['zoo']

    a = app.models['boo'].fields['a']
    b = app.models['boo'].fields['b']
    c = app.models['boo'].fields['c']
    d = app.models['boo'].fields['d']

    assert isinstance(a, RelationOneDef)
    assert isinstance(b, RelationManyDef)
    assert isinstance(c, RelationOne2OneDef)
    assert isinstance(d, RelationOneDef)

    assert a.related_name is None
    assert a.ref_model == zoo
    assert a.related_class == f'example.{zoo.class_name}'

    assert b.related_name == 'rel_name'
    assert b.ref_model == zoo
    assert b.related_class == f'example.{zoo.class_name}'

    assert c.related_name is None
    assert c.ref_model is None
    assert c.related_class == 'me.Foo'

    assert d.related_name == 'rel_name'
    assert d.ref_model is None
    assert d.related_class == 'me.Foo'

    rel_field = zoo.fields['rel_name']
    assert isinstance(rel_field, ReferenceField)
    assert rel_field.model == zoo
    assert rel_field.target_model == app.models['boo']
    assert rel_field.name == 'rel_name'
    assert rel_field.source_field == b


def test_relation_works_in_any_order():
    app = _("""

        #boo
        ----------
        a: one(#zoo -> boos)
        
        #zoo
        ---------
        lala
        
    """)

    assert isinstance(app.models['zoo'].fields['boos'], ReferenceField)


def test_relation_protected_by_default():
    app = _("""

        #boo
        ----------
        a: one(#zoo -> boos)
        
        #zoo
        ---------
        lala
        
    """)

    assert 'on_delete=models.CASCADE' not in app.models['boo'].fields['a'].get_model_field()[1]


def test_relation_protected_can_be_overriden():
    app = _("""

        #boo
        ----------
        a: one(#zoo -> boos) ..{on_delete=models.CASCADE}
        
        #zoo
        ---------
        lala
        
    """)

    assert 'on_delete=models.CASCADE' in app.models['boo'].fields['a'].get_model_field()[1]


def test_relation_behaviour():
    app = _("""

        #boo
        ----------
        a: one(!#zoo)

        #zoo
        ---------
        lala

    """)

    assert 'on_delete=models.CASCADE' in app.models['boo'].fields['a'].get_model_field()[1]


def test_relation_behaviour_null():
    app = _("""

        #boo
        ----------
        a: one(~#zoo)

        #zoo
        ---------
        lala

    """)

    assert 'on_delete=models.SET_NULL' in app.models['boo'].fields['a'].get_model_field()[1]

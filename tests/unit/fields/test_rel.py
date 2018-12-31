from textwrap import dedent

from zmei_generator.config.domain.reference_field import ReferenceField
from zmei_generator.fields.bool import BooleanFieldDef
from zmei_generator.fields.relation import RelationOneDef, RelationManyDef, RelationOne2OneDef
from zmei_generator.fields.text import TextFieldDef, LongTextFieldDef, RichTextFieldDef, RichTextFieldWithUploadDef
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_one_relation():
    cs = _("""
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

    zoo = cs.collections['zoo']

    a = cs.collections['boo'].fields['a']
    b = cs.collections['boo'].fields['b']
    c = cs.collections['boo'].fields['c']
    d = cs.collections['boo'].fields['d']

    assert isinstance(a, RelationOneDef)
    assert isinstance(b, RelationManyDef)
    assert isinstance(c, RelationOne2OneDef)
    assert isinstance(d, RelationOneDef)

    assert a.related_name is None
    assert a.ref_collection == zoo
    assert a.related_class == f'example.{zoo.class_name}'

    assert b.related_name == 'rel_name'
    assert b.ref_collection == zoo
    assert b.related_class == f'example.{zoo.class_name}'

    assert c.related_name is None
    assert c.ref_collection is None
    assert c.related_class == 'me.Foo'

    assert d.related_name == 'rel_name'
    assert d.ref_collection is None
    assert d.related_class == 'me.Foo'

    rel_field = zoo.fields['rel_name']
    assert isinstance(rel_field, ReferenceField)
    assert rel_field.collection == zoo
    assert rel_field.target_collection == cs.collections['boo']
    assert rel_field.name == 'rel_name'
    assert rel_field.source_field == b


def test_relation_works_in_any_order():
    cs = _("""

        #boo
        ----------
        a: one(#zoo -> boos)
        
        #zoo
        ---------
        lala
        
    """)

    assert isinstance(cs.collections['zoo'].fields['boos'], ReferenceField)


def test_relation_protected_by_default():
    cs = _("""

        #boo
        ----------
        a: one(#zoo -> boos)
        
        #zoo
        ---------
        lala
        
    """)

    assert 'on_delete=models.CASCADE' not in cs.collections['boo'].fields['a'].get_model_field()[1]


def test_relation_protected_can_be_overriden():
    cs = _("""

        #boo
        ----------
        a: one(#zoo -> boos) ..{on_delete=models.CASCADE}
        
        #zoo
        ---------
        lala
        
    """)

    assert 'on_delete=models.CASCADE' in cs.collections['boo'].fields['a'].get_model_field()[1]

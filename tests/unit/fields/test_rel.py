from textwrap import dedent

from zmei_generator.config.domain.reference_field import ReferenceField
from zmei_generator.fields.bool import BooleanFieldDef
from zmei_generator.fields.relation import RelationOneDef, RelationManyDef, RelationOne2OneDef
from zmei_generator.fields.text import TextFieldDef, LongTextFieldDef, RichTextFieldDef, RichTextFieldWithUploadDef
from zmei_generator.parser.parser import parse_string
from zmei_generator.parser.populate import populate_collection_set


def _(code):
    tree = parse_string(dedent(code))

    return populate_collection_set(tree, 'example')


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
    assert a.related_class == zoo.class_name

    assert b.related_name == 'rel_name'
    assert b.ref_collection == zoo
    assert b.related_class == zoo.class_name

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

from textwrap import dedent

from zmei_generator.parser.parser import parse_string
from zmei_generator.parser.populate import populate_collection_set


def _(code):
    tree = parse_string(dedent(code))

    return populate_collection_set(tree, 'example')


def test_models():
    cs = _("""
    
        #boo
        ----------
        abc
        cda
        
        #foo_bar
        ----------
    
    """)

    assert len(cs.collections) == 2

    boo = cs.collections['boo']
    foo = cs.collections['foo_bar']

    assert boo.ref == 'boo'
    assert boo.short_ref == 'boo'
    assert boo.name == 'Boo'

    assert foo.ref == 'foo_bar'
    assert foo.short_ref == 'foo_bar'
    assert foo.name == 'Foo bar'


def test_model_parents():
    cs = _("""

        #boo
        ----------
        boo
        
        #boo->foo
        ----------
        boo
        
        #boo~>zoo
        ----------
        boo

    """)

    assert len(cs.collections) == 3

    boo = cs.collections['boo']
    foo = cs.collections['foo']
    zoo = cs.collections['boo_zoo']

    assert boo.polymorphic
    assert foo in boo.child_collections
    assert zoo in boo.child_collections

    assert foo.parent == boo
    assert zoo.parent == boo

    assert foo.ref == 'foo'
    assert zoo.ref == 'boo_zoo'


def test_model_names():
    cs = _("""

        #foo: Сосиска редиска
        ----------
        title

        #boo: Сосиска редиска/Сосиски редиски
        ----------
        title

    """)

    assert len(cs.collections) == 2

    foo = cs.collections['foo']
    boo = cs.collections['boo']

    assert foo.ref == 'foo'
    assert foo.name == 'Сосиска редиска'

    assert boo.ref == 'boo'
    assert boo.name == 'Сосиска редиска'
    assert boo.name_plural == 'Сосиски редиски'


def test_to_string():
    cs = _("""

        #foo
        ----------
        ="lolo {title}"
        title

    """)

    assert len(cs.collections) == 1

    foo = cs.collections['foo']

    assert foo.to_string == 'lolo {title}'

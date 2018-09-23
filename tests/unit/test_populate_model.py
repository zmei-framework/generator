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

        #foo: "Сосиска редиска"
        ----------
        title

        #boo: "Сосиска редиска"/'Сосиски редиски'
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


def test_modifiers():
    cs = _("""

        #foo
        ----------
        $a
        =b
        &c
        !d
        *e
        ~f

    """)

    assert len(cs.collections) == 1

    foo = cs.collections['foo']

    assert foo.fields['a'].translatable is True
    assert foo.fields['b'].display_field is True
    assert foo.fields['c'].unique is True
    assert foo.fields['d'].index is True
    assert foo.fields['e'].required is True
    assert foo.fields['f'].not_null is True


def test_modifiers_all():
    cs = _("""

        #foo
        ----------
        $=&!*~a

    """)

    assert len(cs.collections) == 1

    foo = cs.collections['foo']

    assert foo.translatable is True

    assert foo.fields['a'].translatable is True
    assert foo.fields['a'].display_field is True
    assert foo.fields['a'].unique is True
    assert foo.fields['a'].index is True
    assert foo.fields['a'].required is True
    assert foo.fields['a'].not_null is True


def test_translatable_parent():
    cs = _("""

        #foo
        ------
        $a
        
        #foo->boo
        ----------
        b
        
        #zoo
        ----------
        c

    """)

    assert len(cs.collections) == 3

    foo = cs.collections['foo']
    boo = cs.collections['boo']
    zoo = cs.collections['zoo']

    assert foo.translatable is True
    assert boo.translatable is True
    assert zoo.translatable is False

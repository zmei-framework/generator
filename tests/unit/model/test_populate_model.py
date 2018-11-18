from textwrap import dedent

from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


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


def test_verbose_name():
    cs = _("""

        #foo
        ----------
        title / This is title
        title2 /This is title2
        title3 /"This is title3"
        title4 /'This is title4'

    """)

    assert len(cs.collections) == 1

    foo = cs.collections['foo']

    assert foo.fields['title'].verbose_name == 'This is title'
    assert foo.fields['title2'].verbose_name == 'This is title2'
    assert foo.fields['title3'].verbose_name == 'This is title3'
    assert foo.fields['title4'].verbose_name == 'This is title4'


def test_help():
    cs = _("""

        #foo
        ----------
        title ? This is title
        title2 ?This is title2
        title3 ?"This is title3"
        title4 ?'This is title4'

    """)

    assert len(cs.collections) == 1

    foo = cs.collections['foo']

    assert foo.fields['title'].help == 'This is title'
    assert foo.fields['title2'].help == 'This is title2'
    assert foo.fields['title3'].help == 'This is title3'
    assert foo.fields['title4'].help == 'This is title4'


def test_help_and_verbose_name():
    cs = _("""

        #foo
        ----------
        title /This is title ? Definitely is

    """)

    assert len(cs.collections) == 1

    foo = cs.collections['foo']

    assert foo.fields['title'].verbose_name == 'This is title'
    assert foo.fields['title'].help == 'Definitely is'


def test_modifiers():
    cs = _("""
        @langs(en)

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
        @langs(en)

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
        @langs(en)

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

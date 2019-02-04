from textwrap import dedent

from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_models():
    app = _("""
    
        #boo
        ----------
        abc
        cda
        
        #foo_bar
        ----------
    
    """)

    assert len(app.models) == 2

    boo = app.models['boo']
    foo = app.models['foo_bar']

    assert boo.ref == 'boo'
    assert boo.short_ref == 'boo'
    assert boo.name == 'Boo'

    assert foo.ref == 'foo_bar'
    assert foo.short_ref == 'foo_bar'
    assert foo.name == 'Foo bar'


def test_model_parents():
    app = _("""

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

    assert len(app.models) == 3

    boo = app.models['boo']
    foo = app.models['foo']
    zoo = app.models['boo_zoo']

    assert boo.polymorphic
    assert foo in boo.child_models
    assert zoo in boo.child_models

    assert foo.parent == boo
    assert zoo.parent == boo

    assert foo.ref == 'foo'
    assert zoo.ref == 'boo_zoo'


def test_model_names():
    app = _("""

        #foo: "Сосиска редиска"
        ----------
        title

        #boo: "Сосиска редиска"/'Сосиски редиски'
        ----------
        title

    """)

    assert len(app.models) == 2

    foo = app.models['foo']
    boo = app.models['boo']

    assert foo.ref == 'foo'
    assert foo.name == 'Сосиска редиска'

    assert boo.ref == 'boo'
    assert boo.name == 'Сосиска редиска'
    assert boo.name_plural == 'Сосиски редиски'


def test_to_string():
    app = _("""

        #foo
        ----------
        ="lolo {title}"
        title

    """)

    assert len(app.models) == 1

    foo = app.models['foo']

    assert foo.to_string == 'lolo {title}'


def test_verbose_name():
    app = _("""

        #foo
        ----------
        title / This is title
        title2 /This is title2
        title3 /"This is title3"
        title4 /'This is title4'

    """)

    assert len(app.models) == 1

    foo = app.models['foo']

    assert foo.fields['title'].verbose_name == 'This is title'
    assert foo.fields['title2'].verbose_name == 'This is title2'
    assert foo.fields['title3'].verbose_name == 'This is title3'
    assert foo.fields['title4'].verbose_name == 'This is title4'


def test_verbose_name_real():
    app = _("""

        #tootaja_report: "Töötaja report"/"Töötaja reportid"
        --------------------
        *tooline: one(auth.User -> repordid)
        
        tooaeg_paevane: int /"Tööaeg päevane kokku (kella 6:00-21:59:59)"
        tooaeg_oine: int /"Tööaeg öine kokku (Kella 22:00:00-5:59:59"
        tooaeg_kokku: int /"Töötunnid kokku (päevane ja öine)"
        haigusleht: int /"Haigusleht (mitu tk. kuus)"
        puhkuse_paev: int /"Puhkuse päev (mitu tk. kuus)"


    """)

    assert len(app.models) == 1

    foo = app.models['tootaja_report']
    assert foo.fields['tooaeg_paevane'].verbose_name == 'Tööaeg päevane kokku (kella 6:00-21:59:59)'


def test_help():
    app = _("""

        #foo
        ----------
        title ? This is title
        title2 ?This is title2
        title3 ?"This is title3"
        title4 ?'This is title4'

    """)

    assert len(app.models) == 1

    foo = app.models['foo']

    assert foo.fields['title'].help == 'This is title'
    assert foo.fields['title2'].help == 'This is title2'
    assert foo.fields['title3'].help == 'This is title3'
    assert foo.fields['title4'].help == 'This is title4'


def test_help_and_verbose_name():
    app = _("""

        #foo
        ----------
        title /This is title ? Definitely is

    """)

    assert len(app.models) == 1

    foo = app.models['foo']

    assert foo.fields['title'].verbose_name == 'This is title'
    assert foo.fields['title'].help == 'Definitely is'


def test_modifiers():
    app = _("""
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

    assert len(app.models) == 1

    foo = app.models['foo']

    assert foo.fields['a'].translatable is True
    assert foo.fields['b'].display_field is True
    assert foo.fields['c'].unique is True
    assert foo.fields['d'].index is True
    assert foo.fields['e'].required is True
    assert foo.fields['f'].not_null is True


def test_modifiers_all():
    app = _("""
        @langs(en)

        #foo
        ----------
        $=&!*~a

    """)

    assert len(app.models) == 1

    foo = app.models['foo']

    assert foo.translatable is True

    assert foo.fields['a'].translatable is True
    assert foo.fields['a'].display_field is True
    assert foo.fields['a'].unique is True
    assert foo.fields['a'].index is True
    assert foo.fields['a'].required is True
    assert foo.fields['a'].not_null is True


def test_translatable_parent():
    app = _("""
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

    assert len(app.models) == 3

    foo = app.models['foo']
    boo = app.models['boo']
    zoo = app.models['zoo']

    assert foo.translatable is True
    assert boo.translatable is True
    assert zoo.translatable is False

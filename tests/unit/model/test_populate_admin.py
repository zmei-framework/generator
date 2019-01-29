from textwrap import dedent

from zmei_generator.contrib.admin.extensions.model.admin import AdminModelExtension, AdminInlineConfig
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_admin_empty():
    app = _("""
    
        #boo
        ----------
        abc
        cda
        
        @admin
    
    """)

    boo = app.models['boo']

    assert isinstance(boo[AdminModelExtension], AdminModelExtension)
    assert app.models_support(AdminModelExtension)

    assert boo[AdminModelExtension] in app.extensions


def test_admin_one_line():
    app = _("""
    
        #boo
        ----------
        abc
        cda
        
        @admin(list: *)
    
    """)

    boo = app.models['boo']

    assert isinstance(boo[AdminModelExtension], AdminModelExtension)
    assert app.models_support(AdminModelExtension) is True
    assert [x.name for x in boo[AdminModelExtension].admin_list] == ['abc', 'cda']


def test_admin_with_parent():
    app = _("""
    
        #foo
        ----------
        a
    
        #foo->boo
        ----------
        b
        c
        
        @admin(list: *)
    
    """)

    boo = app.models['boo']

    assert isinstance(boo[AdminModelExtension], AdminModelExtension)
    assert app.models_support(AdminModelExtension) is True
    assert [x.name for x in boo[AdminModelExtension].admin_list] == ['a', 'b', 'c']


def test_admin_with_parent_local_only():
    app = _("""
    
        #foo
        ----------
        a
    
        #foo->boo
        ----------
        b
        c
        
        @admin(list: .*)
    
    """)

    boo = app.models['boo']

    assert isinstance(boo[AdminModelExtension], AdminModelExtension)
    assert app.models_support(AdminModelExtension) is True
    assert [x.name for x in boo[AdminModelExtension].admin_list] == ['b', 'c']


def test_admin_plain_list():
    app = _("""
    
        #boo
        ----------
        weight
        size_x
        size_y
        color_front
        color_back
        
        @admin(
            list: weight, size_x, size_y, color_front
        )
    
    """)

    boo = app.models['boo']

    assert isinstance(boo[AdminModelExtension], AdminModelExtension)
    assert app.models_support(AdminModelExtension) is True
    assert [x.name for x in boo[AdminModelExtension].admin_list] == ['weight', 'size_x', 'size_y', 'color_front']


def test_admin_exclude():
    app = _("""
    
        #boo
        ----------
        weight
        size_x
        size_y
        color_front
        color_back
        
        @admin(
            list: *, ^color_front, ^size_x
        )
    
    """)

    boo = app.models['boo']

    assert isinstance(boo[AdminModelExtension], AdminModelExtension)
    assert app.models_support(AdminModelExtension) is True
    assert [x.name for x in boo[AdminModelExtension].admin_list] == ['weight', 'size_y', 'color_back']


def test_admin_exclude_wildcard():
    app = _("""
    
        #boo
        ----------
        weight
        size_x
        size_y
        color_front
        color_back
        
        @admin(
            list: *, ^color_*
        )
    
    """)

    boo = app.models['boo']

    assert isinstance(boo[AdminModelExtension], AdminModelExtension)
    assert app.models_support(AdminModelExtension) is True
    assert [x.name for x in boo[AdminModelExtension].admin_list] == ['weight', 'size_x', 'size_y']


def test_admin_include_wildcard():
    app = _("""
    
        #boo
        ----------
        weight
        size_x
        size_y
        color_front
        color_back
        
        @admin(
            list: weight, size_*
        )
    
    """)

    boo = app.models['boo']

    assert isinstance(boo[AdminModelExtension], AdminModelExtension)
    assert app.models_support(AdminModelExtension) is True
    assert [x.name for x in boo[AdminModelExtension].admin_list] == ['weight', 'size_x', 'size_y']


def test_admin_list():
    app = _("""
    
        #boo
        ----------
        abc
        cda
        
        @admin(
            list: *
            read_only: *
            list_editable: *
            list_filter: *
            list_search: *
            fields: *
        )
    
    """)

    boo = app.models['boo']

    assert isinstance(boo[AdminModelExtension], AdminModelExtension)
    assert app.models_support(AdminModelExtension) is True
    assert [x.name for x in boo[AdminModelExtension].admin_list] == ['abc', 'cda']
    assert [x.name for x in boo[AdminModelExtension].read_only] == ['abc', 'cda']
    assert [x.name for x in boo[AdminModelExtension].list_editable] == ['abc', 'cda']
    assert [x.name for x in boo[AdminModelExtension].list_filter] == ['abc', 'cda']
    assert [x.name for x in boo[AdminModelExtension].list_search] == ['abc', 'cda']
    assert [x.name for x in boo[AdminModelExtension].fields] == ['abc', 'cda']


def test_admin_tabs_all():
    app = _("""
        @suit
        
        #boo
        ----------
        a
        b
        c

        @admin(
            tabs: foo(*)
        )

    """)

    boo = app.models['boo']

    assert boo[AdminModelExtension].tabs == ['foo']
    assert boo[AdminModelExtension].tab_names == {'foo': 'Foo'}
    assert boo[AdminModelExtension].tab_fields == {
        'a': 'foo',
        'b': 'foo',
        'c': 'foo',
    }


def test_admin_tabs_inherited():
    app = _("""
        @suit
        
        #boo
        ----------
        a
        b
        c

        @admin(
            tabs: foo(*)
        )
        
        #boo->foo
        --------
        d
        
        @admin

    """)

    foo = app.models['foo']

    assert foo[AdminModelExtension].tabs == ['general', 'foo']
    assert foo[AdminModelExtension].tab_names == {'general': 'General', 'foo': 'Foo'}
    assert foo[AdminModelExtension].tab_fields == {
        'a': 'foo',
        'b': 'foo',
        'c': 'foo',
        'd': 'general',
    }


def test_admin_tabs_inherited_merged():
    app = _("""
        @suit

        #data_source
        --------------
        name
        
        @admin
        
        #data_source->db_data_source
        -------------------
        database
        server
        
        @admin
        
        #data_source->report_data_source
        -------------------
        report
        
        @admin


    """)

    foo = app.models['db_data_source']

    assert foo[AdminModelExtension].tab_fields == {
        'name': 'general',
        'database': 'general',
        'server': 'general',
    }

    assert foo[AdminModelExtension].tabs == ['general']
    assert foo[AdminModelExtension].tab_names == {'general': 'General'}

    foo = app.models['report_data_source']

    assert foo[AdminModelExtension].tab_fields == {
        'name': 'general',
        'report': 'general',
    }

    assert foo[AdminModelExtension].tabs == ['general']
    assert foo[AdminModelExtension].tab_names == {'general': 'General'}


def test_admin_tabs_all_but_some():
    app = _("""
        @suit
        
        #boo
        ----------
        a
        b
        c
        d

        @admin(
            tabs: foo(*), lolo(b, d)
        )

    """)

    boo = app.models['boo']

    assert boo[AdminModelExtension].tabs == ['foo', 'lolo']
    assert boo[AdminModelExtension].tab_names == {'foo': 'Foo', 'lolo': 'Lolo'}
    assert boo[AdminModelExtension].tab_fields == {
        'a': 'foo',
        'b': 'lolo',
        'c': 'foo',
        'd': 'lolo',
    }


def test_admin_tabs_verbose_name():
    app = _("""
        @suit
        
        #boo
        ----------
        a
        b
        c

        @admin(
            tabs: foo "Фу"(*)
        )

    """)

    boo = app.models['boo']

    assert boo[AdminModelExtension].tabs == ['foo']
    assert boo[AdminModelExtension].tab_names == {'foo': 'Фу'}
    assert boo[AdminModelExtension].tab_fields == {
        'a': 'foo',
        'b': 'foo',
        'c': 'foo',
    }


def test_admin_tabs_left_to_general():
    app = _("""
        @suit
        
        #boo
        ----------
        a
        b
        c

        @admin(
            tabs: foo(b,c)
        )

    """)

    boo = app.models['boo']

    assert boo[AdminModelExtension].tabs == ['general', 'foo']
    assert boo[AdminModelExtension].tab_names == {'general': 'General', 'foo': 'Foo'}
    assert boo[AdminModelExtension].tab_fields == {
        'a': 'general',
        'b': 'foo',
        'c': 'foo',
    }


def test_admin_tabs_with_fields():
    app = _("""
    @suit
    
    #car
    -------
    nr
    mark
    model
    weight: int
    crashed: bool(true)
    painted: bool

    @admin(
        tabs: main(*), options(crashed, painted)
        fields: *, ^weight
    )

    """)

    boo = app.models['car']

    assert boo[AdminModelExtension].tabs == ['main', 'options']
    assert boo[AdminModelExtension].tab_fields == {
        'nr': 'main',
        'mark': 'main',
        'model': 'main',
        'crashed': 'options',
        'painted': 'options',
    }


def test_admin_inline_simple():
    app = _("""
    #foo
    -------
    a
    b
    
    @admin(
        inline: lala
    )
    
    #bar
    --------
    rel: one(#foo -> lala)
    c
    d
    
    """)

    foo = app.models['foo']
    bar = app.models['bar']

    assert len(foo[AdminModelExtension].inlines) == 1
    inline = foo[AdminModelExtension].inlines[0]

    assert isinstance(inline, AdminInlineConfig)
    assert inline.extension_count == 0
    assert inline.model == foo
    assert inline.target_model == bar
    assert inline.inline_type == 'tabular'
    assert inline.inline_name == 'lala'
    assert inline.source_field_name == 'rel'
    assert inline.field_names == ['c', 'd']


def test_admin_inline_inheritance():
    app = _("""
    
    #data_source
    --------------
    name
    
    @admin(
        inline: fields
    )
    
    #data_source_field
    ---------------------
    name
    data_source: one(#data_source -> fields)
    
    
    #data_source->db_data_source
    -------------------
    database
    server
    
    @admin
    """)

    data_source = app.models['data_source']
    db_data_source = app.models['db_data_source']
    data_source_field = app.models['data_source_field']

    assert len(db_data_source[AdminModelExtension].inlines) == 1
    inline = db_data_source[AdminModelExtension].inlines[0]

    assert isinstance(inline, AdminInlineConfig)
    assert inline.model == data_source
    assert inline.target_model == data_source_field
    assert inline.inline_type == 'tabular'
    assert inline.inline_name == 'fields'
    assert inline.source_field_name == 'data_source'
    assert inline.field_names == ['name']


def test_admin_inline_endclass_with_parent():
    app = _("""
    
    
    #data_source
    --------------
    =name
    
    @admin
    
    
    #data_source->db_data_source
    -------------------
    database
    server
    
    @admin(
        inline: tables
    )
    
    
    #table
    ---------------------
    data_source: one(#db_data_source -> tables)
    name
    """)

    db_data_source = app.models['db_data_source']
    table = app.models['table']

    assert len(db_data_source[AdminModelExtension].inlines) == 1
    inline = db_data_source[AdminModelExtension].inlines[0]

    assert isinstance(inline, AdminInlineConfig)
    assert inline.model == db_data_source
    assert inline.target_model == table
    assert inline.inline_type == 'tabular'
    assert inline.inline_name == 'tables'
    assert inline.source_field_name == 'data_source'
    assert inline.field_names == ['name']


def test_admin_inline_details():
    app = _("""
    
    #foo
    -------
    a
    b
    
    @admin(
        inline: lala(
            type: stacked
            extension: 300
            fields: *, ^c
        )
    )
    
    #bar
    --------
    rel: one(#foo -> lala)
    c
    d
    
    """)

    foo = app.models['foo']
    bar = app.models['bar']

    assert len(foo[AdminModelExtension].inlines) == 1
    inline = foo[AdminModelExtension].inlines[0]

    assert isinstance(inline, AdminInlineConfig)
    assert inline.extension_count == 300
    assert inline.inline_type == 'stacked'
    assert inline.field_names == ['d']


def test_admin_inline_tab():
    app = _("""
    @suit
    
    #foo
    -------
    a
    b
    
    @admin(
        inline: lala(
            type: stacked
            extension: 300
            fields: *, ^c
        )
        tabs: main(*), other(lala)
    )
    
    #bar
    --------
    rel: one(#foo -> lala)
    c
    d
    
    """)

    foo = app.models['foo']
    bar = app.models['bar']

    assert len(foo[AdminModelExtension].inlines) == 1
    inline = foo[AdminModelExtension].inlines[0]
    assert inline.tab == 'other'

    assert foo[AdminModelExtension].tabs == ['main', 'other']
    assert foo[AdminModelExtension].tab_fields == {
        'a': 'main',
        'b': 'main',
        'lala': 'other',
    }


def test_admin_js_css():
    app = _("""

    #foo
    -------
    a

    @admin(
        css: "foo.css", "another/boo.css"
        js: 
            "foo.js", 
            "another/boo.js"
    )

    """)

    foo = app.models['foo']

    assert foo[AdminModelExtension].css == [
        "foo.css", "another/boo.css"
    ]
    assert foo[AdminModelExtension].js == [
        "foo.js", "another/boo.js"
    ]

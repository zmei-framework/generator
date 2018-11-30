from textwrap import dedent

from zmei_generator.extras.model.admin import AdminExtra, AdminInlineConfig
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_admin_empty():
    cs = _("""
    
        #boo
        ----------
        abc
        cda
        
        @admin
    
    """)

    boo = cs.collections['boo']

    assert isinstance(boo.admin, AdminExtra)
    assert cs.admin is True

    assert boo.admin in cs.extras


def test_admin_one_line():
    cs = _("""
    
        #boo
        ----------
        abc
        cda
        
        @admin(list: *)
    
    """)

    boo = cs.collections['boo']

    assert isinstance(boo.admin, AdminExtra)
    assert cs.admin is True
    assert [x.name for x in boo.admin.admin_list] == ['abc', 'cda']


def test_admin_with_parent():
    cs = _("""
    
        #foo
        ----------
        a
    
        #foo->boo
        ----------
        b
        c
        
        @admin(list: *)
    
    """)

    boo = cs.collections['boo']

    assert isinstance(boo.admin, AdminExtra)
    assert cs.admin is True
    assert [x.name for x in boo.admin.admin_list] == ['a', 'b', 'c']


def test_admin_with_parent_local_only():
    cs = _("""
    
        #foo
        ----------
        a
    
        #foo->boo
        ----------
        b
        c
        
        @admin(list: .*)
    
    """)

    boo = cs.collections['boo']

    assert isinstance(boo.admin, AdminExtra)
    assert cs.admin is True
    assert [x.name for x in boo.admin.admin_list] == ['b', 'c']


def test_admin_plain_list():
    cs = _("""
    
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

    boo = cs.collections['boo']

    assert isinstance(boo.admin, AdminExtra)
    assert cs.admin is True
    assert [x.name for x in boo.admin.admin_list] == ['weight', 'size_x', 'size_y', 'color_front']


def test_admin_exclude():
    cs = _("""
    
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

    boo = cs.collections['boo']

    assert isinstance(boo.admin, AdminExtra)
    assert cs.admin is True
    assert [x.name for x in boo.admin.admin_list] == ['weight', 'size_y', 'color_back']


def test_admin_exclude_wildcard():
    cs = _("""
    
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

    boo = cs.collections['boo']

    assert isinstance(boo.admin, AdminExtra)
    assert cs.admin is True
    assert [x.name for x in boo.admin.admin_list] == ['weight', 'size_x', 'size_y']


def test_admin_include_wildcard():
    cs = _("""
    
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

    boo = cs.collections['boo']

    assert isinstance(boo.admin, AdminExtra)
    assert cs.admin is True
    assert [x.name for x in boo.admin.admin_list] == ['weight', 'size_x', 'size_y']


def test_admin_list():
    cs = _("""
    
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

    boo = cs.collections['boo']

    assert isinstance(boo.admin, AdminExtra)
    assert cs.admin is True
    assert [x.name for x in boo.admin.admin_list] == ['abc', 'cda']
    assert [x.name for x in boo.admin.read_only] == ['abc', 'cda']
    assert [x.name for x in boo.admin.list_editable] == ['abc', 'cda']
    assert [x.name for x in boo.admin.list_filter] == ['abc', 'cda']
    assert [x.name for x in boo.admin.list_search] == ['abc', 'cda']
    assert [x.name for x in boo.admin.fields] == ['abc', 'cda']


def test_admin_tabs_all():
    cs = _("""
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

    boo = cs.collections['boo']

    assert boo.admin.tabs == ['foo']
    assert boo.admin.tab_names == {'foo': 'Foo'}
    assert boo.admin.tab_fields == {
        'a': 'foo',
        'b': 'foo',
        'c': 'foo',
    }


def test_admin_tabs_inherited():
    cs = _("""
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

    foo = cs.collections['foo']

    assert foo.admin.tabs == ['general', 'foo']
    assert foo.admin.tab_names == {'general': 'General', 'foo': 'Foo'}
    assert foo.admin.tab_fields == {
        'a': 'foo',
        'b': 'foo',
        'c': 'foo',
        'd': 'general',
    }


def test_admin_tabs_inherited_merged():
    cs = _("""
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

    foo = cs.collections['db_data_source']

    assert foo.admin.tab_fields == {
        'name': 'general',
        'database': 'general',
        'server': 'general',
    }

    assert foo.admin.tabs == ['general']
    assert foo.admin.tab_names == {'general': 'General'}

    foo = cs.collections['report_data_source']

    assert foo.admin.tab_fields == {
        'name': 'general',
        'report': 'general',
    }

    assert foo.admin.tabs == ['general']
    assert foo.admin.tab_names == {'general': 'General'}


def test_admin_tabs_all_but_some():
    cs = _("""
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

    boo = cs.collections['boo']

    assert boo.admin.tabs == ['foo', 'lolo']
    assert boo.admin.tab_names == {'foo': 'Foo', 'lolo': 'Lolo'}
    assert boo.admin.tab_fields == {
        'a': 'foo',
        'b': 'lolo',
        'c': 'foo',
        'd': 'lolo',
    }


def test_admin_tabs_verbose_name():
    cs = _("""
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

    boo = cs.collections['boo']

    assert boo.admin.tabs == ['foo']
    assert boo.admin.tab_names == {'foo': 'Фу'}
    assert boo.admin.tab_fields == {
        'a': 'foo',
        'b': 'foo',
        'c': 'foo',
    }


def test_admin_tabs_left_to_general():
    cs = _("""
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

    boo = cs.collections['boo']

    assert boo.admin.tabs == ['general', 'foo']
    assert boo.admin.tab_names == {'general': 'General', 'foo': 'Foo'}
    assert boo.admin.tab_fields == {
        'a': 'general',
        'b': 'foo',
        'c': 'foo',
    }


def test_admin_tabs_with_fields():
    cs = _("""
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

    boo = cs.collections['car']

    assert boo.admin.tabs == ['main', 'options']
    assert boo.admin.tab_fields == {
        'nr': 'main',
        'mark': 'main',
        'model': 'main',
        'crashed': 'options',
        'painted': 'options',
    }


def test_admin_inline_simple():
    cs = _("""
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

    foo = cs.collections['foo']
    bar = cs.collections['bar']

    assert len(foo.admin.inlines) == 1
    inline = foo.admin.inlines[0]

    assert isinstance(inline, AdminInlineConfig)
    assert inline.extra_count == 0
    assert inline.collection == foo
    assert inline.target_collection == bar
    assert inline.inline_type == 'tabular'
    assert inline.inline_name == 'lala'
    assert inline.source_field_name == 'rel'
    assert inline.field_names == ['c', 'd']


def test_admin_inline_inheritance():
    cs = _("""
    
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

    data_source = cs.collections['data_source']
    db_data_source = cs.collections['db_data_source']
    data_source_field = cs.collections['data_source_field']

    assert len(db_data_source.admin.inlines) == 1
    inline = db_data_source.admin.inlines[0]

    assert isinstance(inline, AdminInlineConfig)
    assert inline.collection == data_source
    assert inline.target_collection == data_source_field
    assert inline.inline_type == 'tabular'
    assert inline.inline_name == 'fields'
    assert inline.source_field_name == 'data_source'
    assert inline.field_names == ['name']


def test_admin_inline_endclass_with_parent():
    cs = _("""
    
    
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

    db_data_source = cs.collections['db_data_source']
    table = cs.collections['table']

    assert len(db_data_source.admin.inlines) == 1
    inline = db_data_source.admin.inlines[0]

    assert isinstance(inline, AdminInlineConfig)
    assert inline.collection == db_data_source
    assert inline.target_collection == table
    assert inline.inline_type == 'tabular'
    assert inline.inline_name == 'tables'
    assert inline.source_field_name == 'data_source'
    assert inline.field_names == ['name']


def test_admin_inline_details():
    cs = _("""
    
    #foo
    -------
    a
    b
    
    @admin(
        inline: lala(
            type: stacked
            extra: 300
            fields: *, ^c
        )
    )
    
    #bar
    --------
    rel: one(#foo -> lala)
    c
    d
    
    """)

    foo = cs.collections['foo']
    bar = cs.collections['bar']

    assert len(foo.admin.inlines) == 1
    inline = foo.admin.inlines[0]

    assert isinstance(inline, AdminInlineConfig)
    assert inline.extra_count == 300
    assert inline.inline_type == 'stacked'
    assert inline.field_names == ['d']


def test_admin_inline_tab():
    cs = _("""
    @suit
    
    #foo
    -------
    a
    b
    
    @admin(
        inline: lala(
            type: stacked
            extra: 300
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

    foo = cs.collections['foo']
    bar = cs.collections['bar']

    assert len(foo.admin.inlines) == 1
    inline = foo.admin.inlines[0]
    assert inline.tab == 'other'

    assert foo.admin.tabs == ['main', 'other']
    assert foo.admin.tab_fields == {
        'a': 'main',
        'b': 'main',
        'lala': 'other',
    }


def test_admin_js_css():
    cs = _("""

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

    foo = cs.collections['foo']

    assert foo.admin.css == [
        "foo.css", "another/boo.css"
    ]
    assert foo.admin.js == [
        "foo.js", "another/boo.js"
    ]

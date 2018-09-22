from textwrap import dedent

from zmei_generator.extras.admin import AdminExtra
from zmei_generator.parser.parser import parse_string
from zmei_generator.parser.populate import populate_collection_set


def _(code):
    tree = parse_string(dedent(code))

    return populate_collection_set(tree, 'example')


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

    assert boo.admin_list == boo.admin.admin_list
    assert boo.admin_read_only == boo.admin.read_only
    assert boo.admin_list_editable == boo.admin.list_editable
    assert boo.admin_list_filter == boo.admin.list_filter
    assert boo.admin_list_search == boo.admin.list_search
    assert boo.admin_fields == boo.admin.fields

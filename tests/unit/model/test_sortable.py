from textwrap import dedent

from zmei_generator.extras.model.admin import AdminExtra, AdminInlineConfig
from zmei_generator.parser.parser import parse_string
from zmei_generator.parser.populate import populate_collection_set


def _(code):
    tree = parse_string(dedent(code))

    return populate_collection_set(tree, 'example')


def test_sortable():
    cs = _("""
    
        #boo
        ----------
        abc
        cda
        
        @sortable(abc)
        
        #foo
        --------
        lala
    
    """)

    boo = cs.collections['boo']

    assert boo.sortable is True
    assert boo.sortable_field == ['abc']


def test_order():
    cs = _("""
    
        #boo
        ----------
        abc
        cda
        
        @order(abc,cda)
    
    """)

    boo = cs.collections['boo']

    assert boo.sortable is False
    assert boo.sortable_field == ['abc', 'cda']

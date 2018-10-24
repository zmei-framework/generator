from textwrap import dedent

import pytest
from zmei_generator.parser.parser import parse_string
from zmei_generator.parser.populate import populate_collection_set


def _(code):
    tree = parse_string(dedent(code))

    return populate_collection_set(tree, 'example')


def test_page_imports():
    cs = _("""
        from lala.lolo import Fofo, Hehe
        from lala.lolo import Dada
        from zoo import Foo1
        
        [boo]        
    """)

    assert cs.page_imports.get_items() == [
        ('lala.lolo', ['Fofo', 'Hehe', 'Dada']),
        ('zoo', ['Foo1']),
    ]


def test_model_imports():
    cs = _("""
        from lala.lolo import Fofo, Hehe
        from lala.lolo import Dada
        from zoo import Foo1
        
        #boo
        -----------    
    """)

    assert cs.model_imports.get_items() == [
        ('lala.lolo', ['Fofo', 'Hehe', 'Dada']),
        ('zoo', ['Foo1']),
    ]


def test_mixed_imports():
    cs = _("""
        from lala.lolo import Page
        
        [boo]
        
        
        from lala.lolo import Model
        
        #foo
        -----------    
    """)

    assert cs.page_imports.get_items() == [
        ('lala.lolo', ['Page']),
    ]

    assert cs.model_imports.get_items() == [
        ('lala.lolo', ['Model']),
    ]

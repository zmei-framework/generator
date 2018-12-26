from textwrap import dedent

import pytest
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_page_imports():
    cs = _("""
        from lala.lolo import Fofo, Hehe
        from lala.lolo import Dada
        from zoo import Foo1
        from zoo import *
        
        [boo]        
    """)

    assert cs.page_imports.get_items() == [
        ('lala.lolo', ['Fofo', 'Hehe', 'Dada']),
        ('zoo', ['*']),
    ]

    assert cs.page_imports.import_sting() == 'from lala.lolo import Fofo, Hehe, Dada\nfrom zoo import *'


def test_simple_imports():
    cs = _("""
        import datetime.datetime
        
        [boo]        
    """)

    assert cs.page_imports.get_items() == [
        (None, ['datetime.datetime']),
    ]

    assert cs.page_imports.import_sting() == 'import datetime.datetime'


def test_relative_imports():
    cs = _("""
        from .auth import *
        
        [boo]        
    """)

    assert cs.page_imports.get_items() == [
        ('.auth', ['*']),
    ]

    assert cs.page_imports.import_sting() == 'from .auth import *'


def test_page_imports_wildcard():
    cs = _("""
        from zoo import Foo1
        from zoo import *
        
        [boo]        
    """)

    assert cs.page_imports.get_items() == [
        ('zoo', ['*']),
    ]


def test_page_imports_wildcard_with_alias():
    cs = _("""
        from zoo import Foo1
        from zoo import *
        from zoo import Boo1 as lala
        
        [boo]        
    """)

    assert cs.page_imports.get_items() == [
        ('zoo', ['*', 'Boo1 as lala']),
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

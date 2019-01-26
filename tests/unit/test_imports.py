from textwrap import dedent

import pytest
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_page_imports():
    app = _("""
        from lala.lolo import Fofo, Hehe
        from lala.lolo import Dada
        from zoo import Foo1
        from zoo import *
        
        [boo]        
    """)

    assert app.page_imports.get_items() == [
        ('lala.lolo', ['Fofo', 'Hehe', 'Dada']),
        ('zoo', ['*']),
    ]

    assert app.page_imports.import_sting() == 'from lala.lolo import Fofo, Hehe, Dada\nfrom zoo import *'


def test_simple_imports():
    app = _("""
        import datetime.datetime
        
        [boo]        
    """)

    assert app.page_imports.get_items() == [
        (None, ['datetime.datetime']),
    ]

    assert app.page_imports.import_sting() == 'import datetime.datetime'


def test_relative_imports():
    app = _("""
        from .auth import *
        
        [boo]        
    """)

    assert app.page_imports.get_items() == [
        ('.auth', ['*']),
    ]

    assert app.page_imports.import_sting() == 'from .auth import *'


def test_page_imports_wildcard():
    app = _("""
        from zoo import Foo1
        from zoo import *
        
        [boo]        
    """)

    assert app.page_imports.get_items() == [
        ('zoo', ['*']),
    ]


def test_page_imports_wildcard_with_alias():
    app = _("""
        from zoo import Foo1
        from zoo import *
        from zoo import Boo1 as lala
        
        [boo]        
    """)

    assert app.page_imports.get_items() == [
        ('zoo', ['*', 'Boo1 as lala']),
    ]


def test_model_imports():
    app = _("""
        from lala.lolo import Fofo, Hehe
        from lala.lolo import Dada
        from zoo import Foo1
        
        #boo
        -----------    
    """)

    assert app.model_imports.get_items() == [
        ('lala.lolo', ['Fofo', 'Hehe', 'Dada']),
        ('zoo', ['Foo1']),
    ]


def test_mixed_imports():
    app = _("""
        from lala.lolo import Page
        
        [boo]
        
        
        from lala.lolo import Model
        
        #foo
        -----------    
    """)

    assert app.page_imports.get_items() == [
        ('lala.lolo', ['Page']),
    ]

    assert app.model_imports.get_items() == [
        ('lala.lolo', ['Model']),
    ]

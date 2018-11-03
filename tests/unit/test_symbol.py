from textwrap import dedent

from zmei_generator.parser.parser import ZmeiParser
from zmei_generator.parser.symbols import SymbolTable


def _(code):
    tree = ZmeiParser().parse_string(dedent(code))

    symbols = SymbolTable()
    symbols.update_from_tree(tree)

    return symbols


def test_pages():
    assert _("""
    
        [boo]
        [bar]
        [foo]
    
    """).page_names() == ['boo', 'bar', 'foo']


def test_page_fields():
    assert _("""
    
        [boo]
        lala:= 123
        lolo:= 123
        lele:= 123
        
        [bar]
        [foo]
    
    """).page_fields('boo') == ['lala', 'lolo', 'lele']


def test_models():
    assert _("""
    
        #boo
        ---------
        abc
        
        #bar
        ---------
        abc
        
        #foo
        ---------
        abc
        
    
    """).model_names() == ['boo', 'bar', 'foo']


def test_models_fields():
    assert _("""
    
        #boo
        ---------
        lala
        lolo
        lele
        
        #bar
        ---------
        abc
        
        #foo
        ---------
        abc
    
    """).model_fields('boo') == ['lala', 'lolo', 'lele']

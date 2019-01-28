from textwrap import dedent

from zmei_generator.generator.application import ZmeiProjectParser
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_simple_page():
    app = _("""
        [boo: /]
    """)

    boo = app.pages['boo']

    assert boo.get_extension_bases() == [
        'ZmeiDataViewMixin'
    ]


def test_simple_inherited_page():
    app = _("""
        [boo: /]
        [boo->foo: /]
        
    """)

    boo = app.pages['boo']
    foo = app.pages['foo']

    assert boo.get_extension_bases() == [
        'ZmeiDataViewMixin'
    ]

    assert foo.get_extension_bases() == []

def test_simple_inherited2_page():
    app = _("""
        [boo: /]
        [boo->foo: /]
        [foo->zoo: /]
        
    """)

    boo = app.pages['boo']
    foo = app.pages['foo']
    zoo = app.pages['zoo']

    assert boo.get_extension_bases() == [
        'ZmeiDataViewMixin'
    ]
    assert foo.get_extension_bases() == []
    assert zoo.get_extension_bases() == []


def test_simple_inherited2_page_with_functions():
    app = _("""
        [boo: /]
        loo()
        
        [boo->foo: /]
        loo()
        
        [foo->zoo: /]
        loo()
        
    """)

    boo = app.pages['boo']
    foo = app.pages['foo']
    zoo = app.pages['zoo']

    assert boo.get_extension_bases() == [
        'ZmeiRemoteInvocationViewMixin'
    ]
    assert foo.get_extension_bases() == []
    assert zoo.get_extension_bases() == []


def test_long_inherited_page():
    app_parser = ZmeiProjectParser()
    app_parser.add_file('main.col', """    
            [bar: /bar]
        """)

    app_parser.add_file('another.col', """    
            [main.bar->boo: ./boo]
            [goo]
        """)

    app = app_parser.parse()

    main_app = app.get_application('main')
    another_app = app.get_application('another')

    bar = main_app.pages['bar']
    boo = another_app.pages['boo']
    goo = another_app.pages['goo']

    assert bar.get_extension_bases() == [
        'ZmeiDataViewMixin'
    ]

    assert boo.get_extension_bases() == []

    assert goo.get_extension_bases() == [
        'ZmeiDataViewMixin'
    ]


def test_long_inherited_page_with_functions():
    app_parser = ZmeiProjectParser()
    app_parser.add_file('main.col', """    
            [bar: /bar]
            boo()
        """)

    app_parser.add_file('another.col', """    
            [main.bar->boo: ./boo]
            doo()
            
            [goo]
            loo()
        """)

    app = app_parser.parse()

    main_app = app.get_application('main')
    another_app = app.get_application('another')

    bar = main_app.pages['bar']
    boo = another_app.pages['boo']
    goo = another_app.pages['goo']

    assert bar.get_extension_bases() == [
        'ZmeiRemoteInvocationViewMixin'
    ]

    assert boo.get_extension_bases() == []

    assert goo.get_extension_bases() == [
        'ZmeiRemoteInvocationViewMixin'
    ]

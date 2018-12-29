from textwrap import dedent

from zmei_generator.generator.application import ZmeiAppParser
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_simple_page():
    cs = _("""
        [boo: /]
    """)

    boo = cs.pages['boo']

    assert boo.get_extra_bases() == [
        'ZmeiDataViewMixin'
    ]


def test_simple_inherited_page():
    cs = _("""
        [boo: /]
        [boo->foo: /]
        
    """)

    boo = cs.pages['boo']
    foo = cs.pages['foo']

    assert boo.get_extra_bases() == [
        'ZmeiDataViewMixin'
    ]

    assert foo.get_extra_bases() == []

def test_simple_inherited2_page():
    cs = _("""
        [boo: /]
        [boo->foo: /]
        [foo->zoo: /]
        
    """)

    boo = cs.pages['boo']
    foo = cs.pages['foo']
    zoo = cs.pages['zoo']

    assert boo.get_extra_bases() == [
        'ZmeiDataViewMixin'
    ]
    assert foo.get_extra_bases() == []
    assert zoo.get_extra_bases() == []


def test_simple_inherited2_page_with_functions():
    cs = _("""
        [boo: /]
        loo()
        
        [boo->foo: /]
        loo()
        
        [foo->zoo: /]
        loo()
        
    """)

    boo = cs.pages['boo']
    foo = cs.pages['foo']
    zoo = cs.pages['zoo']

    assert boo.get_extra_bases() == [
        'ZmeiRemoteInvocationViewMixin'
    ]
    assert foo.get_extra_bases() == []
    assert zoo.get_extra_bases() == []


def test_long_inherited_page():
    app_parser = ZmeiAppParser()
    app_parser.add_file('main.col', """    
            [bar: /bar]
        """)

    app_parser.add_file('another.col', """    
            [main.bar->boo: ./boo]
            [goo]
        """)

    app = app_parser.parse()

    main_app = app.get_collection_set('main')
    another_app = app.get_collection_set('another')

    bar = main_app.pages['bar']
    boo = another_app.pages['boo']
    goo = another_app.pages['goo']

    assert bar.get_extra_bases() == [
        'ZmeiDataViewMixin'
    ]

    assert boo.get_extra_bases() == []

    assert goo.get_extra_bases() == [
        'ZmeiDataViewMixin'
    ]


def test_long_inherited_page_with_functions():
    app_parser = ZmeiAppParser()
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

    main_app = app.get_collection_set('main')
    another_app = app.get_collection_set('another')

    bar = main_app.pages['bar']
    boo = another_app.pages['boo']
    goo = another_app.pages['goo']

    assert bar.get_extra_bases() == [
        'ZmeiRemoteInvocationViewMixin'
    ]

    assert boo.get_extra_bases() == []

    assert goo.get_extra_bases() == [
        'ZmeiRemoteInvocationViewMixin'
    ]

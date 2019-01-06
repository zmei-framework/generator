from textwrap import dedent

import pytest
from zmei_generator.extras.page.flutter import FlutterPageExtra
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_page_flutter():
    cs = _("""

        [boo]
        @flutter
        
        #foo
        ------
        lala
    """)

    assert len(cs.pages) == 1

    assert cs.flutter is True
    boo = cs.pages['boo']

    assert boo.name == 'boo'
    assert isinstance(boo.flutter, FlutterPageExtra)


def test_page_flutter_parent_is_also_flutter():
    cs = _("""
    
        [foo]

        [foo->boo]
        @flutter
        
        #foo
        ------
        lala
    """)

    assert len(cs.pages) == 2

    assert cs.flutter is True
    boo = cs.pages['boo']
    foo = cs.pages['foo']

    assert boo.name == 'boo'
    assert isinstance(boo.flutter, FlutterPageExtra)
    assert isinstance(foo.flutter, FlutterPageExtra)


def test_page_flutter_child_if_not_marked():
    cs = _("""
    
        [foo]
        @flutter()

        [foo->boo]
    """)

    assert len(cs.pages) == 2

    assert cs.flutter is True
    foo = cs.pages['foo']
    boo = cs.pages['boo']

    assert boo.name == 'boo'
    assert isinstance(foo.flutter, FlutterPageExtra)
    assert foo.flutter.include_child is False
    assert not boo.flutter


def test_page_flutter_child_if_marked():
    cs = _("""
    
        [foo]
        @flutter(child: true)

        [foo->boo]
    """)

    assert len(cs.pages) == 2

    assert cs.flutter is True
    foo = cs.pages['foo']
    boo = cs.pages['boo']

    assert boo.name == 'boo'
    assert isinstance(foo.flutter, FlutterPageExtra)
    print(foo.flutter.include_child)
    assert foo.flutter.include_child is True
    assert isinstance(boo.flutter, FlutterPageExtra)


def test_page_flutter_child_if_marked_deeper():
    cs = _("""
    
        [foo]
        @flutter(child: true)

        [foo->boo]
        [boo->zoo]
    """)

    assert len(cs.pages) == 3

    assert cs.flutter is True
    foo = cs.pages['foo']
    boo = cs.pages['boo']
    zoo = cs.pages['zoo']

    assert boo.name == 'boo'
    assert isinstance(foo.flutter, FlutterPageExtra)
    assert foo.flutter.include_child is True

    assert isinstance(boo.flutter, FlutterPageExtra)
    assert isinstance(zoo.flutter, FlutterPageExtra)
    assert zoo.flutter is foo.flutter


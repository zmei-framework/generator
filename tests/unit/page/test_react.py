from textwrap import dedent

import pytest
from zmei_generator.parser.parser import parse_string
from zmei_generator.parser.populate import populate_collection_set


def _(code):
    tree = parse_string(dedent(code))

    return populate_collection_set(tree, 'example')


def test_page_react():
    cs = _("""

        [boo]
        @react {
            <Foo>test</Foo>
        }
        
        #foo
        ------
        lala
    """)

    assert len(cs.pages) == 1

    boo = cs.pages['boo']

    assert boo.name == 'boo'
    assert boo.blocks['content'][0].source == "<Foo>test</Foo>"
    assert boo.react is True
    assert boo.extra_bases == ['ZmeiReactViewMixin']


def test_page_react_another_area():
    cs = _("""

        [boo]
        @react.foo {
            <Foo>test</Foo>
        }
        
        #foo
        ------
        lala
    """)

    assert len(cs.pages) == 1

    boo = cs.pages['boo']

    assert boo.name == 'boo'
    assert boo.blocks['foo'][0].source == "<Foo>test</Foo>"
    assert boo.react is True
    assert boo.extra_bases == ['ZmeiReactViewMixin']

from textwrap import dedent

import pytest
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_page_markdown():
    cs = _("""

        [boo]
        @markdown {
            # test
        }
        
        #foo
        ------
        lala
    """)

    assert len(cs.pages) == 1

    boo = cs.pages['boo']

    assert boo.name == 'boo'
    assert boo.blocks['content'][0].source == "<h1>test</h1>"
    assert boo.react is False
    assert boo.extra_bases == ['ZmeiDataViewMixin']

def test_page_markdown_area():
    cs = _("""

        [boo]
        @markdown.foo {
            # test
        }
        
        #foo
        ------
        lala
    """)

    assert len(cs.pages) == 1

    boo = cs.pages['boo']

    assert boo.name == 'boo'
    assert boo.blocks['foo'][0].source == "<h1>test</h1>"
    assert boo.react is False
    assert boo.extra_bases == ['ZmeiDataViewMixin']

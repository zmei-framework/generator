from textwrap import dedent

import pytest
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_page_markdown():
    app = _("""

        [boo]
        @markdown {
            # test
        }
        
        #foo
        ------
        lala
    """)

    assert len(app.pages) == 1

    boo = app.pages['boo']

    assert boo.name == 'boo'
    assert boo.blocks['content'][0].context['content'] == "<h1>test</h1>"
    assert boo.extension_bases == ['ZmeiDataViewMixin']


def test_page_markdown_area():
    app = _("""

        [boo]
        @markdown.foo {
            # test
        }
        
        #foo
        ------
        lala
    """)

    assert len(app.pages) == 1

    boo = app.pages['boo']

    assert boo.name == 'boo'
    assert boo.blocks['foo'][0].context['content'] == "<h1>test</h1>"
    assert boo.extension_bases == ['ZmeiDataViewMixin']

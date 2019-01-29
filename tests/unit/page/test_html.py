from textwrap import dedent

import pytest
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_page_html():
    app = _("""

        [boo]
        @html {
            <h1>test</h1>
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



def test_page_html_area():
    app = _("""

        [boo]
        @html.foo {
            <h1>test</h1>
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


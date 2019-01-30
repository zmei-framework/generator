from textwrap import dedent

import pytest
from zmei_generator.contrib.react.extensions.page.react import ReactPageExtension
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_page_react():
    app = _("""

        [boo]
        @react
        
        #foo
        ------
        lala
    """)

    assert len(app.pages) == 1

    boo = app.pages['boo']

    assert boo.name == 'boo'
    assert boo.supports(ReactPageExtension)
    assert boo.get_extension_bases() == ['ZmeiReactViewMixin']

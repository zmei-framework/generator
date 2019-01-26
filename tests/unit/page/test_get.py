from textwrap import dedent

import pytest
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_page_get_with_code():
    app = _("""

        [boo]
        @get {
            lala
        }
    """)

    boo = app.pages['boo']

    assert boo.page_code == '\nif request.method == "GET":\n    lala'



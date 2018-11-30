from textwrap import dedent

import pytest
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_page_get_with_code():
    cs = _("""

        [boo]
        @get {
            lala
        }
    """)

    boo = cs.pages['boo']

    assert boo.page_code == '\nif request.method == "GET":\n    lala'



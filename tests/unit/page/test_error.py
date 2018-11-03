from textwrap import dedent

import pytest

from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_page_error404():
    cs = _("""

        [boo]
        @error(404)
    """)

    boo = cs.pages['boo']

    assert 404 in boo.handlers


def test_page_error502():
    cs = _("""

        [boo]
        @error(502)
    """)

    boo = cs.pages['boo']

    assert 502 in boo.handlers

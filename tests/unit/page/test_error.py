from textwrap import dedent

import pytest

from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_page_error404():
    app = _("""

        [boo]
        @error(404)
    """)

    boo = app.pages['boo']

    assert 404 in boo.handlers


def test_page_error502():
    app = _("""

        [boo]
        @error(502)
    """)

    boo = app.pages['boo']

    assert 502 in boo.handlers

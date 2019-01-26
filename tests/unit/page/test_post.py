from textwrap import dedent

import pytest
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_page_post():
    app = _("""

        [boo]
        @post
    """)

    boo = app.pages['boo']

    assert boo.allow_post is True


def test_page_post_with_code():
    app = _("""

        [boo]
        @post {
            lala
        }
    """)

    boo = app.pages['boo']

    assert boo.allow_post is True
    assert boo.page_code == '\nif request.method == "POST":\n    lala'



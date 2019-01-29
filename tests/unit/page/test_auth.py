from textwrap import dedent

import pytest

from zmei_generator.contrib.web.extensions.page.auth import AuthPageExtension
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_page_auth():
    app = _("""

        [boo]
        @auth
    """)

    assert len(app.pages) == 1

    boo = app.pages['boo']

    assert boo[AuthPageExtension].is_added is True
    assert 'AccessMixin' in boo.extension_bases


def test_page_auth_custom():
    app = _("""

        [boo]
        @auth { lalala whatever here }
    """)

    assert len(app.pages) == 1

    boo = app.pages['boo']

    assert boo[AuthPageExtension].is_added is True
    assert 'AccessMixin' in boo.extension_bases

    # ensure the expression is inserted somehow in a page
    assert 'lalala whatever here' in boo.methods['dispatch']



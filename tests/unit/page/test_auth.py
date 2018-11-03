from textwrap import dedent

import pytest
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_page_auth():
    cs = _("""

        [boo]
        @auth
    """)

    assert len(cs.pages) == 1

    boo = cs.pages['boo']

    assert boo.auth is not None
    assert 'AccessMixin' in boo.extra_bases


def test_page_auth_custom():
    cs = _("""

        [boo]
        @auth { lalala whatever here }
    """)

    assert len(cs.pages) == 1

    boo = cs.pages['boo']

    assert boo.auth is not None
    assert 'AccessMixin' in boo.extra_bases

    # ensure the expression is inserted somehow in a page
    assert 'lalala whatever here' in boo.methods['dispatch']



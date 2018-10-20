from textwrap import dedent

import pytest
from zmei_generator.parser.parser import parse_string
from zmei_generator.parser.populate import populate_collection_set


def _(code):
    tree = parse_string(dedent(code))

    return populate_collection_set(tree, 'example')


def test_page_post():
    cs = _("""

        [boo]
        @post
    """)

    boo = cs.pages['boo']

    assert boo.allow_post is True
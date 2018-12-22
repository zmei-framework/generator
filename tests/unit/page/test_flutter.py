from textwrap import dedent

import pytest
from zmei_generator.extras.page.flutter import FlutterPageExtra
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_page_flutter():
    cs = _("""

        [boo]
        @flutter
        
        #foo
        ------
        lala
    """)

    assert len(cs.pages) == 1

    assert cs.flutter is True
    boo = cs.pages['boo']

    assert boo.name == 'boo'
    assert isinstance(boo.flutter, FlutterPageExtra)

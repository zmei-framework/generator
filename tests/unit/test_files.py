
from textwrap import dedent

from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_file_is_stored():
    cs = _("""

        @file "test.txt" {
            lala: 123
        }

    """)

    assert cs.files['test.txt'] == "lala: 123"

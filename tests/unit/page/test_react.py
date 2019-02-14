from textwrap import dedent

import pytest
from zmei_generator.contrib.react.extensions.page.react import ReactPageExtension
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_page_react():
    app = _("""

        [boo]
        @react
        
        #foo
        ------
        lala
    """)

    assert len(app.pages) == 1

    boo = app.pages['boo']

    assert boo.name == 'boo'
    assert boo.supports(ReactPageExtension)
    assert boo.get_extension_bases() == ['ZmeiReactViewMixin']


@pytest.mark.skip
def test_page_react_child_if_marked_deeper():
    app = _("""

        [foo]
        @react(child: true)

        [foo->boo]
        [boo->zoo]
    """)

    assert len(app.pages) == 3

    foo = app.pages['foo']
    boo = app.pages['boo']
    zoo = app.pages['zoo']

    assert foo.supports(ReactPageExtension)
    assert foo[ReactPageExtension].include_child is True

    assert boo.supports(ReactPageExtension)
    assert zoo.supports(ReactPageExtension)
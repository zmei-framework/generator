from textwrap import dedent

import pytest
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_page_react():
    app = _("""

        [boo]
        @react {
            <Foo>test</Foo>
        }
        
        #foo
        ------
        lala
    """)

    assert len(app.pages) == 1

    boo = app.pages['boo']

    assert boo.name == 'boo'
    assert boo.blocks['content'][0].source == "<Foo>test</Foo>"
    assert boo.react is True
    assert boo.extra_bases == ['ZmeiReactViewMixin']


@pytest.mark.parametrize("extra_type_name, client_enabled, server_enabled", [
    ("react", True, True),
    ("react_client", True, False),
    ("react_server", False, True),
])
def test_page_react_type(extra_type_name, client_enabled, server_enabled):
    app = _(f"""

        [boo]
        @{extra_type_name} {{
            <Foo>test</Foo>
        }}
    """)

    page_boo = app.pages['boo']
    assert page_boo.react is True
    assert page_boo.react_client is client_enabled
    assert page_boo.react_server is server_enabled


def test_page_react_another_area():
    app = _("""

        [boo]
        @react.foo {
            <Foo>test</Foo>
        }
        
        #foo
        ------
        lala
    """)

    assert len(app.pages) == 1

    boo = app.pages['boo']

    assert boo.name == 'boo'
    assert boo.blocks['foo'][0].source == "<Foo>test</Foo>"
    assert boo.react is True
    assert boo.extra_bases == ['ZmeiReactViewMixin']

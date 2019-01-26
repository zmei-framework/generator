from textwrap import dedent

from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_theme_default():
    app = _("""
        
    """)

    assert app.theme is None
    assert app.theme_install is False


def test_theme_change():
    app = _("""
        @theme(bluma)
    """)

    assert app.theme == 'bluma'
    assert app.theme_install is False


def test_theme_change_install():
    app = _("""
        @theme(bluma, install=true)
    """)

    assert app.theme == 'bluma'
    assert app.theme_install is True


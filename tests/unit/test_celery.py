from textwrap import dedent

from zmei_generator.contrib.celery.extensions.application.celery import CeleryAppExtension

from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_suit():
    app = _("""
        @celery
    """)

    assert 'celery' in app.get_required_deps()

    assert app.supports(CeleryAppExtension)

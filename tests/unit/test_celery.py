from textwrap import dedent

from zmei_generator.contrib.celery.extras.application.celery import CeleryAppExtra

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

    assert isinstance(app.celery, CeleryAppExtra)

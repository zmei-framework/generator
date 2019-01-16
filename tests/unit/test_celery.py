from textwrap import dedent

import pytest
from zmei_generator.extras.collection_set.celery import CeleryCsExtra

from zmei_generator.extras.collection_set.suit import SuitCsExtra
from zmei_generator.extras.model.admin import AdminExtra, AdminInlineConfig
from zmei_generator.parser.errors import TabsSuitRequiredValidationError
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_suit():
    cs = _("""
        @celery
    """)

    assert 'celery' in cs.get_required_deps()

    assert isinstance(cs.celery, CeleryCsExtra)

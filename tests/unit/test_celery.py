from textwrap import dedent

import pytest

from zmei_generator.extras.collection_set.suit import SuitCsExtra
from zmei_generator.extras.model.admin import AdminExtra, AdminInlineConfig
from zmei_generator.parser.errors import TabsSuitRequiredValidationError
from zmei_generator.parser.parser import parse_string
from zmei_generator.parser.populate import populate_collection_set


def _(code):
    tree = parse_string(dedent(code))

    return populate_collection_set(tree, 'example')


def test_suit():
    cs = _("""
        @celery
    """)

    assert 'celery' in cs.get_required_deps()
    # assert isinstance(cs.celery, SuitCsExtra)

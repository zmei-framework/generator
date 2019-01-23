from textwrap import dedent

import pytest
from zmei_generator.extras.collection_set.suit import SuitCsExtra
from zmei_generator.parser.errors import TabsSuitRequiredValidationError
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_theme_default():
    cs = _("""
        
    """)

    assert cs.theme is None
    assert cs.theme_install is False


def test_theme_change():
    cs = _("""
        @theme(bluma)
    """)

    assert cs.theme == 'bluma'
    assert cs.theme_install is False


def test_theme_change_install():
    cs = _("""
        @theme(bluma, install=true)
    """)

    assert cs.theme == 'bluma'
    assert cs.theme_install is True


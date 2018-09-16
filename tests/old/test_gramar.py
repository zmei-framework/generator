import pytest
from pyparsing import ParseException

from zmei_generator.config.grammar import ref, page_header, page_item, page, collection_set, class_name, ref_or_class_name, extra, extras


def test_page_header():
    parsed = page_header.parseString('[index:/boo/]')
    assert parsed.page_name == 'index'
    assert parsed.uri == '/boo/'

def test_collection_ref():
    assert ref.parseString('#boo').ref == 'boo'


def test_class_name():
    assert class_name.parseString('cratis_profile.User').class_name == 'cratis_profile.User'


def test_ref_or_class_name():
    assert ref_or_class_name.parseString('cratis_profile.User').class_name == 'cratis_profile.User'
    assert ref_or_class_name.parseString('#boo').ref == 'boo'


def test_collection_ref_can_not_have_space():
    with pytest.raises(ParseException):
        ref.parseString('# boo')


def test_extra():
    result = extra.parseString('@foo {123}')

    assert result.extra_name == 'foo'
    assert result.extra_body == '123'


def test_extras():
    result = extras.parseString("""
@foo {123}
@boo {321}
    """)

    assert result.extras[0].extra_name == 'foo'
    assert result.extras[0].extra_body == '123'

    assert result.extras[1].extra_name == 'boo'
    assert result.extras[1].extra_body == '321'


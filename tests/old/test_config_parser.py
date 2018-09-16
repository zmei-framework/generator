import re

from zmei_generator.config.parser import Parser


def clear_spaces(config):
    return re.sub(r'^\s+([^\s])', r'\1', config, flags=re.MULTILINE)


def test_unicode_collection_name():
    parser = Parser()
    result = parser.parse_config(clear_spaces("""
            #foo: Сосиска
            ----------
            title
            """), 'boo')

    assert result.collections['foo'].name == 'Сосиска'

def test_unicode_collection_multiword_name():
    parser = Parser()
    result = parser.parse_config(clear_spaces("""
            #foo: Сосиска редиска
            ----------
            title
            """), 'boo')

    assert result.collections['foo'].name == 'Сосиска редиска'


def test_unicode_collection_multiword_plural():
    parser = Parser()
    result = parser.parse_config(clear_spaces("""
            #foo: Сосиска редиска/Сосиски редиски
            ----------
            title
            """), 'boo')

    assert result.collections['foo'].name == 'Сосиска редиска'
    assert result.collections['foo'].name_plural == 'Сосиски редиски'


def test_unicode_multiword_field_translation():
    parser = Parser()
    result = parser.parse_config(clear_spaces("""
            #foo
            ----------
            title /Шикарный заголовок
            """), 'boo')

    assert result.collections['foo'].fields['title'].verbose_name == 'Шикарный заголовок'

# def test_unicode_multiword_field_translation_and_help():
#     parser = Parser()
#     result = parser.parse_config(clear_spaces("""
#             #foo
#             ----------
#             title /Шикарный заголовок ? и хелппп
#             """), 'boo')
#
#     assert result.collections['foo'].fields['title'].verbose_name == 'Шикарный заголовок'
#     assert result.collections['foo'].fields['title'].help == 'и хелппп'


def test_whitespaces_ignored():
    parser = Parser()
    result = parser.parse_config(clear_spaces("""
        #foo
        ----------
        title
        """), 'boo')

    assert 'foo' in result.collections


def test_multiple_verbose_names():
    parser = Parser()
    result = parser.parse_config(clear_spaces("""
        #foo
        ----------
        title /Заголовок
        text /Текст
        """), 'boo')

    assert result.collections['foo'].fields['title'].verbose_name == 'Заголовок'
    assert result.collections['foo'].fields['text'].verbose_name == 'Текст'


def test_custom_to_string():
    parser = Parser()
    result = parser.parse_config(clear_spaces("""
        #foo
        ----------
        ="Boo {.title}"
        title /Заголовок
        text /Текст
        """), 'boo')

    assert result.collections['foo'].to_string == "Boo {.title}"

#
# def test_simple_collection():
#
#     parser = Parser()
#     result = parser.parse_config("""
#         #foo_bar
#         ----------
#         title
#         """, 'boo')
#
#     assert isinstance(result, CollectionSetDef)
#
#     foo = result.collections['foo_bar']
#
#     assert isinstance(foo, CollectionDef)
#     assert foo.name == 'FooBar'
#
#     title = foo.fields['title']
#
#     assert isinstance(title, FieldDef)
#
#     assert isinstance(title, TextFieldDef)
#     assert title.options == {}


from textwrap import dedent

import pytest
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_pages():
    cs = _("""
    
        [boo: /lala/foo : foo/mytpl.html]
        [bar as yoo]
        [boo->foo : : {some_expr}]
    
    """)

    assert len(cs.pages) == 3

    boo = cs.page_list()[0]
    bar = cs.page_list()[1]
    foo = cs.page_list()[2]

    assert boo.name == 'boo'
    assert boo.url_alias == 'boo'
    assert boo.uri == '/lala/foo'
    assert boo.defined_uri == '/lala/foo'
    assert boo.parsed_template_name == 'foo/mytpl.html'

    assert bar.name == 'bar'
    assert bar.url_alias == 'yoo'

    assert foo.name == 'foo'
    assert foo.parent_name == 'boo'
    assert foo.parent_name == 'boo'
    assert foo.parsed_template_expr == 'some_expr'


def test_home_page():
    cs = _("""
    
        [boo: /]
    """)

    assert len(cs.pages) == 1

    boo = cs.page_list()[0]

    assert boo.name == 'boo'
    assert boo.uri == '/'


def test_i18n_url():
    cs = _("""

        [boo: $/lala/]
    """)

    assert len(cs.pages) == 1

    boo = cs.page_list()[0]

    assert boo.name == 'boo'
    assert boo.uri == '/lala/'
    assert boo.i18n is True


def test_inherited_normal_url():
    cs = _("""
    
        [foo: /a/]
        [foo->boo: /b/]
    """)

    assert len(cs.pages) == 2

    boo = cs.pages['boo']

    assert boo.uri == '/b/'

def test_inherited_local_url():
    cs = _("""
    
        [foo: /a/]
        [foo->boo: ./b/]
    """)

    assert len(cs.pages) == 2

    boo = cs.pages['boo']

    assert boo.uri == '/a/b/'


def test_inherited_local_url_i18n():
    cs = _("""

        [foo: $/a/]
        [foo->boo: ./b/]
    """)

    assert len(cs.pages) == 2

    boo = cs.pages['boo']

    assert boo.uri == '/a/b/'
    assert boo.i18n is True

def test_page_code():
    cs = _("""

        [boo] {
            That's my code!
        }
    """)

    assert len(cs.pages) == 1

    boo = cs.pages['boo']

    assert boo.name == 'boo'
    assert boo.page_code == "That's my code!"


def test_page_items():
    cs = _("""

        [boo]
        lala:= 123
        boo:= a + lala
        sitemap:= 321
    """)

    assert len(cs.pages) == 1

    boo = cs.pages['boo']

    assert len(boo.page_items) == 2
    assert boo.page_items['lala'].expression == '123'
    assert boo.page_items['boo'].expression == 'a + lala'

    # sitemap is special case
    assert boo.sitemap_expr.expression == '321'


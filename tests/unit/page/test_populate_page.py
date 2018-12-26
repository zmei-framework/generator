from textwrap import dedent

import pytest

from zmei_generator.extras.page.stream import StreamPageExtra
from zmei_generator.parser.parser import ZmeiParser
from zmei_generator.parser.errors import GlobalScopeValidationError as ValidationException, \
    ReactAndChannelsRequiredValidationError


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_pages():
    cs = _("""
    
        [boo: /lala/foo : foo/mytpl.html]
        [bar as yoo]
        [boo->foo : : {some_expr}]
        [foo->zoo]
        [goo]
    """)

    assert len(cs.pages) == 5

    boo = cs.page_list()[0]
    bar = cs.page_list()[1]
    foo = cs.page_list()[2]
    zoo = cs.page_list()[3]
    goo = cs.page_list()[4]

    assert boo.name == 'boo'
    assert boo.url_alias == 'boo'
    assert boo.uri == '/lala/foo'
    assert boo.defined_uri == '/lala/foo'
    assert boo.parsed_template_name == 'foo/mytpl.html'

    assert bar.name == 'bar'
    assert bar.url_alias == 'yoo'

    assert foo.name == 'foo'
    assert foo.extend_name is False
    assert foo.parent_name == 'boo'
    assert foo.parsed_template_expr == 'some_expr'

    assert zoo.name == 'zoo'
    assert zoo.parent_name == 'foo'
    assert zoo.view_name == 'ZooView'

    assert goo.name == 'goo'
    assert goo.parent_name is None
    assert goo.view_name == 'GooView'


def test_pages_extend_name():
    cs = _("""
    
        [boo: /lala/foo : foo/mytpl.html]
        [bar as yoo]
        [boo~>foo : : {some_expr}]
        [boo_foo~>zoo]
        [goo]
    """)

    assert len(cs.pages) == 5

    boo = cs.page_list()[0]
    bar = cs.page_list()[1]
    foo = cs.page_list()[2]
    zoo = cs.page_list()[3]
    goo = cs.page_list()[4]

    assert boo.name == 'boo'
    assert boo.url_alias == 'boo'
    assert boo.uri == '/lala/foo'
    assert boo.defined_uri == '/lala/foo'
    assert boo.parsed_template_name == 'foo/mytpl.html'

    assert bar.name == 'bar'
    assert bar.url_alias == 'yoo'

    assert foo.name == 'boo_foo'
    assert foo.extend_name is True
    assert foo.parent_name == 'boo'
    assert foo.parsed_template_expr == 'some_expr'

    assert zoo.name == 'boo_foo_zoo'
    assert zoo.parent_name == 'boo_foo'
    assert zoo.view_name == 'BooFooZooView'

    assert goo.name == 'goo'
    assert goo.parent_name is None
    assert goo.view_name == 'GooView'


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
    
        @langs(en, ru)

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
    
        @langs(en, ru)

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


def test_page_func():
    cs = _("""

        [boo]
        lala:= 123
        
        loo() {
            lolo!
        }
        
        zoo(hoho, abc) {
            zozo!
        }
    """)

    assert len(cs.pages) == 1

    boo = cs.pages['boo']

    assert len(boo.functions) == 2
    assert boo.functions['loo'].args == []
    assert boo.functions['loo'].name == 'loo'
    assert boo.functions['loo'].body == 'lolo!'

    assert boo.functions['zoo'].args == ['hoho', 'abc']
    assert boo.functions['zoo'].name == 'zoo'
    assert boo.functions['zoo'].body == 'zozo!'


def test_page_stream_expr_no_react():
    with pytest.raises(ReactAndChannelsRequiredValidationError):
        cs = _("""
            @channels
            
            [boo]
            foo:= 123
            @stream(Article)
        """)


def test_page_stream_expr_no_channels():
    with pytest.raises(ReactAndChannelsRequiredValidationError):
        cs = _("""
    
            [boo]
            foo:= 123
            @react {
                <Foo />
            }
            
            @stream(foo.Article)
        """)


def test_page_stream_expr_react_after_stream():
    with pytest.raises(ReactAndChannelsRequiredValidationError):
        cs = _("""
    
            [boo]
            foo:= 123
            @stream(foo.Article)
            @react {
                <Foo />
            }
        """)


def test_page_stream_expr():
    cs = _("""
        @channels
        
        [boo]
        foo:= 123
        
        @react {
            <Foo />
        }
        @stream(foo.Article) 
        
    """)

    assert len(cs.pages) == 1

    boo = cs.pages['boo']

    assert boo.stream is not None
    assert isinstance(boo.stream, StreamPageExtra)
    assert len(boo.stream.models) == 1

    assert boo.stream.models[0].target == 'foo.Article'


def test_page_stream_expr_full_syntax():
    cs = _("""
        @channels
        
        [boo]
        foo:= 123
        zoo:= 123
        goo:= 123
        
        @react {
            <Foo />
        }
        @stream(
            #lala{me.name=="hoho"} => foo, goo
            #lolo
            #lulu => *
        )
        
        #lala
        -------
        name
        
        #lolo
        -------
        name

    """)

    assert len(cs.pages) == 1

    boo = cs.pages['boo']

    assert boo.stream is not None
    assert isinstance(boo.stream, StreamPageExtra)
    assert len(boo.stream.models) == 3

    m1 = boo.stream.models[0]
    m2 = boo.stream.models[1]
    m3 = boo.stream.models[2]

    assert m1.target == '#lala'
    assert m1.filter_expr == 'me.name=="hoho"'
    assert m1.fields == ['foo', 'goo']

    assert m2.target == '#lolo'
    assert m2.filter_expr is None
    assert m2.fields is None

    assert m3.target == '#lulu'
    assert m3.filter_expr is None
    assert m3.fields is None

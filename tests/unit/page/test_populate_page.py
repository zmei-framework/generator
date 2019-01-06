from textwrap import dedent

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
    assert zoo.view_name == 'ExampleZooView'

    assert goo.name == 'goo'
    assert goo.parent_name is None
    assert goo.view_name == 'ExampleGooView'


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
    assert foo.url_alias == 'boo_foo'
    assert foo.extend_name is True
    assert foo.parent_name == 'boo'
    assert foo.parsed_template_expr == 'some_expr'

    assert zoo.name == 'boo_foo_zoo'
    assert zoo.parent_name == 'boo_foo'
    assert zoo.view_name == 'ExampleBooFooZooView'

    assert goo.name == 'goo'
    assert goo.parent_name is None
    assert goo.view_name == 'ExampleGooView'


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
    assert boo.page_code == "That's my code!\n"


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


def test_page_func_url_and_request():
        cs = _("""

            [boo]
            lala:= 123

            loo(url, request)

            zoo(hoho, url, abc, request) {
                zozo!
            }
        """)

        assert len(cs.pages) == 1

        boo = cs.pages['boo']

        assert len(boo.functions) == 2
        assert boo.functions['loo'].args == []
        assert boo.functions['loo'].out_args == ['url', 'request']
        assert boo.functions['loo'].name == 'loo'
        assert boo.functions['loo'].body is None

        assert boo.functions['zoo'].args == ['hoho', 'abc']
        assert boo.functions['zoo'].out_args == ['hoho', 'url', 'abc', 'request']
        assert boo.functions['zoo'].name == 'zoo'
        assert boo.functions['zoo'].body == 'zozo!'


def test_page_func_imported():
    cs = _("""

        [boo]
        lala:= 123
        
        loo()
        zoo(hoho, abc)
    """)

    assert len(cs.pages) == 1

    boo = cs.pages['boo']

    assert len(boo.functions) == 2
    assert boo.functions['loo'].args == []
    assert boo.functions['loo'].name == 'loo'
    assert boo.functions['loo'].body is None

    assert boo.functions['zoo'].args == ['hoho', 'abc']
    assert boo.functions['zoo'].name == 'zoo'
    assert boo.functions['zoo'].body is None


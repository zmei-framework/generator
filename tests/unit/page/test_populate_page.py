from textwrap import dedent

from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_page_minimal():
    app = _("""

        [boo]
    """)

    assert len(app.pages) == 1

    boo = app.page_list()[0]

    assert boo.name == 'boo'


def test_pages():
    app = _("""
    
        [boo: /lala/foo : foo/mytpl.html]
        [bar as yoo]
        [boo->foo : : {some_expr}]
        [foo->zoo]
        [goo]
    """)

    assert len(app.pages) == 5

    boo = app.page_list()[0]
    bar = app.page_list()[1]
    foo = app.page_list()[2]
    zoo = app.page_list()[3]
    goo = app.page_list()[4]

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
    app = _("""
    
        [boo: /lala/foo : foo/mytpl.html]
        [bar as yoo]
        [boo~>foo : : {some_expr}]
        [boo_foo~>zoo]
        [goo]
    """)

    assert len(app.pages) == 5

    boo = app.page_list()[0]
    bar = app.page_list()[1]
    foo = app.page_list()[2]
    zoo = app.page_list()[3]
    goo = app.page_list()[4]

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
    app = _("""
    
        [boo: /]
    """)

    assert len(app.pages) == 1

    boo = app.page_list()[0]

    assert boo.name == 'boo'
    assert boo.uri == '/'


def test_i18n_url():
    app = _("""
    
        @langs(en, ru)

        [boo: $/lala/]
    """)

    assert len(app.pages) == 1

    boo = app.page_list()[0]

    assert boo.name == 'boo'
    assert boo.uri == '/lala/'
    assert boo.i18n is True


def test_inherited_normal_url():
    app = _("""
    
        [foo: /a/]
        [foo->boo: /b/]
    """)

    assert len(app.pages) == 2

    boo = app.pages['boo']

    assert boo.uri == '/b/'


def test_inherited_local_url():
    app = _("""
    
        [foo: /a/]
        [foo->boo: ./b/]
    """)

    assert len(app.pages) == 2

    boo = app.pages['boo']

    assert boo.uri == '/a/b/'


def test_inherited_local_url_i18n():
    app = _("""
    
        @langs(en, ru)

        [foo: $/a/]
        [foo->boo: ./b/]
    """)

    assert len(app.pages) == 2

    boo = app.pages['boo']

    assert boo.uri == '/a/b/'
    assert boo.i18n is True


def test_page_code():
    app = _("""

        [boo] {
            That's my code!
        }
    """)

    assert len(app.pages) == 1

    boo = app.pages['boo']

    assert boo.name == 'boo'
    assert boo.page_code == "That's my code!\n"


def test_page_items():
    app = _("""

        [boo]
        lala:= 123
        boo:= a + lala
    """)

    assert len(app.pages) == 1

    boo = app.pages['boo']

    assert len(boo.page_items) == 2
    assert boo.page_items['lala'].expression == '123'
    assert boo.page_items['boo'].expression == 'a + lala'


def test_page_func():
    app = _("""

        [boo]
        lala:= 123
        
        loo() {
            lolo!
        }
        
        zoo(hoho, abc) {
            zozo!
        }
    """)

    assert len(app.pages) == 1

    boo = app.pages['boo']

    assert len(boo.functions) == 2
    assert boo.functions['loo'].args == []
    assert boo.functions['loo'].name == 'loo'
    assert boo.functions['loo'].body == 'lolo!'

    assert boo.functions['zoo'].args == ['hoho', 'abc']
    assert boo.functions['zoo'].name == 'zoo'
    assert boo.functions['zoo'].body == 'zozo!'


def test_page_func_url_and_request():
        app = _("""

            [boo]
            lala:= 123

            loo(url, request)

            zoo(hoho, url, abc, request) {
                zozo!
            }
        """)

        assert len(app.pages) == 1

        boo = app.pages['boo']

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
    app = _("""

        [boo]
        lala:= 123
        
        loo()
        zoo(hoho, abc)
    """)

    assert len(app.pages) == 1

    boo = app.pages['boo']

    assert len(boo.functions) == 2
    assert boo.functions['loo'].args == []
    assert boo.functions['loo'].name == 'loo'
    assert boo.functions['loo'].body is None

    assert boo.functions['zoo'].args == ['hoho', 'abc']
    assert boo.functions['zoo'].name == 'zoo'
    assert boo.functions['zoo'].body is None


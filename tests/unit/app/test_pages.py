from zmei_generator.generator.application import ZmeiApp, ZmeiAppParser


def test_single_file():

    app_parser = ZmeiAppParser()
    app_parser.add_file('main.col', """    
        [boo: /lala/foo : foo/mytpl.html]
        [bar as yoo]
        [boo->foo : : {some_expr}]
        [foo->zoo]
        [goo]
    """)

    app = app_parser.parse()

    assert isinstance(app, ZmeiApp)

    cs = app.get_collection_set('main')

    assert cs.application is app
    assert cs.app_name == 'main'

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
    assert zoo.view_name == 'MainZooView'

    assert goo.name == 'goo'
    assert goo.parent_name is None
    assert goo.view_name == 'MainGooView'


def test_simple_reuse_another_app():

    app_parser = ZmeiAppParser()
    app_parser.add_file('main.col', """    
        [bar: /bar]
    """)

    app_parser.add_file('another.col', """    
        [main.bar->boo: ./boo]
        [goo]
    """)

    app = app_parser.parse()

    assert isinstance(app, ZmeiApp)

    main_app = app.get_collection_set('main')
    another_app = app.get_collection_set('another')

    assert main_app.application is app
    assert main_app.app_name == 'main'
    assert another_app.application is app
    assert another_app.app_name == 'another'

    assert len(main_app.pages) == 1
    assert len(another_app.pages) == 2

    bar = main_app.pages['bar']
    boo = another_app.pages['boo']
    goo = another_app.pages['goo']

    assert bar.name == 'bar'
    assert bar.parent_name is None

    assert boo.name == 'boo'
    assert boo.parent_name == 'main.bar'
    assert boo.get_parent() is bar

    assert goo.name == 'goo'
    assert goo.parent_name is None


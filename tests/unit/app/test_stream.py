from zmei_generator.extras.page.stream import StreamPageExtra
from zmei_generator.generator.application import ZmeiApp, ZmeiAppParser


def test_simple_reuse_another_app():

    app_parser = ZmeiAppParser()
    app_parser.add_file('main.col', """    
        @channels
        
        [bar: /bar]
        @react {}
        @stream(
            #another.foo
            #another.boo
        )
    """)

    app_parser.add_file('another.col', """    
        #foo
        --------
        foo
        
        #boo
        --------
        boo
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

    bar = main_app.pages['bar']

    assert isinstance(bar.stream, StreamPageExtra)

    assert bar.stream.models[0].target == 'Foo'
    assert bar.stream.models[1].target == 'Boo'


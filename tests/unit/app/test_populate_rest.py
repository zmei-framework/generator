from zmei_generator.generator.application import ZmeiAppParser, ZmeiApp


def test_auth():

    app_parser = ZmeiAppParser()
    app_parser.add_file('main.col', """    
        #boo
        ----------
        abc
        cda

        @rest.yes(
            auth(basic,session,token: #another.my_token)
        )
        @rest.default()
    """)

    app_parser.add_file('another.col', """    
        #my_token
        -----------
        lala
    """)

    app = app_parser.parse()

    assert isinstance(app, ZmeiApp)

    main_app = app.get_collection_set('main')

    boo = main_app.collections['boo']

    assert boo.rest_conf['default'].auth_method_classes == []
    assert boo.rest_conf['default'].auth_methods == {}

    assert boo.rest_conf['yes'].auth_method_classes == [
        'BasicAuthentication', 'SessionAuthentication', 'BooYesTokenAuthentication']

    assert boo.rest_conf['yes'].auth_methods == {
        'basic': {},
        'session': {},
        'token': {'model': 'MyToken'},
    }

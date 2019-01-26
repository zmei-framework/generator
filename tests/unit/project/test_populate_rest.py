from zmei_generator.generator.application import ZmeiProjectParser, ZmeiProject


def test_auth():

    app_parser = ZmeiProjectParser()
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

    project = app_parser.parse()

    assert isinstance(project, ZmeiProject)

    main_app = project.get_application('main')

    boo = main_app.models['boo']

    assert boo.rest_conf['default'].auth_method_classes == []
    assert boo.rest_conf['default'].auth_methods == {}

    assert boo.rest_conf['yes'].auth_method_classes == [
        'BasicAuthentication', 'SessionAuthentication', 'BooYesTokenAuthentication']

    assert boo.rest_conf['yes'].auth_methods == {
        'basic': {},
        'session': {},
        'token': {'model': 'MyToken'},
    }

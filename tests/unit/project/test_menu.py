from zmei_generator.contrib.web.extensions.page.menu import MenuItem, MenuPageExtension
from zmei_generator.generator.application import ZmeiProjectParser, ZmeiProject


def test_menu_cases():
    app_parser = ZmeiProjectParser()
    app_parser.add_file('main.col', """    
        [base]
        @menu.main(
            "Home": page(another.index)
            Profile: page(dashboard)
        )
        
        [main.base->dashboard: /dashboard]
    """)

    app_parser.add_file('another.col', """    
        [main.base->index: /]        
        
    """)

    project = app_parser.parse()

    assert isinstance(project, ZmeiProject)

    main_app = project.get_application('main')

    base = main_app.pages['base']

    menu = base[MenuPageExtension]['main']

    assert menu.descriptor == 'main'
    assert len(menu.items) == 2

    assert isinstance(menu.items[0], MenuItem)
    assert isinstance(menu.items[1], MenuItem)

    assert menu.items[0].ref == 'item_0'
    assert menu.items[1].ref == 'item_1'

    assert menu.items[0].label == 'Home'
    assert menu.items[1].label == 'Profile'

    assert menu.items[0].page == 'another.index'
    assert menu.items[1].page == 'dashboard'

    assert menu.render_url(menu.items[0]) == "reverse_lazy('another.index')"
    assert menu.render_ref(menu.items[0]) == "another.index"
    assert menu.render_url(menu.items[1]) == "reverse_lazy('main.dashboard')"
    assert menu.render_ref(menu.items[1]) == "main.dashboard"

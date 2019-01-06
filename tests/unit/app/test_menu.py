from textwrap import dedent

import pytest

from zmei_generator.extras.page.menu import MenuItem
from zmei_generator.generator.application import ZmeiAppParser, ZmeiApp
from zmei_generator.parser.parser import ZmeiParser

def test_menu_cases():
    app_parser = ZmeiAppParser()
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

    app = app_parser.parse()

    assert isinstance(app, ZmeiApp)

    main_app = app.get_collection_set('main')

    base = main_app.pages['base']

    menu = base.menus['main']

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

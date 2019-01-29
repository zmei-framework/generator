from textwrap import dedent

from zmei_generator.contrib.web.extensions.page.menu import MenuItem, MenuPageExtension
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_menu_cases():
    app = _("""

        [base]
        @menu.main(
            "Home": page(index)
            Profile: page(dashboard)
        )
        
        [base->index: /]        
        [base->dashboard: /dashboard]
    """)

    base = app.pages['base']

    menu = base[MenuPageExtension]['main']

    assert menu.descriptor == 'main'
    assert len(menu.items) == 2

    assert isinstance(menu.items[0], MenuItem)
    assert isinstance(menu.items[1], MenuItem)

    assert menu.items[0].ref == 'item_0'
    assert menu.items[1].ref == 'item_1'

    assert menu.items[0].label == 'Home'
    assert menu.items[1].label == 'Profile'

    assert menu.items[0].page == 'index'
    assert menu.items[1].page == 'dashboard'


def test_menu_url():
    app = _("""

        [base]
        @menu.main(
            "Google": "https://google.com"
        )
    """)

    base = app.pages['base']

    menu = base[MenuPageExtension]['main']

    assert len(menu.items) == 1

    assert isinstance(menu.items[0], MenuItem)
    assert menu.items[0].ref == 'item_0'
    assert menu.items[0].label == 'Google'
    assert menu.items[0].url == '"https://google.com"'


def test_menu_expr():
    app = _("""

        [base]
        @menu.main(
            "Google" := reverse_lazy('some.page')
        )
    """)

    base = app.pages['base']

    menu = base[MenuPageExtension]['main']

    assert len(menu.items) == 1

    assert isinstance(menu.items[0], MenuItem)
    assert menu.items[0].ref == 'item_0'
    assert menu.items[0].label == 'Google'
    assert menu.items[0].expr == "reverse_lazy('some.page')"


def test_menu_args():
    app = _("""

        [base]
        @menu.main(
            [icon=lala] "Page": "Some"
            [icon="hoho", boo=lala] "Page2": "Other"
        )
    """)

    base = app.pages['base']

    menu = base[MenuPageExtension]['main']

    assert len(menu.items) == 2

    assert isinstance(menu.items[0], MenuItem)
    assert menu.items[0].ref == 'item_0'
    assert menu.items[0].label == 'Page'
    assert menu.items[0].url == '"Some"'
    assert menu.items[0].args == {'icon': 'lala'}

    assert isinstance(menu.items[1], MenuItem)
    assert menu.items[1].ref == 'item_1'
    assert menu.items[1].label == 'Page2'
    assert menu.items[1].url == '"Other"'
    assert menu.items[1].args == {'icon': 'hoho', 'boo': 'lala'}

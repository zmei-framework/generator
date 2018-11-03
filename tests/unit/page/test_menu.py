from textwrap import dedent

import pytest
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_menu_cases():
    cs = _("""

        [base]
        @menu.main(
            "Home": page(index)
            Profile: page(dashboard)
        )
        
        [base->index: /]        
        [base->dashboard: /dashboard]
    """)

    base = cs.pages['base']

    menu = base.menus['main']

    assert len(menu.items) == 2

    assert menu.items[0].ref == 'item_0'
    assert menu.items[1].ref == 'item_1'

    assert menu.items[0].label == 'Home'
    assert menu.items[1].label == 'Profile'

    assert menu.items[0].page == 'index'
    assert menu.items[1].page == 'dashboard'


def test_menu_url():
    cs = _("""

        [base]
        @menu.main(
            "Google": "https://google.com"
        )
    """)

    base = cs.pages['base']

    menu = base.menus['main']

    assert len(menu.items) == 1

    assert menu.items[0].ref == 'item_0'
    assert menu.items[0].label == 'Google'
    assert menu.items[0].url == 'https://google.com'


def test_menu_expr():
    cs = _("""

        [base]
        @menu.main(
            "Google" := reverse_lazy('some.page')
        )
    """)

    base = cs.pages['base']

    menu = base.menus['main']

    assert len(menu.items) == 1

    assert menu.items[0].ref == 'item_0'
    assert menu.items[0].label == 'Google'
    assert menu.items[0].expr == 'https://google.com'


def test_menu_args():
    cs = _("""

        [base]
        @menu.main(
            [icon=lala] "Page": "Some"
            [icon="hoho", boo=lala] "Page2": "Other"
        )
    """)

    base = cs.pages['base']

    menu = base.menus['main']

    assert len(menu.items) == 2

    assert menu.items[0].ref == 'item_0'
    assert menu.items[0].label == 'Page'
    assert menu.items[0].url == 'Some'
    assert menu.items[0].args == {'icon': 'lala'}

    assert menu.items[1].ref == 'item_1'
    assert menu.items[1].label == 'Page2'
    assert menu.items[1].url == 'Other'
    assert menu.items[1].args == {'icon': 'hoho', 'boo': 'lala'}
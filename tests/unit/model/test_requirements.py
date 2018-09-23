from textwrap import dedent

from zmei_generator.extras.admin import AdminExtra, AdminInlineConfig
from zmei_generator.parser.parser import parse_string
from zmei_generator.parser.populate import populate_collection_set


def _(code):
    tree = parse_string(dedent(code))

    return populate_collection_set(tree, 'example')


def test_admin_empty():
    cs = _("""
    
        #boo
        ----------
        a
    
        #boo->foo
        ----------
        b
    
    """)

    assert 'django-polymorphic' in cs.get_required_deps()
    assert 'polymorphic' in cs.get_required_apps()

from textwrap import dedent

from zmei_generator.extras.model.admin import AdminExtra, AdminInlineConfig
from zmei_generator.parser.parser import parse_string
from zmei_generator.parser.populate import populate_collection_set


def _(code):
    tree = parse_string(dedent(code))

    return populate_collection_set(tree, 'example')


def test_polymorphic():
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


def test_i18n():
    cs = _("""
    
        #boo
        ----------
        $a
    
    """)

    assert cs.translatable is True

    assert 'django-modeltranslation' in cs.get_required_deps()
    assert 'modeltranslation' in cs.get_required_apps()

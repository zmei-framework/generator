from textwrap import dedent

from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_tree_simple():
    app = _("""
    
        #boo
        ----------
        abc
        cda
        
        @tree
    
    """)

    boo = app.models['boo']

    assert boo.tree is True

    assert 'django-mptt' in app.deps
    assert 'django-polymorphic-tree' in app.deps
    assert 'mptt' in app.apps
    assert 'polymorphic_tree' in app.apps
    assert 'polymorphic' in app.apps



def test_tree_poly():
    app = _("""
    
        #boo
        ----------
        abc
        cda
        
        @tree(+polymorphic_list)
    
    """)

    boo = app.models['boo']

    assert boo.tree is True
    assert boo.tree_polymorphic_list is True

    assert 'django-mptt' in app.deps
    assert 'django-polymorphic-tree' in app.deps
    assert 'mptt' in app.apps
    assert 'polymorphic_tree' in app.apps
    assert 'polymorphic' in app.apps


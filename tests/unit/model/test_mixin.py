from textwrap import dedent

from zmei_generator.extras.model.admin import AdminExtra, AdminInlineConfig
from zmei_generator.parser.parser import parse_string
from zmei_generator.parser.populate import populate_collection_set


def _(code):
    tree = parse_string(dedent(code))

    return populate_collection_set(tree, 'example')


def test_mixin():
    cs = _("""
    
        #boo
        ----------
        abc
        cda
        
        @mixin(foo.bar.Baz)
    
    """)

    boo = cs.collections['boo']

    assert boo.mixin_classes == [('foo.bar', 'Baz', 'Baz')]


def test_mixin_same_name():
    cs = _("""
    
        #boo
        ----------
        abc
        cda
        
        @mixin(foo.bar.Boo)
    
    """)

    boo = cs.collections['boo']

    assert boo.mixin_classes == [('foo.bar', 'Boo', 'Boo_')]

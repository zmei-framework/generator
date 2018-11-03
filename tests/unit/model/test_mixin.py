from textwrap import dedent

from zmei_generator.extras.model.admin import AdminExtra, AdminInlineConfig
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


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

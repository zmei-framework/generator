from textwrap import dedent

from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_mixin():
    app = _("""
    
        #boo
        ----------
        abc
        cda
        
        @mixin(foo.bar.Baz)
    
    """)

    boo = app.models['boo']

    assert boo.mixin_classes == [('foo.bar', 'Baz', 'Baz')]


def test_mixin_same_name():
    app = _("""
    
        #boo
        ----------
        abc
        cda
        
        @mixin(foo.bar.Boo)
    
    """)

    boo = app.models['boo']

    assert boo.mixin_classes == [('foo.bar', 'Boo', 'Boo_')]

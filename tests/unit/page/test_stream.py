from textwrap import dedent

from zmei_generator.contrib.channels.extensions.pages.stream import StreamPageExtension
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_page_stream_expr():
    app = _("""
        [boo]
        foo:= 123
        
        @stream(foo.Article) 
        
    """)

    assert app.pages_support(StreamPageExtension)

    assert len(app.pages) == 1

    boo = app.pages['boo']

    assert boo.supports(StreamPageExtension)
    assert len(boo[StreamPageExtension].models) == 1

    assert boo[StreamPageExtension].models[0].model_class_name == 'Article'
    assert boo[StreamPageExtension].models[0].model_app_name == 'foo'


def test_page_stream_expr_full_syntax():
    app = _("""
        @channels
        
        [boo]
        foo:= 123
        zoo:= 123
        goo:= 123
        
        @react
        @stream(
            #lala{me.name=="hoho"} => foo, goo
            #lolo
            #lulu => *
        )
        
        #lala
        -------
        name
        
        #lolo
        -------
        name
        
        #lulu
        -------
        name

    """)

    assert len(app.pages) == 1

    boo = app.pages['boo']

    assert boo.supports(StreamPageExtension)
    assert len(boo[StreamPageExtension].models) == 3

    m1 = boo[StreamPageExtension].models[0]
    m2 = boo[StreamPageExtension].models[1]
    m3 = boo[StreamPageExtension].models[2]

    assert m1.model_class_name == 'Lala'
    assert m1.model_app_name == 'example'
    assert m1.filter_expr == 'me.name=="hoho"'
    assert m1.fields == ['foo', 'goo']

    assert m2.model_class_name == 'Lolo'
    assert m2.model_app_name == 'example'
    assert m2.filter_expr is None
    assert m2.fields is None

    assert m3.model_class_name == 'Lulu'
    assert m3.model_app_name == 'example'
    assert m3.filter_expr is None
    assert m3.fields is None

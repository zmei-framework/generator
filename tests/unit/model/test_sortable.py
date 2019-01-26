from textwrap import dedent

from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_sortable():
    app = _("""
    
        #boo
        ----------
        abc
        cda
        
        @sortable(abc)
        
        #foo
        --------
        lala
    
    """)

    boo = app.models['boo']

    assert boo.sortable is True
    assert boo.sortable_field == ['abc']


def test_order():
    app = _("""
    
        #boo
        ----------
        abc
        cda
        
        @order(abc,cda)
    
    """)

    boo = app.models['boo']

    assert boo.sortable is False
    assert boo.sortable_field == ['abc', 'cda']

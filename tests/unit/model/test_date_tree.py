from textwrap import dedent

from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_date_tree():
    app = _("""
    
        #boo
        ----------
        abc
        cda
        
        @date_tree(cda)
    
    """)

    boo = app.models['boo']

    assert boo.date_hierarchy == 'cda'

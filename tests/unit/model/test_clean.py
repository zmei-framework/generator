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
        
        @clean{
            lala + 3
        }
        
        #foo
        --------
        lala
    
    """)

    boo = app.models['boo']

    assert 'lala + 3' in boo.validators

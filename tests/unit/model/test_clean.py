from textwrap import dedent

from zmei_generator.extras.model.admin import AdminExtra, AdminInlineConfig
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_sortable():
    cs = _("""
    
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

    boo = cs.collections['boo']

    assert 'lala + 3' in boo.validators

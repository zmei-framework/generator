from textwrap import dedent

from zmei_generator.extras.model.admin import AdminExtra, AdminInlineConfig
from zmei_generator.parser.parser import parse_string
from zmei_generator.parser.populate import populate_collection_set


def _(code):
    tree = parse_string(dedent(code))

    return populate_collection_set(tree, 'example')


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

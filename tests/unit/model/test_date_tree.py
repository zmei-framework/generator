from textwrap import dedent

from zmei_generator.extras.model.admin import AdminExtra, AdminInlineConfig
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_date_tree():
    cs = _("""
    
        #boo
        ----------
        abc
        cda
        
        @date_tree(cda)
    
    """)

    boo = cs.collections['boo']

    assert boo.date_hierarchy == 'cda'

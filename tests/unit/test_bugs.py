from textwrap import dedent

from zmei_generator.extras.model.admin import AdminExtra, AdminInlineConfig
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_admin_empty():
    cs = _("""
    
        #boo
        ----------
        abc
        cda
    
        #foo
        ----------
        lolo: one(#boo)
    
        #zoo
        ----------
        lolo: one(#boo)
        
        @admin
    
    """)

    boo = cs.collections['boo']

    assert boo is not None


def test_reuse_of_last_state_error():
    cs = _("""
    
        #query
        --------
        foo
        
        #query~>select
        ----------------
        group
        
        
        #data_export
        --------------
        report
        
        #data_export~>csv
        -------------------
        server
        filename
        
        

    
    """)

    boo = cs.collections['query']

    assert boo is not None

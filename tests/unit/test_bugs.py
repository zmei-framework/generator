from textwrap import dedent

from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_admin_empty():
    app = _("""
    
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

    boo = app.models['boo']

    assert boo is not None


def test_reuse_of_last_state_error():
    app = _("""
    
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

    boo = app.models['query']

    assert boo is not None

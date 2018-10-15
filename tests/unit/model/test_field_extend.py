from textwrap import dedent

from zmei_generator.parser.parser import parse_string
from zmei_generator.parser.populate import populate_collection_set


def _(code):
    tree = parse_string(dedent(code))

    return populate_collection_set(tree, 'example')


def test_extend():
    cs = _("""
    
        #boo
        ----------
        abc: str(255) ..{whatever here}
        cda: str ..{whatever here}
        efg: str {whatever here}
        def: str
    
    """)

    boo = cs.collections['boo']
    field_abc = boo.fields['abc'].prepare_field_arguemnts({'max_length': 255})
    field_cda = boo.fields['cda'].prepare_field_arguemnts({'max_length': 100})
    field_efg = boo.fields['efg'].prepare_field_arguemnts({'max_length': 100})
    field_def = boo.fields['def'].prepare_field_arguemnts({'max_length': 100})

    assert field_abc['max_length'] == 255
    assert field_abc['_'] == 'whatever here'

    assert field_cda['max_length'] == 100
    assert field_cda['_'] == 'whatever here'

    assert field_efg == {'_': 'whatever here'}

    assert '_' not in field_def

from textwrap import dedent

from zmei_generator.contrib.web.fields.custom import CustomFieldDef
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_extend():
    app = _("""
    
        #boo
        ----------
        abc: str(255) ..{whatever here}
        cda: str ..{whatever here}
        efg: str {whatever here}
        def: str
        custom: {whatever here}
    
    """)

    boo = app.models['boo']
    field_abc = boo.fields['abc'].prepare_field_arguemnts({'max_length': 255})
    field_cda = boo.fields['cda'].prepare_field_arguemnts({'max_length': 100})
    field_efg = boo.fields['efg'].prepare_field_arguemnts({'max_length': 100})
    field_def = boo.fields['def'].prepare_field_arguemnts({'max_length': 100})
    field_custom = boo.fields['custom']

    assert field_abc['max_length'] == 255
    assert field_abc['_'] == 'whatever here'

    assert field_cda['max_length'] == 100
    assert field_cda['_'] == 'whatever here'

    assert field_efg == {'_': 'whatever here'}

    assert '_' not in field_def

    assert isinstance(field_custom, CustomFieldDef)
    assert field_custom.custom_declaration == 'whatever here'

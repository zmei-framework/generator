from textwrap import dedent

from zmei_generator.fields.date import DateFieldDef, DateTimeFieldDef, AutoNowDateTimeFieldDef, \
    AutoNowAddDateTimeFieldDef
from zmei_generator.fields.number import IntegerFieldDef, FloatFieldDef, DecimalFieldDef
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_date_field():
    cs = _("""

        #boo
        ----------
        a: date
    """)

    a = cs.collections['boo'].fields['a']

    assert isinstance(a, DateFieldDef)

    assert "models.DateField" in a.get_model_field()[1]


def test_datetime_field():
    cs = _("""

        #boo
        ----------
        a: datetime
    """)

    a = cs.collections['boo'].fields['a']

    assert isinstance(a, DateTimeFieldDef)

    assert "models.DateTimeField" in a.get_model_field()[1]


def test_update_time_field():
    cs = _("""

        #boo
        ----------
        a: update_time
    """)

    a = cs.collections['boo'].fields['a']

    assert isinstance(a, AutoNowDateTimeFieldDef)

    assert "models.DateTimeField" in a.get_model_field()[1]
    assert "auto_now=True" in a.get_model_field()[1]


def test_create_time_field():
    cs = _("""

        #boo
        ----------
        a: create_time
    """)

    a = cs.collections['boo'].fields['a']

    assert isinstance(a, AutoNowAddDateTimeFieldDef)

    assert "models.DateTimeField" in a.get_model_field()[1]
    assert "auto_now_add=True" in a.get_model_field()[1]


def test_auto_fields_are_read_only():
    cs = _("""

        #data_set_order
        -----------------
        created: create_time
        completed: datetime
        ref_id
        success: bool
        
        @admin(
            list: *
            read_only: ref_id, success
        )
    """)

    admin = cs.collections['data_set_order'].admin

    assert [x.name for x in admin.read_only] == ['ref_id', 'success', 'created']

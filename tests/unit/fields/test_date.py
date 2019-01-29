from textwrap import dedent

from zmei_generator.contrib.admin.extensions.model.admin import AdminModelExtension
from zmei_generator.contrib.web.fields.date import DateFieldDef, DateTimeFieldDef, AutoNowDateTimeFieldDef, \
    AutoNowAddDateTimeFieldDef
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_date_field():
    app = _("""

        #boo
        ----------
        a: date
    """)

    a = app.models['boo'].fields['a']

    assert isinstance(a, DateFieldDef)

    assert "models.DateField" in a.get_model_field()[1]


def test_datetime_field():
    app = _("""

        #boo
        ----------
        a: datetime
    """)

    a = app.models['boo'].fields['a']

    assert isinstance(a, DateTimeFieldDef)

    assert "models.DateTimeField" in a.get_model_field()[1]


def test_update_time_field():
    app = _("""

        #boo
        ----------
        a: update_time
    """)

    a = app.models['boo'].fields['a']

    assert isinstance(a, AutoNowDateTimeFieldDef)

    assert "models.DateTimeField" in a.get_model_field()[1]
    assert "auto_now=True" in a.get_model_field()[1]


def test_create_time_field():
    app = _("""

        #boo
        ----------
        a: create_time
    """)

    a = app.models['boo'].fields['a']

    assert isinstance(a, AutoNowAddDateTimeFieldDef)

    assert "models.DateTimeField" in a.get_model_field()[1]
    assert "auto_now_add=True" in a.get_model_field()[1]


def test_auto_fields_are_read_only():
    app = _("""

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

    admin = app.models['data_set_order'][AdminModelExtension]

    assert [x.name for x in admin.read_only] == ['ref_id', 'success', 'created']

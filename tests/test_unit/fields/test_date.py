from textwrap import dedent

from zmei_generator.fields.date import DateFieldDef, DateTimeFieldDef, AutoNowDateTimeFieldDef, \
    AutoNowAddDateTimeFieldDef
from zmei_generator.fields.number import IntegerFieldDef, FloatFieldDef, DecimalFieldDef
from zmei_generator.parser.parser import parse_string
from zmei_generator.parser.populate import populate_collection_set


def _(code):
    tree = parse_string(dedent(code))

    return populate_collection_set(tree, 'example')


def test_date_field():
    cs = _("""

        #boo
        ----------
        a: date
    """)

    a = cs.collections['boo'].fields['a']

    assert isinstance(a, DateFieldDef)


def test_datetime_field():
    cs = _("""

        #boo
        ----------
        a: datetime
    """)

    a = cs.collections['boo'].fields['a']

    assert isinstance(a, DateTimeFieldDef)


def test_update_time_field():
    cs = _("""

        #boo
        ----------
        a: update_time
    """)

    a = cs.collections['boo'].fields['a']

    assert isinstance(a, AutoNowDateTimeFieldDef)


def test_create_time_field():
    cs = _("""

        #boo
        ----------
        a: create_time
    """)

    a = cs.collections['boo'].fields['a']

    assert isinstance(a, AutoNowAddDateTimeFieldDef)

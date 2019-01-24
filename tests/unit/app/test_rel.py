from textwrap import dedent

from zmei_generator.domain import ReferenceField
from zmei_generator.generator.application import ZmeiAppParser, ZmeiApp
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_relation_works_in_any_order_across_app():
    app_parser = ZmeiAppParser()
    app_parser.add_file('main.col', """    
        #boo
        ----------
        a: one(#another.zoo -> boos)
    """)

    app_parser.add_file('another.col', """    
        #zoo
        ---------
        lala
    """)

    app = app_parser.parse()

    assert isinstance(app, ZmeiApp)

    main_app = app.get_collection_set('main')
    another_app = app.get_collection_set('another')

    zoo = another_app.collections['zoo']

    assert isinstance(zoo.fields['boos'], ReferenceField)

    assert main_app.collections['boo'].fields['a'].ref_collection is zoo


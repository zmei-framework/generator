from textwrap import dedent

from zmei_generator.domain.reference_field import ReferenceField
from zmei_generator.generator.application import ZmeiProjectParser, ZmeiProject
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_relation_works_in_any_order_across_app():
    project_parser = ZmeiProjectParser()
    project_parser.add_file('main.col', """    
        #boo
        ----------
        a: one(#another.zoo -> boos)
    """)

    project_parser.add_file('another.col', """    
        #zoo
        ---------
        lala
    """)

    app = project_parser.parse()

    assert isinstance(app, ZmeiProject)

    main_app = app.get_application('main')
    another_app = app.get_application('another')

    zoo = another_app.models['zoo']

    assert isinstance(zoo.fields['boos'], ReferenceField)

    assert main_app.models['boo'].fields['a'].ref_model is zoo


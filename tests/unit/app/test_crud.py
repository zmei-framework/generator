from textwrap import dedent

import pytest
from zmei_generator.generator.application import ZmeiApp, ZmeiAppParser

from zmei_generator.parser.errors import GlobalScopeValidationError as ValidationException
from zmei_generator.extras.page.crud import CrudParams, CrudPageExtra
from zmei_generator.extras.page.crud_create import CrudCreatePageExtra
from zmei_generator.extras.page.crud_delete import CrudDeletePageExtra
from zmei_generator.extras.page.crud_detail import CrudDetailPageExtra
from zmei_generator.extras.page.crud_edit import CrudEditPageExtra
from zmei_generator.parser.parser import ZmeiParser

@pytest.mark.parametrize("extra_type_name, extra_cls", [
    ("crud", CrudPageExtra),
    ("crud_create", CrudCreatePageExtra),
    ("crud_delete", CrudDeletePageExtra),
    ("crud_detail", CrudDetailPageExtra),
    ("crud_edit", CrudEditPageExtra),
])
def test_crud_model(extra_type_name, extra_cls):

    app_parser = ZmeiAppParser()
    app_parser.add_file('main.col', f"""    
        [boo: /mycrud]
        @{extra_type_name}(#another.foo)
    """)

    app_parser.add_file('another.col', """    
        #foo
        ------
        a
        b
        c
    """)

    app = app_parser.parse()

    assert isinstance(app, ZmeiApp)

    main_app = app.get_collection_set('main')

    assert main_app.crud is True

    boo = main_app.pages['boo']
    crud = boo.cruds['_'][extra_type_name]
    assert isinstance(crud, extra_cls)

    params = crud.params

    assert isinstance(params, CrudParams)
    assert params.model == '#another.foo'

    assert crud.app_name == 'another.models'
    assert crud.model_cls == 'Foo'

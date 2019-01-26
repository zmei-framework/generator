import pytest
from zmei_generator.generator.application import ZmeiProject, ZmeiProjectParser

from zmei_generator.contrib.web.extras.page.crud import CrudParams, CrudPageExtra
from zmei_generator.contrib.web.extras.page.crud_create import CrudCreatePageExtra
from zmei_generator.contrib.web.extras.page.crud_delete import CrudDeletePageExtra
from zmei_generator.contrib.web.extras.page.crud_detail import CrudDetailPageExtra
from zmei_generator.contrib.web.extras.page.crud_edit import CrudEditPageExtra


@pytest.mark.parametrize("extra_type_name, extra_cls", [
    ("crud", CrudPageExtra),
    ("crud_create", CrudCreatePageExtra),
    ("crud_delete", CrudDeletePageExtra),
    ("crud_detail", CrudDetailPageExtra),
    ("crud_edit", CrudEditPageExtra),
])
def test_crud_model(extra_type_name, extra_cls):

    app_parser = ZmeiProjectParser()
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

    project = app_parser.parse()

    assert isinstance(project, ZmeiProject)

    main_app = project.get_application('main')

    assert main_app.crud is True

    boo = main_app.pages['boo']
    crud = boo.cruds['_'][extra_type_name]
    assert isinstance(crud, extra_cls)

    params = crud.params

    assert isinstance(params, CrudParams)
    assert params.model == '#another.foo'

    assert crud.app_name == 'another.models'
    assert crud.model_cls == 'Foo'

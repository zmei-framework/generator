import pytest
from zmei_generator.generator.application import ZmeiProject, ZmeiProjectParser

from zmei_generator.contrib.web.extensions.page.crud import CrudParams, CrudPageExtension
from zmei_generator.contrib.web.extensions.page.crud_create import CrudCreatePageExtension
from zmei_generator.contrib.web.extensions.page.crud_delete import CrudDeletePageExtension
from zmei_generator.contrib.web.extensions.page.crud_detail import CrudDetailPageExtension
from zmei_generator.contrib.web.extensions.page.crud_edit import CrudEditPageExtension


@pytest.mark.parametrize("extension_type_name, extension_cls", [
    ("crud", CrudPageExtension),
    ("crud_create", CrudCreatePageExtension),
    ("crud_delete", CrudDeletePageExtension),
    ("crud_detail", CrudDetailPageExtension),
    ("crud_edit", CrudEditPageExtension),
])
def test_crud_model(extension_type_name, extension_cls):

    app_parser = ZmeiProjectParser()
    app_parser.add_file('main.col', f"""    
        [boo: /mycrud]
        @{extension_type_name}(#another.foo)
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
    crud = boo.cruds['_'][extension_type_name]
    assert isinstance(crud, extension_cls)

    params = crud.params

    assert isinstance(params, CrudParams)
    assert params.model == '#another.foo'

    assert crud.app_name == 'another.models'
    assert crud.model_cls == 'Foo'

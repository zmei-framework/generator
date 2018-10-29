from textwrap import dedent

import pytest

from zmei_generator.extras.page.crud import CrudParams, CrudPageExtra
from zmei_generator.extras.page.crud_create import CrudCreatePageExtra
from zmei_generator.extras.page.crud_delete import CrudDeletePageExtra
from zmei_generator.extras.page.crud_detail import CrudDetailPageExtra
from zmei_generator.extras.page.crud_edit import CrudEditPageExtra
from zmei_generator.parser.parser import parse_string
from zmei_generator.parser.populate import populate_collection_set


def _(code):
    tree = parse_string(dedent(code))

    return populate_collection_set(tree, 'example')

@pytest.mark.parametrize("extra_type_name, extra_cls", [
    ("crud", CrudPageExtra),
    ("crud_create", CrudCreatePageExtra),
    ("crud_delete", CrudDeletePageExtra),
    ("crud_detail", CrudDetailPageExtra),
    ("crud_edit", CrudEditPageExtra),
])
def test_crud_model(extra_type_name, extra_cls):
    cs = _(f"""

        [boo]
        @{extra_type_name}(#foo)
        
        #foo
        ------
        a
        b
        c
    """)

    assert cs.crud is True

    assert len(cs.pages) == 1

    boo = cs.pages['boo']
    assert isinstance(boo.cruds['_'][extra_type_name], extra_cls)

    params = boo.cruds['_'][extra_type_name].params

    assert isinstance(params, CrudParams)
    assert params.model == '#foo'

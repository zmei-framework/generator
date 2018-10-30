from textwrap import dedent

import pytest

from zmei_generator.config.domain.exceptions import ValidationException
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
def test_crud_no_uri_on_crud(extra_type_name, extra_cls):
    with pytest.raises(ValidationException):
        cs = _(f"""
    
            [boo]
            @{extra_type_name}(#foo)
            
            #foo
            ------
            a
            b
            c
        """)


@pytest.mark.parametrize("extra_type_name, extra_cls", [
    ("crud", CrudPageExtra),
    ("crud_create", CrudCreatePageExtra),
    ("crud_delete", CrudDeletePageExtra),
    ("crud_detail", CrudDetailPageExtra),
    ("crud_edit", CrudEditPageExtra),
])
def test_crud_model(extra_type_name, extra_cls):
    cs = _(f"""

        [boo: /mycrud]
        @{extra_type_name}(#foo)

        #foo
        ------
        a
        b
        c
    """)

    assert cs.crud is True

    boo = cs.pages['boo']
    assert isinstance(boo.cruds['_'][extra_type_name], extra_cls)

    params = boo.cruds['_'][extra_type_name].params

    assert isinstance(params, CrudParams)
    assert params.model == '#foo'


@pytest.mark.parametrize("extra_type_name", [
    "crud",
    "crud_create",
    "crud_delete",
    "crud_detail",
    "crud_edit",
])
def test_crud_theme(extra_type_name):
    cs = _(f"""

        [boo: /mycrud]
        @{extra_type_name}(
            #foo
            
            theme: lala
        )

        #foo
        ------
        a
        b
        c
    """)

    boo = cs.pages['boo']

    params = boo.cruds['_'][extra_type_name].params

    assert params.theme == 'lala'


def test_crud_subpages():
    cs = _(f"""

        [boo: /mycrud]
        @crud(#foo)

        #foo
        ------
        a
        b
        c
    """)

    assert cs.crud is True

    boo = cs.pages['boo']
    assert isinstance(boo.cruds['_']['crud'], CrudPageExtra)

    params = boo.cruds['_']['crud'].params

    assert isinstance(params, CrudParams)
    assert params.model == '#foo'

    assert len(cs.pages) == 5
    assert len(boo.children) == 4

    for page in boo.children:
        assert page.parent_name == boo.name
        assert page.defined_uri.startswith('/mycrud')

        if page.name == 'boo_create':
            assert 'CreateView' in page.extra_bases
        elif page.name == 'boo_edit':
            assert 'UpdateView' in page.extra_bases
        elif page.name == 'boo_detail':
            assert 'DetailView' in page.extra_bases
        elif page.name == 'boo_delete':
            assert 'DeleteView' in page.extra_bases
        else:
            pytest.fail('Wrong page name: ', page.name)

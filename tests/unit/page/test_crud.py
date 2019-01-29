from textwrap import dedent

import pytest
from zmei_generator.contrib.web.extensions.page.crud_list import CrudListPageExtension

from zmei_generator.parser.errors import GlobalScopeValidationError as ValidationException
from zmei_generator.contrib.web.extensions.page.crud import CrudParams, CrudPageExtension
from zmei_generator.contrib.web.extensions.page.crud_create import CrudCreatePageExtension
from zmei_generator.contrib.web.extensions.page.crud_delete import CrudDeletePageExtension
from zmei_generator.contrib.web.extensions.page.crud_detail import CrudDetailPageExtension
from zmei_generator.contrib.web.extensions.page.crud_edit import CrudEditPageExtension
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


@pytest.mark.parametrize("extension_type_name, extension_cls", [
    ("crud", CrudPageExtension),
    ("crud_list", CrudListPageExtension),
    ("crud_create", CrudCreatePageExtension),
    ("crud_delete", CrudDeletePageExtension),
    ("crud_detail", CrudDetailPageExtension),
    ("crud_edit", CrudEditPageExtension),
])
def test_crud_no_uri_on_crud(extension_type_name, extension_cls):
    with pytest.raises(ValidationException):
        app = _(f"""
    
            [boo]
            @{extension_type_name}(#foo)
            
            #foo
            ------
            a
            b
            c
        """)


def test_crud_same_descriptor():
    with pytest.raises(ValidationException):
        app = _(f"""
    
            [boo: /lala]
            @crud(#foo)
            @crud(#lala)
            @crud(#foo)
            @crud(#boo)
            
            #boo
            ------
            a
            
            #lala
            ------
            a
            
            #foo
            ------
            a
        """)


def test_crud_same_descriptor_different_annotations():
    app = _(f"""

        [boo: /lala]
        @crud(#foo)
        @crud_create(#boo)
        
        #boo
        ------
        a
        
        #foo
        ------
        a
    """)


def test_crud_diff_descriptor():
    app = _(f"""

        [boo: /lala]
        @crud(#foo)
        @crud.foo(#boo)
        
        #boo
        ------
        a
        
        #foo
        ------
        a
    """)


def test_crud_page_parsing():
    app = _("""

        [boo: /mycrud]        
        lala := 123
        
        @crud(#foo)

        #foo
        ------
        a
    """)

    boo = app.pages['boo']

    assert boo.page_items['lala'].expression == '123'


def test_crud_subpage_parsing():
    app = _("""

        [boo: /mycrud]
        zoo := 321
        
        @crud(#foo

            detail(
                lala := 123
                
                @markdown {
                    test
                }
            )
        )

        #foo
        ------
        a
    """)

    assert app.pages_support(CrudPageExtension) is True

    boo = app.pages['boo']
    boo_detail = app.pages['boo_detail']

    assert boo.page_items['zoo'].expression == '321'

    assert boo_detail.page_items['lala'].expression == '123'

    assert len(boo_detail.blocks['content']) == 2


def test_crud_subpage_subcrud():
    app = _("""

        [boo: /mycrud]
        zoo := 321
        
        @crud(#foo

            detail(
                lala := 123
                
                @crud.lala(#goo)
            )
        )

        #foo
        ------
        a
        
        #goo
        ------
        a
    """)

    assert app.pages_support(CrudPageExtension) is True

    boo = app.pages['boo']
    boo_detail = app.pages['boo_detail']
    #
    assert boo.page_items['zoo'].expression == '321'
    assert boo_detail.page_items['lala'].expression == '123'


@pytest.mark.parametrize("extension_type_name, extension_cls", [
    ("crud", CrudPageExtension),
    ("crud_list", CrudListPageExtension),
    ("crud_create", CrudCreatePageExtension),
    ("crud_delete", CrudDeletePageExtension),
    ("crud_detail", CrudDetailPageExtension),
    ("crud_edit", CrudEditPageExtension),
])
def test_crud_model(extension_type_name, extension_cls):
    app = _(f"""

        [boo: /mycrud]
        @{extension_type_name}(#foo)

        #foo
        ------
        a
        b
        c
    """)

    assert app.pages_support(CrudPageExtension) is True

    boo = app.pages['boo']
    crud = boo[CrudPageExtension]['_'][extension_type_name]
    assert isinstance(crud, extension_cls)

    params = crud.params

    assert isinstance(params, CrudParams)
    assert params.model == '#foo'
    assert crud.formatted_query == ".all()"


@pytest.mark.parametrize("extension_type_name", [
    "crud",
    "crud_list",
    "crud_create",
    "crud_delete",
    "crud_detail",
    "crud_edit",
])
def test_crud_theme(extension_type_name):
    app = _(f"""

        [boo: /mycrud]
        @{extension_type_name}(
            #foo
            
            theme: lala
        )

        #foo
        ------
        a
        b
        c
    """)

    boo = app.pages['boo']

    params = boo[CrudPageExtension]['_'][extension_type_name].params

    assert params.theme == 'lala'


def test_crud_subpages():
    app = _(f"""

        [boo: /mycrud]
        @crud(#foo)

        #foo
        ------
        a
        b
        c
    """)

    assert app.pages_support(CrudPageExtension) is True

    boo = app.pages['boo']
    assert isinstance(boo[CrudPageExtension]['_']['crud'], CrudPageExtension)

    params = boo[CrudPageExtension]['_']['crud'].params

    assert isinstance(params, CrudParams)
    assert params.model == '#foo'

    assert len(app.pages) == 5
    print(boo.children)

    for page in boo.children:
        assert page.parent_name == boo.name
        assert page.defined_uri.startswith('/mycrud')

        if page.name == 'boo_create':
            assert 'CreateView' in page.extension_bases
        elif page.name == 'boo_edit':
            assert 'UpdateView' in page.extension_bases
        elif page.name == 'boo_detail':
            assert 'DetailView' in page.extension_bases
        elif page.name == 'boo_delete':
            assert 'DeleteView' in page.extension_bases
        else:
            pytest.fail('Wrong page name: ', page.name)


def test_crud_subpages_skip():
    app = _(f"""

        [boo: /mycrud]
        @crud(#foo, skip: delete, edit)

        #foo
        ------
        a
        b
        c
    """)

    boo = app.pages['boo']

    assert len(app.pages) == 3

    for page in boo.children:
        if page.name == 'boo_create':
            assert 'CreateView' in page.extension_bases
        elif page.name == 'boo_detail':
            assert 'DetailView' in page.extension_bases
        else:
            pytest.fail('Wrong page name: ', page.name)


@pytest.mark.parametrize("extension_type_name", [
    "crud",
    "crud_list",
    "crud_create",
    "crud_delete",
    "crud_detail",
    "crud_edit",
])
def test_crud_model_fields(extension_type_name):
    app = _(f"""

        [boo: /mycrud]
        @{extension_type_name}(#foo, fields: *, ^b)

        #foo
        ------
        a
        b
        c
    """)

    assert app.pages_support(CrudPageExtension) is True

    boo = app.pages['boo']
    crud = boo[CrudPageExtension]['_'][extension_type_name]

    assert list(crud.fields.keys()) == ['a', 'c']

    assert list(crud.list_fields.keys()) == ['a', 'c']

@pytest.mark.parametrize("extension_type_name", [
    "crud",
    "crud_list",
    "crud_create",
    "crud_delete",
    "crud_detail",
    "crud_edit",
])
def test_crud_model_fields(extension_type_name):
    app = _(f"""

        [boo: /mycrud]
        @{extension_type_name}(#foo, fields: a, b{{lala}})

        #foo
        ------
        a
        b
        c
    """)

    assert app.pages_support(CrudPageExtension) is True

    boo = app.pages['boo']
    crud = boo[CrudPageExtension]['_'][extension_type_name]

    assert list(crud.fields.keys()) == ['a', 'b']
    assert list(crud.list_fields.keys()) == ['a', 'b']
    assert crud.field_filters['b'] == 'lala'


@pytest.mark.parametrize("extension_type_name", [
    "crud",
    "crud_list",
    "crud_create",
    "crud_delete",
    "crud_detail",
    "crud_edit",
])
def test_crud_model_list_fields(extension_type_name):
    app = _(f"""

        [boo: /mycrud]
        @{extension_type_name}(#foo, fields: *, ^b list_fields: *, ^c)

        #foo
        ------
        a
        b
        c
    """)

    assert app.pages_support(CrudPageExtension) is True

    boo = app.pages['boo']
    crud = boo[CrudPageExtension]['_'][extension_type_name]

    assert list(crud.fields.keys()) == ['a', 'c']

    assert list(crud.list_fields.keys()) == ['a', 'b']


@pytest.mark.parametrize("extension_type_name", [
    "crud",
    "crud_list",
    "crud_create",
    "crud_delete",
    "crud_detail",
    "crud_edit",
])
def test_crud_pk_param(extension_type_name):
    app = _(f"""

        [boo: /mycrud]
        @{extension_type_name}(#foo, pk_param: foo)

        #foo
        ------
        a
        b
        c
    """)

    assert app.pages_support(CrudPageExtension) is True

    boo = app.pages['boo']
    crud = boo[CrudPageExtension]['_'][extension_type_name].params

    assert crud.pk_param == "foo"


@pytest.mark.parametrize("extension_type_name", [
    "crud",
    "crud_list",
    "crud_create",
    "crud_delete",
    "crud_detail",
    "crud_edit",
])
def test_crud_item_name(extension_type_name):
    app = _(f"""

        [boo: /mycrud]
        @{extension_type_name}(#foo, item_name: foo)

        #foo
        ------
        a
        b
        c
    """)

    assert app.pages_support(CrudPageExtension) is True

    boo = app.pages['boo']
    crud = boo[CrudPageExtension]['_'][extension_type_name]
    params = boo[CrudPageExtension]['_'][extension_type_name].params

    assert params.item_name == "foo"

    # crud.prepare_environment(params, boo)

    assert crud.item_name == "foo"


@pytest.mark.parametrize("extension_type_name", [
    "crud",
    "crud_list",
    "crud_create",
    "crud_delete",
    "crud_detail",
    "crud_edit",
])
def test_crud_block(extension_type_name):
    app = _(f"""

        [boo: /mycrud]
        @{extension_type_name}(#foo, block: foo)

        #foo
        ------
        a
        b
        c
    """)

    assert app.pages_support(CrudPageExtension) is True

    boo = app.pages['boo']
    crud = boo[CrudPageExtension]['_'][extension_type_name].params

    assert crud.block_name == "foo"


@pytest.mark.parametrize("extension_type_name", [
    "crud",
    "crud_list",
    "crud_create",
    "crud_delete",
    "crud_detail",
    "crud_edit",
])
def test_crud_object_expr1(extension_type_name):
    app = _(f"""

        [boo: /mycrud]
        @{extension_type_name}(#foo, 
            object_expr := request.user
        )

        #foo
        ------
        a
        b
        c
    """)

    assert app.pages_support(CrudPageExtension) is True

    boo = app.pages['boo']
    crud = boo[CrudPageExtension]['_'][extension_type_name].params

    assert crud.object_expr == "request.user"


@pytest.mark.parametrize("extension_type_name", [
    "crud",
    "crud_list",
    "crud_create",
    "crud_delete",
    "crud_detail",
    "crud_edit",
])
def test_crud_object_expr2(extension_type_name):
    app = _(f"""

        [boo: /mycrud]
        @{extension_type_name}(#foo, 
            object_expr: {{request.user}}
        )

        #foo
        ------
        a
        b
        c
    """)

    assert app.pages_support(CrudPageExtension) is True

    boo = app.pages['boo']
    crud = boo[CrudPageExtension]['_'][extension_type_name].params

    assert crud.object_expr == "request.user"


@pytest.mark.parametrize("extension_type_name", [
    "crud",
    "crud_list",
    "crud_create",
    "crud_delete",
    "crud_detail",
    "crud_edit",
])
def test_header(extension_type_name):
    app = _(f"""

        [boo: /mycrud]
        @{extension_type_name}(#foo, 
            header: false
        )

        #foo
        ------
        a
        b
        c
    """)

    assert app.pages_support(CrudPageExtension) is True

    boo = app.pages['boo']
    crud = boo[CrudPageExtension]['_'][extension_type_name].params

    assert crud.header is False


@pytest.mark.parametrize("extension_type_name", [
    "crud",
    "crud_list",
    "crud_create",
    "crud_delete",
    "crud_detail",
    "crud_edit",
])
def test_header_default(extension_type_name):
    app = _(f"""

        [boo: /mycrud]
        @{extension_type_name}(#foo)

        #foo
        ------
        a
        b
        c
    """)

    assert app.pages_support(CrudPageExtension) is True

    boo = app.pages['boo']
    crud = boo[CrudPageExtension]['_'][extension_type_name].params

    assert crud.header is True


@pytest.mark.parametrize("extension_type_name", [
    "crud",
    "crud_list",
    "crud_create",
    "crud_delete",
    "crud_detail",
    "crud_edit",
])
def test_list_type(extension_type_name):
    app = _(f"""

        [boo: /mycrud]
        @{extension_type_name}(#foo, 
            list: stacked
        )

        #foo
        ------
        a
        b
        c
    """)

    assert app.pages_support(CrudPageExtension) is True

    boo = app.pages['boo']
    crud = boo[CrudPageExtension]['_'][extension_type_name].params

    assert crud.list_type == 'stacked'


@pytest.mark.parametrize("extension_type_name", [
    "crud",
    "crud_list",
    "crud_create",
    "crud_delete",
    "crud_detail",
    "crud_edit",
])
def test_list_type_default(extension_type_name):
    app = _(f"""

        [boo: /mycrud]
        @{extension_type_name}(#foo)

        #foo
        ------
        a
        b
        c
    """)

    assert app.pages_support(CrudPageExtension) is True

    boo = app.pages['boo']
    crud = boo[CrudPageExtension]['_'][extension_type_name].params

    assert crud.list_type == 'stacked'


@pytest.mark.parametrize("extension_type_name", [
    "crud",
    "crud_list",
    "crud_create",
    "crud_delete",
    "crud_detail",
    "crud_edit",
])
def test_crud_can_edit1(extension_type_name):
    app = _(f"""

        [boo: /mycrud]
        @{extension_type_name}(#foo, 
            can_edit := request.user
        )

        #foo
        ------
        a
        b
        c
    """)

    assert app.pages_support(CrudPageExtension) is True

    boo = app.pages['boo']
    crud = boo[CrudPageExtension]['_'][extension_type_name].params

    assert crud.can_edit == "request.user"


@pytest.mark.parametrize("extension_type_name", [
    "crud",
    "crud_list",
    "crud_create",
    "crud_delete",
    "crud_detail",
    "crud_edit",
])
def test_crud_can_edit2(extension_type_name):
    app = _(f"""

        [boo: /mycrud]
        @{extension_type_name}(#foo, 
            can_edit: {{request.user}}
        )

        #foo
        ------
        a
        b
        c
    """)

    assert app.pages_support(CrudPageExtension) is True

    boo = app.pages['boo']
    crud = boo[CrudPageExtension]['_'][extension_type_name].params

    assert crud.can_edit == "request.user"


@pytest.mark.parametrize("extension_type_name", [
    "crud",
    "crud_list",
    "crud_create",
    "crud_delete",
    "crud_detail",
    "crud_edit",
])
def test_crud_url_prefix(extension_type_name):
    app = _(f"""

        [boo: /mycrud]
        @{extension_type_name}(#foo, 
            url_prefix: "this/is/custom/prefix/"
        )

        #foo
        ------
        a
        b
        c
    """)

    assert app.pages_support(CrudPageExtension) is True

    boo = app.pages['boo']
    crud = boo[CrudPageExtension]['_'][extension_type_name].params

    assert crud.url_prefix == "this/is/custom/prefix/"


@pytest.mark.parametrize("extension_type_name", [
    "crud",
    "crud_list",
    "crud_create",
    "crud_delete",
    "crud_detail",
    "crud_edit",
])
def test_crud_link_suffix(extension_type_name):
    app = _(f"""

        [boo: /mycrud]
        @{extension_type_name}(#foo, 
            link_suffix: "category=url.category"
        )

        #foo
        ------
        a
        b
        c
    """)

    assert app.pages_support(CrudPageExtension) is True

    boo = app.pages['boo']
    crud = boo[CrudPageExtension]['_'][extension_type_name].params

    assert crud.link_suffix == "category=url.category"


@pytest.mark.parametrize("extension_type_name", [
    "crud",
    "crud_list",
    "crud_create",
    "crud_delete",
    "crud_detail",
    "crud_edit",
])
def test_crud_filter(extension_type_name):
    app = _(f"""

        [boo: /mycrud]
        @{extension_type_name}(#foo{{lala.lolo}})

        #foo
        ------
        a
        b
        c
    """)

    assert app.pages_support(CrudPageExtension) is True

    boo = app.pages['boo']
    crud = boo[CrudPageExtension]['_'][extension_type_name]

    assert crud.params.query == "lala.lolo"
    assert crud.formatted_query == ".filter(lala.lolo)"


@pytest.mark.parametrize("extension_type_name", [
    "crud_create",
    "crud_list",
    "crud_delete",
    "crud_detail",
    "crud_edit",
])
def test_crud_success_page(extension_type_name):
    app = _(f"""

        [boo: /mycrud]
        @{extension_type_name}(#foo
            => {{reverse_lazy('some_url', kwargs={{'param1': self.object.pk}})}}
        )

        #foo
        ------
        a
        b
        c
    """)

    assert app.pages_support(CrudPageExtension) is True

    boo = app.pages['boo']
    crud = boo[CrudPageExtension]['_'][extension_type_name]

    assert crud.params.next_page == {'all': "reverse_lazy('some_url', kwargs={'param1': self.object.pk})"}


def test_crud_success_page_main():
    app = _(f"""

        [boo: /mycrud]
        @crud(#foo
            => {{reverse_lazy('some_url', kwargs={{'param1': self.object.pk}})}}
        )

        #foo
        ------
        a
        b
        c
    """)

    assert app.pages_support(CrudPageExtension) is True

    for tname in ('create', 'delete', 'edit'):
        crud = app.pages[f'boo_{tname}'][CrudPageExtension]['_'][f'crud_{tname}']
        assert crud.params.next_page == {'all': "reverse_lazy('some_url', kwargs={'param1': self.object.pk})"}


def test_crud_success_page_main_create_only():
    app = _(f"""

        [boo: /mycrud]
        @crud(#foo
            (create) => {{reverse_lazy('some_url', kwargs={{'param1': self.object.pk}})}}
        )

        #foo
        ------
        a
        b
        c
    """)

    assert app.pages_support(CrudPageExtension) is True

    for tname in ('create', 'delete', 'edit'):
        crud = app.pages[f'boo_{tname}'][CrudPageExtension]['_'][f'crud_{tname}']
        if tname == 'create':
            assert crud.next_page_expr == "reverse_lazy('some_url', kwargs={'param1': self.object.pk})"
        else:
            assert crud.next_page_expr != "reverse_lazy('some_url', kwargs={'param1': self.object.pk})"


@pytest.mark.parametrize("extension_type_name", [
    "crud",
    "crud_list",
    "crud_create",
    "crud_delete",
    "crud_detail",
    "crud_edit",
])
def test_crud_success_url_dq(extension_type_name):
    app = _(f"""

        [boo: /mycrud]
        @{extension_type_name}(#foo
            => "https://google.com/"
        )

        #foo
        ------
        a
        b
        c
    """)

    assert app.pages_support(CrudPageExtension) is True

    boo = app.pages['boo']
    crud = boo[CrudPageExtension]['_'][extension_type_name]

    assert crud.params.next_page == {'all': '"https://google.com/"'}

@pytest.mark.parametrize("extension_type_name", [
    "crud",
    "crud_list",
    "crud_create",
    "crud_delete",
    "crud_detail",
    "crud_edit",
])
def test_crud_success_url_sq(extension_type_name):
    app = _(f"""

        [boo: /mycrud]
        @{extension_type_name}(#foo
            => 'https://google.com/'
        )

        #foo
        ------
        a
        b
        c
    """)

    assert app.pages_support(CrudPageExtension) is True

    boo = app.pages['boo']
    crud = boo[CrudPageExtension]['_'][extension_type_name]

    assert crud.params.next_page == {'all': "'https://google.com/'"}


@pytest.mark.parametrize("extension_type_name", [
    "crud",
    "crud_list",
    "crud_create",
    "crud_delete",
    "crud_detail",
    "crud_edit",
])
def test_crud_descriptor(extension_type_name):
    app = _(f"""

        [boo: /mycrud]
        @{extension_type_name}.zoo(#foo)

        #foo
        ------
        a
        b
        c
    """)

    assert app.pages_support(CrudPageExtension) is True

    boo = app.pages['boo']
    crud = boo[CrudPageExtension]['zoo'][extension_type_name]

    assert crud.descriptor == "zoo"


def test_crud_list():
    app = _(f"""

        [boo: /mycrud]
        @crud_list.zoo(#foo)

        #foo
        ------
        a
        b
        c
    """)

    assert app.pages_support(CrudPageExtension) is True

    boo = app.pages['boo']
    print(boo[CrudPageExtension])
    crud = boo[CrudPageExtension]['zoo']['crud_list']

    assert crud.skip == ['detail', 'create', 'edit', 'delete']



from xml.etree import ElementTree

import re

from cratis_generator.config.domain import PageExtra, ValidationException, PageExpression
from cratis_generator.config.grammar import identifier, field_name_spec
from pyparsing import *

from cratis_generator.extras.page.auth import add_page_auth
from cratis_generator.extras.page.block import PageBlock

field_filter = Optional(QuotedString('<', endQuoteChar='>')).setResultsName('filter_expr')
field = Group(field_name_spec.setResultsName('spec') + field_filter)

ref_parser = Combine(Literal('#') + Word(alphanums + '_')).setResultsName('model') + \
             Optional(QuotedString('<', endQuoteChar='>').setResultsName('query')) + \
             Optional(Suppress('fields:') + Group(delimitedList(field)).setResultsName('fields'))

class_parser = Word(alphanums + '_.').setResultsName('model') + \
               Optional(QuotedString('<', endQuoteChar='>').setResultsName('query'))

parser = ((ref_parser | class_parser) +
          Each([
              Optional(Suppress('fields:') + Group(delimitedList(
                  field_name_spec.setResultsName('spec') + field_filter)).setResultsName('fields')),
              Optional(Suppress('list_fields:') + Group(delimitedList(
                  field_name_spec.setResultsName('spec') + field_filter)).setResultsName('list_fields')),
              Optional(Suppress('skip:') + Group(delimitedList(
                  Literal('create') | Literal('edit') | Literal('delete') | Literal('detail') | Literal('list')
              )).setResultsName('skip')),
              Optional(Suppress('block:') + identifier.setResultsName('block_name')),
              Optional(Suppress('theme:') + identifier.setResultsName('theme')),
              Optional(Suppress('url_prefix:') + Word(alphanums + '-/').setResultsName('url_prefix')),
              Optional(Suppress('pk_param:') + Word(alphanums + '_').setResultsName('pk_param')),
              Optional(Suppress('object_expr:') + restOfLine.setResultsName('object_expr')),
              Optional(Suppress('edit_auth:') + restOfLine.setResultsName('edit_auth')),
              Optional(Suppress('item_name:') + Word(alphanums + '_').setResultsName('item_name')),
              Optional(Suppress('link_extra:') + QuotedString('"').setResultsName('link_extra')),
              Optional(Suppress('link_suffix:') + QuotedString('"').setResultsName('link_suffix'))
          ]) +
          Optional(Suppress('=>') + restOfLine.setResultsName('next_page'))
          ).ignore(cStyleComment)


class CrudPageExtra(PageExtra):
    @classmethod
    def get_name(cls):
        return 'crud'

    link_extra = None
    link_extra_params = None
    name_prefix = None
    name_suffix = None
    block_name = None
    theme = None
    url_prefix = None
    pk_param = None
    crud_pages = None
    app_name = None
    model_cls = None
    fields = None
    list_fields = None
    formatted_query = None
    context_object_name = None
    object_expr = None
    edit_auth = None
    query = None
    next_page_expr = None
    item_name = None
    field_filters = None
    create_list = True
    link_suffix = ''

    def __init__(self, parsed_result, page):
        super().__init__(parsed_result, page)

        page.collection_set.crud = True

        self.raw_extra_body = parsed_result.extra_body
        self.descriptor = parsed_result.descriptor or None

        crud = parser.parseString(parsed_result.extra_body, parseAll=True)

        self.prepare_environment(crud, page)
        self.build_pages(page)

    def prepare_environment(self, crud, page):
        # next page
        if crud.next_page:
            self.next_page_expr = f"return reverse({crud.next_page})" + self.link_suffix
        else:
            self.next_page_expr = f"return self.request.get_full_path()" + self.link_suffix

        self.field_filters = {}
        if crud.fields:
            all_fields = []
            for field in crud.fields:
                all_fields.append(field.spec)
                if field.filter_expr and not field.spec.startswith('^'):
                    self.field_filters[field.spec] = field.filter_expr

            crud.fields = all_fields

        # appname, model_cls, fields
        if crud.model.startswith('#'):
            self.app_name = page.collection_set.app_name + '.models'
            collection = page.collection_set.collections[crud.model[1:]]
            self.model_cls = collection.class_name
            self.fields = {field.name: field.verbose_name or field.name.replace('_', ' ').capitalize() for field in collection.filter_fields(crud.fields or '*') if not field.read_only}
            self.list_fields = {field.name: field.verbose_name or field.name.replace('_', ' ').capitalize() for field in collection.filter_fields(crud.list_fields or crud.fields or '*') if not field.read_only}
        else:
            parts = crud.model.split('.')
            self.app_name = '.'.join(parts[:-1]) + '.models'
            self.model_cls = parts[-1]
            self.fields = {field: field.replace('_', ' ').capitalize() for field in crud.fields}
            self.list_fields = {field: field.replace('_', ' ').capitalize() for field in crud.list_fields} or crud.fields
            if not self.fields:
                raise ValidationException('@crud -> fields for external models are required: {}'.format(crud.model))

        # link extra
        if len(crud.link_extra):
            self.link_extra = crud.link_extra
            link_extra_params = []
            for item in re.split('\s+', self.link_extra):
                key, val = item.split('=')
                link_extra_params.append(f"'{key}': {val}")
            self.link_extra_params = ', '.join(link_extra_params)
        else:
            self.link_extra = ''
            self.link_extra_params = ''

        if crud.link_suffix:
            self.link_suffix = crud.link_suffix

        # name_prefix
        if self.descriptor:
            self.name_prefix = f'{self.descriptor}_'
            self.name_suffix = f'_{self.descriptor}'
        else:
            self.name_prefix = ''
            self.name_suffix = ''

        # item name
        if crud.item_name:
            self.context_object_name = crud.item_name
        else:
            self.context_object_name = self.name_prefix + 'item'

        # block name
        if crud.block_name:
            self.block_name = crud.block_name
        elif self.descriptor:
            self.block_name = f'{self.descriptor}_content'
        else:
            self.block_name = 'content'

        # crud theme
        if crud.theme:
            self.theme = crud.theme

        # url prefix
        if crud.url_prefix:
            self.url_prefix = crud.url_prefix
            if not self.url_prefix.endswith('/'):
                self.url_prefix = self.url_prefix + '/'
        elif self.descriptor:
            self.url_prefix = f'{self.descriptor}/'
        else:
            self.url_prefix = ''
        if not page.defined_uri.endswith('/'):
            self.url_prefix = '/' + self.url_prefix

        # pk
        if crud.pk_param:
            self.pk_param = crud.pk_param
        elif self.descriptor:
            self.pk_param = f'{self.descriptor}_pk'
        else:
            self.pk_param = 'pk'

        # object
        if crud.object_expr:
            self.object_expr = 'self.object = ' + crud.object_expr
        else:
            self.object_expr = 'self.object = self.get_object()'

        # auth
        if crud.edit_auth:
            self.edit_auth = crud.edit_auth

        # formated_query
        self.query = crud.query.strip()
        if self.query != '':
            self.formatted_query = '.filter({})'.format(self.query)
        else:
            self.formatted_query = '.all()'

        if crud.skip:
            self.create_list = 'list' not in list(crud.skip)
        else:
            self.create_list = True

        # pages that are not needed
        self.crud_pages = [
            x for x in ['detail', 'create', 'edit', 'delete'] if x not in list(crud.skip or [])
        ]

    def prepare_block_fields(self, page):
        link_extra = self.link_extra
        if link_extra:
            link_extra = ' ' + link_extra

        # edit_auth = self.edit_auth or None
        edit_auth = None
        if edit_auth:
            edit_auth = edit_auth.strip()
            if len(edit_auth) == 0:
                edit_auth = None

            if edit_auth.startswith('data'):
                edit_auth = edit_auth[5:]

        ctx = {
            'link_suffix': '!' + repr(self.link_suffix),
            'edit_auth': '!' + repr(edit_auth),
            'fields': '!' + repr(self.fields),
            'list_fields': '!' + repr(self.list_fields),
            'meta': f'{self.name_prefix}{self.item_name}_meta',
            'item': f"{self.context_object_name}",
            'items': f"{self.context_object_name}_list",
            'by_id': f"{self.pk_param}={self.context_object_name}.pk",
            'crud_prefix': str(self.name_prefix)
        }

        if page:
            links = {'crud_' + x: f"'{page.collection_set.app_name}.{page.name}{self.name_suffix}_{x}'{link_extra}" for
                     x in
                     self.crud_pages}
            links['crud_list'] = f"'{page.collection_set.app_name}.{page.name}'{link_extra}"

            ctx.update(links)

        return ctx

    def build_pages(self, page):

        if self.create_list:
            page.imports.append(
                (self.app_name, self.model_cls)
            )

            page.page_items[f'{self.name_prefix}{self.item_name}_meta'] = PageExpression(
                f'{self.name_prefix}{self.item_name}_meta', f"{self.model_cls}._meta", page)

            page.page_items[f'_{self.context_object_name}_list'] = PageExpression(
                f'{self.context_object_name}_list', f"{self.model_cls}.objects{self.formatted_query}", page)

            page.add_block(
                self.block_name,

                PageBlock(
                    theme=self.theme,
                    root_el='crud_list',
                    fields=self.prepare_block_fields(page)
                )
            )

        sub_descriptor = '.' + self.descriptor if self.descriptor else ''

        for crud_page in self.crud_pages:
            if crud_page == 'create':
                page.children.append(f"""
[{page.name}->{page.name}{self.name_suffix}_{crud_page}: {page.defined_uri}{self.url_prefix}{crud_page}]
@merge
@crud_{crud_page}{sub_descriptor}<@{self.raw_extra_body} => '{page.collection_set.app_name}.{page.name}', kwargs={{{self.link_extra_params}}}@>
""")
            else:
                page.children.append(f"""
[{page.name}->{page.name}{self.name_suffix}_{crud_page}: {page.defined_uri}{self.url_prefix}<{self.pk_param}>/{crud_page}]
@merge
@crud_{crud_page}{sub_descriptor}<@{self.raw_extra_body} => '{page.collection_set.app_name}.{page.name}', kwargs={{{self.link_extra_params}}}@>
""")


class BaseCrudSubpageExtra(CrudPageExtra):
    crud_page = None

    def build_pages(self, page):
        page.imports.append(
            (self.app_name, self.model_cls)
        )

        page.add_block(
            self.block_name,
            PageBlock(
                theme=self.theme,
                root_el='crud_{}'.format(self.crud_page),
                fields=self.prepare_block_fields(page.get_parent())
            )

        )

        if self.crud_page == 'detail':
            page.imports.append(
                ('django.views.generic.detail', self.get_view_class_name())
            )
        else:
            page.imports.append(
                ('django.views.generic.edit', self.get_view_class_name())
            )

        if self.crud_page in ('edit', 'create') and len(self.field_filters):
            code = "form = super().get_form(*args, **kwargs)\n"

            for name, expr in self.field_filters.items():
                code += "form.fields['{}'].queryset = {}\n".format(name, expr)
            code += "return form\n"

            page.methods['get_form'] = code

        if self.crud_page in ('edit', 'delete', 'create', 'detail'):
            page.imports.append(('django.urls', 'reverse'))
            page.options['pk_url_kwarg'] = f"'{self.pk_param}'"
            page.methods['get_success_url'] = self.next_page_expr

        if self.crud_page in ('edit', 'delete', 'create'):
            if self.edit_auth:
                add_page_auth(self.edit_auth, page)

        if self.crud_page in ('edit', 'delete', 'create', 'detail'):
            page.methods['get_queryset'] = "return " + self.model_cls + ".objects" + self.formatted_query
            page.options['model'] = self.model_cls
            page.options['context_object_name'] = f"'{self.context_object_name}'"

        if self.crud_page in ('edit', 'create'):
            page.options['fields'] = repr([key for key, val in self.fields.items()])

        if self.crud_page in ('edit', 'delete', 'detail'):
            page.methods['get'] = self.object_expr + "\nreturn super().get(self.request, *args, **kwargs)"
            page.methods['post'] = self.object_expr + "\nreturn super().post(self.request, *args, **kwargs)"
            if 'get_object()' not in self.object_expr:
                page.methods['get_object'] = self.object_expr + "\nreturn self.object"

        if self.crud_page in ('create',):
            page.methods['get'] = \
                "self.object = None\nreturn super().get(self.request, *args, **kwargs)"

            page.methods['get_initial'] = f"self.object = {self.model_cls}({self.query})\nreturn super().get_initial()"

        page.extra_bases.append(self.get_view_class_name())

    def get_view_class_name(self):
        if self.crud_page == 'edit':
            return 'UpdateView'
        else:
            return '{}View'.format(self.crud_page.capitalize())


class CrudCreatePageExtra(BaseCrudSubpageExtra):
    @classmethod
    def get_name(cls):
        return 'crud_create'

    @property
    def crud_page(self):
        return 'create'


class CrudUpdatePageExtra(BaseCrudSubpageExtra):
    @classmethod
    def get_name(cls):
        return 'crud_edit'

    @property
    def crud_page(self):
        return 'edit'


class CrudDeletePageExtra(BaseCrudSubpageExtra):
    @classmethod
    def get_name(cls):
        return 'crud_delete'

    @property
    def crud_page(self):
        return 'delete'


class CrudDetailPageExtra(BaseCrudSubpageExtra):
    @classmethod
    def get_name(cls):
        return 'crud_detail'

    @property
    def crud_page(self):
        return 'detail'

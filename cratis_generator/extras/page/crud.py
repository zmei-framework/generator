from cratis_generator.config.domain import PageExtra, ValidationException, PageExpression
from cratis_generator.config.grammar import identifier, field_name_spec
from pyparsing import *

from cratis_generator.extras.page.blocks import PageBlock

ref_parser = Combine(Literal('#') + Word(alphanums + '_')).setResultsName('model') + \
             Optional(QuotedString('<', endQuoteChar='>').setResultsName('query')) + \
             Optional(Suppress('fields:') + Group(delimitedList(field_name_spec)).setResultsName('fields'))

class_parser = Word(alphanums + '_.').setResultsName('model') + \
               Optional(QuotedString('<', endQuoteChar='>').setResultsName('query')) + \
               Optional(Suppress('fields:') + Group(delimitedList(Word(alphanums + '_'))).setResultsName('fields'))

parser = ((ref_parser | class_parser) +
          Each([
              Optional(Suppress('skip:') + Group(delimitedList(
                  Literal('create') | Literal('update') | Literal('delete') | Literal('detail')
              )).setResultsName('skip')),
              Optional(Suppress('block:') + identifier.setResultsName('block_name')),
              Optional(Suppress('url_prefix:') + Word(alphanums + '-/').setResultsName('url_prefix')),
              Optional(Suppress('pk_param:') + Word(alphanums + '_').setResultsName('pk_param')),
              Optional(Suppress('item_name:') + Word(alphanums + '_').setResultsName('item_name')),
              Optional(Suppress('link_extra:') + QuotedString('"').setResultsName('link_extra'))
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
    url_prefix = None
    pk_param = None
    crud_pages = None
    app_name = None
    model_cls = None
    fields = None
    formatted_query = None
    query = None
    next_page_args = None
    item_name = None

    def __init__(self, parsed_result, page):
        super().__init__(parsed_result, page)

        self.raw_extra_body = parsed_result.extra_body
        self.descriptor = parsed_result.descriptor or None

        crud = parser.parseString(parsed_result.extra_body, parseAll=True)

        self.prepare_environment(crud, page)
        self.build_pages(page)

    def prepare_environment(self, crud, page):
        self.next_page_args = crud.next_page or None

        # appname, model_cls, fields
        if crud.model.startswith('#'):
            self.app_name = page.collection_set.app_name + '.models'
            collection = page.collection_set.collections[crud.model[1:]]
            self.model_cls = collection.class_name
            self.fields = [field.name for field in collection.filter_fields(crud.fields or '*')]
        else:
            parts = crud.model.split('.')
            self.app_name = '.'.join(parts[:-1]) + '.models'
            self.model_cls = parts[-1]
            self.fields = crud.fields
            if not self.fields:
                raise ValidationException('@crud -> fields for external models are required: {}'.format(crud.model))

        # item name
        self.item_name = crud.item_name or 'item'

        # link extra
        if len(crud.link_extra):
            self.link_extra = crud.link_extra
            link_extra_params = []
            for item in self.link_extra.split(','):
                key, val = item.split('=')
                link_extra_params.append(f"'{key}': {val}")
            self.link_extra_params = ', '.join(link_extra_params)
        else:
            self.link_extra = ''
            self.link_extra_params = ''

        # name_prefix
        if self.descriptor:
            self.name_prefix = f'{self.descriptor}_'
            self.name_suffix = f'_{self.descriptor}'
        else:
            self.name_prefix = ''
            self.name_suffix = ''

        # block name
        if crud.block_name:
            self.block_name = crud.block_name
        elif self.descriptor:
            self.block_name = f'{self.descriptor}_content'
        else:
            self.block_name = 'content'

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

        # formated_query
        self.query = crud.query.strip()
        if self.query != '':
            self.formatted_query = '.filter({})'.format(self.query)
        else:
            self.formatted_query = '.all()'

        # pages that are not needed
        self.crud_pages = [
            x for x in ['detail', 'create', 'edit', 'delete'] if x not in list(crud.skip or [])
        ]

    def prepare_block_fields(self, page):
        link_extra = self.link_extra
        if link_extra:
            link_extra = ' ' + link_extra

        links = {x: f"'{page.collection_set.app_name}.{page.name}{self.name_suffix}_{x}'{link_extra}" for x in
                 self.crud_pages}
        links['list'] = f"'{page.collection_set.app_name}.{page.name}'{link_extra}"

        return {
            'meta': f'{self.name_prefix}{self.item_name}_meta',
            'item': f"{self.name_prefix}{self.item_name}",
            'items': f"{self.name_prefix}{self.item_name}_list",
            'by_id': f"{self.pk_param}={self.name_prefix}item.pk",
            'crud_prefix': self.name_prefix,
            'crud': links
        }

    def build_pages(self, page):
        page.imports.append(
            (self.app_name, self.model_cls)
        )

        page.page_items[f'{self.name_prefix}{self.item_name}_meta'] = PageExpression(
            f'{self.name_prefix}{self.item_name}_meta', f"{self.model_cls}._meta", page)

        page.page_items[f'_{self.name_prefix}{self.item_name}_list'] = PageExpression(
            f'{self.name_prefix}{self.item_name}_list', f"{self.model_cls}.objects{self.formatted_query}", page)

        page.add_block(
            self.block_name,
            PageBlock(
                name='crud_list',
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
                name='crud_{}'.format(self.crud_page),
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

        if self.crud_page in ('edit', 'delete', 'create', 'detail'):
            page.imports.append(('django.urls', 'reverse_lazy'))
            page.options['pk_url_kwarg'] = f"'{self.pk_param}'"
            page.methods['get_success_url'] = f"return reverse_lazy({self.next_page_args})"

        if self.crud_page in ('edit', 'delete', 'create', 'detail'):
            page.methods['get_queryset'] = "return " + self.model_cls + ".objects" + self.formatted_query
            page.options['model'] = self.model_cls
            page.options['context_object_name'] = f"'{self.name_prefix}item'"

        if self.crud_page in ('edit', 'create'):
            page.options['fields'] = repr(self.fields)

        if self.crud_page in ('edit', 'delete', 'detail'):
            page.methods['get'] = \
                "self.object = self.get_object()\nreturn super().get(request, *args, **kwargs)"

        if self.crud_page in ('create',):
            page.methods['get'] = \
                "self.object = None\nreturn super().get(request, *args, **kwargs)"

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

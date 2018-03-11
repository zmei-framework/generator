from cratis_generator.config.domain import PageExtra, PageDef, ValidationException, PageExpression
from cratis_generator.config.grammar import identifier, field_name_spec
from pyparsing import *

from cratis_generator.extras.page.blocks import PageBlock

ref_parser = Combine(Literal('#') + Word(alphanums + '_')).setResultsName('model') + \
             Optional(QuotedString('<', endQuoteChar='>').setResultsName('query')) + \
             Optional(Suppress('fields:') + Group(delimitedList(field_name_spec)).setResultsName('fields'))

class_parser = Word(alphanums + '_.').setResultsName('model') + \
               Optional(QuotedString('<', endQuoteChar='>').setResultsName('query')) + \
               Optional(Suppress('fields:') + Group(delimitedList(Word(alphanums + '_'))).setResultsName('fields'))

parser = ((ref_parser | class_parser) + \
         Optional(Suppress('skip:') + Group(delimitedList(
             Literal('create') | Literal('update') | Literal('delete') | Literal('detail')
         )).setResultsName('skip')) + \
         Optional(Suppress('block:') + identifier.setResultsName('block_name')) + \
         Optional(Suppress('url_prefix:') + Word(alphanums + '-/').setResultsName('url_prefix')) +\
         Optional(Suppress('pk_param:') + Word(alphanums + '_').setResultsName('pk_param')) +\
         Optional(Suppress('link_extra:') + QuotedString('"').setResultsName('link_extra'))
         ).ignore(cStyleComment)


def parse_crud_extra(page, extra_body):
    crud = parser.parseString(extra_body, parseAll=True)
    if crud.model.startswith('#'):
        app_name = page.collection_set.app_name + '.models'
        collection = page.collection_set.collections[crud.model[1:]]
        model_cls = collection.class_name
        fields = [field.name for field in collection.filter_fields(crud.fields or '*')]
    else:
        parts = crud.model.split('.')
        app_name = '.'.join(parts[:-1]) + '.models'
        model_cls = parts[-1]
        fields = crud.fields
        if not fields:
            raise ValidationException('@crud -> fields for external models are required: {}'.format(crud.model))

    page.imports.append(
        (app_name, model_cls)
    )
    query = crud.query.strip()
    if query != '':
        formatted_query = '.filter({})'.format(query)
    else:
        formatted_query = '.all()'
    return crud, formatted_query, model_cls, fields


class CrudPageExtra(PageExtra):
    @classmethod
    def get_name(cls):
        return 'crud'

    def __init__(self, parsed_result, page):
        super().__init__(parsed_result, page)

        crud, formatted_query, model_cls, fields = parse_crud_extra(page, parsed_result.extra_body)

        descriptor = parsed_result.descriptor or None

        # link extra
        if len(crud.link_extra):
            link_extra = crud.link_extra + " "
            link_extra_params = []
            for item in link_extra.split(','):
                key, val = item.split('=')
                link_extra_params.append(f"'{key}': {val}")
            link_extra_params = ', '.join(link_extra_params)
        else:
            link_extra = ''
            link_extra_params = ''

        # name_prefix
        if descriptor:
            name_prefix = f'{descriptor}_'
            name_suffix = f'_{descriptor}'
        else:
            name_prefix = ''
            name_suffix = ''

        # block name
        if crud.block_name:
            block_name = crud.block_name
        elif descriptor:
            block_name = f'{descriptor}_content'
        else:
            block_name = 'content'

        # url prefix
        if crud.url_prefix:
            url_prefix = crud.url_prefix
            if not url_prefix.endswith('/'):
                url_prefix = url_prefix + '/'
        elif descriptor:
            url_prefix = f'{descriptor}/'
        else:
            url_prefix = ''
        if not page.defined_uri.endswith('/'):
            url_prefix = '/' + url_prefix

        # pk
        if crud.pk_param:
            pk_param = crud.pk_param
        elif descriptor:
            pk_param = f'{descriptor}_pk'
        else:
            pk_param = 'pk'


        skip = list(crud.skip or [])

        page_urls = {'list': f'{page.collection_set.app_name}.{page.name}'}

        if 'details' not in skip:
            page_urls['details'] = f'{page.collection_set.app_name}.{page.name}{name_suffix}_details'
        if 'create' not in skip:
            page_urls['create'] = f'{page.collection_set.app_name}.{page.name}{name_suffix}_create'
        if 'update' not in skip:
            page_urls['update'] = f'{page.collection_set.app_name}.{page.name}{name_suffix}_update'
        if 'delete' not in skip:
            page_urls['delete'] = f'{page.collection_set.app_name}.{page.name}{name_suffix}_delete'

        page.page_items[f'{name_prefix}crud'] = PageExpression(f'{name_prefix}crud', repr(page_urls), page)
        page.page_items[f'_{name_prefix}items'] = PageExpression(f'{name_prefix}items',
                                                                f"{model_cls}.objects{formatted_query}", page)
        if not block_name in page.blocks:
            page.blocks[block_name] = []
        page.blocks[block_name].append(PageBlock(name='crud_list', fields={'crud_prefix': name_prefix, 'pk_param': pk_param, 'link_extra': link_extra}))


        if 'details' not in skip:
            page.children.append(
            f"""
[{page.name}->{page.name}{name_suffix}_details: {page.defined_uri}{url_prefix}<{pk_param}>/]
{name_prefix}item: {model_cls}.objects{formatted_query}.get(pk=url.{pk_param}) 
@blocks.{block_name}(crud_details<crud_prefix={name_prefix}, pk_param={pk_param}, link_extra="{link_extra}">)
            """
        )

        if 'create' not in skip:
            page.children.append(
            f"""
[{page.name}->{page.name}{name_suffix}_create: {page.defined_uri}{url_prefix}add]
@crud_create<@{parsed_result.extra_body} => '{page.collection_set.app_name}.{page.name}', kwargs={{{link_extra_params}}}@> 
@blocks.{block_name}(crud_add<crud_prefix={name_prefix}, pk_param={pk_param}, link_extra="{link_extra}">)
            """
        )

        if 'update' not in skip:
            page.children.append(
            f"""
[{page.name}->{page.name}{name_suffix}_update: {page.defined_uri}{url_prefix}<{pk_param}>/edit]
@crud_update<@{parsed_result.extra_body} => '{page.collection_set.app_name}.{page.name}_details', kwargs={{'{pk_param}': url.{pk_param}, {link_extra_params}}}@>  
@blocks.{block_name}(crud_update<crud_prefix={name_prefix}, pk_param={pk_param}, link_extra="{link_extra}">)
            """
        )

        if 'delete' not in skip:
            page.children.append(
            f"""
[{page.name}->{page.name}{name_suffix}_delete: {page.defined_uri}{url_prefix}<{pk_param}>/delete]
@crud_delete<@{parsed_result.extra_body} => '{page.collection_set.app_name}.{page.name}', kwargs={{{link_extra_params}}}@>  
@blocks.{block_name}(crud_delete<crud_prefix={name_prefix}, pk_param={pk_param}, link_extra="{link_extra}">)
            """
        )


class CrudCreatePageExtra(PageExtra):
    @classmethod
    def get_name(cls):
        return 'crud_create'

    def __init__(self, parsed_result, page):
        super().__init__(parsed_result, page)

        extra_body, next_page = [x.strip() for x in parsed_result.extra_body.split('=>')]

        crud, formatted_query, model_cls, fields = parse_crud_extra(page, extra_body)

        page.imports.append(
            ('django.views.generic.edit', 'CreateView')
        )
        page.imports.append(
            ('django.urls', 'reverse_lazy')
        )

        page.options['model'] = model_cls
        page.options['fields'] = repr(fields)
        page.methods['get_success_url'] = f"return reverse_lazy({next_page})"

        page.methods['get_initial'] = "self.object = {}({})\nreturn super().get_initial()".format(
            model_cls, crud.query)
        page.methods['get_queryset'] = "return " + model_cls + ".objects" + formatted_query
        page.extra_bases.append('CreateView')


class CrudUpdatePageExtra(PageExtra):
    @classmethod
    def get_name(cls):
        return 'crud_update'

    def __init__(self, parsed_result, page):
        super().__init__(parsed_result, page)

        extra_body, next_page = [x.strip() for x in parsed_result.extra_body.split('=>')]

        crud, formatted_query, model_cls, fields = parse_crud_extra(page, extra_body)

        page.imports.append(
            ('django.views.generic.edit', 'UpdateView')
        )
        page.imports.append(
            ('django.urls', 'reverse_lazy')
        )

        page.options['model'] = model_cls
        page.options['object'] = None
        page.options['fields'] = repr(fields)
        page.methods['get_success_url'] = f"return reverse_lazy({next_page})"

        render = "self.object = self.get_object()\nreturn super().get(request, *args, **kwargs)"
        page.methods['get'] = render

        page.methods['get_queryset'] = "return " + model_cls + ".objects" + formatted_query
        page.extra_bases.append('UpdateView')


class CrudDeletePageExtra(PageExtra):
    @classmethod
    def get_name(cls):
        return 'crud_delete'

    def __init__(self, parsed_result, page):
        super().__init__(parsed_result, page)

        extra_body, next_page = [x.strip() for x in parsed_result.extra_body.split('=>')]

        crud, formatted_query, model_cls, fields = parse_crud_extra(page, extra_body)

        page.imports.append(
            ('django.views.generic.edit', 'DeleteView')
        )
        page.imports.append(
            ('django.urls', 'reverse_lazy')
        )

        page.options['model'] = model_cls
        page.methods['get_success_url'] = f"return reverse_lazy({next_page})"

        render = "self.object = self.get_object()\nreturn super().get(request, *args, **kwargs)"
        page.methods['get'] = render

        page.methods['get_queryset'] = "return " + model_cls + ".objects" + formatted_query
        page.extra_bases.append('DeleteView')

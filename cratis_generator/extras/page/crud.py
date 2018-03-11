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

parser = (ref_parser | class_parser) + \
         Optional(Suppress('skip:') + Group(delimitedList(
             Literal('create') | Literal('update') | Literal('delete') | Literal('detail')
         )).setResultsName('skip'))


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

        block_name = parsed_result.descriptor or 'content'

        crud, formatted_query, model_cls, fields = parse_crud_extra(page, parsed_result.extra_body)

        page.has_uri = False

        skip = list(crud.skip or [])

        page_urls = {'list': '{page.collection_set.app_name}.{page.name}'.format(page=page)}

        if 'details' not in skip:
            page_urls['details'] = '{page.collection_set.app_name}.{page.name}_details'.format(page=page)
        if 'create' not in skip:
            page_urls['create'] = '{page.collection_set.app_name}.{page.name}_create'.format(page=page)
        if 'update' not in skip:
            page_urls['update'] = '{page.collection_set.app_name}.{page.name}_update'.format(page=page)
        if 'delete' not in skip:
            page_urls['delete'] = '{page.collection_set.app_name}.{page.name}_delete'.format(page=page)

        page.page_items['crud'] = PageExpression('items', repr(page_urls), page)

        page.children.append(
            """
[{page.name}->{page.name}_list as {page.name}: {page.defined_uri}]
items: {cls}.objects{query}
@blocks.{block_name}(crud_list)
            """.format(block_name=block_name, page=page, cls=model_cls, query=formatted_query)
        )

        if 'details' not in skip:
            page.children.append(
            """
[{page.name}->{page.name}_details: {page.defined_uri}/<pk>/]
item: {cls}.objects{query}.get(pk=url.pk) 
@blocks.{block_name}(crud_details)
            """.format(block_name=block_name, page=page, cls=model_cls, query=formatted_query)
        )

        if 'create' not in skip:
            page.children.append(
            """
[{page.name}->{page.name}_create: {page.defined_uri}/add]
@crud_create({args} => '{page.collection_set.app_name}.{page.name}') 
@blocks.{block_name}(crud_add)
            """.format(block_name=block_name, page=page, args=parsed_result.extra_body)
        )

        if 'update' not in skip:
            page.children.append(
            f"""
[{page.name}->{page.name}_update: {page.defined_uri}/<pk>/edit]
@crud_update({parsed_result.extra_body} => '{page.collection_set.app_name}.{page.name}_details', kwargs={{'pk': url.pk}}) 
@blocks.{block_name}(crud_update)
            """
        )

        if 'delete' not in skip:
            page.children.append(
            """
[{page.name}->{page.name}_delete: {page.defined_uri}/<pk>/delete]
@crud_delete({args} => '{page.collection_set.app_name}.{page.name}') 
@blocks.{block_name}(crud_delete)
            """.format(block_name=block_name, page=page, args=parsed_result.extra_body)
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
        page.methods['get_success_url'] = "return reverse_lazy({})".format(next_page)

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
        page.methods['get_success_url'] = "return reverse_lazy({})".format(next_page)

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
        page.methods['get_success_url'] = "return reverse_lazy({})".format(next_page)

        render = "self.object = self.get_object()\nreturn super().get(request, *args, **kwargs)"
        page.methods['get'] = render

        page.methods['get_queryset'] = "return " + model_cls + ".objects" + formatted_query
        page.extra_bases.append('DeleteView')

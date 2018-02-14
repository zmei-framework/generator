from cratis_generator.config.domain import FieldDeclaration, ValidationException
from cratis_generator.config.extras import Extra
from pyparsing import *


class RestExtra(Extra):

    @classmethod
    def get_name(cls):
        return 'rest'

    def get_parser(self):
        identifier = Word(alphas, alphanums + '_')

        field_name_spec = Literal('*') | (Combine(Optional('^') + identifier))

        extra_rest_gr = Forward()
        extra_rest_gr << (
            Optional(Suppress('fields:') + Group(delimitedList(field_name_spec).setResultsName('list') +
                                                 Optional(Suppress('[') + Word('rw').setResultsName('mode') + Suppress(
                                                     ']'))).setResultsName('fields')) +

            Optional(Suppress('inline:') + Group(delimitedList(Group(identifier.setResultsName('id') +
                                                                     Optional(Suppress('(') + extra_rest_gr + Suppress(
                                                                         ')')).setResultsName('sub')))).setResultsName(
                'inline')) +

            Optional(Suppress('annotate:') + Group(delimitedList(Group(Literal('count').setResultsName('kind') +
                                                                       Suppress('(') + identifier.setResultsName(
                'field') + Suppress(')') +
                                                                       Optional(
                                                                           Suppress('as') + identifier.setResultsName(
                                                                               'alias'))))).setResultsName(
                'annotations'))
        )
        return extra_rest_gr.ignore(cStyleComment) + stringEnd

    def parse(self, extra, collection):

        parsed_body = self.get_parser().parseString(extra.extra_body)

        collection.rest_conf = RestSerializerConfig(collection.class_name, parsed_body, collection)

        if parsed_body.fields:
            collection.rest_mode = parsed_body.fields.mode
        else:
            collection.rest_mode = 'r'

        collection.collection_set.rest = True
        collection.rest = True


class RestSerializerConfig(object):
    def __init__(self, name, parse_result, collection):

        self.serializer_name = name
        self.collection = collection
        self.field_declarations = []
        self.field_imports = []
        self.field_names = ['id']
        self.extra_serializers = []
        self.annotations = []

        inlines = {}

        if parse_result and parse_result.inline:
            for inline in parse_result.inline:
                if inline.id not in collection.fields:
                    raise ValidationException('inline contains wrong field name: {}'.format(inline.id))
                inlines[inline.id] = inline

        if parse_result and parse_result.fields:
            fields = parse_result.fields.list
        else:
            fields = ['*']

        for field in collection.filter_fields(fields, include_refs=True):
            self.field_names.append(field.name)

            if field.name in inlines:

                inline_collection = field.get_rest_inline_collection()

                if not inline_collection:
                    raise ValidationException('field "{}" can not be used as inline'.format(field.name))

                serializer_name = name + '_Inline' + inline_collection.class_name

                self.extra_serializers.append(
                    RestSerializerConfig(serializer_name, inlines[field.name].sub, inline_collection))

                self.field_imports.append(
                    FieldDeclaration('{}.models'.format(inline_collection.collection_set.app_name),
                                     inline_collection.class_name))
                self.field_declarations.append(
                    (field.name, '{}Serializer(many={})'.format(serializer_name, repr(field.is_many))))
            else:
                rest_field = field.get_rest_field()
                if rest_field:
                    for line in rest_field.import_def:
                        self.field_imports.append(line)
                    self.field_declarations.append((field.name, rest_field.declaration))

        if hasattr(parse_result, 'annotations'):
            for ant in parse_result.annotations:
                if ant.kind == 'count':
                    alias = ant.alias or '{}_{}'.format(ant.field, ant.kind)
                    self.field_declarations.append((alias, 'serializers.IntegerField()'))
                    self.field_names.append(alias)
                    self.annotations.append("{}=Count('{}', distinct=True)".format(alias, ant.field))
                    self.field_imports.append(FieldDeclaration('django.db.models', 'Count'))
                else:
                    raise ValidationException('Unknown annotation type: {}'.format(ant.kind))

    def configure_imports(self, imports):
        for import_line in self.field_imports:
            imports.add(*import_line)

        for conf in self.extra_serializers:
            conf.configure_imports(imports)

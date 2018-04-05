from cratis_generator.config.domain import FieldDeclaration, ValidationException
from cratis_generator.config.extras import Extra
from pyparsing import *

from cratis_generator.config.grammar import ref_or_class_name


class RestExtra(Extra):

    @classmethod
    def get_name(cls):
        return 'rest'

    def get_parser(self):
        identifier = Word(alphas, alphanums + '_')

        field_name_spec = Literal('*') | (Combine(Optional('^') + identifier))



        extra_rest_gr = Forward()
        extra_rest_gr << (
            Each([

            Optional(Suppress('user_field:') + identifier.setResultsName('user_field')),
            Optional(Suppress('fields:') + Group(delimitedList(field_name_spec).setResultsName('list') +
                                                 Optional(Suppress('[') + Word('rw').setResultsName('mode') + Suppress(
                                                     ']'))).setResultsName('fields')),
            Optional(Suppress('read_only:') + Group(delimitedList(field_name_spec).setResultsName('list')).setResultsName('read_only_fields')),

            Optional(Suppress('inline:') + Group(delimitedList(Group(identifier.setResultsName('id') +
                                                                     Optional(Suppress('(') + extra_rest_gr + Suppress(
                                                                         ')')).setResultsName('sub')))).setResultsName(
                'inline')),

            Optional(Suppress('annotate:') + Group(delimitedList(Group(Literal('count').setResultsName('kind') +
                                                                       Suppress('(') + identifier.setResultsName(
                'field') + Suppress(')') +
                                                                       Optional(
                                                                           Suppress('as') + identifier.setResultsName(
                                                                               'alias'))))).setResultsName(
                'annotations'))
             ])
        )

        auth_methods = \
            Group(Literal('session').setResultsName('name')) | \
            Group(Literal('basic').setResultsName('name')) | \
            Group(Literal('token').setResultsName('name') + Suppress(':') + Group(ref_or_class_name).setResultsName('token_model'))

        rest = Each([
            Optional(Group(Suppress('auth') + Suppress('(') + delimitedList(auth_methods) + Suppress(')')).setResultsName('auth_methods')),
            Optional(Suppress('i18n:') + (Literal('true') | Literal('false')).setResultsName('i18n')),
            Optional(Suppress('query:') + White() + restOfLine.setResultsName('query')),
            Optional(Suppress('on_create:') + restOfLine.setResultsName('on_create')),

        ]) + extra_rest_gr
        return rest.ignore(cStyleComment) + stringEnd

    def parse(self, extra, collection):

        parsed_body = self.get_parser().parseString(extra.extra_body)

        collection.rest_conf = RestSerializerConfig(collection.class_name, parsed_body, collection)

        collection.collection_set.rest = True
        collection.rest = True


class RestSerializerConfig(object):
    def __init__(self, name, parse_result, collection, parent_field=None):

        self.i18n = parse_result.i18n == 'true'

        self.serializer_name = name
        self.collection = collection
        self.field_declarations = []
        self.field_imports = []
        self.field_names = ['id']
        self.extra_serializers = []
        self.annotations = []
        self.auth_methods = {}
        self.auth_method_classes = []
        self.query = 'all()'
        self.parent_field = parent_field
        self.on_create = ''

        if parse_result.fields:
            self.rest_mode = parse_result.fields.mode
        else:
            self.rest_mode = 'r'

        self.user_field = None
        if parse_result.user_field:
            self.user_field = parse_result.user_field

        if parse_result.query:
            self.query = parse_result.query

        if parse_result.on_create:
            self.on_create = parse_result.on_create.strip()


        if parse_result.auth_methods:
            for method in parse_result.auth_methods:
                if method.name == 'token':
                    self.field_imports.append(('rest_framework.authentication', 'TokenAuthentication'))

                    self.auth_method_classes.append(f'{collection.class_name}TokenAuthentication')

                    if method.token_model.ref:
                        try:
                            ref_collection = self.collection.collection_set.collections[method.token_model.ref]
                        except KeyError:
                            raise ValidationException('@rest token model is unknown: #{}'.format(method.token_model.ref))
                        cls = ref_collection.class_name
                        self.field_imports.append((f'{self.collection.collection_set.app_name}.models', cls))
                    else:
                        cls = method.token_model.class_name

                    self.auth_methods[method.name] = {'model': cls}

                if method.name == 'session':
                    self.field_imports.append(('rest_framework.authentication', 'SessionAuthentication'))
                    self.auth_methods[method.name] = {}
                    self.auth_method_classes.append('SessionAuthentication')

                if method.name == 'basic':
                    self.field_imports.append(('rest_framework.authentication', 'BasicAuthentication'))
                    self.auth_methods[method.name] = {}
                    self.auth_method_classes.append('BasicAuthentication')

            self.field_imports.append(('rest_framework.permissions', 'IsAuthenticated'))
        else:
            self.field_imports.append(('rest_framework.permissions', 'AllowAny'))

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

        if parse_result and parse_result.read_only_fields:
            self.read_only_fields = [field.name for field in collection.filter_fields(parse_result.read_only_fields.list, include_refs=True)]
        else:
            self.read_only_fields = []

        for field in collection.filter_fields(fields, include_refs=True):
            if self.parent_field and hasattr(self.parent_field, 'source_field_name') and field.name == self.parent_field.source_field_name:
                continue
            if self.user_field and field.name == self.user_field:
                continue

            self.field_names.append(field.name)

            if field.name in inlines:
                inline_collection = field.get_rest_inline_collection()

                if not inline_collection:
                    raise ValidationException('field "{}" can not be used as inline'.format(field.name))

                serializer_name = name + '_Inline' + inline_collection.class_name

                self.extra_serializers.append(
                    RestSerializerConfig(serializer_name, inlines[field.name].sub, inline_collection, parent_field=field))

                self.field_imports.append(
                    FieldDeclaration('{}.models'.format(inline_collection.collection_set.app_name),
                                     inline_collection.class_name))

                self.field_declarations.append(
                    (field.name, '{}Serializer(many={}, read_only={})'.format(serializer_name, repr(field.is_many),
                                                                              repr(field.name in self.read_only_fields))))
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

    @property
    def rest_class(self):
        if self.rest_mode == 'rw':
            return 'rest_framework.viewsets', 'ModelViewSet'
        elif self.rest_mode == 'w':
            return 'cratis_api.views', 'WriteOnlyModelViewSet'
        else:
            return 'rest_framework.viewsets', 'ReadOnlyModelViewSet'

    @property
    def is_writable(self):
        return 'w' in self.rest_mode

    @property
    def is_root(self):
        return self.parent_field is None

    def configure_imports(self, imports):

        imports.add(*self.rest_class)

        for import_line in self.field_imports:
            imports.add(*import_line)

        for conf in self.extra_serializers:
            conf.configure_imports(imports)

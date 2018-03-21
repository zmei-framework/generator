import re

from cratis_generator.config.domain import ValidationException, ReferenceField, FieldDeclaration
from cratis_generator.config.extras import Extra
from pyparsing import *

from cratis_generator.config.grammar import field_name_spec


class AdminExtra(Extra):

    @classmethod
    def get_name(cls):
        return 'admin'

    def get_parser(self):

        identifier = Word(alphas, alphanums + '_')

        admin_inline_args = Each([
                            Optional(Suppress('fields:') + Group(delimitedList(field_name_spec)).setResultsName('fields')),
                            Optional(Suppress(',')) + Optional(Suppress('type:') + oneOf('tabular stacked polymorphic').setResultsName('type')),
                            Optional(Suppress(',')) + Optional(Suppress('extra:') + Word(nums).setResultsName('extra_count'))
        ])

        admin_inline = Group(
            identifier.setResultsName('id') + Optional(Suppress('(') + admin_inline_args + Suppress(')')))

        tab_verbose_name = Suppress('/') + OneOrMore(Regex(r"\w+", re.UNICODE)) \
            .setParseAction(lambda tokens: " ".join(tokens)) \
            .setResultsName("verbose_name")

        admin_tab = Group(
            identifier.setResultsName('id') + Optional(tab_verbose_name) + Suppress('(') + Group(delimitedList(field_name_spec)).setResultsName(
                'fields') + Suppress(')'))

        file_name = QuotedString('"')

        return Each([
                   Optional(Suppress('list:') + Group(delimitedList(field_name_spec)).setResultsName('list')) +
                   Optional(Suppress('list_editable:') + Group(delimitedList(field_name_spec)).setResultsName('list_editable')) +
                   Optional(Suppress('list_filter:') + Group(delimitedList(field_name_spec)).setResultsName('list_filter')) +
                   Optional(Suppress('list_search:') + Group(delimitedList(field_name_spec)).setResultsName('list_search')) +
                   Optional(Suppress('fields:') + Group(delimitedList(field_name_spec)).setResultsName('fields')) +
                   Optional(Suppress('inline:') + Group(delimitedList(admin_inline)).setResultsName('inlines')) +
                   Optional(Suppress('tabs:') + Group(delimitedList(admin_tab)).setResultsName('tabs')) +
                   Optional(Suppress('js:') + Group(delimitedList(file_name)).setResultsName('js')) +
                   Optional(Suppress('css:') + Group(delimitedList(file_name)).setResultsName('css'))
               ]).ignore(cStyleComment) + stringEnd

    def parse(self, extra, collection):

        parsed_body = self.get_parser().parseString(extra.extra_body)

        if parsed_body.list:
            collection.admin_list = collection.filter_fields(parsed_body.list)

        if parsed_body.list_editable:
            collection.admin_list_editable = collection.filter_fields(parsed_body.list_editable)

        if parsed_body.list_filter:
            collection.admin_list_filter = collection.filter_fields(parsed_body.list_filter)

        if parsed_body.list_search:
            collection.admin_list_search = collection.filter_fields(parsed_body.list_search)

        if parsed_body.fields:
            collection.admin_fields = collection.filter_fields(parsed_body.fields)

        if parsed_body.js:
            collection.admin_js = list(parsed_body.js)

        if parsed_body.css:
            collection.admin_css = list(parsed_body.css)

        if parsed_body.inlines:
            inlines = []
            for inline in parsed_body.inlines:
                inlines.append(
                    AdminInlineConfig(inline, collection)
                )
            collection.admin_inlines = inlines

        tab_names = {}
        if parsed_body.tabs:
            for tab in parsed_body.tabs:

                tab_names[tab.id] = tab.verbose_name or tab.id

                for field in collection.filter_fields(tab.fields):
                    collection.admin_tab_fields[field.name] = tab.id

                collection.admin_tabs.append(tab.id)

        if len(collection.admin_tabs):
            collection.tab_names.update(tab_names)

            general_fields = []
            for field in (collection.admin_fields or collection.all_fields):
                if field.name not in collection.admin_tab_fields:
                    general_fields.append(field.name)
                    collection.admin_tab_fields[field.name] = 'general'

                    if 'general' not in collection.admin_tabs:
                        collection.admin_tabs = ['general'] + collection.admin_tabs
                        collection.tab_names.update({'general': 'General'})

            # set tabs to inlines
            inline_map = {x.inline_name: x for x in collection.admin_inlines}
            for field_name, tab in collection.admin_tab_fields.items():
                if field_name in inline_map:
                    inline_map[field_name].tab = tab

        collection.collection_set.admin = True
        collection.admin = True


class AdminInlineConfig(object):
    def __init__(self, parse_result, collection):
        self.collection = collection
        self.inline_name = parse_result.id

        if not collection.check_field_exists(self.inline_name):
            raise ValidationException(
                'Field name specified for admin inline: "{}" does not exist'.format(self.inline_name))

        field = collection.all_and_inherited_fields_map[self.inline_name]

        if not isinstance(field, ReferenceField):
            raise ValidationException(
                'Field name specified for admin inline: "{}" is not a reference field (back relation).'.format(
                    self.inline_name))

        self.field = field
        self.source_field_name = field.source_field_name
        self.target_collection = field.target_collection

        self.field_names = field.target_collection.filter_fields(parse_result.fields or ['*'])

        self.inline_type = parse_result.type or 'tabular'
        self.tab = None

        self.extra_count = 0
        if parse_result.extra_count:
            self.extra_count = int(parse_result.extra_count)

            if self.extra_count > 0 and self.inline_type == 'polymorphic':
                raise ValidationException('{}->{}: When using inline type "polymorphic" extra must be 0'.format(
                    self.collection.name,
                    self.inline_name
                ))

        if self.inline_type == 'polymorphic':
            collection.admin_has_polymorphic_inlines = True

    @property
    def class_name(self):
        return '{}{}Inline'.format(
            self.collection.class_name,
            ''.join([x.capitalize() for x in self.inline_name.split('_')])
        )

    @property
    def type_declarations(self):

        declarations = []

        if self.inline_type == 'tabular':
            if self.target_collection.sortable:
                declarations.append(FieldDeclaration('suit.admin', 'SortableTabularInline'))
            else:
                declarations.append(FieldDeclaration('django.contrib.admin', 'TabularInline'))
        elif self.inline_type == 'polymorphic':
            if self.target_collection.sortable:
                declarations.append(FieldDeclaration('cratis_admin.admin', 'StackedPolymorphicSortableInline'))
            else:
                declarations.append(FieldDeclaration('polymorphic.admin', 'StackedPolymorphicInline'))
        else:
            if self.target_collection.sortable:
                declarations.append(FieldDeclaration('suit.admin', 'SortableStackedInline'))
            else:
                declarations.append(FieldDeclaration('django.contrib.admin', 'StackedInline'))

        # if self.target_collection.translatable:
        #     declarations.append(FieldDeclaration('modeltranslation.admin', 'TranslationInlineModelAdmin'))

        return declarations

    @property
    def parent_classes(self):
        return [x.declaration for x in self.type_declarations]

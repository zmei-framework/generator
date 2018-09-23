import re

from zmei_generator.config.domain.collection_set_def import FieldDeclaration
from zmei_generator.config.domain.exceptions import ValidationException
from zmei_generator.config.domain.reference_field import ReferenceField
from zmei_generator.config.extras import Extra
from cPyparsing import *

from zmei_generator.config.grammar import field_name_spec


class AdminExtra(Extra):

    def __init__(self, collection) -> None:
        super().__init__()

        self.collection = collection

        # fields for different purposes
        self.admin_list = None
        self.read_only = None
        self.list_editable = None
        self.list_filter = None
        self.list_search = None
        self.fields = None
        self.inlines = []

        # mapping of field.name => tab.id
        self.tab_fields = {}

        # id of tabs
        self.tabs = []

        # mapping of tab.id => Verbose name of tab
        self.tab_names = {}

        self.has_polymorphic_inlines = False

        self.tabs_raw = []

    @classmethod
    def get_name(cls):
        return 'admin'

    # def get_parser(self):
    #
    #     identifier = Word(alphas, alphanums + '_')
    #
    #     admin_inline_args = Each([
    #                         Optional(Suppress('fields:') + Group(delimitedList(field_name_spec)).setResultsName('fields')),
    #                         Optional(Suppress(',')) + Optional(Suppress('type:') + oneOf('tabular stacked polymorphic').setResultsName('type')),
    #                         Optional(Suppress(',')) + Optional(Suppress('extra:') + Word(nums).setResultsName('extra_count'))
    #     ])
    #
    #     admin_inline = Group(
    #         identifier.setResultsName('id') + Optional(Suppress('(') + admin_inline_args + Suppress(')')))
    #
    #     tab_verbose_name = Suppress('/') + OneOrMore(Regex(r"\w+", re.UNICODE)) \
    #         .setParseAction(lambda tokens: " ".join(tokens)) \
    #         .setResultsName("verbose_name")
    #
    #     admin_tab = Group(
    #         identifier.setResultsName('id') + Optional(tab_verbose_name) + Suppress('(') + Group(delimitedList(field_name_spec)).setResultsName(
    #             'fields') + Suppress(')'))
    #
    #     file_name = QuotedString('"')
    #
    #     return Each([
    #                Optional(Suppress('list:') + Group(delimitedList(field_name_spec)).setResultsName('list')) +
    #                Optional(Suppress('list_editable:') + Group(delimitedList(field_name_spec)).setResultsName('list_editable')) +
    #                Optional(Suppress('list_filter:') + Group(delimitedList(field_name_spec)).setResultsName('list_filter')) +
    #                Optional(Suppress('list_search:') + Group(delimitedList(field_name_spec)).setResultsName('list_search')) +
    #                Optional(Suppress('fields:') + Group(delimitedList(field_name_spec)).setResultsName('fields')) +
    #                Optional(Suppress('read_only:') + Group(delimitedList(field_name_spec)).setResultsName('read_only')) +
    #                Optional(Suppress('inline:') + Group(delimitedList(admin_inline)).setResultsName('inlines')) +
    #                Optional(Suppress('tabs:') + Group(delimitedList(admin_tab)).setResultsName('tabs')) +
    #                Optional(Suppress('js:') + Group(delimitedList(file_name)).setResultsName('js')) +
    #                Optional(Suppress('css:') + Group(delimitedList(file_name)).setResultsName('css'))
    #            ]).ignore(cStyleComment) + stringEnd

    def parse(self, extra, collection):
        if parsed_body.js:
            collection.admin_js = list(parsed_body.js)

        if parsed_body.css:
            collection.admin_css = list(parsed_body.css)

    def register_tab(self, name, verbose_name, fields_expr, prepend=False):

        self.tabs_raw.append(
            (name, verbose_name, fields_expr, prepend)
        )

    def add_tab(self, name, verbose_name, fields_expr, prepend):
        """
        Do delayed field calculation as we need to wait
        until all Reference fields are created
        """
        fields = self.collection.filter_fields(fields_expr, include_refs=True)

        self.add_tab_fieldset(name, verbose_name, fields, prepend)

    def add_tab_fieldset(self, name, verbose_name, fields, prepend):
        # filter out fields that are not meant to be rendered
        if self.fields:
            fields = [f for f in fields if f in self.fields or isinstance(f, ReferenceField)]
        self.tab_names[name] = verbose_name or name.capitalize()
        for field in fields:
            self.tab_fields[field.name] = name
        if prepend:
            self.tabs = [name] + self.tabs
        else:
            self.tabs.append(name)

    def check_tab_consistency(self):
        general_fields = []
        for field in (self.fields or self.collection.all_fields):

            if field.name not in self.tab_fields:
                general_fields.append(field)

        if len(general_fields) > 0:
            self.add_tab_fieldset('general', 'General', general_fields, prepend=True)

    def post_process(self):
        for tab in self.tabs_raw:
            self.add_tab(*tab)

        self.check_tab_consistency()

        # set tabs to inlines
        inline_map = {x.inline_name: x for x in self.inlines}
        print(self.tab_fields)
        for field_name, tab in self.tab_fields.items():
            if field_name in inline_map:
                inline_map[field_name].tab = tab

        for inline in self.inlines:
            inline.post_process()


class AdminInlineConfig(object):
    def __init__(self, admin, name):
        self.admin = admin
        self.collection = admin.collection
        self.inline_name = name
        self.fields_expr = ['*']
        self.extra_count = 0
        self.inline_type = 'tabular'

        self.field = None
        self.source_field_name = None
        self.target_collection = None
        self.field_set = None
        self.tab = None

    def post_process(self):
        collection = self.admin.collection

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

        self.field_set = [f for f in field.target_collection.filter_fields(self.fields_expr) if f.name != self.source_field_name]

        if self.extra_count:
            if self.extra_count > 0 and self.inline_type == 'polymorphic':
                raise ValidationException('{}->{}: When using inline type "polymorphic" extra must be 0'.format(
                    self.collection.name,
                    self.inline_name
                ))

    @property
    def field_names(self):
        return [f.name for f in self.field_set]

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

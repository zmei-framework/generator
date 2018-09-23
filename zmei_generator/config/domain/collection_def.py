from cPyparsing import ParseException

from zmei_generator.config.domain.exceptions import ValidationException
from zmei_generator.config.domain.reference_field import ReferenceField
from zmei_generator.generator.utils import handle_parse_exception


class CollectionDef(object):
    #
    # ref: str
    # name: str
    # fields: Dict[str, FieldDef]

    # rest: False
    # translatable: False


    @property
    def admin_list(self):
        return self.admin.admin_list

    @property
    def admin_read_only(self):
        return self.admin.read_only

    @property
    def admin_list_editable(self):
        return self.admin.list_editable

    @property
    def admin_list_filter(self):
        return self.admin.list_filter

    @property
    def admin_list_search(self):
        return self.admin.list_search

    @property
    def admin_fields(self):
        return self.admin.fields

    @property
    def admin_tab_fields(self):
        return self.admin.tab_fields

    @property
    def admin_tabs(self):
        return self.admin.tabs

    @property
    def tab_names(self):
        return self.admin.tab_names

    @property
    def admin_inlines(self):
        return self.admin.inlines

    @property
    def admin_has_polymorphic_inlines(self):
        return self.admin.has_polymorphic_inlines

    def __init__(self, collection_set) -> None:
        super().__init__()

        # self.raw_ = parse_result

        """:type: CollectionSetDef"""
        self.collection_set = collection_set

        self.ref = None
        self.short_ref = self.ref

        self.name = None
        self.name_plural = None
        self.to_string = None

        self.polymorphic = False
        self.parent = None
        self.child_collections = []

        self.mixin_classes = []
        self.validators = []
        self.signal_handlers = []

        self.translatable = False
        self.admin = None

        self.tree = False
        self.tree_polymorphic_list = False
        self.sortable = False
        self.sortable_field = None

        self.fields = {}

        self.admin_js = []
        self.admin_css = []


        self.rest_conf = {}
        self.published_apis = {}

        self.rest_mode = None
        self.rest = False
        self.api = False

        self.extend_name = False

    def set_parent(self, parent):

        if parent not in self.collection_set.collections:
            raise ValidationException(
                'Collection "{}" marked as parent for "{}", but not yet loaded or do not exist.'.format(
                    parent, self.ref
                ))

        self.parent = self.collection_set.collections[parent]  # type: CollectionDef
        if self.parent.parent:
            raise ValidationException(
                'Collection "{}" marked as parent for "{}", but it\'s already has parent. Multilevel polymorphism is not supported yet.'.format(
                    parent, self.ref
                ))
        self.parent.polymorphic = True
        self.parent.child_collections.append(self)

    def parse_extras(self):

        # TODO: handle parent
        if self.parent:
            self.admin_tab_fields = self.parent.admin_tab_fields.copy()
            self.admin_tabs = self.parent.admin_tabs.copy()
            self.tab_names = self.parent.tab_names.copy()

            self.translatable = self.parent.translatable or self.translatable

        extras = self.collection_set.parser.get_extras_available()

        loaded_extras = []

        # TODO: process extras
        # for extra in self.raw_.extras:
        #
        #     try:
        #         extra_cls = extras[extra.extra_name]
        #         try:
        #             extra_instance = extra_cls()
        #             extra_instance.parse(extra, self)
        #             loaded_extras.append(extra_instance)
        #
        #         except ParseException as e:
        #             handle_parse_exception(e, extra.extra_body,
        #                                    '@{} expression for collection "{}"'.format(extra.extra_name, self.name))
        #     except KeyError as e:
        #         raise ValidationException('Extra not found: {}, reason: {}'.format(extra.extra_name, e))

        for extra in loaded_extras:
            extra.post_process()

    @property
    def model_class_declaration(self):
        classes = []
        if self.parent:
            classes.append(self.parent.class_name)
        elif self.polymorphic:
            if self.tree:
                classes.append('PolymorphicMPTTModel')
            else:
                classes.append('PolymorphicModel')

        elif self.tree:
            classes.append('MPTTModel')

        if not classes:
            classes.append('models.Model')

        return ', '.join(classes)

    @property
    def child_model_classes(self):
        if not self.polymorphic:
            return []

        return [x.class_name for x in self.child_collections]

    @property
    def admin_class_declaration(self):
        return ', '.join([x[1] for x in self.admin_classes])

    @property
    def admin_classes(self):
        classes = []

        model_admin_added = False

        if self.admin_has_polymorphic_inlines:
            classes.append(('polymorphic.admin', 'PolymorphicInlineSupportMixin'))

        if self.parent:
            classes.append(('polymorphic.admin', 'PolymorphicChildModelAdmin'))
            model_admin_added = True
        elif self.polymorphic:
            classes.append(('polymorphic.admin', 'PolymorphicParentModelAdmin'))
            model_admin_added = True

        if self.sortable:
            classes.append(('suit.admin', 'SortableModelAdmin'))
            model_admin_added = True

        if self.tree:
            classes.append(('mptt.admin', 'DraggableMPTTAdmin'))
            model_admin_added = True

        if self.translatable:
            classes.append(('cratis_i18n.admin', 'TranslatableModelAdmin'))
            model_admin_added = True

        if not model_admin_added:
            classes.append(('django.contrib.admin', 'ModelAdmin'))

        return classes

    @property
    def admin_inline_classes(self):
        return [x.class_name for x in self.admin_inlines]

    def fields_for_tab(self, tab):
        fields = []
        for name, tab_name in self.admin_tab_fields.items():
            # skip references
            if isinstance(self.all_and_inherited_fields_map[name], ReferenceField):
                continue

            if tab_name == tab:
                fields.append(self.all_and_inherited_fields_map[name])

        return fields

    @property
    def empty_admin(self):
        return not (self.admin_fields or self.admin_list)

    def check_field_exists(self, field_name):
        fields = self.expand_field_pattern(field_name)
        return len(fields) > 0

    def expand_field_pattern(self, field_pattern):
        fields = []

        # if local_only
        if field_pattern.startswith('.'):
            field_pattern = field_pattern[1:]
        else:
            if self.parent:
                fields += self.parent.expand_field_pattern(field_pattern)

        if field_pattern.endswith('*'):
            prefix = field_pattern[:-1]
            for key in self.fields.keys():
                if key.startswith(prefix):
                    fields.append(key)

        elif field_pattern.startswith('*'):
            suffix = field_pattern[1:]
            for key in self.fields.keys():
                if key.endswith(suffix):
                    fields.append(key)

        elif field_pattern in self.fields:
            fields.append(field_pattern)

        return fields

    def filter_fields(self, filter_spec, include_refs=False, field_set=None):
        allow_parents = filter_spec[0] != '.*'

        if not field_set:
            if not include_refs:

                fields = self.own_fields
                if allow_parents and self.parent:
                    fields = tuple(self.parent.own_fields) + tuple(fields)
            else:
                fields = self.fields.values()
                if allow_parents and self.parent:
                    fields = tuple(self.parent.fields.values()) + tuple(fields)
        else:
            fields = field_set

        if filter_spec[0] in ('*', '.*'):
            exclude_list = []
            for item in filter_spec[1:]:
                if item[0] != '^':
                    raise ValidationException(
                        'If * used in field list, then all other fields should start with ^ (exclude)')

                new_fields = self.expand_field_pattern(item[1:])
                if not new_fields:
                    raise ValidationException(
                        'Field name specified for exclude: "{}" does not exist'.format(item[1:]))
                exclude_list += new_fields

            return [field for field in fields if field.name not in exclude_list]

        else:
            include_list = []
            for item in filter_spec:
                if item == '*':
                    raise ValidationException('* maybe used only as first item in field list')
                if item[0] == '^':
                    raise ValidationException('^ maybe used only with * as first item in field list')

                new_fields = self.expand_field_pattern(item)
                if not new_fields:
                    raise ValidationException(
                        'Field name specified for include: "{}" does not exist'.format(item))

                include_list += new_fields

            return [field for field in fields if field.name in include_list]

    @property
    def class_name(self):
        class_name = ''.join([x.capitalize() for x in self.ref.split('_')])

        # if not self.parent:
        return class_name
        # else:
        #     return '{}{}'.format(self.parent.class_name, class_name)

    @property
    def fqdn(self):
        return '.'.join([self.collection_set.app_name, self.class_name])

    @property
    def display_field(self):
        for field in self.fields.values():
            if field.display_field:
                return field

    @property
    def all_fields(self):
        return self.fields.values()

    @property
    def all_and_inherited_fields_map(self):
        if not self.parent:
            return self.fields

        all_fields = {}
        all_fields.update(self.parent.fields)
        all_fields.update(self.fields)
        return all_fields

    @property
    def own_fields(self):
        return [field for field in self.fields.values() if field.type_name not in ['ref']]

    @property
    def expression_fields(self):
        admin_list = [x.slug for x in self.admin_list]
        return [field for field in self.fields.values() if field.type_name == 'expr' and field.slug not in admin_list]

    @property
    def prepopulated_fields(self):
        prepopulated = {}

        for field in self.all_and_inherited_fields_map.values():
            info = field.get_prepopulated_from()
            if info:
                prepopulated[field.name] = info

        return prepopulated

    @property
    def translatable_fields(self):
        return [field for field in self.own_fields if field.translatable]

    @property
    def expression_fields(self):
        from zmei_generator.fields.expression import ExpressionFieldDef
        return [field for field in self.fields.values() if isinstance(field, ExpressionFieldDef)]

    @property
    def read_only_fields(self):
        return [x for x in self.expression_fields if x in self.all_fields]

    @property
    def relation_fields(self):
        from zmei_generator.fields.relation import RelationDef
        return [field for field in self.own_fields if isinstance(field, RelationDef)]

    def get_required_apps(self):
        all_apps = []
        for field in self.all_fields:
            all_apps.extend(field.get_required_apps())
        return all_apps

    def get_required_deps(self):
        all_deps = []
        for field in self.all_fields:
            all_deps.extend(field.get_required_deps())
        return all_deps

    def get_required_urls(self):
        all_urls = []
        for field in self.all_fields:
            all_urls.extend(field.get_required_urls())
        return all_urls

    def get_required_settings(self):
        all_settings = {}
        for field in self.all_fields:
            all_settings.update(field.get_required_settings())
        return all_settings

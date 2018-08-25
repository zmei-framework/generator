from cPyparsing import ParseException

from cratis_generator.config.domain.exceptions import ValidationException
from cratis_generator.config.domain.reference_field import ReferenceField
from cratis_generator.generator.utils import handle_parse_exception


class CollectionDef(object):
    #
    # ref: str
    # name: str
    # fields: Dict[str, FieldDef]

    # rest: False
    # translatable: False

    def __init__(self, parse_result, collection_set) -> None:
        super().__init__()

        self.raw_ = parse_result

        """:type: CollectionSetDef"""
        self.collection_set = collection_set

        self.ref = parse_result.ref
        self.short_ref = self.ref

        self.name = parse_result.name
        self.name_plural = parse_result.name_plural
        self.to_string = parse_result.to_string

        self.polymorphic = False
        self.parent = False
        self.child_collections = []

        self.mixin_classes = []
        self.validators = []
        self.signal_handlers = []

        if parse_result.parent:
            if parse_result.parent not in self.collection_set.collections:
                raise ValidationException(
                    'Collection "{}" marked as parent for "{}", but not yet loaded or do not exist.'.format(
                        parse_result.parent, self.ref
                    ))

            if parse_result.parent_separator == '~>':
                self.ref = '{}_{}'.format(parse_result.parent, self.ref)

            self.parent = self.collection_set.collections[parse_result.parent]  # type: CollectionDef
            if self.parent.parent:
                raise ValidationException(
                    'Collection "{}" marked as parent for "{}", but it\'s already has parent. Multilevel polymorphism is not supported yet.'.format(
                        parse_result.parent, self.ref
                    ))
            self.parent.polymorphic = True
            self.parent.child_collections.append(self)

        self.translatable = False
        self.admin = False

        self.tree = False
        self.tree_polymorphic_list = False
        self.sortable = False
        self.sortable_field = None

        if not self.name:
            self.name = ' '.join(self.ref.split('_')).capitalize()

        self.fields = {}
        for field in parse_result.fields:
            if field.calculated_expression or field.calculated_static_expression:
                from cratis_generator.fields.expression import ExpressionFieldDef
                field_cls = ExpressionFieldDef
            else:
                field_cls = self.collection_set.parser.get_field_class(field.type_name)

            self.fields[field.name] = field_cls(self, field)

        self.admin_list = None
        self.admin_js = []
        self.admin_css = []
        self.admin_list_editable = None
        self.admin_list_filter = None
        self.admin_list_search = None
        self.admin_list = None
        self.admin_fields = None
        self.admin_inlines = []
        self.admin_has_polymorphic_inlines = False

        self.admin_tab_fields = {}
        self.admin_tabs = []
        self.tab_names = {}

        self.rest_conf = {}
        self.published_apis = {}

        self.rest_mode = None
        self.rest = False
        self.api = False

    def parse_extras(self):

        if self.parent:
            self.admin_tab_fields = self.parent.admin_tab_fields.copy()
            self.admin_tabs = self.parent.admin_tabs.copy()
            self.tab_names = self.parent.tab_names.copy()

            self.translatable = self.parent.translatable or self.translatable

        extras = self.collection_set.parser.get_extras_available()

        loaded_extras = []
        for extra in self.raw_.extras:

            try:
                extra_cls = extras[extra.extra_name]
                try:
                    extra_instance = extra_cls()
                    extra_instance.parse(extra, self)
                    loaded_extras.append(extra_instance)

                except ParseException as e:
                    handle_parse_exception(e, extra.extra_body,
                                           '@{} expression for collection "{}"'.format(extra.extra_name, self.name))
            except KeyError as e:
                raise ValidationException('Extra not found: {}, reason: {}'.format(extra.extra_name, e))

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
            inlcude_list = []
            for item in filter_spec:
                if item == '*':
                    raise ValidationException('* maybe used only as first item in field list')
                if item[0] == '^':
                    raise ValidationException('^ maybe used only with * as first item in field list')

                new_fields = self.expand_field_pattern(item)
                if not new_fields:
                    raise ValidationException(
                        'Field name specified for include: "{}" does not exist'.format(item))

                inlcude_list += new_fields

            return [field for field in fields if field.name in inlcude_list]

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
        from cratis_generator.fields.expression import ExpressionFieldDef
        return [field for field in self.fields.values() if isinstance(field, ExpressionFieldDef)]

    @property
    def read_only_fields(self):
        return [x for x in self.expression_fields if x in self.all_fields]

    @property
    def relation_fields(self):
        from cratis_generator.fields.relation import RelationDef
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



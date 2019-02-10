from zmei_generator.domain.extensions import Extendable
from zmei_generator.domain.frozen import FrozenClass
from zmei_generator.parser.errors import GlobalScopeValidationError as ValidationException


class ModelDef(Extendable, FrozenClass):
    #
    # ref: str
    # name: str
    # fields: Dict[str, FieldDef]

    # rest: False
    # translatable: False

    def __init__(self, application) -> None:
        super().__init__()

        # self.raw_ = parse_result

        """:type: ApplicationDef"""
        self.application = application

        self.ref = None
        self.short_ref = self.ref

        self.name = None
        self.name_plural = None
        self.extend_name = False
        self.to_string = None

        self.polymorphic = False
        self.parent = None
        self.child_models = []

        self.fields = {}
        self.translatable = False

        self.mixin_classes = []
        self.validators = []
        self.signal_handlers = []
        self.tree = False
        self.tree_polymorphic_list = False
        self.sortable = False
        self.sortable_field = None

        self.date_hierarchy = None

        self._freeze()

    def post_process(self):
        for field in list(self.fields.values()):
            field.post_process()

    def set_parent(self, parent):

        if parent not in self.application.models:
            raise ValidationException(
                'Model "{}" marked as parent for "{}", but not yet loaded or do not exist.'.format(
                    parent, self.ref
                ))

        self.parent = self.application.models[parent]  # type: ModelDef
        if self.parent.parent:
            raise ValidationException(
                'Model "{}" marked as parent for "{}", but it\'s already has parent. Multilevel polymorphism is not supported yet.'.format(
                    parent, self.ref
                ))
        self.parent.polymorphic = True
        self.parent.child_models.append(self)

        if self.parent.translatable:
            self.translatable = True

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

        return [x.class_name for x in self.child_models]

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
        return '.'.join([self.application.app_name, self.class_name])

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
    def own_fields_non_expr(self):
        return [field for field in self.fields.values() if field.type_name not in ['ref', 'expr']]

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
        from zmei_generator.contrib.web.fields.expression import ExpressionFieldDef
        return [field for field in self.fields.values() if isinstance(field, ExpressionFieldDef)]

    @property
    def read_only_fields(self):
        return [x for x in self.expression_fields if x in self.all_fields]

    @property
    def relation_fields(self):
        from zmei_generator.contrib.web.fields.relation import RelationDef
        return [field for field in self.own_fields if isinstance(field, RelationDef)]

    def get_required_apps(self):
        all_apps = []
        for field in self.all_fields:
            all_apps.extend(field.get_required_apps())

        if self.polymorphic:
            all_apps.append('polymorphic')

        return all_apps

    def get_required_deps(self):
        all_deps = []
        for field in self.all_fields:
            all_deps.extend(field.get_required_deps())

        if self.polymorphic:
            all_deps.append('django-polymorphic')

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

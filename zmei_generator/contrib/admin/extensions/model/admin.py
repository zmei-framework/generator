from zmei_generator.contrib.web.fields.expression import ExpressionFieldDef
from zmei_generator.domain.application_def import FieldDeclaration
from zmei_generator.domain.reference_field import ReferenceField
from zmei_generator.parser.errors import GlobalScopeValidationError as ValidationException
from zmei_generator.domain.extensions import Extension, ModelExtension
from zmei_generator.contrib.web.fields.date import AutoNowDateTimeFieldDef, AutoNowAddDateTimeFieldDef


class AdminModelExtension(ModelExtension):

    def __init__(self, model) -> None:
        super().__init__(model)

        self.model = model

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

        # media files
        self.css = []
        self.js = []

    def register_tab(self, name, verbose_name, fields_expr, prepend=False):

        self.tabs_raw.append(
            (name, verbose_name, fields_expr, prepend)
        )

    def add_tab(self, name, verbose_name, fields_expr, prepend):
        """
        Do delayed field calculation as we need to wait
        until all Reference fields are created
        """

        fields = self.model.filter_fields(fields_expr, include_refs=True)

        self.add_tab_fieldset(name, verbose_name, fields, prepend)

    def add_tab_fieldset(self, name, verbose_name, fields, prepend):

        # filter out fields that are not meant to be rendered
        if self.fields:
            fields = [f for f in fields if f in self.fields or isinstance(f, ReferenceField)]
        self.tab_names[name] = verbose_name or name.capitalize()
        for field in fields:
            self.tab_fields[field.name] = name

        if name not in self.tabs:
            if prepend:
                self.tabs = [name] + self.tabs
            else:
                self.tabs.append(name)

    def check_tab_consistency(self):
        general_fields = []
        for field in (self.fields or self.model.all_fields):

            if field.name not in self.tab_fields:
                general_fields.append(field)

        if len(general_fields) > 0:
            self.add_tab_fieldset('general', 'General', general_fields, prepend=True)

    def post_process(self):
        if self.model.parent and self.model.parent.supports(AdminModelExtension):
            self.tab_fields = self.model.parent[AdminModelExtension].tab_fields.copy()
            self.tabs = self.model.parent[AdminModelExtension].tabs.copy()
            self.tab_names = self.model.parent[AdminModelExtension].tab_names.copy()
            self.inlines.extend(self.model.parent[AdminModelExtension].inlines.copy())

        for tab in self.tabs_raw:
            self.add_tab(*tab)

        self.check_tab_consistency()

        # set tabs to inlines
        inline_map = {x.inline_name: x for x in self.inlines}

        for field_name, tab in self.tab_fields.items():
            if field_name in inline_map:
                inline_map[field_name].tab = tab

        for inline in self.inlines:
            inline.post_process()

        # check for auto-fields
        for field in self.model.all_and_inherited_fields_map.values():
            if isinstance(field, (AutoNowDateTimeFieldDef, AutoNowAddDateTimeFieldDef)):
                if not self.read_only:
                    self.read_only = []

                self.read_only.append(field)

    def fields_for_tab(self, tab):
        fields = []
        for name, tab_name in self.tab_fields.items():
            # skip references
            if isinstance(self.model.all_and_inherited_fields_map[name], ReferenceField):
                continue

            if isinstance(self.model.all_and_inherited_fields_map[name], ExpressionFieldDef):
                continue

            if tab_name == tab:
                fields.append(self.model.all_and_inherited_fields_map[name])

        return fields

    @property
    def class_declaration(self):
        return ', '.join([x[1] for x in self.classes])

    @property
    def classes(self):
        classes = []

        model_admin_added = False

        if self.has_polymorphic_inlines:
            classes.append(('polymorphic.admin', 'PolymorphicInlineSupportMixin'))

        if self.model.parent:
            classes.append(('polymorphic.admin', 'PolymorphicChildModelAdmin'))
            model_admin_added = True

        elif self.model.polymorphic:
            children_have_admins = len([x for x in self.model.child_models if x.supports(AdminModelExtension)]) > 0

            if children_have_admins:
                classes.append(('polymorphic.admin', 'PolymorphicParentModelAdmin'))
                model_admin_added = True

        if self.model.sortable:
            classes.append(('suit.admin', 'SortableModelAdmin'))
            model_admin_added = True

        if self.model.tree:
            classes.append(('mptt.admin', 'DraggableMPTTAdmin'))
            model_admin_added = True

        if self.model.translatable:
            classes.append(('modeltranslation.admin', 'TabbedTranslationAdmin'))
            model_admin_added = True

        if not model_admin_added:
            classes.append(('django.contrib.admin', 'ModelAdmin'))

        return classes

    @property
    def inline_classes(self):
        return [x.class_name for x in self.inlines]


class AdminInlineConfig(object):
    def __init__(self, admin, name):
        self.admin = admin
        self.model = admin.model
        self.inline_name = name
        self.fields_expr = ['*']
        self.extension_count = 0
        self.inline_type = 'tabular'

        self.field = None
        self.source_field_name = None
        self.target_model = None
        self.field_set = None
        self.tab = None

    def post_process(self):
        model = self.admin.model

        if not model.check_field_exists(self.inline_name):
            raise ValidationException(
                'Field name specified for admin inline: "{}" does not exist'.format(self.inline_name))

        field = model.all_and_inherited_fields_map[self.inline_name]

        if not isinstance(field, ReferenceField):
            raise ValidationException(
                'Field name specified for admin inline: "{}" is not a reference field (back relation).'.format(
                    self.inline_name))

        self.field = field
        self.source_field_name = field.source_field_name
        self.target_model = field.target_model

        self.field_set = [f for f in field.target_model.filter_fields(self.fields_expr) if
                          f.name != self.source_field_name]

        if self.extension_count:
            if self.extension_count > 0 and self.inline_type == 'polymorphic':
                raise ValidationException('{}->{}: When using inline type "polymorphic" extension must be 0'.format(
                    self.model.name,
                    self.inline_name
                ))

    @property
    def field_names(self):
        return [f.name for f in self.field_set]

    @property
    def class_name(self):
        return '{}{}Inline'.format(
            self.model.class_name,
            ''.join([x.capitalize() for x in self.inline_name.split('_')])
        )

    @property
    def type_declarations(self):

        declarations = []

        if self.inline_type == 'tabular':
            if self.target_model.sortable:
                declarations.append(FieldDeclaration('suit.admin', 'SortableTabularInline'))
            else:
                declarations.append(FieldDeclaration('django.contrib.admin', 'TabularInline'))
        elif self.inline_type == 'polymorphic':
            if self.target_model.sortable:
                declarations.append(FieldDeclaration('cratis_admin.admin', 'StackedPolymorphicSortableInline'))
            else:
                declarations.append(FieldDeclaration('polymorphic.admin', 'StackedPolymorphicInline'))
        else:
            if self.target_model.sortable:
                declarations.append(FieldDeclaration('suit.admin', 'SortableStackedInline'))
            else:
                declarations.append(FieldDeclaration('django.contrib.admin', 'StackedInline'))

        # if self.target_model.translatable:
        #     declarations.append(FieldDeclaration('modeltranslation.admin', 'TranslationInlineModelAdmin'))

        return declarations

    @property
    def parent_classes(self):
        return [x.declaration for x in self.type_declarations]

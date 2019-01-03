from zmei_generator.config.domain.collection_def import CollectionDef
from zmei_generator.config.domain.collection_set_def import FieldDeclaration
from zmei_generator.parser.errors import GlobalScopeValidationError as ValidationException
from zmei_generator.config.domain.field_def import FieldDef
from zmei_generator.config.domain.reference_field import ReferenceField
from zmei_generator.generator.utils import gen_args


class RelationDef(FieldDef):
    def __init__(self, collection: CollectionDef, field) -> None:
        super().__init__(collection, field)

        self.ref_collection_def = None  # raw data

        # filled in post process
        self.related_name = None
        self.ref_collection = None
        self.related_class = None
        self.related_app = None

    def post_process(self):

        if self.ref_collection_def:
            ref_collection = self.collection.collection_set.resolve_collection(self.ref_collection_def)

            self.ref_collection = ref_collection
            self.related_class = f'{ref_collection.collection_set.app_name}.{ref_collection.class_name}'

        if self.ref_collection and self.related_name in self.ref_collection.fields:
            raise ValidationException('Can not override field with related field: {}'.format(self.related_name))

        if self.ref_collection and self.related_name:
            self.ref_collection.fields[self.related_name] = \
                ReferenceField(self.ref_collection, self.collection, self.related_name, self)

    @property
    def qualifier(self):
        return ''

    @property
    def is_many(self):
        return None

    @property
    def is_many_reverse(self):
        return None

    @property
    def widget(self):
        return None

    def get_rest_field(self):
        return None

    def get_rest_inline_collection(self):
        return self.ref_collection


class RelationOneDef(RelationDef):

    def prepare_field_arguemnts(self, own_args=None):
        args = super().prepare_field_arguemnts(own_args)
        args['on_delete'] = 'models.PROTECT'
        return args

    def get_flutter_field(self):
        if self.ref_collection:
            return f'{self.ref_collection.class_name}'
        else:
            return 'dynamic'

    def get_flutter_from_json(self, name):
        if self.ref_collection:
            return f"{self.ref_collection.class_name}.fromJson(data['{name}'])"
        else:
            return f"data['{name}']"

    def get_model_field(self):
        args = self.prepare_field_arguemnts({'related_name': self.related_name or '+'})

        return FieldDeclaration(
            [('django.db', 'models')],
            'models.ForeignKey("{}", {})'.format(self.related_class, gen_args(args, ['on_delete']))
        )

    def get_admin_widget(self):
        if not self.collection.collection_set.features.cratis:
            return None
        return FieldDeclaration(
            [('django_select2.forms', 'Select2Widget')],
            'Select2Widget'
        )

    @property
    def qualifier(self):
        return '1'

    @property
    def is_many(self):
        return False

    @property
    def is_many_reverse(self):
        return True


class RelationOne2OneDef(RelationDef):

    def get_flutter_field(self):
        if self.ref_collection:
            return f'{self.ref_collection.class_name}'
        else:
            return 'dynamic'

    def get_flutter_from_json(self, name):
        if self.ref_collection:
            return f"{self.ref_collection.class_name}.fromJson(data['{name}'])"
        else:
            return f"data['{name}']"

    def get_model_field(self):
        args = self.prepare_field_arguemnts({'related_name': self.related_name or '+'})

        return FieldDeclaration(
            [('django.db', 'models')],
            'models.OneToOneField("{}", {}, on_delete=models.CASCADE)'.format(self.related_class, gen_args(args, ['on_delete']))
        )

    def get_admin_widget(self):
        if not self.collection.collection_set.features.cratis:
            return None
        return FieldDeclaration(
            [('django_select2.forms', 'Select2Widget')],
            'Select2Widget'
        )

    @property
    def qualifier(self):
        return '1'

    @property
    def is_many(self):
        return False

    @property
    def is_many_reverse(self):
        return False


class RelationManyDef(RelationDef):

    def get_flutter_field(self):
        if self.ref_collection:
            return f'List<{self.ref_collection.class_name}>'
        else:
            return 'dynamic'

    def get_flutter_from_json(self, name):
        if self.ref_collection:
            return f"data['{name}'].map<{self.ref_collection.class_name}>((item) => {self.ref_collection.class_name}.fromJson(item)).toList()"
        else:
            return f"data['{name}']"

    def get_model_field(self):
        args = self.prepare_field_arguemnts({'related_name': self.related_name or '+'})

        if 'null' in args:
            del args['null']

        return FieldDeclaration(
            [('django.db', 'models')],
            'models.ManyToManyField("{}", {})'.format(self.related_class, gen_args(args, ['on_delete']))
        )

    def get_admin_widget(self):
        if not self.collection.collection_set.features.cratis:
            return None

        return FieldDeclaration(
            [('django_select2.forms', 'Select2MultipleWidget')],
            'Select2MultipleWidget'
        )

    @property
    def admin_list_renderer(self):
        return """return ', '.join(map(str, obj.{}.all()))""".format(self.name)

    @property
    def qualifier(self):
        return '*'

    @property
    def is_many(self):
        return True

    @property
    def is_many_reverse(self):
        return True

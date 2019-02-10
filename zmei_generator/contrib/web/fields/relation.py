from zmei_generator.domain.model_def import ModelDef
from zmei_generator.domain.application_def import FieldDeclaration
from zmei_generator.domain.reference_field import ReferenceField
from zmei_generator.parser.errors import GlobalScopeValidationError as ValidationException
from zmei_generator.domain.field_def import FieldDef
from zmei_generator.generator.utils import gen_args


class RelationDef(FieldDef):
    def __init__(self, model: ModelDef, field) -> None:
        super().__init__(model, field)

        self.ref_model_def = None  # raw data

        # filled in post process
        self.related_name = None
        self.ref_model = None
        self.related_class = None
        self.related_app = None
        self.on_delete = 'PROTECT'

    def post_process(self):

        if self.ref_model_def:
            ref_model = self.model.application.resolve_model(self.ref_model_def)

            self.ref_model = ref_model
            self.related_class = f'{ref_model.application.app_name}.{ref_model.class_name}'

        if self.ref_model and self.related_name in self.ref_model.fields:
            raise ValidationException('Can not override field with related field: {}'.format(self.related_name))

        if self.ref_model and self.related_name:
            self.ref_model.fields[self.related_name] = \
                ReferenceField(self.ref_model, self.model, self.related_name, self)

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

    def get_rest_inline_model(self):
        return self.ref_model


class RelationOneDef(RelationDef):

    def prepare_field_arguemnts(self, own_args=None):
        args = super().prepare_field_arguemnts(own_args)
        args['on_delete'] = f'models.{self.on_delete}'
        return args

    def get_flutter_field(self):
        if self.ref_model:
            return f'{self.ref_model.class_name}'
        else:
            return 'dynamic'

    def get_flutter_from_json(self, name):
        if self.ref_model:
            return f"{self.ref_model.class_name}.fromJson(data['{name}'])"
        else:
            return f"data['{name}']"

    def get_model_field(self):
        args = self.prepare_field_arguemnts({'related_name': self.related_name or '+'})

        return FieldDeclaration(
            [('django.db', 'models')],
            'models.ForeignKey("{}", {})'.format(self.related_class, gen_args(args, ['on_delete']))
        )

    def get_admin_widget(self):
        return None
        # if select2 is installed
        # return FieldDeclaration(
        #     [('django_select2.forms', 'Select2Widget')],
        #     'Select2Widget'
        # )

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
        if self.ref_model:
            return f'{self.ref_model.class_name}'
        else:
            return 'dynamic'

    def get_flutter_from_json(self, name):
        if self.ref_model:
            return f"{self.ref_model.class_name}.fromJson(data['{name}'])"
        else:
            return f"data['{name}']"

    def get_model_field(self):
        args = self.prepare_field_arguemnts({'related_name': self.related_name or '+'})

        return FieldDeclaration(
            [('django.db', 'models')],
            'models.OneToOneField("{}", {}, on_delete=models.CASCADE)'.format(self.related_class, gen_args(args, ['on_delete']))
        )

    def get_admin_widget(self):
        return None

        # return FieldDeclaration(
        #     [('django_select2.forms', 'Select2Widget')],
        #     'Select2Widget'
        # )

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
        if self.ref_model:
            return f'List<{self.ref_model.class_name}>'
        else:
            return 'dynamic'

    def get_flutter_from_json(self, name):
        if self.ref_model:
            return f"data['{name}'].map<{self.ref_model.class_name}>((item) => {self.ref_model.class_name}.fromJson(item)).toList()"
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
        return None  # TODO: requires to install package and url, which is not implemented now

        # return FieldDeclaration(
        #     [('django_select2.forms', 'Select2MultipleWidget')],
        #     'Select2MultipleWidget'
        # )

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

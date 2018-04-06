from cratis_generator.config.domain import FieldDef, CollectionDef, FieldDeclaration, ValidationException, \
    ReferenceField
from cratis_generator.config.grammar import ref, class_name, ref_or_class_name, identifier
from cratis_generator.generator.utils import gen_args
from pyparsing import *


class RelationDef(FieldDef):
    def __init__(self, collection: CollectionDef, field) -> None:
        super().__init__(collection, field)

        self.related_name = None
        self.ref_collection = None

    def parse_options(self):
        options_grammar = ref_or_class_name + Optional(
            Suppress('->') + identifier.setResultsName('related_name')) + stringEnd

        result = options_grammar.parseString(self.options)

        self.related_name = result.related_name

        if result.ref:
            try:
                ref_collection = self.collection.collection_set.collections[result.ref]
            except KeyError:
                raise ValidationException('Reference to unknown collection: #{}'.format(result.ref))
            self.ref_collection = ref_collection

            if self.related_name:
                if self.related_name in ref_collection.fields:
                    raise ValidationException('Can not override field with related field: {}'.format(self.related_name))

                ref_collection.fields[self.related_name] = ReferenceField(ref_collection, self.collection, self.related_name, self)

            self.related_class = ref_collection.class_name
        else:
            self.related_class = result.class_name

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
    def get_model_field(self, collection):
        args = self.prepare_field_arguemnts({'related_name': self.related_name or '+'})

        return FieldDeclaration(
            [('django.db', 'models')],
            'models.ForeignKey("{}", {}, on_delete=models.CASCADE)'.format(self.related_class, gen_args(args))
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
    def get_model_field(self, collection):
        args = self.prepare_field_arguemnts({'related_name': self.related_name or '+'})

        return FieldDeclaration(
            [('django.db', 'models')],
            'models.OneToOneField("{}", {}, on_delete=models.CASCADE)'.format(self.related_class, gen_args(args))
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
    def get_model_field(self, collection):
        args = self.prepare_field_arguemnts({'related_name': self.related_name or '+'})

        if 'null' in args:
            del args['null']

        return FieldDeclaration(
            [('django.db', 'models')],
            'models.ManyToManyField("{}", {})'.format(self.related_class, gen_args(args))
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

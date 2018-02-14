from cratis_generator.config.domain import CollectionDef, ValidationException
from cratis_generator.config.extras import Extra


class SortableExtra(Extra):

    @classmethod
    def get_name(cls):
        return 'sortable'

    def parse(self, extra, collection: CollectionDef):
        field_name = extra.extra_body.strip()

        if not len(field_name):
            raise ValidationException('@sortable: You should specify field name for sortable.')

        if not collection.check_field_exists(field_name):
            raise ValidationException('@sortable: Field "{}" does not belong to collection #{}'.format(field_name, collection.ref))

        collection.sortable = True
        collection.sortable_field = field_name


class OrderExtra(Extra):

    @classmethod
    def get_name(cls):
        return 'order'

    def parse(self, extra, collection: CollectionDef):
        field_name = extra.extra_body.strip()

        if not len(field_name):
            raise ValidationException('@sortable: You should specify field name for sortable.')

        collection.sortable_field = field_name


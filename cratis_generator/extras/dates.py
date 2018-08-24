from cratis_generator.config.domain.collection_def import CollectionDef
from cratis_generator.config.domain.exceptions import ValidationException
from cratis_generator.config.extras import Extra


class DateTreeExtra(Extra):

    @classmethod
    def get_name(cls):
        return 'dateTree'

    def parse(self, extra, collection: CollectionDef):
        field_name = extra.extra_body.strip()

        if not len(field_name):
            raise ValidationException('You should specify field name for date_hierarchy.')

        collection.date_hierarchy = field_name

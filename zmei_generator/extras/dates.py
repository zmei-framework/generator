from zmei_generator.config.domain.collection_def import CollectionDef
from zmei_generator.config.domain.exceptions import ValidationException
from zmei_generator.config.extras import Extra


class DateTreeExtra(Extra):

    def parse(self, extra, collection: CollectionDef):
        field_name = extra.extra_body.strip()

        if not len(field_name):
            raise ValidationException('You should specify field name for date_hierarchy.')

        collection.date_hierarchy = field_name
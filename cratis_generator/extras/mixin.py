from cratis_generator.config.domain import CollectionDef, ValidationException
from cratis_generator.config.extras import Extra
from django.db import models
from django.utils.module_loading import import_string


class MixinExtra(Extra):

    @classmethod
    def get_name(cls):
        return 'mixin'

    def parse(self, extra, collection: CollectionDef):
        class_name = extra.extra_body.strip()

        parts = class_name.split('.')
        collection.mixin_classes.append(
            ('.'.join(parts[:-1]), parts[-1])
        )



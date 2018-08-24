from cratis_generator.config.domain.collection_def import CollectionDef
from cratis_generator.config.extras import Extra


class MixinExtra(Extra):

    @classmethod
    def get_name(cls):
        return 'mixin'

    def parse(self, extra, collection: CollectionDef):
        class_name = extra.extra_body.strip()

        parts = class_name.split('.')
        model_cls = parts[-1]

        if model_cls == collection.class_name:
            alias = '{}_'.format(model_cls)
        else:
            alias = model_cls

        collection.mixin_classes.append(
            ('.'.join(parts[:-1]), parts[-1], alias)
        )



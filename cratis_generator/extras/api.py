from cratis_generator.config.domain.collection_def import CollectionDef
from cratis_generator.config.domain.exceptions import ValidationException
from cratis_generator.config.extras import Extra


class ApiExtra(Extra):

    @classmethod
    def get_name(cls):
        return 'api'

    def parse(self, extra, collection: CollectionDef):
        self.field_name = extra.extra_body.strip()
        self.collection = collection

    def post_process(self):
        if not len(self.field_name):
            raise ValidationException(
                f'@api error: you should specify list of published apis explicitly.')
        else:
            all_apis = {}
            for api in [x.strip() for x in self.field_name.split(',')]:
                if api not in self.collection.rest_conf:
                    raise ValidationException(
                        f'@api error: no such @rest config "{api}"')

                all_apis[api] = self.collection.rest_conf[api]

            self.collection.published_apis = all_apis

        self.collection.api = True
        self.collection.collection_set.api = True


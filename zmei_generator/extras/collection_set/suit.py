import json

from zmei_generator.config.domain.collection_set_extra import CollectionSetExtra


class SuitCsExtra(CollectionSetExtra):

    def __init__(self, collection_set):
        super().__init__(collection_set)

        self.app_name = None
        self.menu = [{'label': 'auth', 'app': 'auth'}]

    @classmethod
    def get_name(cls):
        return 'suit'

    def get_required_apps(self):
        return ['suit']

    def get_required_deps(self):
        return ['django-suit']

    @classmethod
    def write_settings(cls, apps, f):

        # menu

        menu = []

        for app, collection_set in apps.items():
            if collection_set.suit and collection_set.suit.menu:
                menu.extend(collection_set.suit.menu)

            if collection_set.admin:
                models = []
                for collection in collection_set.collections.values():
                    if collection.admin and not collection.parent:
                        models.append(f'{app}.{collection.class_name}', )

                if len(models):
                    menu.append({'label': app, 'models': models})

        # app name

        app_name = None
        for app, collection_set in apps.items():
            if collection_set.suit and collection_set.suit.app_name:
                app_name = collection_set.suit.app_name

        f.write("\nSUIT_CONFIG = {")
        f.write("\n'MENU': ")
        f.write(json.dumps(menu, indent=4))
        f.write(',')

        if app_name:
            f.write("\n'ADMIN_NAME': " + json.dumps(app_name))

        f.write("\n} ")









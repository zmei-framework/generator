import json

from zmei_generator.contrib.admin.extensions.model.admin import AdminModelExtension
from zmei_generator.domain.extensions import ApplicationExtension


class SuitAppExtension(ApplicationExtension):

    def __init__(self, application):
        super().__init__(application)

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

        for app, application in apps.items():
            if application.supports(SuitAppExtension) and application[SuitAppExtension].menu:
                menu.extend(application[SuitAppExtension].menu)

            if application.models_support(AdminModelExtension):
                models = []
                for model in application.models.values():
                    if model.supports(AdminModelExtension) and not model.parent:
                        models.append(f'{app}.{model.class_name}', )

                if len(models):
                    menu.append({'label': app, 'models': models})

        # app name

        app_name = None
        for app, application in apps.items():
            if application.supports(SuitAppExtension) and application[SuitAppExtension].menu:
                app_name = application[SuitAppExtension].app_name

        f.write("\nSUIT_CONFIG = {")
        f.write("\n'MENU': ")
        f.write(json.dumps(menu, indent=4))
        f.write(',')

        if app_name:
            f.write("\n'ADMIN_NAME': " + json.dumps(app_name))

        f.write("\n} ")









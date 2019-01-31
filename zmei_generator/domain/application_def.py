from collections import namedtuple

from zmei_generator.domain.extensions import Extendable
from zmei_generator.domain.frozen import FrozenClass
from zmei_generator.generator.imports import ImportSet
from zmei_generator.parser.errors import GlobalScopeValidationError as ValidationException


class ApplicationDef(Extendable, FrozenClass):
    # app_name: str
    # models: Dict[str, ModelDef]

    def __init__(self, app_name: str) -> None:
        super().__init__()

        self.application = None

        self.app_name = app_name

        self.translatable = False

        self.models = {}
        self.pages = {}

        self.page_imports = ImportSet()
        self.model_imports = ImportSet()

        self.deps = []
        self._apps = [app_name]
        self.extensions = []

        self._freeze()
        
    def pages_support(self, extension_cls):
        for page in self.pages.values():
            if page.supports(extension_cls):
                return True
        return False
        
    def pages_with(self, extension_cls):
        return [page for page in self.pages.values() if page.supports(extension_cls)]
        
    def models_support(self, extension_cls):
        for model in self.models.values():
            if model.supports(extension_cls):
                return True
        return False
        
    def models_with(self, extension_cls):
        return [model for model in self.models.values() if model.supports(extension_cls)]
        
    def resolve_page(self, page_name_def):
        if '.' in page_name_def:
            if not self.application:
                raise ValidationException(
                    'Application have no application assigned. Can not resolve reference.')

            app_name, page_name = page_name_def.split('.', maxsplit=2)

            if app_name not in self.application.applications:
                raise ValidationException(
                    f'Unknown application: {app_name}, when trying to resolve model name "{page_name_def}". '
                    f'Available apps are: {",".join(self.application.applications)}')
            try:
                return self.application.applications[app_name].pages[page_name]
            except KeyError:
                raise ValidationException(
                    f'Unknown page: "{page_name}" in app "{app_name}" '
                    f'Available pages are: {",".join(self.application.applications[app_name].pages.keys())}')
        else:
            try:
                return self.pages[page_name_def]
            except KeyError:
                raise ValidationException(
                    f'Unknown page: "{page_name_def}" in app "{self.app_name}" '
                    f'Available pages are: {",".join(self.pages.keys())}')

    def resolve_model(self, model_name_def):
        try:
            if '.' in model_name_def:
                if not self.application:
                    raise ValidationException(
                        'Application have no application assigned. Can not resolve reference.')

                app_name, model_name = model_name_def.split('.', maxsplit=2)

                if app_name not in self.application.applications:
                    raise ValidationException(
                        f'Unknown application: {app_name}, when trying to resolve model name "{model_name_def}". '
                        f'Available apps are: {",".join(self.application.applications)}')

                return self.application.applications[app_name].models[
                    model_name]
            else:
                return self.models[model_name_def]
        except KeyError:
            raise ValidationException('Reference to unknown model: #{}'.format(model_name_def))
        

    def add_deps(self, deps):
        for dep in deps:
            if dep not in self.deps:
                self.deps.append(dep)

    def add_apps(self, apps):
        for app in apps:
            if app not in self._apps:
                self._apps.append(app)

    @property
    def has_sitemap(self):
        for key, page in self.pages.items():
            if page.has_sitemap:
                return True

        return False

    @property
    def apps(self):
        app_names = self._apps
        return app_names

    def page_list(self):
        return list(self.pages.values())

    def post_process(self):
        for col in self.models.values():
            col.post_process()

    def post_process_extensions(self):
        for extension in self.extensions:
            extension.post_process()

    def get_required_apps(self):
        all_apps = []
        for col in self.models.values():
            all_apps.extend(col.get_required_apps())

        for extension in self.extensions:
            all_apps.extend(extension.get_required_apps())

        return list(set(all_apps))

    def get_required_deps(self):
        all_deps = []
        for col in self.models.values():
            all_deps.extend(col.get_required_deps())

        for extension in self.extensions:
            all_deps.extend(extension.get_required_deps())
        return list(set(all_deps))

    def get_required_urls(self):
        all_urls = []
        for col in self.models.values():
            all_urls.extend(col.get_required_urls())

        for extension in self.extensions:
            all_urls.extend(extension.get_required_urls())
        return all_urls

    def get_required_settings(self):
        all_settings = {}
        for col in self.models.values():
            all_settings.update(col.get_required_settings())

        for extension in self.extensions:
            all_settings.update(extension.get_required_settings())
        return all_settings


FieldDeclaration = namedtuple('FieldDeclaration', ['import_def', 'declaration'])



from collections import namedtuple

from zmei_generator.generator.imports import ImportSet


class CollectionSetDef(object):
    # app_name: str
    # collections: Dict[str, CollectionDef]

    def __init__(self, app_name: str) -> None:

        # self.parser = parser
        self.app_name = app_name
        self.translatable = False

        self.api = False
        self.rest = False
        self.channels = False
        self.crud = False
        self.suit = False
        self.filer = False
        self.langs = False
        self.admin = False
        self.react = False
        self.collections = {}
        self.pages = {}
        self.react_deps = {}
        self.react_imports = ImportSet()
        self.page_imports = ImportSet()
        self.model_imports = ImportSet()

        self.deps = []
        self._apps = [app_name]
        self.extras = []

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
        for col in self.collections.values():
            col.post_process()

    def post_process_extras(self):
        for extra in self.extras:
            extra.post_process()

    def get_required_apps(self):
        all_apps = []
        for col in self.collections.values():
            all_apps.extend(col.get_required_apps())

        for extra in self.extras:
            all_apps.extend(extra.get_required_apps())

        return list(set(all_apps))

    def get_required_deps(self):
        all_deps = []
        for col in self.collections.values():
            all_deps.extend(col.get_required_deps())

        for extra in self.extras:
            all_deps.extend(extra.get_required_deps())
        return list(set(all_deps))

    def get_required_urls(self):
        all_urls = []
        for col in self.collections.values():
            all_urls.extend(col.get_required_urls())

        for extra in self.extras:
            all_urls.extend(extra.get_required_urls())
        return all_urls

    def get_required_settings(self):
        all_settings = {}
        for col in self.collections.values():
            all_settings.update(col.get_required_settings())

        for extra in self.extras:
            all_settings.update(extra.get_required_settings())
        return all_settings


FieldDeclaration = namedtuple('FieldDeclaration', ['import_def', 'declaration'])



from cPyparsing import ParseException
from collections import namedtuple

from zmei_generator.config.domain.collection_def import CollectionDef
from zmei_generator.config.domain.exceptions import ValidationException
from zmei_generator.config.domain.page_def import PageDef
from zmei_generator.config.grammar import page as page_parser
from zmei_generator.generator.imports import ImportSet
from zmei_generator.generator.utils import handle_parse_exception


class CollectionSetDef(object):
    # app_name: str
    # collections: Dict[str, CollectionDef]


    # translatable: False

    def __init__(self, app_name: str) -> None:

        # self.parser = parser
        self.app_name = app_name
        self.translatable = False

        self.api = False
        self.rest = False
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

        self.deps = []
        self._apps = [app_name]

        # self.page_imports = parse_result.page_imports
        # self.collection_imports = parse_result.collection_imports

        # extras = self.parser.get_collection_extras_available()
        self.extras = []

        # TODO: parse collection_extras
        # for extra in parse_result.col_extras:
        #
        #     try:
        #         extra_cls = extras[extra.extra_name]
        #         try:
        #             extra_instance = extra_cls(extra, self)
        #             self.extras.append(extra_instance)
        #
        #         except ParseException as e:
        #             handle_parse_exception(e, extra.extra_body,
        #                                    '@{} expression for collections set "{}"'.format(extra.extra_name, self.app_name))
        #     except KeyError as e:
        #         raise ValidationException('CollectionSet extra not found: {}, reason: {}'.format(extra.extra_name, e))

        # TODO: collection_list by ref
        # for col in parse_result.collections:
        #     collection_def = CollectionDef(col, self)
        #     self.collections[collection_def.ref] = collection_def

        # TODO: collect and process pages
        # for page in parse_result.pages:
        #     page_def = PageDef(page, self)
        #     if page.page_name not in self.pages:
        #         self.pages[page.page_name] = page_def
        #     else:
        #         if page_def.allow_merge:
        #             page_def.merge(self.pages[page.page_name])
        #             self.pages[page.page_name] = page_def
        #         else:
        #             raise ValidationException(f'Can not add page "{page.page_name}" one more time. '
        #                                   f'Page with same name is already added and it do not allow merge.')
        #
        #     for subpage_raw in page_def.children:
        #         try:
        #             subpage_parsed = page_parser.parseString(subpage_raw, parseAll=True)[0]
        #         except ParseException as e:
        #             handle_parse_exception(e, subpage_raw,
        #                                    'Page {} auto-generated subpages: {}'.format(page.page_name, e))
        #
        #         if subpage_parsed.page_name not in self.pages:
        #             self.pages[subpage_parsed.page_name] = PageDef(subpage_parsed, self)
        #         else:
        #             raise ValidationException(f'Can not add page "{subpage_parsed.page_name}" one more time. '
        #                                       f'Page with same name is already added.')

        # TODO: pages post process
        # for page in self.pages.values():
        #     for extra in page.extras:
        #         extra.post_process()

        # TODO: parse collection options
        # for col_name, collection in self.collections.items():
        #     for field_name, field in list(collection.fields.items()):
        #         try:
        #             field.parse_options()
        #         except ParseException as e:
        #             handle_parse_exception(e, field.options,
        #                                    'Options for "{}"->"{}": {}'.format(col_name, field_name, e))

        # TODO: parse collection extras
        # for col_name, collection in self.collections.items():
        #     collection.parse_extras()

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



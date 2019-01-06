import os
import re
from functools import lru_cache
from textwrap import dedent

from zmei_generator.parser.errors import GlobalScopeValidationError as ValidationException


class PageFunction(object):

    def __init__(self) -> None:
        super().__init__()

        self.name = None
        self.args = None
        self.out_args = None
        self.body = None

    def render_python_args(self, out=False):
        return ', '.join(self.args if not out else self.out_args)

    @property
    def python_name(self):
        return f'_remote__{self.name}'


class PageDef(object):
    def __init__(self, collection_set, override=False) -> None:
        super().__init__()

        self.override = override

        # self.raw_ = parse_result
        self._parent = None

        """:type: CollectionSetDef"""
        self.collection_set = collection_set

        self.rss = None
        self.auth = False

        self.extra_bases = ['ZmeiDataViewMixin']

        self.template = True
        self.name = None
        self.extend_name = False
        self.parent_name = None
        self.parsed_template_name = None
        self.parsed_template_expr = None

        self.page_code = None
        self.functions = None  # TODO: [PageFunction(x) for x in parse_result.functions]

        self.allow_merge = False

        # error handler for:
        self.handlers = []

        self.allow_post = False

        if self.parent_name and self.parent_name not in self.collection_set.pages:
            raise ValidationException('Parent "{}" for page "{}" does not exist'.format(self.parent_name, self.name))

        self.uri_params = []

        self.children = []

        self.imports = []

        self.options = {}
        self.methods = {}
        self.menus = {}
        self.blocks = {}
        self.cruds = {}
        self.react_components = {}
        self.page_component_name = None
        self.react_pages = {}
        self.functions = {}
        self.template_libs = []
        self.crud_views = {}

        self.themed_files = {}

        self._flutter = False

        self.react = False
        self.react_client = False
        self.react_server = False

        self.stream = False

        self.defined_url_alias = None

        self._uri = None
        self.defined_uri = None
        self.has_uri = False

        self._i18n = False

        self.crud_overrides = {}

        self.page_items = {}
        # extras = self.collection_set.parser.get_page_extras_available()

        self.extras = []

    def set_html(self, html, react=None, area='content'):
        from zmei_generator.extras.page.block import ReactPageBlock

        if react:
            self.react = react
            if react == '@react_client':
                self.react_client = True
            elif react == '@react_server':
                self.react_server = True
            else:
                self.react_client = True
                self.react_server = True

        self.add_block(area, ReactPageBlock(self, html, area_name=area))

        if self.react:
            if 'ZmeiDataViewMixin' in self.extra_bases:
                self.extra_bases.remove('ZmeiDataViewMixin')

            self.extra_bases.append('ZmeiReactViewMixin')

    def add_crud(self, descriptor, cls):
        if descriptor in self.crud_views:
            raise ValidationException('Two or more @crud annotations with same descriptor are not allowed.')
        self.crud_views[descriptor] = cls

    def add_block(self, area, block):
        if area not in self.blocks:
            self.blocks[area] = []

        self.blocks[area].append(block)

    def get_extra_bases(self):
        parent = self.get_parent()

        if parent:
            if 'ZmeiDataViewMixin' in self.extra_bases:
                self.extra_bases.remove('ZmeiDataViewMixin')

        if len(self.functions) and not self.react:
            if parent:
                if 'ZmeiDataViewMixin' in parent.extra_bases:
                    parent.extra_bases.remove('ZmeiDataViewMixin')

                if 'ZmeiRemoteInvocationViewMixin' not in parent.extra_bases:
                    parent.extra_bases.append('ZmeiRemoteInvocationViewMixin')
            else:
                if 'ZmeiDataViewMixin' in self.extra_bases:
                    self.extra_bases.remove('ZmeiDataViewMixin')

                if 'ZmeiRemoteInvocationViewMixin' not in self.extra_bases:
                    self.extra_bases.append('ZmeiRemoteInvocationViewMixin')

        if not parent:
            return self.extra_bases

        all_bases = self.get_parent().get_all_bases()

        return [x for x in self.extra_bases if x not in all_bases]

    def get_all_bases(self):
        bases = self.extra_bases.copy()
        if self.parent_name:
            bases += self.get_parent().get_all_bases()
        return bases

    def get_parent(self):
        if self.parent_name:
            if not self._parent:
                self._parent = self.collection_set.resolve_page(self.parent_name)

            return self._parent

    def merge(self, page):
        for area, blocks in page.blocks.items():
            if area in self.blocks:
                self.blocks[area] = blocks + self.blocks[area]
            else:
                self.blocks[area] = blocks

    def _find_params(self, match):
        param = match.group(1)
        expr = match.group(3) or '[^\/]+'

        self.uri_params.append(param)
        return '(?P<{}>{})'.format(param, expr)

    @property
    def i18n(self):
        if self._i18n:
            return True

        parent = self.get_parent()

        if parent:
            return parent.i18n

        return False

    @property
    def uri(self):
        _uri = self._uri

        if not _uri:
            return

        if _uri.startswith('.'):
            _uri = _uri[1:]
            parent = self.get_parent()

            if parent:
                if parent.uri:
                    _uri = '/'.join([parent.uri, _uri])
                    _uri = re.sub('/+', '/', _uri)

        return _uri

    def set_uri(self, uri):

        self.defined_uri = uri
        self.has_uri = bool(uri)

        if uri:
            if uri.startswith('$'):
                uri = uri[1:]
                self._i18n = True

            self._uri = re.sub(r'<(\w+)(\s*:\s*([^\>]+))?>', self._find_params, uri)

    def get_parent_flutter(self):
        if self._flutter and self.flutter.include_child:
            return self._flutter

        if self.get_parent():
            return self.get_parent().get_parent_flutter()

    @property
    @lru_cache(maxsize=1)
    def flutter(self):
        if self._flutter:
            return self._flutter

        if self.get_parent():
            return self.get_parent().get_parent_flutter()

    @property
    def react_component_names(self):
        return list(self.react_pages.keys())

    @property
    def page_item_names_with_parents(self):
        names = self.page_item_names
        parent = self.get_parent()
        if parent:
            names += parent.page_item_names_with_parents
        return set(names)

    @property
    def own_item_names(self):
        names = []
        for key in self.page_items.keys():
            if key.startswith('_'):
                key = key[1:]
            names.append(key)
        return list(names)

    @property
    def url_alias(self):
        return self.defined_url_alias or self.name

    @property
    def page_item_names(self):
        return self.own_item_names

    @property
    def parent_view_name(self):
        if not self.parent_name:
            return 'TemplateView'

        return self.collection_set.resolve_page(self.parent_name).view_name

    def get_imports(self):
        imports = self.imports

        if self.react:
            imports.append(('django.conf', 'settings'))
            imports.append(('zmei.react', 'ZmeiReactServer'))
            imports.append(('zmei.react', 'ZmeiReactViewMixin'))

        elif len(self.functions) or self._flutter:
            imports.append(('zmei.views', 'ZmeiRemoteInvocationViewMixin'))

        imports.append(('zmei.views', 'ZmeiDataViewMixin'))

        parent = self.get_parent()
        if parent and parent.collection_set != self.collection_set:
            imports.append((f'{parent.collection_set.app_name}.views', parent.view_name))

        return imports

    @property
    def has_functions(self):
        if len(self.functions):
            return True

        if self.get_parent():
            return self.get_parent().has_functions

        return False

    @property
    def has_streams(self):
        if self.stream:
            return True

        if self.get_parent():
            return self.get_parent().has_streams

        return False

    @property
    def streaming_page(self):
        if self.stream:
            return self

        if self.get_parent():
            return self.get_parent().streaming_page

        return None

    @property
    def has_data(self):
        return len(self.page_item_names_with_parents)

    @property
    def has_sitemap(self):
        return self.sitemap_expr is not None

    @property
    def view_name(self):
        return '{}{}View'.format(
            ''.join([x.capitalize() for x in self.collection_set.app_name.split('_')]),
            ''.join([x.capitalize() for x in self.name.split('_')])
        )

    @property
    def urls_line(self):
        _uri = self.uri

        uri = _uri[1:] if _uri.startswith('/') else _uri
        return '^{}$'.format(uri)

    def render_method_headers(self, use_data=False, use_parent=False, use_url=False, use_request=False):
        code = ""
        if use_data or use_parent:
            code += "data = self._get_data()\n"
        if use_parent:
            code += "parent = type('parent', (object,), data)\n"
        if use_request:
            code += "request = self.request\n"
        if use_url:
            code += "url = type('url', (object,), self.kwargs)\n"

        if len(code) > 0:
            code += "\n"

        return code

    def render_page_code(self):

        code = ""

        for key, item in self.page_items.items():
            indent = 0
            inherited = False
            # private variables
            if key.startswith('_'):
                key = key[1:]
                indent = 4
                inherited = True
                code += "if not inherited:\n"

            if not item.or_404:
                code += " " * indent + key + " = " + item.render_python_code() + "\n"
            else:
                code += " " * indent + "try:\n"
                code += " " * indent + "   " + key + " = " + item.render_python_code() + "\n"
                code += " " * indent + "except ObjectDoesNotExist:\n"
                code += " " * indent + "   raise Http404\n"
            if inherited:
                code += "else:\n"
                code += " " * indent + key + " = None\n"

        code += self.page_code or ''

        code = self.render_method_headers(
            use_data=False,
            use_parent=False,
            use_request=False,
            use_url=False,
        ) + code

        if len(code.strip()) == 0:
            return ''

        return code

    @property
    def defined_template_name(self):
        """
        Returns name of template if it is not an expression
        """
        if self.parsed_template_expr:
            return None
        elif self.parsed_template_name:
            return '{}'.format(self.parsed_template_name)
        else:
            return '{}/{}.html'.format(self.collection_set.app_name, self.name)

    def render_template_name_expr(self):
        if not self.template:
            return ''

        if not self.parsed_template_expr:
            return 'template_name = "{tpl}"'.format(tpl=self.defined_template_name)

        code = self.parsed_template_expr
        code = "def get_template_names(self):\n" + self.render_method_headers(
            use_data='data.' in code,
            use_parent=False,
            use_request='request.' in code,
            use_url='url' in code,
        ) + 'return [' + code + ']\n'

        return code

    def render_method_expr(self, method_code):
        code = method_code

        code = self.render_method_headers(
            use_data='data.' in code,
            use_parent=False,
            use_request='request.' in code,
            use_url='url.' in code,
        ) + code + '\n'

        return code

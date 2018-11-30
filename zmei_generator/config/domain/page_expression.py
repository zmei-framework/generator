import re

from termcolor import colored

from zmei_generator.parser.errors import GlobalScopeValidationError as ValidationException


class PageExpression(object):
    def __init__(self, key, expression, page) -> None:
        self.expression = expression
        self.page = page
        self.key = key

        self.or_404 = False

        self.cache_type = None
        self.cache_expr = None

        self.serialize = False

        if '@cached_as' in self.expression:
            self.cache_type = 'cached_as'
        elif '@cached' in self.expression:
            self.cache_type = 'cached'

        if self.cache_type:
            self.expression, self.cache_expr = self.expression.split('@' + self.cache_type)

            self.expression = self.expression.strip()
            self.cache_expr = self.cache_expr.strip()

            if self.cache_expr == '':
                self.cache_expr = '()'

            if not (self.cache_expr.startswith('(') and self.cache_expr.endswith(')')):
                raise ValidationException('Cache expression must be surrounded with () in expression: {}, parsed cache expr: {}'.format(
                    expression,
                    self.cache_expr
                ))

            self.expression = '{me.cache_type}{me.cache_expr}(lambda: {me.expression})'.format(me=self)

        if '@or_404' in self.expression:
            self.expression = self.expression.replace('@or_404', '')
            self.or_404 = True

        # @rest.xxx
        m = re.search('@rest(\.([_a-zA-Z0-9]+))?', self.expression)
        if m:
            self.expression = self.expression.replace(m.group(0), '')
            self.serialize = True
            descriptor = m.group(2)

            if descriptor:
                self.expression = f'serialize({self.expression}, "{descriptor}")'
            else:
                self.expression = f'serialize({self.expression})'


    def find_collection_by_ref(self, ref):
        try:
            return self.page.collection_set.collections[ref]
        except KeyError:
            raise ValidationException(
                'Can not parese page expression. Collection not found by ref: {} when parsing page: {}\n\n'
                '[..{}..]\n...\n{}: {}\n'.format(
                    '#' + ref,
                    self.page.name,
                    self.page.name,
                    self.key,
                    self.expression.replace('#' + ref, colored('#' + ref, 'white', 'on_red'))
                ))

    def get_imports(self):
        imports = []
        for match in re.findall(r'#(\w+)\.', self.expression):
            col = self.find_collection_by_ref(match)
            imports.append(('{}.models'.format(col.collection_set.app_name), col.class_name))

        if self.or_404:
            imports.append(('django.core.exceptions', 'ObjectDoesNotExist'))
            imports.append(('django.http', 'Http404'))

        if self.cache_type:
            imports.append(('cacheops', self.cache_type))

        if 'get_language(' in self.expression:
            imports.append(('django.utils.translation', 'get_language'))

        if 'thumb(' in self.expression:
            imports.append(('cratis_filer.utils', 'thumb'))

        if self.serialize:
            imports.append(('zmei.serializer', 'serialize'))

        return imports

    def render_python_code(self):
        def replace_col_names(match):
            return '{}.objects.'.format(self.find_collection_by_ref(match.group(1)).class_name)

        expr = self.expression.strip()
        expr = re.sub(r'#(\w+)\.', replace_col_names, expr)

        def replace_params(match):
            param = match.group(1)

            if param not in self.page.uri_params:
                raise ValidationException(
                    'Can not parese page expression. Parameter not found: #{}'.format(param))

            return "self.kwargs['{}']".format(param)

        expr = re.sub(r'<(\w+)>', replace_params, expr)


        return expr



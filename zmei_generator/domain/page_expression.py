import re

from termcolor import colored

from zmei_generator.domain.extensions import Extendable
from zmei_generator.parser.errors import GlobalScopeValidationError as ValidationException


class PageExpression(Extendable):
    def __init__(self, key, expression, page) -> None:
        super().__init__()
        self.expression = expression
        self.page = page
        self.key = key

        self.or_404 = False

        self.cache_type = None
        self.cache_expr = None

        self.serialize = False

        self.model_name = None
        self.model_descriptor = None
        self.model_many = None
        self.model_dict = None

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
            self.model_descriptor = m.group(2)

            self.or_404 = True

        # @rest.xxx
        m = re.search('#([_a-zA-Z0-9_]+(\.[_a-zA-Z0-9_]+)?)(\[\]|\{\})?\s*$', self.expression)
        if m:
            self.expression = self.expression.replace(m.group(0), '')

            self.model_name = m.group(1)
            self.model_many = m.group(3) == '[]'
            self.model_dict = m.group(3) == '{}'

        if self.serialize:
            if self.model_descriptor:
                self.expression = f'serialize({self.expression}, "{self.model_descriptor}")'
            else:
                self.expression = f'serialize({self.expression})'


    def get_annotation_with_braces(self, annot):
        exp = self.expression
        try:
            idx = exp.index(annot)
        except ValueError:
            return

        if not idx:  # if it's in 0 position we also don't care
            return

        try:
            if exp[idx + len(annot)] != '(':
                return
        except IndexError:
            pass

        new_exp = exp[:idx]


        pos = 0
        braces_level = 1
        start_pos = idx + len(annot) + 1
        for char in exp[start_pos:]:
            if char == ')':
                braces_level -= 1
            if char == '(':
                braces_level += 1

            pos += 1

            if braces_level == 0:
                new_exp += exp[idx + start_pos + pos:]
                break

        if braces_level > 0:
            return

        exp_inside = self.expression[start_pos: start_pos + pos -1]

        self.expression = new_exp.strip()

        return exp_inside


    def find_model_by_ref(self, ref):
        try:
            return self.page.application.models[ref]
        except KeyError:
            raise ValidationException(
                'Can not parese page expression. Model not found by ref: {} when parsing page: {}\n\n'
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
            col = self.find_model_by_ref(match)
            imports.append(('{}.models'.format(col.application.app_name), col.class_name))

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
            return '{}.objects.'.format(self.find_model_by_ref(match.group(1)).class_name)

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



import re


from cratis_generator.config.domain.page_extra import PageExtra
from cratis_generator.config.domain.page_expression import PageExpression
from cratis_generator.config.domain.exceptions import ValidationException

from cPyparsing import *

from cratis_generator.config.grammar import identifier

url_expression = Group((Literal('url') | Literal('page') | Literal('reverse')).setResultsName('type') + \
                       QuotedString('(', endQuoteChar=')').setResultsName('expression')).setResultsName('target')

arg = Group(identifier.setResultsName('key') + Suppress('=') + quotedString('"').setResultsName('val'))
args = ZeroOrMore(arg).setResultsName('args')

menu_item = Group(identifier.setResultsName('ref') + Suppress('=>') + \
            (Word(alphanums) | QuotedString('"') | QuotedString("'")).setResultsName('label') + \
            Suppress(':') + url_expression + args)

parser = OneOrMore(menu_item).setResultsName('items').ignore(cStyleComment)


class MenuPageExtra(PageExtra):
    @classmethod
    def get_name(cls):
        return 'menu'

    def __init__(self, parsed_result, page):
        super().__init__(parsed_result, page)

        self.menu_name = parsed_result.descriptor or 'main'

        self.items = parser.parseString(parsed_result.extra_body, parseAll=True)

        page.imports.append(
            ('django.urls', 'reverse_lazy')
        )

        self.page_refs = []

    def render_url(self, item):
        if item.target.type == 'page':
            ref = item.target.expression
            if not re.match('^[a-z0-9_]+$', ref):
                raise ValidationException(f'Invalid page reference: "#{ref}" when parsing menu '
                                          f'extra "{self.menu_name}" item "{item.ref}" for page {self.page}')

            try:
                page = self.page.collection_set.pages[ref]
            except KeyError:
                raise ValidationException(f'Invalid page reference, page do not exist: "#{ref}" when parsing menu '
                                          f'extra "{self.menu_name}" item "{item.ref}" for page {self.page}')

            self.page_refs.append(
                (ref, item.ref, page)
            )

            return f"reverse_lazy('{page.collection_set.app_name}.{page.name}')"
        elif item.target.type == 'url':
            return item.target.expression
        else:
            return f"reverse_lazy({item.target.expression})"

    def post_process(self):

        menu_code = self.page.page_code or '\n'
        menu_code += f"data.menu_{self.menu_name} = {{\n"
        for item in self.items:

            if item.args:
                args = ', ' + ', '.join([f"'{x.key}': {x.val}" for x in item.args])
            else:
                args = ''
            menu_code += f"'{item.ref}': {{'label': _({repr(item.label)}), 'link': {self.render_url(item)}{args} }},\n"
        menu_code += "}\n"
        self.page.page_code = menu_code

        for page_ref, item_ref, page in self.page_refs:
            page.methods[f'activate_{self.menu_name}_menu'] = f"self.get_data().menu_{self.menu_name}['{item_ref}']['active'] = True\n"

            code = page.page_code or '\n'
            code += f'self.activate_{self.menu_name}_menu()\n'

            page.page_code = code

from cratis_generator.config.domain.page_extra import PageExtra

from cPyparsing import *

from cratis_generator.config.grammar import class_name, identifier

parser = class_name.setResultsName('cls')


class FormExtra(PageExtra):

    @classmethod
    def get_name(cls):
        return 'form'

    def __init__(self, parsed_result, page):
        super().__init__(parsed_result, page)

        self.var_name = parsed_result.descriptor or 'form'
        parsed = parser.parseString(parsed_result.extra_body, parseAll=True)

        parts = parsed.cls.split('.')
        cls_from = '.'.join(parts[:-1])
        cls_name = parts[-1]

        page.imports.append(
            ('django.views.generic.edit', 'FormView'),
        )

        page.imports.append(
            (cls_from, cls_name),
        )

        page.extra_bases.append('FormView')
        page.options['form_class'] = cls_name





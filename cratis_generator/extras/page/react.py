import re

from pyparsing import *

from cratis_generator.config.domain import PageExtra

identifier = Word(alphas, alphanums + '_')
package_name = Word(alphanums + '_@/-')
import_from = Word(alphanums + '_@/-')

use_expr = Group(Suppress('use(') + \
           Optional(Suppress('[') + package_name.setResultsName('package_name') + Suppress(']')) + \
           import_from.setResultsName('import_from') + \
           Suppress(':') + Group(delimitedList(identifier)).setResultsName('components') + Suppress(')'))

react_extra_parser = Group(ZeroOrMore(use_expr)).setResultsName('use') + SkipTo(StringEnd()).setResultsName('source')


class ReactPageExtra(PageExtra):

    @classmethod
    def get_name(cls):
        return 'react'

    def __init__(self, parsed_result, page):
        super().__init__(parsed_result, page)

        # area_name = parsed_result.descriptor or 'content'

        parsed_body = react_extra_parser.parseString(parsed_result.extra_body)

        print('***' * 10)
        print('React')
        print('***' * 10)
        for use in parsed_body.use:
            print(f'Install: {use.package_name} From {use.import_from} import {use.components}')
        print('***' * 10)
        print(parsed_body.source)
        print('***' * 10)


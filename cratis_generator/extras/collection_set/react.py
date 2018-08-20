import re

from cPyparsing import *

from cratis_generator.config.domain import CollectionSetExtra

identifier = Word(alphas + '*', alphanums + '_')
package_name = Word(alphanums + '_@/-')
import_from = Word(alphanums + '_@/-')

use_expr = Group(Suppress('use(') +
                 import_from.setResultsName('import_from') +
                 Suppress(':') + Group(delimitedList(identifier)).setResultsName('components') + Suppress(')'))

install_expr = Group(Suppress('install(') +
           import_from.setResultsName('package_name') +
           Suppress(':') + Word(alphanums + '.@~-_').setResultsName('version') + Suppress(')'))

react_extra_parser = Group(ZeroOrMore(install_expr)).setResultsName('install') + \
                     Group(ZeroOrMore(use_expr)).setResultsName('use') + StringEnd()


class ReactCollectionSetExtra(CollectionSetExtra):

    @classmethod
    def get_name(cls):
        return 'react'

    def __init__(self, parsed_result, collection_set):
        super().__init__(parsed_result, collection_set)

        parsed_body = react_extra_parser.parseString(parsed_result.extra_body)

        for install in parsed_body.install:
            collection_set.react_deps[install.package_name] = install.version

        for use in parsed_body.use:
            collection_set.react_imports.add(use.import_from, *use.components)



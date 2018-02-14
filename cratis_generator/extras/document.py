from cratis_generator.config.domain import CollectionDef
from cratis_generator.config.extras import Extra
from pyparsing import *


class DocumentExtra(Extra):

    @classmethod
    def get_name(cls):
        return 'document'

    def get_parser(self):

        identifier = Word(alphas, alphanums + '_')

        name = Suppress('name') + Suppress(':') + QuotedString('"').setResultsName('name')
        template = Suppress('template') + Suppress(':') + QuotedString('"').setResultsName('template')

        key_val = Group(identifier.setResultsName('key') + Suppress(':') + QuotedString('"').setResultsName('val'))
        data = Suppress('data') + Suppress(':') + Suppress('{') + ZeroOrMore(key_val) + Suppress('}')

        document = identifier + Suppress('(') + name + Suppress(',') + template + Suppress(',') + data + Suppress(')')

        return stringStart + delimitedList(document, ',').setResultsName('documents') + stringEnd

    def parse(self, extra, collection: CollectionDef):

        print('***' * 10)
        print('Document')
        print('***' * 10)
        parsed_body = self.get_parser().parseString(extra.extra_body)
        print(parsed_body)


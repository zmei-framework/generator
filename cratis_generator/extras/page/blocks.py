from cratis_generator.config.domain import PageExtra
from pyparsing import *

from cratis_generator.config.grammar import identifier

val = QuotedString('"') | Word(alphanums + '_')
field = Group(identifier.setResultsName('key') + Suppress('=') + Optional(val.setResultsName('value')))

block_expr = identifier.setResultsName('name') + Optional(Suppress('<') + delimitedList(field).setResultsName('fields') + Suppress('>'))
parser = delimitedList(Group(block_expr)).setResultsName('blocks').ignore(cStyleComment)

class PageBlock(object):
    def __init__(self, name, fields=None) -> None:
        super().__init__()
        self.name = name
        self.fields = fields or {}

    @property
    def template_name(self):
        return 'theme/{}.html'.format(self.name)


class BlocksPageExtra(PageExtra):

    @classmethod
    def get_name(cls):
        return 'blocks'

    def __init__(self, parsed_result, page):
        super().__init__(parsed_result, page)

        area_name = parsed_result.descriptor or 'content'

        blocks = []
        for block in parser.parseString(parsed_result.extra_body, parseAll=True).blocks:
            fields = {}
            if block.fields:
                for field in block.fields:
                    fields[field.key] = field.value
            blocks.append(PageBlock(name=block.name, fields=fields))

        if not area_name in page.blocks:
            page.blocks[area_name] = blocks
        else:
            page.blocks[area_name] = page.blocks[area_name] + blocks



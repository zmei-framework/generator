from cratis_generator.config.domain import PageExtra
from pyparsing import *

from cratis_generator.config.grammar import identifier

parser = delimitedList(identifier | Literal('..'))

class PageBlock(object):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

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
        for block_name in parser.parseString(parsed_result.extra_body):
            blocks.append(PageBlock(name=block_name))

        page.blocks[area_name] = blocks




from xml.etree import ElementTree

from cratis_generator.config.domain import PageExtra
from pyparsing import *

from cratis_generator.config.grammar import identifier

# val = QuotedString('"') | Word(alphanums + '_')
# field = Group(identifier.setResultsName('key') + Suppress('=') + Optional(val.setResultsName('value')))
#
# block_expr = identifier.setResultsName('name') + Optional(Suppress('<') + delimitedList(field).setResultsName('fields') + Suppress('>'))
# parser = delimitedList(Group(block_expr)).setResultsName('blocks').ignore(cStyleComment)


class PageBlock(object):
    def __init__(self, theme=None, root_el=None, fields=None, source=None) -> None:
        super().__init__()
        self.theme = theme or 'default'
        self.root_el = root_el or 'block'
        self.fields = fields or {}
        self.source = source

    def render(self):
        if self.source:
            source = self.source
        else:
            el = ElementTree.Element(self.root_el, attrib={key: str(val) for key,val in self.fields.items()})
            source = ElementTree.tostring(el).decode()

        return f'\n<genius:blocks theme="{self.theme}">\n    {source}\n</genius:blocks>'


class BlocksPageExtra(PageExtra):

    @classmethod
    def get_name(cls):
        return 'block'

    def __init__(self, parsed_result, page):
        super().__init__(parsed_result, page)

        area_name = parsed_result.descriptor or 'content'

        blocks = [PageBlock(source=parsed_result.extra_body)]

        if area_name not in page.blocks:
            page.blocks[area_name] = blocks
        else:
            page.blocks[area_name] = page.blocks[area_name] + blocks



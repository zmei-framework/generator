import re
from xml.etree import ElementTree

from cratis_generator.config.domain.page_extra import PageExtra
from defusedxml.ElementTree import fromstring, tostring

from cratis_generator.generator.imports import ImportSet


class ReactPageBlock(object):
    def __init__(self, page=None, source=None) -> None:
        super().__init__()

        self.source = source or ''
        self.page = page
        self.react_components = {}
        self.react_components_imports = ImportSet()


        # make react's <foo messages={} /> => <foo messages="" /> to allow xml parsing.
        xml_safe_source = self.source.replace('{', '"').replace('}', '"')

        xml = fromstring(f'<root>{xml_safe_source}</root>')
        self.collect_components(xml)

        self.xml = xml

        if len(self.react_components) > 0:
            self.page.react = True
            self.page.collection_set.react = True

    def collect_components(self, el):
        if re.match('^[A-Z][a-z0-9]+', el.tag):

            import_source, what = self.page.collection_set.react_imports.find_import_source(el.tag)

            if import_source:
                self.react_components_imports.add(import_source, what)

            else:
                self.react_components_imports.add(f'../Components/{el.tag}', '*' + el.tag)

                imports = ImportSet()
                imports.add('react', 'React')

                self.react_components[el.tag] = (imports, '', '<div>\n    {this.props.children}\n</div>')

        for child in el:
            self.collect_components(child)

    def render(self, area=None, index=None):
        if len(self.xml) > 1:
            source = f'<div>{self.source}</div>'
        else:
            source = self.source

        if len(self.react_components) == 0:
            return self.source  # no react components inside

        cmp_name = f'Page{self.page.name.capitalize()}{area.capitalize()}{index}'

        self.react_components_imports.add('react', 'React')

        body = '\n'.join([f'let {var} = this.props.{var};' for var in self.page.page_item_names_with_parents])
        body = f'\n{body}\n'

        self.page.react_components.update(self.react_components)
        self.page.react_pages.update({cmp_name: (self.react_components_imports, body, source)})

        return '<div id="reactEl-%s">{{ react_page_%s|default:""|safe }}</div>' % (cmp_name, cmp_name)


class PageBlock(object):
    def __init__(self, theme=None, root_el=None, fields=None, source=None) -> None:
        super().__init__()
        self.theme = theme or 'default'
        self.root_el = root_el or 'block'
        self.fields = fields or {}
        self.source = source

    def render(self, area=None, index=None):

        if self.source:
            source = self.source
        else:
            el = ElementTree.Element(self.root_el, attrib={key: str(val) for key, val in self.fields.items()})
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

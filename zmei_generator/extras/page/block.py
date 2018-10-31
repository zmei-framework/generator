import re
from xml.etree import ElementTree

from defusedxml.ElementTree import fromstring, tostring

from zmei_generator.generator.imports import ImportSet
from zmei_generator.generator.utils import render_template, render_file


class ReactPageBlock(object):
    def __init__(self, page=None, source=None, area_name=None) -> None:
        super().__init__()

        self.source = source or ''
        self.area_name = area_name or 'content'
        self.page = page
        self.react_components = {}
        self.react_components_imports = ImportSet()


        # make react's <foo messages={} /> => <foo messages="" /> to allow xml parsing.
        xml_safe_source = self.source.replace('{', '"').replace('}', '"')

        xml = fromstring(f'<root>{xml_safe_source}</root>')
        self.collect_components(xml)

        self.xml = xml

        parent = self.page.get_parent()
        self.is_child_of_react_page = parent and parent.react

        if self.is_child_of_react_page:
            self.parent_component = self.get_parent_react_page(page.get_parent()).page_component_name
        else:
            self.parent_component = None

        if len(self.react_components) > 0 or self.is_child_of_react_page:
            self.page.react = True
            self.page.collection_set.react = True

            self.page.page_component_name = f'Page{self.page.name.capitalize()}{self.area_name.capitalize()}'

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

    def get_parent_react_page(self, page):
        if page.page_component_name:
            return page

        if page.get_parent():
            self.get_parent_react_page(page.get_parent())
        return page

    def render(self, area=None, index=None):
        if area != self.area_name:
            raise AttributeError('This exception shouldn\'t happen and indicates some bug in code')

        if self.parent_component:
            source = f'<{self.parent_component}>\n    {self.source}\n</{self.parent_component}>'
        else:
            if len(self.xml) > 1:
                source = f'<>{self.source}</>'
            else:
                source = self.source

        if len(self.react_components) == 0 and (not self.is_child_of_react_page):
            return self.source  # no react components inside

        self.react_components_imports.add('react', 'React')
        self.react_components_imports.add(f'../Reducers/{self.page.page_component_name}Reducers', f'*reloadPageDataAction')

        if self.parent_component:

            self.react_components_imports.add(f'./{self.parent_component}', f'{{{self.parent_component}}}')

        var_names = ', '.join(self.page.page_item_names_with_parents)
        body = '\nconst {store, dispatch, children} = this.props;' \
               '\nconst {%s} = store;\n\n' % var_names

        self.page.react_components.update(self.react_components)
        self.page.react_pages.update({self.page.page_component_name: (self.react_components_imports, body, source)})

        return '<div id="reactEl-%s">{{ react_page_%s|default:""|safe }}</div>' % (
            self.page.page_component_name,
            self.page.page_component_name
        )


class PageBlock(object):
    def __init__(self, theme=None, root_el=None, fields=None, source=None, area_name=None) -> None:
        super().__init__()
        self.theme = theme or 'default'
        self.root_el = root_el or 'block'
        self.fields = fields or {}
        self.area_name = area_name or 'content'
        self.source = source

    def render(self, area=None, index=None):

        if self.source:
            source = self.source
        else:
            el = ElementTree.Element(self.root_el, attrib={key: str(val) for key, val in self.fields.items()})
            source = ElementTree.tostring(el).decode()

        return f'\n<genius:blocks theme="{self.theme}">\n    {source}\n</genius:blocks>'


class InlineTemplatePageBlock(object):
    def __init__(self, template_name, context=None) -> None:
        super().__init__()

        self.template_name = template_name
        self.context = context

    def render(self, area=None, index=None):
        return render_template(self.template_name, context=self.context)


class InlineFilePageBlock(object):
    def __init__(self, template_name) -> None:
        super().__init__()

        self.template_name = template_name

    def render(self, area=None, index=None):
        return render_file(self.template_name)


class ThemeFileIncludePageBlock(object):
    def __init__(self, page, source, template_name, ns, theme='default', with_expr=None) -> None:
        super().__init__()

        self.template_name = f'{ns}/{theme}/{template_name}'
        self.theme = theme
        self.page = page
        self.source = source
        self.with_expr = with_expr or ' '

        page.themed_files[self.template_name] = source

    def render(self, area=None, index=None):
        return f"{{% include '{self.template_name}'{self.with_expr} %}}"

#
# class BlocksPageExtra(PageExtra):
#
#     @classmethod
#     def get_name(cls):
#         return 'block'
#
#     def __init__(self, parsed_result, page):
#         super().__init__(parsed_result, page)
#
#         area_name = parsed_result.descriptor or 'content'
#
#         blocks = [PageBlock(source=parsed_result.extra_body, area_name=area_name)]
#
#         if area_name not in page.blocks:
#             page.blocks[area_name] = blocks
#         else:
#             page.blocks[area_name] = page.blocks[area_name] + blocks

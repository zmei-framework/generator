import re
from xml.etree import ElementTree

from defusedxml.ElementTree import fromstring, tostring

from zmei_generator.generator.imports import ImportSet
from zmei_generator.generator.utils import render_template, render_file


class Block(object):
    def __init__(self) -> None:
        super().__init__()

        self.sorting = 0

    def render(self, area=None, index=None):
        pass


class BlockPlaceholder(Block):
    pass


class InlinePageBlock(Block):
    def __init__(self, source) -> None:
        super().__init__()

        self.source = source

    def render(self, area=None, index=None):
        return self.source


class InlineTemplatePageBlock(Block):
    def __init__(self, template_name, context=None) -> None:
        super().__init__()

        self.template_name = template_name
        self.context = context

    def render(self, area=None, index=None):
        return render_template(self.template_name, context=self.context)


class InlineFilePageBlock(Block):
    def __init__(self, template_name) -> None:
        super().__init__()

        self.template_name = template_name

    def render(self, area=None, index=None):
        return render_file(self.template_name)


class ThemeFileIncludePageBlock(Block):
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
# class BlocksPageExtension(PageExtension):
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
#         blocks = [PageBlock(source=parsed_result.extension_body, area_name=area_name)]
#
#         if area_name not in page.blocks:
#             page.blocks[area_name] = blocks
#         else:
#             page.blocks[area_name] = page.blocks[area_name] + blocks

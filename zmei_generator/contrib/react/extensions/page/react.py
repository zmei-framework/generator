from copy import copy

from zmei_generator.contrib.web.extensions.page.block import InlinePageBlock, InlineTemplatePageBlock
from zmei_generator.domain.extensions import PageExtension
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class ReactPageExtension(PageExtension):
    def __init__(self, page) -> None:
        super().__init__(page)

        self.react_type = None
        self.area = None
        self.code = None
        self.include_child = False

    # def get_required_deps(self):
    #     return ['py_mini_racer']

    @property
    def can_inherit(self):
        return self.include_child

    def get_required_apps(self):
        return ['rest_framework']

    def get_required_deps(self):
        return ['djangorestframework']

    def modify_extension_bases(self, bases):
        return super().modify_extension_bases(bases)

    def filter_blocks(self, area, blocks, platform):
        filtered = []

        if platform == ReactPageExtension:
            for block in blocks:
                if isinstance(block, InlineTemplatePageBlock):
                    if block.template_name.startswith('theme/'):
                        new_context = copy(block.context)
                        block = InlineTemplatePageBlock(template_name='react/' + block.template_name, ref=block.ref)
                        block.context = new_context
                else:
                    continue

                filtered.append(block)
        else:
            # other platforms:
            filtered = []
            for block in blocks:
                if isinstance(block, InlineTemplatePageBlock):
                    continue
                filtered.append(block)

        return filtered

    def post_process(self):
        super().post_process()

        # page.react_pages.update({page.page_component_name: (react_components_imports, body, 'lala')})
        reducer_cmp = f'Page{self.page.name.capitalize()}Reducer'
        cmp = f'Page{self.page.name.capitalize()}Component'

        self.page.imports.append(('app.utils.react', 'ZmeiReactViewMixin'))

        self.page.add_block('content', InlinePageBlock(f"""
            <div id="reactEl-{cmp}">{{{{ react_page_{cmp}|default:""|safe }}}}</div>
        """))

        self.page.add_block('css', InlinePageBlock(f"""
            <link media="all" rel="stylesheet" href="/static/react/all.bundle.css" />            
            <!-- <link media="all" rel="stylesheet" href="/static/react/{self.page.application.app_name}.bundle.css" /> -->            
        """))

        self.page.add_block('js', InlinePageBlock(f"""
            <script type="text/javascript" src="/static/react/all.bundle.js"></script>
            <!-- <script type="text/javascript" src="/static/react/{self.page.application.app_name}.bundle.js"></script> -->
            <script>
                R.renderClient(R.{reducer_cmp}, null, {{{{ react_state|safe }}}}, document.getElementById('reactEl-{cmp}'), false);
            </script>
        """))

        if 'ZmeiDataViewMixin' in self.page.extension_bases:
            self.page.extension_bases.remove('ZmeiDataViewMixin')

        self.page.extension_bases.append('ZmeiReactViewMixin')


class ReactPageExtensionParserListener(BaseListener):

    def enterAn_react(self, ctx: ZmeiLangParser.An_reactContext):
        extension = ReactPageExtension(self.page)
        self.application.extensions.append(extension)
        extension.react_type = ctx.an_react_type().getText()

        self.page.register_extension(extension)

    def enterAn_react_child(self, ctx: ZmeiLangParser.An_react_childContext):
        if str(ctx.BOOL()) == 'true':
            self.page[ReactPageExtension].include_child = True

from zmei_generator.domain.application_def import ApplicationDef
from zmei_generator.domain.extensions import PageExtension
from zmei_generator.contrib.web.extensions.page.block import InlineTemplatePageBlock
from zmei_generator.parser.errors import ValidationError
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class MenuPageExtension(PageExtension):

    def __init__(self, page) -> None:
        super().__init__(page)

        self.descriptor = 'main'

        self.items = []

        page.imports.append(
            ('django.urls', 'reverse_lazy')
        )

        self.page_refs = []

    def format_extension_value(self, current_value):
        if not current_value:
            current_value = {}
        descriptor = self.descriptor or '_'

        if descriptor not in current_value:
            current_value[descriptor] = {}

        current_value[descriptor] = self

        return current_value

    def render_ref(self, item):
        if item.page:
            page = self.page.application.resolve_page(item.page)

            if not page.uri:
                raise ValidationError(0, 0, f"You are trying to add page {item.page} to a menu, however page has no url defined.")

            self.page_refs.append(
                (item.page, item.ref, page)
            )

            return f"{page.application.app_name}.{page.name}"

    def render_url(self, item):
        if item.page:
            return f"reverse_lazy('{self.render_ref(item)}')"
        elif item.url:
            return item.url
        else:
            return f"{item.expr}"

    def post_process(self):

        menu_code = self.page.page_code or '\n'
        menu_code += f"if 'menu' not in data:\n    data['menu'] = {{}}\n\n"
        menu_code += f"data['menu']['{self.descriptor}'] = {{\n"
        menu_code += "'active': None,\n"
        menu_code += "'items': {\n"
        for item in self.items:
            if item.args:
                args = ', \'args\': ' + repr(item.args)
            else:
                args = ''
            menu_code += f"'{item.ref}': {{'label': _({repr(item.label)}), 'link': {self.render_url(item)}{args} }},\n"
        menu_code += "}\n"
        menu_code += "}\n"
        self.page.page_code = menu_code

        for page_ref, item_ref, page in self.page_refs:
            page.methods[f'activate_{self.descriptor}_menu'] = \
                f"kwargs['menu']['{self.descriptor}']['items']['{item_ref}']['active'] = True\n" \
                f"kwargs['menu']['{self.descriptor}']['active'] = kwargs['menu']['{self.descriptor}']['items']['{item_ref}']"

            code = page.page_code or '\n'
            code += f"self.activate_{self.descriptor}_menu(menu=data['menu'])\n"

            page.page_code = code

        self.page.add_block(
            f"menu_{self.descriptor}",
            InlineTemplatePageBlock(f"theme/menu[_{self.descriptor}].html", {
                'menu_descriptor': self.descriptor
            }, ref=f"menu_{self.descriptor}")
        )


class MenuItem(object):
    def __init__(self) -> None:
        super().__init__()

        self.ref = None
        self.label = None
        self.url = None
        self.page = None
        self.expr = None
        self.args = {}


class MenuPageExtensionParserListener(BaseListener):
    def __init__(self, application: ApplicationDef) -> None:
        super().__init__(application)

        self.menu = None
        self.menu_item = None

    def enterAn_menu(self, ctx: ZmeiLangParser.An_menuContext):
        self.menu = MenuPageExtension(self.page)

        extension = self.menu
        self.application.extensions.append(
            extension
        )

    def exitAn_menu(self, ctx: ZmeiLangParser.An_menuContext):
        self.page.register_extension(self.menu)

    def enterAn_menu_descriptor(self, ctx: ZmeiLangParser.An_menu_descriptorContext):
        self.menu.descriptor = ctx.getText()

    def enterAn_menu_item(self, ctx: ZmeiLangParser.An_menu_itemContext):
        self.menu_item = MenuItem()
        self.menu_item.ref = f'item_{len(self.menu.items)}'
        self.menu.items.append(self.menu_item)

    def enterAn_menu_label(self, ctx: ZmeiLangParser.An_menu_labelContext):
        self.menu_item.label = ctx.getText().strip('\'"')

    def enterAn_menu_item_url(self, ctx: ZmeiLangParser.An_menu_item_urlContext):
        self.menu_item.url = ctx.getText()

    def enterAn_menu_item_page(self, ctx: ZmeiLangParser.An_menu_item_pageContext):
        self.menu_item.page = ctx.an_menu_item_page_ref().getText()

    def enterAn_menu_item_code(self, ctx: ZmeiLangParser.An_menu_item_codeContext):
        self.menu_item.expr = ctx.code_line().PYTHON_CODE().getText().strip()

    def enterAn_menu_item_arg(self, ctx: ZmeiLangParser.An_menu_item_argContext):
        self.menu_item.args[ctx.an_menu_item_arg_key().getText()] = ctx.an_menu_item_arg_val().getText().strip('\'"')

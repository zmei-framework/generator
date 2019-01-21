from textwrap import dedent

from zmei_generator.config.domain.page_def import PageDef
from zmei_generator.config.domain.page_expression import PageExpression
from zmei_generator.extras.page.block import InlineTemplatePageBlock
from zmei_generator.extras.page.crud import BaseCrudSubpageExtra
from zmei_generator.extras.page.crud_parser import CrudBasePageExtraParserListener
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser


class CrudCreatePageExtra(BaseCrudSubpageExtra):
    @classmethod
    def get_name(cls):
        return 'crud_create'

    @property
    def crud_page(self):
        return 'create'

    def get_form_class(self):
        return 'ModelForm'

    def get_form_name(self):
        return ''.join(
            [x.capitalize() for x in f"{self.model_cls}_{self.name_prefix}{self.get_name()[5:]}".split('_')]) + 'Form'

    def get_form_code(self):
        """
        Form code

        :return:
        """

        fields = self.get_model_fields()

        return dedent(f"""
        prefix = {repr(self.descriptor)}
        class Meta:
            model = {self.model_cls}
            fields = {fields}        
        """)

    def get_model_fields(self):
        return ', '.join([repr(x) for x in self.fields])

    def get_form_init(self):
        return "request.POST if request.method == 'POST' else None"

    def get_form_action(self):
        form_name = f'form{self.name_suffix}'
        return f"""
            if {form_name}.is_valid():
                model = {form_name}.save()
        """

    def build_pages(self, base_page: PageDef):
        base_page.add_crud(self.descriptor, self)

        base_page.imports.append(
            ('django.forms', 'ModelForm')
        )

        base_page.imports.append(
            ('zmei.views', 'RedirectAction')
        )

        # Form requires post
        # we handle post with same method
        base_page.allow_post = True

        # form name contains prefix in case of several forms are here
        form_name = f'form{self.name_suffix}'

        base_page.page_items[form_name] = PageExpression(
            form_name, f"{self.get_form_name()}({self.get_form_init()})", base_page)

        code = f"""
        if request.method == "POST":
            {self.get_form_action()}    
        """
        if self.next_page_expr:
            base_page.imports.append(('zmei.views', 'RedirectAction'))
            code += f"""
                raise RedirectAction({self.next_page_expr})
            """

        base_page.page_code = base_page.page_code or ''
        base_page.page_code += dedent(code)

        base_page.add_form(
            self.get_form_name(),
            self
        )

        base_page.add_block(
            self.block_name,

            InlineTemplatePageBlock(self.get_template_name(), {
                'page': base_page,
                'crud': self,
                'form_name': form_name,
            }),

            sorting=100
        )

    def get_template_name(self):
        return "theme/crud_create.html"


class CrudCreatePageExtraParserListener(CrudBasePageExtraParserListener):

    def enterAn_crud_create(self, ctx: ZmeiLangParser.An_crud_createContext):
        self.extra_start(CrudCreatePageExtra, ctx)

    def exitAn_crud_create(self, ctx: ZmeiLangParser.An_crud_createContext):
        self.extra_end(CrudCreatePageExtra, ctx)


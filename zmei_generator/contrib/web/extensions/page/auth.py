from textwrap import dedent

from zmei_generator.domain.extensions import PageExtension
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class AuthPageExtension(PageExtension):
    def __init__(self, page) -> None:
        super().__init__(page)

        self.is_added = False


class AuthPageExtensionParserListener(BaseListener):

    def enterAn_auth(self, ctx: ZmeiLangParser.An_authContext):
        extension = AuthPageExtension(self.page)
        self.application.extensions.append(
            extension
        )
        expr = None
        if ctx.code_block():
            expr = dedent(ctx.code_block().getText().strip('\n'))

        self.page.register_extension(extension)

        add_page_auth(expr, self.page)


def add_page_auth(auth_expr, page):
    page.imports += [
        ('django.contrib.auth.mixins', 'AccessMixin'),
        ('django.core.exceptions', 'PermissionDenied'),
        ('django.contrib.auth.views', 'redirect_to_login')
    ]

    if need_add_auth(page):
        page.extension_bases.append('AccessMixin')

    page[AuthPageExtension].is_added = True

    code = ""
    code += "if not self.request.user.is_authenticated:\n"
    code += "   return redirect_to_login(self.request.get_full_path(), self.get_login_url(), " \
            "self.get_redirect_field_name())\n"
    if auth_expr:
        code += "elif not ({}):\n".format(auth_expr)
        code += "   raise PermissionDenied(self.get_permission_denied_message())\n"
    code += "return super().dispatch(*args, **kwargs)\n"
    page.methods['dispatch'] = code


def need_add_auth(page):
    if page.supports(AuthPageExtension) and page[AuthPageExtension].is_added:
        return False

    if page.parent_name:
        return need_add_auth(page.get_parent())

    return True


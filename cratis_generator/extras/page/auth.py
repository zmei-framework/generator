from cratis_generator.config.domain.page_extra import PageExtra

class AuthExtra(PageExtra):

    @classmethod
    def get_name(cls):
        return 'auth'

    def __init__(self, parsed_result, page):
        super().__init__(parsed_result, page)

        auth_expr = parsed_result.extra_body.strip()

        add_page_auth(auth_expr, page)


def add_page_auth(auth_expr, page):
    page.imports += [
        ('django.contrib.auth.mixins', 'AccessMixin'),
        ('django.core.exceptions', 'PermissionDenied'),
        ('django.contrib.auth.views', 'redirect_to_login')
    ]

    if need_add_auth(page):
        page.extra_bases.append('AccessMixin')

    page.auth = True

    code = ""
    code += "if not self.request.user.is_authenticated:\n"
    code += "   return redirect_to_login(self.request.get_full_path(), self.get_login_url(), " \
            "self.get_redirect_field_name())\n"
    if auth_expr:
        code += "elif not ({}):\n".format(auth_expr)
        code += "   raise PermissionDenied(self.get_permission_denied_message())\n"
    code += "return super().dispatch(request, *args, **kwargs)\n"
    page.methods['dispatch'] = code


def need_add_auth(page):
    if page.auth:
        return False

    if page.parent_name:
        return need_add_auth(page.get_parent())

    return True





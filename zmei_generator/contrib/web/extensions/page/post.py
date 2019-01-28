from zmei_generator.domain.extensions import PageExtension
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener
from textwrap import indent


class PostPageExtension(PageExtension):
    # post
    pass


class PostPageExtensionParserListener(BaseListener):

    def enterAn_post(self, ctx: ZmeiLangParser.An_postContext):
        self.application.extensions.append(
            PostPageExtension(self.page)
        )

        self.page.allow_post = True

        if not self.page.page_code:
            self.page.page_code = ''

        if ctx.code_block():
            self.page.page_code += '\nif request.method == "POST":\n' + \
                               indent(self._get_code(ctx), ' ' * 4)

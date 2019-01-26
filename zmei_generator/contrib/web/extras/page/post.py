from zmei_generator.domain.extras import PageExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener
from textwrap import indent


class PostPageExtra(PageExtra):
    # post
    pass


class PostPageExtraParserListener(BaseListener):

    def enterAn_post(self, ctx: ZmeiLangParser.An_postContext):
        self.application.extras.append(
            PostPageExtra(self.page)
        )

        self.page.allow_post = True

        if not self.page.page_code:
            self.page.page_code = ''

        if ctx.code_block():
            self.page.page_code += '\nif request.method == "POST":\n' + \
                               indent(self._get_code(ctx), ' ' * 4)

from textwrap import indent

from zmei_generator.config.extras import PageExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

class GetPageExtra(PageExtra):
    # get
    pass
    
class GetPageExtraParserListener(BaseListener):

    def enterAn_get(self, ctx: ZmeiLangParser.An_getContext):
        self.collection_set.extras.append(
            GetPageExtra(self.page)
        )

        if not self.page.page_code:
            self.page.page_code = ''

        if ctx.code_block():
            self.page.page_code += '\nif request.method == "GET":\n' + \
                               indent(self._get_code(ctx), ' ' * 4)


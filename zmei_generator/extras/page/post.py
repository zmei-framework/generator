
from zmei_generator.config.extras import PageExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

class PostPageExtra(PageExtra):
    # post
    pass
    
class PostPageExtraParserListener(BaseListener):

    def enterAn_post(self, ctx: ZmeiLangParser.An_postContext):
        self.collection_set.extras.append(
            PostPageExtra(self.page)
        )

        self.page.allow_post = True


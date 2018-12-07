
from zmei_generator.config.domain.collection_set_extra import CollectionSetExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class FileCsExtra(CollectionSetExtra):
    def get_name(cls):
        return 'file'
    

class FileCsExtraParserListener(BaseListener):

    def enterAn_file(self, ctx: ZmeiLangParser.An_fileContext):
        self.collection_set.extras.append(
            FileCsExtra(self.collection_set)
        )
        file_name = ctx.an_file_name().getText().strip('"')
        source = self._get_code(ctx.python_code())

        self.collection_set.files[file_name] = source



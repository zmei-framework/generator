
from zmei_generator.domain.application_extra import ApplicationExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class FileAppExtra(ApplicationExtra):
    def get_name(cls):
        return 'file'
    

class FileAppExtraParserListener(BaseListener):

    def enterAn_file(self, ctx: ZmeiLangParser.An_fileContext):
        self.application.extras.append(
            FileAppExtra(self.application)
        )
        file_name = ctx.an_file_name().getText().strip('"')
        source = self._get_code(ctx.python_code())

        self.application.files[file_name] = source



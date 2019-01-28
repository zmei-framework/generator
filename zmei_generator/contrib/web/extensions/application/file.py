
from zmei_generator.domain.extensions import ApplicationExtension
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class FileAppExtension(ApplicationExtension):
    def get_name(cls):
        return 'file'
    

class FileAppExtensionParserListener(BaseListener):

    def enterAn_file(self, ctx: ZmeiLangParser.An_fileContext):
        self.application.extensions.append(
            FileAppExtension(self.application)
        )
        file_name = ctx.an_file_name().getText().strip('"')
        source = self._get_code(ctx.python_code())

        self.application.files[file_name] = source



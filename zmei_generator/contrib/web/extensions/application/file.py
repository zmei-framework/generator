from zmei_generator.domain.extensions import ApplicationExtension
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class FileAppExtension(ApplicationExtension):

    def __init__(self, application):
        super().__init__(application)

        self.files = {}

    def get_name(cls):
        return 'file'


class FileAppExtensionParserListener(BaseListener):

    def enterAn_file(self, ctx: ZmeiLangParser.An_fileContext):

        if not self.application.supports(FileAppExtension):
            extension = FileAppExtension(self.application)
            self.application.extensions.append(
                extension
            )
            self.application.register_extension(extension)

        file_name = ctx.an_file_name().getText().strip('"')
        source = self._get_code(ctx.python_code())

        self.application[FileAppExtension].files[file_name] = source

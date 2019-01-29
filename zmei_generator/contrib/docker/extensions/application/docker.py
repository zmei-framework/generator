
from zmei_generator.domain.extensions import ApplicationExtension
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

class DockerAppExtension(ApplicationExtension):
    def get_name(cls):
        return 'docker'
    

class DockerAppExtensionParserListener(BaseListener):

    def enterAn_docker(self, ctx: ZmeiLangParser.An_dockerContext):
        extension = DockerAppExtension(self.application)
        self.application.extensions.append(
            extension
        )

        self.application.register_extension(extension)


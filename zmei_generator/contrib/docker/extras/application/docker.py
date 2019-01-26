
from zmei_generator.domain.application_extra import ApplicationExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

class DockerAppExtra(ApplicationExtra):
    def get_name(cls):
        return 'docker'
    

class DockerAppExtraParserListener(BaseListener):

    def enterAn_docker(self, ctx: ZmeiLangParser.An_dockerContext):
        extra = DockerAppExtra(self.application)
        self.application.extras.append(
            extra
        )

        self.application.docker = extra


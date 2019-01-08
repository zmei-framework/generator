
from zmei_generator.config.domain.collection_set_extra import CollectionSetExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

class DockerCsExtra(CollectionSetExtra):
    def get_name(cls):
        return 'docker'
    

class DockerCsExtraParserListener(BaseListener):

    def enterAn_docker(self, ctx: ZmeiLangParser.An_dockerContext):
        extra = DockerCsExtra(self.collection_set)
        self.collection_set.extras.append(
            extra
        )

        self.collection_set.docker = extra


from zmei_generator.config.domain.collection_set_def import CollectionSetDef
from zmei_generator.parser.gen.ZmeiLangParserListener import ZmeiLangParserListener


class BaseListener(ZmeiLangParserListener):

    def __init__(self, collection_set: CollectionSetDef) -> None:
        super().__init__()

        self.collection_set = collection_set

from zmei_generator.config.domain.collection_set_extra import CollectionSetExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class ChannelsCsExtra(CollectionSetExtra):
    def get_name(cls):
        return 'channels'

    def get_required_apps(self):
        return ['channels']

    def get_required_deps(self):
        return ['channels']


    @classmethod
    def write_settings(cls, apps, f):
        f.write("\nASGI_APPLICATION = 'app.routing.application'\n")
        f.write("\nCHANNEL_LAYERS = {\n")
        f.write("\n    'default': {\n")
        f.write("\n        'BACKEND': 'channels.layers.InMemoryChannelLayer',\n")
        f.write("\n    },\n")
        f.write("\n}\n")


class ChannelsCsExtraParserListener(BaseListener):

    def enterAn_channels(self, ctx: ZmeiLangParser.An_channelsContext):
        self.collection_set.extras.append(
            ChannelsCsExtra(self.collection_set)
        )
        self.collection_set.channels = True

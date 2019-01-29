from zmei_generator.domain.extensions import ApplicationExtension
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class ChannelsAppExtension(ApplicationExtension):
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


class ChannelsAppExtensionParserListener(BaseListener):

    def enterAn_channels(self, ctx: ZmeiLangParser.An_channelsContext):
        self.application.extensions.append(
            ChannelsAppExtension(self.application)
        )

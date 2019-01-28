
from zmei_generator.domain.extensions import ModelExtension
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

class MixinModelExtension(ModelExtension):
    def get_name(cls):
        return 'mixin'
    

class MixinModelExtensionParserListener(BaseListener):

    def enterAn_mixin(self, ctx: ZmeiLangParser.An_mixinContext):
        self.application.extensions.append(
            MixinModelExtension(self.model)
        )

        class_name = ctx.classname().getText()

        parts = class_name.split('.')
        model_cls = parts[-1]

        if model_cls == self.model.class_name:
            alias = '{}_'.format(model_cls)
        else:
            alias = model_cls

        self.model.mixin_classes.append(
            ('.'.join(parts[:-1]), parts[-1], alias)
        )


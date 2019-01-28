from zmei_generator.parser.errors import GlobalScopeValidationError as ValidationException
from zmei_generator.domain.extensions import ModelExtension
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class ApiModelExtension(ModelExtension):

    def __init__(self, model) -> None:
        super().__init__(model)

        self.api_names = []
        self.all = False

    def get_required_apps(self):
        return ['rest_framework']

    def post_process(self):
        if self.all:
            self.model.published_apis = self.model.rest_conf
            return

        if len(self.api_names) == 0:
            self.api_names = ['_']

        for api in self.api_names:
            if api not in self.model.rest_conf:
               raise ValidationException(
                   f'@api error: no such @rest config "{api}"')

            self.model.published_apis[api] = self.model.rest_conf[api]


class ApiModelExtensionParserListener(BaseListener):

    def enterAn_api(self, ctx: ZmeiLangParser.An_apiContext):
        extension = ApiModelExtension(self.model)
        self.application.extensions.append(
            extension
        )

        self.application.api = True
        self.model.api = extension

    def enterAn_api_name(self, ctx: ZmeiLangParser.An_api_nameContext):
        self.model.api.api_names.append(ctx.getText())

    def enterAn_api_all(self, ctx: ZmeiLangParser.An_api_allContext):
        self.model.api.all = True








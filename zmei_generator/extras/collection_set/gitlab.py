from zmei_generator.config.domain.collection_set_def import CollectionSetDef
from zmei_generator.config.domain.collection_set_extra import CollectionSetExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class ServiceConfig(object):

    def __init__(self) -> None:
        super().__init__()

        self.name = None
        self.vars = {}


class SeleniumPytestConfig(object):

    def __init__(self) -> None:
        super().__init__()

        self.services = {}
        self.vars = {}


class DeploymentConfig(object):

    def __init__(self) -> None:
        super().__init__()

        self.manual_deploy = False
        self.branch = None
        self.deployment = None
        self.hostname = None
        self.vars = {}


class GitlabCsExtra(CollectionSetExtra):

    def __init__(self, collection_set):
        super().__init__(collection_set)

        self.configs = []  # type: list[DeploymentConfig]
        self.test = None  # type: SeleniumPytestConfig

    def get_name(cls):
        return 'gitlab'
    

class GitlabCsExtraParserListener(BaseListener):

    def __init__(self, collection_set: CollectionSetDef) -> None:
        super().__init__(collection_set)

        self.dp = None  # type: DeploymentConfig
        self.test = None  # type: SeleniumPytestConfig
        self.service = None  # type: ServiceConfig

    def enterAn_gitlab(self, ctx: ZmeiLangParser.An_gitlabContext):
        extra = GitlabCsExtra(self.collection_set)
        self.collection_set.extras.append(
            extra
        )
        self.collection_set.gitlab = extra

    def enterAn_gitlab_test_declaration_selenium_pytest(self,
                                                        ctx: ZmeiLangParser.An_gitlab_test_declaration_selenium_pytestContext):
        self.test = SeleniumPytestConfig()

    def exitAn_gitlab_test_declaration_selenium_pytest(self,
                                                       ctx: ZmeiLangParser.An_gitlab_test_declaration_selenium_pytestContext):
        self.collection_set.gitlab.test = self.test
        self.test = None

    def enterAn_gitlab_test_service(self, ctx: ZmeiLangParser.An_gitlab_test_serviceContext):
        self.service = ServiceConfig()
        self.service.name = ctx.an_gitlab_test_service_name().getText()

    def exitAn_gitlab_test_service(self, ctx: ZmeiLangParser.An_gitlab_test_serviceContext):
        self.test.services[self.service.name] = self.service
        self.service = None

    def enterAn_gitlab_branch_declaration(self, ctx: ZmeiLangParser.An_gitlab_branch_declarationContext):
        self.dp = DeploymentConfig()

    def enterAn_gitlab_branch_deploy_type(self, ctx: ZmeiLangParser.An_gitlab_branch_deploy_typeContext):
        self.dp.manual_deploy = ctx.getText() == '~>'

    def enterAn_gitlab_branch_name(self, ctx: ZmeiLangParser.An_gitlab_branch_nameContext):
        self.dp.branch = ctx.getText()

    def enterAn_gitlab_deployment_name(self, ctx: ZmeiLangParser.An_gitlab_deployment_nameContext):
        self.dp.deployment = ctx.getText()

    def enterAn_gitlab_deployment_host(self, ctx: ZmeiLangParser.An_gitlab_deployment_hostContext):
        self.dp.hostname = ctx.getText()

    def enterAn_gitlab_deployment_variable(self, ctx: ZmeiLangParser.An_gitlab_deployment_variableContext):
        if self.service:
            obj = self.service
        elif self.test:
            obj = self.test
        elif self.dp:
            obj = self.dp
        else:
            raise Exception('No destination for variable. Grammar error?')

        obj.vars[ctx.an_gitlab_deployment_variable_name().getText()] = ctx.an_gitlab_deployment_variable_value().getText()

    def exitAn_gitlab_branch_declaration(self, ctx: ZmeiLangParser.An_gitlab_branch_declarationContext):
        super().exitAn_gitlab_branch_declaration(ctx)

        self.collection_set.gitlab.configs.append(self.dp)
        self.dp = None







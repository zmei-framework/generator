from zmei_generator.domain.application_def import ApplicationDef
from zmei_generator.domain.extensions import ApplicationExtension
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
        self.environment = None
        self.hostname = None
        self.vars = {}

    @property
    def coverage(self):
        return 'coverage' in self.vars

    @property
    def deployment(self):
        return self.environment.replace('/', '-')


class GitlabAppExtension(ApplicationExtension):

    def __init__(self, application):
        super().__init__(application)

        self.configs = []  # type: list[DeploymentConfig]
        self.test = None  # type: SeleniumPytestConfig

    def get_name(cls):
        return 'gitlab'
    

class GitlabAppExtensionParserListener(BaseListener):

    def __init__(self, application: ApplicationDef) -> None:
        super().__init__(application)

        self.dp = None  # type: DeploymentConfig
        self.test = None  # type: SeleniumPytestConfig
        self.service = None  # type: ServiceConfig

    def enterAn_gitlab(self, ctx: ZmeiLangParser.An_gitlabContext):
        extension = GitlabAppExtension(self.application)
        self.application.extensions.append(
            extension
        )
        self.application.register_extension(extension)

    def enterAn_gitlab_test_declaration_selenium_pytest(self,
                                                        ctx: ZmeiLangParser.An_gitlab_test_declaration_selenium_pytestContext):
        self.test = SeleniumPytestConfig()

    def exitAn_gitlab_test_declaration_selenium_pytest(self,
                                                       ctx: ZmeiLangParser.An_gitlab_test_declaration_selenium_pytestContext):
        self.application[GitlabAppExtension].test = self.test
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
        val = ctx.getText()
        if '*' in val:
            val = val.replace('/', '\/')
            val = val.replace('*', '.*')
            val = f'/^{val}$/'
        self.dp.branch = val

    def enterAn_gitlab_deployment_name(self, ctx: ZmeiLangParser.An_gitlab_deployment_nameContext):
        val = ctx.getText()
        self.dp.environment = val

    def enterAn_gitlab_deployment_host(self, ctx: ZmeiLangParser.An_gitlab_deployment_hostContext):
        val = ctx.getText()
        self.dp.hostname = val

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

        if 'coverage' in self.dp.vars:
            val = self.dp.vars['coverage'].strip('"\'')
            if not val.endswith('/'):
                val += '/'
            self.dp.vars['coverage'] = val

        self.application[GitlabAppExtension].configs.append(self.dp)
        self.dp = None







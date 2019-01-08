from zmei_generator.config.domain.collection_set_def import CollectionSetDef
from zmei_generator.config.domain.collection_set_extra import CollectionSetExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class DeploymentConfig(object):

    def __init__(self) -> None:
        super().__init__()

        self.branch = None
        self.deployment = None
        self.hostname = None
        self.vars = {}


class GitlabCsExtra(CollectionSetExtra):

    def __init__(self, collection_set):
        super().__init__(collection_set)

        self.configs = []  # type: list[DeploymentConfig]

    def get_name(cls):
        return 'gitlab'
    

class GitlabCsExtraParserListener(BaseListener):

    def __init__(self, collection_set: CollectionSetDef) -> None:
        super().__init__(collection_set)

        self.dp = None # type: DeploymentConfig

    def enterAn_gitlab(self, ctx: ZmeiLangParser.An_gitlabContext):
        extra = GitlabCsExtra(self.collection_set)
        self.collection_set.extras.append(
            extra
        )
        self.collection_set.gitlab = extra

    def enterAn_gitlab_branch_declaration(self, ctx: ZmeiLangParser.An_gitlab_branch_declarationContext):
        super().enterAn_gitlab_branch_declaration(ctx)

        self.dp = DeploymentConfig()

    def enterAn_gitlab_branch_name(self, ctx: ZmeiLangParser.An_gitlab_branch_nameContext):
        super().enterAn_gitlab_branch_name(ctx)

        self.dp.branch = ctx.getText()

    def enterAn_gitlab_deployment_name(self, ctx: ZmeiLangParser.An_gitlab_deployment_nameContext):
        super().enterAn_gitlab_deployment_name(ctx)

        self.dp.deployment = ctx.getText()

    def enterAn_gitlab_deployment_host(self, ctx: ZmeiLangParser.An_gitlab_deployment_hostContext):
        super().enterAn_gitlab_deployment_host(ctx)

        self.dp.hostname = ctx.getText()

    def enterAn_gitlab_deployment_variable(self, ctx: ZmeiLangParser.An_gitlab_deployment_variableContext):
        super().enterAn_gitlab_deployment_variable(ctx)

        self.dp.vars[ctx.an_gitlab_deployment_variable_name().getText()] = ctx.an_gitlab_deployment_variable_value().getText()

    def exitAn_gitlab_branch_declaration(self, ctx: ZmeiLangParser.An_gitlab_branch_declarationContext):
        super().exitAn_gitlab_branch_declaration(ctx)

        self.collection_set.gitlab.configs.append(self.dp)
        self.dp = None







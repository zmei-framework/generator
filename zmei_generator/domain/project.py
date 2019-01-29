from zmei_generator.domain.extensions import Extendable


class ZmeiProject(Extendable):

    def __init__(self) -> None:
        super().__init__()

        self.applications = {}

    def add_application(self, name, application):
        application.application = self
        self.applications[name] = application

    def get_application(self, name):
        return self.applications[name]
        
    def applications_support(self, extension_cls):
        for application in self.applications.values():
            if application.supports(extension_cls):
                return True
        return False
        
    def applications_with(self, extension_cls):
        return [application for application in self.applications.values() if application.supports(extension_cls)]
        
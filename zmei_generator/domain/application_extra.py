from zmei_generator.domain.extras import Extra


class ApplicationExtra(Extra):

    def __init__(self, application):
        super().__init__()

        self.application = application




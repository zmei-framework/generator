from zmei_generator.domain.project import ZmeiProject
from zmei_generator.parser.parser import ZmeiParser


class ZmeiProjectParser(object):

    def __init__(self) -> None:
        super().__init__()

        self.files = {}

    def _parse_file(self, app, name, source):
        app_name = name[:-4]

        parser = ZmeiParser()

        parser.parse_string(source)

        return app_name, parser

    def add_file(self, name, source):
        if not name.endswith('.col'):
            raise ValueError('Only col files allowed')

        if name.startswith('col/'):
            name = name[4:]

        self.files[name] = source

    def parse(self):
        project = ZmeiProject()

        # initialise parsers
        parsers = {}
        for file_name, source in self.files.items():
            app_name, parser = self._parse_file(project, file_name, source)
            parsers[app_name] = parser

        # parse model set
        for app_name, parser in parsers.items():
            app = parser.build_application(app_name)
            parser.process_application(app)

            project.add_application(app_name, app)

        # post process (relation late-binding mostly)
        for app in project.applications.values():
            app.post_process()

        # model extensions parsing
        for app_name, parser in parsers.items():
            parser.process_model_extensions(project.applications[app_name])

        # page parsing
        for app_name, parser in parsers.items():
            parser.process_page_extensions(project.applications[app_name])

        # page extensions parsing
        for app in project.applications.values():
            app.post_process_extensions()

        return project

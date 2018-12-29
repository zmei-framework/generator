from zmei_generator.parser.parser import ZmeiParser


class ZmeiAppParser(object):

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
        app = ZmeiApp()

        # initialise parsers
        parsers = {}
        for file_name, source in self.files.items():
            app_name, parser = self._parse_file(app, file_name, source)
            parsers[app_name] = parser

        # parse collection set
        for app_name, parser in parsers.items():
            cs = parser.build_collection_set(app_name)
            parser.process_collection_set(cs)

            app.add_cs(app_name, cs)

        # post process (relation late-binding mostly)
        for cs in app.collection_sets.values():
            cs.post_process()

        # model extras parsing
        for app_name, parser in parsers.items():
            parser.process_model_extras(app.collection_sets[app_name])

        # page parsing
        for app_name, parser in parsers.items():
            parser.process_page_extras(app.collection_sets[app_name])

        # page extras parsing
        for cs in app.collection_sets.values():
            cs.post_process_extras()

        return app


class ZmeiApp(object):

    def __init__(self) -> None:
        super().__init__()

        self.collection_sets = {}

    def add_cs(self, name, collection_set):
        collection_set.application = self
        self.collection_sets[name] = collection_set

    def get_collection_set(self, name):
        return self.collection_sets[name]
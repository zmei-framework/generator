class ImportSet(object):

    def __init__(self) -> None:
        self.imports = {}

        super().__init__()

    def add(self, source, *what):
        if source not in self.imports:
            self.imports[source] = []

        for one in what:
            if one not in self.imports[source]:
                self.imports[source].append(one)

    def import_sting(self):
        items = sorted(self.imports.items())
        return '\n'.join(['from {} import {}'.format(source, ', '.join(what)) for source, what in items])

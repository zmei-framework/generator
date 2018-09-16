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

    def find_import_source(self, what):
        for import_from, whats in self.imports.items():
            if what in whats:
                return import_from, what
            if f'*{what}' in whats:
                return import_from, f'*{what}'
        return None, None

    def import_sting(self):
        items = sorted(self.imports.items())
        return '\n'.join(['from {} import {}'.format(source, ', '.join(what)) for source, what in items])

    def import_sting_js(self):
        items = sorted(self.imports.items())

        grouped = {}
        ungrouped = {}

        for source, what_items in items:
            for what in what_items:
                if what[0] == '*':
                    if source not in grouped:
                        grouped[source] = set()

                    grouped[source].add(what[1:])
                else:
                    if source not in ungrouped:
                        ungrouped[source] = set()

                    ungrouped[source].add(what)

        stm = []

        for source, what in grouped.items():
            stm.append("import {{{}}} from '{}';".format(', '.join(what), source))

        for source, what in ungrouped.items():
            stm.append("import {} from '{}';".format(', '.join(what), source))

        return '\n'.join(stm)

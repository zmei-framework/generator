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

    def import_sting_js(self):
        items = sorted(self.imports.items())

        stm = []

        for source, what in items:
            if len(what) == 1:
                what = what[0]
            else:
                what = '{' + ', '.join(what) + '}'
            stm.append("import {} from '{}';".format(what, source))

        return '\n'.join(stm)

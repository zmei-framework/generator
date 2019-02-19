from functools import reduce


class ImportSet(object):

    def __init__(self) -> None:
        self.imports = {}

        super().__init__()

    def add(self, source, *what):
        if source not in self.imports:
            self.imports[source] = []

        for one in what:
            self.imports[source].append(one)

    def find_import_source(self, what):
        for import_from, whats in self.imports.items():
            if what in whats:
                return import_from, what
            if f'*{what}' in whats:
                return import_from, f'*{what}'
        return None, None

    def import_sting(self):
        items = self.get_items()

        def format_expr(source, what):
            expr = 'import {}'.format(', '.join(what))
            if source:
                expr = 'from {} {}'.format(source, expr)
            return expr

        return '\n'.join([format_expr(source, what) for source, what in items])

    def get_items(self):
        def simplify(imports, b):
            if b == '*':
                imports = [x for x in imports if ' as ' in x]

            if '*' in imports and ' as ' not in b:
                return imports

            if b in imports:
                return imports

            return imports + [b]

        # NB! source maybe None as well, so can not be sorted easily
        return [(source, reduce(simplify, values, [])) for source, values in self.imports.items()]

    def import_sting_js(self):
        items = self.get_items()

        grouped = {}
        ungrouped = {}

        for source, what_items in items:
            for what in what_items:
                if what[0] == '*' and ' as ' not in what:
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

    def __str__(self) -> str:
        return self.import_sting()


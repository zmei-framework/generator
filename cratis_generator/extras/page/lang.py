from cratis_generator.config.domain import PageExtra


class LangPageExtra(PageExtra):
    @property
    def has_python_code(self):
        return True

    def get_imports(self):
        imports = []
        for match in re.findall(r'#(\w+)\.', self.expression):
            col = self.find_collection_by_ref(match)
            imports.append(('{}.models'.format(col.collection_set.app_name), col.class_name))

        if self.or_404:
            imports.append(('django.core.exceptions', 'ObjectDoesNotExist'))
            imports.append(('django.http', 'Http404'))

        return imports

    def get_python_code(self):
        code = """
data['']             
"""
        return True

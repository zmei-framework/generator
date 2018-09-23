class PageExtra(object):

    def __init__(self, parsed_result, page):
        self.page = page

    @property
    def has_python_code(self):
        return False

    def get_imports(self):
        return []

    def get_python_code(self):
        return ''

    def post_process(self):
        pass

    def get_required_apps(self):
        return []

    def get_required_deps(self):
        return []

    def get_required_settings(self):
        return {}

    def get_required_urls(self):
        return []


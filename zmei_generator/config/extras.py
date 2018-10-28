from abc import abstractmethod, abstractclassmethod


class Extra(object):

    @classmethod
    @abstractclassmethod
    def get_name(cls):  # pragma: no cover
        pass

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

    @classmethod
    def write_settings(cls, apps, f):
        pass

    @classmethod
    def generate(cls, apps, target_path):
        pass

class ModelExtra(Extra):

    def __init__(self, model) -> None:
        super().__init__()

        self.model = model


class PageExtra(Extra):

    def __init__(self, page) -> None:
        super().__init__()

        self.page = page
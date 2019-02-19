class Extension(object):

    extension_many = False

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

    def format_extension_value(self, current_value):
        """

        :param current_value:
        :param extension: Extension
        :return:
        """
        return self

    def get_extension_type(self):
        """

        :param current_value:
        :param extension: Extension
        :return:
        """
        return type(self)


class ApplicationExtension(Extension):

    def __init__(self, application):
        super().__init__()

        application.register_extension(self)

        self.application = application


class ModelExtension(Extension):

    def __init__(self, model) -> None:
        super().__init__()

        model.register_extension(self)

        self.model = model


class PageExtension(Extension):

    def __init__(self, page) -> None:
        super().__init__()

        self.page = page

    @property
    def can_inherit(self):
        return False

    def filter_blocks(self, area, blocks, platform):
        return blocks

    def get_extension_bases(self, bases):
        return bases


class Extendable(object):

    def __init__(self) -> None:
        super().__init__()

        self._extensions = {}

    def register_extension(self, extension: Extension):
        _type = extension.get_extension_type()
        self._extensions[_type] = extension.format_extension_value(self._extensions.get(_type))

    def supports(self, cls):
        return cls in self._extensions

    def get_extensions(self):
        return self._extensions.values()

    def __getitem__(self, cls):
        if cls in self._extensions:
            return self._extensions[cls]

        raise IndexError(f'{self} does not support {cls} extension')
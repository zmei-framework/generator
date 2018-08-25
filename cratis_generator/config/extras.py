from abc import abstractmethod, abstractclassmethod


class Extra(object):

    @classmethod
    @abstractclassmethod
    def get_name(cls):  # pragma: no cover
        pass

    @abstractmethod
    def parse(self, extra, collection):  # pragma: no cover
        pass

    def post_process(self):
        pass



def cached(func, suffix='data'):
    def _wrap(self, *args, **kwargs):
        if hasattr(self, '_' + suffix):
            return getattr(self, '_' + suffix)
        data = func(self, *args, **kwargs)
        setattr(self, '_' + suffix, data)
        return data
    return _wrap

class _Data(object):
    def __init__(self, data=None):
        self.__dict__.update(data or {})

    def __add__(self, data):
        return _Data({**self.__dict__, **data})


class _View(object):
    def get_data(self, inherited):
        return _Data()

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**self.kwargs)
        return {**data, **self.get_data().__dict__}

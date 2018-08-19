import json

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
        context_data = super().get_context_data(**self.kwargs)
        data = self.get_data().__dict__

        all_data = {**context_data, **data}

        return all_data

def to_react_json(view, data):
    state = {}

    for key, val in data.__dict__.items():
        if key == 'url':
            state['url'] = view.kwargs
        else:
            state[key] = val

    return json.dumps(state)
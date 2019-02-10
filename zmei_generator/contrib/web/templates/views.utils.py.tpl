from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.base import View, ContextMixin


class ImproperlyConfigured(Exception):
    pass


class Data(dict):
    def __getattr__(self, item):
        return self[item]


class RedirectAction(Exception):

    def __init__(self, url_name=None, url=None, **kwargs) -> None:
        super().__init__()

        if not url:
            url = reverse(url_name, kwargs=kwargs)

        self.response = redirect(url)


class ZmeiDataViewMixin(ContextMixin, View):
    _data = None

    def get_data(self, url, request, inherited=False):
        return {}

    def _get_data(self):
        if not self._data:
            url = type('url', (object,), self.kwargs)
            self._data = self.get_data(
                url=url,
                request=self.request,
                inherited=False
            )
            self._data['url'] = url

        return self._data

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        return {**context_data, **self._get_data()}

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except RedirectAction as action:
            return action.response
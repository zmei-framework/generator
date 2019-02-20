import json

from django.http import HttpResponseRedirect, HttpResponse

from .rest import ZmeiJsonEncoder, ZmeiRemoteInvocationViewMixin


class ZmeiReactViewMixin(ZmeiRemoteInvocationViewMixin):
    react_server = None
    react_components = None
    server_render = False

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        data['react_state'] = ZmeiJsonEncoder(
            view=self).encode(self._get_data())

        return data

    def dispatch(self, request, *args, **kwargs):
        accept = self.request.META.get('HTTP_ACCEPT')
        if accept and 'application/json' in accept:
            try:
                response = super().dispatch(request, *args, **kwargs)
            except Exception as e:
                response = HttpResponse(json.dumps(self.error(e)))

            if isinstance(response, HttpResponseRedirect):
                return HttpResponse(json.dumps({'__redirect__': response.url}), content_type='application/json')

            return response

        return super().dispatch(request, *args, **kwargs)


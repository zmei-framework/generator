import json

from django.forms import Form, BaseForm
from django.http import HttpResponse
from django.utils.decorators import classonlymethod
from django.utils.module_loading import import_string
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import serializers
from json import JSONEncoder
from django.db.models import QuerySet, Model

from .views import ZmeiDataViewMixin

from django.forms import widgets, fields


def pretty_name(name):
    """Converts 'first_name' to 'First name'"""
    if not name:
        return u''
    return name.replace('_', ' ').capitalize()


class FormJSONSchemaEncoder(object):
    def convert_form(self, form, json_schema=None):
        json_schema = json_schema or {
            # 'title':dockit_schema._meta
            # 'description'
            'type': 'object',
            'fields': [],
            'required': []
        }

        initial = {}

        for bound_field in form:
            json_schema['fields'].append(self.convert_formfield(form, bound_field.name, bound_field))

            if bound_field.field.required:
                json_schema['required'].append(bound_field.name)

            if bound_field.value():
                initial[f'{form.prefix}-{bound_field.name}' if form.prefix else bound_field.name] = bound_field.value()

        return {
            'prefix': form.prefix,
            'schema': json_schema,
            'initial': initial,
            'errors': form.non_field_errors(),
        }

    input_type_map = {
        'text': 'string',
    }

    def convert_formfield(self, form, name, bound_field):
        field = bound_field.field
        widget = field.widget

        target_def = {
            'name': f'{form.prefix}-{name}' if form.prefix else name,
            'title': field.label or pretty_name(name),
            'description': field.help_text,
        }
        if bound_field.errors:
            target_def['serverErrors'] = bound_field.errors

        # if bound_field.value():
        # target_def['value'] = bound_field.value() or ''

        if isinstance(field, fields.URLField):
            target_def['type'] = 'url'
            # target_def['format'] = 'url'
        elif isinstance(field, fields.FileField):
            target_def['type'] = 'text'
        elif isinstance(field, fields.DateField):
            target_def['type'] = 'date'
        elif isinstance(field, fields.DateTimeField):
            target_def['type'] = 'datetime'
        elif isinstance(field, (fields.DecimalField, fields.FloatField)):
            target_def['type'] = 'number'
        elif isinstance(field, fields.IntegerField):
            target_def['type'] = 'number'
        elif isinstance(field, fields.EmailField):
            target_def['type'] = 'email'
        elif isinstance(field, fields.NullBooleanField):
            target_def['type'] = 'checkbox'
        elif isinstance(widget, widgets.CheckboxInput):
            target_def['type'] = 'checkbox'
        elif isinstance(widget, widgets.Select):
            if widget.allow_multiple_selected:
                target_def['type'] = 'choices'
            else:
                target_def['type'] = 'choices'
            target_def['options'] = [{'label': title, 'value': value} for value, title in field.choices]

        elif isinstance(widget, widgets.Input):
            # translated_type = self.input_type_map.get(widget.input_type, 'text')
            target_def['type'] = 'text'
        else:
            target_def['type'] = 'text'
        return target_def


class DefaultModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = None
        exclude = []

    def get_field_names(self, declared_fields, info):
        return super().get_field_names(declared_fields, info) + '__str__'


def create_default_serializer(model):
    serializer = type('_', (DefaultModelSerializer,), {})
    serializer.Meta.model = model

    return serializer


def get_model_serializer(model, descriptor='_', strict=False):
    serializer = None
    try:
        index_import_path = f"{'.'.join(model.__module__.split('.')[:-1])}.serializers.index"
        serializer_index = import_string(index_import_path)

        if model in serializer_index:
            serializer = serializer_index[model].get(descriptor)
            if not serializer and strict:
                raise AttributeError(
                    f'Serializer with name "{descriptor}" does not exist for model "{model}"')
    except ImportError:
        pass

    if not serializer:
        serializer = create_default_serializer(model)

    return serializer


def serialize(qs_or_model, descriptor='_'):
    if isinstance(qs_or_model, QuerySet):
        model = qs_or_model.model
        many = True
    elif isinstance(qs_or_model, Model):
        model = qs_or_model
        many = False
    else:
        raise AttributeError(
            'serialize method accept only QuerySet or Model. Given: ', type(qs_or_model))

    return get_model_serializer(model, descriptor=descriptor, strict=True)(qs_or_model, many=many).data


class ZmeiJsonEncoder(JSONEncoder):
    def __init__(self, *, view=None, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True,
                 sort_keys=False,
                 indent=None, separators=None, default=None):
        super().__init__(skipkeys=skipkeys, ensure_ascii=ensure_ascii, check_circular=check_circular,
                         allow_nan=allow_nan, sort_keys=sort_keys, indent=indent, separators=separators,
                         default=default)
        if not view:
            raise AttributeError('ZmeiJsonEncoder: View is required')
        self.view = view

        self.serializers_cache = {}

    def get_model_serializer(self, model):
        if model not in self.serializers_cache:
            self.serializers_cache[model] = get_model_serializer(model)

        return self.serializers_cache[model]

    def default(self, o):
        # url object
        if hasattr(o, '__name__') and o.__name__ == 'url':
            return self.view.kwargs

        if isinstance(o, QuerySet):
            serializer = self.get_model_serializer(o.model)
            return serializer(o, many=True).data

        if isinstance(o, Model):
            serializer = self.get_model_serializer(type(o))
            return serializer(o).data

        if o.__class__.__name__ == '__proxy__':
            return str(o)

        if isinstance(o, BaseForm):
            return FormJSONSchemaEncoder().convert_form(o)

        print(
            f'WARN: ZmeiJsonEncoder -> Do not know how to encode "{o.__class__}"', o)
        return None


class ZmeiRemoteInvocationViewMixin(ZmeiDataViewMixin):

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        accept = self.request.META.get('HTTP_ACCEPT')
        if accept and 'application/json' in accept:
            return HttpResponse(ZmeiJsonEncoder(view=self).encode(self.state(self._get_data())),
                                content_type='application/json')

        return self.render_to_response(context)

    @classonlymethod
    def as_view(cls, **initkwargs):
        return ensure_csrf_cookie(super().as_view(**initkwargs))

    def _remote_response(self, data):
        return HttpResponse(ZmeiJsonEncoder(view=self).encode(data), content_type='application/json')

    def state(self, data):
        return {'__state__': data}

    def error(self, data):
        return {'__error__': data}

    def post(self, request, *args, **kwargs):
        if 'application/json' not in self.request.META['HTTP_ACCEPT']:
            raise ValueError('Only json is available as a response type.')

        call = json.loads(request.body)
        method_name = f"_remote__{call.get('method')}"

        if not hasattr(self, method_name):
            raise ValueError('Unknown method')

        method = getattr(self, method_name)

        result = method(
            type('url', (object,), self.kwargs),
            request,
            *(call.get('args') or [])
        )

        if not result:
            return self._remote_response(self.state(self._get_data()))

        return self._remote_response(result)

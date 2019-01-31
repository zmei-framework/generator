import re

from zmei_generator.domain.application_def import ApplicationDef
from zmei_generator.domain.extensions import PageExtension
from zmei_generator.domain.frozen import FrozenClass
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class StreamModel(FrozenClass):

    def __init__(self, page) -> None:
        self.page = page
        self.model_app_name = None
        self.model_class_name = None
        self.filter_expr = None
        self.fields = None

        self._freeze()

    @property
    def class_name(self):
        return self.target

    @property
    def stream_name(self):
        return re.sub('[^a-z0-9]+', '_', self.target.lower())


class StreamPageExtension(PageExtension):
    # stream

    def __init__(self, page) -> None:
        super().__init__(page)

        self.models = []

    def get_required_apps(self):
        return ['django_query_signals']

    def get_required_deps(self):
        return ['django-query-signals']


class StreamPageExtensionParserListener(BaseListener):

    def __init__(self, application: ApplicationDef) -> None:
        super().__init__(application)

        self.stream_model = None

    def enterAn_stream(self, ctx: ZmeiLangParser.An_streamContext):
        stream = StreamPageExtension(self.page)
        self.application.extensions.append(
            stream
        )
        self.page.register_extension(stream)

    def enterAn_stream_target_model(self, ctx: ZmeiLangParser.An_stream_target_modelContext):
        super().enterAn_stream_target_model(ctx)

        stream_model = StreamModel(self.page)
        target = ctx.getText()

        if target.startswith('#'):
            model = self.application.resolve_model(target[1:])
            stream_model.model_class_name = model.class_name
            stream_model.model_app_name = model.application.app_name
        else:
            stream_model.model_class_name = target.split('.')[-1]
            stream_model.model_app_name = '.'.join(target.split('.')[:-1])

        self.page[StreamPageExtension].models.append(
            stream_model
        )

        self.stream_model = stream_model

    def enterAn_stream_target_filter(self, ctx: ZmeiLangParser.An_stream_target_filterContext):
        self.stream_model.filter_expr = self._get_code(ctx)

    def enterAn_stream_field_name(self, ctx: ZmeiLangParser.An_stream_field_nameContext):
        field_name = ctx.getText()

        if not self.stream_model.fields:
            self.stream_model.fields = [field_name]
        else:
            self.stream_model.fields.append(field_name)

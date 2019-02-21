from zmei_generator.domain.application_def import FieldDeclaration, ApplicationDef
from zmei_generator.parser.errors import GlobalScopeValidationError as ValidationException
from zmei_generator.domain.extensions import ModelExtension
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class RestModelExtension(ModelExtension):

    def __init__(self, model) -> None:
        super().__init__(model)

        self.config = None
        self.rest_conf = {}
        self.published_apis = {}
        self.rest_mode = None

    def get_required_apps(self):
        return ['rest_framework']

    def get_required_deps(self):
        return ['djangorestframework']

    def post_process(self):
        for config in self.model[RestModelExtension].rest_conf.values():
            config.post_process()


class RestModelExtensionParserListener(BaseListener):
    def __init__(self, application: ApplicationDef) -> None:
        super().__init__(application)

        self.rest_config = None
        self.rest_config_stack = []

    def ensure_defaults(self):
        # fields
        if not self.rest_config.fields:
            self.rest_config.set_fields(self.rest_config.model.filter_fields(['*'], include_refs=True))

    def enterAn_rest(self, ctx: ZmeiLangParser.An_restContext):
        if not self.model.supports(RestModelExtension):
            ext = RestModelExtension(self.model)
            self.application.extensions.append(ext)
            self.model.register_extension(ext)

        self.rest_config = RestSerializerConfig(self.model.class_name, self.model)

    def exitAn_rest_main_part(self, ctx: ZmeiLangParser.An_rest_main_partContext):
        self.ensure_defaults()

    def exitAn_rest(self, ctx: ZmeiLangParser.An_restContext):
        self.ensure_defaults()

        # Place config where it should be
        if not self.model[RestModelExtension].rest_conf:
            self.model[RestModelExtension].rest_conf = {}

        self.model[RestModelExtension].rest_conf[self.rest_config.descriptor] = self.rest_config

    def enterAn_rest_descriptor(self, ctx: ZmeiLangParser.An_rest_descriptorContext):
        self.rest_config.set_descriptor(ctx.getText())

    def enterAn_rest_fields(self, ctx: ZmeiLangParser.An_rest_fieldsContext):
        self.rest_config.set_fields(self.rest_config.model.filter_fields(self._get_fields(ctx), include_refs=True))

    def enterAn_rest_i18n(self, ctx: ZmeiLangParser.An_rest_i18nContext):
        self.rest_config.i18n = ctx.BOOL().getText() == 'true'

    def enterAn_rest_str(self, ctx: ZmeiLangParser.An_rest_strContext):
        self.rest_config.str = ctx.BOOL().getText() == 'true'

    def enterAn_rest_fields_write_mode(self, ctx: ZmeiLangParser.An_rest_fields_write_modeContext):
        if ctx.write_mode_expr():
            self.rest_config.rest_mode = ctx.write_mode_expr().WRITE_MODE().getText()

    def enterAn_rest_user_field(self, ctx: ZmeiLangParser.An_rest_user_fieldContext):
        self.rest_config.user_field = ctx.id_or_kw().getText()

    def enterAn_rest_query(self, ctx: ZmeiLangParser.An_rest_queryContext):
        self.rest_config.query = self._get_code(ctx.python_code())

    def enterAn_rest_on_create(self, ctx: ZmeiLangParser.An_rest_on_createContext):
        self.rest_config.on_create = self._get_code(ctx.python_code())

    def enterAn_rest_filter_in(self, ctx: ZmeiLangParser.An_rest_filter_inContext):
        self.rest_config.filter_in = self._get_code(ctx.python_code())

    def enterAn_rest_filter_out(self, ctx: ZmeiLangParser.An_rest_filter_outContext):
        self.rest_config.filter_out = self._get_code(ctx.python_code())

    def exitAn_rest_auth_type(self, ctx: ZmeiLangParser.An_rest_auth_typeContext):
        ref = None
        if ctx.an_rest_auth_token_model():
            ref = ctx.an_rest_auth_token_model().getText()

        if ctx.an_rest_auth_token_class():
            ref = ctx.an_rest_auth_token_class().getText()

        self.rest_config.add_auth_method(ctx.an_rest_auth_type_name().getText(), ref)

    def enterAn_rest_inline_decl(self, ctx: ZmeiLangParser.An_rest_inline_declContext):
        name = ctx.an_rest_inline_name().getText()
        field = self.rest_config.fields_index[name]

        inline_model = field.get_rest_inline_model()
        if not inline_model:
            raise ValidationException('field "{}" can not be used as inline'.format(field.name))

        serializer_name = self.rest_config.serializer_name + '_Inline' + inline_model.class_name

        new_config = RestSerializerConfig(serializer_name, inline_model, field)

        self.rest_config.inlines[name] = new_config

        self.rest_config.extension_serializers.append(new_config)

        self.rest_config.field_imports.append(
            FieldDeclaration('{}.models'.format(inline_model.application.app_name),
                             inline_model.class_name))

        self.rest_config.field_declarations.append(
            (field.name, '{}Serializer(many={}, read_only={})'.format(serializer_name, repr(field.is_many),
                                                                      repr(
                                                                          field.name in self.rest_config.read_only_fields))))

        self.rest_config_stack.append(self.rest_config)
        self.rest_config = new_config

    def exitAn_rest_inline_decl(self, ctx: ZmeiLangParser.An_rest_inline_declContext):
        self.rest_config = self.rest_config_stack.pop()

    def enterAn_rest_read_only(self, ctx: ZmeiLangParser.An_rest_read_onlyContext):
        self.rest_config.read_only_fields = [f.name for f in
                                             self.rest_config.model.filter_fields(self._get_fields(ctx))]

    def enterAn_rest_annotate_count(self, ctx: ZmeiLangParser.An_rest_annotate_countContext):
        field = ctx.an_rest_annotate_count_field().getText()
        kind = 'count'

        if ctx.an_rest_annotate_count_alias():
            alias = ctx.an_rest_annotate_count_alias().getText()
        else:
            alias = '{}_{}'.format(field, kind)

        self.rest_config.field_declarations.append((alias, 'serializers.IntegerField()'))
        self.rest_config.field_names.append(alias)
        self.rest_config.annotations.append("{}=Count('{}', distinct=True)".format(alias, field))
        self.rest_config.field_imports.append(FieldDeclaration('django.db.models', 'Count'))


class RestSerializerConfig(object):

    def __init__(self, serializer_name, model, parent_field=None) -> None:
        self.descriptor = '_'
        self.fields = None
        self.fields_index = {}
        self.i18n = False
        self.str = True
        self.model = model
        self.parent_field = parent_field
        self.serializer_name = serializer_name

        self.field_declarations = []
        self.field_imports = []
        self.field_names = None
        self.annotations = []
        self.auth_methods = {}
        self.auth_method_classes = []
        self.query = 'all()'
        self.on_create = ''
        self.filter_in = ''
        self.filter_out = ''
        self.rest_mode = 'r'
        self.user_field = None

        self.extension_serializers = []
        self.inlines = {}

        self.read_only_fields = []

        self.field_names = ['id']

        self.processed = False

    def set_descriptor(self, descriptor):
        self.descriptor = descriptor

        if descriptor != '_':
            self.serializer_name = f'{self.serializer_name}{descriptor.capitalize()}'

    def set_fields(self, fields):
        self.fields = fields
        self.fields_index = {f.name: f for f in fields}

    def add_auth_method(self, method, ref):
        if method == 'token':
            self.field_imports.append(('rest_framework.authentication', 'TokenAuthentication'))

            self.auth_method_classes.append(f'{self.serializer_name}TokenAuthentication')

            if ref:
                if ref[0] == '#':
                    ref = ref[1:]
                    ref_model = self.model.application.resolve_model(ref)

                    cls = ref_model.class_name
                    self.field_imports.append((f'{ref_model.application.app_name}.models', cls))
                else:
                    cls = ref
            else:
                raise ValidationException('@rest->auth->token require an argument)')

            self.auth_methods[method] = {'model': cls}

        if method == 'session':
            self.field_imports.append(('rest_framework.authentication', 'SessionAuthentication'))
            self.auth_methods[method] = {}
            self.auth_method_classes.append('SessionAuthentication')

        if method == 'basic':
            self.field_imports.append(('rest_framework.authentication', 'BasicAuthentication'))
            self.auth_methods[method] = {}
            self.auth_method_classes.append('BasicAuthentication')

        self.field_imports.append(('rest_framework.permissions', 'IsAuthenticated'))

    def post_process(self):
        if self.processed:
            raise Exception('Already processed!')

        self.processed = True

        if len(self.auth_method_classes) == 0:
            self.field_imports.append(('rest_framework.permissions', 'AllowAny'))

        for config in self.extension_serializers:
            config.post_process()

        for field in self.fields:
            if self.parent_field and hasattr(self.parent_field,
                                             'source_field_name') and field.name == self.parent_field.source_field_name:
                continue
            if self.user_field and field.name == self.user_field:
                continue

            self.field_names.append(field.name)

            if field.name not in self.inlines:
                rest_field = field.get_rest_field()

                if rest_field:
                    for line in rest_field.import_def:
                        self.field_imports.append(line)
                    self.field_declarations.append((field.name, rest_field.declaration))

        if self.str:
            self.field_names.append('__str__')
            self.read_only_fields.append('__str__')

    @property
    def descriptor_suffix(self):
        if self.descriptor == '_':
            return ''
        return '_' + self.descriptor

    @property
    def rest_class(self):
        if self.rest_mode == 'rw':
            return 'rest_framework.viewsets', 'ModelViewSet'
        elif self.rest_mode == 'w':
            return 'cratis_api.views', 'WriteOnlyModelViewSet'
        else:
            return 'rest_framework.viewsets', 'ReadOnlyModelViewSet'

    @property
    def is_writable(self):
        return 'w' in self.rest_mode

    @property
    def is_root(self):
        return self.parent_field is None

    def configure_imports(self, imports):

        imports.add(*self.rest_class)

        imports.add('.serializers', f'{self.serializer_name}Serializer')
        imports.add(f'{self.model.application.app_name}.models', self.model.class_name)

        for import_line in self.field_imports:
            imports.add(*import_line)

        for conf in self.extension_serializers:
            conf.configure_imports(imports)

    def configure_model_imports(self, imports):

        if self.model:
            imports.add(f'{self.model.application.app_name}.models', self.model.class_name)

        for conf in self.extension_serializers:
            conf.configure_model_imports(imports)

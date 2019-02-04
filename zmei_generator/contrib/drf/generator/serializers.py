import os

from zmei_generator.contrib.drf.extensions.model.api import ApiModelExtension
from zmei_generator.contrib.drf.extensions.model.rest import RestModelExtension
from zmei_generator.generator.imports import ImportSet
from zmei_generator.generator.utils import generate_file, package_to_path, generate_package


def generate(target_path, project):
    has_api = False

    for application in project.applications.values():
        if not application.models_support(ApiModelExtension) and not application.models_support(RestModelExtension):
            continue

        app_name = application.app_name

        has_api = True
        imports = ImportSet()
        imports.add('rest_framework', 'serializers')

        for model in application.models_with(RestModelExtension):
            for name, rest_conf in model[RestModelExtension].rest_conf.items():
                rest_conf.configure_model_imports(imports)

        generate_file(target_path, '{}/serializers.py'.format(app_name), 'serializers.py.tpl', {
            'imports': imports.import_sting(),
            'application': application,
            'rest_ext':  RestModelExtension,
            'api_ext':  ApiModelExtension,
            'models': [(model.ref, model) for model in application.models_with(RestModelExtension)],
        })

        url_imports = ImportSet()
        url_imports.add('django.conf.urls', 'url')
        url_imports.add('django.conf.urls', 'include')
        url_imports.add('rest_framework', 'routers')

        for model in application.models_with(RestModelExtension):
            for rest_conf in model[RestModelExtension].published_apis.values():
                url_imports.add('.views_rest', f'{rest_conf.serializer_name}ViewSet')

        context = {
            'package_name': app_name,
            'application': application,
            'ext': RestModelExtension,
            'url_imports': url_imports.import_sting(),
        }
        filepath = os.path.join(package_to_path(app_name), 'urls_rest.py')
        generate_file(target_path, filepath, 'urls_rest.py.tpl', context)

        # views_rest.py

        imports = ImportSet()

        for model in application.models_with(RestModelExtension):
            for name, rest_conf in model[RestModelExtension].rest_conf.items():
                rest_conf.configure_imports(imports)


        generate_file(target_path, f'{app_name}/views_rest.py', 'views_rest.py.tpl', {
            'package_name': app_name,
            'application': application,
            'ext': RestModelExtension,
            'models': [(name, model) for name, model in application.models.items() if model.supports(RestModelExtension)],
            'imports': imports
        })

    has_pages = False
    for application in project.applications.values():
        if len(application.pages):
            has_pages = True

    if has_api or has_pages:
        generate_package('app.utils', path=target_path)
        generate_file(target_path, 'app/utils/rest.py', template_name='rest.utils.py.tpl')
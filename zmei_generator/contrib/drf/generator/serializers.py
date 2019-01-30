import os

from zmei_generator.contrib.drf.extensions.model.api import ApiModelExtension
from zmei_generator.contrib.drf.extensions.model.rest import RestModelExtension
from zmei_generator.generator.imports import ImportSet
from zmei_generator.generator.utils import generate_file, package_to_path


def generate(target_path, project):
    for app_name, application in project.applications_with(ApiModelExtension):
        imports = ImportSet()
        imports.add('rest_framework', 'serializers')

        for model in application.models_with(RestModelExtension):
            for name, rest_conf in model[RestModelExtension].rest_conf.items():
                rest_conf.configure_model_imports(imports)

        generate_file(target_path, '{}/serializers.py'.format(app_name), 'serializers.py.tpl', {
            'imports': imports.import_sting(),
            'application': application,
            'models': [(name, model) for name, model in application.models_with(RestModelExtension)],
        })

        url_imports = ImportSet()
        url_imports.add('django.conf.urls', 'url')
        url_imports.add('django.conf.urls', 'include')
        url_imports.add('rest_framework', 'routers')

        for name, model in application.models_with(ApiModelExtension):
            for rest_conf in model[ApiModelExtension].published_apis.values():
                url_imports.add('.views', f'{rest_conf.serializer_name}ViewSet')

        context = {
            'package_name': app_name,
            'application': application,
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

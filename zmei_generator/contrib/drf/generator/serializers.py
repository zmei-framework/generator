import os

from zmei_generator.generator.imports import ImportSet
from zmei_generator.generator.utils import generate_file, package_to_path


def generate(target_path, project):
    for app_name, application in project.applications.items():
        if not application.api:
            continue

        imports = ImportSet()
        imports.add('rest_framework', 'serializers')

        for col in application.models.values():
            if col.rest:
                for name, rest_conf in col.rest_conf.items():
                    rest_conf.configure_model_imports(imports)

        generate_file(target_path, '{}/serializers.py'.format(app_name), 'serializers.py.tpl', {
            'imports': imports.import_sting(),
            'application': application,
            'models': [(name, col) for name, col in application.models.items() if col.rest],
        })

        url_imports = ImportSet()
        url_imports.add('django.conf.urls', 'url')
        url_imports.add('django.conf.urls', 'include')
        url_imports.add('rest_framework', 'routers')

        for name, model in application.models.items():
            if model.api:
                for rest_conf in model.published_apis.values():
                    url_imports.add('.views', f'{rest_conf.serializer_name}ViewSet')

        context = {
            'package_name': app_name,
            'application': application,
            'url_imports': url_imports.import_sting(),
        }

        filepath = os.path.join(package_to_path(app_name), 'urls_rest.py')
        generate_file(target_path, filepath, 'urls_rest.py.tpl', context)


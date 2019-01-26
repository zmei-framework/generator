from zmei_generator.generator.imports import ImportSet
from zmei_generator.generator.utils import generate_file


def generate(target_path, app):
    for app_name, application in app.applications.items():

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

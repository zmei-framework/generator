from zmei_generator.generator.imports import ImportSet
from zmei_generator.generator.utils import generate_file


def generate(target_path, app):
    for app_name, collection_set in app.collection_sets.items():

        imports = ImportSet()
        imports.add('rest_framework', 'serializers')

        for col in collection_set.collections.values():
            if col.rest:
                for name, rest_conf in col.rest_conf.items():
                    rest_conf.configure_model_imports(imports)

        generate_file(target_path, '{}/serializers.py'.format(app_name), 'serializers.py.tpl', {
            'imports': imports.import_sting(),
            'collection_set': collection_set,
            'collections': [(name, col) for name, col in collection_set.collections.items() if col.rest],
        })

from zmei_generator.generator.imports import ImportSet
from zmei_generator.generator.utils import generate_file


def generate(target_path, app):
    for app_name, collection_set in app.collection_sets.items():
        imports = ImportSet()
        imports.add('modeltranslation.translator', 'translator')
        imports.add('modeltranslation.translator', 'TranslationOptions')

        for col in collection_set.collections.values():
            if not col.translatable:
                continue

            imports.add('{}.models'.format(app_name), col.class_name)

        generate_file(target_path, '{}/translation.py'.format(app_name), 'translation.py.tpl', {
            'imports': imports.import_sting(),
            'collections': [(name, col) for name, col in collection_set.collections.items() if col.translatable]
        })

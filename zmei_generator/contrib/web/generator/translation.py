


def generate_translation_py(target_path, app_name, collection_set):
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

from zmei_generator.generator.imports import ImportSet
from zmei_generator.generator.utils import generate_file


def generate(target_path, project):
    for app_name, application in project.applications.items():
        has_i18n = any([x.translatable for x in application.models.values()])
        if not has_i18n:
            continue

        imports = ImportSet()
        imports.add('modeltranslation.translator', 'translator')
        imports.add('modeltranslation.translator', 'TranslationOptions')

        for col in application.models.values():
            if not col.translatable:
                continue

            imports.add('{}.models'.format(app_name), col.class_name)

        generate_file(target_path, '{}/translation.py'.format(app_name), 'translation.py.tpl', {
            'imports': imports.import_sting(),
            'models': [(name, col) for name, col in application.models.items() if col.translatable]
        })

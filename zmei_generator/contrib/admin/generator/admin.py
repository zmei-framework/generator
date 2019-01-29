from zmei_generator.contrib.admin.extensions.model.admin import AdminModelExtension
from zmei_generator.generator.imports import ImportSet
from zmei_generator.generator.utils import generate_file


def generate(target_path, project):
    for app_name, application in project.applications.items():

        if not application.models_support(AdminModelExtension):
            continue

        imports = ImportSet()
        imports.add('django.contrib', 'admin')
        imports.add('django', 'forms')

        for model in application.models_with(AdminModelExtension):
            imports.add('{}.models'.format(app_name), model.class_name)

            for class_import in model[AdminModelExtension].classes:
                imports.add(*class_import)

            if model.polymorphic:
                for child in model.child_models:
                    imports.add('{}.models'.format(app_name), child.class_name)

            # inlines
            for inline in model[AdminModelExtension].inlines:
                for declaration in inline.type_declarations:
                    imports.add(*declaration)

                if inline.inline_type == 'polymorphic':
                    for target_model in inline.target_model.child_models:

                        if target_model.translatable:
                            imports.add('cratis_i18n.admin', 'TranslatableInlineModelAdmin')

                        imports.add('{}.models'.format(app_name), target_model.class_name)

                imports.add('{}.models'.format(app_name), inline.target_model.class_name)

            for field in model.fields.values():
                if field.get_admin_widget():
                    import_data, model_field = field.get_admin_widget()

                    for source, what in import_data:
                        imports.add(source, what)

        generate_file(target_path, '{}/admin.py'.format(app_name), 'admin.py.tpl', {
            'imports': imports.import_sting(),
            'ext': AdminModelExtension,
            'application': application,
            'models': [(name, model) for name, model in application.models.items() if model.supports(AdminModelExtension)]
        })


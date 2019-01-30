from zmei_generator.domain.model_def import ModelDef
from zmei_generator.domain.application_def import FieldDeclaration
from zmei_generator.domain.field_def import FieldDef
from zmei_generator.generator.imports import ImportSet
from zmei_generator.generator.utils import generate_file


def generate(target_path, project):
    for app_name, application in project.applications.items():
        if not len(application.models):
            continue

        imports = ImportSet()
        imports.add('django.db', 'models')

        for model in application.models.values():  # type: ModelDef

            for handlers, code in model.signal_handlers:
                for signal_import in handlers:
                    imports.add('django.dispatch', 'receiver')
                    imports.add(*signal_import)

            if model.polymorphic and model.tree:
                imports.add('polymorphic_tree.models', 'PolymorphicMPTTModel', 'PolymorphicTreeForeignKey')
            else:
                if model.polymorphic:
                    imports.add('polymorphic.models', 'PolymorphicModel')

                if model.tree:
                    imports.add('mptt.models', 'MPTTModel', 'TreeForeignKey')

            if model.validators:
                imports.add('django.core.exceptions', 'ValidationError')

            if model.mixin_classes:
                for import_decl in model.mixin_classes:
                    pkg, cls, alias = import_decl
                    if alias != cls:
                        cls = '{} as {}'.format(cls, alias)
                    imports.add(*(pkg, cls))

            for field in model.own_fields:  # type: FieldDef
                model_field = field.get_model_field()
                if model_field:
                    import_data, model_field = model_field  # type: FieldDeclaration

                    for source, what in import_data:
                        imports.add(source, what)

        generate_file(target_path, '{}/models.py'.format(app_name), 'models.py.tpl', {
            'imports': imports.import_sting(),
            'application': application,
            'models': application.models.items()
        })

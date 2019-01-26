from zmei_generator.domain.application_def import FieldDeclaration
from zmei_generator.domain.field_def import FieldDef
from zmei_generator.generator.utils import gen_args


class ImageFieldDef(FieldDef):
    def get_model_field(self):
        args = self.prepare_field_arguemnts({
            'upload_to': self.options or f'image_upload/{self.model.ref}/{self.name}',
        })

        return FieldDeclaration(
            [('django.db', 'models')],
            'models.ImageField({})'.format(gen_args(args))
        )

    def get_required_deps(self):
        return ['Pillow']


class SimpleFieldDef(FieldDef):
    def get_model_field(self):
        args = self.prepare_field_arguemnts({
            'upload_to': self.options or f'image_upload/{self.model.ref}/{self.name}',
        })

        return FieldDeclaration(
            [('django.db', 'models')],
            'models.FileField({})'.format(gen_args(args))
        )


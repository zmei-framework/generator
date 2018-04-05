from cratis_generator.config.domain import FieldDef, FieldDeclaration
from cratis_generator.generator.utils import gen_args


class ImageFieldDef(FieldDef):
    def get_model_field(self, collection):
        args = self.prepare_field_arguemnts({
            'upload_to': self.options or f'image_upload/{self.collection.ref}/{self.name}',
        })

        return FieldDeclaration(
            [('django.db', 'models')],
            'models.ImageField({})'.format(gen_args(args))
        )

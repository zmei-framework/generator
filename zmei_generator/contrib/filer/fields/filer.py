from zmei_generator.domain.application_def import FieldDeclaration
from zmei_generator.parser.errors import GlobalScopeValidationError as ValidationException
from zmei_generator.domain.field_def import FieldDef
from zmei_generator.generator.utils import gen_args


class FilerFileFieldDef(FieldDef):

    """
    Image field

    """

    sizes = None

    def get_model_field(self):
        args = self.prepare_field_arguemnts({
            'related_name': '+'
        })

        return FieldDeclaration(
            [('filer.fields.file', 'FilerFileField')],
            'FilerFileField(on_delete=models.SET_NULL, {})'.format(gen_args(args))
        )

    def get_rest_field(self):
        return FieldDeclaration(
            [
                ('cratis_filer.serializers', 'FileSerializer')
             ],
            'FileSerializer()'
        )


class FilerFileFolderDef(FilerFileFieldDef):

    """
    Image field

    """

    def get_model_field(self):
        args = self.prepare_field_arguemnts({
            'related_name': '+'
        })

        return FieldDeclaration(
            [('filer.fields.folder', 'FilerFolderField')],
            'FilerFolderField(on_delete=models.SET_NULL, {})'.format(gen_args(args))
        )

    # def get_rest_field(self):
    #     return FieldDeclaration(
    #         [
    #             ('cratis_filer.serializers', 'FileSerializer')
    #          ],
    #         'FileSerializer()'
    #     )


class ImageSize(object):
    name = None
    width = None
    height = None
    filters = None


class FilerImageFieldDef(FilerFileFieldDef):

    """
    Image field

    """

    sizes = None

    def get_model_field(self):
        args = self.prepare_field_arguemnts({
            'related_name': '+'
        })

        return FieldDeclaration(
            [('filer.fields.image', 'FilerImageField')],
            'FilerImageField(on_delete=models.SET_NULL, {})'.format(gen_args(args))
        )

    def get_rest_field(self):
        sizes_prepared = []

        for size in self.sizes:

            filters = []

            for filter in size.filters:
                if filter.name not in ('crop', 'upscale'):
                    raise ValidationException('Unknown image filter: {}'.format(filter.name))
                filters.append(filter.name)

                sizes_prepared.append('"{}": Size({}, {}, crop={}, upscale={})'.format(
                size.name, size.width, size.height, 'crop' in filters, 'upscale' in filters
            ))

        sizes_prepared = '{\n%s\n}' % (', \n'.join(sizes_prepared))

        return FieldDeclaration(
            [
                ('cratis_filer.serializers', 'ThumbnailImageField'),
                ('cratis_filer.utils', 'Size')
             ],
            'ThumbnailImageField({})'.format(sizes_prepared)
        )

    @property
    def admin_list_renderer(self):
        return """
        from cratis_filer.serializers import ThumbnailImageField
        from cratis_filer.utils import Size
        try:
            return '<img src="{}" style="width: 60px; height: 60px;" />'.format(ThumbnailImageField({'thumb': Size(60, 60)}).to_representation(obj.%s)['thumb']['url'])
        except KeyError as e:
            return '-'
        """ % self.name


class FilerImageFolderFieldDef(FilerImageFieldDef):

    def get_model_field(self):
        args = self.prepare_field_arguemnts({
            'related_name': '+'
        })

        return FieldDeclaration(
            [('filer.fields.folder', 'FilerFolderField')],
            'FilerFolderField(on_delete=models.SET_NULL, {})'.format(gen_args(args))
        )

    def get_rest_field(self):
        args = self.prepare_field_arguemnts()

        return FieldDeclaration(
            [
                ('cratis_filer.serializers', 'ImageFolderSerializer'),
                ('cratis_filer.utils', 'Size')
             ],
            'ImageFolderSerializer({}, {})'.format(self.sizes, gen_args(args))
        )






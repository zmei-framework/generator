from cratis_generator.config.domain import FieldDef, FieldDeclaration, ValidationException, CollectionDef
from cratis_generator.config.grammar import identifier
from cratis_generator.generator.utils import gen_args

from cPyparsing import *


class FilerFileFieldDef(FieldDef):

    """
    Image field

    """

    sizes = None

    def get_model_field(self, collection):
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

class FilerFileFolderDef(FieldDef):

    """
    Image field

    """

    def get_model_field(self, collection):
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




class FilerImageFieldDef(FieldDef):

    """
    Image field

    """

    sizes = None

    def parse_options(self):

        filter = Group(Suppress('|') + identifier.setResultsName('name'))

        size_grammar = Group(identifier.setResultsName('name') + Suppress(':') + \
                          Word(nums).setResultsName('width') + Suppress('x') + \
                          Word(nums).setResultsName('height') + Group(ZeroOrMore(filter)).setResultsName('filters'))

        options_grammar = delimitedList(size_grammar).setResultsName('sizes') + stringEnd

        sizes = []

        if self.options and self.options != '':
            for size in options_grammar.parseString(self.options).sizes:

                filters = []

                for filter in size.filters:
                    if filter.name not in ('crop', 'upscale'):
                        raise ValidationException('Unknown image filter: {}'.format(filter.name))
                    filters.append(filter.name)

                sizes.append('"{}": Size({}, {}, crop={}, upscale={})'.format(
                    size.name, size.width, size.height, 'crop' in filters, 'upscale' in filters
                ))

            self.sizes = '{\n%s\n}' % (', \n'.join(sizes))


    def get_model_field(self, collection):
        args = self.prepare_field_arguemnts({
            'related_name': '+'
        })

        return FieldDeclaration(
            [('filer.fields.image', 'FilerImageField')],
            'FilerImageField(on_delete=models.SET_NULL, {})'.format(gen_args(args))
        )

    def get_rest_field(self):
        return FieldDeclaration(
            [
                ('cratis_filer.serializers', 'ThumbnailImageField'),
                ('cratis_filer.utils', 'Size')
             ],
            'ThumbnailImageField({})'.format(self.sizes)
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

    def get_model_field(self, collection):
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






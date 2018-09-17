from textwrap import dedent

from zmei_generator.fields.date import DateFieldDef, DateTimeFieldDef, AutoNowDateTimeFieldDef, \
    AutoNowAddDateTimeFieldDef
from zmei_generator.fields.filer import FilerImageFieldDef, FilerFileFieldDef, FilerFileFolderDef, \
    FilerImageFolderFieldDef
from zmei_generator.fields.image import ImageFieldDef, SimpleFieldDef
from zmei_generator.fields.number import IntegerFieldDef, FloatFieldDef, DecimalFieldDef
from zmei_generator.parser.parser import parse_string
from zmei_generator.parser.populate import populate_collection_set


def _(code):
    tree = parse_string(dedent(code))

    return populate_collection_set(tree, 'example')


def test_image_file_field():
    cs = _("""

        #boo
        ----------
        a: image_file
    """)

    a = cs.collections['boo'].fields['a']

    assert isinstance(a, ImageFieldDef)


def test_image_field():
    cs = _("""

        #boo
        ----------
        a: image(default=300x300|crop|upscale, foo=1024x600|crop)
    """)

    a = cs.collections['boo'].fields['a']

    assert isinstance(a, FilerImageFieldDef)
    assert len(a.sizes) == 2

    assert a.sizes[0].width == 300
    assert a.sizes[0].height == 300
    assert a.sizes[0].filters == ['crop', 'upscale']

    assert a.sizes[1].width == 1024
    assert a.sizes[1].height == 600
    assert a.sizes[1].filters == ['crop']


def test_filer_image_field():
    cs = _("""

        #boo
        ----------
        a: filer_image
    """)

    a = cs.collections['boo'].fields['a']

    assert isinstance(a, FilerImageFieldDef)


def test_filer_file_field():
    cs = _("""

        #boo
        ----------
        a: filer_file
    """)

    a = cs.collections['boo'].fields['a']

    assert isinstance(a, FilerFileFieldDef)


def test_file_field():
    cs = _("""

        #boo
        ----------
        a: file
    """)

    a = cs.collections['boo'].fields['a']

    assert isinstance(a, FilerFileFieldDef)


def test_simple_file_field():
    cs = _("""

        #boo
        ----------
        a: simple_file
    """)

    a = cs.collections['boo'].fields['a']

    assert isinstance(a, SimpleFieldDef)


def test_folder_field():
    cs = _("""

        #boo
        ----------
        a: folder
    """)

    a = cs.collections['boo'].fields['a']

    assert isinstance(a, FilerFileFolderDef)


def test_image_folder_field():
    cs = _("""

        #boo
        ----------
        a: image_folder(default=300x300|crop|upscale, foo=1024x600|crop)
    """)

    a = cs.collections['boo'].fields['a']

    assert isinstance(a, FilerImageFolderFieldDef)
    assert len(a.sizes) == 2

    assert a.sizes[0].width == 300
    assert a.sizes[0].height == 300
    assert a.sizes[0].filters == ['crop', 'upscale']

    assert a.sizes[1].width == 1024
    assert a.sizes[1].height == 600
    assert a.sizes[1].filters == ['crop']


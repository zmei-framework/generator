from textwrap import dedent

from zmei_generator.contrib.filer.fields.filer import FilerImageFieldDef, FilerFileFieldDef, FilerFileFolderDef, \
    FilerImageFolderFieldDef
from zmei_generator.contrib.web.fields.image import SimpleFieldDef, ImageFieldDef
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_image_field():
    app = _("""

        #boo
        ----------
        a: image(default=300x300|crop|upscale, foo=1024x600|crop)
    """)

    a = app.models['boo'].fields['a']

    assert isinstance(a, ImageFieldDef)
    assert len(a.sizes) == 2

    assert a.sizes[0].width == 300
    assert a.sizes[0].height == 300
    assert a.sizes[0].filters == ['crop', 'upscale']

    assert a.sizes[1].width == 1024
    assert a.sizes[1].height == 600
    assert a.sizes[1].filters == ['crop']


def test_filer_image_field():
    app = _("""

        #boo
        ----------
        a: filer_image
    """)

    a = app.models['boo'].fields['a']

    assert isinstance(a, FilerImageFieldDef)


def test_filer_file_field():
    app = _("""

        #boo
        ----------
        a: filer_file
    """)

    a = app.models['boo'].fields['a']

    assert isinstance(a, FilerFileFieldDef)


def test_file_field():
    app = _("""

        #boo
        ----------
        a: file
    """)

    a = app.models['boo'].fields['a']

    assert isinstance(a, SimpleFieldDef)


def test_folder_field():
    app = _("""

        #boo
        ----------
        a: filer_folder
    """)

    a = app.models['boo'].fields['a']

    assert isinstance(a, FilerFileFolderDef)


def test_image_folder_field():
    app = _("""

        #boo
        ----------
        a: filer_image_folder(default=300x300|crop|upscale, foo=1024x600|crop)
    """)

    a = app.models['boo'].fields['a']

    assert isinstance(a, FilerImageFolderFieldDef)
    assert len(a.sizes) == 2

    assert a.sizes[0].width == 300
    assert a.sizes[0].height == 300
    assert a.sizes[0].filters == ['crop', 'upscale']

    assert a.sizes[1].width == 1024
    assert a.sizes[1].height == 600
    assert a.sizes[1].filters == ['crop']


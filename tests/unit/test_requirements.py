from textwrap import dedent

import pytest

from zmei_generator.parser.errors import LangsRequiredValidationError
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_polymorphic():
    app = _("""
    
        #boo
        ----------
        a
    
        #boo->foo
        ----------
        b
    
    """)

    assert 'django-polymorphic' in app.get_required_deps()
    assert 'polymorphic' in app.get_required_apps()


def test_i18n():
    app = _("""
        @langs(en)
    
        #boo
        ----------
        $a
    
    """)

    assert app.translatable is True

    print(app.get_required_deps())

    assert 'django-modeltranslation==0.13-beta1' in app.get_required_deps()
    assert 'modeltranslation' in app.get_required_apps()


def test_i18n_no_annot():
    with pytest.raises(LangsRequiredValidationError):
        _("""
            #boo
            -----
            $a
        """)

#
# def test_filer():
#     app = _("""
#
#         @filer
#
#     """)
#
#     assert 'django-filer' in app.get_required_deps()
#     assert 'filer' in app.get_required_apps()
#     assert 'easy_thumbnails' in app.get_required_apps()
#     assert 'mptt' in app.get_required_apps()

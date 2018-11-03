from textwrap import dedent

import pytest

from zmei_generator.extras.model.admin import AdminExtra, AdminInlineConfig
from zmei_generator.parser.errors import LangsRequiredValidationError
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_polymorphic():
    cs = _("""
    
        #boo
        ----------
        a
    
        #boo->foo
        ----------
        b
    
    """)

    assert 'django-polymorphic' in cs.get_required_deps()
    assert 'polymorphic' in cs.get_required_apps()


def test_i18n():
    cs = _("""
        @langs(en)
    
        #boo
        ----------
        $a
    
    """)

    assert cs.translatable is True

    print(cs.get_required_deps())

    assert 'django-modeltranslation==0.13-beta1' in cs.get_required_deps()
    assert 'modeltranslation' in cs.get_required_apps()


def test_i18n_no_annot():
    with pytest.raises(LangsRequiredValidationError):
        _("""
            #boo
            -----
            $a
        """)

#
# def test_filer():
#     cs = _("""
#
#         @filer
#
#     """)
#
#     assert 'django-filer' in cs.get_required_deps()
#     assert 'filer' in cs.get_required_apps()
#     assert 'easy_thumbnails' in cs.get_required_apps()
#     assert 'mptt' in cs.get_required_apps()

from textwrap import dedent

from zmei_generator.contrib.admin.extensions.model.admin import AdminModelExtension
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_admin_simple():
    app = _("""
    
        #boo
        ----------
        abc
        cda
        
        @admin
    
    """)

    boo = app.models['boo']

    assert boo[AdminModelExtension].class_declaration == 'ModelAdmin'


def test_admin_i18n():
    app = _("""
        @langs(en)
        
        #boo
        ----------
        $abc
        cda
        
        @admin
    
    """)

    boo = app.models['boo']

    assert boo[AdminModelExtension].class_declaration == 'TabbedTranslationAdmin'


def test_admin_poly():
    app = _("""

        #boo
        ----------
        a

        @admin
        
        #boo->foo1
        -----------
        b
        @admin

    """)

    boo = app.models['boo']
    foo1 = app.models['foo1']

    assert boo[AdminModelExtension].class_declaration == 'PolymorphicParentModelAdmin'

    assert foo1[AdminModelExtension].class_declaration == 'PolymorphicChildModelAdmin'


def test_admin_poly__non_poly_child():
    app = _("""

        #boo
        ----------
        a

        @admin

        #boo->foo1
        -----------
        b

    """)

    boo = app.models['boo']
    foo1 = app.models['foo1']

    assert boo[AdminModelExtension].class_declaration == 'ModelAdmin'

    assert not foo1.supports(AdminModelExtension)


def test_admin_poly_inline():
    app = _("""
    
        #zoo
        ------
        z
        
        @admin(
            inline: boos(type: polymorphic)
        )

        #boo
        ----------
        a: one(#zoo -> boos)

        #boo->foo1
        -----------
        b

    """)

    zoo = app.models['zoo']

    assert zoo[AdminModelExtension].class_declaration == \
        'PolymorphicInlineSupportMixin, ModelAdmin'

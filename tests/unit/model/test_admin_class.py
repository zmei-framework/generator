from textwrap import dedent

from zmei_generator.extras.model.admin import AdminExtra, AdminInlineConfig
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_admin_simple():
    cs = _("""
    
        #boo
        ----------
        abc
        cda
        
        @admin
    
    """)

    boo = cs.collections['boo']

    assert boo.admin.class_declaration == 'ModelAdmin'


def test_admin_i18n():
    cs = _("""
        @langs(en)
        
        #boo
        ----------
        $abc
        cda
        
        @admin
    
    """)

    boo = cs.collections['boo']

    assert boo.admin.class_declaration == 'TabbedTranslationAdmin'


def test_admin_poly():
    cs = _("""

        #boo
        ----------
        a

        @admin
        
        #boo->foo1
        -----------
        b
        @admin

    """)

    boo = cs.collections['boo']
    foo1 = cs.collections['foo1']

    assert boo.admin.class_declaration == 'PolymorphicParentModelAdmin'

    assert foo1.admin.class_declaration == 'PolymorphicChildModelAdmin'


def test_admin_poly__non_poly_child():
    cs = _("""

        #boo
        ----------
        a

        @admin

        #boo->foo1
        -----------
        b

    """)

    boo = cs.collections['boo']
    foo1 = cs.collections['foo1']

    assert boo.admin.class_declaration == 'ModelAdmin'

    assert foo1.admin is None


def test_admin_poly_inline():
    cs = _("""
    
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

    zoo = cs.collections['zoo']

    assert zoo.admin.class_declaration == \
        'PolymorphicInlineSupportMixin, ModelAdmin'

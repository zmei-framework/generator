from textwrap import dedent

from zmei_generator.contrib.web.extensions.page.block import BlockPlaceholder, InlineTemplatePageBlock
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_page_priority_default():
    app = _("""

        [boo]
        @markdown {
            # test
        }
        @@
        @markdown {
            # cats
        }
        
        #foo
        ------
        lala
    """)

    assert len(app.pages) == 1

    boo = app.pages['boo']

    assert boo.name == 'boo'
    assert len(boo.blocks['content']) == 3
    assert boo.blocks['content'][0].context['content'] == "<h1>test</h1>"
    assert isinstance(boo.blocks['content'][1], BlockPlaceholder)
    assert boo.blocks['content'][2].context['content'] == "<h1>cats</h1>"

    boo.add_block('content', InlineTemplatePageBlock(template_name='lala.html', context={'content': 'lala'}, ref='hoho'))

    assert len(boo.blocks['content']) == 4
    assert boo.blocks['content'][0].context['content'] == "<h1>test</h1>"
    assert isinstance(boo.blocks['content'][1], BlockPlaceholder)
    assert boo.blocks['content'][2].context['content'] == "<h1>cats</h1>"
    assert isinstance(boo.blocks['content'][3], InlineTemplatePageBlock)
    assert boo.blocks['content'][3].context['content'] == 'lala'
    assert boo.blocks['content'][3].ref == 'hoho'


def test_page_priority_before_after():
    app = _("""

        [boo]
        @markdown {
            # test
        }
        @@
        @markdown {
            # cats
        }
        
        #foo
        ------
        lala
    """)

    assert len(app.pages) == 1

    boo = app.pages['boo']

    assert boo.name == 'boo'
    assert len(boo.blocks['content']) == 3
    assert boo.blocks['content'][0].context['content'] == "<h1>test</h1>"
    assert isinstance(boo.blocks['content'][1], BlockPlaceholder)
    assert boo.blocks['content'][2].context['content'] == "<h1>cats</h1>"

    boo.add_block('content', InlineTemplatePageBlock(template_name='lala.html', context={'content': 'lala'}), append=True)

    assert len(boo.blocks['content']) == 4
    assert boo.blocks['content'][0].context['content'] == "<h1>test</h1>"
    assert isinstance(boo.blocks['content'][1], InlineTemplatePageBlock)
    assert boo.blocks['content'][1].context['content'] == 'lala'
    assert isinstance(boo.blocks['content'][2], BlockPlaceholder)
    assert boo.blocks['content'][3].context['content'] == "<h1>cats</h1>"



def test_page_priority_markdown_and_crud():
    app = _("""

        [boo: /]
        @markdown {
            # test
        }
        @crud_detail(#foo)
        
        #foo
        ------
        lala
    """)

    assert len(app.pages) == 1

    boo = app.pages['boo']

    assert isinstance(boo.blocks['content'][0], InlineTemplatePageBlock)

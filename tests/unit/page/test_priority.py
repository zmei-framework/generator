from textwrap import dedent

import pytest
from zmei_generator.extras.page.block import BlockPlaceholder, PageBlock, ReactPageBlock
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_page_priority_default():
    cs = _("""

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

    assert len(cs.pages) == 1

    boo = cs.pages['boo']

    assert boo.name == 'boo'
    assert len(boo.blocks['content']) == 3
    assert boo.blocks['content'][0].source == "<h1>test</h1>"
    assert isinstance(boo.blocks['content'][1], BlockPlaceholder)
    assert boo.blocks['content'][2].source == "<h1>cats</h1>"

    boo.add_block('content', PageBlock(source='lala'))

    assert len(boo.blocks['content']) == 4
    assert boo.blocks['content'][0].source == "<h1>test</h1>"
    assert isinstance(boo.blocks['content'][1], BlockPlaceholder)
    assert boo.blocks['content'][2].source == "<h1>cats</h1>"
    assert isinstance(boo.blocks['content'][3], PageBlock)
    assert boo.blocks['content'][3].source == 'lala'


def test_page_priority_before_after():
    cs = _("""

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

    assert len(cs.pages) == 1

    boo = cs.pages['boo']

    assert boo.name == 'boo'
    assert len(boo.blocks['content']) == 3
    assert boo.blocks['content'][0].source == "<h1>test</h1>"
    assert isinstance(boo.blocks['content'][1], BlockPlaceholder)
    assert boo.blocks['content'][2].source == "<h1>cats</h1>"

    boo.add_block('content', PageBlock(source='lala'), append=True)

    assert len(boo.blocks['content']) == 4
    assert boo.blocks['content'][0].source == "<h1>test</h1>"
    assert isinstance(boo.blocks['content'][1], PageBlock)
    assert boo.blocks['content'][1].source == 'lala'
    assert isinstance(boo.blocks['content'][2], BlockPlaceholder)
    assert boo.blocks['content'][3].source == "<h1>cats</h1>"



def test_page_priority_markdown_and_crud():
    cs = _("""

        [boo: /]
        @markdown {
            # test
        }
        @crud_detail(#foo)
        
        #foo
        ------
        lala
    """)

    assert len(cs.pages) == 1

    boo = cs.pages['boo']

    assert isinstance(boo.blocks['content'][0], ReactPageBlock)

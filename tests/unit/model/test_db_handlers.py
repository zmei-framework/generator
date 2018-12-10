from textwrap import dedent

import pytest

from zmei_generator.extras.model.admin import AdminExtra, AdminInlineConfig
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')

@pytest.mark.skip
def test_db_handlers():
    cs = _("""
    
        #boo
        ----------
        abc
        cda
        
        @pre_save {
            lala + 1
        }
        
        @post_save {
            lala + 2
        }
        
        @pre_delete {
            lala + 3
        }
        
        @post_delete {
            lala + 4
        }
        
        @m2m_changed {
            lala + 5
        }
    
    """)

    boo = cs.collections['boo']

    assert boo.signal_handlers[0] == ([('django.db.models.signals', 'pre_save')], 'lala + 1')
    assert boo.signal_handlers[1] == ([('django.db.models.signals', 'post_save')], 'lala + 2')
    assert boo.signal_handlers[2] == ([('django.db.models.signals', 'pre_delete')], 'lala + 3')
    assert boo.signal_handlers[3] == ([('django.db.models.signals', 'post_delete')], 'lala + 4')
    assert boo.signal_handlers[4] == ([('django.db.models.signals', 'm2m_changed')], 'lala + 5')

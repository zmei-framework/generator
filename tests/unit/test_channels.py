from textwrap import dedent

import pytest
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_channels_enabled():
    cs = _("""

        @channels
    """)

    assert cs.channels is True


def test_channels_disabled():
    cs = _("""
    """)

    assert cs.channels is False


def test_channels_disabled_real_example():
    cs = _("""
        [index: /]
        messages:= Message.objects.all()
        
        @react_client{
            <Main>{
                messages.map((message) =>
                    <li key={message.id}>
                      {message.text}
                    </li>
                  )
            }</Main>
        }
        
        [messages: /messages]
        @crud(#message)
        
        #message
        -------
        text

    """)

    assert cs.channels is False
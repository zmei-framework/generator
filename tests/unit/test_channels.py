from textwrap import dedent

import pytest
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_channels_enabled():
    app = _("""

        @channels
    """)

    assert app.channels is True


def test_channels_disabled():
    app = _("""
    """)

    assert app.channels is False


def test_channels_disabled_real_example():
    app = _("""
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

    assert app.channels is False
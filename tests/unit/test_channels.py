from textwrap import dedent

import pytest

from zmei_generator.contrib.channels.extensions.application.channels import ChannelsAppExtension
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_channels_enabled():
    app = _("""

        @channels
    """)

    assert app.supports(ChannelsAppExtension)


def test_channels_disabled():
    app = _("""
    """)

    assert not app.supports(ChannelsAppExtension)


def test_channels_disabled_real_example():
    app = _("""
        [index: /]
        messages:= Message.objects.all()
        
        @react
        
        [messages: /messages]
        @crud(#message)
        
        #message
        -------
        text

    """)

    assert not app.supports(ChannelsAppExtension)
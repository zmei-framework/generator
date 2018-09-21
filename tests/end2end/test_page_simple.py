import os

import pytest
from django.http import HttpRequest


# @pytest.mark.skip
@pytest.mark.zmei('page1', """
[home]
message:= 'Hello'

""")
def test_simple_page():
    from page1.views import HomeView
    view = HomeView(request=HttpRequest(), kwargs={})

    data = view.get_context_data()

    assert data['message'] == 'Hello'

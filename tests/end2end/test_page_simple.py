import os

import pytest
from django.http import HttpRequest


# @pytest.mark.skip
@pytest.mark.zmei('page1', """
[home]
message:= 'Hello'

""")
def test_simple_page_no_url():
    from page1.views import Page1HomeView
    view = Page1HomeView(request=HttpRequest(), kwargs={})

    data = view.get_context_data()

    assert data['message'] == 'Hello'




@pytest.mark.zmei('page1', """
[home: /]
cnt := Foo.objects.count()

#foo
------
text

""")
@pytest.mark.zmei_before('migrate')
def test_page_with_model():
    from page1.views import Page1HomeView
    view = Page1HomeView(request=HttpRequest(), kwargs={})

    data = view.get_context_data()

    assert data['cnt'] == 0


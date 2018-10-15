import os

import pytest
from django.http import HttpRequest


# @pytest.mark.skip
@pytest.mark.zmei('page1', """
[home]
message:= 'Hello'

""")
def test_simple_page_no_url():
    from page1.views import HomeView
    view = HomeView(request=HttpRequest(), kwargs={})

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
def test_page_with_collection():
    from page1.views import HomeView
    view = HomeView(request=HttpRequest(), kwargs={})

    data = view.get_context_data()

    assert data['cnt'] == 0

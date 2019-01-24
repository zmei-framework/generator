# flake8: noqa

import sys
import pytest
from selenium import webdriver

if '--driver' in sys.argv:
    import chromedriver_binary
else:
    collect_ignore = ["tests/selenium"]  # pragma: no cover

@pytest.fixture
def chrome_options():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    return chrome_options
{% for config in gitlab.configs %}
# {{ config.hostname }}{% endfor %}

{%- if gitlab.test %}{% for config in gitlab.configs if config.coverage %}{% if loop.first %}
[![Coverage Status](https://{{ config.hostname }}/build/coverage-report/coverage.svg)](https://{{ config.hostname }}/build/coverage-report/index.html)
[![Style Status](https://{{ config.hostname }}/build/style-report/quality.svg)](https://{{ config.hostname }}/build/style-report/index.html)
{% endif %}{% endfor %}{% endif %}

## Dependencies

Install:

- redis
- mysql

## Start

`pip install -r requirements.dev.txt`

`python manage.py migrate`
`python manage.py runserver`

or

`zmei gen up`

{% if gitlab.test %}
## Test

Integration + unit tests:

`py.test`

All tests including selenium:

`y.test --driver Chrome`

Unit only:

`py.test tests/unit`

Integration only:

`py.test tests/integration`

Selenium only:

`py.test tests/selenium --driver Chrome`

{% endif %}
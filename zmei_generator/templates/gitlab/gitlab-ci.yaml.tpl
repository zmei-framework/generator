image: docker:latest


variables:
  APP_IMAGE: $CI_REGISTRY_IMAGE/app:$CI_COMMIT_REF_SLUG
  NGINX_IMAGE: $CI_REGISTRY_IMAGE/nginx:$CI_COMMIT_REF_SLUG

stages:
- test
- build
- delivery
- deploy

{% if gitlab.test %}
test_images:
  image: joyzoursky/python-chromedriver:3.6-xvfb-selenium
  stage: test
  {%- if gitlab.test.services %}
  services:{% for service in gitlab.test.services.values() %}{% if service.vars %}
  - alias: {{ service.name }}{% for key, val in service.vars.items() %}
    {% if key == 'image' %}name{% else %}{{ key }}{% endif %}: {{ val }}{% endfor %}
  {% else %}
  - {{ service.name }}{% endif %}{% endfor %}{% endif %}
  cache:
    paths:
    - .cache
  {%- if gitlab.test.vars %}
  variables:{% for key, val in gitlab.test.vars.items() %}
    {{ key }}: {{ val }}{% endfor %}{% endif %}
  script:
  - pip install -r requirements.dev.txt
  - xvfb-run --server-args="-screen 0 1024x768x24"
    py.test --cov . --cov-report html:coverage/ --driver Chrome
  - coverage-badge -o coverage/coverage.svg
  - flake8 --format=html --htmldir=flake/ || true
  - flake8 --format svg --image flake/quality.svg || true
  artifacts:
    paths:
    - coverage/
    - flake/
{% endif %}

{%- for config in gitlab.configs %}{% if config.deployment == 'dev' %}
build_dev_images:
  stage: build
  dependencies:
  - test_images
  script:
  - mkdir -p web/build/coverage-report/
  - mkdir -p web/build/style-report/
  - cp -rf coverage/* web/build/coverage-report/
  - cp -rf flake/* web/build/style-report/
  - docker login -u "$CI_REGISTRY_USER" -p "$CI_REGISTRY_PASSWORD" $CI_REGISTRY
  - docker build --target app -t "$APP_IMAGE" .
  - docker build --target nginx -t "$NGINX_IMAGE" .
  only:
  - {{ config.branch }}
{% endif %}{% endfor %}
build_prod_images:
  stage: build
  script:
  - docker login -u "$CI_REGISTRY_USER" -p "$CI_REGISTRY_PASSWORD" $CI_REGISTRY
  - docker build --target app -t "$APP_IMAGE" .
  - docker build --target nginx -t "$NGINX_IMAGE" .
  only:
  {%- for config in gitlab.configs %}{% if config.deployment != 'dev' and not config.manual_deploy %}
  - {{ config.branch }}
{% endif %}{%- endfor %}
push_images:
  stage: delivery
  script:
  - docker login -u "$CI_REGISTRY_USER" -p "$CI_REGISTRY_PASSWORD" $CI_REGISTRY
  - docker push "$APP_IMAGE"
  - docker push "$NGINX_IMAGE"
  only:
  {%- for config in gitlab.configs %}{% if not config.manual_deploy %}
  - {{ config.branch }}{% endif %}{%- endfor %}
{% for config in gitlab.configs %}
deploy_{{ config.deployment }}:
  stage: deploy
  variables:
    APP_HOSTNAME: {{ config.hostname }}
    APP_STACK_NAME: {{ config.deployment }}
  environment:
    name: {{ config.deployment }}
    url: https://{{ config.hostname }}
  script:
  - docker login -u "$CI_REGISTRY_USER" -p "$CI_REGISTRY_PASSWORD" $CI_REGISTRY
  {%- if config.vars.docker %}
  - export DOCKER_HOST={{ config.vars.docker }}
  {%- endif %}
  {%- if config.vars.key %}
  - export DOCKER_TLS_VERIFY="1"
  - export DOCKER_CERT_PATH="/root/.dockercerts"
  # extract certs (collected with "tar -czf - -C $DOCKER_CERT_PATH . |base64 |pbcopy")
  - mkdir -p $DOCKER_CERT_PATH; echo ${{ config.vars.key }} |base64 -d |tar xzf - -C $DOCKER_CERT_PATH
  {%- endif %}{% for key, val in config.vars.items() if key not in ('key', 'docker') %}
  - export {{ key }}={{ val }}{% endfor %}
  - docker stack deploy --compose-file docker-compose.yaml --with-registry-auth $APP_STACK_NAME
  {%- if config.manual_deploy %}
  when: manual
  {%- endif %}
  only:
  - {{ config.branch }}
{% endfor %}
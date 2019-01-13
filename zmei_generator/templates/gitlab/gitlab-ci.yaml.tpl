image: docker:latest

variables:
  APP_IMAGE: $CI_REGISTRY_IMAGE/app:$CI_COMMIT_REF_SLUG
  NGINX_IMAGE: $CI_REGISTRY_IMAGE/nginx:$CI_COMMIT_REF_SLUG

stages:
  - build
  - deploy

before_script:
  - docker login -u "$CI_REGISTRY_USER" -p "$CI_REGISTRY_PASSWORD" $CI_REGISTRY

build_images:
  stage: build
  script:
    - docker build --target app -t "$APP_IMAGE" .
    - docker push "$APP_IMAGE"
    - docker build --target nginx -t "$NGINX_IMAGE" .
    - docker push "$NGINX_IMAGE"
  only:
    {%- for config in gitlab.configs %}
    - {{ config.branch }}
    {%- endfor %}

{% for config in gitlab.configs %}
deploy_{{ config.deployment }}:
  stage: deploy
  variables:
    APP_HOSTNAME: {{ config.hostname }}
    APP_STACK_NAME: {{ config.deployment }}

  script:
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

    # deploy
    - echo "docker stack deploy --compose-file docker-compose.yaml --with-registry-auth $APP_STACK_NAME"
    - docker stack deploy --compose-file docker-compose.yaml --with-registry-auth $APP_STACK_NAME
  only:
    - {{ config.branch }}
{% endfor %}
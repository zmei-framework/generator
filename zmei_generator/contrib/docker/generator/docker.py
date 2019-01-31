import os
import random
import string

from zmei_generator.contrib.celery.extensions.application.celery import CeleryAppExtension
from zmei_generator.contrib.channels.extensions.application.channels import ChannelsAppExtension
from zmei_generator.contrib.docker.extensions.application.docker import DockerAppExtension
from zmei_generator.generator.application import ZmeiProject
from zmei_generator.generator.utils import generate_file


def generate(target_path, project: ZmeiProject):
    has_docker = any([app.supports(DockerAppExtension) for app in project.applications.values()])
    has_celery = any([app.supports(CeleryAppExtension) for app in project.applications.values()])
    has_channels = any([app.supports(ChannelsAppExtension) for app in project.applications.values()])

    if not has_docker:
        return

    context = {
        'req_file': os.environ.get('ZMEI_REQUIREMNETS_FILE', 'requirements.txt'),
        'has_channels': has_channels,
        'has_celery': has_celery,
        'admin_pass': ''.join(random.choice(
            string.ascii_letters + string.digits + string.punctuation.replace('"', '')) for _ in range(16)),
        'admin_user': 'admin-' + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(4)),
    }

    generate_file(target_path, 'requirements.prod.txt', 'docker/requirements.prod.txt.tpl', context)
    generate_file(target_path, 'app/settings_prod.py', 'docker/settings_prod.py.tpl', context)
    generate_file(target_path, 'Dockerfile', 'docker/dockerfile.tpl', context)
    generate_file(target_path, '.dockerignore', 'docker/dockerignore.tpl', context)
    generate_file(target_path, 'docker-compose.yaml', 'docker/docker-compose.yaml.tpl', context)
    generate_file(target_path, 'deploy/init.sh', 'docker/init.sh.tpl', context)
    generate_file(target_path, 'deploy/nginx.conf', 'docker/nginx.conf.tpl', context)
    if not has_channels:
        generate_file(target_path, 'deploy/uwsgi.ini', 'docker/uwsgi.ini.tpl', context)
    else:
        generate_file(target_path, 'app/asgi.py', 'docker/asgi.py.tpl', context)

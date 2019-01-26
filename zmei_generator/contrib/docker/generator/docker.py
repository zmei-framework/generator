import os
import random
import string

from zmei_generator.generator.utils import generate_file


def generate(target_path, app):
    has_docker = False
    has_celery = False

    generate_file(target_path, 'requirements.prod.txt', 'docker/requirements.prod.txt.tpl', {
        'req_file': os.environ.get('ZMEI_REQUIREMNETS_FILE', 'requirements.txt')
    })
    generate_file(target_path, 'app/settings_prod.py', 'docker/settings_prod.py.tpl', {
        'has_celery': has_celery
    })
    generate_file(target_path, 'Dockerfile', 'docker/dockerfile.tpl')
    generate_file(target_path, '.dockerignore', 'docker/dockerignore.tpl')
    generate_file(target_path, 'docker-compose.yaml', 'docker/docker-compose.yaml.tpl', {
        'has_celery': has_celery
    })

    generate_file(target_path, 'deploy/init.sh', 'docker/init.sh.tpl', {
        'admin_pass': ''.join(random.choice(
            string.ascii_letters + string.digits + string.punctuation.replace('"', '')) for _ in range(16)),
        'admin_user': 'admin-' + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(4)),
    })
    generate_file(target_path, 'deploy/nginx.conf', 'docker/nginx.conf.tpl')
    generate_file(target_path, 'deploy/uwsgi.ini', 'docker/uwsgi.ini.tpl')
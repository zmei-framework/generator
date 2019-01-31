#!/bin/bash

mysql -u root -p123123 -h mysql -e "CREATE DATABASE IF NOT EXISTS app CHARACTER SET utf8 COLLATE utf8_general_ci;"

python manage.py migrate

cat <<EOF | python manage.py shell
from django.contrib.auth import get_user_model

User = get_user_model()

User.objects.filter(username="{{ admin_user }}").exists() or \
    User.objects.create_superuser("{{ admin_user }}", "", "{{ admin_pass }}")
EOF
{% if has_channels %}
daphne -b 0.0.0.0 -p 8000 app.asgi:application
{% else %}
uwsgi --ini deploy/uwsgi.ini
{% endif %}

-r {{ req_file }}

mysqlclient
django-redis-cache
{% if has_channels %}
channels_redis
{% else %}
uwsgi
{% endif %}
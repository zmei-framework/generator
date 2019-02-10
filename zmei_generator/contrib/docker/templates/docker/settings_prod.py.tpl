from .settings import *

DEBUG=False

ALLOWED_HOSTS += ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'app',
        'USER': 'root',
        'PASSWORD': '123123',
        'HOST': 'mysql',
        'PORT': '3306',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': [
            'redis:6379',
        ],
        'OPTIONS': {
            'DB': 1,
            'PARSER_CLASS': 'redis.connection.HiredisParser',
            'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
            'CONNECTION_POOL_CLASS_KWARGS': {
                'max_connections': 50,
                'timeout': 20,
            },
            'MAX_CONNECTIONS': 1000,
            'PICKLE_VERSION': -1,
        },
    },
}

STATIC_ROOT = '/var/www/var/static/'
MEDIA_ROOT = '/var/www/var/media/'

{% if has_celery %}
CELERY_BROKER_URL = 'redis://redis'
CELERY_RESULT_BACKEND = 'redis://redis'
{% endif %}

{% if has_channels %}
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("redis", 6379)],
        },
    },
}
{% endif %}

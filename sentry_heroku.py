import os

from dj_database_url import config
from sentry.conf.server import *


DATABASES = {
    'default': config(default='postgres://localhost')
}

SENTRY_KEY = str(DATABASES['default'])

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = os.environ['PORT']
SENTRY_WEB_OPTIONS = {
    'workers': 3,  # the number of gunicorn workers
    'worker_class': 'gevent'
}

for env_key, env_value in os.environ.iteritems():
    if env_key.startswith('SENTRY_'):
        globals()[env_key] = env_value

import os

import dj_database_url
from sentry.conf.server import *


DATABASES = {
    'default': dj_database_url.config(default='postgres://localhost')
}

SENTRY_KEY = str(DATABASES['default'])

for env_key, env_value in os.environ.iteritems():
    if env_key.startswith('SENTRY_'):
        globals()[env_key] = env_value

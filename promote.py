#!/usr/bin/env python
import os
import re
import sys


if len(sys.argv) < 2:
    print >> sys.stderr, 'usage:', sys.argv[0], 'app_id', '[your_username]'
    raise SystemExit


app_id = sys.argv[1]
with os.popen('heroku auth:whoami') as out:
    email = out.read().strip()
username = sys.argv[2] if len(sys.argv) > 2 else email[:email.index('@')]
os.system('heroku apps:create ' + app_id)
with os.popen('heroku addons:add heroku-postgresql:dev') as out:
    match = re.search('HEROKU_POSTGRESQL_[A-Z_]+', out.read())
os.system('heroku pg:promote ' + match.group(0))
os.system('heroku config:set '
          'SENTRY_URL_PREFIX=http://{0}.herokuapp.com/'.format(app_id))
os.system('heroku run -- sentry --config=sentry_heroku.py upgrade')
os.system('heroku run -- sentry --config=sentry_heroku.py createsuperuser '
          '--email={0} --username={1}'.format(email, username))
os.system('heroku run -- sentry --config=sentry_heroku.py repair --owner=' +
          username)

sentry-heroku
=============

It's a small Heroku app source tree that runs your own Sentry_ service.

.. code-block:: console

   $ heroku login
   $ heroku create my-sentry
   $ git clone git://github.com/dahlia/sentry-heroku.git
   $ cd sentry-heroku/
   $ git push heroku master
   $ ./promote.py my-sentry yourusername
   Creating my-sentry... done, stack is cedar
   http://my-sentry.herokuapp.com/ | git@heroku.com:my-sentry.git
   Git remote heroku added
   Adding heroku-postgresql:dev on my-sentry... done, v2 (free)
   Attached as HEROKU_POSTGRESQL_ROSE_URL
   Database has been created and is available
   Use `heroku addons:docs heroku-postgresql:dev` to view documentation.
   Promoting HEROKU_POSTGRESQL_ROSE_URL to DATABASE_URL... done
   Running `sentry --config=sentry_heroku.py upgrade` attached to terminal...
   Syncing...
   Creating tables ...
   Installing custom SQL ...
   Installing indexes ...
   Installed 0 object(s) from 0 fixture(s)
   Migrating...

In the middle you will meet prompts to create super user:

.. code-block:: console

   Running `sentry --config=sentry_heroku.py createsuperuser` attached to terminal... up, run.2
   Username (leave blank to use 'yourusername'):
   E-mail address (leave blank to use 'yourheroku@login.com'): 
   Password: 
   Password (again): 
   Superuser created successfully.

.. _Sentry: http://sentry.readthedocs.org/

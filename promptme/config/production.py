# Settings that are unique to production go here
from .base import *  # noqa

DEBUG = True

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())

#Configure Django app for Google App Engine
from google.appengine.ext import vendor

vendor.add('lib')

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# Check to see if MySQLdb is available; if not, have pymysql masquerade as
# MySQLdb. This is a convenience feature for developers who cannot install
# MySQLdb locally; when running in production on Google App Engine Standard
# Environment, MySQLdb will be used.
try:
    import MySQLdb  # noqa: F401
except ImportError:
    import pymysql
    pymysql.install_as_MySQLdb()

# [START db_setup]
if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine'):
    # Running on production App Engine, so connect to Google Cloud SQL using
    # the unix socket at /cloudsql/<your-cloudsql-connection string>
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '/cloudsql/promptme:us-west2:promptme-instance',
            'NAME': 'mvp_db',
            'USER': 'admin',
            'PASSWORD': 'bish@op',
        }
    }
else:
    # Running locally so connect to either a local MySQL instance or connect to
    # Cloud SQL via the proxy. To start the proxy via command line:
    #
    #     $ cloud_sql_proxy -instances=[INSTANCE_CONNECTION_NAME]=tcp:3306
    #
    # See https://cloud.google.com/sql/docs/mysql-connect-proxy
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'NAME': 'mvp_db',
            'USER': 'admin',
            'PASSWORD': 'bish@op',
        }
    }
# [END db_setup]

# Settings that are unique to production go here
from .base import *  # noqa

DEBUG = True

# Configure Django App for Heroku.
import os
import django_heroku
django_heroku.settings(locals())

# set site_id for social login to promptme.herokuapp.com
SITE_ID = 6

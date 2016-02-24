from .common import *

DEBUG = False

INSTALLED_APPS += ("gunicorn", "dj_database_url",)

import dj_database_url
DATABASES['default'] = dj_database_url.config()
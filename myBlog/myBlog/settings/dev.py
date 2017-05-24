from __future__ import absolute_import, unicode_literals

from .base import *
ALLOWED_HOSTS = ['172.104.154.119', 'localhost', '127.0.0.1']
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-73+i)&&m*ivtowpkbtyt_i!-(msno*mghvw9nsh3d4hs9rq!a'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass

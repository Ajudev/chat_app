from .base import *
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6_#^c^+llg84=#^6=i^ln*gxvo^*)iwp17a0u-xdr15k!!(glh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Static Details
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'django-static')

# Media Details
MEDIA_URL = '/media/'
MEDIA_LOCAL_URL = 'http://localhost:8000'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CSRF_COOKIE_SECURE = False

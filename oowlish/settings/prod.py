from .base import *

DEBUG = False

WSGI_APPLICATION = 'oowlish.wsgi_prod.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ecommerce_db',
        'USER': 'oowlish',
        'PASSWORD': '',
        'HOST': 'ecommerce_db',
        'PORT': 5432
    }
}

from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'oowlish',
        'USER': 'oowlish',
        'PASSWORD': '',
        'HOST': 'ecommerce_db',
        'PORT': 5432
    }
}

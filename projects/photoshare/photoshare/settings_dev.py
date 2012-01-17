# -*- coding: utf-8 -*-

import warnings
warnings.filterwarnings('error', r"DateTimeField received a naive datetime", RuntimeWarning, r'django\.db\.models\.fields')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'photoshare',
        'USER': 'root',
        'PASSWORD': 'a',
        'HOST': '',
        'PORT': '',
    }
}

MEDIA_URL = '/uploads/'

STATIC_URL = '/static/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



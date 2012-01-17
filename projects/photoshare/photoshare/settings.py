# -*- coding: utf-8 -*-

import os
import sys


PROJECT_ROOT = os.path.dirname(__file__)

# add apps to path
sys.path.insert(0, os.path.join(PROJECT_ROOT, "../../../apps"))
sys.path.insert(0, os.path.join(PROJECT_ROOT, "../../../apps_ext/django-userena"))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Maciej Marczewski', 'maciej@marczewski.net.pl'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'photoshare',                      # Or path to database file if using sqlite3.
        'USER': 'photoshare',                      # Not used with sqlite3.
        'PASSWORD': 'bvf9Rhjftyuu765rty',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Warsaw'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pl'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# A tuple of directories where Django looks for translation files.
LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT, '../../../locale/'),
)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, '../../../uploads/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/uploads/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, '../static-collected/')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, '../static/'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'im2srm@vr-**xro^$74!yet$4w72(6v6nb7j0fzk(@#yx&amp;+omz'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'photoshare.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'photoshare.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, '../../../templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'context_extras.context_processors.current_site',
    'context_extras.context_processors.project_settings',
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'django.contrib.comments',

    'guardian',
    'easy_thumbnails',
    'userena',
    'userena.contrib.umessages',
    'context_extras',

    'profiles',
    'photos',
)


### email settings ###
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = ''
#EMAIL_HOST_PASSWORD = ''
#EMAIL_HOST_USER = ''
#EMAIL_PORT = 25
#EMAIL_USE_TLS = False
# Default email address to use for various automated correspondence from the site manager(s).
DEFAULT_FROM_EMAIL = 'admin@barszcz.info'
# The email address that error messages come from, such as those sent to ADMINS and MANAGERS.
#SERVER_EMAIL = ''
EMAIL_SUBJECT_PREFIX = '[photoshare] '
# Whether to send an email to the MANAGERS each time somebody visits a Django-powered page
# that is 404ed with a non-empty referer (i.e., a broken link).
SEND_BROKEN_LINK_EMAILS = True


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

LOGIN_URL = '/users/signin/'
LOGOUT_URL = '/users/signout/'
LOGIN_REDIRECT_URL = '/users/%(username)s/'
AUTH_PROFILE_MODULE = 'profiles.Profile'

AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)



### django-guardian ###
ANONYMOUS_USER_ID = -1



### userena ###

# Defines if usernames are used within userena. Currently it’s often for the users convenience that only an email is used for identification. With this setting you get just that.
USERENA_WITHOUT_USERNAMES = False

# A string which defines the URI where the user will be redirected to after signin.
USERENA_SIGNIN_REDIRECT_URL = LOGIN_REDIRECT_URL

# Defines the default privacy value for a newly registered user. There are three options:
# closed - Only the owner of the profile can view their profile.
# registered - All registered users can view their profile.
# open - All users (registered and anonymous) can view their profile.
USERENA_DEFAULT_PRIVACY = 'open'

# Boolean value that defines if userena should use the django messages framework to notify the user of any changes.
USERENA_USE_MESSAGES = True



### my custom settings ###

# slogan used under site title in header
SLOGAN = u"Tu jakiś przykładowy slogan"

# separator used in title between "path" elements
TITLE_SEPARATOR = ' / '





# override settings if FLAVOUR env variable is set
FLAVOUR = os.environ.get('FLAVOUR', None)
if FLAVOUR == 'dev':
    from settings_dev import *


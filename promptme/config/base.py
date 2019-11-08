"""
Django settings for promptme project.

Generated by 'django-admin startproject' using Django 2.1.7

Kickstarted from the 2.2 starter by Kickstart Coding, found at:
    http://github.com/kickstartcoding/django-kcproject-starter

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: On production, set SECRET_KEY env variable to override
SECRET_KEY = '*1n^7uub3ki!i&gf3)_ih(y-tl9ti&ckxy2h#dq&2^qze&#b_o'

ALLOWED_HOSTS = ['*']


# Application definition

LOCAL_APPS = [
    'apps.core',
    'apps.accounts',
]

THIRD_PARTY_APPS = [
    'bootstrap4',
    'tinymce',
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS = LOCAL_APPS + THIRD_PARTY_APPS + DJANGO_APPS

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'promptme.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

TINYMCE_DEFAULT_CONFIG = {
    'height': 360,
    'width': 1120,
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
    'selector': "textarea:not(.mceNoEditor)",
    'theme': 'modern',
    'plugins': '''
            textcolor spellchecker save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'TINYMCE_SPELLCHECKER': True,
    'contextmenu': 'formats | link image',
    'menubar': False,
    'statusbar': True,
    }

WSGI_APPLICATION = 'wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = "/static/"

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../apps/core/static'),
)

STATICFILES_STORAGE = 'promptme.storage.WhiteNoiseStaticFilesStorage'


# We also needed to add this to specify where the downloads go
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads/')
MEDIA_URL = '/media/'

LOGIN_URL = '/account/login/'
STATIC_JS_DIR = os.path.join(STATIC_URL, "js")
TINYMCE_JS_ROOT = os.path.join(STATIC_JS_DIR, "tinymce")
TINYMCE_JS_URL = os.path.join(TINYMCE_JS_ROOT, "tinymce.min.js")

# Specify we are using a custom user model
AUTH_USER_MODEL = 'accounts.User'

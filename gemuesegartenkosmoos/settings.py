4"""
Django settings for gemuesegartenkosmoos project.
"""

from juntagrico import defaults

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('JUNTAGRICO_SECRET_KEY')

DEBUG = os.environ.get("JUNTAGRICO_DEBUG", 'False')=='True'

ALLOWED_HOSTS = ['gemuesegartenkosmoos.juntagrico.science', 'localhost','my.gemuesegartenkosmoos.ch']


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'juntagrico.apps.JuntagricoAdminConfig',
    'gemuesegartenkosmoos',
    'juntagrico',  # juntagrico muss neu nach den addons stehen
    'import_export',  # benötigt ab 1.6
    'impersonate',
    'crispy_forms',
    'adminsortable2',
    'polymorphic',
    'crispy_bootstrap4',
    'django_select2',
    'djrichtextfield',
]

ROOT_URLCONF = 'gemuesegartenkosmoos.urls'

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('JUNTAGRICO_DATABASE_ENGINE','django.db.backends.sqlite3'), 
        'NAME': os.environ.get('JUNTAGRICO_DATABASE_NAME','gemuesegartenkosmoos.db'), 
        'USER': os.environ.get('JUNTAGRICO_DATABASE_USER'), #''junatagrico', # The following settings are not used with sqlite3:
        'PASSWORD': os.environ.get('JUNTAGRICO_DATABASE_PASSWORD'), #''junatagrico',
        'HOST': os.environ.get('JUNTAGRICO_DATABASE_HOST'), #'localhost', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': os.environ.get('JUNTAGRICO_DATABASE_PORT', False), #''', # Set to empty string for default.
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'juntagrico.context_processors.vocabulary',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ],
            'debug' : True
        },
    },
]

WSGI_APPLICATION = 'gemuesegartenkosmoos.wsgi.application'


LANGUAGE_CODE = 'de'

DJRICHTEXTFIELD_CONFIG = defaults.richtextfield_config(LANGUAGE_CODE)

EMAIL_BACKEND='juntagrico.backends.email.EmailBackend'

SITE_ID = 1

# This is used by Django, for example if you reset the password
DEFAULT_FROM_EMAIL = 'info@gemuesegartenkosmoos.ch'
# This is used by Django, for example in the subject of the password reset mail.
# It changes the example.com from site id 1 to this domain
# -> funktioniert leider nicht (siehe https://github.com/juntagrico/juntagrico/issues/418)
DEFAULT_FROM_DOMAIN = 'gemuesegartenkosmoos.ch'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

DATE_INPUT_FORMATS =['%d.%m.%Y',]

AUTHENTICATION_BACKENDS = (
    'juntagrico.util.auth.AuthenticateWithEmail',
    'django.contrib.auth.backends.ModelBackend'
)


MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'impersonate.middleware.ImpersonateMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware'
    
]

EMAIL_HOST = os.environ.get('JUNTAGRICO_EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('JUNTAGRICO_EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('JUNTAGRICO_EMAIL_PASSWORD')
EMAIL_PORT = int(os.environ.get('JUNTAGRICO_EMAIL_PORT', '25' ))
EMAIL_USE_TLS = os.environ.get('JUNTAGRICO_EMAIL_TLS', 'False')=='True'
EMAIL_USE_SSL = os.environ.get('JUNTAGRICO_EMAIL_SSL', 'False')=='True'

WHITELIST_EMAILS = []

def whitelist_email_from_env(var_env_name):
    email = os.environ.get(var_env_name)
    if email:
        WHITELIST_EMAILS.append(email.replace('@gmail.com', '(\+\S+)?@gmail.com'))


if DEBUG is True:
    for key in os.environ.keys():
        if key.startswith("JUNTAGRICO_EMAIL_WHITELISTED"):
            whitelist_email_from_env(key)
            


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}

IMPERSONATE = {
    'REDIRECT_URL': '/my/profile',
}

LOGIN_REDIRECT_URL = "/"

"""
    File & Storage Settings
"""
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

MEDIA_ROOT = 'media'

"""
     Crispy Settings
"""
CRISPY_TEMPLATE_PACK = 'bootstrap4'

"""
     juntagrico Settings
"""
ORGANISATION_NAME = "Gemüsegarten Kosmoos"
ORGANISATION_LONG_NAME = "Gemüsegarten Kosmoos"
ORGANISATION_ADDRESS = {"name":"Gemüsegarten Kosmoos", 
            "street" : "Bütikofen",
            "number" : "56",
            "zip" : "3422",
            "city" : "Kirchberg",
            "extra" : ""}
ORGANISATION_BANK_CONNECTION = {"PC" : "-",
            "IBAN" : "CH2408390039389810002",
            "BIC" : "ABSOCH22",
            "NAME" : "ABS",
            "ESR" : ""}
SHARE_PRICE = "50"

CONTACTS = {
    "general": "info@gemuesegartenkosmoos.ch"
}

ORGANISATION_WEBSITE = {
    'name': "www.gemuesegartenkosmoos.ch",
    'url': "https://www.gemuesegartenkosmoos.ch"
}

STYLES = { 'static': ['gemuesegartenkosmoos/css/customize.css']}

USE_TZ = True
TIME_ZONE = 'Europe/Zurich'

FROM_FILTER = {'filter_expression': r'solawi@juntagrico\.ch', 'replacement_from': 'info@gemuesegartenkosmoos.ch'}

DEPOT_LIST_GENERATION_DAYS = [2]

VOCABULARY = { "package": "Kiste" }

IMPORT_EXPORT_EXPORT_PERMISSION_CODE = 'view'

REQUIRED_SHARES = 1

ALLOW_JOB_UNSUBSCRIBE = False

ENABLE_NOTIFICATIONS = ['job_subscribed']
DISABLE_NOTIFICATIONS = []

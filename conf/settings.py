################################################################################
################################################################################
##                             FOR YUNOHOST USERS                             ##
################################################################################
################################################################################

# Please do not modify this file, it will be reset at the next update.
# You can edit the file __INSTALL_DIR__/local_settings.py and add/modify the settings you need.
# The parameters you add in local_settings.py will overwrite these,
# but you can use the options and documentation in this file to find out what can be done.

################################################################################
################################################################################

#!/usr/bin/env python

# Third Party
import environ

# wger
from wger.settings_global import *

env = environ.Env(
    # set casting, default value
    DJANGO_DEBUG=(bool, False)
)

# Use 'DEBUG = True' to get more details for server errors
DEBUG = env("DJANGO_DEBUG")

if os.environ.get('DJANGO_ADMINS'):
    ADMINS = [env.tuple('DJANGO_ADMINS'), ]
    MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '__DB_NAME__',
        'USER': '__DB_USER__',
        'PASSWORD': '__DB_PWD__',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

# Timezone for this installation. Consult settings_global.py for more information
TIME_ZONE = env.str("TIME_ZONE", 'Europe/Berlin')

# Make this unique, and don't share it with anybody.
SECRET_KEY = env.str("SECRET_KEY", '__KEY__')

# Your reCaptcha keys
RECAPTCHA_PUBLIC_KEY = env.str('RECAPTCHA_PUBLIC_KEY', '')
RECAPTCHA_PRIVATE_KEY = env.str('RECAPTCHA_PRIVATE_KEY', '')

# The site's URL (e.g. http://www.my-local-gym.com or http://localhost:8000)
# This is needed for uploaded files and images (exercise images, etc.) to be
# properly served.
SITE_URL = env.str('SITE_URL', 'https://__DOMAIN__')

# Path to uploaded files
# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = env.str("DJANGO_MEDIA_ROOT", '__DATA_DIR__/media')
STATIC_ROOT = env.str("DJANGO_STATIC_ROOT", '__INSTALL_DIR__/static')

# If you change these, adjust nginx alias definitions as well
MEDIA_URL = env.str('MEDIA_URL', '/media/')
STATIC_URL = env.str('STATIC_URL', '/static/')

LOGIN_REDIRECT_URL = env.str('LOGIN_REDIRECT_URL', '/')

# Allow all hosts to access the application. Change if used in production.
ALLOWED_HOSTS = ['__DOMAIN__']

SESSION_ENGINE = "django.contrib.sessions.backends.db"

# Configure a real backend in production
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
if env.bool("ENABLE_EMAIL", True):
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = '__DOMAIN__'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = '__APP__'
    EMAIL_HOST_PASSWORD = '__MAIL_PWD__'
    EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", True)
    EMAIL_USE_SSL = env.bool("EMAIL_USE_SSL", False)
    EMAIL_TIMEOUT = 60

# Sender address used for sent emails
DEFAULT_FROM_EMAIL = env.str("FROM_EMAIL", "wger Workout Manager <__APP__@__DOMAIN__")
WGER_SETTINGS['EMAIL_FROM'] = DEFAULT_FROM_EMAIL
SERVER_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_FROM_ADDRESS = DEFAULT_FROM_EMAIL

# Management
WGER_SETTINGS["ALLOW_GUEST_USERS"] = env.bool("ALLOW_GUEST_USERS", True)
WGER_SETTINGS["ALLOW_REGISTRATION"] = env.bool("ALLOW_REGISTRATION", True)
WGER_SETTINGS["ALLOW_UPLOAD_VIDEOS"] = env.bool("ALLOW_UPLOAD_VIDEOS", True)
WGER_SETTINGS["DOWNLOAD_INGREDIENTS_FROM"] = env.str("DOWNLOAD_INGREDIENTS_FROM", "WGER")
WGER_SETTINGS["EXERCISE_CACHE_TTL"] = env.int("EXERCISE_CACHE_TTL", 3600)
WGER_SETTINGS["MIN_ACCOUNT_AGE_TO_TRUST"] = env.int("MIN_ACCOUNT_AGE_TO_TRUST", 21)  # in days
WGER_SETTINGS["SYNC_EXERCISES_CELERY"] = env.bool("SYNC_EXERCISES_CELERY", False)
WGER_SETTINGS["SYNC_EXERCISE_IMAGES_CELERY"] = env.bool("SYNC_EXERCISE_IMAGES_CELERY", False)
WGER_SETTINGS["SYNC_EXERCISE_VIDEOS_CELERY"] = env.bool("SYNC_EXERCISE_VIDEOS_CELERY", False)
WGER_SETTINGS["SYNC_INGREDIENTS_CELERY"] = env.bool("SYNC_INGREDIENTS_CELERY", False)
WGER_SETTINGS["SYNC_OFF_DAILY_DELTA_CELERY"] = env.bool("SYNC_OFF_DAILY_DELTA_CELERY", False)
WGER_SETTINGS["USE_RECAPTCHA"] = env.bool("USE_RECAPTCHA", False)
WGER_SETTINGS["USE_CELERY"] = env.bool("USE_CELERY", False)

#
# Auth Proxy Authentication
# https://wger.readthedocs.io/en/latest/administration/auth_proxy.html
AUTH_PROXY_HEADER = env.str("AUTH_PROXY_HEADER", '')
AUTH_PROXY_TRUSTED_IPS = env.list("AUTH_PROXY_TRUSTED_IPS", default=[])
AUTH_PROXY_CREATE_UNKNOWN_USER = env.bool("AUTH_PROXY_CREATE_UNKNOWN_USER", False)
AUTH_PROXY_USER_EMAIL_HEADER = env.str("AUTH_PROXY_USER_EMAIL_HEADER", '')
AUTH_PROXY_USER_NAME_HEADER = env.str("AUTH_PROXY_USER_NAME_HEADER", '')

# Cache
if os.environ.get("DJANGO_CACHE_BACKEND"):
    CACHES = {
        'default': {
            'BACKEND': env.str("DJANGO_CACHE_BACKEND"),
            'LOCATION': env.str("DJANGO_CACHE_LOCATION"),
            'TIMEOUT': env.int("DJANGO_CACHE_TIMEOUT"),
            'OPTIONS': {
                'CLIENT_CLASS': env.str("DJANGO_CACHE_CLIENT_CLASS")
            }
        }
    }

    if os.environ.get('DJANGO_CACHE_CLIENT_PASSWORD'):
        CACHES['default']['OPTIONS']['PASSWORD'] = env.str('DJANGO_CACHE_CLIENT_PASSWORD')

    CONNECTION_POOL_KWARGS = dict()
    if "DJANGO_CACHE_CLIENT_SSL_KEYFILE" in os.environ:
        CONNECTION_POOL_KWARGS['ssl_keyfile'] = env.str("DJANGO_CACHE_CLIENT_SSL_KEYFILE")

    if "DJANGO_CACHE_CLIENT_SSL_CERTFILE" in os.environ:
        CONNECTION_POOL_KWARGS['ssl_certfile'] = env.str("DJANGO_CACHE_CLIENT_SSL_CERTFILE")

    if "DJANGO_CACHE_CLIENT_SSL_CERT_REQS" in os.environ:
        CONNECTION_POOL_KWARGS['ssl_cert_reqs'] = env.str("DJANGO_CACHE_CLIENT_SSL_CERT_REQS")

    if "DJANGO_CACHE_CLIENT_SSL_CHECK_HOSTNAME" in os.environ:
        CONNECTION_POOL_KWARGS['ssl_check_hostname'] = env.bool(
            "DJANGO_CACHE_CLIENT_SSL_CHECK_HOSTNAME")

    if CONNECTION_POOL_KWARGS:
        CACHES["default"]["OPTIONS"]["CONNECTION_POOL_KWARGS"] = CONNECTION_POOL_KWARGS

# Folder for compressed CSS and JS files
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_ENABLED = env.bool('COMPRESS_ENABLED', not DEBUG)

# The site's domain as used by the email verification workflow
EMAIL_PAGE_DOMAIN = SITE_URL

#
# Django Axes
#
AXES_ENABLED = env.bool('AXES_ENABLED', True)
AXES_LOCKOUT_PARAMETERS = env.list('AXES_LOCKOUT_PARAMETERS', default=['ip_address'])
AXES_FAILURE_LIMIT = env.int('AXES_FAILURE_LIMIT', 10)
AXES_COOLOFF_TIME = timedelta(minutes=env.float('AXES_COOLOFF_TIME', 30))
AXES_HANDLER = env.str('AXES_HANDLER', 'axes.handlers.cache.AxesCacheHandler')
AXES_IPWARE_PROXY_COUNT = env.int('AXES_IPWARE_PROXY_COUNT', 1)
AXES_IPWARE_META_PRECEDENCE_ORDER = env.list('AXES_IPWARE_META_PRECEDENCE_ORDER',
                                             default=['HTTP_X_FORWARDED_FOR', 'REMOTE_ADDR'])

#
# Django Rest Framework SimpleJWT
#
SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'] = timedelta(minutes=env.int("ACCESS_TOKEN_LIFETIME", 15))
SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'] = timedelta(hours=env.int("REFRESH_TOKEN_LIFETIME", 24))
SIMPLE_JWT['SIGNING_KEY'] = env.str("SIGNING_KEY", SECRET_KEY)

#
# https://docs.djangoproject.com/en/4.1/ref/csrf/
#
CSRF_TRUSTED_ORIGINS = env.list(
    "CSRF_TRUSTED_ORIGINS",
    default=['https://__DOMAIN__'],
)

if env.bool('X_FORWARDED_PROTO_HEADER_SET', False):
    SECURE_PROXY_SSL_HEADER = (
        env.str('SECURE_PROXY_SSL_HEADER', 'HTTP_X_FORWARDED_PROTO'),
        'https'
    )

REST_FRAMEWORK['NUM_PROXIES'] = env.int('NUMBER_OF_PROXIES', 1)

#
# Celery message queue configuration
#
CELERY_BROKER_URL = env.str("CELERY_BROKER", "redis://127.0.0.1:6379/__REDIS_DB__")
CELERY_RESULT_BACKEND = env.str("CELERY_BACKEND", "redis://127.0.0.1:6379/__REDIS_DB__")

#
# Prometheus metrics
#
EXPOSE_PROMETHEUS_METRICS = env.bool('EXPOSE_PROMETHEUS_METRICS', False)
PROMETHEUS_URL_PATH = env.str('PROMETHEUS_URL_PATH', 'super-secret-path')

#
# Logging
#
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': 'level={levelname} ts={asctime} module={module} path={pathname} line={lineno} message={message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': env.str('LOG_LEVEL_PYTHON', 'INFO').upper(),
            'propagate': True,
        },
    }
}

# Yunohost hack so users can define a new conf, and we can just replace the conf
try:
    from .local_settings import *
except ImportError:
    pass

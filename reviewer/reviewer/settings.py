import os
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

env = environ.Env(
    ALLOWED_HOSTS=(list, ['*']),
    DB_HOST=(str, 'localhost'),
    DB_NAME=(str, 'db'),
    DB_PASSWORD=(str, 'password'),
    DB_PORT=(str, '5432'),
    DB_USER=(str, 'postgres'),
    DEBUG=(bool, True),
    EMAIL_ADDRESS=(str, 'example@gmail.com'),
    EMAIL_APP_PASSWORD=(str, 'password'),
    REDIS_HOST=(str, '127.0.0.1'),
    REDIS_PORT=(str, '6379'),
    SECRET_KEY=(str, 'dummy-key'),
    USERS_AUTOACTIVATE=(bool, True),
)

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')
USERS_AUTOACTIVATE = env('USERS_AUTOACTIVATE')

ALLOWED_HOSTS = env('ALLOWED_HOSTS')

INSTALLED_APPS = [
    # default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # installed apps
    'django_cleanup.apps.CleanupConfig',
    'rest_framework',
    'sorl.thumbnail',
    'widget_tweaks',
    # created apps
    'api.apps.ApiConfig',
    'genres.apps.GenresConfig',
    'feeds.apps.FeedsConfig',
    'movies.apps.MoviesConfig',
    'persons.apps.PersonsConfig',
    'rating.apps.RatingConfig',
    'roles.apps.RolesConfig',
    'users.apps.UsersConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG:
    INSTALLED_APPS += [
        'debug_toolbar',
    ]
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]

ROOT_URLCONF = 'reviewer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'reviewer.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.'
        'password_validation.'
        'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.'
        'password_validation.'
        'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.'
        'password_validation.'
        'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.'
        'password_validation.'
        'NumericPasswordValidator',
    },
]

REDIS_HOST = env('REDIS_HOST')
REDIS_PORT = env('REDIS_PORT')

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static_dev',
]

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'users.User'

THUMBNAIL_DEBUG = True

EMAIL = env('EMAIL_ADDRESS')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_FILE_PATH = BASE_DIR / 'sent_emails'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = EMAIL
EMAIL_HOST_PASSWORD = env('EMAIL_APP_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True


CELERY_BROKER_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}'
CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
CELERY_RESULT_BACKEND = f'redis://{REDIS_HOST}:{REDIS_PORT}'
CELERY_ACCEPT_TOKEN = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

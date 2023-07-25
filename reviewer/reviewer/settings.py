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
    REDIS_HOST=(str, '127.0.0.1'),
    REDIS_PORT=(str, '6379'),
    SECRET_KEY=(str, 'dummy-key'),
)

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

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
    'sorl.thumbnail',
    'widget_tweaks',
    # created apps
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

LOGIN_URL = '/auth/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'users.User'

THUMBNAIL_DEBUG = True

REDIS_HOST = env('REDIS_HOST')
REDIS_PORT = env('REDIS_PORT')

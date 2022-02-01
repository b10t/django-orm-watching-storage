import os

from environs import Env

env = Env()
env.read_env()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': env.str('DB_HOST', ''),
        'PORT': env.str('DB_PORT', '5434'),
        'NAME': env.str('DB_NAME', ''),
        'USER': env.str('DB_USER', ''),
        'PASSWORD': env.str('DB_PASSWORD', ''),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv('SECRET_KEY', '')

DEBUG = env.bool("DEBUG", False)

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

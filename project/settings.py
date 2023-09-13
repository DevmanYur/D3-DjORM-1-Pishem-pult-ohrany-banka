import os
from environs import Env
env = Env()
env.read_env()


DATABASES = {
    'default': {
        'ENGINE': env("ENGINE"),
        'HOST': env("HOST"),
        'PORT': env("PORT"),
        'NAME': env("NAME"),
        'USER': env("USER"),
        'PASSWORD': env("PASSWORD"),
    }
}

INSTALLED_APPS = [env("INSTALLED_APPS")]

SECRET_KEY = env("SECRET_KEY")


DEBUG = env.bool("DEBUG_FALSE", "DEBUG_TRUE")

ROOT_URLCONF = env("ROOT_URLCONF")

ALLOWED_HOSTS = [env("ALLOWED_HOSTS")]


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

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

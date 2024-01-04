"""
Django settings for loja project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path
from pprint import pprint
from django.contrib.messages import constants

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ol2wu7mv^s=f5853fb^j@h*0mq876-@r)-uauls$o$c5#y#*gl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'produto',
    'pedido',
    'perfil',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'crispy_forms',
    'crispy_bootstrap4',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'loja.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'loja.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# Define o prefixo que será usado para construir URLs dos arquivos estáticos (como CSS, JavaScript e imagens). 
# No caso, os arquivos estáticos seriam servidos em URLs começando com 'static/'
STATIC_URL = 'static/'

# Especifica o diretório no qual os arquivos estáticos serão coletados (ou seja, reunidos) quando você executa o comando collectstatic do Django. 
# Geralmente, é usado para coletar todos os arquivos estáticos de aplicativos individuais em um local centralizado para implantação.
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Uma lista de diretórios adicionais dos quais o Django deve coletar arquivos estáticos. 
# Aqui, os.path.join('static') especifica que deve procurar arquivos estáticos no diretório static do seu projeto.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'templates/static')
]

# Define o prefixo para construir URLs dos arquivos de mídia (como uploads de usuários). 
# No caso, os arquivos de mídia seriam servidos em URLs começando com '/media/'
MEDIA_URL = '/media/'

# Especifica o diretório no qual os arquivos de mídia serão salvos no servidor. 
# Este é o diretório no qual os arquivos enviados pelos usuários serão armazenados.
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MESSAGE_TAGS = {
    constants.DEBUG: 'alert-info',
    constants.ERROR: 'alert-danger',
    constants.INFO: 'alert-info',
    constants.SUCCESS: 'alert-success',
    constants.WARNING: 'alert-warning',
}

# Sessão em dias: 60s * 60m * 24h * 1d
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7

# Salvar a cada requisição
SESSION_SAVE_EVERY_REQUEST = False

# Serializar - Padrão JSON
# SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
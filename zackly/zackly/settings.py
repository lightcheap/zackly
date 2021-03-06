"""
Django settings for zackly project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ovb!a$4envs+_fma61$@l=zyt7ggybs7)2#rby3f7=0*u*9l8r'

# SECURITY WARNING: don't run with debug turned on in production!
# デプロイするためにFalseにしてます。
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin', #管理サイトを使うのに必要
    'django.contrib.auth', #管理サイトを使うのに必要
    'django.contrib.contenttypes', #管理サイトを使うのに必要
    'django.contrib.sessions', #管理サイトを使うのに必要
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'zacklymain.apps.ZacklymainConfig', # zackly アプリ本体
    'accounts.apps.AccountsConfig', #サインアップ用
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', #管理サイトを使うのに必要
    'django.contrib.messages.middleware.MessageMiddleware', #管理サイトを使うのに必要
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'zackly.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth', #管理サイトを使うのに必要
                'django.contrib.messages.context_processors.messages', #管理サイトを使うのに必要
            ],
        },
    },
]

WSGI_APPLICATION = 'zackly.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3'
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
        'NAME': 'zackly',
        'USER': 'postgres',
        'PASSWORD': 'mm358358',
        'HOST': '127.0.0.1',
        'POST': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/
# 日本語にする
LANGUAGE_CODE = 'jp-JP'
# タイムゾーンを日本に
TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

# ログイン後に一旦トップにリダイレクトする
#LOGIN_REDIRECT_URL ='zacklymain:main'

# 開発環境用ファイルの読み込み
try:
    from .local_settings import *
except ImportError:
    pass

if not DEBUG:
    import django_heroku
    django_heroku.settings(locals())
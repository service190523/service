"""
Django settings for service project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
db_from_env = dj_database_url.config()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-lm6#&qsrnw+59&*6!yj(_5%*&xi6p&=nrl=pjc78is)=u%10dz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
#DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'service777.herokuapp.com',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'orlov',
    'django_cleanup',
    'crispy_forms',
    'widget_tweaks',
    'cloudinary_storage',
    'cloudinary',   
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',        
]

ROOT_URLCONF = 'service.urls'

TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
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

WSGI_APPLICATION = 'service.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': BASE_DIR / 'db.sqlite3',
    #}

    #'default': {
    #    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #    'NAME': 'service',
    #    'USER' : 'customer',
    #    'PASSWORD' : 'customer',
    #    'HOST' : '127.0.0.1',
    #    'PORT' : '5432',
    #}

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd2rhc0dic3fh1j',
        'USER' : 'vnmtzprjqqccxd',
        'PASSWORD' : 'bfec8c12323bc4d02af5473f7a1b0c55bfb224f569ddee7a35b20ff23779f260',
        'HOST' : 'ec2-3-211-6-217.compute-1.amazonaws.com',
        'PORT' : '5432',
    }
    
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/
LANGUAGE_CODE = 'ru-Ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True 

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

LANGUAGES = (
    ('ru', 'Russian'),
    ('en', 'English'),
)

#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, "static"),
#]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# MEDIA_ROOT - это абсолютный путь файловой системы к каталогу для загруженных пользователем файлов.
# MEDIA_URL - это URL-адрес, который можно использовать в наших шаблонах для файлов.
# Папку media необходимо создать в корневой папке проекта
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')
MEDIA_URL = '/media/'

# Redirect to home URL after login (Default redirects to /accounts/profile/)
# Теперь, при входе в систему, вы по умолчанию должны перенаправляться на домашнюю страницу сайта а не на /accounts/profile/
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/index'

# Сохранения изображения
"""
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'hxswkk9jx',
    'API_KEY': '997576523626946',
    'API_SECRET': '9DIwU54439Nf3LjUWQ8xo8ort8w',
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
"""

# Отправка почты
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_HOST_USER = 'service26022022@mail.ru' 
EMAIL_HOST_PASSWORD = 'KHQ303RQuaPQPtpuXqwC'
DEFAULT_FROM_EMAIL  = 'service26022022@mail.ru'
EMAIL_PORT = 25
EMAIL_USE_TLS = True



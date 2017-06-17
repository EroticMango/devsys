#-*- coding:utf8 -*-

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_*b844))&omdj+7)zx#1$%c4a$*cv61a)d3t=a!mr0^+ylxh2&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

from constant import svr_config as Conf


#========================Celery Settings==============
CELERY_CONF = Conf['CELERY']
BROKER_URL = CELERY_CONF['broker_url']
#CELERY_RESULT_BACKEND = "redis://:foo@localhost:6379/15"
CELERY_RESULT_BACKEND = CELERY_CONF['celery_result_backend']

ALLOWED_HOSTS = ['*']


# Application definition

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

CUSTOM_APPS = [
    'demo',
    'accounts',
    'utils',
    'blog',
    'middleware',
    'cache'
]

THIRD_APPS = [
    'rest_framework',
    'corsheaders'
]

INSTALLED_APPS = DEFAULT_APPS + CUSTOM_APPS + THIRD_APPS

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', #跨域
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'devsysproj.urls'

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

WSGI_APPLICATION = 'devsysproj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
if Conf['DB']['db_type'] == 'sqlite':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DB_CONF = Conf['DB']
    DATABASES = {
        'default': {
            'ENGINE': DB_CONF['engine'],
            'NAME': DB_CONF['name'],
            'USER': DB_CONF['user'],
            'PASSWORD': DB_CONF['password'],
            'HOST': DB_CONF['host'],
            'PORT': DB_CONF['port']
        }
    }

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

#=================REST_FRAME_WORK SETTINGS=============
REST_FRAMEWORK = {

    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),

    'DEFAULT_AUTHENTICATION_CLASSES':(
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication'
    )
}


#==============CORS SETTINGS===================
CORS_ORIGIN_ALLOW_ALL = False

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Access-Control-Allow-Origin'
)

CORS_ORIGIN_WHITELIST = (
    'google.com',
    'hostname.example.com',
    'localhost:8000',
    '127.0.0.1:8080',
    '127.0.0.1:8000',
    '0.0.0.0:8080',
    'localhost:8080',
    '192.168.1.217:8080'
)

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)

CUR_PATH = os.getcwd()

#=================Logging Settings===============
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '{cur_path}/log/debug.log'.format(cur_path=CUR_PATH),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

#=========Email Settings==========
EMAIL_CONF = Conf['EMAIL']
EMAIL_HOST = EMAIL_CONF['email_host']
EMAIL_HOST_USER = EMAIL_CONF['email_host_user']# 用户
EMAIL_HOST_PASSWORD = EMAIL_CONF['email_host_password'] # 密码
EMAIL_SUBJECT_PREFIX = u'[重置密码]' # 为邮件Subject-line前缀,默认是'[django]'
EMAIL_USE_TLS = False #与SMTP服务器通信时，是否启动TLS链接(安全链接)。默认是false


#============Memcached Settings=======
MEMACHED_CONF = Conf['MEMCACHED']
MEMACHED_CONF_HOST = MEMACHED_CONF['location']
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': MEMACHED_CONF_HOST,
    }
}

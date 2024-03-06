import os
from dotenv import load_dotenv
from django.core.management.utils import get_random_secret_key

# Base configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dotenv_path = os.path.join(os.path.dirname(BASE_DIR), '.env')
load_dotenv(dotenv_path)

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', get_random_secret_key())
DEBUG = os.getenv('DEBUG', 'False') == 'True' #Don't user DEBUG in production

SITE_ID = 1
LOGIN_REDIRECT_URL = '/admin'

ROOT_URLCONF = '_setup.urls'
WSGI_APPLICATION = '_setup.wsgi.application'

STATIC_URL = '/static/'
STATIC_ROOT = '/static'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'back,localhost,127.0.0.1').split(',')

# Application definition
INSTALLED_APPS = [
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
   
    # Rest framework
    'rest_framework',
    'django_filters',

    # Custom apps
    'devices',
    'observatories',
    'asteroids',
    'sightings',
    'commons',

     # Other apps
    'corsheaders',
    'drf_spectacular',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['Templates', f'{BASE_DIR}/_setup/templates'],
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


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

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

# Rest framework configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',),
    'DEFAULT_SCHEMA_CLASS': 'commons.rest.fast_auto_schema.FastAutoSchema',
}

# CORS configuration
CORS_ALLOW_METHODS = ['DELETE', 'GET', 'OPTIONS', 'PATCH', 'POST', 'PUT']
CORS_ALLOW_HEADERS = ('accept', 'accept-encoding', 'authorization', 'content-type', 'origin', 'user-agent', 'x-csrftoken', 'x-requested-with',)
if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True
else: 
    CORS_ALLOWED_ORIGINS = os.getenv('CORS_ALLOWED_ORIGINS', 'http://localhost:3000,http://127.0.0.1:3000').split(',')

#CSRF configuration
CSRF_TRUSTED_ORIGINS = ['http://localhost','http://localhost:3000', 'http://localhost:8000']

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Database configuration
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("DATABASE_NAME"),
        'USER': os.getenv("DATABASE_USER"),
        'HOST': os.getenv("DATABASE_HOST"),
        'PORT': os.getenv("DATABASE_PORT"),
        'PASSWORD': os.getenv("DATABASE_PASSWORD"),
    }
}

# Swagger configuration
SPECTACULAR_SETTINGS = {
    'TITLE': 'Base API',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}

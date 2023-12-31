# flake8: noqa
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent


DATA_DIR = BASE_DIR.parent / 'data' / 'web' 


SECRET_KEY = os.getenv('SECRET_KEY', 'change-me')


DEBUG = bool(int(os.getenv('DEBUG', '0')))


ALLOWED_HOSTS = [
    h.strip() for h in os.getenv('ALLOWED_HOSTS', '').split(',')
    if h.strip()
]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'adminlte3',
    'adminlte3_theme',
    'localflavor',
    'app',
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


ROOT_URLCONF = 'gerenciamento_pet.urls'


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


WSGI_APPLICATION = 'gerenciamento_pet.wsgi.application'


# email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'marcelolemesgalli2@gmail.com'
EMAIL_HOST_PASSWORD = '{token_email}'


DATABASES = {
  'default': {
    'ENGINE': os.getenv('DATABASE_URL'),
    'NAME': os.getenv('DATABASE_NAME'),
    'HOST': os.getenv('DATABASE_HOST'),
    'PORT': os.getenv('DATABASE_PORT'),
    'USER': os.getenv('DATABASE_USERNAME'),
    'PASSWORD': os.getenv('DATABASE_PASSWORD')
  }
}


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


LANGUAGE_CODE = 'pt-br'


TIME_ZONE = 'America/Sao_Paulo'


USE_I18N = True


USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = DATA_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = DATA_DIR / 'media'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# modulo para authentication
AUTH_USER_MODEL = 'app.Funcionario'


# redefinindo rotas de login e logout
LOGOUT_URL = 'logout'
LOGIN_URL = 'login'

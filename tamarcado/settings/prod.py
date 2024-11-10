from tamarcado.settings.base import *
from dotenv import load_dotenv
import os
load_dotenv()

DEBUG = False

ALLOWED_HOSTS = os.environ.get('ALLOWED', '').split(',')


DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': os.environ.get('DATABASE_NAME'),  
        'USER': os.environ.get('DATABASE_USER'), 
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'), 
        'HOST': 'DESKTOP-9PIP9L1\SQLEXPRESS',
        'PORT': '',  # Se não precisar de uma porta específica, deixe vazio
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',  # Corrigido
        },
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'lmirandaeb@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
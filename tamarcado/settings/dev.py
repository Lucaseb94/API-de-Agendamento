from tamarcado.settings.base import *
from dotenv import load_dotenv
import os

load_dotenv()

DEBUG = True

ALLOWED_HOSTS = []

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

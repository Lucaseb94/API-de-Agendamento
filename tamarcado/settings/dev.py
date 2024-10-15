from tamarcado.settings.base import *
from dotenv import load_dotenv
import os

load_dotenv()

DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': os.environ.get('DATABASE_NAME'),  
        'USER': os.environ.get('DATABASE_USER'), 
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'), 
        'HOST': os.environ.get('DATABASE_HOST'),  
        'PORT': '',  # Se não precisar de uma porta específica, deixe vazio
        'OPTIONS': {
            'driver': os.environ.get('DATABASE_DRIVER'),  
        },
    }
}


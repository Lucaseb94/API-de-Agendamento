from tamarcado.settings.base import *
from dotenv import load_dotenv
import os
load_dotenv()

DEBUG = False

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE'),
        'NAME': os.environ.get('DATABASE_NAME'),  
        'USER': os.environ.get('DATABASE_USER'), 
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'), 
        'HOST': os.environ.get('DATABASE_HOST'),  
        'PORT': '1433',  # Se não precisar de uma porta específica, deixe vazio
        'OPTIONS': {
            'driver': os.environ.get('DATABASE_DRIVER'),  
        },
    }
}

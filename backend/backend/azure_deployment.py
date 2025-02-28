"""
    This is file contains the deployment configurations for Azure Services.
"""
import os
from .settings import *
from .settings import BASE_DIR

ALLOWED_HOSTS = [os.environ.get('WEBSITE_HOSTNAME')]
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ.get('WEBSITE_HOSTNAME')]
DEBUG = False

connection_string = os.environ.get('AZURE_POSTGRESQL_CONNECTIONSTRING')
parameters = {pair.split("="):pair.split("=")[1] for pair in connection_string.split(' ')}

SECRET_KEY = None

AZURE_OPENAI_API_KEY = None
AZURE_OPENAI_ENDPOINT = None

POPPLER_PATH = None
POSTGRES_DB_USER = parameters["user"]
POSTGRES_DB_PASSWORD = parameters["password"]
DB_HOST = parameters["host"]
DB_NAME = parameters["dbname"]
DB_PORT = None


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": DB_NAME,
        "USER": POSTGRES_DB_USER,
        "PASSWORD": POSTGRES_DB_PASSWORD,
        "HOST": DB_HOST
    }
}
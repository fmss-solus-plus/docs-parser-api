"""
    This is file contains the deployment configurations for Amazon web services.
"""
from .settings import *
from backend.utils import get_env_variable

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_variable("DJANGO_SECRET_KEY")

AZURE_OPENAI_API_KEY = get_env_variable("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = get_env_variable("AZURE_OPENAI_ENDPOINT")

POPPLER_PATH = get_env_variable("POPPLER_PATH")
POSTGRES_DB_USER = get_env_variable("POSTGRES_DB_USER")
POSTGRES_DB_PASSWORD = get_env_variable("POSTGRES_DB_PASSWORD")
DB_HOST = get_env_variable("DB_HOST")
DB_PORT = get_env_variable("DB_PORT")
DB_NAME = get_env_variable("DB_NAME")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": DB_NAME,
        "USER": POSTGRES_DB_USER,
        "PASSWORD": POSTGRES_DB_PASSWORD,
        "HOST": DB_HOST,
        "PORT": DB_PORT,
    }
}

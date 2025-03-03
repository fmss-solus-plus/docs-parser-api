"""
    This is file contains the deployment configurations for Azure Services.
"""
import os
from .settings import *
from .settings import BASE_DIR

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME']]
DEBUG = False

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

print("USING AZURE ENV")
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

conn_string = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
conn_string_params = {pair.split("="):pair.split("=")[1] for pair in conn_string.split(' ')}

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

AZURE_OPENAI_API_KEY = os.environ['AZURE_OPENAI_API_KEY']
AZURE_OPENAI_ENDPOINT = None

POPPLER_PATH = None
POSTGRES_DB_USER = conn_string_params["user"]
POSTGRES_DB_PASSWORD = conn_string_params["password"]
DB_HOST = conn_string_params["host"]
DB_NAME = conn_string_params["dbname"]
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
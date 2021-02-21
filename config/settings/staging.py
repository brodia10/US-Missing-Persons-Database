from .base import *
from decouple import config

DEBUG = False

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

ALLOWED_HOSTS = [
    "us-missing-persons-staging.herokuapp.com",
]

# This ensures that Django will be able to detect a secure connection
# properly on Heroku.
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Redirect HTTP to HTTPS
SECURE_SSL_REDIRECT = True

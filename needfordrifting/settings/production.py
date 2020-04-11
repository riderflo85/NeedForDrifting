from .default import *
import os


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = []

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
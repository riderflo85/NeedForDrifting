from .default import *
import os


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['79.137.28.80']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, 'static'),)

from .default import *
import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['www.needfordrifting.ovh', 'needfordrifting.ovh', '79.137.28.80']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, 'static'),)

sentry_sdk.init(
    dsn="https://bc70242a511f4e2184f2ad152a57a640@o279273.ingest.sentry.io/5209357",
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

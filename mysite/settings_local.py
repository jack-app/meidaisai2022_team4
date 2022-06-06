import os

from mysite.settings import BASE_DIR
# Djangoの秘密キー
SECRET_KEY = 'django-insecure-!6t)9zkc9g6n62d2$b$rg&o#yah#971sf(@^3rrjdm&*89ih*y'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# DB接続情報
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

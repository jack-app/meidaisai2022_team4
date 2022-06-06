import os

from mysite.settings import BASE_DIR
# Djangoの秘密キー
SECRET_KEY = 'i2u1hdlo4pqam20uxuzli5e&x#z=_f534kvihyh!of)!#3$m=u'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# DB接続情報
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True
ALLOWED_HOSTS=["localhost", '127.0.0.1',]
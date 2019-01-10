import os.path

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
THREADED = True
threaded = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage.db')

SQLALCHEMY_TRACK_MODIFICATIONS  = True

SECRET_KEY = 'TI_INTEGRADO_IA/SD'
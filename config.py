import os


# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'my precious'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI']
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False

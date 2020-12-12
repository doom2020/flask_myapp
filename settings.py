class Config(object):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = 'prod'
    DATABASE_URI = ''

class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'dev'
    DATABASE_URI = ''

import os

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:4543@localhost/coffeeandcode'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'Mwiks01'

    DEBUG = True

class ProdConfig(Config):
    '''
    Production configuration child class
    '''
    pass
    DEBUG = True

class DevConfig(Config):
    '''
    Development configuration child class
    '''
    pass
    DEBUG = True

config_options = {
   "production" :ProdConfig,
   'development' :DevConfig,
}
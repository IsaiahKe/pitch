import os


class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://izzie:Access@localhost/pitch'
    UPLOADED_PHOTOS_DEST='app/static/img'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class DevConfig(Config):

    DEBUG = True


class ProdConfig(Config):
    pass


config_options = {'development': DevConfig, 'production': ProdConfig}

# coding: utf-8
import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Configuration():
    """
    Base Configuration for Flask App.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
        '{u\xad\xd1\xc7\xe1F\x8dQt\x07\xd8\x19\x8f)\xa9\xeaE\x10\xb2\xd0x>D'
    # SQLALCHEMY
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # MAIL
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_SUBJECT_PREFIX = '[FlaskBlog]'
    MAIL_SENDER = 'Flask Team <webdev1905@gmail.com>'
    # PAGE
    ITEMS_PER_PAGE = 20
    # UPLOAD FOLDER
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'app/static/uploads/images')
    # ALLOWED EXTENTIONS
    IMAGE_ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Configuration):
    """
    Configuration for Development Environment.
    """
    DEBUG = True
    # MAIL
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # SQLALCHEMY
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'db/data-dev.sqlite')


class TestingConfig(Configuration):
    """
    Configuration for Testing Flask App.
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'db/data-test.sqlite')


class ProductionConfig(Configuration):
    """
    Configuration for Production.
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'db/data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

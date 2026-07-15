import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///courses.db'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-dev-key'
    DEBUG = True

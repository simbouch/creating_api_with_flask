import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///site.db') if 'SQLALCHEMY_DATABASE_URI' in os.environ else None
    SQLALCHEMY_TRACK_MODIFICATIONS = False

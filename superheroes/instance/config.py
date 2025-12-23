import os

SQLALCHEMY_DATABASE_URI = 'sqlite:///superheroes.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'super-secret-key'

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')

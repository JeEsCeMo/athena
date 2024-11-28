import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'amVzc1NlY3JldEtleQ==')
    SQLALCHEMY_DATABASE_URI = 'postgresql://jessicacedeno:151299@localhost/athena'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

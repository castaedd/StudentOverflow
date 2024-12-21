import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+pg8000://postgres:Soyenergia93@localhost/studentoverflow'
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'supersecretkey'
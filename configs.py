from flask import Config
import os

class AppConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
from dotenv import load_dotenv
from flask import Config
import os

load_dotenv()

class AppConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
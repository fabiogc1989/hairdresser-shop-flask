from configs import APP_CONFIG
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import Base
from views import routes

# Create the app
app = Flask(__name__)

# Configure the MysSQL database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = APP_CONFIG['DATABASE_URI']

app.register_blueprint(routes) # Register the blueprint of routes

# Initialize the db with the extension SQLAlchemy
db = SQLAlchemy(model_class = Base)
db.init_app(app)

if __name__ == '__main__':
    app.run()
from configs import AppConfig
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import Base
from views import routes

# Create the app
app = Flask(__name__)

# Set the configure object to the flask app
app.config.from_object(AppConfig)

# Register all Blueprints
app.register_blueprint(routes)

# Initialize the db with the extension SQLAlchemy
db = SQLAlchemy(model_class = Base)
db.init_app(app)

if __name__ == '__main__':
    app.run()
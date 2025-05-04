from flask import Flask
from configs import AppConfig
from src.extensions import db
from src.shop_service.views import views as shop_service_views
from src.person.customer.views import views as customer_views


def create_app(test_config=None):
    # create and configure the src
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(AppConfig)

    if test_config is None:
       # load the instance config, if it exists, when not testing
        app.config.from_object(AppConfig)
    else:
        # load the test config if passed in
        app.config.from_object(test_config)

    # register all blueprints
    app.register_blueprint(shop_service_views, name = 'shop_service_views', url_prefix='/shop_service')
    app.register_blueprint(customer_views, name = 'customer_views', url_prefix='/customer')

    # initialize the app with the extension SQLAlchemy
    db.init_app(app)

    return app
from flask import Blueprint

routes = Blueprint('routes', __name__, url_prefix='/', template_folder='./templates')

@routes.route('/')
def index():
    return 'Hello World!'
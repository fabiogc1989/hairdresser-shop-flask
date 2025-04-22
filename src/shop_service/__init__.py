from flask import Blueprint

views = Blueprint('views', __name__, url_prefix='/shop_service', template_folder='./templates')
from flask import render_template
import src.shop_service.services as services
from src.shop_service import views

@views.route('/', methods=['GET'])
def index():
    shop_services = services.get_shop_services()
    return render_template('shop_service/index.html', shop_services = shop_services)
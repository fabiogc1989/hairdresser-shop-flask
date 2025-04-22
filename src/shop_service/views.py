from src.shop_service import views

@views.route('/')
def index():
    return 'Hello World!'
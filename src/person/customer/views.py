from flask import render_template
import src.person.customer.services as services
from src.person.customer import views

@views.route('/', methods=['GET'])
def index():
    customers = services.get_customers()
    return render_template('customer/index.html', customers=customers)
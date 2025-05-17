from flask import render_template
import src.person.customer.services as services
from src.person.customer import views

@views.route('/', methods=['GET'])
def index():
    customers = services.get_customers()
    return render_template('customer/index.html', customers=customers)


@views.route('/create', methods=['GET', 'POST'])
def create_customer():
    return render_template('customer/create.html')

@views.route('/<int:id>', methods=['DELETE'])
def delete_customer(id: int):
    """Delete a customer by ID."""
    customer = services.get_customer_by_id(id)
    if not customer:
        pass
    if services.delete_customer_by_id(id):
        return f'The customer {customer.full_name()} has been deleted successfully.'
    else:
        return f'The customer {customer.full_name()} could not be deleted.'
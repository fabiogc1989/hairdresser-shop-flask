from typing import List
from sqlalchemy import ScalarResult, select
from src.extensions import db
from src.person.models import Customer

def get_customers() -> ScalarResult[List[Customer]]:
    return db.session.execute(select(Customer)).scalars()


def get_customer_by_id(id):
    pass


def delete_customer_by_id(id):
    pass


def create_customer():
    pass


def update_customer():
    pass
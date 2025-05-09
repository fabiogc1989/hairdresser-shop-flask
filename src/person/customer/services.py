from typing import List
from sqlalchemy import ScalarResult, select
from src.extensions import db
from src.person.models import Customer

def get_customers() -> ScalarResult[List[Customer]]:
    return db.session.execute(select(Customer)).scalars()


def get_customer_by_id(id: int) -> ScalarResult[Customer]:
    """Get a customer by ID."""
    return db.session.execute(select(Customer).where(Customer.id == id)).scalar_one_or_none()


def delete_customer_by_id(id: int) -> bool:
    """Delete a customer by ID."""
    db.session.delete_customer_by_id(id)
    db.session.commit()


def create_customer():
    pass


def update_customer():
    pass
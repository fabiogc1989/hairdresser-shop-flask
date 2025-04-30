from src.extensions import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, relationship

class Customer(Base):
    __tablename__ = 'customer'

    # Customer's address
    address = mapped_column(String(256))
    state = mapped_column(String(256))
    city = mapped_column(String(256))
    country = mapped_column(String(90))
    postal_code = mapped_column(String(18), nullable=False)

    # Foreign key
    person_id = mapped_column(ForeignKey('person.id'))

    # Relationships
    person = relationship('Person', back_populates='customer')
from src.extensions import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from src.user.models import User

class Person(Base):
    __tablename__ = 'person'

    # Person's information
    first_name = mapped_column(String(256), nullable=False)
    last_name = mapped_column(String(256), nullable=False)

    # Person's contacts
    phone_number = mapped_column(String(26), nullable=False)
    email = mapped_column(String(254))

    def full_name(self):
        """Return the full name of the person."""
        return f'{self.first_name} {self.last_name}'


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
    person = relationship('Person')


class Employee(Base):
    __tablename__ = 'employee'

    # Employee's address
    address = mapped_column(String(256), nullable=False)
    state = mapped_column(String(256), nullable=False)
    city = mapped_column(String(256), nullable=False)
    country = mapped_column(String(90), nullable=False)
    postal_code = mapped_column(String(18), nullable=False)

    # Foreign key
    person_id = mapped_column(ForeignKey('person.id'))

    # Relationships
    person = relationship('Person')
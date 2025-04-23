from src.extensions import Base, db
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, relationship

class Employee(Base, db.Model):
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
    person = relationship('Person', back_populates='employee')
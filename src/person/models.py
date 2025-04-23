from src.extensions import Base, db
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, relationship

class Person(Base, db.Model):
    __tablename__ = 'person'

    # Person's information
    first_name = mapped_column(String(256), nullable=False)
    last_name = mapped_column(String(256), nullable=False)

    # Person's contacts
    phone_number = mapped_column(String(26), nullable=False)
    email = mapped_column(String(254))

    # Foreign key
    user_id = mapped_column(ForeignKey('user.id'))

    # Relationships
    user = relationship('User', back_populates='person')
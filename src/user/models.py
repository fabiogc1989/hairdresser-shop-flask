from src.extensions import Base, db
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, relationship

class User(Base, db.Model):
    __tablename__ = 'user'

    username = mapped_column(String(256), nullable=False, unique=True)
    password = mapped_column(String(256), nullable=False)

    # Relationships
    person = relationship('Person', back_populates='user')
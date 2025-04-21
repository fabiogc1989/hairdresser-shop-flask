from configs import AppConfig
from sqlalchemy import Integer, String, Double, DateTime, create_engine, ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship


class Base(DeclarativeBase):
    id = mapped_column(Integer, primary_key=True)
    created_by = mapped_column(String(256), nullable=False)
    created_at = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )
    modified_by = mapped_column(String(256))
    modified_at = mapped_column(DateTime(timezone=True))


class User(Base):
    __tablename__ = 'user'

    username = mapped_column(String(256), nullable=False, unique=True)
    password = mapped_column(String(256), nullable=False)

    # Relationships
    person = relationship('Person', back_populates='user')


class Person(Base):
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
    person = relationship('Person', back_populates='employee')


class ShopService(Base):
    __tablename__ = 'shop_service'

    name = mapped_column(String(256), nullable=False, unique=True)
    description = mapped_column(String(256))
    price = mapped_column(Double, nullable=False)


if __name__ == '__main__':
    print('Creating database...')
    engine = create_engine(AppConfig.SQLALCHEMY_DATABASE_URI)
    Base.metadata.create_all(bind = engine)
    print('Done')

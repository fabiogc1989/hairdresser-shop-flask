from src.extensions import Base, db
from sqlalchemy import String, Double
from sqlalchemy.orm import mapped_column

class ShopService(Base, db.Model):
    __tablename__ = 'shop_service'

    name = mapped_column(String(256), nullable=False, unique=True)
    description = mapped_column(String(256))
    price = mapped_column(Double, nullable=False)
from typing import List
from src.extensions import db
from src.shop_service.models import ShopService
from sqlalchemy import select, ScalarResult


def get_shop_services() -> ScalarResult[List[ShopService]]:
    return db.session.execute(select(ShopService)).scalars()


def get_shop_service_by_id(id):
    pass


def delete_shop_service_by_id(id):
    pass


def create_shop_service():
    pass


def update_shop_service():
    pass
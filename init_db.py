from sqlalchemy import create_engine
from configs import AppConfig
from src.extensions import db

import src.shop_service.models
import src.user.models
import src.person.models
import src.person.customer.models
import src.person.employee.models


if __name__ == '__main__':
    print('Creating database...')
    engine = create_engine(AppConfig.SQLALCHEMY_DATABASE_URI)
    db.metadata.create_all(engine)
    print('Done')

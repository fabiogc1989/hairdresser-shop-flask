from src.extensions import db, engine

import src.shop_service.models
import src.user.models
import src.person.models


if __name__ == '__main__':
    print('Creating database...')
    db.metadata.create_all(engine)
    print('Done')

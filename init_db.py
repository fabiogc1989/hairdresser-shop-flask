from sqlalchemy import create_engine
from src.configs import AppConfig
from src.extensions import Base


if __name__ == '__main__':
    print('Creating database...')
    engine = create_engine(AppConfig.SQLALCHEMY_DATABASE_URI)
    Base.metadata.create_all(bind = engine)
    print('Done')

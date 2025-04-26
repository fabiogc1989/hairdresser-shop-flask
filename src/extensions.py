from configs import AppConfig
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, DateTime, func, create_engine
from sqlalchemy.orm import DeclarativeBase, mapped_column


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


db = SQLAlchemy(model_class = Base)

engine = create_engine(AppConfig.SQLALCHEMY_DATABASE_URI)
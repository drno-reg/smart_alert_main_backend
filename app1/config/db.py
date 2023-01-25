import os

from sqlalchemy import (
    MetaData,
    create_engine
)

from databases import Database

DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URI")

# SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)
metadata = MetaData()

# databases query builder
database = Database(DATABASE_URL)
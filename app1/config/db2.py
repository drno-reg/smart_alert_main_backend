import os

from sqlalchemy import create_engine, MetaData

# DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URI")

DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URI")

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()
conn = engine.connect()
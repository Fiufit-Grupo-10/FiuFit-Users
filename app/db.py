import os

from databases import Database
from sqlalchemy import (Column, Integer, DateTime, String, Table, create_engine, MetaData)
from sqlalchemy.sql import func

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("last_name", String(50)),
    Column("description", String(100)),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)


db = Database(DATABASE_URL)


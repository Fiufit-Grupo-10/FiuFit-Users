from sqlalchemy import Column, String


from .database import Base


class User(Base):
    __tablename__ = "users"

    email = Column(String, unique=True, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

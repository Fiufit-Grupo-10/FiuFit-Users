from sqlalchemy import Column, Integer, PrimaryKeyConstraint, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"

    uid = Column(String, unique=True, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    birthday = Column(String, nullable=True)  # Fix type
    height = Column(Integer, nullable=True)
    weight = Column(Integer, nullable=True)
    gender = Column(String, nullable=True)
    target = Column(String, nullable=True)
    level = Column(String, nullable=True)
    latitude = Column(String, nullable=True)
    longitude = Column(String, nullable=True)

    interests = relationship("UserInterest", back_populates="owner")


class Interest(Base):
    __tablename__ = "interests"

    name = Column(String, primary_key=True, unique=True, index=True)
    desc = Column(String)


class UserInterest(Base):
    __tablename__ = "user_interests"

    user = Column(String, ForeignKey("users.username"), primary_key=True)
    interest = Column(String, ForeignKey("interests.name"), primary_key=True)

    __table_args__ = (PrimaryKeyConstraint("user", "interest"),)

    owner = relationship("User", back_populates="interests")

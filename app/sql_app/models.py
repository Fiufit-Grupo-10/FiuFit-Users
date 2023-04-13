from sqlalchemy import (
    Column,
    Integer,
    PrimaryKeyConstraint,
    String,
    ForeignKey,
    DECIMAL,
    Date,
    Text,
)
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"

    uid = Column(String(length=50), unique=True, primary_key=True, index=True)
    email = Column(String(length=100), unique=True, index=True)
    username = Column(String(length=50), unique=True, index=True)
    birthday = Column(Date, nullable=True)
    height = Column(Integer, nullable=True)
    weight = Column(Integer, nullable=True)
    gender = Column(String(length=1), nullable=True)
    target = Column(String, nullable=True)
    level = Column(String, nullable=True)
    latitude = Column(DECIMAL(9, 6), nullable=True)
    longitude = Column(DECIMAL(9, 6), nullable=True)
    user_type = Column(String(length=7), nullable=True)

    trainingtypes = relationship("UserTrainingType", back_populates="owner")


class TrainingType(Base):
    __tablename__ = "trainingtypes"

    name = Column(String(length=50), primary_key=True, unique=True, index=True)
    desc = Column(Text)


class UserTrainingType(Base):
    __tablename__ = "user_trainingtype"

    user = Column(String, ForeignKey("users.username"), primary_key=True)
    trainingtype = Column(String, ForeignKey("trainingtypes.name"), primary_key=True)

    __table_args__ = (PrimaryKeyConstraint("user", "trainingtype"),)

    owner = relationship("User", back_populates="trainingtypes")


class Admin(Base):
    __tablename__ = "admins"

    uid = Column(String(length=50), unique=True, primary_key=True, index=True)
    email = Column(String(length=100), unique=True, index=True)
    username = Column(String(length=50), unique=True, index=True)

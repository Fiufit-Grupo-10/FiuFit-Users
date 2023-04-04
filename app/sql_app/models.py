from sqlalchemy import Column, Integer, PrimaryKeyConstraint, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"

    email = Column(String, unique=True, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    height = Column(Integer, nullable=True)
    weight = Column(Integer, nullable=True)
    gender = Column(String, nullable=True)
    target = Column(String, nullable=True)

    interests = relationship("Interest", back_populates="owner")

    


class Interest(Base):
    __tablename__ = "interests"

    user = Column(String, ForeignKey("users.username"), primary_key=True)
    name = Column(String, primary_key=True)

    __table_args__ = (PrimaryKeyConstraint("user", "name"),)

    owner = relationship("User", back_populates="interests")
    

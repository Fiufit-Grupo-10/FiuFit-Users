from sqlalchemy import (
    Column,
    Float,
    Integer,
    PrimaryKeyConstraint,
    String,
    ForeignKey,
    Date,
    Boolean,
)
from sqlalchemy.orm import relationship
from ...config.database import Base


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
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    user_type = Column(String(length=7), nullable=True)
    image_url = Column(String, nullable=True)
    token = Column(String, nullable=True)
    blocked = Column(Boolean, default=False)
    certified = Column(Boolean, default=False)

    trainingtypes = relationship(
        "UserTrainingType",
        back_populates="owner",
        cascade="all, delete, delete-orphan",
        passive_deletes=True,
    )


class UserTrainingType(Base):
    __tablename__ = "user_trainingtype"

    username = Column(
        String,
        ForeignKey("users.username", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    )
    trainingtype = Column(
        String,
        ForeignKey("trainingtypes.name", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    )

    __table_args__ = (PrimaryKeyConstraint("username", "trainingtype"),)

    owner = relationship("User", back_populates="trainingtypes")


class FollowingRelationship(Base):
    __tablename__ = "following_relationships"

    followed_uid = Column(
        String,
        ForeignKey("users.uid", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    )
    follower_uid = Column(
        String,
        ForeignKey("users.uid", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    )

    __table_args__ = (PrimaryKeyConstraint("followed_uid", "follower_uid"),)

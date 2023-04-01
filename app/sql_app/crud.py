from sqlalchemy.orm import Session
from . import models, schemas


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    db_user = models.User(
        email=user.email, username=user.username, password=user.password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

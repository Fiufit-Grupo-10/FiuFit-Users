from sqlalchemy.orm import Session
from . import models, schemas


def create_user(db: Session, user: schemas.User) -> models.User:
    new_user = models.User(id=user.id,email=user.email, username=user.username)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def update_user(db: Session, user: schemas.User) -> models.User:
    old_user = db.query(models.User).filter_by(username=user.username).first()
    if old_user is None:
        return create_user(db, user)

    else:
        old_user.height = user.height
        old_user.weight = user.weight
        old_user.gender = user.gender
        old_user.target = user.target
        db.commit()
        add_user_interests(db, user)
        db.refresh(old_user)
        return old_user


def add_user_interests(db: Session, user: schemas.User):
    for interest in user.interests:
        db.add(models.Interest(user=user.username, name=interest))
        db.commit()

def get_user(db: Session,user_id: str) -> models.User:
    return db.query(models.User).filter(models.User.id == user_id).first() 
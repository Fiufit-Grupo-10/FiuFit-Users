from sqlalchemy.orm import Session
from . import models, schemas


def create_user(db: Session, user: schemas.UserRequest, uid: str) -> models.User:
    new_user = models.User(uid= uid, email=user.email, username=user.username)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def update_user(db: Session, user: schemas.UserRequest, uid: str) -> models.User:
    old_user = get_user(db,uid)
    old_user.height = user.height
    old_user.weight = user.weight
    old_user.gender = user.gender
    old_user.target = user.target
    old_user.birthday = user.birthday
    old_user.level = user.level
    old_user.latitude = user.latitude
    old_user.longitude = user.longitude
    old_user.user_type = user.user_type
    db.commit()
    update_user_training_types(db, user)
    db.refresh(old_user)
    return old_user


def update_user_training_types(db: Session, user: schemas.UserRequest):
    rows_to_delete = db.query(models.UserTrainingType).filter_by(user=user.username).all()
    for row in rows_to_delete:
        db.delete(row)
    db.commit()
    for trainingtype in user.trainingtypes:
        db.add(models.UserTrainingType(user=user.username, trainingtype=trainingtype))
        db.commit()


def get_user(db: Session, user_id: str) -> models.User:
    return db.query(models.User).filter(models.User.uid == user_id).first()


def get_training_types(db: Session):
    return db.query(models.TrainingType).all()

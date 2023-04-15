from sqlalchemy.orm import Session
from . import models, schemas


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    new_user = models.User(uid=user.uid, email=user.email, username=user.username)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def update_user(db: Session, user: schemas.UserRequest, uid: str) -> models.User:
    old_user = get_user(db, uid)
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
    rows_to_delete = (
        db.query(models.UserTrainingType).filter_by(username=user.username).all()
    )
    for row in rows_to_delete:
        db.delete(row)
    db.commit()
    for trainingtype in user.trainingtypes:
        db.add(
            models.UserTrainingType(username=user.username, trainingtype=trainingtype)
        )
        db.commit()


def get_user(db: Session, user_id: str) -> models.User:
    return db.query(models.User).filter(models.User.uid == user_id).first()

def get_users(db: Session):
    return db.query(models.User).all()

def get_training_types(db: Session):
    return db.query(models.TrainingType).all()


def create_admin(db: Session, admin: schemas.AdminCreate) -> models.Admin:
    new_admin = models.Admin(uid=admin.uid, email=admin.email, username=admin.username)
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return new_admin


def get_admin(db: Session, uid: str) -> models.Admin:
    return db.query(models.Admin).filter(models.Admin.uid == uid).first()


def get_admins(db: Session):
    return db.query(models.Admin).all()

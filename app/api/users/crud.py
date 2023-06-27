from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from . import models, schemas


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    new_user = models.User(
        uid=user.uid,
        email=user.email,
        username=user.username,
        birthday=user.birthday,
        height=user.height,
        weight=user.weight,
        target=user.target,
        level=user.level,
        latitude=user.latitude,
        longitude=user.longitude,
        user_type=user.user_type,
        image_url=user.image_url,
        token=user.token,
        blocked=user.blocked,
        certified=user.certified,
    )
    db.add(new_user)
    db.commit()
    try:
        update_user_training_types(db, user)
    except Exception as e:
        db.delete(new_user)
        db.commit()
        raise e
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
    old_user.image_url = user.image_url
    old_user.token = user.token
    old_user.blocked = user.blocked
    old_user.username = user.username
    old_user.email = user.email
    db.commit()
    try:
        update_user_training_types(db, user)
    except Exception as e:
        raise e
    db.refresh(old_user)
    return old_user


def update_user_training_types(db: Session, user: schemas.UserRequest):
    rows_to_delete = (
        db.query(models.UserTrainingType).filter_by(username=user.username).all()
    )
    for row in rows_to_delete:
        db.delete(row)
    if user.trainingtypes is None:
        return
    for trainingtype in user.trainingtypes:
        db.add(
            models.UserTrainingType(username=user.username, trainingtype=trainingtype)
        )
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise Exception(f"{trainingtype}")


def add_user_follower(
    db: Session, followed_uid: str, follower_uid: str
) -> models.FollowingRelationship:
    new_following_relationship = models.FollowingRelationship(
        followed_uid=followed_uid, follower_uid=follower_uid
    )
    db.add(new_following_relationship)
    db.commit()
    db.refresh(new_following_relationship)
    return new_following_relationship


def delete_user_follower(db: Session, followed_uid: str, follower_uid: str):
    following_relationship = (
        db.query(models.FollowingRelationship)
        .filter_by(followed_uid=followed_uid, follower_uid=follower_uid)
        .first()
    )
    if following_relationship is None:
        return
    db.delete(following_relationship)
    db.commit()


def get_users_followers(db: Session, uid: str) -> list[models.FollowingRelationship]:
    return (
        db.query(models.FollowingRelationship)
        .filter(models.FollowingRelationship.followed_uid.like(uid))
        .all()
    )


def get_users_following(db: Session, uid: str) -> list[models.FollowingRelationship]:
    return (
        db.query(models.FollowingRelationship)
        .filter(models.FollowingRelationship.follower_uid.like(uid))
        .all()
    )


def update_user_block(users: list[schemas.UserBlock], db: Session) -> list[models.User]:
    updated_users = []
    for user in users:
        old_user = get_user(db, user.uid)
        old_user.blocked = user.blocked
        db.commit()
        updated_users.append(old_user)

    return updated_users


def update_user_certified(uid: str, db: Session, certified: bool):
    old_user = get_user(db=db, user_id=uid)
    old_user.certified = certified
    db.commit()


def get_user(db: Session, user_id: str) -> models.User:
    return db.query(models.User).filter(models.User.uid == user_id).first()


def get_users(db: Session, skip: int, limit: int) -> list[models.User]:
    return db.query(models.User).offset(skip).limit(limit).all()


def get_trainers(db: Session, skip: int = 0, limit: int = 10) -> list[models.User]:
    return (
        db.query(models.User)
        .filter(models.User.user_type == "trainer")
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_users_by_username(
    db: Session, skip: int, limit: int, username: str
) -> list[models.User]:
    return (
        db.query(models.User)
        .filter(models.User.username.ilike(f"{username}%"))
        .offset(skip)
        .limit(limit)
        .all()
    )

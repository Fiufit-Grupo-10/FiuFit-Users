from sqlalchemy.orm import Session
from app.api.admins import schemas, models


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

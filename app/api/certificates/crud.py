from sqlalchemy.orm import Session
from . import models, schemas


def load_certificate(
    db: Session, certificate: schemas.CertificateRequest, uid: str
) -> models.Certificate:
    new_certificate = models.Certificate(
        uid=uid, state=certificate.state, link=certificate.link
    )
    db.add(new_certificate)
    db.commit()
    db.refresh(new_certificate)
    return new_certificate


def update_certificate(
    db: Session, certificate: schemas.CertificateRequest, id: int, uid: str
) -> models.Certificate:
    old_certificate = (
        db.query(models.Certificate)
        .filter(models.Certificate.id == id, models.Certificate.uid == uid)
        .first()
    )
    if old_certificate is None:
        return None
    old_certificate.state = certificate.state
    old_certificate.link = certificate.link
    db.commit()
    db.refresh(old_certificate)
    return old_certificate


def get_certificates(db: Session, uid: str) -> list[models.Certificate]:
    return db.query(models.Certificate).filter(models.Certificate.uid.like(uid)).all()


def get_all_certificates(
    db: Session, skip: int, limit: int
) -> list[models.Certificate]:
    return db.query(models.Certificate).offset(skip).limit(limit).all()

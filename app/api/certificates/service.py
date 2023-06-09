from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from . import schemas, crud, models
from app.api.users.crud import update_user_certified
from app.config.config import logger


def load_certificate(
    certificate: schemas.CertificateRequest, uid: str, db: Session
) -> models.Certificate:
    logger.info("Reaching previous requests", uid=uid)
    previous_request = crud.get_certificates(db=db, uid=uid)

    for request in previous_request:
        if request.state is None or request.state:
            logger.info("Request open or approved found", uid=uid)
            raise Exception("Certificate request for uid: '{uid}' is still active")

    try:
        logger.info("Loading certificate", uid=uid)
        return crud.load_certificate(certificate=certificate, db=db, uid=uid)
    except IntegrityError:
        raise


def update_certificate(
    certificate: schemas.CertificateRequest, db: Session, id: int, uid: str
) -> models.Certificate:
    try:
        logger.info("Reaching previous certificate request", uid=uid)
        certificate = crud.update_certificate(
            certificate=certificate, db=db, id=id, uid=uid
        )
        if certificate is None:
            return None
        if certificate.state:
            logger.info("Updating state in users data", uid=uid)
            update_user_certified(uid=uid, certified=certificate.state, db=db)
        return certificate
    except Exception:
        raise


def get_certificate(uid: str, db: Session):
    try:
        requests = crud.get_certificates(db=db, uid=uid)
        for request in requests:
            if request.state is None or request.state:
                return request

    except Exception:
        raise

    return None

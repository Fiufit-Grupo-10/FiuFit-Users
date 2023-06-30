from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from . import service, crud
from app.dependencies import get_db
from . import schemas
from app.config.config import logger


router = APIRouter(tags=["certificates"])


@router.post(
    "/certificates/{user_id}",
    response_model=schemas.CertificateReturn,
    status_code=status.HTTP_201_CREATED,
)
def load_certificate(
    certificate: schemas.CertificateRequest, user_id: str, db: Session = Depends(get_db)
):
    logger.info("Post certificate request", uid=user_id)
    try:
        return service.load_certificate(certificate=certificate, db=db, uid=user_id)
    except IntegrityError:
        logger.info("Post certificate request failed, uid not found", uid=user_id)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with uid: '{user_id}' not found",
        )
    except Exception as e:
        logger.info("Post certificate request failed, conflict", uid=user_id)
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))


@router.put(
    "/certificates/{user_id}/{id}",
    response_model=schemas.CertificateReturn,
    status_code=status.HTTP_200_OK,
)
def update_certificate(
    user_id: str,
    id: int,
    certificate: schemas.CertificateRequest,
    db: Session = Depends(get_db),
):
    logger.info("Update certificate request", uid=user_id)
    try:
        certificate = service.update_certificate(
            certificate=certificate, db=db, id=id, uid=user_id
        )
        if certificate is None:
            logger.info("Reaching previous certificate request failed", uid=user_id)
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with uid:{user_id} does not have an open request",
            )
        return certificate
    except IntegrityError:
        logger.info("User id not found", uid=user_id)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with uid:{user_id} not found",
        )


@router.get(
    "/certificates/{user_id}",
    response_model=schemas.CertificateReturn,
    status_code=status.HTTP_200_OK,
)
def get_user_certificate(user_id: str, db: Session = Depends(get_db)):
    logger.info("Get certificate request", uid=user_id)
    try:
        logger.info("Reaching certificate request", uid=user_id)
        certificate = service.get_certificate(uid=user_id, db=db)
        if certificate is None:
            logger.info("Reaching certificate request failed", uid=user_id)
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with uid:{user_id} does not have an open request",
            )
        return certificate
    except IntegrityError:
        logger.info("User id not found", uid=user_id)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with uid:{user_id} not found",
        )


@router.get(
    "/certificates",
    response_model=list[schemas.CertificateReturn],
    status_code=status.HTTP_200_OK,
)
def get_certificates(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    logger.info("Get certificates request")
    return crud.get_all_certificates(skip=skip, limit=limit, db=db)

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from . import crud
from app.dependencies import get_db
from app.api.users.utils import raise_integrity_error
from . import schemas
from app.config.config import logger

router = APIRouter(tags=["admins"])


@router.post(
    "/admins", response_model=schemas.AdminResponse, status_code=status.HTTP_201_CREATED
)
def create_admin(admin: schemas.AdminCreate, db: Session = Depends(get_db)):
    logger.info("Post admin request", uid=admin.uid)
    try:
        return crud.create_admin(db=db, admin=admin)
    except IntegrityError as e:
        logger.info("Post admin request failed", uid=admin.uid)
        raise_integrity_error(
            e, uid=admin.uid, username=admin.username, email=admin.email, type="Admin"
        )


@router.get(
    "/admins",
    response_model=list[schemas.AdminResponse],
    status_code=status.HTTP_200_OK,
)
def get_admins(db: Session = Depends(get_db)):
    logger.info("Get admins request")
    return crud.get_admins(db=db)


@router.get(
    "/admins/{user_id}",
    response_model=schemas.AdminResponse,
    status_code=status.HTTP_200_OK,
)
def get_admin(user_id: str, db: Session = Depends(get_db)):
    logger.info("Get admin request", uid=user_id)
    admin = crud.get_admin(db=db, uid=user_id)
    if admin is None:
        logger.info("Get admin request failed", uid=user_id)
        detail = f"Admin {user_id} not found"
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
    return admin

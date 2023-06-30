from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.api.training_types import schemas, crud
from app.dependencies import get_db
from app.config.config import logger


router = APIRouter(tags=["trainingtypes"])


@router.get(
    "/trainingtypes",
    response_model=list[schemas.TrainingType],
    status_code=status.HTTP_200_OK,
)
def get_training_types(db: Session = Depends(get_db)):
    logger.info("Training types request")
    return crud.get_training_types(db=db)

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.dependencies import get_db
from ..sql_app import crud, schemas


router = APIRouter(tags=["trainingtypes"])


@router.get("/trainingtypes", response_model=list[schemas.TrainingType])
def get_interests(db: Session = Depends(get_db)):
    return crud.get_training_types(db=db)

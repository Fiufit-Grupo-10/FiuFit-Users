from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.dependencies import get_db
from ..sql_app import crud, schemas


router = APIRouter(tags=['interests'])


@router.get("/interests", response_model= list[schemas.Interest])
def get_interests(db: Session = Depends(get_db)):
    return crud.get_interests(db=db)
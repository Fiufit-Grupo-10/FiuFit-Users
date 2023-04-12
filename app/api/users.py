from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.dependencies import get_db
from ..sql_app import crud, schemas


router = APIRouter(tags=["users"])


@router.post("/users", response_model=schemas.UserReturn)
def create_user(user: schemas.UserCreate,db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@router.put("/users/{user_id}", response_model=schemas.UserReturn)
def update_user(user: schemas.UserRequest, user_id: str, db: Session = Depends(get_db)):
    return crud.update_user(db=db, user=user,uid=user_id)


@router.get("/users/{user_id}", response_model=schemas.UserReturn)
def get_user(user_id: str, db: Session = Depends(get_db)):
    return crud.get_user(db=db, user_id=user_id)

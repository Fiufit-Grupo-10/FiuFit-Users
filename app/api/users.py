from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.sql_app.database import SessionLocal
from ..sql_app import crud, schemas


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.post("/users", response_model=schemas.User)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@router.put("/users", response_model=schemas.User)
def update_user(user: schemas.User, db: Session = Depends(get_db)):
    return crud.update_user(db=db, user=user)

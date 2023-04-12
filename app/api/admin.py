from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.dependencies import get_db
from ..sql_app import crud, schemas


router = APIRouter(tags=["admins"])


@router.post("/admin/{user_id}", response_model=schemas.AdminResponse)
def create_admin(admin: schemas.AdminRequest, user_id: str,db: Session = Depends(get_db)):
    return crud.create_admin(db=db, admin = admin, uid = user_id)


@router.get("/admin", response_model= list[schemas.AdminResponse])
def get_admins(db: Session = Depends(get_db)):
    return crud.get_admins(db=db)

@router.get("/admin/{user_id}", response_model= schemas.AdminResponse)
def get_admin(user_id: str,db: Session = Depends(get_db)):
    return crud.get_admin(db=db, uid = user_id)
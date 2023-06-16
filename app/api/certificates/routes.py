from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from . import service,crud
from app.dependencies import get_db
from . import schemas


router = APIRouter(tags=["certificates"])


@router.post("/certificates", response_model=schemas.Certificate, status_code=201)
def load_certificate(certificate: schemas.Certificate, db: Session = Depends(get_db)):
    try:
        return service.load_certificate(certificate=certificate,db=db)
    except IntegrityError as _:
        raise HTTPException(status_code=404, detail=f"User with uid:{certificate.uid} does not exist")
    except Exception as e:
        raise HTTPException(status_code=409, detail=str(e))
    
    
@router.put("/certificates/{id}", response_model=schemas.Certificate, status_code=200)
def load_certificate(id: int,certificate: schemas.Certificate, db: Session = Depends(get_db)):
    try:
        return service.update_certificate(certificate=certificate,db=db)
    except IntegrityError as _:
        raise HTTPException(status_code=404, detail=f"Certificate: with id{id} does not exist")
    
    
        

@router.get("/certificates/{user_id}", response_model=schemas.Certificate, status_code=200)
def get_user_certificate(user_id: str, db: Session = Depends(get_db)):
    try:
        certificate = service.get_certificate(uid=user_id,db=db)
        if certificate is None:
            raise HTTPException(status_code=404, detail=f"User with uid:{user_id} does not have an open request")
        return certificate
    except IntegrityError as _:
        raise HTTPException(status_code=404, detail=f"User with uid:{user_id} does not exist")
    
@router.get("/certificates", response_model=list[schemas.Certificate], status_code=200)
def get_certificates(skip: int = 0,limit: int = 10,db: Session = Depends(get_db)):
    return crud.get_all_certificates(skip=skip,limit=limit,db=db)
    

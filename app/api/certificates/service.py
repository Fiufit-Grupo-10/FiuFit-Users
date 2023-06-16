from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from . import schemas, crud, models


def load_certificate(certificate: schemas.Certificate, db: Session) -> models.Certificate:
    previous_request = crud.get_certificates(db=db,uid=certificate.uid)
    for request in previous_request:
        if not request.state:
            raise Exception("Certificate request for uid {certificate.uid} is still active")
        
    try:
        return crud.load_certificate(certificate=certificate,db=db)    
    except IntegrityError as e:
        raise
    
    
def update_certificate(certificate: schemas.Certificate, db: Session,id:int) -> models.Certificate:
    try:
        crud.update_certificate(certificate=certificate,db=db,id=id)
    except:
        raise    
    
    
def get_certificate(uid: str,db: Session):
    try:
        requests = crud.get_certificates(db=db,uid=uid)
        for request in requests:
            if request.state is None:
                return request
    
    except Exception:
        raise
    
    return None
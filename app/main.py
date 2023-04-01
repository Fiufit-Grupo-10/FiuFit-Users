from fastapi import FastAPI, Depends
from app.api import ping
from sqlalchemy.orm import Session
from .sql_app.database import SessionLocal, engine
from .sql_app import crud, models, schemas

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def default():
    return {"welcome": "working"}


@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


app.include_router(ping.router)

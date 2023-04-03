from fastapi import FastAPI
from app.api import users
from .sql_app.database import engine
from .sql_app import models

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
def default():
    return {"welcome": "working"}


app.include_router(users.router)

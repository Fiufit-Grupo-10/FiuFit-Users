from fastapi import FastAPI
from app.api import training_types, users, admin
from .sql_app.database import engine
from .sql_app import models

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


app.include_router(users.router)
app.include_router(training_types.router)
app.include_router(admin.router)

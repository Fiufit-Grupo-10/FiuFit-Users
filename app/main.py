from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.api import training_types, users, admin
from .sql_app.database import engine
from .sql_app import models
from sqlalchemy.exc import IntegrityError

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.exception_handler(IntegrityError)
async def integrity_error_handler(request, exc):
    msg = f"uid {exc.params['uid']} already exists"
    content = {"detail": [{"loc": ["body", "uid"], "msg": msg, "type": "value.error"}]}
    return JSONResponse(status_code=409, content=content)


app.include_router(users.router)
app.include_router(training_types.router)
app.include_router(admin.router)

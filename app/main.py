from fastapi import FastAPI
from app.api.users import routes as users_routes
from app.api.users import models as users_models
from app.api.training_types import routes as training_type_routes
from app.api.training_types import models as training_types_models
from app.api.admins import routes as admins_routes
from app.api.admins import models as admins_models
from app.api.certificates import routes as certificate_routes
from app.api.certificates import models as certificate_models
from .config.database import engine

# Esto podria hacerse solo si se esta en develop/corriendo el ci (capaz no hace falta igual) 
users_models.Base.metadata.create_all(bind=engine)
admins_models.Base.metadata.create_all(bind=engine)
training_types_models.Base.metadata.create_all(bind=engine)
certificate_models.Base.metadata.create_all(bind=engine)
#
app = FastAPI()


app.include_router(users_routes.router)
app.include_router(training_type_routes.router)
app.include_router(admins_routes.router)
app.include_router(certificate_routes.router)

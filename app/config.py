import logging
from functools import lru_cache
from pydantic import Field, BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    enviroment: str = "dev"
    testing: bool = False


#    database_url: str = Field(..., env='DATABASE_URL')


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settins fron ENV")
    return Settings()

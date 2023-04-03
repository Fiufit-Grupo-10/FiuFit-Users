from pydantic import BaseModel


class Interest(BaseModel):
    name: str

    class Config:
        orm_mode = True


class User(BaseModel):
    email: str
    username: str
    height: int | None = None  # cm
    weight: int | None = None  # kg
    gender: str | None = None
    target: str | None = None
    interests: list[str] | None = None

    class Config:
        orm_mode = True

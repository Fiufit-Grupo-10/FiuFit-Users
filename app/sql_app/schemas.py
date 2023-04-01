from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    username: str
    password: str


class User(UserCreate):
    username: str
    # genero: str #Esto hay que hacer un enum
    # cumpleaños: str #Esto un datetime
    # altura: int # En cm
    # peso: int # En Kg

    class Config:
        orm_mode = True

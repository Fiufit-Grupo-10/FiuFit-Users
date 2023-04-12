from datetime import date
from pydantic import BaseModel, validator


class TrainingType(BaseModel):
    name: str
    desc: str

    class Config:
        orm_mode = True


class UserTrainingType(BaseModel):
    user: str
    trainingtype: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    username: str

class UserRequest(UserBase):
    birthday: date | None
    level: str | None
    latitude: float | None
    longitude: float | None
    height: int | None = None  # cm
    weight: int | None = None  # kg
    gender: str | None = None
    target: str | None = None
    trainingtypes: list[str] | None = None
    user_type: str | None

    class Config:
        orm_mode = True

class UserCreate(UserRequest):
    uid : str
    

class UserReturn(UserCreate):
    @validator("trainingtypes", pre=True)
    def extract_interests_names(cls, v):
        return [trainingtype.trainingtype for trainingtype in v]

class AdminRequest(UserBase):
    class Config:
        orm_mode = True

class AdminResponse(UserBase):
    uid: str
    class Config:
        orm_mode = True
        
class AdminCreate(AdminResponse):
    pass
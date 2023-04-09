from pydantic import BaseModel, validator


class Interest(BaseModel):
    name: str
    desc: str

    class Config:
        orm_mode = True


class UserInterest(BaseModel):
    user: str
    interest: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    uid: str
    email: str
    username: str
    birthday: str | None
    level: str | None
    latitude: str | None
    longitude: str | None
    height: int | None = None  # cm
    weight: int | None = None  # kg
    gender: str | None = None
    target: str | None = None
    interests: list[str] | None = None

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    pass


class User(UserBase):
    @validator("interests", pre=True)
    def extract_interests_names(cls, v):
        return [interest.interest for interest in v]

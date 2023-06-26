from datetime import date
from enum import Enum
from pydantic import BaseModel, Field, validator


class UserTrainingType(BaseModel):
    username: str
    trainingtype: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    username: str


class Gender(str, Enum):
    M = "M"
    F = "F"
    U = "U"
    
class UserType(str, Enum):
    athlete = "athlete"
    trainer = "trainer"


class UserRequest(UserBase):
    birthday: date | None = Field(default=None, description="format YYYY-MM-DD")
    level: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    height: int | None = Field(default=None, description="unit: cm")
    weight: int | None = Field(default=None, description="unit: kg")
    gender: Gender | None = Field(default=None, max_length=1)
    target: str | None = None
    trainingtypes: list[str] | None = None
    user_type: UserType | None = Field(default=None, max_length=7)
    image_url: str | None = Field(default=None)
    token: str | None = Field(default=None)
    blocked: bool | None = Field(default=False)
    certified: bool | None = Field(default=False)

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "email": "user@mail.com",
                "username": "user",
                "birthday": "2000-12-21",
                "level": "amateur",
                "latitude": 50,
                "longitude": 50,
                "height": 180,
                "weight": 80,
                "gender": "M",
                "target": "loss fat",
                "trainingtypes": ["Cardio"],
                "user_type": "athlete",
                "image_url": "image.com",
                "token": "token_example",
                "blocked": False,
                "certified": False,
            }
        }


class UserCreate(UserRequest):
    uid: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "uid": "10",
                "email": "user@mail.com",
                "username": "user",
                "birthday": "2000-12-21",
                "level": "amateur",
                "latitude": 50,
                "longitude": 50,
                "height": 180,
                "weight": 80,
                "gender": "M",
                "target": "loss fat",
                "trainingtypes": ["Cardio"],
                "user_type": "athlete",
                "image_url": "image.com",
                "token": "token_example",
                "blocked": False,
                "certified": False,
            }
        }


class UserReturn(UserCreate):
    @validator("trainingtypes", pre=True)
    def extract_interests_names(cls, v):
        return [trainingtype.trainingtype for trainingtype in v]


class FollowerReturn(BaseModel):
    followed_uid: str
    follower_uid: str


class UserBlock(BaseModel):
    uid: str
    blocked: bool

from pydantic import BaseModel, validator


class Interest(BaseModel):
    name: str

    class Config:
        orm_mode = True     
    

class UserBase(BaseModel):
    id : str
    email: str
    username: str
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
    @validator('interests', pre=True)
    def extract_interests_names(cls, v):
        return [interest.name for interest in v]
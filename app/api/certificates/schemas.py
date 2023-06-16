from pydantic import BaseModel, Field


class Certificate(BaseModel):
    id: int | None = Field(...)
    uid: str = Field(description="Trainer uid who requested the certificate")
    state: bool | None = Field(default=None,description="Indicates wheter the certificate has/has not/is pending to be aprroved")
    link: str = Field(description= "Link to video associated to the request")
    

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "uid": "10",
                "state": True,
                "link": "video.com"
            }
        }


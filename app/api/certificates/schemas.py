from pydantic import BaseModel, Field


class CertificateRequest(BaseModel):
    state: bool | None = Field(
        default=None,
        description="Indicates wheter the certificate has/has not/is pending to be aprroved",
    )
    link: str = Field(description="Link to video associated to the request")

    class Config:
        orm_mode = True
        schema_extra = {"example": {"state": True, "link": "video.com"}}


class CertificateReturn(CertificateRequest):
    id: int = Field(...)
    uid: str = Field(description="Trainer uid who requested the certificate")

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {"id": 5, "uid": "10", "state": True, "link": "video.com"}
        }

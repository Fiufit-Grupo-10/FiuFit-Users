from sqlalchemy import Boolean, ForeignKey, Integer, String, Column
from ...config.database import Base


class Certificate(Base):
    __tablename__ = "certificates"
    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(
        String(length=50),
        ForeignKey("users.uid", ondelete="CASCADE", onupdate="CASCADE"),
    )
    state = Column(Boolean)
    link = Column(String(length=200))

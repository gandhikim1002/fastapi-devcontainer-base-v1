from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import datetime


class UrlBase(SQLModel):
    long_url: str = Field(nullable=False)
    # expires_at: Optional[datetime] = None 
    # user_id: Optional[int] = None


class Url(UrlBase, table=True):
    __tablename__ = "urls"

    id: Optional[int] = Field(default=None, primary_key=True)
    short_code: str = Field(max_length=10, nullable=False, unique=True)
    # created_at: datetime = Field(default_factory=datetime.now(), nullable=False)
    # click_count: int = Field(default=0)
    

class UrlCreate(UrlBase):
    pass


class UrlInsert(UrlBase):
     short_code: str = Field(max_length=10, nullable=False, unique=True)


class UrlRedirect(UrlBase):
    pass


# class UrlUpdate(UrlBase):
    # expires_at: Optional[datetime] = None
    # click_count: int = Field(default=0)
    # user_id: Optional[int] = None


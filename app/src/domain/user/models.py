import uuid
from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel
from app.src.domain.item import models


class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    is_active: bool = True
    is_superuser: bool = False
    full_name: str | None = Field(default=None, max_length=255)


class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    hashed_password: str
    items: list["models.Item"] = Relationship(back_populates="owner", cascade_delete=True)


class UserCreate(UserBase):
    password: str

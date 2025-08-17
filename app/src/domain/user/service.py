import uuid
from fastapi import HTTPException
from sqlmodel import Session, select
from app.src.domain.user import models as user_models
from app.src.domain.item import models as item_models
from app.resources.strings import USER_DOES_NOT_EXIST_ERROR
from app.src.routers.auth import get_password_hash


def get_user_by_email(db: Session, email: str):
    return db.exec(select(user_models.User).where(user_models.User.email == email)).first()


def create_user(db: Session, user: user_models.UserCreate):
    fake_hashed_password = get_password_hash(user.password)
    db_user = user_models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.exec(select(user_models.User).offset(skip).limit(limit)).all()


def get_user(db: Session, user_id: uuid.UUID):
    return db.get(user_models.User, user_id)


def remove_user(db: Session, user_id: uuid.UUID):
    with db:
        db_user = db.get(user_models.User, user_id)
        if db_user is None:
            raise HTTPException(status_code=404, detail=USER_DOES_NOT_EXIST_ERROR)
        db.delete(db_user)
        db.commit()
    return {"ok": True}


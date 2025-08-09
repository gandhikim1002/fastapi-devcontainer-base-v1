import uuid
# from sqlalchemy.orm import Session
from sqlmodel import Session, select

from app.src.domain.user import models as user_models
from app.src.domain.item import models as item_models


def get_user(db: Session, user_id: uuid.UUID):
    # return db.query(models.User).filter(models.User.id == user_id).first()
    return db.exec(select(user_models.User).where(user_models.User.id == user_id)).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    # return db.query(models.User).offset(skip).limit(limit).all()
    return db.exec(select(user_models.User).offset(skip).limit(limit)).all()


def get_user_by_email(db: Session, email: str):
    # return db.query(models.User).filter(models.User.email == email).first()
    return db.exec(select(user_models.User).where(user_models.User.email == email)).first()


def create_user(db: Session, user: user_models.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = user_models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    # return db.query(models.Item).offset(skip).limit(limit).all()
    return db.exec(select(user_models.Item).offset(skip).limit(limit)).all()


def create_user_item(db: Session, item: item_models.ItemCreate, user_id: uuid.UUID):
    db_item = item_models.Item(**item.model_dump(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def remove_user(db: Session, db_user: user_models.User):
    db.delete(db_user)
    db.commit
    return True

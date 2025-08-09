import uuid

from sqlmodel import Session, select

from app.src.domain.item import models as item_models


def get_item(db: Session, item_id: uuid.UUID):
    return db.exec(select(item_models.Item).where(item_models.Item.id == item_id)).first()


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.exec(select(item_models.Item).offset(skip).limit(limit)).all()


def create_user_item(db: Session, item: item_models.ItemCreate, user_id: uuid.UUID):
    db_item = item_models.Item(**item.model_dump(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def remove_teim(db: Session, db_item: item_models.Item):
    db.delete(db_item)
    db.commit
    return True

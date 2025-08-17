import uuid
from fastapi import HTTPException
from sqlmodel import Session, select
from app.src.domain.item import models
from app.resources.strings import ITEM_DOES_NOT_EXIST_ERROR


def create_user_item(db: Session, item: models.ItemCreate, user_id: uuid.UUID):
    db_item = models.Item(**item.model_dump(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.exec(select(models.Item).offset(skip).limit(limit)).all()


def get_item(db: Session, item_id: uuid.UUID):
    db_item = db.get(models.Item, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail=ITEM_DOES_NOT_EXIST_ERROR)
    return db_item


def remove_item(db: Session, item_id: uuid.UUID):
    with db:
        db_item = db.get(models.Hero, item_id)
        if db_item is None:
            raise HTTPException(status_code=404, detail=ITEM_DOES_NOT_EXIST_ERROR)
        db.delete(db_item)
        db.commit()
    return {"ok": True}


import uuid

from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.src.dependencies import get_db
from app.src.domain.item import service, models


router = APIRouter(
    prefix="/items",
    tags=["items"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}})


@router.post("", response_model=models.Item)
def create_item(user_id: uuid.UUID, item: models.ItemCreate, db: Session = Depends(get_db)):
    return service.create_user_item(db, item, user_id)


@router.get("", response_model=List[models.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = service.get_items(db, skip, limit)
    return items


@router.get("/{item_id}", response_model=models.Item)
def read_item(item_id: uuid.UUID, db: Session = Depends(get_db)):
    return service.get_item(db, item_id)


@router.delete("/{item_id}", response_model=str)
def delete_user(item_id: uuid.UUID, db: Session = Depends(get_db)):
    return service.remove_item(db, item_id)


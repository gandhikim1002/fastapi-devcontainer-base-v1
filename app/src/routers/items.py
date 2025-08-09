import uuid

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.src.dependencies import get_token_header, get_db
from app.src.domain.item import service, models as item_models
from app.resources.strings import ITEM_DOES_NOT_EXIST_ERROR


router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/{item_id}", response_model=item_models.Item)
def read_item(item_id: uuid.UUID, db: Session = Depends(get_db)):
    db_item = service.get_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail=ITEM_DOES_NOT_EXIST_ERROR)
    return db_item


@router.get("/test/{item_id}", response_model=item_models.Item)
def read_item_test(item_id: uuid.UUID, db: Session = Depends(get_db)):
    db_item = service.get_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail=ITEM_DOES_NOT_EXIST_ERROR)
    return db_item

@router.get("/", response_model=List[item_models.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = service.get_items(db, skip=skip, limit=limit)
    return items

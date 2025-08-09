import uuid
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.src.dependencies import get_db
from app.src.domain.user import service, models as user_models
from app.src.domain.item import models as item_models


router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=user_models.User, status_code=201)
def create_user(user: user_models.UserCreate, db: Session = Depends(get_db)):
    db_user = service.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return service.create_user(db=db, user=user)


@router.get("/{user_id}", response_model=user_models.User)
def read_user(user_id: uuid.UUID, db: Session = Depends(get_db)):
    db_user = service.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/", response_model=List[user_models.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = service.get_users(db, skip=skip, limit=limit)
    return users


@router.delete("/{user_id}", response_model=bool)
def delete_user(user_id: uuid.UUID, db: Session = Depends(get_db)):
    db_user = service.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return service.remove_user(db, db_user=user_models.User)


@router.post("/users/{user_id}/items/", response_model=item_models.Item)
def create_item_for_user(
        user_id: uuid.UUID, item: item_models.ItemCreate, db: Session = Depends(get_db)
):
    return service.create_user_item(db=db, item=item, user_id=user_id)

import logging
from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List, Optional
from app.src.dependencies import get_db
from app.src.domain.hero import service, models


router = APIRouter(
    prefix="/heros",
    tags=["heros"],
    responses={404: {"description": "Not found"}})


@router.post("", response_model=models.Hero)
def create_hero(hero: models.HeroCreate, db: Session = Depends(get_db)):
    logging.info("======hero[", hero)
    return service.create_hero(db, hero)


@router.get("", response_model=List[models.Hero])
def read_heros(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_heros(db, skip, limit)


@router.get("/{hero_id}", response_model=models.Hero)
def read_hero(hero_id: int, db: Session = Depends(get_db)):
    return service.get_hero(db, hero_id)


@router.delete("/{hero_id}", response_model=str)
def delete_hero(hero_id: int, db: Session = Depends(get_db)):
    return service.remove_hero(db, hero_id)


@router.patch("", response_model=models.Hero)
def update_hero(hero: models.Hero, db: Session = Depends(get_db)):
    return service.update_hero(db, hero)


@router.post("/filter", response_model=List[models.Hero])
def read_filter_heros(
    name: Optional[str] = None,
    secret_name: Optional[str] = None,
    age_min: Optional[int] = None,
    age_max: Optional[int] = None,
    db: Session = Depends(get_db)):
    return service.get_filter_heros(db, name, secret_name, age_min, age_max)


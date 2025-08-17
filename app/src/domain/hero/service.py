from fastapi import HTTPException
from sqlmodel import Session, select
from typing import Optional
from app.src.domain.hero import models
from app.resources.strings import HERO_DOES_NOT_EXIST_ERROR


def create_hero(db: Session, hero: models.HeroCreate):
    db_hero = models.Hero(**hero.model_dump())
    db.add(db_hero)
    db.commit()
    db.refresh(db_hero)
    return db_hero


def get_heros(db: Session, skip: int = 0, limit: int = 100):
    return db.exec(select(models.Hero).offset(skip).limit(limit)).all()


def get_hero(db: Session, hero_id: int):
    db_hero = db.get(models.Hero, hero_id)
    if db_hero is None:
        raise HTTPException(status_code=404, detail=HERO_DOES_NOT_EXIST_ERROR)
    return db_hero


def remove_hero(db: Session, hero_id: int):
    with db:
        db_hero = db.get(models.Hero, hero_id)
        if db_hero is None:
            raise HTTPException(status_code=404, detail=HERO_DOES_NOT_EXIST_ERROR)
        db.delete(db_hero)
        db.commit()
    return {"ok": True}


def update_hero(db: Session, hero: models.Hero):
    with db:
        db_hero = db.get(models.Hero, hero.id)
        if db_hero is None:
            raise HTTPException(status_code=404, detail=HERO_DOES_NOT_EXIST_ERROR)
        
        convert(db_hero, hero)

        db.add(db_hero)
        db.commit()
        db.refresh(db_hero)
    return db_hero


def convert(db_hero: models.Hero, hero: models.Hero):
        db_hero.name = hero.name
        db_hero.secret_name = hero.secret_name
        db_hero.age = hero.age


def get_filter_heros(
        db: Session,
        name: Optional[str],
        secret_name: Optional[str],
        age_min: Optional[int],
        age_max: Optional[int]):
    
    query = select(models.Hero)

    if name:
        query = query.filter(models.Hero.name == name)
    if secret_name:
        query = query.filter(models.Hero.secret_name == secret_name)
    if age_min:
        query = query.filter(models.Hero.age >= age_min)
    if age_max:
        query = query.filter(models.Hero.age <= age_max)

    return db.exec(query).all()


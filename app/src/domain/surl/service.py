from sqlmodel import Session, select, func
from app.src.domain.surl import models
from app.src.s_url.short_url_v2 import id_to_short_url, short_url_to_id


def create_url(db: Session, url: models.UrlCreate):
    with db:
        db_url_cnt = db.exec(select(func.max(models.Url.id))).one_or_none()

        # when init db 
        if db_url_cnt is None:
            db_url_cnt = 0

        db_url_cnt += 1
        short_code = id_to_short_url(db_url_cnt)
        
        insert_url = convertCreateToInsert(url, short_code)

        db_url = models.Url(**insert_url.model_dump())
        db.add(db_url)
        db.commit()
        db.refresh(db_url)
        
        return db_url.short_code


def convertCreateToInsert(url: models.UrlCreate, short_code: str):
    return models.UrlInsert(
        long_url = url.long_url,
        short_code = short_code
        # expires_at = url.expires_at,
        # user_id = url.user_id
    )


def read_surl(db: Session, s_url: str):
    return db.exec(select(models.Url.long_url).where(models.Url.short_code == s_url)).first()

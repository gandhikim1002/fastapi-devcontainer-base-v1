from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlmodel import Session
from app.src.dependencies import get_db
import validators
from app.src.domain.surl import service, models


router = APIRouter(
    prefix="/surl",
    tags=["s-url"],
    responses={404: {"description": "Not found"}})


@router.post("", response_model=str)
def create_surl(url: models.UrlCreate, db: Session = Depends(get_db)):
    if not validators.url(url.long_url):
        raise HTTPException(status_code=400, detail="Invalid Url")
    
    short_url = service.create_url(db, url)
    return short_url


@router.get("/{s_url}", response_class=RedirectResponse)
def read_surl(s_url: str, db: Session = Depends(get_db)):
    long_url = service.read_surl(db, s_url)
    if long_url is None:
        raise HTTPException(status_code=400, detail="Invalid Url")
    return RedirectResponse(url=long_url)
    

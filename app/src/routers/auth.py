from datetime import datetime, timedelta
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.src.dependencies import get_db, jwt
from app.src.domain.user import service, models as user_models
from app.src.config import SECRET_KEY, ALGORITHM, JWT_EXPIRE_TIME


router = APIRouter(tags=["auth"])


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    data["hashed_password"] = ""
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=JWT_EXPIRE_TIME)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@router.post("/login/", response_model=dict)
def create_user(user: user_models.UserCreate, db: Session = Depends(get_db)):
    db_user = service.get_user_by_email(db, email=user.email)
    if db_user and user.password == db_user.hashed_password:
        raise HTTPException(status_code=400, detail="Email already registered")
    return {"Authorization": "Bearer " + create_access_token(user.model_dump())}

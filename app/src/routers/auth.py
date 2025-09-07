from datetime import datetime, timedelta
from typing import Optional
from passlib.context import CryptContext
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.src.dependencies import get_db, jwt
from app.src.domain.user import service, models as user_models
from app.src.config import SECRET_KEY, ALGORITHM, JWT_EXPIRE_TIME

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter(tags=["auth"])


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password) -> str:
    return pwd_context.hash(password)


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
def create_user(user: user_models.UserCreate, db: Session = Depends(get_db)) -> str:
    db_user = service.get_user_by_email(db, email=user.email)
    print("db_user[",db_user)
    if db_user and not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid auth")
    return {"Authorization": "Bearer " + create_access_token(user.model_dump())}

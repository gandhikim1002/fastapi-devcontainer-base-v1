import jwt
from fastapi import Header, HTTPException

from sqlmodel import Session
from app.src.database import engine
from app.src.config import SECRET_KEY, ALGORITHM


def decode(token):
    striped_token = token.replace("Bearer ", "")
    return jwt.decode(striped_token, SECRET_KEY, algorithms=[ALGORITHM])


def get_db():
    with Session(engine) as session:
        yield session


def get_db2():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()


async def get_token_header(x_token: str = Header(...)):
    try:
        payload = decode(x_token)
        username: str = payload.get("email")
        if username is None:
            raise HTTPException(status_code=403, detail="Unauthorized(None username)")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="Unauthorized(Expired time)") 
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=403, detail="Unauthorized(Invalid token)") 

from sqlmodel import SQLModel, create_engine
from app.src.config import DATABASE_URI


engine = create_engine(str(DATABASE_URI))


def conn():
    SQLModel.metadata.create_all(engine)

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager

from app.src.database import conn
from app.src.routers.api import router as router_api
from app.src.config import API_PREFIX, ALLOWED_HOSTS
from app.src.internal import admin
from app.src.dependencies import get_token_header
from app.src.routers.handlers.http_error import http_error_handler


@asynccontextmanager
async def lifespan(app: FastAPI):
    print('startup app')
    conn()
    yield
    print('shutdown app')

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(HTTPException, http_error_handler)

app.include_router(router_api, prefix=API_PREFIX)

app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


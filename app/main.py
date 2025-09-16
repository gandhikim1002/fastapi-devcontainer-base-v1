from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager

from app.src.database import conn
from app.src.routers.api import router as router_api
from app.src.config import API_PREFIX, ALLOWED_HOSTS
from app.src.internal import admin
from app.src.dependencies import get_token_header
from app.src.routers.handlers.http_error import http_error_handler
from app.src.custom_route import CustomRoute
from app.src.a_short_url import short_url
from app.src.b_qr_code import qr_code_routers

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('startup app')
    conn()
    yield
    print('shutdown app')

app = FastAPI(
    lifespan=lifespan, 
    route_class=CustomRoute
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(HTTPException, http_error_handler)

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(router_api, prefix=API_PREFIX)

app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)

app.include_router(
    short_url.router,
    prefix="/s-url",
    tags=["s-url"],
    responses={418: {"description": "I'm a teapot"}},
)

app.include_router(
    qr_code_routers.router,
    prefix="/qrcode",
    tags=["qrcode"],
    responses={418: {"description": "I'm a teapot"}},
)

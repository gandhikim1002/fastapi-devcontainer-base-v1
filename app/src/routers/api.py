from fastapi import APIRouter

from app.src.routers import items, users, auth, hero
from app.src.config import ROUTE_PREFIX_V1

router = APIRouter()


def include_api_routes():
    router.include_router(auth.router)
    router.include_router(items.router, prefix=ROUTE_PREFIX_V1)
    router.include_router(users.router, prefix=ROUTE_PREFIX_V1)
    router.include_router(hero.router, prefix=ROUTE_PREFIX_V1)


include_api_routes()

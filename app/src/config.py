from typing import List

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret


###
# Properties configurations
###

API_PREFIX = "/api"

JWT_TOKEN_PREFIX = "Authorization"

ROUTE_PREFIX_V1 = "/v1"

config = Config(".env")

ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default="",
)

# auth
SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')
JWT_EXPIRE_TIME = config('JWT_EXPIRE_TIME', cast=float)

# database
DATABASE_URI = config('DATABASE_URI', cast=Secret)

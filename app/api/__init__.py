from fastapi import APIRouter
from .endpoints import logs, math
api_router = APIRouter()
api_router.include_router(math.router)
api_router.include_router(logs.router)

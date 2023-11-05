from fastapi import APIRouter

from app.api.endpoints.v1 import root

api_router: APIRouter = APIRouter()

api_router.include_router(
    root.router,
    prefix=""
)

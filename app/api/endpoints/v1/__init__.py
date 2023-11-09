from fastapi import APIRouter

from app.api.endpoints.v1 import root, hematological_slides
from configuration.configs import settings

api_router: APIRouter = APIRouter()

api_router.include_router(
    root.router,
)

api_router.include_router(
    hematological_slides.router,
)

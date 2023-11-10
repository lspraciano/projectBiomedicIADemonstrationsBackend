from fastapi import APIRouter

from app.api.endpoints.v1 import root, hematological_slides, blood_serum, ki67, melanoma, sperm

api_router: APIRouter = APIRouter()

api_router.include_router(
    root.router,
)

api_router.include_router(
    hematological_slides.router,
)

api_router.include_router(
    blood_serum.router,
)

api_router.include_router(
    ki67.router,
)

api_router.include_router(
    melanoma.router,
)

api_router.include_router(
    sperm.router,
)

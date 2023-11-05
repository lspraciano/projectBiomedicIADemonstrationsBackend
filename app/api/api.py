from typing import Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.endpoints.v1 import api_router
from app.core.metadata.metadata import get_project_metadata
from configuration.configs import settings


def api_factory() -> FastAPI:
    """
    Creates a new FastAPI application.

    Returns:
        A new FastAPI application.
    """
    origins: list = ["*"]
    project_metadata: Dict = get_project_metadata()

    current_api: FastAPI = FastAPI(
        title=project_metadata["name"],
        description=project_metadata["description"],
        version=project_metadata["version"],
        swagger_ui_parameters={
            "defaultModelsExpandDepth": -1,
            "operationsSorter": "method",
            "filter": True,
            "docExpansion": None
        },
    )

    current_api.include_router(
        api_router
    )

    current_api.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["Detections"]
    )

    current_api: FastAPI = register_events(
        api=current_api
    )

    return current_api


def register_events(
        api: FastAPI
) -> FastAPI:
    """
    Register event handlers for a FastAPI application.

    This function registers event handlers for the FastAPI application,
    such as startup and shutdown events.

    Args:
        api (FastAPI): The FastAPI application instance.

    Returns:
        FastAPI: The FastAPI application with event handlers registered.
    """

    @api.on_event("startup")
    async def startup():
        print(f"Running Mode: {settings.APP_RUNNING_MODE}")

    @api.on_event("shutdown")
    async def shutdown():
        print(f"Closing Application")

    return api

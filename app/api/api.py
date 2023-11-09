from typing import Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.endpoints.v1 import api_router
from app.core.metadata.metadata import get_project_metadata
from configuration.configs import settings


def api_factory() -> FastAPI:
    """
    Creates a FastAPI application with CORS enabled and the specified project metadata.

    **Returns**

    A FastAPI application.
    """

    origins: list = ["*"]
    project_metadata: Dict = get_project_metadata()

    current_api: FastAPI = FastAPI(
        title=project_metadata["name"],
        description=project_metadata["description"],
        version=project_metadata["version"],
        docs_url=f"{settings.API_URL}/docs",
        servers=[
            {
                "url": f"http://34.172.245.118",
                "description": "Production environment"
            },
            {
                "url": f"http://127.0.0.1:8000",
                "description": "Development environment"
            },
        ],
        swagger_ui_parameters={
            "defaultModelsExpandDepth": -1,
            "operationsSorter": "method",
            "filter": True,
            "docExpansion": None,
        },
    )

    current_api.include_router(
        api_router,
        prefix=f"{settings.API_URL}"
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
    Registers startup and shutdown events for the specified FastAPI application.

    **Parameters**

    * **api** (FastAPI): The FastAPI application to register events for.

    **Returns**

    The FastAPI application with the events registered.
    """

    @api.on_event("startup")
    async def startup():
        print(f"Running Mode: {settings.APP_RUNNING_MODE}")

    @api.on_event("shutdown")
    async def shutdown():
        print(f"Closing Application")

    return api

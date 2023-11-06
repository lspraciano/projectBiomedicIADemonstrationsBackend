import asyncio
import sys
from asyncio import AbstractEventLoop
from typing import Generator

import pytest as pytest
import pytest_asyncio
from asgi_lifespan import LifespanManager
from httpx import AsyncClient

from app.main import app
from configuration.configs import settings

mock_image_path: str = settings.ROOT_PATH_FOR_DYNACONF + "/app/utils/images_handler/mock_image.jpg"

if (
        (
                "pytest" in sys.modules
                and
                settings.APP_RUNNING_MODE != "testing"
        )
        or
        (
                "pytest" not in sys.modules
                and
                settings.APP_RUNNING_MODE == "testing"
        )

):
    raise Exception(
        """
        If you are trying to run the application in test mode,
        use one of the commands:
         
        "python -m run_tests" 
        or
        "poetry run python -m run_tests".

        If this is not the case, check the IAHEMSCAN_APP_RUNNING_MODE
        environment variable and try again
        """
    )


@pytest_asyncio.fixture(
    scope="module"
)
async def async_client() -> Generator:
    """
    Creates an async client for the API.

    **Returns**

    An AsyncClient object.
    """

    async with AsyncClient(
            app=app,
            base_url=f"http://{settings.API_URL}"
    ) as client, LifespanManager(app):
        yield client


@pytest.fixture(
    scope="session"
)
def event_loop() -> Generator:
    """
    Creates an event loop.

    **Returns**

    An event loop object.
    """

    loop: AbstractEventLoop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

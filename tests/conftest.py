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

        If this is not the case, check the GLWAPI_APP_RUNNING_MODE
        environment variable and try again
        """
    )


@pytest_asyncio.fixture(
    scope="module"
)
async def async_client() -> Generator:
    """
    A fixture that provides an asynchronous client for testing.

    Returns:
        Generator: An asynchronous client that can be used for
        making asynchronous requests.
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
    A fixture that provides an asyncio event loop for testing.

    Returns:
        Generator: An asyncio event loop that can be used for asynchronous operations.
    """
    loop: AbstractEventLoop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

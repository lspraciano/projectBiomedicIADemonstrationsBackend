import os
import platform
import subprocess


async def _alembic_upgrade_head() -> None:
    """
    Asynchronous function to upgrade the database using Alembic.

    This function prints a message and then runs the "alembic upgrade head" command.

    Returns:
        None
    """
    print("Updating Database")

    subprocess.run(["alembic", "stamp", "base"])
    subprocess.run(["alembic", "upgrade", "head"])


async def _run_pytest() -> None:
    """
    Asynchronous function to run pytest for testing.

    This function prints a message and then runs the "pytest" command.

    Returns:
        None
    """
    print("Starting Tests")

    subprocess.run(["pytest"])


async def _drop_all_tables() -> None:
    """
    Asynchronous function to drop all tables in the database for testing.

    This function checks if the database URL contains the testing mode.
    If not, it raises an exception. It then resets the database by dropping
    all tables and disposes of the engine.

    Returns:
        None
    """
    db_url: str = str(engine_async.url)

    print(f"Target Database URL: {db_url}")

    if app_mode not in db_url:
        raise Exception("The detected database is not for testing.")

    print("Resetting the database")

    async with engine_async.begin() as conn:
        await conn.run_sync(
            ModelBase.metadata.drop_all
        )

    await engine_async.dispose()


async def _run_app_tests():
    """
    Asynchronous function to run application tests.

    This function sequentially performs the following tasks:
    1. Drops all tables in the database for testing using _drop_all_tables.
    2. Upgrades the database to the latest Alembic revision using _alembic_upgrade_head.
    3. Runs pytest for testing using _run_pytest.

    Returns:
        None
    """
    await _drop_all_tables()
    await _alembic_upgrade_head()
    await _run_pytest()


if __name__ == "__main__":
    app_mode: str = "testing"
    os.environ["BEQVISIONAPI_APP_RUNNING_MODE"] = app_mode

    import asyncio
    from app.core.database.database import engine_async, ModelBase
    from configuration.configs import settings
    from app.models import *

    print("RUNNING MODE: " + settings["APP_RUNNING_MODE"])

    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(_run_app_tests())

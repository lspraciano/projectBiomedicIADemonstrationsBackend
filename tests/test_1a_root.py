from typing import Dict

import pytest
from httpx import AsyncClient, Response

from app.core.metadata.metadata import get_project_metadata


@pytest.mark.asyncio
async def test_root_returns_correct_status_code(
        async_client: AsyncClient
):
    project_metadata: Dict = get_project_metadata()
    async_client.base_url = "http://"
    response: Response = await async_client.get(
        url="/",
        headers={
            "Content-Type": "application/json"
        },
    )

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_root_returns_correct_json(
        async_client: AsyncClient
):
    project_metadata: Dict = get_project_metadata()
    async_client.base_url = "http://"
    response: Response = await async_client.get(
        url="/",
        headers={
            "Content-Type": "application/json"
        },
    )

    response_json: Dict = response.json()

    assert response_json == {
        "status": "online",
        "name": project_metadata["name"],
        "version": project_metadata["version"],
        "description": project_metadata["description"],
        "authors": project_metadata["authors"],
        "documentation": project_metadata["documentation"]
    }

import os

import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch

os.environ.setdefault("OPENAI_API_KEY", "test-key")

from app.main import app  # noqa: E402 — env must be set before import
from app.models.schemas import ArtifactType, GenerateResponse, Requirement


@pytest.fixture(scope="module")
def client():
    return TestClient(app)


@pytest.fixture
def mock_response():
    return GenerateResponse(
        title="Test Project SRS",
        summary="Requirements specification for a test project.",
        requirements=[
            Requirement(id=1, type="FR", description="Users shall be able to register with email"),
            Requirement(id=2, type="NFR", description="API shall respond within 200ms at p95"),
        ],
        artifact_type=ArtifactType.SRS,
    )


@pytest.fixture
def mock_ai(mock_response):
    with patch("app.routers.generate.generate_artifacts", new_callable=AsyncMock) as m:
        m.return_value = mock_response
        yield m

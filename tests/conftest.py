import pytest
from fastapi.testclient import TestClient

from app.main import app
from clients.api_client import APIClient


@pytest.fixture
def api_client():
    client = TestClient(app)

    return APIClient(client)
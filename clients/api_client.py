from typing import Any

from fastapi.testclient import TestClient


class APIClient:
    """Reusable client for interacting with the SupportGuard API."""

    def __init__(self, client: TestClient):
        self.client = client

    def health_check(self):
        return self.client.get("/health")

    def chat(self, message: str):
        return self.client.post(
            "/api/chat",
            json={"message": message},
        )

    def post_chat(self, payload: dict[str, Any]):
        return self.client.post(
            "/api/chat",
            json=payload,
        )

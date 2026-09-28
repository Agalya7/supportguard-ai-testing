def validate_chat_response(data: dict) -> None:
    """Validate the basic structure of a chat API response."""

    assert isinstance(data, dict)
    assert "response" in data
    assert isinstance(data["response"], str)
    assert data["response"].strip() != ""
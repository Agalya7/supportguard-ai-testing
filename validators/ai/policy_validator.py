def validate_return_policy(response: str) -> None:
    """Validate that the AI response follows the known return policy."""

    response_lower = response.lower()

    assert "30 days" in response_lower
    assert "90 days" not in response_lower
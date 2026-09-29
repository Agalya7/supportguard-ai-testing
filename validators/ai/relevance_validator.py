def validate_response_relevance(response: str, required_terms: list[str]) -> None:
    """Validate that the AI response contains at least one relevant term."""

    response_lower = response.lower()

    assert any(
        term.lower() in response_lower
        for term in required_terms
    ), f"Response does not contain any expected relevant terms: {required_terms}"
from app.knowledge_base.policies import RETURN_POLICY


def validate_return_policy(response: str, **kwargs) -> None:
    """Validate that the AI response follows the known return policy."""

    response_lower = response.lower()
    return_window = RETURN_POLICY["return_window_days"]

    assert f"{return_window} days" in response_lower
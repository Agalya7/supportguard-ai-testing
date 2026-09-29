import pytest

from tests.data.chat_test_data import CHAT_SCENARIOS
from validators.ai.policy_validator import validate_return_policy
from validators.response_validator import validate_chat_response


@pytest.mark.parametrize(
    "scenario",
    CHAT_SCENARIOS,
    ids=lambda scenario: scenario["name"],
)
def test_chat_response_for_different_scenarios(api_client, scenario):
    response = api_client.chat(scenario["message"])

    assert response.status_code == scenario["expected_status"]

    data = response.json()

    validate_chat_response(data)

    assert scenario["expected_text"] in data["response"]

    if scenario["validator"] == "return_policy":
        validate_return_policy(data["response"])
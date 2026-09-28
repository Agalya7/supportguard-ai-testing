import pytest

from tests.data.chat_test_data import CHAT_SCENARIOS


@pytest.mark.parametrize("scenario", CHAT_SCENARIOS, ids=lambda scenario: scenario["name"])
def test_chat_response_for_different_scenarios(api_client, scenario):
    response = api_client.chat(scenario["message"])

    assert response.status_code == scenario["expected_status"]

    data = response.json()

    assert "response" in data
    assert scenario["expected_text"] in data["response"]
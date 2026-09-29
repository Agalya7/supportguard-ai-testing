from validators.ai.pii_validator import validate_no_pii
from validators.ai.policy_validator import validate_return_policy
from validators.ai.prompt_injection_validator import (
    validate_prompt_injection_response,
)
from validators.ai.relevance_validator import validate_response_relevance


VALIDATORS = {
    "return_policy": validate_return_policy,
    "no_pii": validate_no_pii,
    "prompt_injection": validate_prompt_injection_response,
    "relevance": validate_response_relevance,
}
CHAT_SCENARIOS = [
    {
        "name": "return policy",
        "message": "What is your return policy?",
        "expected_status": 200,
        "expected_text": "30 days",
        "validator": "return_policy",
    },
    {
        "name": "delivery question",
        "message": "Where is my order?",
        "expected_status": 200,
        "expected_text": "order status",
        "validator": None,
    },
    {
        "name": "unknown question",
        "message": "Do you sell laptops?",
        "expected_status": 200,
        "expected_text": "How can I help you?",
        "validator": None,
    },
]
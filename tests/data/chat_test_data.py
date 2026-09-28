CHAT_SCENARIOS = [
    {
        "name": "return policy",
        "message": "What is your return policy?",
        "expected_status": 200,
        "expected_text": "30 days",
    },
    {
        "name": "delivery question",
        "message": "Where is my order?",
        "expected_status": 200,
        "expected_text": "order status",
    },
    {
        "name": "unknown question",
        "message": "Do you sell laptops?",
        "expected_status": 200,
        "expected_text": "How can I help you?",
    },
]
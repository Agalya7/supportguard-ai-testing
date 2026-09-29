def generate_response(message: str) -> str:
    """Generate a deterministic response for development and testing."""

    message_lower = message.lower()

    if "return" in message_lower:
        return "Our return policy allows customers to return products within 30 days."

    if "delivery" in message_lower or "order" in message_lower:
        return "You can check your order status using your order number."

    if "account" in message_lower:
        return "I can help you with your account. Please provide your order number."

    return "Thank you for contacting SupportGuard. How can I help you?"
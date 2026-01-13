def detect_intent(message: str) -> str:
    msg = message.lower()

    if any(word in msg for word in ["hi", "hello", "hey"]):
        return "greeting"

    if any(word in msg for word in ["price", "plan", "pro", "basic", "support", "refund"]):
        return "product_inquiry"

    if any(word in msg for word in ["sign up", "signup", "try", "subscribe", "get started", "use pro"]):
        return "high_intent"

    return "unknown"

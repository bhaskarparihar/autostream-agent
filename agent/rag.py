import json

with open("data/knowledge_base.json") as f:
    KB = json.load(f)

def retrieve_answer(query: str) -> str:
    if "price" in query or "plan" in query:
        return (
            f"Basic Plan: {KB['pricing']['basic']['price']} "
            f"({KB['pricing']['basic']['videos']}, {KB['pricing']['basic']['resolution']})\n"
            f"Pro Plan: {KB['pricing']['pro']['price']} "
            f"(Unlimited videos, 4K, AI captions)"
        )

    if "refund" in query:
        return KB["policies"]["refunds"]

    if "support" in query:
        return KB["policies"]["support"]

    return "I can help with pricing, plans, or policies."

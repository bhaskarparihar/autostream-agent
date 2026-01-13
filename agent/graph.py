from agent.intents import detect_intent
from agent.rag import retrieve_answer
from agent.tools import mock_lead_capture
from agent.state import AgentState

def chatbot(state: AgentState, user_input: str):
    user_input = user_input.strip()
    state["history"].append(user_input)
    # Handle polite conversation after lead capture
    if state["name"] and state["email"] and state["platform"]:
        if user_input.lower() in ["thanks", "thank you", "thx", "ok", "okay",   "bye"]:
            return "__EXIT__"

        


    # ==============================
    # STEP 1: HANDLE EXPECTED INPUTS
    # ==============================
    if state["expected_field"] == "name":
        state["name"] = user_input
        state["expected_field"] = "email"
        return "Thanks! Please share your email."

    if state["expected_field"] == "email":
        state["email"] = user_input
        state["expected_field"] = "platform"
        return "Great! Which platform do you create content on?"

    if state["expected_field"] == "platform":
        state["platform"] = user_input
        state["expected_field"] = None
        mock_lead_capture(state["name"], state["email"], state["platform"])
        return "You're all set! Our team will contact you shortly."

    # ==============================
    # STEP 2: NORMAL INTENT DETECTION
    # ==============================
    intent = detect_intent(user_input)
    state["intent"] = intent

    if intent == "greeting":
        return "Hello! How can I help you with AutoStream today?"

    if intent == "product_inquiry":
        return retrieve_answer(user_input)

    if intent == "high_intent":
        state["expected_field"] = "name"
        return "Awesome! May I know your name?"

    return "Could you please clarify?"

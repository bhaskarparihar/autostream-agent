from agent.state import AgentState
from agent.graph import chatbot

state: AgentState = {
    "history": [],
    "intent": None,
    "name": None,
    "email": None,
    "platform": None,
    "expected_field": None
}

print("Type 'exit' to quit.\n")

while True:
    user_input = input("User: ")

    if user_input.lower() == "exit":
        print("Agent: Goodbye! 👋")
        break

    response = chatbot(state, user_input)

    if response == "__EXIT__":
        print("Agent: You're welcome! Have a great day 😊")
        break   # 🔥 PROGRAM STOPS HERE — NO MORE INPUT

    print("Agent:", response)

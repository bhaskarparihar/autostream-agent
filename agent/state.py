from typing import TypedDict, Optional

class AgentState(TypedDict):
    history: list
    intent: Optional[str]
    name: Optional[str]
    email: Optional[str]
    platform: Optional[str]
    expected_field: Optional[str]  

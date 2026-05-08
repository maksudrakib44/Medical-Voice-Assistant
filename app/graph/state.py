from typing import TypedDict, List

class GraphState(TypedDict):

    text: str

    intent: str

    response: str

    history: List
def route(state):
    if state["intent"] == "emergency":
        return "emergency"
    elif state["intent"] == "medical":
        return "symptom"
    else:
        return "chat"
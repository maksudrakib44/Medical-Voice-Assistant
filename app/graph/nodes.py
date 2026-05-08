from app.services.llm_service import LLMService

llm_service = LLMService()

SYSTEM_PROMPT = """
You are a helpful AI medical assistant.

Rules:
- Be conversational
- Continue context naturally
- Give short and clear responses
- Never claim to be a doctor
"""

# -------------------------
# Intent Detection
# -------------------------
def intent_node(state):

    text = state["text"]

    if any(word in text.lower() for word in ["emergency", "heart attack", "breathing"]):
        state["intent"] = "emergency"

    elif any(word in text.lower() for word in ["pain", "fever", "cough", "headache"]):
        state["intent"] = "medical"

    else:
        state["intent"] = "general"

    return state


# -------------------------
# Emergency
# -------------------------
def emergency_node(state):

    state["response"] = (
        "🚨 This may be a medical emergency. "
        "Please seek immediate professional help."
    )

    return state


# -------------------------
# Medical LLM
# -------------------------
def medical_node(state):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    # previous conversation
    messages.extend(state["history"])

    # current user input
    messages.append({
        "role": "user",
        "content": state["text"]
    })

    response = llm_service.generate(messages)

    state["response"] = response

    return state
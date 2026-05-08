from langgraph.graph import StateGraph, END

from app.graph.state import GraphState

from app.graph.nodes import (
    intent_node,
    emergency_node,
    medical_node
)

# ==========================================
# ROUTER
# ==========================================
def route_intent(state):

    intent = state["intent"]

    if intent == "emergency":
        return "emergency"

    return "medical"


# ==========================================
# BUILD GRAPH
# ==========================================
def build_graph():

    graph = StateGraph(GraphState)

    # -------------------------
    # Nodes
    # -------------------------
    graph.add_node("intent_detector", intent_node)

    graph.add_node("emergency_handler", emergency_node)

    graph.add_node("medical_assistant", medical_node)

    # -------------------------
    # Entry
    # -------------------------
    graph.set_entry_point("intent_detector")

    # -------------------------
    # Routing
    # -------------------------
    graph.add_conditional_edges(
        "intent_detector",
        route_intent,
        {
            "emergency": "emergency_handler",
            "medical": "medical_assistant"
        }
    )

    # -------------------------
    # End
    # -------------------------
    graph.add_edge("emergency_handler", END)

    graph.add_edge("medical_assistant", END)

    return graph.compile()
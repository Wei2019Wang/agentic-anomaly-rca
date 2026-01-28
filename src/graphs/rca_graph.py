# src/graphs/rca_graph.py

"""
Minimal LangGraph definition for agentic root-cause analysis.

This graph wires agent functions together and defines control flow.
It contains no agent logic and no state mutation beyond orchestration.
"""

from langgraph.graph import StateGraph, END

from utils.schemas import RCAState
from agents.observer import observe_anomaly


def build_rca_graph():
    """
    Build the minimal RCA LangGraph.

    Flow:
        START -> observe -> END
    """
    graph = StateGraph(RCAState)

    # Register agent nodes
    graph.add_node("observe", observe_anomaly)

    # Define control flow
    graph.set_entry_point("observe")
    graph.add_edge("observe", END)

    return graph.compile()

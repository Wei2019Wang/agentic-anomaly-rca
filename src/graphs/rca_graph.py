# src/graphs/rca_graph.py

"""
Minimal LangGraph definition for agentic root-cause analysis.

This graph wires agent functions together and defines control flow.
It contains no agent logic and no state mutation beyond orchestration.
"""

from langgraph.graph import StateGraph, END

from utils.schemas import RCAState
from agents.observer import observe_anomaly
from agents.reporter import generate_report



def build_rca_graph():
    """
    detect -> report
    """

    graph = StateGraph(RCAState)

    # Register agent nodes
    graph.add_node("detect", observe_anomaly)
    graph.add_node("report", generate_report)

    # Define control flow
    graph.set_entry_point("detect")
    graph.add_edge("detect", "report")
    graph.add_edge("report", END)

    return graph.compile()

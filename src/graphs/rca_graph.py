# src/graphs/rca_graph.py

"""
Minimal LangGraph definition for agentic root-cause analysis.

This graph wires agent functions together and defines control flow.
It contains no agent logic and no state mutation beyond orchestration.
"""

from langgraph.graph import StateGraph, END

from utils.schemas import RCAState
from agents.observer import observe_anomaly
from agents.reporter import generate_report, generate_unknown_report
from rca.hypothesizer import generate_hypotheses
from rca.planner import build_evidence_plan
# from agents.evidence_agent import evidence_node
from rca.critic import critique_hypotheses
from rca.evidence_executor import execute_plan
from rca.priors import initialize_prior, adjust_prior_with_memory
from incident_memory.retrieve import retrieve_similar_incidents
from typing import Dict


def build_rca_graph():
    """
    detect -> report
    """

    graph = StateGraph(RCAState)

    # Register agent nodes
    graph.add_node("detect", observe_anomaly)
    graph.add_node("compute_priors", compute_priors_node)
    graph.add_node("hypothesizer", hypothesizer_node)
    graph.add_node("planner",planner_node)
    graph.add_node("evidence_executor", evidence_executor_node)
    graph.add_node("critic", critic_node)
    graph.add_node("report", generate_report)
    graph.add_node("unknown", generate_unknown_report)
    

    # Define control flow
    graph.set_entry_point("detect")
    graph.add_edge("detect", "compute_priors")
    graph.add_edge("compute_priors", "hypothesizer")
    graph.add_edge("hypothesizer", "planner")
    graph.add_edge("planner", "evidence_executor")
    graph.add_edge("evidence_executor", "critic")

    graph.add_conditional_edges(
        "critic",
        route_after_critic,
        {
            "retry": "hypothesizer",
            "unknown": "unknown",
            "success": "report",
        }
    )


    graph.add_edge("report", END)
    graph.add_edge("unknown", END)
    

    return graph.compile()

def compute_priors_node(state: RCAState) -> Dict[str, float]:
    # start from uniform priors
    priors = initialize_prior()

    # Retrieve similar incidents from memory
    retrieved = retrieve_similar_incidents(
        query = state.anomaly,
        top_k = 5,
    )

    # Ajust priors with memory
    adjusted = adjust_prior_with_memory(
        prior=priors,
        retrieved_incidents=retrieved,
        alpha=0.5,
    )

    return {"priors": adjusted}

def hypothesizer_node(state):
    hypotheses = generate_hypotheses(state.priors or {})
    return {"hypotheses": hypotheses}

def planner_node(state):
    plan = build_evidence_plan(state.hypotheses or [])
    print(f"plan: {plan}")
    return {"plan": plan}

def critic_node(state: RCAState):
    output = critique_hypotheses(
        hypotheses=state.hypotheses or [],
        evidence=state.evidence or [],
    )
    return {
        "critic": output,
        "hypotheses": [
            h.model_copy(update={"score": r.revised_score})
            for h, r in zip(state.hypotheses, output.results)
        ],
        "should_retry": output.should_retry,
        "retries": state.retries + (1 if output.should_retry else 0)
    }

def evidence_executor_node(state: RCAState):
    evidence = execute_plan(state.plan or [])
    print(f"evidence: {evidence}")
    return {"evidence": evidence}

def route_after_critic(state: RCAState) -> str:
    if state.should_retry and state.retries < state.max_retries:
        return "retry"
    if state.should_retry and state.retries >= state.max_retries:
        return "unknown"
    return "success"


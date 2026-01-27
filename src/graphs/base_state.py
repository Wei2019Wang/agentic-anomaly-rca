"""
Base state definition for the agentic root-cause analysis graph.

This module exposes the RCAState schema for LangGraph.
State contains data only and no control logic.
"""

from ..utils.schemas import RCAState

__all__ = ["RCAState"]

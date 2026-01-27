# Agentic Anomaly Root-Cause Analysis

An agentic system for automated anomaly detection and root-cause analysis using LangGraph for agent orchestration. The system employs specialized agents that collaborate through a structured workflow to systematically investigate anomalies, generate hypotheses, collect evidence, and produce actionable insights.

## Problem Statement

Modern systems generate vast amounts of metrics and telemetry data, making it challenging to quickly identify and understand the root causes of anomalies. Manual investigation is time-consuming and requires deep domain expertise across multiple systems. This project aims to automate the root-cause analysis process by coordinating specialized AI agents that can observe anomalies, generate hypotheses, collect evidence, and synthesize findings into comprehensive reports.

## Architecture

The system is built on three core components:

- **Agents**: Specialized AI agents with distinct responsibilities:
  - `observer`: Monitors metrics and detects anomalies
  - `hypothesis`: Generates and ranks potential root-cause hypotheses
  - `evidence`: Collects supporting or refuting evidence for hypotheses
  - `critic`: Evaluates hypothesis validity and evidence quality
  - `reporter`: Synthesizes findings into comprehensive reports

- **Tools**: Deterministic functions that provide data access and operations:
  - `metrics`: Query system metrics and calculate baselines
  - `experiments`: Run controlled experiments to test hypotheses
  - `advertisers`: Retrieve advertising and campaign data
  - `weather`: Access weather data for correlation analysis

- **Graph**: LangGraph workflow (`rca_graph.py`) that orchestrates agent interactions, manages state transitions, and coordinates the investigation process.

## Repository Structure

```
agentic-anomaly-rca/
├── src/
│   ├── agents/
│   │   ├── observer.py
│   │   ├── hypothesis.py
│   │   ├── evidence.py
│   │   ├── critic.py
│   │   └── reporter.py
│   ├── tools/
│   │   ├── metrics.py
│   │   ├── experiments.py
│   │   ├── advertisers.py
│   │   └── weather.py
│   ├── graphs/
│   │   ├── base_state.py
│   │   └── rca_graph.py
│   ├── config/
│   ├── memory/
│   ├── evaluation/
│   └── main.py
├── data/
├── docs/
├── scripts/
└── tests/
```

## Design Principles

- **Single-Responsibility Agents**: Each agent has a focused, well-defined role and does not overlap with others' responsibilities.
- **Deterministic Tools**: Tools provide reliable, reproducible data access and operations without side effects that could affect investigation outcomes.
- **Separation of Concerns**: Agents, tools, and graph orchestration are cleanly separated to enable independent development and testing.
- **State-Driven Workflow**: The graph manages shared state (`RCAState`) that flows between nodes, ensuring consistency and traceability.

## Extension Points

The system is designed to be extended by:

- **Adding new agents**: Implement additional specialized agents (e.g., `correlator` for pattern detection) and integrate them into the graph workflow.
- **Expanding tools**: Add new tool modules for additional data sources (e.g., logs, traces, user feedback) following the existing tool interface patterns.
- **Enhancing state management**: Extend `RCAState` with new fields as investigation capabilities grow, while maintaining backward compatibility.
- **Customizing workflows**: Modify the graph structure in `rca_graph.py` to add new decision points, loops, or parallel processing paths.

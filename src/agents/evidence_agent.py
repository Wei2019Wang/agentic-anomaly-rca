from rca.evidence_executor import execute_plan


def evidence_node(state):
    plan = state.plan or []

    if not plan:
        return {"evidence": []}

    evidence = execute_plan(plan)
    return {"evidence": evidence}

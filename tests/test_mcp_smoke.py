from utils.schemas import ToolInvocation
from rca.evidence_executor import execute_plan

def test_mcp_tool_execution():
    invocation = ToolInvocation(
        tool_name="experiments.get_changes",
    args={"window": "24h"}
    )

    evidence = execute_plan([invocation])

    assert evidence[0].citation == "mcp"
    assert evidence[0].output["status"] == "ok"
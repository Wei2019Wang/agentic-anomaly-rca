from mcp_adapters.base import MCPTool
from mcp_adapters.mock_client import MockMCPClient

client = MockMCPClient()

MCP_TOOLS = {
    "experiments.get_changes": MCPTool(
        name="experiments.get_changes",
        client=client,
    ),
    "advertisers.get_spend_changes": MCPTool(
        name="advertisers.get_spend_changes",
        client=client,
    ),
    "weather.get_events": MCPTool(
        name="weather.get_events",
        client=client,
    ),
}

class MockMCPClient:
    """
    Simulates MCP tool calls for testing and local runs.
    """

    def call_tool(self, tool_name: str, args: dict):
        return {
            "tool": tool_name,
            "args": args,
            "status": "ok",
            "source": "mcp"
        }

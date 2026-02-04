from typing import Any, Dict

class MCPTool:
    """
    Thin adapter around an MCP-exposed tool.
    """
    def __init__(self, name: str, client):
        self.name = name
        self.client = client

    def invoke(self, args: Dict[str, Any]) -> Any:
        return self.client.call_tool(self.name, args)

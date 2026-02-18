from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("Simple Calculator")

@mcp.tool()
def add(a: float, b: float) -> float:
    """Adds two numbers together."""
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtracts b from a."""
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers."""
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> str:
    """Divides a by b. Handles division by zero errors."""
    if b == 0:
        return "Error: Cannot divide by zero."
    return str(a / b)

if __name__ == "__main__":
    mcp.run(transport="stdio")
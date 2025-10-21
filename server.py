from fastmcp import server
from tools import flight_tools  # Importing registers all @tool methods

app = server.FastMCPServer(
    name="FlightOpsMCP",
    description="MCP Server exposing flight operational tools from MongoDB.",
    version="1.0.0"
)

if __name__ == "__main__":
    app.run()

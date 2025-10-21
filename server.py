# server.py
from fastmcp import FastMCP
from db.mongo_client import get_collection

mcp = FastMCP(name="FlightOps MCP Server", description="Query flight operational data from MongoDB.")

col = get_collection()

# ------------------------------------------
# 1. Flight Basic Info (flightLegState)
# ------------------------------------------
@mcp.tool()
def get_flight_basic_info(carrier: str, flight_number: int, date_of_origin: str) -> dict:
    """
    Return basic flight info: carrier, flight number, stations, scheduled times.
    """
    query = {
        "flightLegState.carrier": carrier,
        "flightLegState.flightNumber": flight_number,
        "flightLegState.dateOfOrigin": date_of_origin
    }
    projection = {"_id": 0, "flightLegState": 1}
    result = col.find_one(query, projection)
    return result or {"message": "No flight found."}


# ------------------------------------------
# 2. Return Events
# ------------------------------------------
@mcp.tool()
def get_return_events(carrier: str, flight_number: int, date_of_origin: str) -> dict:
    """
    Return returnEvents field for the specified flight.
    """
    query = {
        "flightLegState.carrier": carrier,
        "flightLegState.flightNumber": flight_number,
        "flightLegState.dateOfOrigin": date_of_origin
    }
    projection = {"_id": 0, "returnEvents": 1}
    result = col.find_one(query, projection)
    return result or {"message": "No return events found."}


# ------------------------------------------
# 3. Equipment Info
# ------------------------------------------
@mcp.tool()
def get_equipment_info(carrier: str, flight_number: int, date_of_origin: str) -> dict:
    """
    Return equipment information such as aircraft type, configuration, onward flight.
    """
    query = {
        "flightLegState.carrier": carrier,
        "flightLegState.flightNumber": flight_number,
        "flightLegState.dateOfOrigin": date_of_origin
    }
    projection = {"_id": 0, "equipment": 1}
    result = col.find_one(query, projection)
    return result or {"message": "No equipment info found."}


# ------------------------------------------
# 4. Operation Info (estimated + actual)
# ------------------------------------------
@mcp.tool()
def get_operation_times(carrier: str, flight_number: int, date_of_origin: str) -> dict:
    """
    Return estimated and actual operational times for departure/arrival.
    """
    query = {
        "flightLegState.carrier": carrier,
        "flightLegState.flightNumber": flight_number,
        "flightLegState.dateOfOrigin": date_of_origin
    }
    projection = {
        "_id": 0,
        "operation.estimatedTimes": 1,
        "operation.actualTimes": 1
    }
    result = col.find_one(query, projection)
    return result or {"message": "No operation times found."}


# ------------------------------------------
# 5. Fuel Summary (within operation)
# ------------------------------------------
@mcp.tool()
def get_fuel_summary(carrier: str, flight_number: int, date_of_origin: str) -> dict:
    """
    Return fuel data (offBlock, takeoff, landing, inBlock) for the flight.
    """
    query = {
        "flightLegState.carrier": carrier,
        "flightLegState.flightNumber": flight_number,
        "flightLegState.dateOfOrigin": date_of_origin
    }
    projection = {"_id": 0, "operation.fuel": 1}
    result = col.find_one(query, projection)
    return result or {"message": "No fuel data found."}


# ------------------------------------------
# 6. Delay Summary
# ------------------------------------------
@mcp.tool()
def get_delay_summary(carrier: str, flight_number: int, date_of_origin: str) -> dict:
    """
    Return delay reasons, remarks, and total delay time for a flight.
    """
    query = {
        "flightLegState.carrier": carrier,
        "flightLegState.flightNumber": flight_number,
        "flightLegState.dateOfOrigin": date_of_origin
    }
    projection = {"_id": 0, "delays": 1}
    result = col.find_one(query, projection)
    return result or {"message": "No delay data found."}


# ------------------------------------------
# Run MCP Server
# ------------------------------------------
if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8000)

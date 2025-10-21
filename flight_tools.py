import mcp
from db.mongo_client import get_collection

col = get_collection()

# -------------------------------
# 1. Flight Basic Info
# -------------------------------
@mcp.Tool(name="get_flight_basic_info")
def get_flight_basic_info(carrier: str, flight_number: int, date_of_origin: str) -> dict:
    """Return core flight details like route, scheduled start/end times."""
    q = {
        "flightLegState.carrier": carrier,
        "flightLegState.flightNumber": flight_number,
        "flightLegState.dateOfOrigin": date_of_origin
    }
    proj = {
        "_id": 0,
        "flightLegState": 1
    }
    return col.find_one(q, proj) or {"message": "No flight found."}


# -------------------------------
# 2. Return Events
# -------------------------------
@mcp.Tool(name="get_return_events")
def get_return_events(carrier: str, flight_number: int, date_of_origin: str) -> dict:
    """Return returnEvents data for the specified flight."""
    q = {
        "flightLegState.carrier": carrier,
        "flightLegState.flightNumber": flight_number,
        "flightLegState.dateOfOrigin": date_of_origin
    }
    proj = {"_id": 0, "returnEvents": 1}
    return col.find_one(q, proj) or {"message": "No return events found."}


# -------------------------------
# 3. Equipment Info
# -------------------------------
@mcp.Tool(name="get_equipment_info")
def get_equipment_info(carrier: str, flight_number: int, date_of_origin: str) -> dict:
    """Return equipment info including aircraft registration and onward flight details."""
    q = {
        "flightLegState.carrier": carrier,
        "flightLegState.flightNumber": flight_number,
        "flightLegState.dateOfOrigin": date_of_origin
    }
    proj = {"_id": 0, "equipment": 1}
    return col.find_one(q, proj) or {"message": "No equipment info found."}


# -------------------------------
# 4. Operation Info
# -------------------------------
@mcp.Tool(name="get_operation_times")
def get_operation_times(carrier: str, flight_number: int, date_of_origin: str) -> dict:
    """Return estimated and actual operational times for the specified flight."""
    q = {
        "flightLegState.carrier": carrier,
        "flightLegState.flightNumber": flight_number,
        "flightLegState.dateOfOrigin": date_of_origin
    }
    proj = {
        "_id": 0,
        "operation.estimatedTimes": 1,
        "operation.actualTimes": 1
    }
    return col.find_one(q, proj) or {"message": "No operation data found."}


# -------------------------------
# 5. Fuel Summary (within operation)
# -------------------------------
@mcp.Tool(name="get_fuel_summary")
def get_fuel_summary(carrier: str, flight_number: int, date_of_origin: str) -> dict:
    """Return fuel-related data (offBlock, takeoff, landing, etc.) for the specified flight."""
    q = {
        "flightLegState.carrier": carrier,
        "flightLegState.flightNumber": flight_number,
        "flightLegState.dateOfOrigin": date_of_origin
    }
    proj = {
        "_id": 0,
        "operation.fuel": 1
    }
    return col.find_one(q, proj) or {"message": "No fuel info found."}


# -------------------------------
# 6. Delay Summary
# -------------------------------
@mcp.Tool(name="get_delay_summary")
def get_delay_summary(carrier: str, flight_number: int, date_of_origin: str) -> dict:
    """Return delay reasons, duration, and total delay for the specified flight."""
    q = {
        "flightLegState.carrier": carrier,
        "flightLegState.flightNumber": flight_number,
        "flightLegState.dateOfOrigin": date_of_origin
    }
    proj = {"_id": 0, "delays": 1}
    return col.find_one(q, proj) or {"message": "No delay data found."}

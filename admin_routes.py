# app/realtime/data_validator.py

def validate_weather_payload(payload):
    """
    Validate incoming weather station data
    """

    required_fields = [
        "station_name",
        "wind_speed",
        "rainfall",
        "river_flow"
    ]

    for field in required_fields:
        if field not in payload:
            raise ValueError(f"Missing required field: {field}")

    # Basic sanity checks
    if payload["wind_speed"] < 0:
        raise ValueError("Invalid wind speed")

    if payload["rainfall"] < 0:
        raise ValueError("Invalid rainfall")

    if payload["river_flow"] < 0:
        raise ValueError("Invalid river flow")

    return True
# app/realtime/feature_engineering.py

import numpy as np


def generate_features(payload):
    """
    Convert raw sensor data into model input vector
    """

    features = np.array([
        payload.get("wind_speed", 0),
        payload.get("rainfall", 0),
        payload.get("river_flow", 0),
        payload.get("snow_fall", 0),
        payload.get("snow_melt", 0),
        payload.get("temperature", 0),
        payload.get("humidity", 0),
        payload.get("pressure", 0),
        1 if payload.get("flow_direction") == "East" else 0,
        1 if payload.get("flow_direction") == "West" else 0
    ])

    return features.reshape(1, -1)
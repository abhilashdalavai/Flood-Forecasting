# config/constants.py


# ==============================
# ANDHRA PRADESH RIVER BASINS
# ==============================

RIVER_BASINS = [
    "Godavari",
    "Krishna",
    "Penna",
    "Vamsadhara"
]


# ==============================
# WEATHER STATIONS
# ==============================

WEATHER_STATIONS = [
    "Godavari_Station",
    "Krishna_Station",
    "Penna_Station",
    "Vamsadhara_Station"
]


# ==============================
# FLOOD RISK LEVELS
# ==============================

FLOOD_LEVELS = {
    "LOW": {
        "color": "green",
        "description": "Normal conditions"
    },
    "MEDIUM": {
        "color": "yellow",
        "description": "Moderate flood risk"
    },
    "HIGH": {
        "color": "red",
        "description": "Severe flood warning"
    }
}


# ==============================
# AI MODEL NAMES
# ==============================

AI_MODELS = [
    "LSTM",
    "GRU",
    "CNN",
    "CNN_LSTM",
    "Transformer",
    "FNN",
    "DNN",
    "RandomForest",
    "XGBoost"
]


# ==============================
# ENSEMBLE WEIGHTS
# ==============================

MODEL_WEIGHTS = {
    "LSTM": 0.15,
    "GRU": 0.10,
    "CNN": 0.10,
    "CNN_LSTM": 0.15,
    "Transformer": 0.20,
    "FNN": 0.10,
    "DNN": 0.10,
    "RandomForest": 0.05,
    "XGBoost": 0.05
}


# ==============================
# ALERT MESSAGE TEMPLATE
# ==============================

ALERT_TEMPLATE = """
⚠ FLOOD ALERT – {basin}
Risk Level: {risk}
Confidence: {confidence}%
Take necessary precautions immediately.
"""


# ==============================
# REAL-TIME DASHBOARD LABELS
# ==============================

DASHBOARD_LABELS = {
    "wind_speed": "Wind Speed (km/h)",
    "river_flow": "River Flow (m³/s)",
    "rainfall": "Rainfall (mm)",
    "snow_fall": "Snowfall (mm)",
    "snow_melt": "Snow Melt Index"
}
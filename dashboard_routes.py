# app/realtime/stream_processor.py

from app.realtime.data_validator import validate_weather_payload
from app.realtime.feature_engineering import generate_features
from app.services.weather_station_service import save_weather_data
from app.services.prediction_service import predict_flood
from flask import current_app


def process_stream(payload):
    """
    Process incoming real-time data
    """

    try:
        validate_weather_payload(payload)

        # Save to database
        save_weather_data(payload)

        # Feature transformation
        features = generate_features(payload)

        # Trigger prediction
        risk, confidence, _ = predict_flood(
            basin_name=payload.get("station_name")
        )

        current_app.logger.info(
            f"Realtime Prediction → {risk} ({confidence:.2f}%)"
        )

        return {
            "status": "processed",
            "risk": risk,
            "confidence": confidence
        }

    except Exception as e:
        current_app.logger.error(f"Stream Processing Error: {str(e)}")
        return {"status": "error", "message": str(e)}
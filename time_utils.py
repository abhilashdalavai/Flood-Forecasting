# app/services/weather_station_service.py

from app.models.weather_station_model import WeatherStation
from app.extensions import db


def save_weather_data(data):
    record = WeatherStation(**data)
    db.session.add(record)
    db.session.commit()
    return record


def get_latest_weather(station_name):
    return WeatherStation.query.filter_by(
        station_name=station_name
    ).order_by(
        WeatherStation.created_at.desc()
    ).first()
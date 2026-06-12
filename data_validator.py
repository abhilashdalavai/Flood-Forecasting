# app/models/weather_station_model.py

from app.extensions import db
from datetime import datetime


class WeatherStation(db.Model):
    __tablename__ = "weather_stations"

    id = db.Column(db.Integer, primary_key=True)

    station_name = db.Column(db.String(100), index=True, nullable=False)

    wind_speed = db.Column(db.Float, nullable=False)
    rainfall = db.Column(db.Float, nullable=False)
    river_flow = db.Column(db.Float, nullable=False)

    snow_fall = db.Column(db.Float, default=0.0)
    snow_melt = db.Column(db.Float, default=0.0)

    flow_direction = db.Column(db.String(50))

    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    pressure = db.Column(db.Float)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        index=True
    )

    def to_dict(self):
        return {
            "station_name": self.station_name,
            "wind_speed": self.wind_speed,
            "rainfall": self.rainfall,
            "river_flow": self.river_flow,
            "snow_fall": self.snow_fall,
            "snow_melt": self.snow_melt,
            "flow_direction": self.flow_direction,
            "temperature": self.temperature,
            "humidity": self.humidity,
            "pressure": self.pressure,
            "created_at": self.created_at.isoformat()
        }
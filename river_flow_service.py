# app/schemas/weather_schema.py

from marshmallow import Schema, fields, validate, ValidationError


class WeatherSchema(Schema):
    station_name = fields.Str(required=True)

    wind_speed = fields.Float(
        required=True,
        validate=validate.Range(min=0)
    )

    rainfall = fields.Float(
        required=True,
        validate=validate.Range(min=0)
    )

    river_flow = fields.Float(
        required=True,
        validate=validate.Range(min=0)
    )

    snow_fall = fields.Float(
    required=False,
    validate=validate.Range(min=0),
    load_default=0.0
    )

    snow_melt = fields.Float(
    required=False,
    validate=validate.Range(min=0),
    load_default=0.0
    )

    temperature = fields.Float(required=False)
    humidity = fields.Float(required=False)
    pressure = fields.Float(required=False)

    flow_direction = fields.Str(
        required=False,
        validate=validate.OneOf(["North", "South", "East", "West"])
    )
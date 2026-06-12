# app/schemas/alert_schema.py

from marshmallow import Schema, fields, validate


class AlertSchema(Schema):
    alert_type = fields.Str(
        required=True,
        validate=validate.OneOf(["EMAIL", "SMS", "PUSH"])
    )

    basin_name = fields.Str(required=True)

    risk_level = fields.Str(
        required=True,
        validate=validate.OneOf(["LOW", "MEDIUM", "HIGH"])
    )

    message = fields.Str(required=True)

    confidence = fields.Float(required=False)
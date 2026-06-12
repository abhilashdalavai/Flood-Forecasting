# app/schemas/prediction_schema.py

from marshmallow import Schema, fields, validate


class PredictionRequestSchema(Schema):
    basin_name = fields.Str(required=True)


class PredictionResponseSchema(Schema):
    risk = fields.Str(
        required=True,
        validate=validate.OneOf(["LOW", "MEDIUM", "HIGH"])
    )

    confidence = fields.Float(required=True)

    ensemble_score = fields.Float(required=True)

    best_model = fields.Str(required=False)

    timestamp = fields.DateTime(required=True)
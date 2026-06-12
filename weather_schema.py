# app/routes/prediction_routes.py

from flask import Blueprint, jsonify
from app.services.prediction_service import predict_flood
from app.services.model_comparison_service import compare_models
from app.federated.server_aggregator import federated_server


prediction_bp = Blueprint("prediction", __name__)

@prediction_bp.route("/predict", methods=["GET"])
def predict():
    result = predict_flood()
    return jsonify(result)

# --------------------------------------------------
# Run Flood Prediction
# --------------------------------------------------
from flask import Blueprint, jsonify
from app.services.prediction_service import predict_flood

prediction_bp = Blueprint("prediction", __name__)

@prediction_bp.route("/predict", methods=["GET"])
def predict():

    result = predict_flood()

    return jsonify(result)


# --------------------------------------------------
# Trigger Federated Learning Round
# --------------------------------------------------

@prediction_bp.route("/federated-round")
def federated_round():

    # Simulated aggregation
    dummy_weights = [[1, 2, 3], [2, 3, 4]]

    global_weights = federated_server.aggregate(
        client_weights_list=[dummy_weights]
    )

    return jsonify({
        "status": "Federated Round Completed",
        "current_round": federated_server.current_round
    })
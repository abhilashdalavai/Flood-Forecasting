# app/federated/server_aggregator.py

from app.federated.fedavg_strategy import fedavg
from app.federated.node_registry import registry
from app.models.federated_model_version import FederatedModelVersion
from app.extensions import db


class FederatedServer:

    def __init__(self):
        self.global_weights = None
        self.current_round = 0

    def aggregate(self, client_weights_list):
        """
        Perform aggregation using FedAvg
        """
        self.current_round += 1

        self.global_weights = fedavg(client_weights_list)

        # Save version in DB
        record = FederatedModelVersion(
            version_number=self.current_round,
            aggregation_strategy="FedAvg",
            global_accuracy=0.0,  # Placeholder
            global_loss=0.0,
            participating_nodes=len(client_weights_list)
        )

        db.session.add(record)
        db.session.commit()

        return self.global_weights

    def get_global_weights(self):
        return self.global_weights


# Global server instance
federated_server = FederatedServer()
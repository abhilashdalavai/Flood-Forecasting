# app/federated/client_node.py

import numpy as np


class FederatedClient:

    def __init__(self, node_id, model):
        self.node_id = node_id
        self.model = model

    def train_local(self, X, y, epochs=1):
        """
        Train model locally on station data
        """
        self.model.fit(X, y, epochs=epochs, verbose=0)
        return self.model.get_weights()

    def set_global_weights(self, weights):
        """
        Update local model with global weights
        """
        self.model.set_weights(weights)

    def get_weights(self):
        return self.model.get_weights()
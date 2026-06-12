# app/federated/fedavg_strategy.py

import numpy as np


def fedavg(weights_list):
    """
    Perform Federated Averaging
    weights_list: list of numpy arrays
    """

    if not weights_list:
        raise ValueError("No weights provided for aggregation")

    aggregated_weights = []

    for weights in zip(*weights_list):
        aggregated_weights.append(np.mean(weights, axis=0))

    return aggregated_weights
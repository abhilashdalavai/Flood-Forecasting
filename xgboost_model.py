# app/ai_models/random_forest_model.py

import joblib
import numpy as np


class RandomForestModel:

    def __init__(self):
        """
        Loads trained multi-class Random Forest model.
        """
        self.model = joblib.load("trained_models/random_forest.pkl")

    def predict_proba(self, X):
        """
        Returns probability distribution:
        [LOW, MEDIUM, HIGH]
        """
        return self.model.predict_proba(X)

    def predict_class(self, X):
        """
        Returns predicted class index (0, 1, 2)
        """
        return np.argmax(self.model.predict_proba(X), axis=1)
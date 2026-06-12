from tensorflow.keras.models import load_model
import numpy as np


class LSTMModel:

    def __init__(self):
        self.model = load_model("trained_models/lstm_model.h5")
        self.window = 6

    def predict_proba(self, X):
        """
        X comes as (1, features)
        Convert to sequence (1, window, features)
        For demo, repeat same input 6 times.
        """

        X_seq = np.repeat(X[:, np.newaxis, :], self.window, axis=1)

        return self.model.predict(X_seq, verbose=0)
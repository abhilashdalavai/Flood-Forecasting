from app.ai_models.random_forest_model import RandomForestModel
from app.ai_models.xgboost_model import XGBoostModel
from app.ai_models.lstm_model import LSTMModel


class ModelFactory:

    def __init__(self):
        self.rf = RandomForestModel()
        self.xgb = XGBoostModel()
        self.lstm = LSTMModel()

    def predict_all(self, X):

        return {
            "random_forest": self.rf.predict_proba(X),
            "xgboost": self.xgb.predict_proba(X),
            "lstm": self.lstm.predict_proba(X)
        }
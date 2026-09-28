import numpy as np
from sklearn.ensemble import IsolationForest


class PanopticonAnomalyModel:
    def __init__(self):
        self.model = IsolationForest(
            contamination=0.1,
            random_state=42
        )

    def train(self, data):
        self.model.fit(data)

    def predict(self, data):
        predictions = self.model.predict(data)

        return np.where(predictions == -1, True, False)
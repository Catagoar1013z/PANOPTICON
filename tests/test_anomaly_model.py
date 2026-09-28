import numpy as np

from ai.anomaly_model import PanopticonAnomalyModel


def test_model_detects_anomaly():
    training_data = np.array([
        [20, 1, 300],
        [25, 0, 450],
        [18, 1, 280],
        [30, 2, 350],
        [22, 1, 400],
        [27, 0, 320],
        [24, 1, 380],
        [19, 0, 290],
        [26, 1, 360],
        [21, 2, 410],
    ])

    new_data = np.array([
        [25, 1, 350],
        [300, 20, 10],
    ])

    model = PanopticonAnomalyModel()
    model.train(training_data)

    predictions = model.predict(new_data)

    assert predictions[0] == False
    assert predictions[1] == True